---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics:
- rounding
- precision
- numeric-formatting
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Round Number
- Round Decimal
- Round Function
tags:
- rounding
- precision
- decimals
- formatting
- numeric
---

# ROUND

## Description

**ROUND** rounds a number to a specified number of decimal places. It takes any numeric value and returns it rounded to the precision you specify. When the digit to be dropped is 5 or greater, ROUND rounds away from zero (up for positive numbers, down for negative numbers). When it's less than 5, ROUND rounds toward zero. This is the standard "round half away from zero" behavior that most people learn in school.

The `num_digits` parameter controls precision in both directions. Positive values specify decimal places (2 means round to cents, 3 means round to thousandths). Zero rounds to the nearest whole number. **Negative values round to the left of the decimal point**—this is ROUND's secret superpower. Use -1 to round to the nearest ten, -2 to round to the nearest hundred, -3 to round to the nearest thousand. For example, `=ROUND(1234, -2)` returns 1200, rounding to the nearest hundred.

**A crucial distinction: ROUND vs display formatting.** Formatting a cell to show 2 decimal places only affects how the number *looks*—the underlying value remains unchanged and is used in all calculations. ROUND actually *changes* the value. This matters enormously for financial calculations where you need true rounding, not just cosmetic display. If you format 2.345 to show 2 decimals, it displays as 2.35 but still calculates as 2.345. If you ROUND(2.345, 2), it becomes exactly 2.35.

**Banker's rounding vs ROUND:** Some financial systems use "banker's rounding" (also called "round half to even"), where 0.5 rounds to the nearest even number to minimize cumulative bias. Excel and Sheets use "round half away from zero" instead—0.5 always rounds up to 1, 2.5 rounds to 3, and -0.5 rounds to -1. If you specifically need banker's rounding, you'll need a custom formula. For most purposes, ROUND's behavior is what you want and expect.

## Syntax

> [!f(x)] ROUND Syntax
>
> ```
> =ROUND(number, num_digits)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number` | Yes | The numeric value to round. Can be a literal number, cell reference, or formula result. Accepts any numeric expression including negative numbers, decimals, and results of other functions. |
| `num_digits` | Yes | The number of digits to round to. Positive values specify decimal places (1 = tenths, 2 = hundredths). Zero rounds to nearest integer. Negative values round to powers of 10 (-1 = tens, -2 = hundreds, -3 = thousands). |

### Return Value

Returns a numeric value rounded to the specified number of digits. The result is an actual number that can be used in further calculations. If `number` is 0, ROUND returns 0. If `num_digits` is very large, the function returns the original number unchanged.

## Examples

> [!f(x)] ROUND Examples

### Example 1: Round to Two Decimal Places
```
=ROUND(2.345, 2)
```
**Result:** 2.35

**Explanation:** The third decimal (5) is 5 or greater, so the value rounds up. This is the most common use case—rounding currency values to cents, percentages to two decimal places, or any precision to hundredths.

---

### Example 2: Round to Whole Number
```
=ROUND(7.8, 0)
```
**Result:** 8

**Explanation:** With num_digits of 0, ROUND returns the nearest integer. Since 7.8 is closer to 8 than to 7, it rounds up. `=ROUND(7.4, 0)` would return 7 because .4 rounds down.

---

### Example 3: Round Negative Numbers
```
=ROUND(-2.5, 0)
```
**Result:** -3

**Explanation:** ROUND uses "round half away from zero"—for negative numbers, 0.5 rounds toward negative infinity (further from zero). This is mathematically consistent: -2.5 rounds to -3, just as 2.5 rounds to 3.

---

### Example 4: Round to Nearest Ten
```
=ROUND(1234, -1)
```
**Result:** 1230

**Explanation:** Negative num_digits rounds to the left of the decimal. -1 means round to the nearest 10. Since the ones digit (4) is less than 5, the number rounds down to 1230.

---

