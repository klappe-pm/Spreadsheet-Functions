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
- ceiling
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Round Up
- Round Away From Zero
- Always Round Up
tags:
- rounding
- precision
- ceiling
- conservative-estimates
- resource-planning
---

# ROUNDUP

## Description

**ROUNDUP** rounds a number away from zero to a specified number of decimal places. Unlike standard ROUND which follows the "5 or greater rounds up" rule, ROUNDUP always rounds away from zero regardless of the digit being dropped. Positive numbers get larger; negative numbers become more negative. Even if you're rounding 2.001 to an integer, ROUNDUP returns 3, not 2.

This function is essential for **conservative estimates and resource planning**. When calculating how many trucks you need to ship orders, you can't use half a truck—ROUNDUP ensures you always have enough capacity. When determining minimum staffing levels, required inventory, or safety margins, ROUNDUP prevents shortfalls by always erring on the side of more.

Like ROUND, the `num_digits` parameter accepts negative values for rounding to the left of the decimal point. `=ROUNDUP(1234, -2)` returns 1300—rounding 1234 up to the nearest hundred. This works away from zero: `=ROUNDUP(-1234, -2)` returns -1300, not -1200. The direction is always away from zero, whether the number is positive or negative.

**ROUNDUP vs CEILING:** Both round up, but they differ in meaning and behavior. ROUNDUP rounds to a specified number of decimal places (or powers of 10 with negative values). CEILING rounds to a specified multiple. `=ROUNDUP(2.3, 0)` gives 3 (nearest integer away from zero). `=CEILING(2.3, 1)` also gives 3 (nearest multiple of 1 upward). For non-integer multiples, use CEILING: `=CEILING(2.3, 0.5)` rounds to 2.5. ROUNDUP is simpler when you're thinking in decimal places.

## Syntax

> [!f(x)] ROUNDUP Syntax
>
> ```
> =ROUNDUP(number, num_digits)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number` | Yes | The numeric value to round up. Can be positive or negative. For positive numbers, ROUNDUP increases the value; for negative numbers, ROUNDUP makes the value more negative (further from zero). |
| `num_digits` | Yes | The number of digits to round to. Positive values specify decimal places. Zero rounds to the nearest integer (away from zero). Negative values round to powers of 10—use -1 for tens, -2 for hundreds, -3 for thousands. |

### Return Value

Returns a numeric value rounded away from zero to the specified precision. For positive numbers, the result is always greater than or equal to the input. For negative numbers, the result is always less than or equal to the input (more negative). Returns 0 if the number is 0.

## Examples

> [!f(x)] ROUNDUP Examples

### Example 1: Basic Round Up to Integer
```
=ROUNDUP(2.1, 0)
```
**Result:** 3

**Explanation:** Even though 2.1 would normally round to 2, ROUNDUP always goes away from zero. Any fractional part causes the number to round up. This is the fundamental ROUNDUP behavior.

---

### Example 2: Round Up with Larger Decimal
```
=ROUNDUP(2.9, 0)
```
**Result:** 3

**Explanation:** 2.9 would round to 3 with standard ROUND anyway, and ROUNDUP gives the same result here. ROUNDUP and ROUND agree when rounding away from zero is the standard behavior.

---

### Example 3: Round Up to Two Decimal Places
```
=ROUNDUP(3.14159, 2)
```
**Result:** 3.15

**Explanation:** The third decimal (1) would normally round down with ROUND, but ROUNDUP forces it up. 3.14159 becomes 3.15. Useful when you need conservative estimates with decimal precision.

---

### Example 4: Round Up Negative Numbers
```
=ROUNDUP(-2.1, 0)
```
**Result:** -3

**Explanation:** For negative numbers, "away from zero" means more negative. -2.1 rounds to -3, not -2. This is mathematically consistent—ROUNDUP always increases the absolute value.

---

### Example 5: Round Up to Nearest Ten
```
=ROUNDUP(1234, -1)
```
**Result:** 1240

**Explanation:** With num_digits of -1, we round to tens. 1234 rounds up to 1240, not down to 1230. Even the small "4" in the ones place triggers rounding up.

---

### Example 6: Round Up to Nearest Hundred
```
=ROUNDUP(1201, -2)
```
**Result:** 1300

**Explanation:** Any amount above 1200—even just 1201—rounds up to 1300. This is powerful for budgeting: if you need $1,201, budget for $1,300 when rounding to hundreds.

---

### Example 7: Round Up to Nearest Thousand
```
=ROUNDUP(5001, -3)
```
**Result:** 6000

**Explanation:** 5001 rounds up to 6000. ROUNDUP is aggressive—any fractional part of the rounding unit triggers the upward round. Perfect for safety margins.

---

### Example 8: Round Up Negative to Nearest Hundred
```
=ROUNDUP(-1250, -2)
```
**Result:** -1300

**Explanation:** For negative numbers with negative num_digits, ROUNDUP still goes away from zero. -1250 becomes -1300, not -1200. Debts and expenses round to larger absolute values.

---

