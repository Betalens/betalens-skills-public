# Betalens Agent Skills

Reusable agent guidance for developing with Betalens and building factor research workflows.

## Skills

- `betalens-dev`: work with the public Betalens Python API and its research modules.
- `factor-forge`: turn a factor report or formula family into YAML-configured factor scripts.

These skills describe project conventions, not a frozen API specification. Check the target checkout's documentation, source, and tests when signatures or behavior may have changed. Data schemas and database access vary by installation; never assume a local database layout or embed credentials in a skill or generated artifact.

## Install

Copy the skill folder you need into your agent's skills directory. For Codex, a user-level location is `~/.codex/skills/<skill-name>/`. Each installed folder must contain its `SKILL.md` at the top level.

## Scope

The package contains portable instructions and small helper code only. It does not contain market data, database configuration, machine-specific paths, research outputs, or private workspace procedures.

Licensed under the MIT License; see [LICENSE](LICENSE).
