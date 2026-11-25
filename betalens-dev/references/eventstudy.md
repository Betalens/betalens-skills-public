# Event Studies

Use the event-study API in the target checkout and verify how it aligns event dates with trading sessions. A basic shape is:

```python
from betalens.datafeed import Datafeed
from betalens.eventstudy import EventStudy

study = EventStudy(Datafeed(table_name))
result = study.analyze(
    events,
    code=security_code,
    window_before=5,
    window_after=5,
    metric=price_metric,
)
```

Before interpreting results, confirm event timestamp, duplicate-event handling, trading calendar, price metric, and benchmark assumptions. Do not include private event datasets in examples or fixtures.
