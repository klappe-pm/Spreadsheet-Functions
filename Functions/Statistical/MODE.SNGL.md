---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Statistical Analysis
use-case:
  - Calls Without a Repeat
  - Most Frequent Visit Count
related:
  - AVERAGE
  - FREQUENCY
  - MEDIAN
  - MODE
  - MODE.MULT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mode-sngl-function
  - https://support.google.com/docs/answer/3094029
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Most Frequent Value
  - Single Most Common Value
tags:
  - averages
  - excel
  - mode
  - sheets
  - statistics
---

# MODE.SNGL

## Description

**MODE.SNGL** returns the value that appears most often in a set of numbers. It is the modern replacement for MODE when you want one most-common value, such as the most frequent order size or the most common number of visits per customer. Microsoft lists it alongside MODE.MULT in the statistical functions, and recommends it for new workbooks.

When two or more values tie for the highest count, MODE.SNGL returns just one of them. If you need every tied value, use MODE.MULT instead. When no number repeats, MODE.SNGL returns the `#N/A` error, so wrap the formula in IFERROR if a message is clearer. The function ignores text, logical values, and blank cells in ranges and references, and it includes zeros.

MODE.SNGL does not count text. To find the most common label, such as the most popular product name, count each label with COUNTIF and pick the largest count instead. Google Sheets documents only MODE on its help page, so use MODE when the workbook must calculate there.

## Syntax

```excel
=MODE.SNGL(number1, [number2], ...)
```

<!-- Image 1: One Most Common Value. See Images/Statistical/MODE.SNGL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or array to evaluate, for example `B2:B10`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. |

### Return Value

A single number: the value that appears most often. When several values tie, one of them is returned. It returns `#N/A` when no value repeats. It returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

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
=MODE.SNGL(B2:B10)
```

**Result:** `4`

The value 4 appears three times, more than any other value in the list.

### Example 2: No Repeated Value

```excel
=MODE.SNGL(1, 2, 3, 4)
```

**Result:** `#N/A`

Every number is different, so no mode exists.

### Example 3: Readable Message for No Repeat

```excel
=IFERROR(MODE.SNGL(C2:C6), "No repeat")
```

**Result:** `No repeat`

The quotes 3, 5, 8, 10, and 12 are all different, so IFERROR returns the message.

### Example 4: Count of the Most Common Value

```excel
=COUNTIF(B2:B10, MODE.SNGL(B2:B10))
```

**Result:** `3`

MODE.SNGL finds 4, and COUNTIF counts how many times 4 appears in the same range. This pairing confirms how strong the most common value is.

## Story Problems

### Problem 1: Most Frequent Visit Count

A clinic records how many visits each of six patients made in `A1:B7`.

| Patient | Visits |
| --- | --- |
| Ruiz | 3 |
| Chen | 5 |
| Okafor | 5 |
| Silva | 2 |
| Patel | 5 |
| Moore | 3 |

**Task:** Find the number of visits that occurs most often, so the clinic can plan appointment slots.

**Solution:**

```excel
=MODE.SNGL(B2:B7)
```

**Answer:** `5`. Five visits occurred three times, while 3 occurred twice.

### Problem 2: Calls Without a Repeat

A help desk logs the number of calls per day for four days in `A1:B5`: 4, 6, 9, and 2.

**Task:** Find the most common number of daily calls, and show a clear message if none repeats.

**Solution:**

```excel
=IFERROR(MODE.SNGL(B2:B5), "No repeat")
```

**Answer:** `No repeat`. Each daily total is different, so MODE.SNGL returns `#N/A`, and IFERROR shows the message instead.

<!-- Image 2: Story Problem Result. See Images/Statistical/MODE.SNGL.md -->

## Use Cases

### Most Frequent Visit Count

**Scenario:** A clinic manager wants the most common number of visits per patient in a quarter to set the standard booking pattern.

```excel
=MODE.SNGL(Visits[Count])
```

**Why It Works:** The formula returns one value, which suits a summary cell. When the answer matters for a tie, check the result with MODE.MULT.

### Calls Without a Repeat

**Scenario:** A support lead wants a daily staffing benchmark, and needs a clear note when the call volumes do not repeat.

```excel
=IFERROR(MODE.SNGL(CallLog[Calls]), "No typical day")
```

**Why It Works:** IFERROR converts the `#N/A` into a message that a dashboard can display without an error code.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No value repeats in the data. | Wrap the formula in IFERROR, or confirm the data has repeats with COUNTIF. |
| Unexpected result | Several values tie, and only one is returned. | Use MODE.MULT to list every tied value. |
| Unexpected result | Labels such as product names are not counted. | Count each label with COUNTIF, then find the largest count. |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Recommended for a single most-common value. Returns one value when ties exist. |
| Google Sheets | Not documented separately | The Google help page covers MODE only. Use MODE for the same single most-common value. |

## Tips and Best Practices

- Use MODE.SNGL for new work instead of the legacy MODE function.
- Check for ties with MODE.MULT when the answer must be unique.
- Wrap the formula in IFERROR when the result feeds a report or another formula.
- Keep the data numeric. Count text labels with COUNTIF and compare the counts.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MODE](MODE.md) | The legacy version, kept for compatibility. |
| [MODE.MULT](MODE.MULT.md) | Returns every value that ties for the most frequent count. |
| [FREQUENCY](FREQUENCY.md) | Builds a count of values in bins, which helps when a mode is hard to see. |
| [MEDIAN](MEDIAN.md) | Returns the middle value rather than the most frequent value. |
| [AVERAGE](AVERAGE.md) | Returns the arithmetic mean. |

## Official Documentation

- [Microsoft Support: MODE.SNGL function](https://support.microsoft.com/en-us/excel/functions/mode-sngl-function)
- [Google Docs Editors Help: MODE](https://support.google.com/docs/answer/3094029)
