---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Counting
  - Data Validation
use-case:
  - Customer Feedback Sample Size
  - Inventory Count Verification
  - Survey Completion Rate
related:
  - COUNTA
  - COUNTBLANK
  - COUNTIF
  - COUNTIFS
  - ISNUMBER
  - ROWS
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/count-function
  - https://support.google.com/docs/answer/3093620
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Numbers
  - Numeric Count
tags:
  - counting
  - data-validation
  - excel
  - numeric
  - sheets
---

# COUNT

## Description

**COUNT** returns how many cells in a range or list of arguments hold a number. Dates count too, because both Excel and Google Sheets store dates as serial numbers. Text, empty cells, error values and logical values inside a range are not counted, so COUNT answers the question "how many numeric entries are there?"

COUNT is the right choice when the column should hold numbers, such as quantities, ratings or amounts. It is not the right choice when you need to know how many cells are filled with anything at all. Use COUNTA for that. A column of 100 customer names gives COUNT a result of 0 and COUNTA a result of 100. A column of 100 prices gives both functions 100.

The most common surprise comes from numbers that look correct but are stored as text, such as values pasted from a web page or an export. COUNT skips them, so the result is lower than expected. Check the alignment of the cells or convert the values before you count.

## Syntax

```excel
=COUNT(value1, [value2], ...)
```

<!-- Image 1: Numbers Versus Text in a Range. See Images/Statistical/COUNT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first item, cell reference or range in which to count numbers. |
| `value2, ...` | No | Additional items, cell references or ranges. Excel accepts up to 255 more arguments after `value1`. Google Sheets documents a limit of 30 and supports more in practice. |

### Return Value

A whole number: the count of numeric values. COUNT returns 0 when no numbers are found, and it does not return an error for ranges that contain text or error values.

## Examples

### Example 1: Count Numbers in a Mixed Column

Cells `A2:A8` hold 12, 7, the text Pending, 30, a blank cell, 18 and 41.

```excel
=COUNT(A2:A8)
```

**Result:** `5`

The five numbers are counted. The text and the blank cell are skipped.

### Example 2: Dates Count as Numbers

Cells `B2:B5` hold 3/1/2026, 3/15/2026, the text TBD and 4/2/2026.

```excel
=COUNT(B2:B5)
```

**Result:** `3`

Each date is a serial number and counts. The text TBD does not. Dates typed as text, such as "3 March 2026" entered as text, do not count.

### Example 3: Logical Values Passed Directly

```excel
=COUNT(1, 2, "three", 4, TRUE, 6)
```

**Result:** `5` in Excel

Excel counts numbers and logical values that you type directly into the argument list, so 1, 2, 4, TRUE and 6 are counted. The text "three" is not. The same rule does not apply to logical values inside a range. Google Sheets does not describe how logical values are counted, so test this case before you rely on it.

### Example 4: Numbers Stored as Text Inside a Range

Cells `C2:C4` hold the text '100 (typed with a leading apostrophe), 250 and 300.

```excel
=COUNT(C2:C4)
```

**Result:** `2`

The text 100 is not counted, because COUNT ignores text inside a range. Convert it with `VALUE` or re-enter it as a number.

### Example 5: Count Across Two Ranges

```excel
=COUNT(A2:A8, C2:C4)
```

**Result:** `7`

Five numbers come from `A2:A8` and two from `C2:C4`. Use commas to add as many ranges as the sheet needs.

### Example 6: Completion Rate

Cells `D2:D11` hold 10 rows, and 8 of them contain numbers.

```excel
=COUNT(D2:D11)/ROWS(D2:D11)
```

**Result:** `0.8` (display as 80 percent)

Dividing by the number of rows gives the share of rows that have a numeric entry.

<!-- Image 2: Completion Rate Calculation. See Images/Statistical/COUNT.md -->

## Story Problems

### Problem 1: Customer Feedback Ratings

A service team collects a rating from 1 to 5 for each customer. Some customers skip the rating, and one writes N/A.

| Customer | Rating | Comment |
| --- | --- | --- |
| Harbor Dental | 5 | Quick visit |
| Lin Studio | 4 | Friendly staff |
| Oak Print | (blank) | Waiting time was long |
| Vale Cafe | 3 | Good value |
| Rivera Shop | N/A | Not yet visited |
| Pine Clinic | 5 | Clear instructions |

