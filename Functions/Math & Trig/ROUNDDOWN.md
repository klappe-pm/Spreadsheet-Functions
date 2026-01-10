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
- truncation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Round Down
- Round Toward Zero
- Truncate Decimal
tags:
- rounding
- precision
- truncation
- floor
- conservative
---

# ROUNDDOWN

## Description

**ROUNDDOWN** rounds a number toward zero to a specified number of decimal places. Unlike standard ROUND which follows mathematical rounding rules, ROUNDDOWN always moves toward zero regardless of the digits being dropped. Positive numbers get smaller; negative numbers get closer to zero (less negative). If you ROUNDDOWN 2.999 to an integer, you get 2, not 3.

This function is essential for **"already completed" calculations**. When determining how many complete hours have passed, how many full units have been produced, or how much has been fully earned, ROUNDDOWN tells you what's definitively done without counting partial progress. It's the opposite of ROUNDUP's optimistic "better safe than sorry" approach.

Like its siblings ROUND and ROUNDUP, the `num_digits` parameter accepts negative values for rounding to powers of 10. `=ROUNDDOWN(1999, -3)` returns 1000—rounding down to the nearest thousand. For negative numbers, ROUNDDOWN moves toward zero: `=ROUNDDOWN(-2.9, 0)` returns -2, not -3. The direction is always toward zero.

**ROUNDDOWN vs TRUNC vs INT:** These three functions seem similar but differ importantly. ROUNDDOWN takes a precision parameter and works on any decimal position. TRUNC also rounds toward zero but traditionally takes no precision parameter (though Excel allows one). INT rounds toward negative infinity—for negative numbers, INT(-2.3) = -3 while ROUNDDOWN(-2.3, 0) = -2. For positive numbers, all three behave identically when rounding to integers.

## Syntax

> [!f(x)] ROUNDDOWN Syntax
>
> ```
> =ROUNDDOWN(number, num_digits)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number` | Yes | The numeric value to round down. Can be positive or negative. For positive numbers, ROUNDDOWN decreases the value toward zero; for negative numbers, ROUNDDOWN increases the value toward zero (makes it less negative). |
| `num_digits` | Yes | The number of digits to round to. Positive values specify decimal places (2 = hundredths). Zero rounds to integer toward zero. Negative values round to powers of 10—use -1 for tens, -2 for hundreds, -3 for thousands, always toward zero. |

### Return Value

Returns a numeric value rounded toward zero to the specified precision. For positive numbers, the result is always less than or equal to the input. For negative numbers, the result is always greater than or equal to the input (less negative). Returns 0 if the input is 0.

## Examples

> [!f(x)] ROUNDDOWN Examples

### Example 1: Basic Round Down to Integer
```
=ROUNDDOWN(2.9, 0)
```
**Result:** 2

**Explanation:** Even though 2.9 is closer to 3, ROUNDDOWN always goes toward zero. The decimal portion is discarded. This returns what's "fully completed" without partial credit.

---

### Example 2: Round Down Small Fraction
```
=ROUNDDOWN(2.1, 0)
```
**Result:** 2

**Explanation:** 2.1 would round down with standard ROUND too, but ROUNDDOWN guarantees it. There's never any "rounding up" regardless of the fractional part.

---

### Example 3: Round Down to Two Decimal Places
```
=ROUNDDOWN(3.14959, 2)
```
**Result:** 3.14

**Explanation:** The value is truncated at the second decimal place. 3.14959 becomes 3.14—the 959 portion is simply dropped, not considered for rounding.

---

### Example 4: Round Down Negative Numbers
```
=ROUNDDOWN(-2.9, 0)
```
**Result:** -2

**Explanation:** For negative numbers, "toward zero" means less negative. -2.9 becomes -2, not -3. This is the key difference from INT, which would give -3.

---

### Example 5: Round Down to Nearest Ten
```
=ROUNDDOWN(1999, -1)
```
**Result:** 1990

**Explanation:** With num_digits of -1, we round to tens toward zero. 1999 drops to 1990. The 9 in the ones place is discarded without rounding up.

---

### Example 6: Round Down to Nearest Hundred
```
=ROUNDDOWN(1999, -2)
```
**Result:** 1900

**Explanation:** Rounding to hundreds toward zero. 1999 becomes 1900. No matter how close to 2000, ROUNDDOWN stays at the lower hundred.

---

### Example 7: Round Down to Nearest Thousand
```
=ROUNDDOWN(9999, -3)
```
**Result:** 9000

**Explanation:** 9999 rounds down to 9000. The 999 portion is dropped entirely. This is aggressive truncation—useful for conservative reporting.

---

### Example 8: Round Down Negative to Nearest Hundred
```
=ROUNDDOWN(-1850, -2)
```
**Result:** -1800

**Explanation:** For negative numbers with negative num_digits, ROUNDDOWN still moves toward zero. -1850 becomes -1800 (less negative), not -1900.

---

### Example 9: Complete Hours Calculation
```
=ROUNDDOWN(TotalMinutes/60, 0)
```
**Result:** Number of complete hours

