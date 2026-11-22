---
domain: Spreadsheet Functions
category: Information
subcategory: Market Data
purpose:
  - Data Import
  - Investment Analysis
use-case:
  - Monthly Price Trend Reports
  - Share Volume Reviews
  - Stock Return Tracking
related:
  - AVERAGE
  - FILTER
  - GOOGLEFINANCE
  - MAX
  - MIN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/stockhistory-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Historical Stock Prices
  - Stock History
tags:
  - dynamic-array
  - excel
  - financial-data
  - market-data
  - stocks
---

# STOCKHISTORY

## Description

**STOCKHISTORY** loads historical prices and trading volume for a stock or other financial instrument into a worksheet. You give it a ticker, or a cell that holds a Stocks data type, plus a start date and an optional end date. You then choose the interval (daily, weekly or monthly), whether to include headers, and up to six columns to return: Date, Close, Open, High, Low and Volume.

The function returns an array. When it is the final result of a formula, the array spills into the cells below and to the right, and Excel sizes the range for you. Headers are part of the returned array when you request them. Use STOCKHISTORY when you want a table of prices that refreshes from market data, instead of typing prices by hand.

The function has several limits. It needs a Microsoft 365 subscription: Personal, Family, Business Standard or Business Premium. Some instruments that appear as Stocks data types have no historical data, and most popular index funds, including the S&P 500, are examples. Data generally updates only after a trading day completes. With weekly or monthly intervals, the first date returned can fall earlier than the start date you requested.

## Syntax

```excel
=STOCKHISTORY(stock, start_date, [end_date], [interval], [headers], [property0], [property1], [property2], [property3], [property4], [property5])
```

<!-- Image 1: Syntax Anatomy. See Images/Information/STOCKHISTORY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `stock` | Yes | A ticker in double quotes, such as `"XNAS:AMZN"`, or a cell that holds a Stocks data type. Add a four-character ISO market identifier code (MIC) and a colon to choose an exchange. The default is the instrument's usual exchange. |
| `start_date` | Yes | The earliest date to retrieve. Enter it as text in quotes, as a formula such as `TODAY()-30`, or as a cell reference. |
| `end_date` | No | The latest date to retrieve. Defaults to `start_date`. |
| `interval` | No | `0` for daily, `1` for weekly, `2` for monthly. Defaults to `0`. |
| `headers` | No | `0` for no headers, `1` for headers, `2` for the instrument identifier and headers. Defaults to `1`. |
| `property0` to `property5` | No | Columns to return, in the order given: `0` for Date, `1` for Close, `2` for Open, `3` for High, `4` for Low, `5` for Volume. Defaults to `0,1` (Date and Close). |

### Return Value

An array of prices and dates. Each row is one period, and each requested property is one column, in the order you list them. The result includes header labels when `headers` is 1 or 2. Dates are the first trading day of each daily or weekly period, or the first day of each month for monthly data. The function does not apply a number format, so cells left behind after the formula is deleted use the General format.

## Examples

These examples show the shape of each result. The values depend on live market data, so each example describes the result rather than a fixed number.

### Example 1: Daily Closing Prices for One Month

```excel
=STOCKHISTORY("XNAS:AMZN", "1/2/2024", "1/31/2024")
```

**Result:** A two-column spill with the headers Date and Close, followed by one row for each trading day in January 2024.

The defaults return Date and Close with headers. The quoted dates use the US format; use a date cell or DATE() in other locales.

### Example 2: Monthly Prices With Chosen Columns

```excel
=STOCKHISTORY("XNYS:KO", "1/1/2023", "12/31/2023", 2, 1, 0, 2, 3, 4, 1)
```

**Result:** A five-column spill with the headers Date, Open, High, Low and Close, and one row for each month of 2023.

The interval `2` requests monthly data, which returns far fewer rows than daily data. The property order `0, 2, 3, 4, 1` sets the column order.

<!-- Image 2: Spill Layout With Headers. See Images/Information/STOCKHISTORY.md -->

### Example 3: Lowest Daily Low in a Period

```excel
=MIN(STOCKHISTORY("XNAS:CSCO", "3/1/2024", "6/30/2024", 0, 0, 4))
```

**Result:** A single number: the lowest daily low between March 1 and June 30, 2024.

Setting `headers` to 0 keeps labels out of the array, so the summary function receives only prices.

### Example 4: Total Shares Traded

```excel
=SUM(STOCKHISTORY("XNAS:INTC", "1/1/2024", "3/31/2024", 0, 0, 5))
```

**Result:** A single number: the total number of shares traded between January 1 and March 31, 2024.

Property `5` returns Volume, so the sum is the shares traded over the period.

### Example 5: Driving the Request From Cells

```excel
=STOCKHISTORY(A2, B2, C2)
```

**Result:** A Date and Close spill for the instrument in A2, between the dates in B2 and C2.

Keeping the ticker and dates in cells lets one formula serve many instruments and periods. A2 can hold a Stocks data type.

