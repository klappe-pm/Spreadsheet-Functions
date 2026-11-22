---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
use-case:
  - Attendance Rates
  - Customer Satisfaction Scores
  - Mixed Entry Columns
related:
  - AVERAGE
  - AVERAGEIF
  - COUNT
  - COUNTA
  - SUM
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/averagea-function
  - https://support.google.com/docs/answer/3093617
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Average With Text
tags:
  - averages
  - excel
  - logical-values
  - mixed-data
  - sheets
---

# AVERAGEA

## Description

**AVERAGEA** returns the arithmetic mean of its arguments, but it counts every value differently from AVERAGE. Text inside a cell reference or range is treated as the number 0 and included in the count. The logical value TRUE is treated as 1 and FALSE as 0, also inside a reference. Numbers are counted normally. The result is the sum of all those values divided by the total number of values.

Use AVERAGEA when a column mixes numbers with text markers such as `Skipped` or `N/A`, and each marker should lower the average as a zero would. A common case is attendance, where TRUE means present and FALSE means absent, so the average gives the share of days attended.

AVERAGE is the better choice in most other cases. It ignores text and logical values inside references, so a text placeholder does not change the result. Choose AVERAGEA only when counting those values as zeros or ones is the intended business rule. Excel's help page says empty cells are ignored, but its own example only works if an empty cell counts as zero. Keep blank cells out of AVERAGEA ranges, or check the result against a manual calculation before relying on it.

## Syntax

```excel
=AVERAGEA(value1, [value2, ...])
```

<!-- Image 1: Text and Logical Values Counted. See Images/Statistical/AVERAGEA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, cell, or range to include. Between 1 and 255 arguments are accepted in Excel. |
| `value2, ...` | No | Additional values, cells, or ranges. Up to 255 arguments in total in Excel. |

### Return Value

A number: the sum of the counted values divided by the number of values. Text in a reference counts as 0, TRUE counts as 1 and FALSE counts as 0. A value typed directly into the argument list must be a number, a logical value or text that represents a number. Text that cannot be translated into a number causes an error, and error values in the arguments pass the error through.

## Examples

### Example 1: Text Counts as Zero

Values in `A2:A6`: 4, `Not available`, 6, TRUE, 3.

```excel
=AVERAGEA(A2:A6)
```

**Result:** `2.8`

The values count as 4, 0, 6, 1 and 3. Their total is 14, and dividing by five values gives 2.8.

### Example 2: The Same Range With AVERAGE

Values in `A2:A6`: 4, `Not available`, 6, TRUE, 3.

```excel
=AVERAGE(A2:A6)
```

**Result:** `4.33`

AVERAGE skips the text and the logical value inside the range. The three numbers 4, 6 and 3 total 13, and dividing by 3 gives 4.33. The gap between this result and Example 1 shows why the choice of function matters.

<!-- Image 2: AVERAGEA Versus AVERAGE on One Range. See Images/Statistical/AVERAGEA.md -->

### Example 3: Logical Values Typed Directly

```excel
=AVERAGEA(10, TRUE, 5)
```

**Result:** `5.33`

TRUE counts as 1 when it is typed into the argument list. The total is 16, and dividing by three values gives 5.33.

### Example 4: Ratings With a Text Marker

Ratings in `B2:B5`: 5, 4, `Not rated`, 3.

```excel
=AVERAGEA(B2:B5)
```

**Result:** `3`

The text marker counts as 0, so the four values total 12 and the average is 3. If the team wants unrated items left out, use AVERAGE, which returns 4 for the same range.

## Story Problems

### Problem 1: Satisfaction Scores With Skipped Surveys

A support team collects satisfaction ratings from five customers in `A1:B6`. The entry `Skipped` marks a customer who declined the survey, and the team wants that customer to lower the score.

| Customer | Rating |
| --- | --- |
| Customer 1 | 4 |
| Customer 2 | 5 |
| Customer 3 | Skipped |
| Customer 4 | 3 |
| Customer 5 | 2 |

