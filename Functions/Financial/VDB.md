---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
  - Financial Modeling
use-case:
  - Fleet Vehicle Write Down
  - Machinery Declining Balance
  - Partial Period Depreciation
related:
  - DB
  - DDB
  - SLN
  - SYD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/vdb-function
  - https://support.google.com/docs/answer/9199424
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Declining Balance Depreciation
  - Variable Declining Balance
tags:
  - declining-balance
  - depreciation
  - excel
  - sheets
---

# VDB

## Description

**VDB** returns the depreciation of an asset for a specified period or span of periods, using a declining balance method. Each period's charge is a fraction of the asset's remaining book value, so the charges are largest at the start and shrink over time. Unlike SLN or SYD, VDB can calculate a span that starts and ends at any point in the asset's life, including partial periods.

By default, VDB uses a factor of 2, which is the double-declining balance rate. The factor sets how fast the balance falls, and a smaller factor gives smaller early charges. By default VDB also switches to straight-line depreciation in the period where straight-line produces a larger charge than the declining balance method. That switch keeps the asset from depreciating too slowly near the end of its life. Set no_switch to TRUE to keep the declining balance method for the whole life.

The start and end arguments count periods from the beginning of the asset's life. A start of 0 and an end of 1 covers the first period. Start and end are measured in the same units as life, so a span of months needs a life in months.

Use VDB when you need a declining balance schedule over a span that is not a whole number of years, or when the schedule must switch to straight-line automatically. For a simpler whole-year schedule, DDB and SYD are often easier to read.

## Syntax

