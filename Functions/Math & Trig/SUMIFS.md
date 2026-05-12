---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics:
- conditional-aggregation
- multiple-criteria
- advanced-filtering
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Multi-Condition Sum
- Sum Multiple Criteria
- Conditional Sum Multiple
tags:
- conditional
- aggregation
- multi-criteria
- filtering
- wildcards
- AND-logic
---

# SUMIFS

## Description

**SUMIFS** sums values based on multiple conditions simultaneously. Where SUMIF handles one criterion, SUMIFS handles two, three, or dozens—all combined with AND logic. Every row must match ALL specified criteria to be included in the sum. This is the go-to function for complex business analysis: sum sales for the East region AND the Electronics category AND Q4 2025.

**Critical difference from SUMIF: argument order is reversed.** SUMIFS puts the sum_range first, followed by pairs of criteria_range and criteria. This design accommodates unlimited criteria pairs: `=SUMIFS(sum_range, range1, criteria1, range2, criteria2, range3, criteria3, ...)`. Many users stumble when switching between SUMIF and SUMIFS because the sum range moves from last (optional) to first (required).

**All criteria use AND logic, never OR.** If you specify Region="East" and Category="Electronics", only rows matching BOTH conditions are summed. For OR logic (East OR West), you need alternative approaches: multiple SUMIFS added together, or SUMPRODUCT with an array formula. This AND-only design covers the majority of business reporting needs but occasionally requires creative workarounds.

**Wildcards work identically to SUMIF.** Use `*` for any sequence of characters, `?` for a single character, and `~` to escape literal wildcards. All text comparisons are case-insensitive. Date comparisons work by concatenating operators with DATE functions or cell references. The function handles up to 127 criteria pairs in Excel—far more than any practical scenario requires.

## Syntax

