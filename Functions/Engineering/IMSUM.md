---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Aggregation
  - Complex Numbers
use-case:
  - Parallel Branch Current Totals
  - Series Voltage Totals
related:
  - COMPLEX
  - IMABS
  - IMAGINARY
  - IMPRODUCT
  - IMREAL
  - IMSUB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsum-function
  - https://support.google.com/docs/answer/7408295
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Add Complex Numbers
  - Complex Addition
tags:
  - arithmetic
  - complex-numbers
  - excel
  - sheets
---

# IMSUM

## Description

**IMSUM** adds two or more complex numbers and returns the total as text in `x+yi` or `x+yj` form, such as `4+7i`. Like IMSUB, it adds the real parts together and the imaginary parts together, so one call gives the total of both parts.

Use IMSUM when several complex values must be combined, such as the currents on a parallel branch or the voltages in a series string. You can list the numbers as separate arguments or pass a range of cells that hold complex text. The IMSUB function does the matching subtraction, and COMPLEX builds a value from separate real and imaginary coefficients.

All numbers in one call must use the same suffix, either `i` or `j`. Google Sheets documents that mixing suffixes is not allowed, so a value such as `4+3i` cannot be added to `1+2j` in the same call. A plain real number can be added to complex values, and it counts as having an imaginary part of zero.

## Syntax

```excel
=IMSUM(inumber1, [inumber2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMSUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber1` | Yes | The first complex number to add. Use text in `x+yi` or `x+yj` form, a COMPLEX result, or a cell that holds one. Google Sheets calls this argument `value1`. |
| `[inumber2], ...` | No | Additional complex numbers to add, up to 255 arguments in total in Excel. Google Sheets calls these `value2, ...` and accepts ranges as well. |

### Return Value

A text string in `x+yi` or `x+yj` form that holds the sum. The function returns an error when an argument is not a valid complex number. Google Sheets also returns an error when the arguments mix the `i` and `j` suffixes.

## Examples

### Example 1: Adding Two Text Values

```excel
=IMSUM("2+3i","6-1i")
```

**Result:** `8+2i`

The real parts give 2 plus 6 equals 8, and the imaginary parts give 3 plus (-1) equals 2.

### Example 2: Adding COMPLEX Results

```excel
=IMSUM(COMPLEX(5,2),COMPLEX(-3,4))
```

**Result:** `2+6i`

The real parts give 5 plus (-3) equals 2, and the imaginary parts give 2 plus 4 equals 6.

### Example 3: Mixing Complex Text With Real Numbers

```excel
=IMSUM("7+2j",3,"j")
```

**Result:** `10+3j`

The number 3 is a real value and adds only to the real part, giving 7 plus 3 equals 10. The text `"j"` is the complex number 0+1j, so it adds 1 to the imaginary part, giving 2 plus 1 equals 3.

### Example 4: Summing a Range of Cells

```excel
=IMSUM(B2:B4)
```

**Result:** `7+2i` (with B2 holding `4+1i`, B3 holding `1+3i` and B4 holding `2-2i`)

Every cell in the range is added in one step. The real parts give 4 plus 1 plus 2 equals 7, and the imaginary parts give 1 plus 3 plus (-2) equals 2.

<!-- Image 2: Summing a Range of Complex Values. See Images/Engineering/IMSUM.md -->

### Example 5: Adding Several Values Listed Directly

```excel
=IMSUM("1+1i","2+2i","3+3i")
```

**Result:** `6+6i`

Listing values as separate arguments works the same way as a range. Each added value contributes to both parts of the total.

## Story Problems

### Problem 1: Parallel Branch Current Totals

A panel feeds three parallel branches. The branch currents, in amps, are stored as text in `B2:B4`.

| Branch | Current (amps) |
| --- | --- |
| Lighting | 3+2i |
| Heating | -1+4i |
| Pumps | 2+1i |

**Task:** Find the total current the panel supplies to the three branches.

**Solution:**

```excel
=IMSUM(B2:B4)
```

**Answer:** `4+7i`. The real parts total 3 plus (-1) plus 2, which is 4, and the imaginary parts total 2 plus 4 plus 1, which is 7.

### Problem 2: Voltage Across a Series String

A string of three measurement stages is connected in series. Each stage reports a complex voltage in `B2:B4`.

| Stage | Voltage |
| --- | --- |
| Stage 1 | 5+1i |
| Stage 2 | 2+2i |
| Stage 3 | -3+0i |

**Task:** Find the total voltage across the string.

**Solution:**

```excel
=IMSUM(B2:B4)
```

**Answer:** `4+3i`. The real parts total 5 plus 2 plus (-3), which is 4, and the imaginary parts total 1 plus 2 plus 0, which is 3.

## Use Cases

### Parallel Branch Current Totals

**Scenario:** A facility engineer adds the branch currents on a distribution board to check the total load against the feeder rating.

```excel
=IMSUM(Branches)
```

**Why It Works:** The named range `Branches` holds one complex current per row, so new branches join the total when they are added inside the range. Keep every row on the same suffix.

### Series Voltage Totals

**Scenario:** A test technician sums the stage voltages of a multi-stage amplifier to compare the total with the supply.

```excel
=IMSUM(StageVoltages)
```

**Why It Works:** IMSUM adds the real and imaginary parts separately, so the phase information in each stage is kept in the total.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `4+3i`, or build it with COMPLEX. |
| Error value | The arguments mix `i` and `j` suffixes, such as `4+3i` and `1+2j`. | Use one suffix for every value in the call. |
| Wrong total | A cell in the range holds a label or blank text that was not meant to be included. | Limit the range to the rows that hold complex values. |
| Unexpected result | A number is typed as a fraction or date. | Enter the value as a plain number or as complex text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts up to 255 arguments in total. Argument names are inumber1 and [inumber2]. |
| Google Sheets | Available | Argument names are value1 and value2. Mixing `i` and `j` suffixes is not allowed. |

## Tips and Best Practices

- Use a range argument when the values are already in a column; this keeps the formula short and easy to extend.
- Combine IMSUM with IMSUB to find a net change, such as subtracting one total from another.
- Check the suffix in each row before summing; one mismatched row stops the whole total.
- Use COMPLEX to create values from numeric columns instead of building text strings by hand.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds a complex number from real and imaginary coefficients to add. |
| [IMABS](IMABS.md) | Returns the magnitude of a complex total. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient of the total. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies complex numbers instead of adding them. |
| [IMREAL](IMREAL.md) | Returns the real coefficient of the total. |
| [IMSUB](IMSUB.md) | Subtracts one complex number from another, the counterpart to IMSUM. |

## Official Documentation

- [Microsoft Support: IMSUM function](https://support.microsoft.com/en-us/excel/functions/imsum-function)
- [Google Docs Editors Help: IMSUM](https://support.google.com/docs/answer/7408295)
