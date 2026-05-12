---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics:
- conditional-aggregation
- extremes
- multiple-criteria
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Conditional Maximum
- Maximum If Condition
- Max With Criteria
tags:
- maximum
- conditional
- multi-criteria
- filtering
- extremes
- AND-logic
---

# MAXIFS

## Description

**MAXIFS** returns the maximum value from a range based on one or more conditions. It's the conditional version of MAX—instead of finding the largest value in an entire range, it finds the largest value only among rows that match all specified criteria. "What's the highest sale in the East region?" or "What's the maximum temperature on weekdays?"—these are MAXIFS questions.

The syntax follows the SUMIFS pattern: max_range comes first, followed by pairs of criteria_range and criteria. All criteria use AND logic—a value is only considered if its row matches every specified condition. This differs from MAX, which has no built-in filtering capability and simply returns the largest value regardless of any associated data.

**MAXIFS is relatively new, introduced in Excel 2019 and Microsoft 365.** Before MAXIFS, conditional maximums required array formulas: `=MAX(IF(criteria_range=criterion, max_range))` entered with Ctrl+Shift+Enter. MAXIFS eliminates this complexity with a clean, non-array syntax. Google Sheets has supported MAXIFS for longer, maintaining good cross-platform compatibility.

**MAXIFS returns 0 when no values match the criteria.** This behavior can be surprising—you might expect an error or blank when nothing matches. In contexts where 0 could be a valid maximum (like temperatures), this ambiguity can cause confusion. Consider wrapping with IF and COUNTIFS to handle zero-match scenarios explicitly.

## Syntax

> [!f(x)] MAXIFS Syntax
>
> ```
> =MAXIFS(max_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `max_range` | Yes | The range of cells from which to find the maximum. Must contain numeric values. Same dimensions required as all criteria_ranges. |
| `criteria_range1` | Yes | The first range to evaluate against criteria1. Must be the same size as max_range. Contains the values to test against the first criterion. |
| `criteria1` | Yes | The condition for criteria_range1. Can be number, text, cell reference, expression with operators (">100", "<>N/A"), or wildcard pattern ("*Corp"). |
| `criteria_range2, criteria2, ...` | No | Additional pairs of ranges and criteria. Each range must match max_range dimensions. Up to 126 additional pairs in Excel. |

### Return Value

Returns a single numeric value representing the largest number in max_range where ALL corresponding criteria_range cells match their respective criteria. Returns 0 if no cells match all criteria. Returns an error if ranges have mismatched sizes or arguments are invalid.

## Examples

> [!f(x)] MAXIFS Examples

### Example 1: Maximum with One Condition
```
=MAXIFS(C2:C100, A2:A100, "East")
```
**Result:** Largest value in C where A equals "East"

**Explanation:** The simplest MAXIFS pattern. Finds the highest value in column C, but only for rows where column A contains "East". All other rows are ignored.

---

### Example 2: Maximum with Two Conditions
```
=MAXIFS(D2:D500, A2:A500, "Electronics", B2:B500, "Online")
```
**Result:** Largest value in D where A is "Electronics" AND B is "Online"

**Explanation:** Both conditions must match. Finds the maximum sale for Electronics products sold through the Online channel.

---

### Example 3: Using Cell References as Criteria
```
=MAXIFS(Sales, Region, G1, Category, H1, Year, I1)
```
**Result:** Maximum sale for region/category/year specified in G1, H1, I1

**Explanation:** Dynamic criteria from cells enable interactive dashboards. Change the filter cells and the maximum updates automatically.

---

### Example 4: Maximum with Numeric Comparison
```
=MAXIFS(C2:C200, B2:B200, ">=100", A2:A200, "Active")
```
**Result:** Largest value in C where B is at least 100 AND A is "Active"

**Explanation:** Combines text equality ("Active") with numeric comparison (">=100"). Finds maximum among active accounts with balance of 100 or more.

---

### Example 5: Maximum within Date Range
```
=MAXIFS(E2:E1000, D2:D1000, ">="&DATE(2025,1,1), D2:D1000, "<="&DATE(2025,12,31))
```
**Result:** Maximum value in E where dates in D fall within 2025

**Explanation:** Apply the same criteria_range twice with different operators for date ranges. Finds the highest value during the specified year.

---

### Example 6: Maximum with Dynamic Date Range
```
=MAXIFS(Sales, Dates, ">="&StartDate, Dates, "<="&EndDate, Status, "Completed")
```
**Result:** Maximum completed sale within date range from named cells

**Explanation:** Combines date filtering with status filtering. User-defined date range from StartDate and EndDate cells.

---

### Example 7: Maximum Using Wildcards
```
=MAXIFS(B2:B100, A2:A100, "*Corp*")
```
**Result:** Largest value in B where A contains "Corp" anywhere

**Explanation:** Wildcards work in MAXIFS. Matches "ABC Corp", "BigCorp Inc", "Corporate Services", etc.

---

### Example 8: Maximum Excluding Specific Values
```
=MAXIFS(D2:D300, C2:C300, "<>Cancelled", B2:B300, "<>Pending")
```
**Result:** Maximum in D excluding cancelled and pending items

**Explanation:** Use `<>` to exclude values. Finds highest value among finalized transactions only.

---

### Example 9: Maximum by Month (Current Month)
```
=MAXIFS(B2:B500, A2:A500, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), A2:A500, "<"&DATE(YEAR(TODAY()),MONTH(TODAY())+1,1))
```
**Result:** Maximum value in B for the current month

**Explanation:** Dynamic month filtering. First date is start of current month, second is start of next month. Updates automatically.

---

### Example 10: Maximum with Boolean Criteria
```
=MAXIFS(C2:C100, D2:D100, TRUE, A2:A100, "Premium")
```
**Result:** Maximum in C where D is TRUE (checked) AND A is "Premium"

**Explanation:** TRUE/FALSE from checkboxes or logical formulas can be criteria. Finds maximum among checked Premium items.

---

### Example 11: Maximum in Numeric Range
```
=MAXIFS(C2:C200, B2:B200, ">=50", B2:B200, "<=100")
```
**Result:** Maximum in C where B is between 50 and 100 inclusive

**Explanation:** Use same range twice for "between" logic. Finds maximum among rows where the filter value falls within bounds.

---

### Example 12: Maximum with Blank/Non-Blank Criteria
```
=MAXIFS(D2:D100, C2:C100, "<>", B2:B100, "Active")
```
**Result:** Maximum in D where C is not blank AND B is "Active"

**Explanation:** `<>` alone matches any non-blank cell. Ensures C has a value while B equals "Active".

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Ranges have different sizes | All criteria_ranges must have exactly the same dimensions as max_range. Verify row counts match. |
| `#NAME?` | Misspelled function, or function not available in your Excel version | MAXIFS requires Excel 2019 or later. Check spelling and Excel version. |
| `0 unexpected` | No rows match all criteria | MAXIFS returns 0 when nothing matches. Use COUNTIFS to verify matches exist. |
| `#REF!` | Referenced cells have been deleted | Check if any cells in your ranges have been removed. |
| `Wrong result` | Criteria format mismatch | Text "100" won't match number 100. Check for hidden spaces or wrong data types. |
| `Missing criteria pair` | Odd number of arguments after max_range | Criteria must come in pairs: range, criterion, range, criterion. |

