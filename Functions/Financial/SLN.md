---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
purpose:
  - Depreciation
  - Financial Modeling
use-case:
  - Delivery Van Depreciation
  - Equipment Book Value
  - Machine Cost Allocation
related:
  - DB
  - DDB
  - SYD
  - VDB
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sln-function
  - https://support.google.com/docs/answer/3093245
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Straight Line Depreciation
tags:
  - depreciation
  - excel
  - fixed-assets
  - sheets
---

# SLN

## Description

**SLN** returns the straight-line depreciation of an asset for one period. Straight-line depreciation spreads the cost of an asset evenly over its useful life. Each period records the same expense, so the asset's book value falls by the same amount every year until it reaches the salvage value.

The calculation subtracts the salvage value from the cost and divides the result by the number of periods in the useful life. A forty-two thousand dollar vehicle with a six thousand dollar salvage value and a six-year life depreciates by 6,000 each year.

Straight-line is the simplest depreciation method. Accelerated methods such as SYD, DDB and VDB record larger charges in early periods. Use SLN when the asset's usefulness is roughly even over time, and use an accelerated method when it loses value faster at first.

The function returns the depreciation for one period. To see the full schedule, copy the formula down the rows or use the period-based functions for accelerated methods.

## Syntax

```excel
=SLN(cost, salvage, life)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/SLN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `cost` | Yes | The initial cost of the asset, including the amount paid to bring it into service. |
| `salvage` | Yes | The value of the asset at the end of its depreciation, also called the salvage value. It can be 0. |
| `life` | Yes | The number of periods over which the asset is depreciated, also called its useful life. |

### Return Value

A number: the depreciation charge for one period. The charge equals (cost minus salvage) divided by life. The official pages for this function list no specific error values.

## Examples

### Example 1: Annual Depreciation of a Vehicle

```excel
=SLN(42000, 6000, 6)
```

**Result:** `6,000.00`

The vehicle cost 42,000 and is expected to be worth 6,000 after six years. The difference of 36,000 spread over six years gives a charge of 6,000 each year.

### Example 2: Machine With a Long Life

```excel
=SLN(18500, 1000, 8)
```

**Result:** `2,187.50`

The machine loses 17,500 of value over eight years, which is 2,187.50 each year. After eight charges, the book value equals the 1,000 salvage value.

### Example 3: No Salvage Value

```excel
=SLN(12000, 0, 4)
```

**Result:** `3,000.00`

When an asset is expected to have no value at the end of its life, the salvage argument is 0 and the full cost is spread across the life.

### Example 4: Monthly Charge From an Annual Figure

```excel
=SLN(42000, 6000, 6)/12
```

**Result:** `500.00`

Dividing the annual charge by 12 gives the monthly depreciation for a management report that tracks expenses by month. The annual life of 6 is still in years, so the division by 12 converts only the output.

## Story Problems

### Problem 1: Delivery Van Expense for the Year

A bakery buys a delivery van for 42,000. The bakery expects to sell it for 6,000 after six years and uses straight-line depreciation.

| Item | Value |
| --- | --- |
| Cost | 42,000 |
| Salvage value | 6,000 |
| Useful life | 6 years |

**Task:** Find the depreciation expense for one year.

**Solution:**

```excel
=SLN(42000, 6000, 6)
```

**Answer:** `6,000.00`. Each year the van loses 6,000 of value on the books.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/SLN.md -->

### Problem 2: Equipment Book Value After Three Years

A print shop buys a press for 18,500 with a salvage value of 1,000 and an eight-year life. The accountant wants the book value after three years.

| Item | Value |
| --- | --- |
| Cost | 18,500 |
| Salvage value | 1,000 |
| Useful life | 8 years |
| Years elapsed | 3 |

**Task:** Find the annual charge, then subtract three years of charges from the cost.

**Solution:**

```excel
=18500 - 3*SLN(18500, 1000, 8)
```

**Answer:** `11,937.50`. The annual charge is 2,187.50, so three charges total 6,562.50 and the remaining book value is 11,937.50.

## Use Cases

### Delivery Van Depreciation

**Scenario:** A small business records the annual depreciation expense for a delivery van it bought for 42,000.

```excel
=SLN(42000, 6000, 6)
```

**Why It Works:** The same charge appears every year, which makes the expense easy to forecast in a budget. Change the life argument if the business's policy uses a different useful life.

### Equipment Book Value

**Scenario:** An asset register needs the book value of each machine at year end.

```excel
=Cost - SLN(Cost, Salvage, Life) * YearsUsed
```

**Why It Works:** Subtracting the accumulated charges from the cost gives the book value, which should never fall below the salvage value. Check that YearsUsed does not exceed Life.

### Machine Cost Allocation

**Scenario:** A plant allocates the cost of a machine to production over its life so that each product bears a steady share of the expense.

```excel
=SLN(18500, 1000, 8)
```

**Why It Works:** A constant annual charge gives a stable overhead rate. Use the same formula each year, and divide by expected units to get a cost per unit.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, such as a currency symbol stored in a cell. | Enter each argument as a number. |
| Unexpectedly large charge | The life was entered in months but the schedule is annual. | Enter life in the same period unit as the schedule. |
| Charge continues after the asset is fully depreciated | The formula does not stop at the salvage value. | Use a schedule that stops when book value reaches the salvage value. |
| Charge differs from the expected figure | The salvage value was omitted or set to the cost. | Confirm the salvage value in the asset register. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Arguments are named cost, salvage and life. |
| Google Sheets | Available | Arguments are named cost, salvage and life, in the same order as Excel. |

## Tips and Best Practices

- Use the same period unit for life and for the schedule. Annual life gives an annual charge.
- Keep the salvage value in a separate cell so the register can update it without changing formulas.
- Compare SLN with SYD or DDB when the asset loses value faster in its early years.
- Stop depreciating when book value reaches the salvage value, even if the calendar life has not ended.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DB](../Financial/DB.md) | Fixed-declining balance depreciation, which applies a constant rate to the remaining book value. |
| [DDB](../Financial/DDB.md) | Double-declining balance depreciation, which records larger charges in early periods. |
| [SYD](SYD.md) | Sum-of-years digits depreciation, which records charges that fall by the same amount each period. |
| [VDB](VDB.md) | Variable declining balance depreciation for any period or partial period. |

## Official Documentation

- [Microsoft Support: SLN function](https://support.microsoft.com/en-us/excel/functions/sln-function)
- [Google Docs Editors Help: SLN](https://support.google.com/docs/answer/3093245)