### Example 5: Round to Nearest Hundred
```
=ROUND(1256, -2)
```
**Result:** 1300

**Explanation:** With num_digits of -2, ROUND gives the nearest hundred. The tens digit (5) triggers rounding up, so 1256 becomes 1300. This is useful for budget estimates, financial summaries, and when exact figures aren't needed.

---

### Example 6: Round to Nearest Thousand
```
=ROUND(78500, -3)
```
**Result:** 79000

**Explanation:** The -3 parameter rounds to thousands. 78500 is exactly halfway between 78000 and 79000—and since ROUND uses "round half away from zero," it rounds up to 79000.

---

### Example 7: High Precision Rounding
```
=ROUND(3.141592653589793, 6)
```
**Result:** 3.141593

**Explanation:** Rounding pi to 6 decimal places. The 7th digit (6) causes rounding up. Excel maintains 15 significant digits of precision, so you can round to any precision within that limit.

---

### Example 8: Round a Calculation Result
```
=ROUND(A1/B1, 2)
```
**Result:** Division result rounded to 2 decimal places

**Explanation:** ROUND can wrap any formula. This divides A1 by B1 and rounds the result to cents. Essential when division produces long decimal results that need clean presentation or further calculation.

---

### Example 9: Round SUM Results
```
=ROUND(SUM(A1:A100), 2)
```
**Result:** Sum rounded to 2 decimal places

**Explanation:** Combining ROUND with aggregation functions. This totals a range and then rounds—important for financial reports where penny-level precision matters. Note: ROUND(SUM(...)) rounds the total, not each individual value.

---

### Example 10: The Midpoint Case (x.5)
```
=ROUND(2.5, 0)    → 3
=ROUND(3.5, 0)    → 4
=ROUND(4.5, 0)    → 5
```
**Result:** Always rounds away from zero

**Explanation:** Unlike banker's rounding (which would give 2, 4, 4), ROUND consistently rounds 0.5 away from zero. This predictable behavior is what most users expect, though it can introduce slight upward bias in statistical contexts.

---

### Example 11: Round Very Small Numbers
```
=ROUND(0.00456, 4)
```
**Result:** 0.0046

**Explanation:** Works correctly with very small values. The 5th decimal (6) causes rounding up. Useful for scientific data, currency exchange rates, and any context requiring precision with small numbers.

---

### Example 12: Round Large Numbers to Significant Figures
```
=ROUND(123456789, -6)
```
**Result:** 123000000

**Explanation:** Rounds to the nearest million. For very large numbers in reports or presentations, this creates cleaner, more readable figures. The -6 zeroes out everything below the millions place.

---

### Example 13: No Rounding Needed
```
=ROUND(5.00, 2)
```
**Result:** 5

**Explanation:** When the number already has equal or fewer decimal places than requested, ROUND returns the value unchanged (though it might display differently based on cell formatting). No precision is added—ROUND doesn't pad with zeros.

---

### Example 14: Rounding for Currency Calculations
```
=ROUND(A1 * 0.0825, 2)
```
**Result:** Tax calculation rounded to cents

**Explanation:** Calculating 8.25% tax and rounding to the nearest cent. Essential for invoicing, point-of-sale systems, and any monetary calculation. Never rely on display formatting alone for money—always ROUND.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Non-numeric input in either argument | Ensure both `number` and `num_digits` are numeric. Check for text formatted as numbers or formulas returning text. |
| `#NAME?` | Misspelled function name | Verify spelling: ROUND, not ROUNDS or ROUNDING. |
| `Unexpected result` | Floating-point representation issues | Very long decimals (0.1 + 0.2 = 0.30000000000000004) can cause surprises. For currency, always ROUND final results. |
| `Result shows more decimals` | Cell formatting overriding result | The ROUND function returns the correct value—adjust cell formatting to match the precision you want displayed. |
| `Wrong direction` | Confusion with ROUNDUP/ROUNDDOWN | ROUND uses standard rounding (>=5 rounds away from zero). Use ROUNDUP to always round up, ROUNDDOWN to always round toward zero. |
| `Negative result unexpected` | Negative numbers round away from zero | -2.5 rounds to -3, not -2. This is mathematically correct "away from zero" behavior. |

