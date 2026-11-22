---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Google Data Services
purpose:
  - Data Retrieval
  - Investment Analysis
use-case:
  - Historical Price Review
  - Portfolio Value Tracking
  - Watchlist Price Checks
related:
  - IFERROR
  - IMPORTDATA
  - IMPORTXML
  - INDEX
  - QUERY
  - SPARKLINE
level: 3
source:
  - https://support.google.com/docs/answer/3093281
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Google Finance
  - Stock Price Lookup
tags:
  - finance
  - market-data
  - sheets
  - stocks
---

# GOOGLEFINANCE

## Description

**GOOGLEFINANCE** returns current or historical market data for a security from Google Finance, such as its latest price, its market capitalization, or its daily closing prices over a date range. It needs no add-in or API key, so a sheet can show a live price for a listed company or fund without a separate data connection.

The function has two modes. Without dates, it returns a single real-time value, such as the price or the price-to-earnings ratio. Adding a start date makes the request historical, and then only the historical attributes are allowed. Historical results appear as an expanded array with column headers, even when the request covers a single day.

The data is not live to the second. Real-time price data is delayed by up to 20 minutes, and the `datadelay` attribute shows the delay for a security. The official page also notes that the data is for information only, not for trading or advice, and that professional use may need a third-party license. Historical data cannot be read through the Sheets API or Apps Script, and those requests return `#N/A`. Mutual fund attributes are not supported.

The ticker should include its exchange, such as `NASDAQ:GOOG`, because the function chooses an exchange only when you leave it out. GOOGLEFINANCE is available only in Google Sheets, and Excel offers different tools for market data, described in the platform section.

<!-- Image 1: GOOGLEFINANCE Ticker and Attribute Cells. See Images/Google-specific/GOOGLEFINANCE.md -->

## Syntax

```excel
=GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date|num_days], [interval])
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `ticker` | Yes | The security to look up, with its exchange, such as `"NASDAQ:GOOG"`. Use the exchange prefix so the correct listing is returned. |
| `attribute` | No | The data to return. It defaults to `"price"`. The attribute is required when a date is given. |
| `start_date` | No | The first day of a historical range. A start date alone returns that single day. |
| `end_date` or `num_days` | No | Either a last date for the range, or a number of days counted from `start_date`. |
| `interval` | No | `"DAILY"` or `"WEEKLY"`, or the number `1` for daily or `7` for weekly. Other numbers are not allowed. |

Parameters must be in quotation marks or be cell references to text, with two exceptions: a numeric `interval` and a numeric `num_days`.

### Attributes

Real-time attributes (used without dates): `price`, `priceopen`, `high`, `low`, `volume`, `marketcap`, `tradetime`, `datadelay`, `volumeavg`, `pe`, `eps`, `high52`, `low52`, `change`, `beta`, `changepct`, `closeyest`, `shares` and `currency`.

Historical attributes (used with dates): `open`, `close`, `high`, `low`, `volume` and `all`, which returns all of the above.

Currencies have no trading window, so `open`, `low`, `high` and `volume` do not return for a currency.

### Return Value

A single value for a real-time request, shown in one cell. For a historical request, an expanded array with column headers. An unrecognized ticker or an unavailable attribute returns `#N/A`.

## Examples

### Example 1: Latest Price for One Ticker

```excel
=GOOGLEFINANCE("NASDAQ:GOOG")
```

**Result:** The latest price as one number. The value changes during the trading day and can lag the market by up to 20 minutes.

Omitting the attribute returns the `price` attribute by default.

### Example 2: Market Capitalization

```excel
=GOOGLEFINANCE("NASDAQ:GOOG", "marketcap")
```

**Result:** One number for the company's market capitalization in its trading currency. It changes as the share price changes.

### Example 3: Ticker and Attribute From Cells

```excel
=GOOGLEFINANCE(A2, B2)
```

**Result:** The attribute named in B2 for the ticker named in A2. If B2 is blank, the price attribute is used instead.

Keeping tickers in cells lets one formula serve every row of a watchlist.

### Example 4: Daily Closing Prices for a Date Range

```excel
=GOOGLEFINANCE("NASDAQ:GOOG", "close", DATE(2024,1,2), DATE(2024,1,31), "DAILY")
```

**Result:** An expanded table with a header row and one row for each trading day in the range. The values are fixed historical closes, so the table does not change over time.

Exact closing prices should be read from the sheet after it calculates, because the official page does not list them.

<!-- Image 2: GOOGLEFINANCE Historical Table. See Images/Google-specific/GOOGLEFINANCE.md -->

### Example 5: Weekly Closing Prices for a Recent Period

```excel
=GOOGLEFINANCE("NASDAQ:GOOG", "close", TODAY()-30, 30, "WEEKLY")
```

**Result:** An expanded table of weekly closing prices for the 30 days before today, with a header row. The number of rows depends on the calendar and the trading days.

Weekly data is useful for trend charts over a longer span, because it has fewer points than daily data.

## Story Problems

Both problems below use pasted values rather than live prices, so each answer stays fixed. In a live sheet, the GOOGLEFINANCE formula would replace the pasted cells.