## Use Cases

### [[Top Performance by Category]]

**Scenario:** Find the highest sales figure, best score, or peak performance within specific categories or segments.

**Implementation:**
```
=MAXIFS(SalesData[Revenue], SalesData[Region], "Northeast", SalesData[Year], 2025)
```

**Business Application:** Identify top performers within segments, set regional benchmarks, understand peak performance by category. "What's our best month in the East region?"

**Technical Details:** Combine with INDEX/MATCH to find WHO achieved the maximum, not just the value. Use COUNTIFS to verify the criteria actually match rows before relying on the MAXIFS result.

---

### [[Peak Value Analysis with Time Constraints]]

**Scenario:** Find maximum values within specific time periods for trend analysis and peak identification.

**Implementation:**
```
=MAXIFS(Readings[Temperature], Readings[Date], ">="&FirstOfMonth, Readings[Date], "<="&LastOfMonth, Readings[Station], "Main")
```

**Business Application:** Peak demand identification for capacity planning, highest temperature/pressure readings for equipment limits, maximum traffic volumes for infrastructure design.

**Technical Details:** Create a summary table with time periods and use MAXIFS to find peaks for each period. Compare peaks across periods for trend analysis.

---

### [[Competitive Analysis - Best in Class]]

**Scenario:** Identify the highest value among competitors, product lines, or market segments.

**Implementation:**
```
=MAXIFS(Products[Price], Products[Category], "Premium", Products[Competitor], "<>OurBrand")
```

**Business Application:** Competitive pricing analysis, market positioning, product gap identification. "What's the highest price our competitors charge in the Premium category?"

**Technical Details:** Use exclusion criteria (`<>`) to compare against competition. Combine with MINIFS to see the range of competitor offerings.

---

### [[Quality Control - Upper Limits]]

**Scenario:** Find maximum measurements to verify they're within acceptable upper control limits.

**Implementation:**
```
=MAXIFS(Measurements[Value], Measurements[BatchID], CurrentBatch, Measurements[TestType], "Pressure")
```

**Business Application:** Manufacturing quality control, process monitoring, compliance verification. Alert if maximum exceeds specification limits.

