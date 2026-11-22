---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Most Common Shoe Size
  - Repeat Check on Order Quantities
related:
  - AVERAGE
  - COUNTIF
  - MEDIAN
  - MODE.MULT
  - MODE.SNGL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mode-function
  - https://support.google.com/docs/answer/3094029
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Most Common Value
  - Most Frequent Value
tags:
  - compatibility
  - excel
  - mode
  - sheets
  - statistics
---

# MODE

## Description

**MODE** returns the value that occurs most often in a set of numbers. Count how many times each number appears, and MODE returns the one with the highest count. It is useful for finding the most common size, the most frequent error code, or the most popular quantity in an order log.

MODE is a legacy function. Microsoft lists it under compatibility and recommends MODE.SNGL for a single most-common value and MODE.MULT when several values tie. MODE still works in current Excel and keeps older workbooks calculating, but new work should use the newer functions. The modern replacement for MODE is MODE.SNGL, and MODE.MULT covers the case where more than one value is most common.

When no number repeats, MODE returns the `#N/A` error. Wrap the formula in IFERROR when a message is clearer than an error code. MODE ignores text, logical values, and blank cells in ranges and references, and it includes zeros. Google Sheets documents MODE for the same purpose, but its help page does not describe the result when no value repeats.

## Syntax

```excel
=MODE(number1, [number2], ...)
```

<!-- Image 1: Frequency Count of Values. See Images/Statistical/MODE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or array to evaluate, for example `B2:B10`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. |

### Return Value

A single number: the value that appears most often. It returns `#N/A` when no value repeats. It returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

All examples use the values in `B2:B10` and `C2:C6` below, unless the example says otherwise.

| Order | Quantity | Quote |
| --- | --- | --- |
| 1 | 4 | 3 |
| 2 | 7 | 5 |
| 3 | 4 | 8 |
| 4 | 9 | 10 |
| 5 | 7 | 12 |
| 6 | 4 | |
| 7 | 2 | |
| 8 | 9 | |
| 9 | 5 | |

### Example 1: Most Common Quantity

```excel
=MODE(B2:B10)
```

**Result:** `4`

The value 4 appears three times, which is more than any other value. Seven and nine each appear twice.

### Example 2: No Repeated Value

```excel
=MODE(1, 2, 3, 4)
```

**Result:** `#N/A`

Each number appears once, so no mode exists. The `#N/A` result is the function's way of saying so.

### Example 3: Handling No Repeat Gracefully

```excel
=IFERROR(MODE(C2:C6), "No repeat")
```

**Result:** `No repeat`

The quotes 3, 5, 8, 10, and 12 are all different. IFERROR replaces the `#N/A` with a readable message.

### Example 4: Modern Equivalent

```excel
=MODE.SNGL(B2:B10)
```

**Result:** `4`

MODE.SNGL returns the same result for this data. Use it in new workbooks, because it is the function Microsoft recommends for a single most-common value.

<!-- Image 2: Modern Replacement Versus Legacy Name. See Images/Statistical/MODE.md -->

## Story Problems

### Problem 1: Most Common Shoe Size

A store records the size of each pair sold in one morning in `A1:B9`.

| Sale | Size |
| --- | --- |
| 1 | 8 |
| 2 | 9 |
| 3 | 9 |
| 4 | 10 |
| 5 | 9 |
| 6 | 11 |
| 7 | 8 |
| 8 | 9 |

**Task:** Find the shoe size that sold most often, so the buyer knows what to reorder first.

**Solution:**

```excel
=MODE(B2:B9)
```

**Answer:** `9`. Size 9 sold four times, more than any other size.

### Problem 2: Repeat Check on Order Quantities

A warehouse checks whether any order quantity repeats in the day's log. The header is in `A1`, and the quantities 4, 7, 10, and 12 are in `A2:A5`.

**Task:** Determine whether one quantity is more common than the others, and show a clear message when none is.

**Solution:**

```excel
=IFERROR(MODE(A2:A5), "No repeat")
```

**Answer:** `No repeat`. Each quantity appears once, so MODE returns `#N/A`, which IFERROR replaces with the message.

## Use Cases

### Most Common Order Quantity

**Scenario:** A purchasing manager wants to know which pack size customers order most often so the warehouse can keep enough of it.

```excel
=MODE(Orders[PackSize])
```

**Why It Works:** MODE counts each pack size and returns the most frequent. In a workbook that must work in both current and older versions of Excel, this formula still calculates.

### Repeat Check on Error Codes

**Scenario:** A support team wants the most frequent numeric error code from a log, and a clear message when no code repeats.

```excel
=IFERROR(MODE(ErrorLog[Code]), "No repeats")
```

**Why It Works:** IFERROR turns the `#N/A` result into a readable message. Use MODE.SNGL or MODE.MULT for new work.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No value repeats in the data. | Wrap the formula in IFERROR, or confirm the data has repeats with COUNTIF. |
| Unexpected result | A number is stored as text, so it is not counted. | Convert the cells to numbers before calculating. |
| Unexpected result | Several values tie, and only one is returned. | Use MODE.MULT to see every value that ties. |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Listed as a compatibility function. Microsoft recommends MODE.SNGL and MODE.MULT. |
| Google Sheets | Available | The help page documents the same purpose. It does not describe the result when no value repeats. |

## Tips and Best Practices

- Use MODE.SNGL for new single-value work, and MODE.MULT when ties matter.
- Count the repeats with COUNTIF before relying on MODE, so you know whether a mode exists.
- Wrap MODE in IFERROR when the result feeds another formula or a report.
- Keep the data numeric. Text labels such as "Red" are not counted by MODE, so use a count of each label instead.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MODE.SNGL](MODE.SNGL.md) | The modern replacement for one most-common value. |
| [MODE.MULT](MODE.MULT.md) | Returns every value that ties for the most frequent count. |
| [MEDIAN](MEDIAN.md) | Returns the middle value, a different measure of a typical value. |
| [AVERAGE](AVERAGE.md) | Returns the arithmetic mean. |
| [COUNTIF](COUNTIF.md) | Counts how often each value appears, to check for repeats. |

## Official Documentation

- [Microsoft Support: MODE function](https://support.microsoft.com/en-us/excel/functions/mode-function)
- [Google Docs Editors Help: MODE](https://support.google.com/docs/answer/3094029)
