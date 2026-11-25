"""Extract candidate factor paragraphs from PDF or DOCX research reports."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

KEYWORDS = (
    r"factor", r"alpha", r"formula", r"IC[A-Z]?\b", r"return", r"group",
    r"rolling", r"window", r"因子", r"公式", r"分组", r"多空", r"换手率",
)
KEYWORD_RE = re.compile("|".join(KEYWORDS), re.IGNORECASE)


def read_pdf(path: Path, pages: range | None) -> list[tuple[str, str]]:
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Install the PDF extra with: python -m pip install pypdf")

    reader = PdfReader(str(path))
    selected = pages if pages is not None else range(len(reader.pages))
    result = []
    for index in selected:
        if index >= len(reader.pages):
            break
        result.append((f"PDF page {index + 1}", reader.pages[index].extract_text() or ""))
    return result


def read_docx(path: Path) -> list[tuple[str, str]]:
    try:
        from docx import Document
    except ImportError:
        sys.exit("Install the DOCX extra with: python -m pip install python-docx")

    document = Document(str(path))
    return [
        (f"DOCX paragraph {index + 1}", paragraph.text)
        for index, paragraph in enumerate(document.paragraphs)
    ]


def parse_pages(value: str | None) -> range | None:
    if value is None:
        return None
    try:
        if "-" in value:
            first, last = (int(part) for part in value.split("-", maxsplit=1))
            if first < 1 or last < first:
                raise ValueError
            return range(first - 1, last)
        page = int(value)
        if page < 1:
            raise ValueError
        return range(page - 1, page)
    except ValueError:
        raise argparse.ArgumentTypeError("pages must be N or N-M, using 1-based page numbers")


def extract_candidates(
    pages: list[tuple[str, str]], limit: int
) -> list[tuple[str, str]]:
    candidates = []
    for location, page_text in pages:
        paragraphs = re.split(r"\n\s*\n|(?<=[。.!?])\n", page_text)
        for paragraph in paragraphs:
            text = paragraph.strip()
            if 10 <= len(text) <= 800 and KEYWORD_RE.search(text):
                candidates.append((location, text))
                if len(candidates) >= limit:
                    return candidates
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--pages", help="PDF page or range, for example 5 or 5-15")
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")

    suffix = args.path.suffix.lower()
    if suffix == ".pdf":
        try:
            selected_pages = parse_pages(args.pages)
        except argparse.ArgumentTypeError as error:
            parser.error(str(error))
        pages = read_pdf(args.path, selected_pages)
    elif suffix == ".docx":
        if args.pages is not None:
            parser.error("--pages applies only to PDF files")
        pages = read_docx(args.path)
    else:
        parser.error("only .pdf and .docx files are supported")

    candidates = extract_candidates(pages, args.limit)
    print(f"# Candidate paragraphs ({len(candidates)})")
    for location, text in candidates:
        print(f"\n--- {location} ---\n{text}")


if __name__ == "__main__":
    main()
