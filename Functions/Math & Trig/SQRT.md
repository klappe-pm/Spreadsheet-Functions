---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics:
- square-root
- exponents
- radicals
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Square Root
- Root
- Radical
tags:
- square-root
- exponents
- radicals
- mathematics
- geometry
---

# SQRT

## Description

**SQRT** returns the positive square root of a number. Given a value, SQRT returns the number that, when multiplied by itself, equals that value. SQRT(25) = 5 because 5 x 5 = 25. SQRT(2) returns approximately 1.414, the famously irrational square root of 2. It's one of the most fundamental mathematical operations, appearing in everything from geometry to statistics to finance.

The function requires a **non-negative input**. Negative numbers don't have real square roots—asking for SQRT(-4) returns #NUM! because no real number multiplied by itself gives -4. If your data might contain negative values, wrap with ABS first: `=SQRT(ABS(A1))`. Or use error handling: `=IFERROR(SQRT(A1), "Invalid")`. For complex number square roots, Excel provides IMSQRT.

**Common applications include**: the Pythagorean theorem for distances (`=SQRT(a^2 + b^2)`), standard deviation calculations, geometric mean, area-to-side conversions, and the quadratic formula. Anytime you need to "undo" a squared value, SQRT is your function.

SQRT is equivalent to raising to the power of 0.5: `SQRT(x)` equals `POWER(x, 0.5)` equals `x^0.5`. Use whichever is clearest for your context. For other roots, use POWER: cube root is `POWER(x, 1/3)`, fourth root is `POWER(x, 0.25)`. Only the square root has its own dedicated function.

## Syntax

> [!f(x)] SQRT Syntax
>
> ```
> =SQRT(number)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number` | Yes | A non-negative numeric value for which you want the square root. Can be zero (returns 0), a positive integer, a decimal, a cell reference, or formula result. Negative numbers return #NUM! error. |

### Return Value

Returns the positive square root of the input number. Result is always non-negative. For perfect squares (1, 4, 9, 16...), returns an integer. For non-perfect squares, returns a decimal approximation to 15 significant digits.

## Examples

> [!f(x)] SQRT Examples

### Example 1: Square Root of Perfect Square
```
=SQRT(25)
```
**Result:** 5

**Explanation:** 5 x 5 = 25, so SQRT(25) = 5. Perfect squares return clean integer results.

---

### Example 2: Square Root of Non-Perfect Square
```
=SQRT(2)
```
**Result:** 1.41421356237...

**Explanation:** The square root of 2 is irrational—it cannot be expressed as a simple fraction. Excel returns approximately 1.41421356237 (to 15 digits).

---

### Example 3: Square Root of Zero
```
=SQRT(0)
```
**Result:** 0

**Explanation:** Zero is the only number that is its own square root. 0 x 0 = 0, so SQRT(0) = 0.

---

### Example 4: Square Root of Decimal
```
=SQRT(0.25)
```
**Result:** 0.5

**Explanation:** 0.5 x 0.5 = 0.25. Square roots of fractions work the same as whole numbers.

---

### Example 5: Pythagorean Theorem - Distance
```
=SQRT(A1^2 + B1^2)
```
**Result:** Hypotenuse length

**Explanation:** If A1=3 and B1=4, result is 5. The classic 3-4-5 right triangle. This calculates the straight-line distance given horizontal and vertical components.

---

### Example 6: Euclidean Distance (2D)
```
=SQRT((X2-X1)^2 + (Y2-Y1)^2)
```
**Result:** Distance between two points

**Explanation:** Distance formula in 2D coordinates. If points are (1,1) and (4,5), distance is SQRT(9+16) = SQRT(25) = 5.

---

### Example 7: Standard Deviation Component
```
=SQRT(Variance)
```
**Result:** Standard deviation

**Explanation:** Standard deviation is the square root of variance. If you've calculated variance separately, SQRT converts it to the more interpretable standard deviation.

---

### Example 8: Area to Side Length
```
=SQRT(SquareArea)
```
**Result:** Side length of square

**Explanation:** A square with area 144 square feet has sides of SQRT(144) = 12 feet. Useful in construction, real estate, and geometry.

---

### Example 9: Handling Negative Input (Error)
```
=SQRT(-16)
```
**Result:** #NUM!

**Explanation:** Negative numbers have no real square root. SQRT(-16) returns #NUM! error. Use IMSQRT for complex results, or wrap with ABS if magnitude is intended.

---