**Explanation:** If someone worked 179 minutes, that's 2 complete hours (with 59 minutes partial). `=ROUNDDOWN(179/60, 0)` = 2. Only count fully completed hours.

---

### Example 10: Units Produced at Capacity
```
=ROUNDDOWN(HoursWorked * UnitsPerHour, 0)
```
**Result:** Whole units completed

**Explanation:** If capacity is 7.5 units/hour and they worked 3 hours, theoretical output is 22.5 units. ROUNDDOWN gives 22—you can't ship half a unit.

---

### Example 11: Elapsed Full Days
```
=ROUNDDOWN((EndDate - StartDate), 0)
```
**Result:** Complete days elapsed

**Explanation:** Date differences often include fractional days. ROUNDDOWN counts only fully completed days, not partial ones.

---

### Example 12: Commission Tiers
```
=ROUNDDOWN(SalesAmount/1000, 0) * 1000
```
**Result:** Sales rounded down to commission tier

**Explanation:** If commission tiers are per $1,000 and sales are $4,750, this returns $4,000—the completed tier for commission calculation.

---

### Example 13: Age Calculation in Years
```
=ROUNDDOWN(YEARFRAC(BirthDate, TODAY()), 0)
```
**Result:** Age in complete years

**Explanation:** YEARFRAC gives precise age as a decimal. ROUNDDOWN converts to the integer age we typically use. Someone 29.9 years old is "29 years old."

---

### Example 14: Inventory Reorder Point
```
=ROUNDDOWN(SafetyStock + LeadTimeDemand, -1)
```
**Result:** Reorder point rounded down to nearest 10

**Explanation:** Conservative inventory planning—round the reorder trigger down to avoid ordering too early. Balances against carrying costs.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Non-numeric input | Ensure both arguments are numbers. Check for text that looks like numbers or empty cells being calculated. |
| `#NAME?` | Misspelled function name | Verify spelling: ROUNDDOWN (one word). Common mistake: ROUND_DOWN or ROUND DOWN. |
| `Confusion with INT` | Different behavior for negative numbers | INT(-2.3) = -3 (toward negative infinity). ROUNDDOWN(-2.3, 0) = -2 (toward zero). Use the one that matches your need. |
| `Unexpected truncation` | Used ROUNDDOWN when ROUND was intended | ROUNDDOWN 2.9 = 2, not 3. For standard mathematical rounding, use ROUND instead. |
| `Missing decimals` | Expected more precision | ROUNDDOWN doesn't add precision—it only removes it. 5.0 rounded to 2 decimals is still 5, not 5.00. |
| `Negative num_digits confusion` | Sign and direction mismatch | Negative num_digits rounds to powers of 10, still toward zero. -2 means hundreds place, not negative direction. |

## Use Cases

### [[Completed Work Calculations]]

**Scenario:** Determine how many whole units, hours, or tasks have been fully completed.

**Implementation:**
```
=ROUNDDOWN(TasksAttempted * CompletionRate, 0)
=ROUNDDOWN(TotalSeconds/3600, 0)                → Complete hours
=ROUNDDOWN(MilesRun/MarathonDistance, 0)        → Marathons completed
```

**Business Application:** Productivity tracking, manufacturing output, service delivery metrics. Count only what's fully done, not work in progress.

**Technical Details:** ROUNDDOWN prevents over-reporting. If 10.9 widgets are in various stages, only 10 are shippable. Partial credit can be tracked separately with MOD: `=MOD(Widgets, 1)` gives the fractional remainder.

---

### [[Conservative Financial Reporting]]

**Scenario:** Report figures rounded down to avoid overstating performance or assets.

**Implementation:**
```
=ROUNDDOWN(RevenueEstimate, -3)                 → Revenue to nearest thousand (low)
=ROUNDDOWN(AssetValue * DepreciationFactor, 2) → Conservative asset value
=ROUNDDOWN(ProjectedSavings, -2)                → Savings to nearest hundred
```

**Business Application:** Financial reporting, audit preparation, investor communications. Conservative figures reduce risk of restatement.

**Technical Details:** Pair with ROUNDUP for range reporting: "Revenue between $4,500,000 and $4,600,000" using ROUNDDOWN and ROUNDUP on the same estimate.

---

### [[Quantity and Packaging Calculations]]

**Scenario:** Calculate how many complete packages, containers, or units can be fulfilled.

**Implementation:**
```
=ROUNDDOWN(AvailableInventory/PackSize, 0)      → Complete packs possible
=ROUNDDOWN(BulkVolume/ContainerSize, 0)         → Full containers
=ROUNDDOWN(TotalWeight/MaxTruckLoad, 0)         → Full truckloads
```

**Business Application:** Order fulfillment, shipping logistics, warehouse operations. You can only ship complete units.

**Technical Details:** The remainder (partial pack) can be calculated as `=MOD(Inventory, PackSize)`. Combine for complete picture: "Can ship 5 full packs with 3 loose units remaining."

---

### [[Time and Duration Calculations]]