## Use Cases

### [[Financial Reporting and Currency Calculations]]

**Scenario:** Calculate tax amounts, discounts, and totals that must be rounded to cents.

**Implementation:**
```
=ROUND(Subtotal * TaxRate, 2)
=ROUND(ListPrice * (1 - DiscountPercent), 2)
=ROUND(SUM(LineItems), 2)
```

**Business Application:** Invoicing systems, e-commerce platforms, accounting ledgers, payroll calculations. Any context where monetary values must be exact to the penny.

**Technical Details:** Always ROUND at the end of calculations, not intermediate steps, to minimize rounding errors. For multi-step calculations, carry full precision until the final result. Financial regulations may specify rounding rules—verify compliance requirements.

---

### [[Statistical Data Presentation]]

**Scenario:** Round calculated statistics for cleaner reports and dashboards.

**Implementation:**
```
=ROUND(AVERAGE(SurveyScores), 1)
=ROUND(STDEV(Measurements), 3)
=ROUND(Correlation * 100, 1) & "%"
```

**Business Application:** Research reports, quality control metrics, performance dashboards, academic publications. Presenting data with appropriate precision for the audience.

**Technical Details:** Match rounding precision to the data's inherent accuracy. Rounding to 4 decimal places doesn't add precision if your measurements are only accurate to 2. Consider significant figures conventions in scientific contexts.

---

### [[Budget and Forecast Simplification]]

**Scenario:** Round financial projections to thousands or millions for executive summaries.

**Implementation:**
```
=ROUND(AnnualRevenue, -3)         → Nearest thousand
=ROUND(TotalBudget, -6)           → Nearest million
=ROUND(DepartmentSpend, -2)/100   → Hundreds displayed as "45" for "$4,500"
```

**Business Application:** Board presentations, annual reports, investor decks, strategic planning documents. High-level numbers are easier to comprehend and compare.

**Technical Details:** Negative num_digits is powerful for executive reporting. Consider creating two views: detailed operational data with full precision, and summary views with appropriate rounding for different audiences.

---

### [[Inventory and Quantity Calculations]]

**Scenario:** Round calculated quantities to whole units or packaging quantities.

**Implementation:**
```
=ROUND(DailyUsage * 30, 0)                    → Monthly usage to whole units
=ROUND(OrderQuantity/PackSize, 0) * PackSize  → Round to pack quantities
=ROUND(ForecastDemand, -1)                    → Round to nearest 10 units
```

**Business Application:** Inventory planning, purchase orders, production scheduling, warehouse management. Physical items can't be fractional.

**Technical Details:** For inventory, consider whether ROUNDUP might be safer (to avoid stockouts) or whether the context requires exact rounding. Combine with MIN/MAX to enforce minimum order quantities.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Precision:** 15 significant digits maximum
- **Rounding method:** Round half away from zero (standard)
- **Negative num_digits:** Fully supported, rounds to powers of 10
- **Performance:** Highly optimized, negligible overhead

### Google Sheets
- **Availability:** All versions
- **Precision:** 15 significant digits, matching Excel
- **Rounding method:** Round half away from zero (identical to Excel)
- **Negative num_digits:** Fully supported, identical behavior
- **Performance:** Comparable to Excel

### Both Platforms
- Both use IEEE 754 floating-point, so both exhibit the same floating-point quirks (0.1 + 0.2 does not equal exactly 0.3)
- Both return numeric values, not text—further calculations work correctly
- Both return #VALUE! error when given non-numeric input
- Banker's rounding is not available natively in either platform

## Tips and Best Practices

