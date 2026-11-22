---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Circuit Frequency Response
  - Filter Gain Analysis
  - Logarithmic Signal Scales
related:
  - COMPLEX
  - IMLN
  - IMLOG2
  - LOG
  - LOG10
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imlog10-function
  - https://support.google.com/docs/answer/9366497
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - complex-numbers
  - engineering
  - excel
  - logarithm
  - sheets
---

# IMLOG10

## Description

**IMLOG10** returns the base-10 (common) logarithm of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number written in the same text form, so `=IMLOG10("1+2i")` returns `0.3495+0.4808i` (rounded here to four decimal places).

Use IMLOG10 when a model works in base 10 and one of its values is complex, such as a transfer function value taken at each point of a frequency sweep. A plain real number also works. In Google Sheets, a real input such as 100 returns a plain number (2), because the result has no imaginary part.

For real numbers that are not complex, LOG10 is the simpler choice. For base 2, use IMLOG2. Excel has no complex logarithm function for other bases; combine IMLN with IMDIV and divide by the natural log of the base instead.

## Syntax

```excel
=IMLOG10(inumber)
```

<!-- Image 1: Complex Number Text Format. See Images/Engineering/IMLOG10.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to take the base-10 logarithm of. Enter it as text in `x+yi` or `x+yj` form, such as `"3+4i"`, or pass the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `value`. |

### Return Value

The base-10 logarithm as a complex number in `x+yi` text form. Google Sheets returns a plain number when the result is real, such as `=IMLOG10(100)` returning 2. The function returns an error when the input is not a valid complex number. Microsoft does not list specific error values for this function.

## Examples

### Example 1: Complex Gain Reading

```excel
=IMLOG10("1+2i")
```

**Result:** `0.3495+0.4808i` (rounded to four decimal places; Excel shows more digits)

The function works on both parts of the value, so the real and imaginary parts of the result both change when the input changes.

### Example 2: Coefficients From Separate Cells

Cell `A2` holds the real part (2) and cell `B2` holds the imaginary part (1).

```excel
=IMLOG10(COMPLEX(A2, B2))
```

**Result:** `0.3495+0.2014i` (rounded to four decimal places)

COMPLEX builds the complex number from two numeric cells, which avoids joining text with the `&` operator.

<!-- Image 2: Complex Input From Two Cells. See Images/Engineering/IMLOG10.md -->

### Example 3: Real Input

```excel
=IMLOG10(1000)
```

**Result:** `3`

A real input has no imaginary part, so the result is a real number. Ten to the third power is 1000, which gives a logarithm of 3.

### Example 4: Guarded Calculation

```excel
=IFERROR(IMLOG10(A2), "Check input")
```

**Result:** `Check input` when `A2` holds text that is not a complex number, such as `abc`.

Wrap the call in IFERROR when the input comes from users or imported data, so one bad cell does not stop a column of results.

## Story Problems

### Problem 1: Filter Response Sweep

A lab measures the complex gain of a filter at three test points and records each value as text.

| Test Point | Gain |
| --- | --- |
| 1 | 2+1i |
| 2 | 3+3i |
| 3 | 1-2i |

**Task:** Find the base-10 logarithm of the gain at test point 2, which is in cell `B3`.

**Solution:**

```excel
=IMLOG10(B3)
```

**Answer:** `0.6276+0.3411i` (rounded to four decimal places), because the base-10 logarithm of 3+3i has a real part of about 0.6276 and an imaginary part of about 0.3411.

### Problem 2: Reading Scale Totals

A data logger stores two readings in `B2` and `B3`: 1000 and 10. The team wants the sum of their base-10 logarithms.

| Reading | Value |
| --- | --- |
| A | 1000 |
| B | 10 |

**Task:** Add the base-10 logarithm of reading A to the base-10 logarithm of reading B.

**Solution:**

```excel
=IMLOG10(B2)+IMLOG10(B3)
```

**Answer:** `4`, because the logarithm of 1000 is 3 and the logarithm of 10 is 1.

## Use Cases

### Filter Gain Analysis

**Scenario:** An analyst reviews a sweep of complex gain values and wants the base-10 logarithm of each point next to the raw value.

```excel
=IMLOG10(B2)
```

**Why It Works:** Fill the formula down the column. Each row calculates on its own, so a bad entry shows an error only in its own row.

### Transfer Function Checks

**Scenario:** A control engineer needs to flag any sweep point whose input is not a valid complex number before the logarithms feed a report.

```excel
=IFERROR(IMLOG10(B2), "Not complex")
```

**Why It Works:** IFERROR keeps the column readable and marks the rows that need correction, so the report does not fail on a single typo.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form, for example `3 plus 4i`. | Rewrite the value as `"3+4i"` or build it with COMPLEX. |
| `#VALUE!` | A result in text form is used in arithmetic, for example `=IMLOG10(A2)+1`. | Extract the real part with IMREAL or the imaginary part with IMAGINARY before adding. |
| Text instead of a number | The result is complex text, so comparisons with numbers return unexpected results. | Use IMREAL or IMAGINARY to get the number you need. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Takes one argument named `inumber`. Returns complex text in `x+yi` form. |
| Google Sheets | Available | Takes one argument named `value`. Returns a plain number when the result is real, such as `IMLOG10(100)`. |

## Tips and Best Practices

- Build complex inputs with COMPLEX(real, imaginary) so the formula reads from numeric cells instead of text joins.
- Use one suffix, `i` or `j`, consistently across a workbook so the text is easy to scan.
- Pull out the parts you need with IMREAL and IMAGINARY before using the result in ordinary math.
- Use IFERROR around imported data, because a single invalid string stops a column of results.
- Use LOG10 instead when the values are real numbers, since it is simpler and returns a number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary coefficients. |
| [IMLN](IMLN.md) | Natural logarithm of a complex number; the base for other logarithms. |
| [IMLOG2](IMLOG2.md) | Base-2 logarithm of a complex number. |
| [LOG](../Math%20%26%20Trig/LOG.md) | Logarithm of a real number in any base you specify. |
| [LOG10](../Math%20%26%20Trig/LOG10.md) | Base-10 logarithm of a real number. |

## Official Documentation

- [Microsoft Support: IMLOG10 function](https://support.microsoft.com/en-us/excel/functions/imlog10-function)
- [Google Docs Editors Help: IMLOG10](https://support.google.com/docs/answer/9366497)
