---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
purpose:
  - Error Handling
  - Type Checking
use-case:
  - Flagging Broken Calculations
  - Forecast Error Reporting
related:
  - ERROR.TYPE
  - IFERROR
  - ISERROR
  - ISNA
  - VLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093348
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Error Except NA Test
tags:
  - error-checks
  - error-handling
  - excel
  - sheets
---

# ISERR

## Description

**ISERR** tests whether a value is an error, with one exception: it ignores `#N/A`. It returns TRUE for `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?`, `#NUM!` and `#NULL!`, and FALSE for `#N/A` and for any value that is not an error.

Use ISERR when `#N/A` is an expected result, such as a lookup for a month that has no data yet, and other errors signal a real problem that needs attention. The exception is the reason the function exists. ISERROR counts `#N/A` as an error too, so it would flag the expected results along with the real problems.

ISERR is most often used inside IF, because the test on its own only returns TRUE or FALSE. If you need to catch every error, including `#N/A`, use ISERROR instead. If you need only the `#N/A` case, use ISNA.

## Syntax

```excel
=ISERR(value)
```

<!-- Image 1: Error Exception Table. See Images/Information/ISERR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. It can be a formula, a cell reference or a constant such as `#DIV/0!`. |

### Return Value

TRUE when the value is an error other than `#N/A`. FALSE when the value is `#N/A` or is not an error at all. A range passed directly returns one result, so use SUMPRODUCT or ARRAYFORMULA to test many cells.

## Examples

Cells A1 to A4 hold these values: A1 `=1/0`, A2 `=NA()`, A3 the number 10 and A4 `=SQRT(-1)`.

### Example 1: Division Error

```excel
=ISERR(A1)
```

**Result:** `TRUE`

`#DIV/0!` is an error other than `#N/A`, so the test returns TRUE.

### Example 2: The Excluded Case

```excel
=ISERR(A2)
```

**Result:** `FALSE`

`#N/A` is the one error ISERR ignores, so the result is FALSE.

### Example 3: A Normal Number

```excel
=ISERR(A3)
```

**Result:** `FALSE`

A number is not an error, so the test returns FALSE.

### Example 4: Flagging a Real Problem

```excel
=IF(ISERR(A4), "Check input", "OK")
```

**Result:** `Check input`

`SQRT(-1)` returns `#NUM!`, which is not `#N/A`, so the IF formula shows the warning.

### Example 5: Keeping an Expected Gap

```excel
=IF(ISERR(A2), "Error", "No error")
```

**Result:** `No error`

The `#N/A` in A2 is an expected gap, so the formula does not report it as an error.

<!-- Image 2: ISERR Versus ISERROR Results. See Images/Information/ISERR.md -->

## Story Problems

### Problem 1: Counting Real Errors in a Forecast

A monthly forecast column returns `#N/A` for months without data, which is expected. Other errors are real problems.

| Month | Forecast |
| --- | --- |
| Jan | 1200 |
| Feb | `#N/A` |
| Mar | `#DIV/0!` |
| Apr | 1350 |
| May | `#VALUE!` |

**Task:** Count the real errors in B2:B6 that are not `#N/A`.

**Solution:**

```excel
=SUMPRODUCT(--ISERR(B2:B6))
```

**Answer:** `2`. March (`#DIV/0!`) and May (`#VALUE!`) are real errors. February is `#N/A`, which ISERR ignores.

### Problem 2: Flagging Broken Margins

A margin sheet holds one value per product. Alpha and Gamma are fine or expected, while Beta and Delta have broken formulas.

| Product | Margin |
| --- | --- |
| Alpha | 0.25 |
| Beta | `#DIV/0!` |
| Gamma | `#N/A` |
| Delta | `#VALUE!` |

**Task:** Put `=IF(ISERR(B2), "Check", "OK")` in C2 and fill it down to row 5.

**Solution:**

```excel
=IF(ISERR(B2), "Check", "OK")
```

**Answer:** Alpha shows `OK`, Beta shows `Check`, Gamma shows `OK` because its `#N/A` is ignored, and Delta shows `Check`.

## Use Cases

### Forecast Error Reporting

**Scenario:** A regional forecast leaves `#N/A` in months that have no sales data, but the finance lead wants a list of only the formulas that are broken.

```excel
=SUMPRODUCT(--ISERR(Forecast!B2:B13))
```

**Why It Works:** The count ignores the expected `#N/A` values and counts the broken formulas, so the number is a useful alert.

### Flagging Broken Calculations

**Scenario:** A pricing model should show a check mark for each product when the margin formula works and a warning when it does not.

```excel
=IF(ISERR(B2), "Check formula", "OK")
```

**Why It Works:** The warning appears for real errors, while expected gaps still display their own `#N/A` result for the reader.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| FALSE for an error that looks real | The error is `#N/A`, which ISERR excludes. | Use ISERROR or ISNA when every `#N/A` must be caught. |
| One result for a range | ISERR tests one value at a time when given a single reference. | Use SUMPRODUCT with `--ISERR(range)` in Excel, or ARRAYFORMULA in Google Sheets. |
| Errors missed from a lookup | A lookup returns `#N/A` for no match, which ISERR ignores. | Decide whether `#N/A` is expected, then pick ISERR or ISERROR. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions, including Excel for the web | Ignores only `#N/A`. Use SUMPRODUCT or ARRAYFORMULA for ranges. |
| Google Sheets | Available | Same definition as Excel: an error other than `#N/A`. Use ARRAYFORMULA for ranges. |

## Tips and Best Practices

- Use ISERR when `#N/A` is an acceptable result and other errors need attention.
- Pair ISERR with IF to return a message rather than a bare TRUE or FALSE.
- Use ISNA when only the `#N/A` case matters.
- Use ERROR.TYPE to identify which error occurred when the report needs the type.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERROR.TYPE](ERROR.TYPE.md) | Returns the number of the error type, for reports that need the kind of error. |
| [IFERROR](../Logical/IFERROR.md) | Returns a fallback value for any error, without a separate test. |
| [ISERROR](ISERROR.md) | Tests for any error, including `#N/A`. |
| [ISNA](ISNA.md) | Tests only for the `#N/A` error. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | A common source of `#N/A` results that ISERR ignores. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISERR](https://support.google.com/docs/answer/3093348)
