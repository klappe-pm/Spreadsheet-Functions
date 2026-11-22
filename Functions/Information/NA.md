---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
purpose:
  - Error Handling
use-case:
  - Chart Gaps for Missing Readings
  - Marking Unavailable Inputs
  - Sensor Gap Totals
related:
  - ERROR.TYPE
  - IFERROR
  - IFNA
  - ISERROR
  - ISNA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/na-function
  - https://support.google.com/docs/answer/3093359
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Missing Value Marker
  - Not Available Error
tags:
  - charts
  - error-handling
  - excel
  - missing-data
  - sheets
---

# NA

## Description

**NA** returns the error value `#N/A`, which means "value not available." Use it to mark a result as missing on purpose. Because an `#N/A` is an error, it stands out in a sheet, does not look like a real zero, and is skipped by charts that plot gaps for missing points.

The function takes no arguments, but the empty parentheses are required. Typing `=NA()` in a cell gives the same result as typing `#N/A` directly, and both Microsoft and Google describe NA as included for compatibility with other spreadsheet programs.

An `#N/A` spreads through a calculation. Any formula that refers to a cell holding `#N/A` also returns `#N/A`, so a single missing input can make a total unusable. Use ISNA or IFNA to detect and handle these values before they reach a summary.

## Syntax

```excel
=NA()
```

<!-- Image 1: Syntax Anatomy. See Images/Information/NA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| None | No | NA takes no arguments. The empty parentheses are still required. |

### Return Value

The error value `#N/A`. No other value is returned, and the result cannot be used as a number until an error check or IFERROR or IFNA replaces it.

## Examples

All examples use this sample data:

| Cell | Value |
| --- | --- |
| B2 | 45 |
| B3 | (blank) |
| B4 | 52 |
| B5 | 61 |

### Example 1: Returning the Marker

```excel
=NA()
```

**Result:** `#N/A`

The formula returns the error value directly.

### Example 2: Marking a Blank Input as Missing

```excel
=IF(B3="", NA(), B3)
```

**Result:** `#N/A`

B3 is blank, so the formula returns the marker instead of a 0. A blank cell would otherwise look like a real zero in a chart or average.

### Example 3: Keeping a Present Value

```excel
=IF(B2="", NA(), B2)
```

**Result:** `45`

B2 has a value, so the formula returns it unchanged. The same pattern works for any input that might be missing.

### Example 4: Testing for the Marker

Assume `D3` holds the formula from Example 2.

```excel
=ISNA(D3)
```

**Result:** `TRUE`

ISNA returns TRUE only for `#N/A`. Other errors, such as `#DIV/0!`, return FALSE.

### Example 5: Error Propagation

Assume `D3` holds the formula from Example 2.

```excel
=D3*2
```

**Result:** `#N/A`

The marker passes through the arithmetic, so any formula that depends on a missing input also shows `#N/A`.

### Example 6: One Missing Value Spoils an Average

Assume `D3` holds the formula from Example 2.

```excel
=AVERAGE(B2, D3, B4)
```

**Result:** `#N/A`

One `#N/A` argument makes the whole average an error. Replacing the marker with IFNA, as in the story problems below, keeps the calculation working.

<!-- Image 2: Error Spreading Through a Total. See Images/Information/NA.md -->

## Story Problems

### Problem 1: Hours With No Sensor Reading

A temperature logger records one reading per hour. Two hours produced no data. Column C converts each reading into a value that charts and totals can handle, with `#N/A` for the gaps.

| Hour | Reading | Column C |
| --- | --- | --- |
| 1 | 21 | 21 |
| 2 | 22 | 22 |
| 3 | (blank) | `#N/A` |
| 4 | 23 | 23 |
| 5 | 24 | 24 |
| 6 | 24 | 24 |
| 7 | (blank) | `#N/A` |
| 8 | 22 | 22 |

Column C holds `=IF(B2="", NA(), B2)` filled down to row 9.

**Task:** Count the hours with no reading, using the markers in column C.

**Solution:**

```excel
=SUMPRODUCT(ISNA(C2:C9)*1)
```

**Answer:** `2`. ISNA flags the two `#N/A` markers in hours 3 and 7, and multiplying by 1 turns each flag into a count.

### Problem 2: Average of the Months That Reported

A store reports monthly sales in thousands. April has no figure yet, so it holds `#N/A`. A plain AVERAGE would fail, so the reader wants the average of the four months that reported.

| Month | Sales |
| --- | --- |
| Jan | 40 |
| Feb | 52 |
| Mar | 48 |
| Apr | `#N/A` |
| May | 61 |

**Task:** Average the reported months in `B2:B6` without changing the April marker.

**Solution:**

```excel
=AVERAGE(IFNA(B2:B6, ""))
```

**Answer:** `50.25`. The formula turns April into an empty text value, which AVERAGE ignores, so the result is (40 + 52 + 48 + 61) / 4.

## Use Cases

### Chart Gaps for Missing Readings

**Scenario:** A line chart plots daily sensor readings. A missing day should show as a gap, not as a drop to zero.

```excel
=IF(B2="", NA(), B2)
```

**Why It Works:** Excel line and scatter charts skip `#N/A` points, so the line bridges or stops at the gap instead of dropping to 0.

### Marking Unavailable Inputs

**Scenario:** A pricing sheet needs a unit cost for each product. Some products have no cost yet, and the sheet should show that clearly.

```excel
=IF(C2="", NA(), C2 * D2)
```

**Why It Works:** Products without a cost show `#N/A` in the result column instead of a misleading zero margin. Anyone reading the sheet can see which rows are incomplete.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The function was typed as `=NA` without parentheses. | Add the empty parentheses: `=NA()`. |
| `#N/A` in a total | One `#N/A` in the range flows into SUM, AVERAGE or another total. | Wrap the range in IFNA, or exclude the marked rows. |
| `#N/A` shown to readers | The marker remains in a summary or dashboard cell. | Replace it with a readable label in the display column, such as `IFNA(value, "Not reported")`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions | Line and scatter charts skip `#N/A` points. |
| Google Sheets | Available | Same return value as Excel. |

## Tips and Best Practices

- Use NA for missing data you want charts to skip, and use a blank or zero only when zero is a real value.
- Put the check next to the input, not in the total, so the cause of the gap is easy to find.
- Use IFNA rather than IFERROR when you want to replace only the missing-value marker and leave other errors visible.
- Document the meaning of `#N/A` in the workbook so reviewers do not treat it as a broken formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISNA](ISNA.md) | Tests whether a value is `#N/A` so you can count or flag missing data. |
| [IFNA](../Logical/IFNA.md) | Replaces only `#N/A` with a value you choose. |
| [IFERROR](../Logical/IFERROR.md) | Replaces any error, including `#N/A`, with a value you choose. |
| [ISERROR](ISERROR.md) | Tests for any error value, not only `#N/A`. |
| [ERROR.TYPE](ERROR.TYPE.md) | Returns a number that identifies which error a cell holds. |

## Official Documentation

- [Microsoft Support: NA function](https://support.microsoft.com/en-us/excel/functions/na-function)
- [Google Docs Editors Help: NA](https://support.google.com/docs/answer/3093359)