> [!f(x)] SUMIFS Syntax
>
> ```
> =SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `sum_range` | Yes | The range of cells to sum. Unlike SUMIF, this comes FIRST and is required. All criteria_ranges should have the same dimensions as sum_range. |
| `criteria_range1` | Yes | The first range to evaluate against criteria1. Must be the same size as sum_range. This is typically a column of category labels, dates, statuses, or other classifiers. |
| `criteria1` | Yes | The condition for criteria_range1. Can be number, text, cell reference, expression with operators, or wildcard pattern. Text and expressions must be in quotes. |
| `criteria_range2, criteria2, ...` | No | Additional pairs of ranges and criteria. Each range must match sum_range dimensions. Up to 127 pairs in Excel, practically unlimited in Sheets. |

### Return Value

Returns a single numeric value representing the sum of cells in sum_range where ALL corresponding criteria_range cells match their respective criteria. Returns 0 if no rows match all criteria. Returns an error if ranges have mismatched sizes or criteria are invalid.

## Examples

> [!f(x)] SUMIFS Examples

### Example 1: Two Criteria - Category and Region
```
=SUMIFS(D2:D100, A2:A100, "Electronics", B2:B100, "East")
```
**Result:** Sum of D values where A is "Electronics" AND B is "East"

**Explanation:** The fundamental SUMIFS pattern. Sums sales amounts (column D) only for Electronics products (column A) in the East region (column B). Both conditions must match for a row to be included.

---

### Example 2: Three Criteria - Category, Region, and Year
```
=SUMIFS(E2:E500, B2:B500, "Furniture", C2:C500, "West", D2:D500, 2025)
```
**Result:** Sum of E values where B="Furniture", C="West", AND D=2025

**Explanation:** Adding more criteria is straightforward—just add more range/criteria pairs. This sums Furniture sales in the West region for 2025 only.

---

### Example 3: Using Cell References for All Criteria
```
=SUMIFS(Sales, Region, G2, Category, H2, Year, I2)
```
**Result:** Dynamic sum based on values in G2, H2, and I2

**Explanation:** Reference cells instead of hardcoding criteria. Change G2, H2, or I2 and the sum updates. Essential for interactive dashboards and parameter-driven reports.

---

### Example 4: Numeric Comparison - Greater Than
```
=SUMIFS(C2:C200, A2:A200, "Completed", B2:B200, ">1000")
```
**Result:** Sum of completed items where value exceeds 1000

**Explanation:** Combines text matching ("Completed") with numeric comparison (">1000"). Useful for filtering by status AND value thresholds.

---

### Example 5: Date Range - Between Two Dates
```
=SUMIFS(D2:D500, C2:C500, ">="&DATE(2025,1,1), C2:C500, "<="&DATE(2025,12,31))
```
**Result:** Sum of D values where dates in C fall within year 2025

**Explanation:** Use the same criteria_range twice with different operators to create a date range. The `&` concatenates the operator with the DATE function result.

---

### Example 6: Date Range with Cell References
```
=SUMIFS(E2:E1000, D2:D1000, ">="&A1, D2:D1000, "<="&B1)
```
**Result:** Sum of E values where dates in D are between dates in A1 and B1

**Explanation:** Dynamic date range filtering. Put start date in A1 and end date in B1 for user-controllable date filtering. Common in financial reporting.

---

### Example 7: Wildcard with Additional Criteria
```
=SUMIFS(C2:C500, A2:A500, "*Corp*", B2:B500, "Active")
```
**Result:** Sum for active companies with "Corp" in their name

**Explanation:** Wildcards work within multi-criteria contexts. This finds all companies containing "Corp" (like "ABC Corp", "BigCorp Inc") that also have Active status.

---

### Example 8: Excluding Values (Not Equal)
```
=SUMIFS(D2:D200, A2:A200, "Sales", B2:B200, "<>Cancelled", C2:C200, "<>Pending")
```
**Result:** Sum of Sales department records that aren't Cancelled or Pending

**Explanation:** Use `<>` to exclude specific values. This sums Sales department amounts excluding both Cancelled and Pending statuses—only finalized transactions.

---

### Example 9: Current Month Calculations
```
=SUMIFS(B2:B500, A2:A500, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), A2:A500, "<"&DATE(YEAR(TODAY()),MONTH(TODAY())+1,1))
```
**Result:** Sum of B values where A dates are in the current month

**Explanation:** Dynamic current-month calculation. First date is the 1st of current month, second is 1st of next month. Automatically adjusts as months change.

---

### Example 10: Multiple Text Conditions
```
=SUMIFS(E2:E300, A2:A300, "North*", B2:B300, "Premium", C2:C300, "Delivered", D2:D300, "Paid")
```
**Result:** Premium, delivered, paid orders from North regions

**Explanation:** Four criteria combining wildcard pattern, exact matches. Each additional criterion narrows the result set. All must match for inclusion.

---

### Example 11: Numeric Range (Between Values)
```
=SUMIFS(C2:C100, B2:B100, ">=50", B2:B100, "<=100")
```
**Result:** Sum of C values where B is between 50 and 100 inclusive

**Explanation:** Apply the same criteria range twice with different operators for numeric "between" logic. Works for quantities, prices, scores, etc.

---

### Example 12: Blank and Non-Blank Criteria
```
=SUMIFS(D2:D200, A2:A200, "Active", B2:B200, "<>", C2:C200, "")
```
**Result:** Sum for Active records where B is not blank AND C is blank

**Explanation:** `""` matches blanks, `<>` (alone) matches non-blanks. This finds Active items with an assigned value in B but nothing in C.

---

### Example 13: Combining Exact Match and Greater/Less Than
```
=SUMIFS(F2:F1000, A2:A1000, "Widget", B2:B1000, "East", C2:C1000, ">=100", D2:D1000, "<500", E2:E1000, 2025)
```
**Result:** Widget sales in East, quantity 100-499, in 2025

**Explanation:** Five criteria covering product, region, quantity range, and year. Complex business queries become manageable with systematic criteria pairing.

---

### Example 14: Using Boolean/Checkbox Values
```
=SUMIFS(C2:C100, A2:A100, TRUE, B2:B100, "Active")
```
**Result:** Sum where column A checkbox is checked AND B is Active

**Explanation:** TRUE/FALSE values from checkboxes can be criteria. Sums amounts for checked items with Active status.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Ranges have different sizes | All criteria_ranges must have exactly the same dimensions as sum_range. Check for mismatched row counts. |
| `#NAME?` | Misspelled function or unquoted text criteria | Ensure text is in quotes: `"East"` not `East`. Verify function name spelling. |
| `0 unexpected` | No rows match ALL criteria, or criteria format mismatch | Check each criterion individually. A typo in any criterion returns 0. Verify data types match (text vs. number). |
| `Wrong order confusion` | Used SUMIF argument order (range, criteria, sum_range) | SUMIFS is sum_range FIRST, then criteria pairs. This is the opposite of SUMIF. |
| `#REF!` | Deleted cells referenced in ranges | Check if any cells in your ranges have been removed. |
| `Criteria not filtering` | Criteria doesn't match data format | Text "100" won't match number 100. Ensure dates are actual dates, not text. Check for hidden spaces. |
| `Partial results` | One criteria pair is wrong | Test each criteria pair independently with single SUMIF calls to isolate the problem. |

