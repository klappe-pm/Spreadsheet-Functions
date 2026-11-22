---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Cascaded Gain Chains
  - Phase Shift Accumulation
  - Series Signal Processing
related:
  - COMPLEX
  - IMDIV
  - IMPOWER
  - IMSUB
  - IMSUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/improduct-function
  - https://support.google.com/docs/answer/7409679
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Product
tags:
  - complex-numbers
  - engineering
  - excel
  - sheets
---

# IMPRODUCT

## Description

**IMPRODUCT** multiplies between 1 and 255 complex numbers and returns the product as a complex number in `x+yi` text form. Each factor can be text such as `"3+4i"`, a result of COMPLEX, a real number, or a range of cells that hold complex values.

Use IMPRODUCT when several complex factors act in sequence, such as the gains of cascaded stages or the phase shifts applied one after another. Multiplying complex numbers combines their magnitudes and adds their angles, so the order of the factors does not change the result.

For two complex numbers, IMPRODUCT is the same as writing the product with the * operator on COMPLEX results, but the function accepts a range and many factors at once. To raise one complex number to a power, use IMPOWER. For a sum rather than a product, use IMSUM.

## Syntax

```excel
=IMPRODUCT(inumber1, [inumber2], ...)
```

<!-- Image 1: Factor Arguments and Range Input. See Images/Engineering/IMPRODUCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber1` | Yes | The first complex number or range to multiply. Google Sheets calls this argument `factor1`. |
| `[inumber2], ...` | No | Up to 254 more complex numbers or ranges, for a total of 255 factors. Google Sheets calls these `factor2, ...`. |

### Return Value

The product as a complex number in `x+yi` text form, such as `5-5i`. A real factor is treated as a complex number with no imaginary part. Microsoft does not list specific error values for this function. Google Sheets requires every factor to use the same suffix, either `i` or `j`.

## Examples

### Example 1: Two Factors

```excel
=IMPRODUCT("2+1i", "1-3i")
```

**Result:** `5-5i`

The product is 2 times 1, then 2 times -3i, then 1i times 1, then 1i times -3i. Those terms add to `5-5i`, because i squared is -1.

### Example 2: Complex Value Times a Real Number

```excel
=IMPRODUCT(COMPLEX(3, -1), 2)
```

**Result:** `6-2i`

A real factor scales both parts of the complex number, so 3-i doubles to 6-2i.

### Example 3: Three Factors

```excel
=IMPRODUCT("1+1i", "1-1i", "2i")
```

**Result:** `4i`

The first two factors multiply to 2, and 2 times 2i is 4i. Order does not change the product.

### Example 4: Product of a Range

Cells `A2:A4` hold the values `1+1i`, `2` and `1-1i`.

```excel
=IMPRODUCT(A2:A4)
```

**Result:** `4`

The complex factors cancel to a real number, so the result is returned without an imaginary part.

## Story Problems

### Problem 1: Two-Stage Amplifier

A two-stage amplifier has a complex gain for each stage. The overall gain is the product of the stage gains.

| Stage | Gain |
| --- | --- |
| 1 | 2+1i |
| 2 | 1-3i |

**Task:** Find the overall gain of the amplifier from the two stage values in `B2:B3`.

**Solution:**

```excel
=IMPRODUCT(B2:B3)
```

**Answer:** `5-5i`, because (2+1i)(1-3i) expands to 2, minus 6i, plus 1i, minus 3i squared, which is `5-5i`.

### Problem 2: Three-Stage Chain With a Phase Shift

A signal passes through a third stage with a pure phase shift of `2i`. The team extends the chain to three stages.

| Stage | Gain |
| --- | --- |
| 1 | 2+1i |
| 2 | 1-3i |
| 3 | 2i |

**Task:** Find the combined gain of all three stages from `B2:B4`.

**Solution:**

```excel
=IMPRODUCT(B2:B4)
```

**Answer:** `10+10i`, because the first two stages give 5-5i, and (5-5i) times 2i is 10 + 10i.

<!-- Image 2: Stage Table and Combined Gain. See Images/Engineering/IMPRODUCT.md -->

## Use Cases

### Cascaded Gain Chains

**Scenario:** A design team lists the complex gain of each stage in a column and needs the total gain of the chain.

```excel
=IMPRODUCT(B2:B9)
```

**Why It Works:** One formula covers the whole column, so adding a stage means extending the range rather than rewriting a chain of multiplications.

### Phase Shift Accumulation

**Scenario:** A network applies a phase shift at each node. The engineer wants the total shift for a path that uses three nodes.

```excel
=IMPRODUCT(D2:D4)
```

**Why It Works:** The product combines the magnitudes and adds the angles of the nodes, so the single result describes the whole path.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Rejected factor (Google Sheets) | Factors mix suffixes, for example `"4+3i"` and `"1+2j"`. | Use the same suffix, `i` or `j`, in every factor. |
| Error value | A factor is text that is not a complex number. | Check the cells in the range and correct the text. |
| Too many factors | The call passes more than 255 factors. | Split the list into two products and multiply the results. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Accepts 1 to 255 complex numbers or ranges. |
| Google Sheets | Available | Factors must share the same suffix. Arguments are named `factor1` and `factor2, ...`. |

## Tips and Best Practices

- Keep one suffix, `i` or `j`, in each column of factors so mixed input does not fail.
- Build complex cells with COMPLEX when the source data is numeric.
- Use a range rather than a long list of arguments so new stages are picked up by extending the range.
- Use IMSUM when the values are added rather than multiplied.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds a complex factor from real and imaginary coefficients. |
| [IMDIV](IMDIV.md) | Divides one complex number by another, the inverse of multiplying. |
| [IMPOWER](IMPOWER.md) | Raises one complex number to a power, the repeated-product case. |
| [IMSUB](IMSUB.md) | Subtracts one complex number from another. |
| [IMSUM](IMSUM.md) | Adds complex numbers instead of multiplying them. |

## Official Documentation

- [Microsoft Support: IMPRODUCT function](https://support.microsoft.com/en-us/excel/functions/improduct-function)
- [Google Docs Editors Help: IMPRODUCT](https://support.google.com/docs/answer/7409679)
