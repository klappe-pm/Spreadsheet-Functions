---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
use-case:
  - Equipment Depreciation Schedule
  - Mid-Year Asset Purchase
  - Vehicle Fixed Asset Register
related:
  - DDB
  - SLN
  - SYD
  - VDB
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/db-function
  - https://support.google.com/docs/answer/3093162
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fixed Declining Balance
  - Fixed Declining Balance Depreciation
tags:
  - depreciation
  - excel
  - fixed-declining-balance
  - sheets
---

# DB

## Description

**DB** returns the depreciation of an asset for one period using the fixed-declining balance method. Each year the asset loses a fixed percentage of its remaining book value, so the charge is largest in the first period and falls each year after that. The percentage is calculated from the cost, the salvage value and the useful life, and it is rounded to three decimal places before use.

Use DB when an asset loses value fastest at the start and the accounting policy or tax schedule calls for a fixed rate on the declining balance. DB also handles a partial first year. When an asset is bought partway through the year, the `month` argument prorates the first period, and the remaining months fall into one extra period at the end of the schedule.

DB is closely related to [DDB](DDB.md), which applies a factor of 2 by default and does not use a fixed percentage based on salvage value. Use [SLN](SLN.md) for straight-line depreciation with equal charges each period, and [SYD](SYD.md) for the sum-of-years-digits method.

Google Sheets provides DB with the same arguments and the same arithmetic declining balance method. Its help page does not document error behavior or example outputs, so test unusual inputs in Sheets before depending on them.

## Syntax

```excel
=DB(cost, salvage, life, period, [month])
```

<!-- Image 1: DB Argument Layout. See Images/Financial/DB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The initial cost of the asset. |
| `salvage` | Yes | The value of the asset at the end of its depreciation, also called the salvage value. Enter 0 when the asset has no residual value. |
| `life` | Yes | The number of periods over which the asset is depreciated, also called the useful life. |
| `period` | Yes | The period for which you want the depreciation. It must use the same units as `life`, and periods are counted from 1. |
| `month` | No | The number of months in the first year. If omitted, it is 12. Use a smaller value for an asset bought partway through the year. |

### Return Value

A number giving the depreciation charge for the requested period. The rate used in the calculation is `1 - (salvage / cost)^(1/life)`, rounded to three decimal places. In the first period the charge is `cost * rate * month / 12`. Each later full period is `(cost minus depreciation so far) * rate`. The final partial period, which occurs when `month` is less than 12, is `(cost minus depreciation so far) * rate * (12 minus month) / 12`.

## Examples

All examples use an asset costing 10000 with a salvage value of 1000 and a useful life of 5 years.

### Example 1: First Full Year

```excel
=DB(10000, 1000, 5, 1)
```

**Result:** `3690.00`

The rate is `1 - (1000 / 10000)^(1/5)`, which is 0.369 after rounding. The first year charge is 10000 times 0.369.

### Example 2: Second Year

```excel
=DB(10000, 1000, 5, 2)
```

**Result:** `2328.39`

The charge falls because it applies the same rate to the lower remaining balance of 6310.

### Example 3: Last Full Year

```excel
=DB(10000, 1000, 5, 5)
```

**Result:** `584.98`

By year 5 the charge is much smaller, and the book value approaches the salvage value.

### Example 4: Asset Bought in July

```excel
=DB(10000, 1000, 5, 1, 7)
```

**Result:** `2152.50`

With 7 months in the first year, the first charge is 10000 times 0.369 times 7 divided by 12. The remaining 5 months are charged in the period after the fifth full year.

<!-- Image 2: Partial First Year Schedule. See Images/Financial/DB.md -->

### Example 5: Second Year After a Partial First Year

```excel
=DB(10000, 1000, 5, 2, 7)
```

**Result:** `2895.73`

The second period applies the rate to the balance left after the prorated first year, which is 10000 minus 2152.50, times 0.369.

## Story Problems

### Problem 1: Printing Press Depreciation

A print shop buys a press for 24000. The manufacturer estimates a salvage value of 3000 after 5 years. The owner wants the depreciation for year 2.