**Technical Details:** Use with conditional formatting: `=MAXIFS(...)>UpperLimit` to highlight batches with out-of-spec readings. Combine with date criteria for time-bound quality reporting.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 2019, Microsoft 365 (not available in Excel 2016 or earlier)
- **Criteria pairs limit:** Up to 126 criteria_range/criteria pairs
- **Performance:** Optimized for large datasets
- **Legacy alternative:** `=MAX(IF(conditions, range))` as array formula (Ctrl+Shift+Enter)
- **Wildcards:** Full support for `*`, `?`, and `~` escape

### Google Sheets
- **Availability:** All versions (has been available longer than in Excel)
- **Criteria pairs limit:** Practically unlimited
- **Performance:** Efficient for typical use; may slow on very large datasets
- **Array behavior:** Works within ARRAYFORMULA context
- **Wildcards:** Full support matching Excel behavior

### Both Platforms
- Max_range comes FIRST (same as SUMIFS)
- All ranges must have identical dimensions
- Uses AND logic exclusively (all criteria must match)
- Case-insensitive text matching
- Returns 0 when no matches found (not an error)
- Empty cells in max_range are ignored (not treated as 0)

## Tips and Best Practices

1. **Verify your Excel version:** MAXIFS is not available in Excel 2016 or earlier. Use `=MAX(IF(condition, range))` as an array formula for older versions.

2. **Handle the "0 when nothing matches" behavior:** MAXIFS returns 0 when no rows match, which can be misleading. Use: `=IF(COUNTIFS(criteria_ranges, criteria)>0, MAXIFS(...), "No matches")`.

3. **Use named ranges for readability:** `=MAXIFS(Sales, Region, "East", Year, 2025)` is clearer than `=MAXIFS(D2:D1000, A2:A1000, "East", C2:C1000, 2025)`.

4. **Test criteria independently:** If MAXIFS returns unexpected results, use COUNTIFS with the same criteria to verify how many rows match.

5. **For "top N within category," combine with LARGE:** MAXIFS gives only the single maximum. For second or third highest within a category, you need LARGE with FILTER: `=LARGE(FILTER(Range, Condition), 2)`.

6. **Remember all criteria use AND logic:** For OR logic (max where A="East" OR A="West"), add separate MAXIFS: `=MAX(MAXIFS(...,"East"), MAXIFS(...,"West"))`.

7. **Keep ranges aligned:** All criteria ranges must start and end on the same rows as max_range. Misaligned ranges cause #VALUE! errors.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MAX]] | Maximum without conditions | When you want the overall maximum, no filtering needed |
| [[MINIFS]] | Minimum with conditions | When you need the conditional minimum, not maximum |
| [[SUMIFS]] | Sum with multiple conditions | When you need the total, not the largest value |
| [[AVERAGEIFS]] | Average with conditions | When you need the mean, not the extreme |
| [[LARGE]] | Nth largest value | When you need second, third, etc. largest (unconditional) |

### Commonly Used Together

**[[MINIFS]]** - Find both extremes

*Get range within category:*
```
=MAXIFS(Values, Category, "A") - MINIFS(Values, Category, "A")
```
Shows the spread of values within a filtered subset.

---

**[[COUNTIFS]]** - Verify matches exist

*Handle zero-match scenarios:*
```
=IF(COUNTIFS(Region,"East",Year,2025)>0, MAXIFS(Sales,Region,"East",Year,2025), "No data")
```
Prevents misleading 0 results when criteria don't match any rows.

---

**[[INDEX]]/[[MATCH]]** - Find what achieved the maximum

*Return associated data:*
```
=INDEX(Names, MATCH(MAXIFS(Scores,Category,"A"), IF(Category="A",Scores), 0))
```
Locates the row with the conditional maximum.

---

**[[FILTER]]** - Modern alternative

*More flexible filtering:*
```
=MAX(FILTER(Values, (Region="East")*(Year=2025)))
```
FILTER with MAX offers more control, including OR logic with `+` instead of `*`.

---

**[[SUMIFS]]** - Related conditional aggregation

*Use together for weighted analysis:*
```
=MAXIFS(UnitPrice, Product, "Widget") vs. =SUMIFS(Revenue, Product, "Widget")
```
Compare peak price to total revenue for the same category.

## Official Documentation

- **Microsoft Excel:** [MAXIFS function](https://support.microsoft.com/en-us/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883)
- **Google Sheets:** [MAXIFS function](https://support.google.com/docs/answer/7013817)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 2019 | 2019 | Initial release |
| Microsoft 365 | Continuous | Available in all 365 versions |
| Excel 2016 | Not available | Use MAX/IF array formula instead |
| Google Sheets | ~2017 | Available before Excel implementation |

---

*Last updated: 2026-01-10*
