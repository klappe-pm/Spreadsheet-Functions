---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
  - Financial Modeling
use-case:
  - Front Loaded Asset Charges
  - Server Equipment Depreciation
  - Trailer Depreciation Schedule
related:
  - DB
  - DDB
  - SLN
  - VDB
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/syd-function
  - https://support.google.com/docs/answer/3093261
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Accelerated Depreciation
  - Sum of Years Digits
tags:
  - accelerated-depreciation
  - depreciation
  - excel
  - sheets
---

# SYD

## Description

**SYD** returns the sum-of-years' digits depreciation of an asset for a specified period. It is an accelerated method: it records larger depreciation charges in the early years of an asset's life and smaller charges later. This matches assets that lose the most value when they are new, such as computers and vehicles.

The method works from the asset's depreciable base, which is cost minus salvage value. Each period's share of that base equals the remaining life divided by the sum of all the years' digits. For a five-year life, the digits add up to 15, so the first year takes 5/15 of the base, the second year takes 4/15, and so on. The charges decline by the same amount each period.

Use SYD when you want faster depreciation than straight-line but a method that is simpler to explain than the declining balance methods. For an even charge each period, use SLN. For a fixed percentage of remaining book value, use DDB or DB. For a period that falls inside a longer life, or a partial period, use VDB.

The period argument must use the same units as the life argument. A five-year life with a period of 2 returns the depreciation for the second year.

## Syntax

```excel
=SYD(cost, salvage, life, per)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/SYD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The initial cost of the asset. |
| `salvage` | Yes | The value of the asset at the end of its depreciation, also called the salvage value. |
| `life` | Yes | The number of periods over which the asset is depreciated, also called its useful life. |
| `per` | Yes | The period to calculate. It must use the same units as `life`, and it is usually a whole number from 1 to the life. |

### Return Value

A number: the depreciation charge for the specified period. The official pages for this function list no specific error values.

## Examples

### Example 1: First Year Charge

```excel
=SYD(24000, 2000, 5, 1)
```

**Result:** `7,333.33`

The depreciable base is 22,000. The first year takes 5 of the 15 digits, so the charge is 22,000 times 5/15, which is 7,333.33.

### Example 2: Middle Year Charge

```excel
=SYD(24000, 2000, 5, 3)
```

**Result:** `4,400.00`

The third year takes 3 of the 15 digits, so 22,000 times 3/15 gives 4,400.00. The charge is lower than the first year, as the method intends.

### Example 3: Final Year Charge

```excel
=SYD(24000, 2000, 5, 5)
```

**Result:** `1,466.67`

The last year takes 1 of the 15 digits, so the charge is the smallest in the schedule. Over all five years the charges total 22,000, which is the depreciable base.

### Example 4: Two Years Combined

```excel
=SYD(24000, 2000, 5, 1)+SYD(24000, 2000, 5, 2)
```

**Result:** `13,200.00`

Adding the first two annual charges gives the total depreciation after two years, which is the amount to subtract from the cost to find the book value.

## Story Problems

### Problem 1: Server Charge in Year Two

A company buys a server for 24,000. It expects the server to be worth 2,000 after five years and uses sum-of-years' digits depreciation.

| Item | Value |
| --- | --- |
| Cost | 24,000 |
| Salvage value | 2,000 |
| Useful life | 5 years |
| Period | 2 |

**Task:** Find the depreciation expense for year two.

**Solution:**

```excel
=SYD(24000, 2000, 5, 2)
```

**Answer:** `5,866.67`. The second year takes 4 of the 15 digits, so 22,000 times 4/15 gives the charge.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/SYD.md -->

### Problem 2: Trailer Schedule Over Four Years

A landscaping firm buys a trailer for 9,600 with a salvage value of 600 and a four-year life. The bookkeeper wants the charge for the second year.

| Item | Value |
| --- | --- |
| Cost | 9,600 |
| Salvage value | 600 |
| Useful life | 4 years |
| Period | 2 |

**Task:** Find the depreciation charge for year two.

**Solution:**

```excel
=SYD(9600, 600, 4, 2)
```

**Answer:** `2,700.00`. The digits add up to 10, the second year takes 3 of them, and 9,000 times 3/10 gives the charge.

## Use Cases

### Server Equipment Depreciation

**Scenario:** An IT department records faster depreciation on hardware that loses value quickly in its first years.

```excel
=SYD(24000, 2000, 5, 1)
```

**Why It Works:** The first year's charge is the largest, which reflects the early loss in value. Copy the formula across the year columns to build the full schedule.

### Trailer Depreciation Schedule

**Scenario:** A small firm builds a four-year depreciation schedule for a trailer so that the monthly books match the annual charges.

```excel
=SYD(9600, 600, 4, 2)
```

**Why It Works:** Changing the period argument moves the formula through the schedule. Check that the schedule totals the depreciable base of 9,000 before using it.

### Front Loaded Asset Charges

**Scenario:** A manager compares the first-year charge under SYD with the straight-line charge to see how much earlier the expense is recognized.

```excel
=SYD(24000, 2000, 5, 1)-SLN(24000, 2000, 5)
```

**Why It Works:** The difference shows how much more SYD records in year one than straight-line does. The result, 2,933.33, is the extra first-year charge (7,333.33 under SYD against 4,400.00 under straight-line).

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, not a number. | Enter each argument as a number. |
| Result for the wrong year | The period was entered as a calendar year, such as 2026. | Enter the period number counted from the start of the asset's life. |
| Period units do not match | The life is in years but the period is in months. | Convert both arguments to the same unit. |
| Schedule totals less than the base | The period loop stops before the last period. | Sum every period from 1 to the life and compare the total with cost minus salvage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | The official page lists Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Arguments are named cost, salvage, life and per. |
| Google Sheets | Available | The fourth argument is named period. Life and period must be measured in the same units. |

## Tips and Best Practices

- Check a schedule by adding every period from 1 to the life. The total must equal cost minus salvage.
- Keep the period number in its own cell so a schedule can be built by copying one formula down a column.
- Use SLN to compare the total charge in the early years with a straight-line charge.
- Enter a period that is a whole number. Partial periods belong to VDB.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DB](DB.md) | Fixed-declining balance depreciation, which applies a constant rate to book value. |
| [DDB](DDB.md) | Double-declining balance depreciation, which applies a factor to book value each period. |
| [SLN](SLN.md) | Straight-line depreciation, which records the same charge every period. |
| [VDB](VDB.md) | Variable declining balance depreciation, which works across any period or partial period. |

## Official Documentation

- [Microsoft Support: SYD function](https://support.microsoft.com/en-us/excel/functions/syd-function)
- [Google Docs Editors Help: SYD](https://support.google.com/docs/answer/3093261)