## Use Cases

### [[Multi-Dimensional Sales Analysis]]

**Scenario:** Calculate sales by multiple dimensions: region, product category, time period, and sales channel.

**Implementation:**
```
=SUMIFS(Sales[Amount], Sales[Region], "Northeast", Sales[Category], "Electronics", Sales[Quarter], "Q4", Sales[Channel], "Online")
```

**Business Application:** Executive dashboards, quarterly business reviews, strategic planning. Answer questions like "How did online Electronics sales perform in Northeast during Q4?"

**Technical Details:** Create parameter cells for each dimension to enable drill-down analysis. Use data validation dropdowns for user-friendly filtering. Consider PivotTables for extensive multi-dimensional analysis.

---

### [[Date-Bounded Financial Reporting]]

**Scenario:** Sum transactions within specific date ranges for period-over-period comparison.

**Implementation:**
```
=SUMIFS(Transactions[Amount], Transactions[Date], ">="&StartDate, Transactions[Date], "<="&EndDate, Transactions[Type], "Revenue")
```
Where StartDate and EndDate are named ranges containing dates.

**Business Application:** Monthly financial close, quarterly reporting, YoY comparisons, budget vs. actual analysis. Essential for any time-based financial analysis.

**Technical Details:** Use EOMONTH for month-end dates, DATE functions for quarter boundaries. Create a date parameter table for common periods (MTD, QTD, YTD, Prior Year).

---

### [[Inventory Management with Status Filtering]]

**Scenario:** Calculate inventory value by warehouse location, product status, and category.

**Implementation:**
```
=SUMIFS(Inventory[Value], Inventory[Warehouse], "Main", Inventory[Status], "<>Damaged", Inventory[Status], "<>Reserved", Inventory[Category], F2)
```

**Business Application:** Warehouse capacity planning, available inventory reporting, reorder point calculations, inventory valuation for financial statements.

**Technical Details:** Exclusion criteria (`<>`) are powerful for filtering out problematic items. Combine with COUNTIFS for unit counts alongside value sums.

---

### [[Employee Compensation Analysis]]

**Scenario:** Sum salaries by department, job level, location, and employment status.

**Implementation:**
```
=SUMIFS(HR[Salary], HR[Department], "Engineering", HR[Level], "Senior", HR[Location], "HQ", HR[Status], "Active")
```

**Business Application:** Compensation benchmarking, budget planning, headcount analysis, departmental cost allocation.

**Technical Details:** Add date criteria for point-in-time snapshots. Use wildcards for flexible job title matching ("*Engineer*"). Protect sensitive HR data with appropriate access controls.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 2007 and later
- **Criteria pairs limit:** Up to 127 criteria_range/criteria pairs
- **Performance:** Highly optimized; handles millions of rows efficiently
- **Array behavior:** In Excel 365, works with dynamic arrays for spill results
- **Wildcards:** Full support for `*`, `?`, and `~` escape

### Google Sheets
- **Availability:** All versions
- **Criteria pairs limit:** Practically unlimited
- **Performance:** May slow on very large datasets with many criteria
- **Array behavior:** Similar to Excel 365 with ArrayFormula context
- **Wildcards:** Full support matching Excel behavior