### Example 10: Safe SQRT with ABS
```
=SQRT(ABS(A1))
```
**Result:** Square root of absolute value

**Explanation:** If data might contain negatives and you want magnitude, wrap with ABS. SQRT(ABS(-16)) = SQRT(16) = 4.

---

### Example 11: SQRT with Error Handling
```
=IFERROR(SQRT(A1), "Invalid")
```
**Result:** Square root or "Invalid" for errors

**Explanation:** Gracefully handles negative inputs or other errors by returning a custom message instead of #NUM!.

---

### Example 12: Cube Root Using POWER (Comparison)
```
=POWER(27, 1/3)
```
**Result:** 3

**Explanation:** While SQRT handles square roots, other roots use POWER. Cube root of 27 is 3 because 3 x 3 x 3 = 27.

---

### Example 13: SQRT in Quadratic Formula
```
=(-B + SQRT(B^2 - 4*A*C)) / (2*A)
```
**Result:** One root of quadratic equation

**Explanation:** The quadratic formula requires SQRT of the discriminant. If discriminant (B^2-4AC) is negative, SQRT returns #NUM!, indicating no real solutions.

---

### Example 14: Geometric Mean
```
=SQRT(A1 * B1)
```
**Result:** Geometric mean of two numbers

**Explanation:** Geometric mean of 4 and 9 is SQRT(4*9) = SQRT(36) = 6. For more numbers, use POWER with 1/n exponent.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#NUM!` | Negative input value | Ensure input is non-negative. Use ABS if you need magnitude, or IMSQRT for complex results. |
| `#VALUE!` | Non-numeric input | Verify input is a number, not text. Check cell for text-formatted numbers. |
| `#NAME?` | Misspelled function name | Check spelling: SQRT, not SQROOT or SQUAREROOT. |
| `Unexpected result` | Very large or very small numbers | Floating-point precision issues with extreme values. Results accurate to 15 significant digits. |
| `#DIV/0!` | SQRT used in formula that divides | The error is from division, not SQRT. Check surrounding formula logic. |
| `Integer expected` | Got decimal for perfect square | Floating-point can return 2.9999999... instead of 3. Use ROUND if integer needed: ROUND(SQRT(x), 0). |

## Use Cases

### [[Distance and Geometry Calculations]]

**Scenario:** Calculate distances, diagonals, and other geometric measures.

**Implementation:**
```
=SQRT((X2-X1)^2 + (Y2-Y1)^2)                   → 2D distance
=SQRT((X2-X1)^2 + (Y2-Y1)^2 + (Z2-Z1)^2)       → 3D distance
=SQRT(2) * SideLength                          → Diagonal of square
=SQRT(Length^2 + Width^2 + Height^2)           → Box diagonal
```

**Business Application:** Logistics routing, facility layout, GIS mapping, construction calculations. Any spatial analysis requires distance calculations.

**Technical Details:** For lat/long coordinates, use haversine formula or great circle distance—simple Euclidean distance doesn't account for Earth's curvature.

---

### [[Statistical Analysis]]

**Scenario:** Calculate standard deviation, root mean square, and other statistical measures.

**Implementation:**
```
=SQRT(Variance)                                → Standard deviation
=SQRT(SUMPRODUCT((Actual-Predicted)^2)/N)      → Root Mean Square Error
=SQRT(P*(1-P)/N)                               → Standard error of proportion
=SQRT(AVERAGE(Data^2) - AVERAGE(Data)^2)       → Alternative StDev calculation
```

**Business Application:** Quality control, forecasting accuracy, A/B testing, financial risk analysis. Standard deviation and related measures are fundamental to statistical inference.

**Technical Details:** These formulas assume population measures. For sample statistics, use N-1 denominator. Built-in STDEV functions handle this automatically.

---

### [[Financial Calculations]]

**Scenario:** Calculate volatility, Sharpe ratio components, and geometric returns.

**Implementation:**
```
=SQRT(Variance) * SQRT(252)                    → Annualized volatility
=SQRT(A1 * B1)                                 → Geometric mean of two periods
=SQRT(1 + TotalReturn) - 1                     → Related to CAGR calculations
```

**Business Application:** Investment analysis, risk management, portfolio optimization. Volatility is the square root of variance of returns.

**Technical Details:** Annualization uses SQRT of time periods (252 trading days). This assumes independence of returns—an imperfect but standard approximation.

---

### [[Engineering and Physics]]

**Scenario:** Calculate velocities, forces, and other physics-based measures.