**Scenario:** Convert durations to whole time units without over-counting.

**Implementation:**
```
=ROUNDDOWN(TotalMinutes/60, 0)                  → Complete hours
=ROUNDDOWN((NOW()-StartTime)*24, 0)             → Hours elapsed
=ROUNDDOWN(YEARFRAC(StartDate, EndDate)*12, 0)  → Complete months
```

**Business Application:** Time tracking, project duration reporting, milestone calculations. Report definitive completed time periods.

**Technical Details:** For elapsed time calculations, be consistent about whether you're counting completed periods or current period. ROUNDDOWN gives completed; you might add 1 for "currently in Nth period."

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 2000
- **Behavior:** Always rounds toward zero for both positive and negative numbers
- **Negative num_digits:** Fully supported for rounding to tens, hundreds, thousands
- **Precision:** 15 significant digits

### Google Sheets
- **Availability:** All versions
- **Behavior:** Identical to Excel—rounds toward zero
- **Negative num_digits:** Fully supported, same behavior as Excel
- **Precision:** 15 significant digits

### Both Platforms
- Consistent toward-zero behavior regardless of number sign
- Zero input returns zero
- ROUNDDOWN(n, 0) equivalent to TRUNC(n) for integers
- Different from INT for negative numbers

## Tips and Best Practices

1. **Use for "completed" counts:** ROUNDDOWN is perfect when you need to count finished units, not work in progress. If 3.7 widgets are done, only 3 are shippable.

2. **Understand the INT difference:** For positive numbers, ROUNDDOWN and INT are identical. For negative: ROUNDDOWN(-2.7, 0) = -2, INT(-2.7) = -3. Choose based on whether you want toward-zero or toward-negative-infinity.

3. **Combine with MOD for remainders:** `=ROUNDDOWN(A1/B1, 0)` gives quotient, `=MOD(A1, B1)` gives remainder. Together they provide complete division information.

4. **Pair with ROUNDUP for ranges:** When estimating, give conservative low (ROUNDDOWN) and high (ROUNDUP) bounds: "Project cost: $45,000 to $50,000."

5. **Use negative num_digits for magnitude rounding:** `=ROUNDDOWN(value, -3)` rounds to thousands toward zero—simpler than division approaches for summary reporting.

6. **Watch for data type issues:** ROUNDDOWN on text-that-looks-like-numbers returns #VALUE!. Use VALUE() to convert text to numbers first.

7. **Consider TRUNC as alternative:** For simple truncation to integer, TRUNC(n) is equivalent to ROUNDDOWN(n, 0) and may be more readable.

8. **Test negative number scenarios:** If your data includes negatives, verify ROUNDDOWN gives the direction you expect. -$2.50 becoming -$2.00 might not be the conservative choice for expenses.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[ROUND]] | Standard rounding (5+ rounds away from zero) | When you want normal mathematical rounding behavior |
| [[ROUNDUP]] | Always rounds away from zero | When you need conservative "at least" estimates |
| [[TRUNC]] | Truncates toward zero | Essentially identical for most uses, slightly simpler syntax |
| [[INT]] | Rounds toward negative infinity | When negative numbers should round more negative, not toward zero |
| [[FLOOR]] | Rounds down to nearest multiple | When rounding to specific intervals (0.25, 5, 100) |
| [[FLOOR.MATH]] | Floor with direction control | When you need floor behavior with sign options |

### Commonly Used Together

**[[MOD]]** - Get the remainder after ROUNDDOWN

*Complete division information:*
```
Quotient:  =ROUNDDOWN(A1/B1, 0)
Remainder: =MOD(A1, B1)
```
Together they reconstruct the original: quotient * divisor + remainder = original.

---

**[[ROUNDUP]]** - Create range estimates

*Low and high bounds:*
```
Low:  =ROUNDDOWN(Estimate, -2)
High: =ROUNDUP(Estimate, -2)
```
Provides conservative range for planning.

---

**[[IF]]** - Conditional rounding direction

*Round based on sign:*
```
=IF(A1>=0, ROUNDDOWN(A1, 0), ROUNDUP(A1, 0))
```
Custom rounding logic based on value.

---

**[[QUOTIENT]]** - Alternative for integer division

*When you only need whole number result:*
```
=QUOTIENT(A1, B1)        → Integer quotient
=ROUNDDOWN(A1/B1, 0)     → Same result
```
QUOTIENT is more explicit about intent.

---

**[[TRUNC]]** - Simpler truncation

*When no precision parameter needed:*
```
=TRUNC(3.7)             → 3
=ROUNDDOWN(3.7, 0)      → 3 (same result, more verbose)
```
TRUNC is cleaner when just removing decimals.

## Official Documentation

- **Microsoft Excel:** [ROUNDDOWN function](https://support.microsoft.com/en-us/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53)
- **Google Sheets:** [ROUNDDOWN function](https://support.google.com/docs/answer/3093442)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2000 | Original introduction |
| Excel 2007+ | All subsequent | No functional changes |
| Google Sheets | Original launch | Matches Excel behavior |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
