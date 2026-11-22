---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
use-case:
  - Accelerated Depreciation Schedule
  - Computer Equipment Write Down
  - Equipment Replacement Planning
related:
  - DB
  - SLN
  - SYD
  - VDB
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/ddb-function
  - https://support.google.com/docs/answer/3093163
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Double Declining Balance
  - Double Declining Balance Depreciation
tags:
  - depreciation
  - double-declining-balance
  - excel
  - sheets
---

# DDB

## Description

**DDB** returns the depreciation of an asset for one period using the double-declining balance method or another declining balance method that you choose. In the default method, the charge is twice the straight-line rate applied to the book value that remains at the start of the period. An asset that costs 10000 with a 5-year life therefore loses 40% of its remaining value each year, and the charge shrinks as the balance falls.

Use DDB when an asset loses value faster in its early years, such as computers, vehicles or technology equipment, and you want larger deductions up front. The `factor` argument changes the speed of depreciation. A factor of 1.5 gives a slower decline than the default of 2.

DDB never takes a charge that would push the book value below the salvage value. In the last years of an asset's life, the charge is limited to whatever amount remains above the salvage value. For a schedule that switches to straight-line depreciation at the point where that gives a larger charge, use [VDB](VDB.md). For a method with a fixed rate based on salvage value, use [DB](DB.md). Use [SLN](SLN.md) for equal charges and [SYD](SYD.md) for the sum-of-years-digits method.

Google Sheets provides the same function with the same arguments. Its help page gives no example outputs and does not describe error behavior, so check unusual inputs in Sheets before relying on them.

## Syntax

```excel
=DDB(cost, salvage, life, period, [factor])
```

<!-- Image 1: DDB Argument Layout. See Images/Financial/DDB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The initial cost of the asset. |
| `salvage` | Yes | The value at the end of depreciation. The Microsoft page says it can be 0. |
| `life` | Yes | The number of periods over which the asset is depreciated. |
| `period` | Yes | The period for which you want the depreciation. It must use the same units as `life`, and periods start at 1. |
| `factor` | No | The rate at which the balance declines. If omitted, it is 2, which gives the double-declining balance method. |

### Return Value

A number giving the depreciation charge for the requested period. Each period's charge is the smaller of two amounts: the remaining book value multiplied by `factor / life`, and the remaining book value minus the salvage value. The second limit stops depreciation once the asset reaches its salvage value.

## Examples

All examples use an asset costing 10000 with a salvage value of 1000 and a useful life of 5 years.

### Example 1: First Year Charge

```excel
=DDB(10000, 1000, 5, 1)
```

**Result:** `4000.00`

The first charge is 10000 times 2 divided by 5, which is 40% of the cost.

### Example 2: Second Year Charge

```excel
=DDB(10000, 1000, 5, 2)
```

**Result:** `2400.00`

The second charge applies the same 40% to the remaining 6000.

### Example 3: Fourth Year Charge

```excel
=DDB(10000, 1000, 5, 4)
```

**Result:** `864.00`

By year 4 the charge is still below the salvage limit, so the formula returns the full declining balance amount.

### Example 4: Charge Limited by Salvage Value

```excel
=DDB(10000, 1000, 5, 5)
```

**Result:** `296.00`

The declining balance charge would be 518.40, but only 296.00 remains above the salvage value of 1000. The formula returns the smaller amount so the book value stops at 1000.

### Example 5: Slower Declining Factor

```excel
=DDB(10000, 1000, 5, 1, 1.5)
```

**Result:** `3000.00`

With a factor of 1.5, the first charge is 10000 times 1.5 divided by 5, which is 30% of the cost instead of 40%.

<!-- Image 2: Declining Balance Schedule With Salvage Limit. See Images/Financial/DDB.md -->

## Story Problems

### Problem 1: Laptop Fleet Write Down

A company buys a laptop for 3000. The laptop has a salvage value of 300 and a 3-year life. The accountant needs the depreciation for year 2 using the default method.