### Problem 1: Average Close Over Five Days

An analyst pasted five closing prices for a stock into `B2:B6`.

| Day | Close |
| --- | --- |
| Day 1 | 101.20 |
| Day 2 | 103.50 |
| Day 3 | 99.80 |
| Day 4 | 104.00 |
| Day 5 | 106.30 |

**Task:** Find the average closing price over the five days and place it in `D2`.

**Solution:**

```excel
=AVERAGE(B2:B6)
```

**Answer:** `102.96`, because the five closes total 514.80 and 514.80 divided by 5 is 102.96.

### Problem 2: Value of a Small Holding

A portfolio sheet pasted the share counts in `B2:B4` and the prices in `C2:C4`.

| Holding | Shares | Price |
| --- | --- | --- |
| Holding A | 40 | 52.10 |
| Holding B | 25 | 118.40 |
| Holding C | 60 | 9.75 |

**Task:** Find the total market value of the three holdings and place it in `D2`.

**Solution:**

```excel
=SUMPRODUCT(B2:B4, C2:C4)
```

**Answer:** `5629`, because 40 times 52.10 is 2084, 25 times 118.40 is 2960, and 60 times 9.75 is 585, and those three values total 5629. In a live sheet, C2:C4 would hold GOOGLEFINANCE formulas.

## Use Cases

### Historical Price Review

**Scenario:** An analyst wants a year of daily closing prices to build a trend chart for a board report.

```excel
=GOOGLEFINANCE("NASDAQ:GOOG", "close", DATE(2025,1,1), DATE(2025,12,31), "DAILY")
```

**Why It Works:** The date range is fixed, so the table stays the same from one open of the sheet to the next. Because historical results expand into several cells, leave the space below the formula empty.

### Portfolio Value Tracking

**Scenario:** An individual investor keeps a list of holdings and wants the current market value of each one.

```excel
=IFERROR(GOOGLEFINANCE(A2) * B2, "Check ticker")
```

**Why It Works:** The ticker is read from A2 and multiplied by the share count in B2. IFERROR shows a message instead of `#N/A` when a ticker is not recognized.

### Watchlist Price Checks

**Scenario:** A trader monitors a short list of stocks and wants the latest price and today's change in one row.

```excel
=GOOGLEFINANCE(A2, "price") & " / " & GOOGLEFINANCE(A2, "changepct")
```

**Why It Works:** Both values come from the same ticker in A2. The data is delayed by up to 20 minutes, so the sheet is useful for a quick overview, not for placing trades.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The ticker is not recognized, or the security is not covered. | Add the exchange prefix, such as `"NASDAQ:GOOG"`, and check the ticker on Google Finance. |
| `#N/A` | The attribute is not valid for the security, or it is a historical attribute used without dates. | Check the spelling, and use only attributes that match the request type. |
| `#N/A` | The formula was called through the Sheets API or Apps Script for historical data. | Run the formula in the sheet, or copy the values as a snapshot. |
| `#REF!` | The historical array needs more empty cells than the sheet has. | Clear the cells below and to the right of the formula. |
| `#VALUE!` | A date is stored as text, or `num_days` is not a valid integer. | Use DATE or a cell that holds a real date, and a whole number for `num_days`. |
| Old value | The data is delayed by up to 20 minutes. | Treat the result as delayed; use a trading platform for live prices. |
| Blank or zero volume | The market is closed, or there was no trading for that security. | Check whether the market is open before reading the value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as GOOGLEFINANCE. The closest alternatives are STOCKHISTORY for historical prices and the Stocks data type for current information. | Excel's tools use different syntax, and they do not support every attribute that GOOGLEFINANCE does. |
| Google Sheets | Available | Real-time and historical attributes, with prices delayed by up to 20 minutes. Historical data is not available through the Sheets API or Apps Script. |

## Tips and Best Practices

- Put each ticker in its own cell, and include the exchange prefix, so the lookup is reliable.
- Wrap the formula in IFERROR for dashboards, so one bad ticker does not break the layout.
- Store a copy of the values for reports that must not change, instead of leaving live formulas in place.
- Leave empty space below historical formulas, because the expanded table needs room.
- Read attributes such as `changepct` as they are returned, and check the format before dividing or multiplying them.
- Use INDEX to pick one column from a historical result when only the closing prices are needed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFERROR](../Logical/IFERROR.md) | Returns a fallback message when a ticker or attribute fails. |
| [IMPORTDATA](../Web/IMPORTDATA.md) | Imports CSV or TSV data from a URL, for sources that GOOGLEFINANCE does not cover. |
| [IMPORTXML](../Web/IMPORTXML.md) | Pulls values from a web page with XPath, for data outside Google Finance. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Extracts a single column or row from a historical result. |
| [QUERY](QUERY.md) | Filters or sorts a historical table, such as the days above a price. |
| [SPARKLINE](SPARKLINE.md) | Draws a small trend chart from historical prices inside one cell. |

## Official Documentation

- [Google Docs Editors Help: GOOGLEFINANCE](https://support.google.com/docs/answer/3093281)