1. **Round final results, not intermediate calculations:** Rounding at each step compounds errors. Keep full precision through calculations and ROUND only the final output. For example, `=ROUND(A1*B1*C1, 2)` is better than `=ROUND(A1,2)*ROUND(B1,2)*ROUND(C1,2)`.

2. **Use negative num_digits for thousands/millions:** `=ROUND(value, -3)` rounds to thousands—cleaner than dividing by 1000 and then trying to round. Perfect for executive summaries and simplified reporting.

3. **Don't confuse ROUND with display formatting:** Formatting a cell to show 2 decimals doesn't change the underlying value. If you need the actual rounded value for calculations or exports, use ROUND explicitly.

4. **Know your rounding family:** ROUND gives standard rounding. ROUNDUP always rounds away from zero. ROUNDDOWN always rounds toward zero. INT rounds down to integer. TRUNC removes decimals without rounding. Choose based on your needs.

5. **Watch for floating-point surprises:** Due to binary representation, `=ROUND(2.225, 2)` might give unexpected results. If exact decimal arithmetic is critical, consider ROUND(ROUND(value, 10), 2) to clean up floating-point noise first.

6. **Combine with TEXT for formatted strings:** `=TEXT(ROUND(value, 2), "#,##0.00")` gives you a formatted string with guaranteed 2 decimal places displayed. Useful for concatenation and display.

7. **Test edge cases with 5:** Verify that x.5 values round as expected for your use case. ROUND always rounds away from zero, which may or may not match regulatory or business requirements.

8. **Consider MROUND for custom intervals:** If you need to round to nearest 0.25, 0.5, or other intervals, MROUND is more direct than ROUND. `=MROUND(value, 0.25)` rounds to nearest quarter.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[ROUNDUP]] | Always rounds away from zero | When you need to round up regardless of the digit value (e.g., calculating needed resources) |
| [[ROUNDDOWN]] | Always rounds toward zero | When you need to truncate without standard rounding (e.g., calculating whole completed units) |
| [[TRUNC]] | Removes decimal portion | When you want to simply remove decimals without rounding logic |
| [[INT]] | Rounds down to nearest integer | When you need floor function behavior (always toward negative infinity) |
| [[MROUND]] | Rounds to nearest multiple | When rounding to non-decimal intervals (nearest 5, nearest 0.25, etc.) |
| [[CEILING]] | Rounds up to nearest multiple | When rounding up to specific intervals |
| [[FLOOR]] | Rounds down to nearest multiple | When rounding down to specific intervals |

### Commonly Used Together

**[[SUM]]** - Aggregate before rounding

*Round the total, not individual values:*
```
=ROUND(SUM(A1:A100), 2)
```
Rounds the sum to 2 decimal places. More accurate than summing pre-rounded values.

---

**[[AVERAGE]]** - Round calculated averages

*Clean up mean calculations:*
```
=ROUND(AVERAGE(B1:B50), 1)
```
Averages often produce many decimal places. ROUND provides appropriate precision.

---

**[[TEXT]]** - Format rounded values as strings

*Create display-ready text:*
```
=TEXT(ROUND(A1, 2), "$#,##0.00")
```
Combines rounding with number formatting for labels, reports, and concatenation.

---

**[[IF]]** - Conditional rounding precision

*Different precision based on conditions:*
```
=ROUND(A1, IF(A1>1000, 0, 2))
```
Round large values to whole numbers, small values to cents.

---

**[[ABS]]** - Round absolute values

*Round magnitude, preserve sign:*
```
=SIGN(A1) * ROUND(ABS(A1), 2)
```
When you need custom rounding behavior based on absolute value.

## Official Documentation

- **Microsoft Excel:** [ROUND function](https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e904ad0d8e)
- **Google Sheets:** [ROUND function](https://support.google.com/docs/answer/3093440)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function, unchanged behavior |
| Excel 2007+ | All subsequent | No functional changes |
| Google Sheets | Original launch | Matches Excel behavior exactly |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
