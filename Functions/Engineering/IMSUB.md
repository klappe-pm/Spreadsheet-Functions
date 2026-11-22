---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Branch Current Balancing
  - Impedance Change Tracking
related:
  - COMPLEX
  - IMAGINARY
  - IMDIV
  - IMPRODUCT
  - IMREAL
  - IMSUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imsub-function
  - https://support.google.com/docs/answer/7408393
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Subtraction
  - Subtract Complex Numbers
tags:
  - arithmetic
  - complex-numbers
  - excel
  - sheets
---

# IMSUB

## Description

**IMSUB** subtracts one complex number from another and returns the difference as text in `x+yi` or `x+yj` form, such as `6+5i`. It works on the real parts and the imaginary parts separately: the real part of the second number is subtracted from the real part of the first, and the same happens for the imaginary parts.

Use IMSUB when a value has two parts that must be tracked together, such as impedance in AC circuit work, where the resistance (real part) and the reactance (imaginary part) change at the same time. The companion functions IMSUM, IMPRODUCT and IMDIV handle the other basic operations on complex numbers, and COMPLEX builds a complex number from separate real and imaginary coefficients.

Both arguments must use the same suffix, either `i` or `j`. Google Sheets documents that mixing the two suffixes in one call is not allowed, so write both values with the same letter. The result uses that suffix. Google Sheets also accepts a plain real number as the second argument, while the Excel examples in this page pass real values as complex text such as `4+0i`.

## Syntax

```excel
=IMSUB(inumber1, inumber2)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMSUB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber1` | Yes | The complex number to subtract from. Use text in `x+yi` or `x+yj` form, or the result of COMPLEX. Google Sheets calls this argument `first_number`. |
| `inumber2` | Yes | The complex number to subtract. Its value is removed from `inumber1`. Google Sheets calls this argument `second_number`. |

### Return Value

A text string in `x+yi` or `x+yj` form that holds the difference. The function returns an error when either argument is not a valid complex number. Google Sheets also returns an error when the two arguments use different suffixes.

## Examples

### Example 1: Subtracting Two Text Values

```excel
=IMSUB("10+7i","4+2i")
```

**Result:** `6+5i`

The real parts give 10 minus 4 equals 6, and the imaginary parts give 7 minus 2 equals 5.

### Example 2: Subtracting COMPLEX Results

```excel
=IMSUB(COMPLEX(9,3),COMPLEX(2,-1))
```

**Result:** `7+4i`

COMPLEX(2,-1) is the number `2-1i`. Subtracting it means the real part becomes 9 minus 2 and the imaginary part becomes 3 minus (-1), which is 4.

<!-- Image 2: Real and Imaginary Parts Subtracted Separately. See Images/Engineering/IMSUB.md -->

### Example 3: Working With the `j` Suffix

```excel
=IMSUB("15+6j","2j")
```

**Result:** `15+4j`

A bare `2j` has a real part of 0, so only the imaginary part changes: 6 minus 2 equals 4. The result keeps the `j` suffix.

### Example 4: Real Number as the Second Argument

```excel
=IMSUB("12+5i","4+0i")
```

**Result:** `8+5i`

Writing 4 as `4+0i` gives Excel a complex value with an imaginary part of zero. Google Sheets accepts the plain number 4 in the same position and gives the same result.

### Example 5: Subtracting Values From Cells

```excel
=IMSUB(B3,B2)
```

**Result:** `-5+5i` (with B2 holding `7+3i` and B3 holding `2+8i`)

The formula subtracts the value in B2 from the value in B3. Swapping the arguments would give the opposite sign, `5-5i`, so keep the number being subtracted in the second position.

## Story Problems

### Problem 1: Impedance Change After an Upgrade

A test engineer records a circuit's impedance before and after a component upgrade. The values are stored as text in `A1:B3`.

| Measurement | Impedance |
| --- | --- |
| Before Upgrade | 18+6i |
| After Upgrade | 12+9i |

**Task:** Find how the impedance changed, with the after value subtracted from the before value, so the result shows the change in each part.

**Solution:**

```excel
=IMSUB(B3,B2)
```

**Answer:** `-6+3i`. The real part fell by 6 ohms and the imaginary part rose by 3, because 12 minus 18 is -6 and 9 minus 6 is 3.

### Problem 2: Current Left on a Main Line

A distribution panel carries a main line current of `25+8j` amps. A branch circuit draws `10+3j` amps from it. The main line and branch values are stored in `B2` and `B3`.

| Line | Current (amps) |
| --- | --- |
| Main Line | 25+8j |
| Branch Draw | 10+3j |

**Task:** Find the current that stays on the main line after the branch draw is removed.

**Solution:**

```excel
=IMSUB(B2,B3)
```

**Answer:** `15+5j`, because 25 minus 10 is 15 and 8 minus 3 is 5.

## Use Cases

### Impedance Change Tracking

**Scenario:** A lab compares a sensor circuit across several revisions and wants each revision's change in impedance against the previous one.

```excel
=IMSUB(C3,C2)
```

**Why It Works:** Each row holds the impedance of one revision as text, so the formula gives the change in both parts at once. Keep the suffix the same in every row to avoid errors.

### Branch Current Balancing

**Scenario:** A facility engineer tracks how much current remains on a feeder after several branch circuits are removed.

```excel
=IMSUB(Feeder, BranchDraw)
```

**Why It Works:** Named ranges make the formula readable. Subtract one branch at a time, or keep the branch values in a range and combine them with IMSUM before subtracting.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is not in `x+yi` or `x+yj` form. | Rewrite the value as text such as `4+3i`, or build it with COMPLEX. |
| Error value | The two arguments use different suffixes, such as `4+3i` and `1+2j`. | Write both values with the same suffix. |
| Wrong sign | The arguments are swapped. | Place the number to subtract in the second argument. |
| Unexpected result | A cell holds a number formatted as a fraction or a date instead of complex text. | Enter the value as text or wrap it in COMPLEX. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Argument names are inumber1 and inumber2. The result is text in `x+yi` or `x+yj` form. |
| Google Sheets | Available | Argument names are first_number and second_number. Accepts a plain real number as the second argument. Mixing `i` and `j` suffixes returns an error. |

## Tips and Best Practices

- Build complex values with COMPLEX when the real and imaginary parts come from separate cells.
- Use one suffix for an entire column so the rows can be combined without suffix errors.
- Wrap the formula in IFERROR when the values come from user entry, for example `=IFERROR(IMSUB(B2,B3),"Check input")`.
- Use IMSUM to total several complex numbers before subtracting one total from another.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds a complex number from real and imaginary coefficients. |
| [IMAGINARY](IMAGINARY.md) | Returns the imaginary coefficient of a complex number. |
| [IMDIV](IMDIV.md) | Divides one complex number by another. |
| [IMPRODUCT](IMPRODUCT.md) | Multiplies complex numbers. |
| [IMREAL](IMREAL.md) | Returns the real coefficient of a complex number. |
| [IMSUM](IMSUM.md) | Adds complex numbers, the counterpart to IMSUB. |

## Official Documentation

- [Microsoft Support: IMSUB function](https://support.microsoft.com/en-us/excel/functions/imsub-function)
- [Google Docs Editors Help: IMSUB](https://support.google.com/docs/answer/7408393)
