---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Bottle Fill Variation
  - Full Season Score Spread
  - Machine Output Consistency
related:
  - AVERAGEA
  - STDEV.P
  - STDEV.S
  - STDEVA
  - STDEVP
  - VARPA
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/stdevpa-function
  - https://support.google.com/docs/answer/3094058
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Standard Deviation With Text
tags:
  - excel
  - population
  - sheets
  - spread
  - statistical
---

# STDEVPA

## Description

**STDEVPA** returns the standard deviation of a population, the spread of values around their average when the data is the complete group you care about. It differs from STDEVP in one important way: it does not skip text and logical values that appear in a range. Text in a range counts as `0`, and in Excel `TRUE` counts as `1` and `FALSE` counts as `0`. This makes STDEVPA useful when a blank-looking cell or a placeholder such as "n/a" should pull the average down and widen the spread on purpose.

Use STDEVPA when every value in a range belongs to the population and any text entry should be treated as a real zero. For a clean list of numbers, STDEVPA and STDEV.P return the same result. Use STDEV.P when text should be ignored, and use STDEV.S or STDEV when the data is a sample of a larger population.

Excel and Google Sheets both support it. STDEV.P covers most new work, and STDEVPA is the choice when a workbook depends on the text and logical handling described above.

## Syntax

```excel
=STDEVPA(value1, [value2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/STDEVPA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, range, array or reference that belongs to the population. |
| `value2` | No | Additional values, ranges or arrays. Excel accepts up to 255 arguments in total. |

### Return Value

A number that is zero or greater: the population standard deviation of the values supplied. Text in a range or reference counts as `0`. Excel returns an error when a value in the arguments is an error or when text typed directly into the argument list cannot convert to a number. Google Sheets returns `#DIV/0!` when fewer than two values are supplied.

## Examples

### Example 1: Standard Deviation of a Complete Set

Values in `A2:A6`: 4, 8, 6, 5 and 7.

```excel
=STDEVPA(A2:A6)
```

**Result:** `1.414214`

The average is 6. The squared distances from 6 add up to 10, and dividing by the five values gives 2. The square root of 2 is 1.414214.

### Example 2: A Text Entry Counts as Zero

Values in `A2:A7`: 4, 8, 6, "n/a", 5 and 7.

```excel
=STDEVPA(A2:A7)
```

**Result:** `2.581989`

The text entry is treated as `0`, so the average falls to 5 and the spread grows. The same range with STDEVP returns `1.414214` because STDEVP skips the text.

<!-- Image 2: Text Versus Number Handling. See Images/Statistical/STDEVPA.md -->

### Example 3: Values Typed Directly

```excel
=STDEVPA(4, 8, 6, 5, 7)
```

**Result:** `1.414214`

Values typed into the argument list are numbers, so they produce the same result as Example 1.

### Example 4: Coefficient of Variation

```excel
=STDEVPA(A2:A6)/AVERAGE(A2:A6)
```

**Result:** `0.235702`

Dividing the standard deviation by the average expresses the spread as a share of the typical value, which makes two data sets with different averages comparable.

## Story Problems

### Problem 1: Bottle Fill Volumes

A bottling line fills eight bottles in one run, and the run is the full population the plant wants to measure. Volumes in millilitres are in `A1:B9`.

| Bottle | Volume (ml) |
| --- | --- |
| 1 | 498 |
| 2 | 502 |
| 3 | 500 |
| 4 | 497 |
| 5 | 505 |
| 6 | 501 |
| 7 | 499 |
| 8 | 503 |

**Task:** Find the population standard deviation of the fill volumes.

**Solution:**

```excel
=STDEVPA(B2:B9)
```

**Answer:** `2.496873`. The average fill is 500.625 ml, and every bottle in the run is counted.

<!-- Image 3: Bottle Fill Worksheet. See Images/Statistical/STDEVPA.md -->

### Problem 2: Weekly Parts Output With a Closed Day

A machine shop records parts produced per day in `A1:B7`. Saturday shows the text "Closed" because the shop did not run that day.

| Day | Parts |
| --- | --- |
| Mon | 120 |
| Tue | 135 |
| Wed | 128 |
| Thu | 140 |
| Fri | 131 |
| Sat | Closed |

**Task:** Find the population standard deviation of daily output, counting Saturday as the placeholder text does in STDEVPA.

**Solution:**

```excel
=STDEVPA(B2:B7)
```

**Answer:** `49.132474`. The text counts as `0`, which is the spread the shop should see if it wants Saturday to pull the average down. For the five working days alone, STDEVP returns `6.734983`.

## Use Cases

### Bottle Fill Variation

**Scenario:** A plant measures every bottle in a production run and wants the spread of fill volumes for the run.

```excel
=STDEVPA(Batch[Volume])
```

**Why It Works:** Each bottle in the batch is part of the population, so the population formula is correct. Any text placeholder in the Volume column is treated as zero, so check the column for stray labels first.

### Full Season Score Spread

**Scenario:** A coach records the points scored in every game of a season, including a forfeited game entered as text.

```excel
=STDEVPA(Season[Points])
```

**Why It Works:** The season is the whole population of games. Using STDEVPA keeps the forfeit visible in the spread, while STDEV.P would hide it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Larger than expected spread | A text placeholder in the range counts as `0`. | Clean the range, or use STDEV.P if text should be ignored. |
| Unexpected average shift | A logical `TRUE` in a range counts as `1` in Excel. | Replace logical values with numbers or remove them from the range. |
| `#VALUE!` | Text typed directly into the arguments cannot convert to a number. | Put the value in a cell, or type a number. |
| `#DIV/0!` | Google Sheets received fewer than two values. | Supply at least two values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Counts text in a reference as `0` and `TRUE` as `1`, `FALSE` as `0`. Empty cells are ignored. |
| Google Sheets | Available | Counts text as `0`. The page does not document how logical values are treated. Accepts more arguments than the documented 30. |

## Tips and Best Practices

- Use STDEVPA only when text and logical placeholders should count, and say so in the sheet notes.
- Use STDEV.P for a population that contains clean numbers and no placeholders.
- Check a range with `=COUNTA(range)` against `=COUNT(range)` to find text entries before you trust the result.
- Compare STDEVPA and STDEV.P on the same range to see how much the text entries change the spread.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV.P](STDEV.P.md) | Population standard deviation that ignores text and logical values in references. |
| [STDEVP](STDEVP.md) | Older population standard deviation with the same text handling as STDEV.P. |
| [STDEV.S](STDEV.S.md) | Sample standard deviation for data that is a sample of a larger population. |
| [STDEVA](STDEVA.md) | Sample standard deviation that counts text and logical values, the sample version of STDEVPA. |
| [VARPA](VARPA.md) | Population variance that counts text and logical values, the squared form of this result. |
| [AVERAGEA](AVERAGEA.md) | Average that counts text and logical values, useful beside STDEVPA. |

## Official Documentation

- [Microsoft Support: STDEVPA function](https://support.microsoft.com/en-us/excel/functions/stdevpa-function)
- [Google Docs Editors Help: STDEVPA](https://support.google.com/docs/answer/3094058)
