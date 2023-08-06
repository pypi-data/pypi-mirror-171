# Platts Python SDK

Consuming the Platts API in Python

## Installation

`pip install platts-sdk`

## Getting Started

```python
import platts_sdk as platts

t = platts.token.TokenClient("username", "password", "apikey")

m = platts.market_data.MarketData(t)

sym = ["PCAAS00", "PCAAT00"]
cur_df = m.get_current_assessments(["PCAAS00"])
print(cur_df)

mdc = "ET"
mdc_df = m.get_current_assessments_by_mdc(mdc)
print(mdc_df)
```