### Example 9: Resource Calculation - Trucks Needed
```
=ROUNDUP(Items/TruckCapacity, 0)
```
**Result:** Number of trucks needed (always enough)

**Explanation:** If you have 1050 items and each truck holds 100, `=ROUNDUP(1050/100, 0)` = 11 trucks. You can't ship with 10.5 trucks. ROUNDUP ensures sufficient capacity.

---

### Example 10: Time Calculation - Hours to Bill
```
=ROUNDUP(TotalMinutes/60, 0)
```
**Result:** Billable hours (rounded up)

**Explanation:** If a service takes 61 minutes, that's 2 billable hours. 45 minutes is 1 hour. ROUNDUP ensures you never under-bill for partial time periods.

---

### Example 11: Packaging Units Required
```
=ROUNDUP(OrderQuantity/PackSize, 0) * PackSize
```
**Result:** Quantity rounded up to full packs

**Explanation:** If pack size is 12 and order is 25, you need 3 packs (36 units). `=ROUNDUP(25/12, 0) * 12` = 36. Always ship complete packages.

---

### Example 12: Round Up Tiny Fractions
```
=ROUNDUP(0.001, 0)
```
**Result:** 1

**Explanation:** Even the smallest positive fraction rounds up to 1. There's no threshold—any non-zero decimal triggers rounding up. This ensures conservative estimates.

---

### Example 13: Safety Stock Calculation
```
=ROUNDUP(AverageDemand * SafetyFactor, -1)
```
**Result:** Safety stock rounded up to nearest 10

**Explanation:** If average demand is 73 and safety factor is 1.5, raw calculation is 109.5. ROUNDUP to nearest 10 gives 110, ensuring adequate buffer inventory.

---

### Example 14: Price Increase Calculation
```
=ROUNDUP(CurrentPrice * 1.03, 2)
```
**Result:** New price with 3% increase, rounded up to nearest cent

**Explanation:** A $19.95 item with 3% increase is $20.5485. ROUNDUP gives $20.55, not $20.54. Revenue-protective rounding for price adjustments.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Non-numeric input | Ensure both arguments are numbers or cell references containing numbers. Check for text that looks like numbers. |
| `#NAME?` | Misspelled function name | Verify spelling: ROUNDUP (one word, no space). |
| `Unexpected direction` | Negative number behavior | Remember ROUNDUP goes away from zero. -2.1 becomes -3, not -2. If you want to round toward positive infinity, use CEILING. |
| `Too aggressive rounding` | Used ROUNDUP when ROUND was appropriate | ROUNDUP is for conservative estimates. For standard rounding, use ROUND. For financial totals, ROUND is usually correct. |
| `Zero result` | Input is exactly zero | Zero is already at zero—can't round further. ROUNDUP(0, n) = 0 for any n. |
| `Wrong decimal places` | Confusion about num_digits sign | Positive num_digits = decimal places. Negative num_digits = powers of 10. -2 means hundreds, not two decimal places. |

## Use Cases

### [[Resource and Capacity Planning]]

**Scenario:** Calculate required trucks, containers, staff, or equipment where partial units aren't possible.

**Implementation:**
```
=ROUNDUP(TotalVolume/ContainerCapacity, 0)
=ROUNDUP(ProjectHours/40, 0)                    → Full weeks needed
=ROUNDUP(Attendees/TablesSeating, 0)            → Tables needed for event
```

**Business Application:** Logistics planning, workforce scheduling, event coordination, manufacturing capacity. Any scenario where you must have enough and can't use fractional resources.

**Technical Details:** ROUNDUP prevents the common error of under-provisioning. 10.01 units of need becomes 11 units of capacity. Combine with MAX to ensure minimum quantities: `=MAX(ROUNDUP(demand, 0), MinOrder)`.

---

### [[Conservative Budget Estimates]]

**Scenario:** Round cost projections upward to ensure adequate funding.

**Implementation:**
```
=ROUNDUP(EstimatedCost * 1.1, -3)               → Add 10% contingency, round to thousands
=ROUNDUP(MonthlyExpense * 12, -2)               → Annual budget to nearest hundred
=ROUNDUP(SUM(LineItems), -4)                    → Project total to nearest $10,000
```

**Business Application:** Budget proposals, capital requests, project estimates, financial planning. Conservative estimates prevent budget shortfalls.

**Technical Details:** Negative num_digits simplifies executive-level budgets. -3 rounds to thousands, -6 to millions. Combining contingency factors with ROUNDUP creates appropriately padded estimates.

---

### [[Billing and Invoicing]]

**Scenario:** Round time, usage, or quantities upward for billing purposes.

**Implementation:**
```
=ROUNDUP(ServiceMinutes/15, 0) * 15             → Bill in 15-minute increments
=ROUNDUP(DataUsageGB, 0)                        → Bill whole gigabytes
=ROUNDUP(PartialMonth/30, 2)                    → Prorate to hundredths
```

**Business Application:** Professional services billing, utility metering, subscription services, rental agreements. Standard practice is to round up for billing.

**Technical Details:** Many industries have minimum billing increments. ROUNDUP to the increment, then multiply back. Verify billing rules match customer expectations and contract terms.