### Example 6: A Rolling Thirty-Day Window

```excel
=STOCKHISTORY("XNAS:AMZN", TODAY()-30, TODAY()-1)
```

**Result:** A Date and Close spill covering the trading days in the last 30 days, ending with yesterday.

Ending with `TODAY()-1` avoids a gap for the current day, because data updates only after a trading day completes.

## Story Problems

### Problem 1: Monthly Price Range

An investment club pulled monthly closing prices with a monthly interval. The table below holds the Close values, with the header in row 1.

| Month | Close |
| --- | --- |
| Jan | 52.00 |
| Feb | 58.50 |
| Mar | 49.25 |
| Apr | 61.75 |
| May | 55.00 |
| Jun | 57.25 |

**Task:** Find the spread between the highest and lowest monthly close.

**Solution:**

```excel
=MAX(B2:B7)-MIN(B2:B7)
```

**Answer:** `12.50`. The highest close is 61.75 in April and the lowest is 49.25 in March, so 61.75 minus 49.25 is 12.50.

### Problem 2: Average Daily Volume

A trader pulled the Date and Volume properties for four trading days in early January 2024. The volumes are in column B, starting in row 2.

| Date | Volume |
| --- | --- |
| 1/2/2024 | 1,200,000 |
| 1/3/2024 | 950,000 |
| 1/4/2024 | 1,430,000 |
| 1/5/2024 | 880,000 |

**Task:** Find the average daily volume for the four days.

**Solution:**

```excel
=AVERAGE(B2:B5)
```

**Answer:** `1,115,000` shares per day, because 4,460,000 divided by 4 is 1,115,000.

## Use Cases

### Monthly Price Trend Reports

**Scenario:** A management report charts a stock's monthly closing price from the start of 2023 to today.

```excel
=STOCKHISTORY("XNAS:AMZN", "1/1/2023", TODAY(), 2, 1, 0, 1)
```

**Why It Works:** The monthly interval keeps the table short enough to chart, and the Date and Close columns feed the chart directly. The headers make the output readable on the report.

### Share Volume Reviews

**Scenario:** An analyst checks whether unusually heavy trading days coincide with news events in the first quarter.

```excel
=STOCKHISTORY("XNYS:KO", "1/1/2024", "3/31/2024", 0, 1, 0, 5)
```

**Why It Works:** Daily data with Date and Volume columns shows each day's activity. Sorting the spill by Volume puts the heaviest days at the top.

### Stock Return Tracking

**Scenario:** A portfolio report needs the average closing price for the first quarter, to compare with a later period.

```excel
=AVERAGE(STOCKHISTORY("XNAS:AMZN", "1/1/2024", "3/31/2024", 0, 0, 1))
```

**Why It Works:** Headers are off and only the Close column is requested, so AVERAGE receives only prices. The result is one number that can sit in a summary table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| No data returned | Some instruments, such as most index funds including the S&P 500, have no historical data. | Use a stock or fund that has history, and check the instrument's Stocks data type before building a report. |
| Today's trading is missing | Data updates only after a trading day completes. | Set the end date to the last completed trading day, such as `TODAY()-1`. |
| Earlier date than requested | With weekly or monthly intervals, the first point can fall before `start_date`. | Expect the earlier date, or request daily data and summarize it. |
| `#SPILL!` | Cells where the array would spill are not empty. | Clear the cells in the spill range. |
| Formula not recognized | The Excel version or subscription does not include STOCKHISTORY. | Confirm the subscription listed in Platform Differences. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Requires a Microsoft 365 Personal, Family, Business Standard or Business Premium subscription | Available in Excel for Microsoft 365, Excel for Microsoft 365 for Mac, Excel for the web and Excel for iPhone. |
| Google Sheets | Not available | GOOGLEFINANCE is the closest alternative. It fetches market data in Sheets and can return historical prices for a date range. |

## Tips and Best Practices

- Use the monthly interval for long periods, because it returns far fewer rows than daily data.
- Set `headers` to 0 when you pass the result to MIN, MAX, AVERAGE or SUM, so labels stay out of the calculation.
- Keep the ticker and dates in cells, so one formula can serve several instruments and periods.
- Check that an instrument has historical data before you build a report on it.
- Allow for the trading-day delay by ending the window at the last completed trading day.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](../Statistical/AVERAGE.md) | Averages a returned Close or Volume column. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Keeps only the rows of the spill that meet a condition, such as a volume threshold. |
| [GOOGLEFINANCE](../Google-specific/GOOGLEFINANCE.md) | Fetches market data in Google Sheets, where STOCKHISTORY is not available. |
| [MAX](../Statistical/MAX.md) | Finds the highest value in a returned column, such as the top High. |
| [MIN](../Statistical/MIN.md) | Finds the lowest value in a returned column, such as the lowest Low. |

## Official Documentation

- [Microsoft Support: STOCKHISTORY function](https://support.microsoft.com/en-us/excel/functions/stockhistory-function)
