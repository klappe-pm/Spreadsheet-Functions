---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - AC Impedance Analysis
  - Signal Phase Analysis
related:
  - IMABS
  - IMAGINARY
  - IMARGUMENT
  - IMCONJUGATE
  - IMREAL
  - IMSUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/complex-function
  - https://support.google.com/docs/answer/7407888
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Number
  - Imaginary Number
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
---

# COMPLEX

## Description

**COMPLEX** combines a real coefficient and an imaginary coefficient into one complex number, written as text in the form `x+yi` or `x+yj`. Engineers use complex numbers to describe alternating current, where resistance is the real part and reactance is the imaginary part. The result is text, so pass it to an IM function such as IMABS or IMSUM to calculate with it.

The suffix argument selects the letter for the imaginary part. Excel accepts a lowercase `i`, which is the default, or a lowercase `j`. An uppercase `I` or `J` returns `#VALUE!`. When the imaginary coefficient is 0, the result omits it, so `COMPLEX(1,0)` returns `1`.

Do not add COMPLEX results with the plus sign, because the output is text. IMSUM is the function that adds complex values.

## Syntax

```excel
=COMPLEX(real_num, i_num, [suffix])
```

<!-- Image 1: Real and Imaginary Axes With a Plotted Point. See Images/Engineering/COMPLEX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `real_num` | Yes | The real coefficient. Non-numeric input returns `#VALUE!`. |
| `i_num` | Yes | The imaginary coefficient. Non-numeric input returns `#VALUE!`. |
| `suffix` | No | The letter for the imaginary part: `"i"` or `"j"`. The default is `"i"`. Any other value, including uppercase, returns `#VALUE!`. |

### Return Value

A text value that holds the complex number, such as `3+4i` or `3+4j`. The function returns `#VALUE!` when a coefficient is not numeric or the suffix is not `"i"` or `"j"`.

## Examples

### Example 1: Default Suffix

```excel
=COMPLEX(3,4)
```

**Result:** `3+4i`

The real coefficient 3 comes first, and the imaginary coefficient 4 is followed by the default suffix `i`.

### Example 2: Engineering Suffix

```excel
=COMPLEX(3,4,"j")
```

**Result:** `3+4j`

The suffix `"j"` is common in electrical engineering, where `i` already stands for current. The number itself is unchanged.

### Example 3: Pure Imaginary Value

```excel
=COMPLEX(0,1)
```

**Result:** `i`

A real part of 0 is left out, and an imaginary coefficient of 1 shows only the suffix.

### Example 4: Negative Imaginary Part

```excel
=COMPLEX(3,-1)
```

**Result:** `3-i`

A negative imaginary coefficient is written with a minus sign in front of the suffix.

## Story Problems

### Problem 1: Impedance of Three Branches

A lab measures three branches of an AC circuit. Each branch has a resistance (the real part) and a reactance (the imaginary part), in ohms. The engineer needs each impedance as a complex value and its overall magnitude, which is the length of the complex number.

| Branch | Resistance | Reactance |
| --- | --- | --- |
| Branch A | 3 | 4 |
| Branch B | 6 | -8 |
| Branch C | 5 | 0 |

**Task:** Build the impedance for each branch from columns B and C, starting at row 2, and calculate its magnitude.

**Solution:**

```excel
=COMPLEX(B2,C2,"j")
```

Enter this in D2 and fill it down to D4. In E2, enter `=IMABS(D2)` and fill it down to E4.

**Answer:** The impedances are `3+4j`, `6-8j`, and `5`. Their magnitudes are `5`, `10`, and `5`, because the lengths are the square roots of 3 squared plus 4 squared, 6 squared plus 8 squared, and 5 squared.

### Problem 2: Two Branches in Series

The same lab connects Branch A and Branch B in series. In a series circuit the complex impedances add, so the total is found with IMSUM, which accepts the text values that COMPLEX returns.

| Branch | Impedance |
| --- | --- |
| Branch A | 3+4j |
| Branch B | 6-8j |

**Task:** Find the total impedance of the two branches in series.

**Solution:**

```excel
=IMSUM(COMPLEX(3,4,"j"),COMPLEX(6,-8,"j"))
```

**Answer:** `9-4j`. The real parts add to 9, and the imaginary parts add to 4 minus 8, which is -4.

<!-- Image 2: Impedance Table With Magnitudes. See Images/Engineering/COMPLEX.md -->

## Use Cases

### AC Impedance Analysis

**Scenario:** A design sheet calculates the magnitude of each branch impedance from its resistance and reactance columns.

```excel
=IMABS(COMPLEX(B2,C2,"j"))
```

**Why It Works:** COMPLEX builds the complex value from the two columns, and IMABS returns its length. Use the same pattern to compare branch magnitudes against a rated limit.

### Signal Phase Analysis

**Scenario:** A signal analysis sheet needs the phase angle of a complex value in radians.

```excel
=IMARGUMENT(COMPLEX(3,4))
```

**Why It Works:** IMARGUMENT returns the angle of the point 3+4i, which is about 0.9273 radians. Keep the angle in radians unless a later formula converts it with DEGREES.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The suffix is uppercase (`"I"` or `"J"`) or is not a valid letter. | Use lowercase `"i"` or `"j"`. |
| `#VALUE!` | A coefficient is text or blank in a way that cannot be read as a number. | Check the source cells. |
| `#VALUE!` | The result is added with `+`. | Use IMSUM, which reads the text value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Suffix must be `"i"` or `"j"`, and the default is `"i"`. |
| Google Sheets | Available | The help page documents `"i"` as the default suffix and shows `"j"` in its examples. It does not list the error conditions. |

## Tips and Best Practices

- Keep the coefficients in their own cells so each part of the impedance can be audited.
- Use `"j"` for electrical work if the rest of the workbook follows that convention, and keep one suffix for the whole sheet.
- Pair COMPLEX with IMREAL and IMAGINARY to recover the two coefficients from a stored value.
- Round results only at the presentation step, since IM functions return text.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMABS](IMABS.md) | Returns the magnitude of a complex value. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient of a complex value. |
| [IMARGUMENT](IMARGUMENT.md) | Returns the phase angle in radians. |
| [IMCONJUGATE](IMCONJUGATE.md) | Returns the complex conjugate. |
| [IMREAL](IMREAL.md) | Returns the real coefficient of a complex value. |
| [IMSUM](IMSUM.md) | Adds complex values, the correct way to combine COMPLEX results. |

## Official Documentation

- [Microsoft Support: COMPLEX function](https://support.microsoft.com/en-us/excel/functions/complex-function)
- [Google Docs Editors Help: COMPLEX](https://support.google.com/docs/answer/7407888)