```excel
=VDB(cost, salvage, life, start_period, end_period, [factor], [no_switch])
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/VDB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The initial cost of the asset. Must be a positive number. |
| `salvage` | Yes | The value of the asset at the end of its depreciation. It can be 0. |
| `life` | Yes | The number of periods over which the asset is depreciated. Must be a positive number. |
| `start_period` | Yes | The point in the asset's life where the span begins. Counted from 0 at the start of the life, in the same units as life. |
| `end_period` | Yes | The point in the asset's life where the span ends, in the same units as life. |
| `factor` | No | The rate at which the balance declines. Defaults to 2, the double-declining balance method. |
| `no_switch` | No | `TRUE` keeps the declining balance method even when straight-line gives a larger charge. `FALSE` or omitted allows the switch to straight-line. |

### Return Value

A number: the depreciation for the span from `start_period` to `end_period`. The span can include partial periods. The official pages list no other error values, and all arguments except salvage and no_switch must be positive numbers.

## Examples

All examples use an asset with a cost of 1,800, a salvage value of 200 and a life of 8 years unless the example shows otherwise.

### Example 1: First Year Depreciation

```excel
=VDB(1800, 200, 8, 0, 1)
```

**Result:** `450.00`

The first year's charge is the cost times the factor of 2 divided by the life, which is 1,800 times 2/8. The schedule starts at 0 and ends at 1, so it covers only the first period.

### Example 2: Span From Year 2 to Year 4

```excel
=VDB(1800, 200, 8, 1, 4)
```

**Result:** `780.47`

The span starts after year 1 and ends after year 4, so it covers years 2, 3 and 4. The three charges are 337.50, 253.13 and 189.84, which total 780.47.

### Example 3: Declining Balance With the Switch

```excel
=VDB(1000, 0, 4, 1, 4)
```

**Result:** `500.00`

The charges are 500, 250, 125 and 125. In year 4 straight-line would give 125 and declining balance gives 62.50, so the switch applies and the last charge is 125. Years 2 to 4 total 500.

### Example 4: Declining Balance Without the Switch

```excel
=VDB(1000, 0, 4, 1, 4, 2, TRUE)
```

**Result:** `437.50`

With no_switch set to TRUE, the year 4 charge stays at 62.50 instead of switching to straight-line. The total for years 2 to 4 falls from 500 to 437.50.

## Story Problems

### Problem 1: Machinery Charges in the Middle Years

A workshop buys a lathe for 1,800. It expects the lathe to be worth 200 after eight years and uses the default declining balance method. The bookkeeper wants the total depreciation for years 2 to 4.

| Item | Value |
| --- | --- |
| Cost | 1,800 |
| Salvage value | 200 |
| Useful life | 8 years |
| Span | Year 2 to year 4 |

**Task:** Find the total depreciation for years 2, 3 and 4.

**Solution:**

```excel
=VDB(1800, 200, 8, 1, 4)
```

**Answer:** `780.47`. The charges are 337.50, 253.13 and 189.84, and they add up to 780.47.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/VDB.md -->

### Problem 2: Fleet Van With a Factor of 1.5

A courier company buys a van for 10,000 with a salvage value of 1,000 and a five-year life. It uses a factor of 1.5 instead of the default 2, and it wants the total depreciation for years 2 and 3.

| Item | Value |
| --- | --- |
| Cost | 10,000 |
| Salvage value | 1,000 |
| Useful life | 5 years |
| Factor | 1.5 |
| Span | Year 2 to year 3 |

**Task:** Find the depreciation for years 2 and 3 together.

**Solution:**

```excel
=VDB(10000, 1000, 5, 1, 3, 1.5)
```

**Answer:** `3,570.00`. Year 2 is 2,100.00 and year 3 is 1,470.00, which total 3,570.00.

## Use Cases

### Fleet Vehicle Write Down

**Scenario:** A logistics firm writes down its fleet using a declining balance schedule and wants the first year's charge for a new vehicle.

```excel
=VDB(10000, 1000, 5, 0, 1, 1.5)
```

**Why It Works:** The first-year charge is the largest in the schedule, which reflects a vehicle losing value quickly when new. The result, 3,000.00, reduces the book value that the next year's charge uses.

### Machinery Declining Balance

**Scenario:** A manufacturer depreciates a production line using the default schedule and checks that each year's charge is correct before closing the books.

```excel
=VDB(1800, 200, 8, 1, 4)
```

**Why It Works:** Because the function works from the remaining book value, a schedule built with it always reflects the asset's current balance. Check that the schedule stops at the salvage value.

### Partial Period Depreciation

**Scenario:** An asset is bought partway through a year, and the accountant needs the charge for a span that does not start on a whole-period boundary.

```excel
=VDB(1800, 200, 8, 0.5, 1.5)
```

**Why It Works:** The official page describes VDB as covering partial periods, so the span does not need to start or end on a whole period. Confirm the partial-period result against the company's policy, because partial-period conventions vary.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text rather than a number. | Enter each argument as a number. |
| Error or wrong result | cost, life or a period value is zero or negative. The official pages require positive values for these arguments. | Enter positive values for cost, life and the period arguments. |
| Charges too large late in the life | The switch to straight-line was disabled with no_switch TRUE. | Set no_switch to FALSE or omitted to allow the switch. |
| Span gives the wrong year | Start and end were entered as calendar years. | Enter the period count from the start of the asset's life. |
| Total differs from cost minus salvage | The span does not cover the whole life. | Sum the spans from 0 to life to confirm the schedule. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Arguments are named cost, salvage, life, start_period, end_period, factor and no_switch. The default factor is 2 and the default no_switch is FALSE. |
| Google Sheets | Available | The arguments carry the same names. The official page gives the default factor of 2 but does not state the default for no_switch. |

## Tips and Best Practices

- Use the default factor of 2 unless the asset's policy calls for a different declining rate.
- Keep the default switch to straight-line in place so the schedule reaches the salvage value in its final years.
- Build a full schedule from period 0 to the life and check that the charges total cost minus salvage.
- Keep start, end and life in the same units, such as months for a monthly schedule.
- Use DDB or SYD for whole-year schedules that need a simpler formula to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DB](DB.md) | Fixed-declining balance depreciation, which uses a rate computed from the asset's life. |
| [DDB](DDB.md) | Double-declining balance depreciation for one whole period at a time. |
| [SLN](SLN.md) | Straight-line depreciation, which records the same charge every period. |
| [SYD](SYD.md) | Sum-of-years digits depreciation, which records charges that fall by the same amount each period. |

## Official Documentation

- [Microsoft Support: VDB function](https://support.microsoft.com/en-us/excel/functions/vdb-function)
- [Google Docs Editors Help: VDB](https://support.google.com/docs/answer/9199424)