| Input | Value |
| --- | --- |
| Cost | 24000 |
| Salvage value | 3000 |
| Useful life in years | 5 |

**Task:** Put the cost in `B2`, the salvage value in `B3` and the life in `B4`, then find the charge for year 2.

**Solution:**

```excel
=DB(B2, B3, B4, 2)
```

**Answer:** `5385.60`. The rate is 0.340 after rounding, so year 1 is 8160.00 and year 2 applies 34% to the remaining 15840.

### Problem 2: Machine Installed Mid-Year

A bakery installs an oven for 18000 in month 9 of its fiscal year. The oven has a salvage value of 2000 and a 4-year life. The bookkeeper needs the first-year charge.

| Input | Value |
| --- | --- |
| Cost | 18000 |
| Salvage value | 2000 |
| Useful life in years | 4 |
| Months in first year | 9 |

**Task:** Use the input cells in `B2` to `B5` and find the depreciation for period 1.

**Solution:**

```excel
=DB(B2, B3, B4, 1, B5)
```

**Answer:** `5710.50`. The rate is 0.423, and 9 of the 12 months fall in the first year, so the charge is 18000 times 0.423 times 9 divided by 12.

## Use Cases

### Equipment Depreciation Schedule

**Scenario:** A manufacturer builds a yearly depreciation table for its production line.

```excel
=DB(Cost, Salvage, Life, Period)
```

**Why It Works:** Put the period number in a column and copy the formula down. Each row uses the same named inputs, so one change to the cost updates the whole table.

### Mid-Year Asset Purchase

**Scenario:** A company records a delivery van bought in month 7 of its fiscal year.

```excel
=DB(Cost, Salvage, Life, 1, 6)
```

**Why It Works:** The month argument prorates the first charge. The schedule then continues for the full years that follow, and a final partial period picks up the rest.

### Vehicle Fixed Asset Register

**Scenario:** An accountant tracks depreciation for several vehicles, each with its own purchase date.

```excel
=DB(Cost, Salvage, Life, Year, MonthsInFirstYear)
```

**Why It Works:** Storing the months in service per asset in the register keeps the calculation consistent across the fleet.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A text value was entered for one of the arguments. | Enter numbers only and check for text that looks like a number. |
| Charge differs from a manual calculation | The rate is rounded to three decimal places before use. | Compute the rate with the same rounding, or accept the small difference. |
| Full cost written off in year 1 | The salvage value was entered as 0 or left blank, which makes the rate equal to 1. | Enter a real salvage value, or use another method if the asset has no residual value. |
| Schedule seems one period too long | A `month` value below 12 creates a partial final period after the life. | Expect the extra period when `month` is less than 12. |
| Wrong charge for a later period | `period` and `life` use different units. | Convert both to years or both to months. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | `month` defaults to 12 and the rate is rounded to three decimal places. The Microsoft page does not list error conditions. |
| Google Sheets | Available | Same argument order and the arithmetic declining balance method. The help page documents `month` as optional with a default of 12 but gives no example outputs. |

## Tips and Best Practices

- Enter 0 for salvage only when the asset has no residual value, because the rate depends on that input.
- Keep `life` and `period` in the same unit, such as years, to avoid incorrect charges.
- Use the `month` argument for assets bought partway through the first year rather than adjusting the result afterward.
- Compare DB with [DDB](DDB.md) on the same asset to see how the two methods differ in the early years.
- Document the rounding of the rate in the model so that auditors can reproduce the figures.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DDB](DDB.md) | Double-declining balance method with a default factor of 2. |
| [SLN](SLN.md) | Straight-line depreciation with equal charges each period. |
| [SYD](SYD.md) | Sum-of-years-digits depreciation, with charges that fall each period. |
| [VDB](VDB.md) | Variable declining balance, which can cover any part of a period. |

## Official Documentation

- [Microsoft Support: DB function](https://support.microsoft.com/en-us/excel/functions/db-function)
- [Google Docs Editors Help: DB](https://support.google.com/docs/answer/3093162)
