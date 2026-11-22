---
domain: Spreadsheet Functions
category: Statistical
subcategory: Extremes
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Earliest Order Date
  - Lowest Shipping Quote
  - Minimum Stock Check
related:
  - AGGREGATE
  - MAX
  - MINA
  - MINIFS
  - SMALL
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/min-function
  - https://support.google.com/docs/answer/3094017
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Minimum Value
  - Smallest Value
tags:
  - aggregation
  - excel
  - extremes
  - minimum
  - sheets
---

# MIN

## Description

**MIN** returns the smallest number in a set of values. You can give it a range, several ranges, individual numbers, or a mix of them, and it returns the one value that is lower than all the others. Use it to find the lowest price, the earliest date, the smallest stock count, or the floor of a dataset.

MIN reads only numbers from ranges and references. Text, logical values (TRUE and FALSE), and empty cells inside a range are skipped. Values typed straight into the argument list follow different rules: a logical value counts as 1 or 0, and a number stored as text, such as `"7"`, counts as a number. Text that cannot be read as a number typed into the list causes an error.

MIN returns 0 when no numbers are found. Because 0 can look like a real minimum, confirm that the range contains numbers with COUNT before you trust a 0. For the smallest value that meets a condition, use MINIFS. For the nth smallest value, use SMALL. When TRUE and FALSE values or numbers stored as text in a range must count, use MINA.

## Syntax

```excel
=MIN(number1, [number2], ...)
```

<!-- Image 1: Range and Typed Arguments. See Images/Statistical/MIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or named range to evaluate, for example `12`, `B2`, or `B2:B8`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. |

### Return Value

A single number: the smallest numeric value among all arguments. It returns 0 when no argument contains a number. It returns an error when any argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

All examples use the store sales in `B2:B8` and the online sales in `C2:C8` below, unless the example says otherwise.

| Day | Store Sales | Online Sales |
| --- | --- | --- |
| Mon | 420 | 300 |
| Tue | 615 | 880 |
| Wed | 380 | 1005 |
| Thu | 915 | 150 |
| Fri | 540 | 600 |
| Sat | 705 | 700 |
| Sun | 260 | 990 |

### Example 1: Smallest Value in a Range

```excel
=MIN(B2:B8)
```

**Result:** `260`

The lowest store sales figure is the Sunday value. Every other cell in the range is compared against it.

### Example 2: Smallest Value From Listed Numbers

```excel
=MIN(50, 12, 87, 3, 45)
```

**Result:** `3`

The numbers in the list are compared directly, and 3 is the smallest.

### Example 3: Smallest Value Across Two Ranges

```excel
=MIN(B2:B8, C2:C8)
```

**Result:** `150`

The lowest online sale, on Thursday, is lower than every store sale in the table, so it becomes the result.

### Example 4: Ignoring Text and Blank Cells

Assume `D2:D6` holds `Late`, `88`, a blank cell, `91`, and `77`.

```excel
=MIN(D2:D6)
```

**Result:** `77`

The word `Late` and the blank cell are skipped, so the comparison uses only 88, 91, and 77.

### Example 5: Earliest Date in a List

Assume `F2:F5` holds the dates 3/14/2026, 1/9/2026, 2/20/2026, and 2/2/2026, formatted as dates.

```excel
=MIN(F2:F5)
```

**Result:** `1/9/2026`

Excel and Google Sheets store dates as serial numbers, so the smallest date is the earliest one. Format the result cell as a date so it displays correctly.

### Example 6: Empty Range Returns Zero

Assume `G2:G4` is blank.

```excel
=MIN(G2:G4)
```

**Result:** `0`

No numbers exist in the range, so MIN returns 0. Guard the formula with COUNT when a zero would be mistaken for a real minimum.

## Story Problems

### Problem 1: Lowest Shipping Quote

A small business requests a shipping quote from four carriers and records them in `A1:B5`.

| Carrier | Quote |
| --- | --- |
| Ace | 14.50 |
| Bolt | 11.75 |
| Crest | 19.00 |
| Dash | 12.40 |

**Task:** Find the lowest quote so the business can book the cheapest carrier.

**Solution:**

```excel
=MIN(B2:B5)
```

**Answer:** `11.75`, the quote from Bolt. The lowest value is found without checking each carrier by hand.

<!-- Image 2: Lowest Value Result. See Images/Statistical/MIN.md -->

### Problem 2: Smallest Stock Count

A retailer counts units on hand at four warehouses in `A1:B5`.

| Warehouse | Units |
| --- | --- |
| North | 48 |
| South | 12 |
| East | 30 |
| West | 75 |

**Task:** Find the lowest stock count so the buyer knows which warehouse needs a reorder first.

**Solution:**

```excel
=MIN(B2:B5)
```

**Answer:** `12`, the count at the South warehouse. The South warehouse is the first to reorder.

## Use Cases

### Minimum Stock Check

**Scenario:** A warehouse manager wants to know whether any product has fallen below a safe level.

```excel
=IF(MIN(Inventory[OnHand])<ReorderLevel, "Reorder", "Stock OK")
```

**Why It Works:** MIN finds the lowest count across the table, and the IF test compares it with the reorder level. Use MINIFS to check one product line or location.

### Earliest Order Date

**Scenario:** A support team needs the date of the oldest open ticket to meet a response target.

```excel
=MIN(Tickets[OpenedOn])
```

**Why It Works:** Dates are stored as numbers, so MIN returns the earliest date. Format the cell as a date so the result reads as a calendar day.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `0` | The range is empty or holds only text. | Check the range with COUNT, or wrap the result in IF(COUNT(range)>0, MIN(range), "No data"). |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the argument list. | Put the text in a cell and reference it, or remove it from the list. |
| Wrong result | A number stored as text inside the range is skipped. | Convert the cells to numbers, then recalculate. |
| Wrong result | A full column reference includes a header that is a number, such as a year. | Start the range below the header, for example `B2:B`. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Up to 255 arguments. Logical values and text in references are ignored. Use MINA to include them. |
| Google Sheets | Available | The help page documents 30 arguments. Cells without numbers are ignored in ranges. Text typed directly as an argument returns `#VALUE!`. |

## Tips and Best Practices

- Use MINIFS when the smallest value must meet a condition, such as a category or a status.
- Pair MIN with INDEX and MATCH to return the supplier or date that belongs to the lowest value.
- Remove 0 from the range with a condition such as `">0"` in MINIFS when 0 means missing data.
- Use a table reference such as `Inventory[OnHand]` so the formula grows with the data.
- Check for numbers stored as text when MIN returns a larger value than expected.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MAX](MAX.md) | Returns the largest number in the same kind of range. |
| [SMALL](SMALL.md) | Returns the nth smallest value, for a bottom three or bottom five list. |
| [MINIFS](MINIFS.md) | Returns the smallest value that meets one or more conditions. |
| [MINA](MINA.md) | Also counts TRUE and FALSE values and numbers stored as text in references. |
| [AGGREGATE](../Math%20%26%20Trig/AGGREGATE.md) | Finds the minimum while ignoring errors or hidden rows. |

## Official Documentation

- [Microsoft Support: MIN function](https://support.microsoft.com/en-us/excel/functions/min-function)
- [Google Docs Editors Help: MIN](https://support.google.com/docs/answer/3094017)