### Both Platforms
- Sum_range comes FIRST (different from SUMIF)
- All ranges must have identical dimensions
- Uses AND logic exclusively (all criteria must match)
- Case-insensitive text matching
- Returns 0 when no matches found (not an error)
- Text and logical values in sum_range treated as 0

## Tips and Best Practices

1. **Remember the argument order switch:** SUMIFS puts sum_range first, unlike SUMIF where it's optional and last. This is the most common source of errors when transitioning between the two functions.

2. **Use named ranges for readability:** `=SUMIFS(Sales, Region, "East", Category, "Electronics")` is much clearer than `=SUMIFS(D2:D1000, A2:A1000, "East", B2:B1000, "Electronics")`.

3. **For OR logic, add multiple SUMIFS:** Want East OR West? Use `=SUMIFS(..., Region, "East") + SUMIFS(..., Region, "West")`. This is cleaner than complex SUMPRODUCT alternatives.

4. **Test criteria individually:** If SUMIFS returns unexpected results, test each criterion with a separate SUMIF or COUNTIFS to find which one isn't matching as expected.

5. **Use the same range for "between" conditions:** For date or value ranges, apply the same criteria_range twice: `=SUMIFS(D:D, C:C, ">=100", C:C, "<=200")`. This creates an inclusive range.

6. **Watch for text-formatted numbers:** Numbers stored as text won't match numeric criteria. Look for the green triangle warning in Excel, or use VALUE to convert.

7. **Keep ranges aligned:** All criteria ranges must start and end on the same rows as sum_range. `=SUMIFS(D2:D100, A1:A99, ...)` will error because the ranges don't align.

8. **Consider FILTER for modern solutions:** In Excel 365 and Google Sheets, `=SUM(FILTER(range, condition1*condition2*...))` offers more flexibility for complex scenarios with OR logic.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[SUMIF]] | Sum based on one condition | When you only have a single criterion (simpler syntax) |
| [[COUNTIFS]] | Count with multiple conditions | When you need the count, not the sum |
| [[AVERAGEIFS]] | Average with multiple conditions | When you need the average, not the sum |
| [[MAXIFS]] | Maximum with conditions | When you need the largest matching value |
| [[MINIFS]] | Minimum with conditions | When you need the smallest matching value |
| [[SUMPRODUCT]] | Flexible array-based summing | When you need OR logic or complex conditions |

### Commonly Used Together

**[[COUNTIFS]]** - Count alongside sums

*Calculate average of matching records:*
```
=SUMIFS(C:C, A:A, "East", B:B, "2025") / COUNTIFS(A:A, "East", B:B, "2025")
```
Divides sum by count for average (same as AVERAGEIFS).

---

**[[IF]]** - Handle zero-match scenarios

*Avoid division by zero or show custom message:*
```
=IF(COUNTIFS(A:A,"East",B:B,"2025")>0, SUMIFS(C:C,A:A,"East",B:B,"2025"), "No data")
```
Checks if data exists before summing.

---

**[[IFERROR]]** - Graceful error handling

*Default value on errors:*
```
=IFERROR(SUMIFS(C:C, A:A, D1, B:B, E1), 0)
```
Returns 0 if any error occurs (useful for dynamic criteria that might be invalid).

---

**[[INDIRECT]]** - Dynamic range references

*Variable sheet references:*
```
=SUMIFS(INDIRECT(A1&"!C:C"), INDIRECT(A1&"!A:A"), "East", INDIRECT(A1&"!B:B"), "2025")
```
When the sheet name is stored in a cell.

---

**[[FILTER]]** - Modern alternative for complex logic

*When you need OR or complex conditions:*
```
=SUM(FILTER(C:C, (A:A="East") + (A:A="West")))
```
FILTER with + (OR) or * (AND) offers flexibility SUMIFS lacks.

## Official Documentation

- **Microsoft Excel:** [SUMIFS function](https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b)
- **Google Sheets:** [SUMIFS function](https://support.google.com/docs/answer/3238496)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 2007 | Original introduction | Part of new *IFS function family |
| Excel 2010+ | All subsequent | Performance improvements |
| Excel 2019/365 | Current | Dynamic array support, larger limits |
| Google Sheets | Original launch | Full compatibility with Excel syntax |

---

*Last updated: 2026-01-10*
