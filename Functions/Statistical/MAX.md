---
domain: Spreadsheet Functions
category: Statistical
subcategory: Extremes
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Highest Order Value
  - Peak Daily Visitors
  - Peak Demand Planning
related:
  - AGGREGATE
  - LARGE
  - MAXA
  - MAXIFS
  - MIN
  - SMALL
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/max-function
  - https://support.google.com/docs/answer/3094013
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Largest Value
  - Maximum Value
tags:
  - aggregation
  - excel
  - extremes
  - maximum
  - sheets
---

# MAX

## Description

**MAX** returns the largest number in a set of values. You can give it a single range, several ranges, individual numbers, or any mix of them, and it returns the one value that is greater than all the others. It is the basic tool for finding a peak: the highest sale, the longest delay, or the largest reading in a log.

MAX reads only numbers from ranges and references. Text, logical values (TRUE and FALSE), and empty cells inside a range are skipped. Values typed straight into the argument list are treated differently: a logical value counts as 1 or 0, and a number stored as text, such as `"7"`, counts as a number. Text that cannot be read as a number typed into the list causes an error.

MAX returns 0 when no numbers are found, for example when the range is empty or holds only text. A 0 can look like a real answer, so check the data with COUNT when an empty range is possible. When you need the largest value that meets a condition, use MAXIFS. When you need TRUE and FALSE values or numbers stored as text in a range to count, use MAXA.

## Syntax

```excel
=MAX(number1, [number2], ...)
```

<!-- Image 1: Range and Typed Arguments. See Images/Statistical/MAX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or named range to evaluate, for example `42`, `B2`, or `B2:B8`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. |

### Return Value

A single number: the largest numeric value among all arguments. It returns 0 when no argument contains a number. It returns an error when any argument is an error value, or when text that cannot be read as a number is typed directly into the list.

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

### Example 1: Largest Value in a Range

```excel
=MAX(B2:B8)
```

**Result:** `915`

The largest store sales figure is the Thursday value. Every other cell in the range is compared against it.

### Example 2: Largest Value From Listed Numbers

```excel
=MAX(10, 25, 5, 42, 18)
```

**Result:** `42`

Numbers typed directly into the formula are compared the same way as numbers in a range. This is useful for quick checks.

### Example 3: Largest Value Across Two Ranges

```excel
=MAX(B2:B8, C2:C8)
```

**Result:** `1005`

Both ranges are scanned together. The largest online sale on Wednesday is higher than every store sale, so it becomes the result.

<!-- Image 2: Text, Blanks and Numbers in a Range. See Images/Statistical/MAX.md -->

### Example 4: Ignoring Text and Blank Cells

Assume `D2:D6` holds `Late`, `88`, a blank cell, `91`, and `77`.

```excel
=MAX(D2:D6)
```

**Result:** `91`

The word `Late` and the blank cell are skipped, so the comparison uses only 88, 91, and 77.

### Example 5: Spread Between the Highest and Lowest Value

```excel
=MAX(B2:B8) - MIN(B2:B8)
```

**Result:** `655`

The highest store sales figure (915) minus the lowest (260) gives the range of the data. A wide spread points to uneven results.

### Example 6: Empty Range Returns Zero

Assume `E2:E4` is blank.

```excel
=MAX(E2:E4)
```

**Result:** `0`

No numbers exist in the range, so MAX returns 0 instead of an error. Wrap the formula in an IF with COUNT when 0 would be misleading.

## Story Problems

### Problem 1: Peak Daily Visitors

A museum counts visitors each day of one week in `A1:B7`.

| Day | Visitors |
| --- | --- |
| Mon | 412 |
| Tue | 538 |
| Wed | 497 |
| Thu | 621 |
| Fri | 589 |
| Sat | 344 |

**Task:** Find the highest number of visitors recorded on any single day.

**Solution:**

```excel
=MAX(B2:B7)
```

**Answer:** `621`, the Thursday count. No other day is higher.

<!-- Image 3: Peak Visitor Result. See Images/Statistical/MAX.md -->

### Problem 2: Largest Order Across Two Stores

A chain records the order values from two stores in `A1:B5`. Store A is in column A and Store B is in column B, with the first order on row 2.

| Store A | Store B |
| --- | --- |
| 230 | 512 |
| 415 | 300 |
| 98 | 445 |
| 370 | 129 |

**Task:** Find the single largest order placed at either store.

**Solution:**

```excel
=MAX(A2:B5)
```

**Answer:** `512`, the largest value in Store B. Using one range that covers both columns avoids comparing each store separately.

## Use Cases

### Peak Demand Planning

**Scenario:** A call center wants to know the busiest hour in a month so it can schedule enough staff.

```excel
=MAX(CallLog[Calls])
```

**Why It Works:** The formula reads the whole column in a table, so new rows are included as the table grows. Compare the result with the staffing plan to find shortfalls.

### Highest Order Value

**Scenario:** A sales manager wants the largest single invoice in a quarter to check approval limits.

```excel
=MAX(Invoices[Amount])
```

**Why It Works:** The table reference keeps the formula correct when invoices are added. For a value that must match a region or product, use MAXIFS instead.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `0` | The range is empty or holds only text. | Check the range with COUNT, or wrap the result in IF(COUNT(range)>0, MAX(range), "No data"). |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the argument list. | Put the text in a cell and reference it, or remove it from the list. |
| Wrong result | A header row with a number in it is included in a full column reference. | Start the range below the header, for example `B2:B`, or use `B2:B100`. |
| Missed value | A number is stored as text inside the range, so MAX skips it. | Convert the cells to numbers with VALUE or Paste Special, then recalculate. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Up to 255 arguments. Logical values and text in references are ignored. Use MAXA to include them. |
| Google Sheets | Available | The help page documents 30 arguments. Blank cells and cells without numbers are ignored in ranges. Text typed directly as an argument returns `#VALUE!`. |

## Tips and Best Practices

- Use MAXIFS when the largest value must meet a condition, instead of nesting MAX inside an array formula.
- Pair MAX with INDEX and MATCH to return the name or date that belongs to the highest value.
- Keep the range off the header row so a label cannot be read as a number.
- Use a table reference such as `Sales[Amount]` so the formula grows with the data.
- Check for numbers stored as text when MAX returns a smaller value than expected.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MIN](MIN.md) | Returns the smallest number in the same kind of range. |
| [LARGE](LARGE.md) | Returns the nth largest value, for a top three or top five list. |
| [MAXIFS](MAXIFS.md) | Returns the largest value that meets one or more conditions. |
| [MAXA](MAXA.md) | Also counts TRUE and FALSE values and numbers stored as text in references. |
| [SMALL](SMALL.md) | Returns the nth smallest value. |
| [AGGREGATE](../Math%20%26%20Trig/AGGREGATE.md) | Finds the maximum while ignoring errors or hidden rows. |

## Official Documentation

- [Microsoft Support: MAX function](https://support.microsoft.com/en-us/excel/functions/max-function)
- [Google Docs Editors Help: MAX](https://support.google.com/docs/answer/3094013)
