---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
  - Statistical Analysis
use-case:
  - Paired Energy Totals
  - Squared Distance From Origin
related:
  - MMULT
  - SUMPRODUCT
  - SUMSQ
  - SUMX2MY2
  - SUMXMY2
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sumx2py2-function
  - https://support.google.com/docs/answer/3094260
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Sum of Square Sums
tags:
  - arrays
  - excel
  - sheets
  - statistics
---

# SUMX2PY2

## Description

**SUMX2PY2** takes two arrays of the same length, squares each value in both arrays, adds each pair of squares, and returns the total. The result is the sum of (x squared plus y squared) across all pairs. It is a specialist function that appears in statistical and geometric calculations that work with paired squares.

The function pairs values by position, so the first value in `array_x` goes with the first value in `array_y`. Because every term is a square plus a square, the total is never negative. Use SUMX2MY2 when you need the difference of the squares instead, and SUMXMY2 when you need the squared differences.

Text, logical values and empty cells in an array or reference are ignored. Cells that contain zero are included. When the two arrays hold different numbers of values, the function returns `#N/A`.

## Syntax

```excel
=SUMX2PY2(array_x, array_y)
```

<!-- Image 1: Paired Arrays. See Images/Math & Trig/SUMX2PY2.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array_x` | Yes | The first array or range of values. Each value is squared. |
| `array_y` | Yes | The second array or range of values. Each value is squared and added to the square of the matching `array_x` value. |

### Return Value

A single number equal to the sum of the squared `array_x` values plus the squared `array_y` values. The result is zero or positive. The function returns `#N/A` when the arrays contain different numbers of values.

## Examples

All examples use these values. The first array is in `A2:A5`: 5, 3, 8 and 4. The second array is in `B2:B5`: 2, 6, 1 and 4.

### Example 1: Two Ranges

```excel
=SUMX2PY2(A2:A5, B2:B5)
```

**Result:** `171`

The pairs give 25 plus 4 (29), 9 plus 36 (45), 64 plus 1 (65) and 16 plus 16 (32). Their sum is 171.

### Example 2: Array Constants

```excel
=SUMX2PY2({5,3,8,4}, {2,6,1,4})
```

**Result:** `171`

The same values typed directly in the formula give the same total as Example 1.

### Example 3: Square Root of the Total

```excel
=ROUND(SQRT(SUMX2PY2(A2:A5, B2:B5)), 2)
```

**Result:** `13.08`

The square root of 171 is 13.0767, which ROUND shows as 13.08.

### Example 4: Mismatched Arrays

```excel
=SUMX2PY2(A2:A5, B2:B4)
```

**Result:** `#N/A`

The arrays have four and three values, so the function returns `#N/A`. Extend the second range to B5 to fix the formula.

## Story Problems

### Problem 1: Squared Distance of Points

A surveyor records the east (X) and north (Y) offsets of two survey points from a reference marker. The sum of squared distances from the marker is the total of each point's squared X plus squared Y.

| Point | X | Y |
| --- | --- | --- |
| A | 3 | 4 |
| B | 6 | 8 |

**Task:** Calculate the sum of the squared X offsets plus the squared Y offsets for both points.

**Solution:**

```excel
=SUMX2PY2(B2:B3, C2:C3)
```

**Answer:** `125`, from 9 + 16 (point A, 25) and 36 + 64 (point B, 100).

<!-- Image 2: Survey Point Table. See Images/Math & Trig/SUMX2PY2.md -->

### Problem 2: Paired Energy Readings

A technician logs two independent energy readings for each test cell, in arbitrary units. The lab reports the combined squared energy across cells.

| Cell | Reading 1 | Reading 2 |
| --- | --- | --- |
| 1 | 2 | 1 |
| 2 | 3 | 5 |
| 3 | 4 | 0 |

**Task:** Calculate the total of the squared readings for all three cells.

**Solution:**

```excel
=SUMX2PY2(B2:B4, C2:C4)
```

**Answer:** `55`, from 5 (cell 1), 34 (cell 2) and 16 (cell 3). A zero reading still counts, because cells that contain zero are included.

## Use Cases

### Squared Distance From Origin

**Scenario:** A logistics team measures each warehouse's offset from a central hub and needs the total squared distance across warehouses.

```excel
=SUMX2PY2(Warehouses[East Offset], Warehouses[North Offset])
```

**Why It Works:** Each warehouse contributes its squared east offset plus its squared north offset. Taking the square root of one row's result gives that warehouse's straight-line distance.

### Paired Energy Totals

**Scenario:** A lab combines two independent measurement channels into one squared-energy total for a test batch.

```excel
=SUMX2PY2(Batch[Channel 1], Batch[Channel 2])
```

**Why It Works:** The two channels are squared and added, so a negative reading in one channel still adds to the total.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The arrays hold different numbers of values. | Make both ranges the same length. |
| Total seems too large | The function returns squares, not the distance itself. | Take the square root of the result to get a length. |
| Unexpected total | Text or blank cells were skipped in one array but not the other. | Check that both arrays contain numbers in the same rows. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Returns `#N/A` for arrays of different sizes. Ignores text, logical values and empty cells. |
| Google Sheets | Available | The arguments are `array_x` and `array_y`. The help page describes the same pairing but does not state a size rule, so test with your data before relying on the result. |

## Tips and Best Practices

- Check that the arrays are aligned row by row before you use the total.
- Use array constants such as `{5,3,8}` to check the formula against known values.
- Wrap the result in SQRT only when the total represents a sum of squared lengths.
- Keep the arrays in the same order, because the pairing depends on position.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MMULT](MMULT.md) | Multiplies matrices, a related array operation. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies paired arrays and sums the products. |
| [SUMSQ](SUMSQ.md) | Sums the squares of one set of values. |
| [SUMX2MY2](SUMX2MY2.md) | Sums the difference of the squares of paired values. |
| [SUMXMY2](SUMXMY2.md) | Sums the squares of the differences between paired values. |

## Official Documentation

- [Microsoft Support: SUMX2PY2 function](https://support.microsoft.com/en-us/excel/functions/sumx2py2-function)
- [Google Docs Editors Help: SUMX2PY2](https://support.google.com/docs/answer/3094260)
