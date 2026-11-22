---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Binary Storage Planning
  - Doubling Sequence Analysis
  - Signal Bit Depth
related:
  - COMPLEX
  - IMLN
  - IMLOG10
  - LOG
  - LOG10
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imlog2-function
  - https://support.google.com/docs/answer/9366426
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

# IMLOG2

## Description

**IMLOG2** returns the base-2 logarithm of a complex number. The input is text in `x+yi` or `x+yj` form, or a complex number built with COMPLEX. The result is a complex number in the same text form, so `=IMLOG2("1+2i")` returns `1.1610+1.5973i` (rounded here to four decimal places).

Use IMLOG2 when a calculation counts doublings or binary steps and one of the values is complex. For a real number such as 256, the result is a real number (8), because 2 raised to the eighth power is 256. The function is the base-2 member of the IMLOG family alongside IMLOG10, which uses base 10.

For real numbers without a complex part, LOG with a base of 2 gives the same answer in a simpler form. Excel has no complex logarithm function for other bases, so for those cases combine IMLN with IMDIV and divide by the natural log of the base.

## Syntax

```excel
=IMLOG2(inumber)
```

<!-- Image 1: Complex Number Text Format. See Images/Engineering/IMLOG2.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number to take the base-2 logarithm of. Enter it as text in `x+yi` or `x+yj` form, such as `"1+2i"`, or pass the result of COMPLEX. A real number is treated as a complex number with an imaginary part of 0. Google Sheets calls this argument `value`. |

### Return Value

The base-2 logarithm as a complex number in `x+yi` text form. A real input such as 256 returns the real result 8. The function returns an error when the input is not a valid complex number. Microsoft does not list specific error values for this function.

## Examples

### Example 1: Complex Input as Text

```excel
=IMLOG2("1+2i")
```

**Result:** `1.1610+1.5973i` (rounded to four decimal places)

The text is read as the real part 1 and the imaginary part 2. The result is returned in the same text form.

### Example 2: Complex Input From Two Cells

Cell `A2` holds the real part (3) and cell `B2` holds the imaginary part (3).

```excel
=IMLOG2(COMPLEX(A2, B2))
```

**Result:** `2.0850+1.1331i` (rounded to four decimal places)

COMPLEX turns the two numeric cells into a complex number, so the formula does not need to join text.

<!-- Image 2: Complex Input From Two Cells. See Images/Engineering/IMLOG2.md -->

### Example 3: Real Input

```excel
=IMLOG2(256)
```

**Result:** `8`

Two multiplied by itself eight times gives 256, so the base-2 logarithm of 256 is 8.

### Example 4: Guarded Calculation

```excel
=IFERROR(IMLOG2(A2), "Check input")
```

**Result:** `Check input` when `A2` holds text that is not a complex number, such as `abc`.

IFERROR keeps a long column of results readable when one imported value is invalid.

## Story Problems

### Problem 1: Sensor Bit Depth

A camera sensor stores a number of brightness levels for each pixel. Its engineers want the number of bits needed for each level count.

| Sensor | Levels |
| --- | --- |
| Basic | 256 |
| Mid | 4096 |
| High | 65536 |

**Task:** Find the number of bits needed for the mid-range sensor, which has 4096 levels in cell `B3`.

**Solution:**

```excel
=IMLOG2(B3)
```

**Answer:** `12`, because 2 raised to the twelfth power is 4096.

### Problem 2: Doubling Stages

A data pipeline has two buffers. Each buffer doubles the number of slots in the stage before it, so the team tracks how many doublings separate the two sizes.

| Buffer | Slots |
| --- | --- |
| Input | 8 |
| Output | 32 |

**Task:** Add the base-2 logarithm of the input buffer size to the base-2 logarithm of the output buffer size.

**Solution:**

```excel
=IMLOG2(B2)+IMLOG2(B3)
```

**Answer:** `8`, because the logarithm of 8 is 3 and the logarithm of 32 is 5. The sum of the two logarithms is the total number of doublings in both stages.

## Use Cases

### Binary Storage Planning

**Scenario:** A planner needs the number of bits required to address a given number of records in a table of sizes that are powers of two.

```excel
=IMLOG2(B2)
```

**Why It Works:** Each row returns the bit count for its record total. Values that are not powers of two return fractional results, so round up with ROUNDUP when you need whole bits.

### Signal Bit Depth Checks

**Scenario:** An engineer checks a column of level counts from several converters and flags any entry that is not a valid number.

```excel
=IFERROR(IMLOG2(B2), "Not valid")
```

**Why It Works:** IFERROR labels the bad entries so the rest of the column remains usable for the report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form. | Rewrite the value as `"1+2i"` or build it with COMPLEX. |
| `#VALUE!` | A text result is used in arithmetic, for example `=IMLOG2(A2)*2`. | Extract the part you need with IMREAL or IMAGINARY first. |
| Text instead of a number | A complex result is compared with a number, so the comparison fails. | Compare the real part with IMREAL instead of the whole result. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Takes one argument named `inumber`. Returns complex text in `x+yi` form. |
| Google Sheets | Available | Takes one argument named `value`. Returns a plain number when the result is real, such as `IMLOG2(256)`. |

## Tips and Best Practices

- Build complex inputs with COMPLEX(real, imaginary) so the formula reads from numeric cells.
- Keep one suffix, `i` or `j`, across a workbook to make the text easy to scan.
- Use IMREAL and IMAGINARY to split a result into numbers before using it in other calculations.
- Wrap imported data in IFERROR so one invalid string does not stop a column of results.
- Use LOG with base 2 for real-only data, which returns a number and needs no text parsing.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex number from real and imaginary coefficients. |
| [IMLN](IMLN.md) | Natural logarithm of a complex number; the base for other logarithms. |
| [IMLOG10](IMLOG10.md) | Base-10 logarithm of a complex number. |
| [LOG](../Math%20%26%20Trig/LOG.md) | Logarithm of a real number in any base you specify, including 2. |
| [LOG10](../Math%20%26%20Trig/LOG10.md) | Base-10 logarithm of a real number. |

## Official Documentation

- [Microsoft Support: IMLOG2 function](https://support.microsoft.com/en-us/excel/functions/imlog2-function)
- [Google Docs Editors Help: IMLOG2](https://support.google.com/docs/answer/9366426)