| Input | Value |
| --- | --- |
| Cost | 3000 |
| Salvage value | 300 |
| Useful life in years | 3 |

**Task:** Put the cost in `B2`, the salvage value in `B3` and the life in `B4`, then find the charge for year 2.

**Solution:**

```excel
=DDB(B2, B3, B4, 2)
```

**Answer:** `666.67`. The first charge is 2000.00, leaving 1000.00. The formula would give 666.67 for year 2, which is below the limit of 700.00 that remains above salvage, so no cap applies.

### Problem 2: Production Machine Schedule

A factory buys a machine for 50000 with a salvage value of 5000 and a 6-year life. The plant manager wants the charge for year 3.

| Input | Value |
| --- | --- |
| Cost | 50000 |
| Salvage value | 5000 |
| Useful life in years | 6 |

**Task:** Find the depreciation for period 3 using the default factor.

**Solution:**

```excel
=DDB(B2, B3, B4, 3)
```

**Answer:** `7407.41`. The charges are 16666.67 in year 1 and 11111.11 in year 2, so the balance before year 3 is 22222.22, and one third of it is the year 3 charge.

## Use Cases

### Accelerated Depreciation Schedule

**Scenario:** A finance team builds a five-year schedule for a fleet of delivery vehicles and wants larger early deductions.

```excel
=DDB(Cost, Salvage, Life, Period)
```

**Why It Works:** Copy the formula down one row per year. The salvage limit is applied automatically, so the schedule never shows a book value below the residual value.

### Computer Equipment Write Down

**Scenario:** An IT department writes down servers that lose most of their value in the first two years.

```excel
=DDB(Cost, Salvage, 3, Period, 2)
```

**Why It Works:** Setting the factor explicitly documents the method in the formula. The default of 2 can be left out when it is the policy in use.

### Equipment Replacement Planning

**Scenario:** A manager compares the book value of a machine under declining balance and straight-line methods before choosing when to replace it.

```excel
=Cost - (DDB(Cost, Salvage, Life, 1) + DDB(Cost, Salvage, Life, 2))
```

**Why It Works:** Subtracting the first two charges from the cost gives the book value after two years, which can be compared with the machine's resale value.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A text value was entered for one of the arguments. | Enter numbers only. |
| Unexpected result or error | An argument is zero or negative, and the Microsoft page says all arguments must be positive. | Enter positive numbers for cost, life, period and factor. |
| Charge is smaller than expected | The period is greater than 1 and the earlier charges have used most of the cost above salvage. | Check the cumulative total against cost minus salvage. |
| Zero salvage gives an odd result | The Microsoft page says all arguments must be positive, and it also says salvage can be 0. | Test a zero salvage value in your version before depending on it. |
| Charge differs from a schedule built with VDB | DDB does not switch to straight-line depreciation. | Use [VDB](VDB.md) if the schedule should switch when straight-line gives a larger charge. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | `factor` defaults to 2. The Microsoft page does not name specific error values. |
| Google Sheets | Available | Same arguments and the same default factor of 2. The help page gives no example outputs and does not describe error behavior. |

## Tips and Best Practices

- Use the default factor of 2 unless a policy or tax rule specifies another value.
- Keep `life` and `period` in the same unit so that the period matches the schedule.
- Check that the sum of all charges equals cost minus salvage value before publishing a schedule.
- Compare DDB with [DB](DB.md) on the same asset to see how the two declining methods differ.
- Store the factor in its own cell when a schedule may be tested with several policies.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DB](DB.md) | Fixed-declining balance method that uses a rate based on salvage value. |
| [VDB](VDB.md) | Declining balance with an option to switch to straight-line depreciation. |
| [SLN](SLN.md) | Straight-line depreciation with equal charges each period. |
| [SYD](SYD.md) | Sum-of-years-digits method, with charges that fall by a fixed amount each year. |

## Official Documentation

- [Microsoft Support: DDB function](https://support.microsoft.com/en-us/excel/functions/ddb-function)
- [Google Docs Editors Help: DDB](https://support.google.com/docs/answer/3093163)
