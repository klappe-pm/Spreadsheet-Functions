---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
  - Statistical Analysis
use-case:
  - Before and After Comparisons
  - Paired Measurement Checks
related:
  - MMULT
  - SUMPRODUCT
  - SUMSQ
  - SUMX2PY2
  - SUMXMY2
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sumx2my2-function
  - https://support.google.com/docs/answer/3094257
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Sum X Squared Minus Y Squared
tags:
  - arrays
  - excel
  - sheets
  - statistics
---

# SUMX2MY2

## Description

**SUMX2MY2** takes two arrays of the same length, squares each value in the first array, squares the matching value in the second array, subtracts the second square from the first, and adds the differences. The result is the sum of (x squared minus y squared) across all pairs. It is a specialist function that appears in statistical calculations that work with paired squares.

The function pairs values by position, so the first value in `array_x` goes with the first value in `array_y`. Positive and negative differences can cancel, so the result can be negative. Use SUMXMY2 when you need the squared differences instead, and SUMX2PY2 when you need the sum of both squares.

Text, logical values and empty cells in an array or reference are ignored. Cells that contain zero are included. When the two arrays hold different numbers of values, the function returns `#N/A`.

## Syntax

```excel
=SUMX2MY2(array_x, array_y)
```

<!-- Image 1: Paired Arrays. See Images/Math & Trig/SUMX2MY2.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array_x` | Yes | The first array or range of values. Each value is squared. |
| `array_y` | Yes | The second array or range of values. Each value is squared and subtracted from the square of the matching `array_x` value. |

### Return Value

A single number equal to the sum of the squared `array_x` values minus the squared `array_y` values. The result can be negative. The function returns `#N/A` when the arrays contain different numbers of values.

## Examples

All examples use these values. The first array is in `A2:A5`: 5, 3, 8 and 4. The second array is in `B2:B5`: 2, 6, 1 and 4.

### Example 1: Two Ranges

```excel
=SUMX2MY2(A2:A5, B2:B5)
```

**Result:** `57`

The differences are 25 minus 4 (21), 9 minus 36 (-27), 64 minus 1 (63) and 16 minus 16 (0). Their sum is 57.

### Example 2: Array Constants

```excel
=SUMX2MY2({5,3,8,4}, {2,6,1,4})
```

**Result:** `57`

The same values typed directly in the formula give the same answer as Example 1.

### Example 3: Average Per Pair

```excel
=ROUND(SUMX2MY2(A2:A5, B2:B5) / COUNT(A2:A5), 2)
```

**Result:** `14.25`

Dividing the total of 57 by the four pairs gives 14.25 per pair.

### Example 4: Mismatched Arrays

```excel
=SUMX2MY2(A2:A5, B2:B4)
```

**Result:** `#N/A`

The first array has four values and the second has three, so the function returns `#N/A`. Extend the second range to B5 to fix the formula.

## Story Problems

### Problem 1: Comparing Two Sensors

Two sensors record readings for the same three test runs. The engineer wants the sum of the differences of the squared readings.

| Run | Sensor X | Sensor Y |
| --- | --- | --- |
| 1 | 6 | 3 |
| 2 | 2 | 5 |
| 3 | 9 | 4 |

**Task:** Calculate the sum of the squared X readings minus the squared Y readings.

**Solution:**

```excel
=SUMX2MY2(B2:B4, C2:C4)
```

**Answer:** `71`, from 27 (36 minus 9), minus 21 (4 minus 25), plus 65 (81 minus 16).

<!-- Image 2: Sensor Pairs Table. See Images/Math & Trig/SUMX2MY2.md -->

### Problem 2: Paired Test Scores With the Same Totals

A coach records each athlete's squared speed rating before and after a training block. The coach wants the overall change in squared ratings for three athletes. Values are on a 0 to 10 scale.

| Athlete | Before | After |
| --- | --- | --- |
| Lena | 4 | 2 |
| Omar | 7 | 7 |
| Pia | 3 | 6 |

**Task:** Calculate the sum of the squared "before" values minus the squared "after" values.

**Solution:**

```excel
=SUMX2MY2(B2:B4, C2:C4)
```

**Answer:** `-15`, from 12 (16 minus 4), 0 (49 minus 49) and -27 (9 minus 36). The result is negative because the after values are larger overall.

## Use Cases

### Paired Measurement Checks

**Scenario:** A lab compares two calibrated instruments that measure the same samples.

```excel
=SUMX2MY2(Readings[Instrument A], Readings[Instrument B])
```

**Why It Works:** The total shows whether one instrument's squared readings are consistently higher than the other's. Because the differences can cancel, pair this check with SUMXMY2 when the size of the error matters.

### Before and After Comparisons

**Scenario:** An analyst compares squared scores from two test periods for a group of students.

```excel
=SUMX2MY2(Scores[Period 1], Scores[Period 2])
```

**Why It Works:** Positive and negative differences are kept in one number, so the sign of the result shows which period had larger squared scores overall.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The arrays hold different numbers of values. | Make both ranges the same length. |
| Negative result | The second array has larger squared values. | This is expected. Interpret the sign with the data. |
| Unexpected total | Text or blank cells were skipped in one array but not the other. | Check that both arrays contain numbers in the same rows. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Returns `#N/A` for arrays of different sizes. Ignores text, logical values and empty cells. |
| Google Sheets | Available | The arguments are `array_x` and `array_y`. The help page describes the same pairing but does not state a size rule, so test with your data before relying on the result. |

## Tips and Best Practices

- Confirm the arrays are aligned row by row before you use the result.
- Use array constants such as `{5,3,8}` to test the formula with known values.
- Pair this function with SUMXMY2 when you need both the sign and the size of the differences.
- Keep the arrays in the same order, because the pairing depends on position.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MMULT](MMULT.md) | Multiplies matrices, a related array operation. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies paired arrays and sums the products. |
| [SUMSQ](SUMSQ.md) | Sums the squares of one set of values. |
| [SUMX2PY2](SUMX2PY2.md) | Sums the squares of both arrays and adds them together. |
| [SUMXMY2](SUMXMY2.md) | Sums the squares of the differences between paired values. |

## Official Documentation

- [Microsoft Support: SUMX2MY2 function](https://support.microsoft.com/en-us/excel/functions/sumx2my2-function)
- [Google Docs Editors Help: SUMX2MY2](https://support.google.com/docs/answer/3094257)