**Task:** Count how many customers gave a numeric rating.

**Solution:**

```excel
=COUNT(B2:B7)
```

**Answer:** `4`. The ratings 5, 4, 3 and 5 are counted. The blank cell and N/A are not numbers, so they are skipped.

### Problem 2: Inventory Count Sheet

A warehouse team enters the quantity counted for each item in `B2:B7`. Item 2 was counted as zero. Item 3 was flagged for recount, and item 6 has not been counted yet.

| Item | Quantity Counted |
| --- | --- |
| Bracket | 24 |
| Gasket | 0 |
| Hinge | Recount |
| Latch | 9 |
| Panel | 15 |
| Washer | (blank) |

**Task:** Count the items that have a numeric quantity, including the item counted as zero.

**Solution:**

```excel
=COUNT(B2:B7)
```

**Answer:** `4`. Zero is a number, so the Gasket row counts. The Hinge text and the blank Washer row do not.

## Use Cases

### Customer Feedback Sample Size

**Scenario:** A product manager reviews average ratings only when enough customers have answered the rating question.

```excel
=IF(COUNT(Ratings) >= 30, AVERAGE(Ratings), "Sample Too Small")
```

**Why It Works:** COUNT gives the number of usable ratings, so the average appears only when the sample meets the minimum. Blank and text entries do not inflate the count.

### Inventory Count Verification

**Scenario:** A warehouse supervisor checks that every item received a numeric quantity before the count is closed.

```excel
=IF(COUNT(Quantities) = COUNTA(Items), "Count Complete", "Items Missing Quantities")
```

**Why It Works:** COUNTA counts the items and COUNT counts the numeric quantities. When the two match, every item has a number. A mismatch points to missing or text entries.

### Survey Completion Rate

**Scenario:** An analyst tracks how many respondents answered a numeric question in a survey export.

```excel
=COUNT(Responses) / ROWS(Responses)
```

**Why It Works:** The ratio shows the completion rate for the numeric question, and formatting the cell as a percentage makes it easy to read.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result is 0 | Every value is text, blank or an error. | Check the data types and convert text numbers. |
| Result is lower than expected | Numbers were imported as text. | Convert with `VALUE` or multiply by 1, and check for leading apostrophes. |
| Date not counted | The date was entered as text. | Re-enter it as a date so it is stored as a number. |
| Result is lower than expected | Hidden spaces or characters around numbers. | Use `TRIM` and `CLEAN` before counting. |
| Confusion with COUNTA | COUNT ignores text, while COUNTA counts it. | Use COUNTA when you need every filled cell. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Accepts `value1` plus up to 255 more arguments. Counts logical values and numeric text typed directly into the argument list, but not inside a range. |
| Google Sheets | Available | The help page documents a limit of 30 arguments but notes that Sheets accepts an arbitrary number. Text values are ignored. The help page does not describe logical values. |

## Tips and Best Practices

- Pair COUNT with COUNTA when you want to compare numeric entries with all entries in a column.
- Check a column's alignment after import. Numbers aligned to the left are often text.
- Use a bounded range such as `A2:A500` instead of a whole column when the sheet holds other content below the data.
- Use COUNTIF or COUNTIFS when you need to count numbers that meet a condition.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTA](COUNTA.md) | Counts every non-empty cell, including text. |
| [COUNTBLANK](COUNTBLANK.md) | Counts the empty cells in a range. |
| [COUNTIF](COUNTIF.md) | Counts cells that meet one condition. |
| [COUNTIFS](COUNTIFS.md) | Counts cells that meet several conditions at once. |
| [ISNUMBER](../Information/ISNUMBER.md) | Tests a single cell for a number, returning TRUE or FALSE. |
| [ROWS](../Lookup%20%26%20Reference/ROWS.md) | Returns the number of rows, the denominator for a completion rate. |

## Official Documentation

- [Microsoft Support: COUNT function](https://support.microsoft.com/en-us/excel/functions/count-function)
- [Google Docs Editors Help: COUNT](https://support.google.com/docs/answer/3093620)