**Implementation:**
```
=SQRT(2 * Height * 9.8)                        → Velocity from falling
=SQRT(Tension / LinearDensity)                 → Wave speed on string
=SQRT(Power / Resistance)                      → Current from power/resistance
```

**Business Application:** Product design, mechanical engineering, electrical engineering, physics simulations. Square roots appear throughout physical formulas.

**Technical Details:** Ensure units are consistent. SQRT preserves unit relationships—SQRT(m^2) = m, SQRT(m/s^2) = m/s, etc.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Precision:** 15 significant digits
- **Error handling:** Returns #NUM! for negative inputs
- **Complex numbers:** Use IMSQRT for complex number square roots
- **Performance:** Highly optimized

### Google Sheets
- **Availability:** All versions
- **Precision:** 15 significant digits (same as Excel)
- **Error handling:** Returns #NUM! for negative inputs (same as Excel)
- **Complex numbers:** No native complex number support
- **Performance:** Equivalent to Excel

### Both Platforms
- Identical behavior for positive numbers
- Same error behavior for negative inputs
- Same 15-digit precision limitation
- SQRT(0) = 0 on both platforms
- Equivalent to POWER(x, 0.5) on both platforms

## Tips and Best Practices

1. **Always check for negative inputs:** SQRT of negative numbers returns #NUM!. Use IFERROR, ABS, or MAX(x, 0) to handle potential negatives gracefully.

2. **Use SQRT for readability:** While `x^0.5` and `POWER(x, 0.5)` work identically, SQRT(x) is more immediately understandable for square roots.

3. **Remember SQRT for "undoing" squares:** If you squared something earlier in your calculation, SQRT brings it back to original scale. Essential in standard deviation (SQRT of variance).

4. **Combine with SUM of squares for distance:** The pattern `=SQRT(A^2 + B^2)` is ubiquitous. Know it well for Pythagorean calculations.

5. **Watch for precision with perfect squares:** Due to floating-point, SQRT(9) might return 2.999999... in edge cases. Use ROUND if exact integers are needed.

6. **Use POWER for other roots:** SQRT is only for square roots. For cube root, use POWER(x, 1/3). For nth root, use POWER(x, 1/n).

7. **Consider SQRT in array formulas:** SQRT works element-wise in arrays. `=SQRT(A1:A10)` returns 10 square roots in dynamic array Excel/Sheets.

8. **Understand the statistics connection:** Variance measures squared deviations; SQRT converts back to original units as standard deviation. This interpretability is why we use StDev, not variance, in reporting.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[POWER]] | Raise to any power | For roots other than square root: POWER(x, 1/3) for cube root |
| [[SQRTPI]] | Square root of (number x pi) | When calculating with pi-based areas (circles) |
| [[IMSQRT]] | Square root of complex number | When working with imaginary/complex numbers |
| [[EXP]] | Raise e to a power | For exponential calculations, inverse of LN |
| [[LOG]] | Logarithm | Inverse operation family, undoes exponentiation |

### Commonly Used Together

**[[POWER]]** - Squares and other operations

*Complete distance formula:*
```
=SQRT(POWER(X2-X1, 2) + POWER(Y2-Y1, 2))
```
POWER for squaring, SQRT for root. Equivalent to using ^2.

---

**[[ABS]]** - Safe square root

*Handle potential negatives:*
```
=SQRT(ABS(A1))
```
Ensures non-negative input to avoid #NUM! error.

---

**[[SUM]]** / **[[SUMPRODUCT]]** - Sum of squares

*Root mean square:*
```
=SQRT(SUMPRODUCT(A1:A10^2) / COUNT(A1:A10))
```
Sum squared values, divide, then take root for RMS.

---

**[[AVERAGE]]** - Statistical measures

*Standard deviation pattern:*
```
=SQRT(AVERAGE((Data - AVERAGE(Data))^2))
```
Variance (average squared deviation) under SQRT gives StDev.

---

**[[ROUND]]** - Clean up results

*Integer side length:*
```
=ROUND(SQRT(Area), 0)
```
When you need integer results from SQRT calculations.

## Official Documentation

- **Microsoft Excel:** [SQRT function](https://support.microsoft.com/en-us/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf)
- **Google Sheets:** [SQRT function](https://support.google.com/docs/answer/3093577)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function |
| Excel 2007+ | All subsequent | No changes to behavior |
| Google Sheets | Original launch | Identical to Excel |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