**Task:** Calculate the average rating when the skipped survey counts as zero.

**Solution:**

```excel
=AVERAGEA(B2:B6)
```

**Answer:** `2.8`. The values total 14 (4 + 5 + 0 + 3 + 2), and dividing by 5 gives 2.8. AVERAGE would return 3.5 because it leaves the skipped survey out.

### Problem 2: Attendance Rate From Yes and No Flags

A training coordinator records whether each person attended each day, with TRUE for attended and FALSE for missed, in `A1:B6`.

| Day | Attended |
| --- | --- |
| Monday | TRUE |
| Tuesday | TRUE |
| Wednesday | FALSE |
| Thursday | TRUE |
| Friday | FALSE |

**Task:** Find the share of days attended.

**Solution:**

```excel
=AVERAGEA(B2:B6)
```

**Answer:** `0.6`, or 60 percent. TRUE counts as 1 three times and FALSE counts as 0 twice, so the total is 3 across five days. Format the cell as a percentage to display 60%.

## Use Cases

### Attendance Rates

**Scenario:** A training program tracks daily attendance as TRUE or FALSE for each participant and reports the attendance rate.

```excel
=AVERAGEA(C2:C31)
```

**Why It Works:** TRUE counts as 1 and FALSE as 0, so the average is the share of days attended. Use AVERAGE instead if the column also holds text notes that should be ignored.

### Customer Satisfaction Scores

**Scenario:** A service team wants unanswered surveys to lower the satisfaction score, so each unanswered entry is recorded as a text marker.

```excel
=AVERAGEA(RatingRange)
```

**Why It Works:** The text marker counts as zero, which matches the team's rule that a missing survey counts against the service. Document this rule next to the report so readers do not mistake the score for a rating average.

### Mixed Entry Columns

**Scenario:** A shared sheet collects numbers from several people, and some of them type `n/a` or `pending` instead of leaving a cell blank.

```excel
=AVERAGEA(D2:D100)
```

**Why It Works:** Each text entry counts as zero, so the result is conservative. Scan the column for text entries before reporting so the team can decide which ones should count.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A value typed directly into the formula is text that cannot be read as a number. | Put the value in a cell and reference it, or correct the entry. |
| Error value | An error in the referenced range passes through to the result. | Fix or wrap the source cells before averaging. |
| Unexpected result | Text entries lower the average because each counts as zero. | Use AVERAGE if text should be ignored, or clean the column first. |
| Unexpected result | TRUE and FALSE values in a range count as 1 and 0. | Confirm that the logical values mean what the average assumes. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Text in a reference counts as 0; TRUE counts as 1 and FALSE as 0. Up to 255 arguments. |
| Google Sheets | Available | Text in the value arguments is set to 0 and included. The help page does not describe logical values or blanks, so test them in your sheet. |

## Tips and Best Practices

- Use AVERAGEA only when text or logical values should count as zeros or ones.
- Scan the source column for unexpected text before averaging, since every text entry lowers the result.
- Name the rule in the report, for example "skipped surveys count as zero", so readers know how to read the number.
- Compare the result with AVERAGE on the same range to see how much the text entries affect it.
- Use COUNTA to count the entries that were filled in, including text markers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Skips text and logical values inside references, which gives a different result on mixed data. |
| [AVERAGEIF](AVERAGEIF.md) | Averages only the values that meet a condition, which is useful for excluding text markers. |
| [COUNT](COUNT.md) | Counts numeric cells, which helps confirm how many values were actually numbers. |
| [COUNTA](COUNTA.md) | Counts every nonblank cell, including text markers. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Totals the same values that AVERAGEA divides. |

## Official Documentation

- [Microsoft Support: AVERAGEA function](https://support.microsoft.com/en-us/excel/functions/averagea-function)
- [Google Docs Editors Help: AVERAGEA](https://support.google.com/docs/answer/3093617)