---

### [[Safety and Compliance Margins]]

**Scenario:** Calculate requirements with built-in safety margins that always err on the side of caution.

**Implementation:**
```
=ROUNDUP(MinimumRequired * SafetyFactor, 0)
=ROUNDUP(RatedCapacity * 0.8, -1)               → Derate to 80%, round up to tens
=ROUNDUP(OccupancyLimit * 0.9, 0)               → 90% max occupancy, rounded
```

**Business Application:** Safety engineering, regulatory compliance, risk management, quality assurance. Margins should always be rounded conservatively.

**Technical Details:** Safety calculations should never under-estimate requirements. ROUNDUP combined with safety factors creates robust margins. Document rounding methodology for compliance audits.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 2000
- **Behavior:** Rounds away from zero for both positive and negative numbers
- **Negative num_digits:** Fully supported for rounding to tens, hundreds, thousands
- **Precision:** 15 significant digits

### Google Sheets
- **Availability:** All versions
- **Behavior:** Identical to Excel—rounds away from zero
- **Negative num_digits:** Fully supported, same as Excel
- **Precision:** 15 significant digits

### Both Platforms
- Rounding direction is always away from zero (positive numbers increase, negative numbers decrease)
- Zero input always returns zero
- Very small numbers (0.0001) still round up to 1 when num_digits is 0
- Both handle floating-point precision the same way

## Tips and Best Practices

1. **Use ROUNDUP for "at least" calculations:** When you need "at least N trucks" or "at least M hours," ROUNDUP ensures you never come up short. It's the "better safe than sorry" function.

2. **Understand negative number behavior:** ROUNDUP(-2.1, 0) = -3, not -2. "Away from zero" means more negative for negative numbers. If you want -2.1 to become -2, use ROUNDDOWN or TRUNC.

3. **Combine with division for unit conversions:** `=ROUNDUP(Quantity/PackSize, 0)` tells you how many packs you need. Multiply back by PackSize to get actual quantity shipped.

4. **Use negative num_digits for budget rounding:** `=ROUNDUP(estimate, -3)` rounds to thousands—much cleaner than complex division and multiplication formulas.

5. **Don't use ROUNDUP for financial totals:** For invoice totals and accounting, standard ROUND is usually correct. ROUNDUP is for planning and estimates, not for representing actual amounts.

6. **Consider CEILING for custom intervals:** To round up to the nearest 0.25 or nearest 5, CEILING is more direct. `=CEILING(value, 0.25)` rounds to quarters. ROUNDUP only works with decimal places.

7. **Document your rounding choices:** When ROUNDUP affects customer-facing numbers (bills, estimates), document why you chose conservative rounding. It's a policy decision, not just a formula choice.

8. **Test with edge cases:** Verify behavior with exactly whole numbers (5.0), very small fractions (0.001), and negative values. ROUNDUP can be aggressive—make sure that's what you want.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[ROUND]] | Standard rounding (5+ rounds away) | When you want normal mathematical rounding, not always-up |
| [[ROUNDDOWN]] | Always rounds toward zero | When you need conservative "already completed" calculations |
| [[CEILING]] | Rounds up to nearest multiple | When rounding to specific intervals (0.25, 5, 100) |
| [[CEILING.MATH]] | Rounds up with direction control | When you need ceiling behavior with sign control |
| [[INT]] | Rounds down to integer | When you want floor behavior for positive numbers |
| [[TRUNC]] | Truncates to specified digits | When you want to simply remove decimal places |

### Commonly Used Together

**[[IF]]** - Conditional application of ROUNDUP

*Apply ROUNDUP only when needed:*
```
=IF(A1>0, ROUNDUP(A1/100, 0)*100, 0)
```
Round up to nearest 100 only for positive values.

---

**[[MAX]]** - Enforce minimum after rounding

*Ensure minimum quantity:*
```
=MAX(ROUNDUP(Demand, 0), MinimumOrder)
```
Round up demand but never order less than minimum.

---

**[[SUM]]** - Total before rounding up

*Round the sum, not individual values:*
```
=ROUNDUP(SUM(Requirements), -1)
```
Total all requirements, then round up to nearest 10.

---

**[[ROUNDDOWN]]** - Paired for range calculations

*Calculate range with both directions:*
```
Low estimate:  =ROUNDDOWN(Value, -2)
High estimate: =ROUNDUP(Value, -2)
```
Provides conservative low and high bounds.

---

**[[CEILING]]** - Alternative for multiples

*When you need specific intervals:*
```
=CEILING(Value, 0.5)    → Rounds up to nearest 0.5
=ROUNDUP(Value*2, 0)/2  → Equivalent but less elegant
```
CEILING is cleaner for non-power-of-10 intervals.

## Official Documentation

- **Microsoft Excel:** [ROUNDUP function](https://support.microsoft.com/en-us/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7)
- **Google Sheets:** [ROUNDUP function](https://support.google.com/docs/answer/3093443)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2000 | Original introduction |
| Excel 2007+ | All subsequent | No functional changes |
| Google Sheets | Original launch | Matches Excel behavior |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
