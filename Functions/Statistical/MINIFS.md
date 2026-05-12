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
- Conditional Minimum
- Minimum If Condition
- Min With Criteria
tags:
- minimum
- conditional
- multi-criteria
- filtering
- extremes
- AND-logic
---

# MINIFS

## Description

**MINIFS** returns the minimum value from a range based on one or more conditions. It's the conditional version of MIN—instead of finding the smallest value in an entire range, it finds the smallest value only among rows that match all specified criteria. "What's the lowest price in the Electronics category?" or "What's the minimum lead time for Priority orders?"—these are MINIFS questions.

The syntax mirrors MAXIFS and follows the SUMIFS pattern: min_range comes first, followed by pairs of criteria_range and criteria. All criteria use AND logic—a value is only considered if its row matches every specified condition. This differs from MIN, which has no built-in filtering and simply returns the smallest value from the entire range.

**MINIFS is relatively new, introduced alongside MAXIFS in Excel 2019 and Microsoft 365.** Before MINIFS, conditional minimums required array formulas: `=MIN(IF(criteria_range=criterion, min_range))` entered with Ctrl+Shift+Enter. MINIFS provides a cleaner, non-array alternative. Google Sheets has supported MINIFS for longer, so cross-platform compatibility is generally good.

**MINIFS returns 0 when no values match the criteria.** This behavior is particularly problematic for minimums—0 often looks like a valid small value when it actually indicates no matches. A "lowest price" of $0 probably means your criteria didn't match anything, not that something is free. Always validate with COUNTIFS or wrap with IF to handle zero-match scenarios.

## Syntax

> [!f(x)] MINIFS Syntax
>
> ```
> =MINIFS(min_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `min_range` | Yes | The range of cells from which to find the minimum. Must contain numeric values. Same dimensions required as all criteria_ranges. |
| `criteria_range1` | Yes | The first range to evaluate against criteria1. Must be the same size as min_range. Contains the values to test against the first criterion. |
| `criteria1` | Yes | The condition for criteria_range1. Can be number, text, cell reference, expression with operators ("<50", "<>Cancelled"), or wildcard pattern ("*Ltd"). |
| `criteria_range2, criteria2, ...` | No | Additional pairs of ranges and criteria. Each range must match min_range dimensions. Up to 126 additional pairs in Excel. |

### Return Value

Returns a single numeric value representing the smallest number in min_range where ALL corresponding criteria_range cells match their respective criteria. Returns 0 if no cells match all criteria. Returns an error if ranges have mismatched sizes or arguments are invalid.

## Examples

> [!f(x)] MINIFS Examples

### Example 1: Minimum with One Condition
```
=MINIFS(C2:C100, A2:A100, "Active")
```
**Result:** Smallest value in C where A equals "Active"

**Explanation:** The simplest MINIFS pattern. Finds the lowest value in column C, but only for rows where column A contains "Active". Inactive rows are ignored.

---

### Example 2: Minimum with Two Conditions
```
=MINIFS(D2:D500, A2:A500, "Electronics", B2:B500, "InStock")
```
**Result:** Smallest value in D where A is "Electronics" AND B is "InStock"

**Explanation:** Both conditions must match. Finds the minimum price for Electronics products currently in stock.

---

### Example 3: Using Cell References as Criteria
```
=MINIFS(Prices, Category, G1, Supplier, H1, Status, I1)
```
**Result:** Minimum price for category/supplier/status specified in G1, H1, I1

**Explanation:** Dynamic criteria from cells. Change the filter cells and the minimum updates automatically. Essential for interactive price comparison tools.

---

### Example 4: Minimum with Numeric Comparison
```
=MINIFS(C2:C200, B2:B200, ">=10", A2:A200, "Available")
```
**Result:** Smallest value in C where B is at least 10 AND A is "Available"

**Explanation:** Combines text matching with numeric filtering. Finds the lowest price among available products with quantity of 10 or more.

---

### Example 5: Minimum within Date Range
```
=MINIFS(E2:E1000, D2:D1000, ">="&DATE(2025,1,1), D2:D1000, "<="&DATE(2025,3,31))
```
**Result:** Minimum value in E where dates in D fall within Q1 2025

**Explanation:** Apply the same criteria_range twice with different operators for date ranges. Finds the lowest value during the specified quarter.

---

### Example 6: Minimum with Dynamic Date Range
```
=MINIFS(Prices, Dates, ">="&StartDate, Dates, "<="&EndDate, Vendor, "Preferred")
```
**Result:** Minimum preferred vendor price within date range

**Explanation:** Combines date filtering with vendor filtering. StartDate and EndDate from named cells for user control.

---

### Example 7: Minimum Using Wildcards
```
=MINIFS(B2:B100, A2:A100, "Express*")
```
**Result:** Smallest value in B where A starts with "Express"

**Explanation:** Wildcards work in MINIFS. Matches "Express", "Express Shipping", "Express Premium", etc.

---

### Example 8: Minimum Excluding Specific Values
```
=MINIFS(D2:D300, C2:C300, "<>Discontinued", B2:B300, "<>OutOfStock")
```
**Result:** Minimum in D excluding discontinued and out-of-stock items

**Explanation:** Use `<>` to exclude values. Finds lowest price among currently available products only.

---

### Example 9: Minimum by Month (Previous Month)
```
=MINIFS(B2:B500, A2:A500, ">="&EOMONTH(TODAY(),-2)+1, A2:A500, "<="&EOMONTH(TODAY(),-1))
```
**Result:** Minimum value in B for the previous month

**Explanation:** Uses EOMONTH to calculate previous month boundaries. Finds the lowest value from last month's data.

---

### Example 10: Minimum with Boolean Criteria
```
=MINIFS(C2:C100, D2:D100, TRUE, A2:A100, "Standard")
```
**Result:** Minimum in C where D is TRUE (checked) AND A is "Standard"

**Explanation:** Checkbox TRUE/FALSE values work as criteria. Finds minimum among checked Standard items.

---

### Example 11: Minimum in Numeric Range
```
=MINIFS(C2:C200, B2:B200, ">=1000", B2:B200, "<=5000")
```
**Result:** Minimum in C where B is between 1000 and 5000 inclusive

**Explanation:** Use same range twice for "between" logic. Finds minimum among mid-range values only.

---

### Example 12: Minimum Greater Than Zero
```
=MINIFS(B2:B100, B2:B100, ">0", A2:A100, "Active")
```
**Result:** Smallest positive value in B for Active items

**Explanation:** Exclude zeros from consideration. Useful when 0 represents missing data rather than a valid value.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Ranges have different sizes | All criteria_ranges must have exactly the same dimensions as min_range. Verify row counts match. |
| `#NAME?` | Misspelled function, or function not available in your Excel version | MINIFS requires Excel 2019 or later. Check spelling and Excel version. |
| `0 unexpected` | No rows match all criteria | MINIFS returns 0 when nothing matches. This is especially misleading for minimums. Use COUNTIFS to verify. |
| `#REF!` | Referenced cells have been deleted | Check if any cells in your ranges have been removed. |
| `Wrong result` | Criteria format mismatch | Text "100" won't match number 100. Check data types and hidden spaces. |
| `Negative when expecting positive` | Data contains negatives | MINIFS finds the actual minimum, including negatives. Add ">0" criterion if needed. |

## Use Cases

### [[Price Comparison and Lowest Cost Finding]]

**Scenario:** Find the lowest price point within categories, vendors, or conditions for procurement decisions.

**Implementation:**
```
=MINIFS(Catalog[Price], Catalog[Category], "Laptops", Catalog[InStock], TRUE)
```

**Business Application:** Procurement optimization, competitive pricing analysis, budget planning. "What's the cheapest laptop we can order that's currently in stock?"

**Technical Details:** Combine with INDEX/MATCH to find the product name, not just the price: identify what offers the best value. Add quality or rating criteria to avoid finding cheap but unsuitable options.

---

### [[Lead Time and Delivery Analysis]]

**Scenario:** Find minimum delivery times, shortest lead times, or fastest processing among filtered options.

**Implementation:**
```
=MINIFS(Orders[DeliveryDays], Orders[Carrier], "Express", Orders[Destination], "International")
```

**Business Application:** Supply chain optimization, customer promise management, service level determination. "What's the fastest we can deliver internationally with Express carriers?"

**Technical Details:** Use date filtering to find recent minimums (lead times may have changed). Combine with MAXIFS to see the range of delivery times for capacity planning.

---

### [[Threshold and Floor Value Identification]]

**Scenario:** Identify minimum acceptable values, floor prices, or baseline measurements within categories.

**Implementation:**
```
=MINIFS(Bids[Amount], Bids[Status], "Approved", Bids[Vendor], VendorName)
```

**Business Application:** Bid analysis, price floor identification, baseline performance measurement. "What's the lowest approved bid from this vendor?"

**Technical Details:** Minimum values often represent floor constraints or worst-case scenarios. Document why certain minimums exist and whether they're outliers or systematic.

---

### [[Earliest Date Within Categories]]

**Scenario:** Find the earliest date (as minimum date serial number) among filtered records.

**Implementation:**
```
=MINIFS(Orders[OrderDate], Orders[Customer], CustomerID, Orders[Status], "Completed")
```

**Business Application:** Customer first-order analysis, earliest occurrence identification, historical record lookup. "When was this customer's first completed order?"

**Technical Details:** Dates are numbers, so MINIFS finds the earliest (smallest) date. Format the result as a date. Use for customer tenure, product launch dates, first occurrence tracking.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 2019, Microsoft 365 (not available in Excel 2016 or earlier)
- **Criteria pairs limit:** Up to 126 criteria_range/criteria pairs
- **Performance:** Optimized for large datasets
- **Legacy alternative:** `=MIN(IF(conditions, range))` as array formula (Ctrl+Shift+Enter)
- **Wildcards:** Full support for `*`, `?`, and `~` escape

### Google Sheets
- **Availability:** All versions (available before Excel implementation)
- **Criteria pairs limit:** Practically unlimited
- **Performance:** Efficient for typical use; may slow on very large datasets
- **Array behavior:** Works within ARRAYFORMULA context
- **Wildcards:** Full support matching Excel behavior

### Both Platforms
- Min_range comes FIRST (same as SUMIFS pattern)
- All ranges must have identical dimensions
- Uses AND logic exclusively (all criteria must match)
- Case-insensitive text matching
- Returns 0 when no matches found (not an error)
- Empty cells in min_range are ignored (not treated as 0)

## Tips and Best Practices

1. **Verify your Excel version:** MINIFS is not available in Excel 2016 or earlier. Use `=MIN(IF(condition, range))` as an array formula for older versions.

2. **Handle the "0 when nothing matches" very carefully:** For minimums, 0 often looks valid. Always verify: `=IF(COUNTIFS(criteria_ranges, criteria)>0, MINIFS(...), "No matches")`.

3. **Exclude zeros when they mean "no data":** If 0 represents missing information, add `min_range, ">0"` as an additional criterion: `=MINIFS(Prices, Prices, ">0", Category, "Electronics")`.

4. **Use named ranges for readability:** `=MINIFS(LeadTime, Carrier, "Express", Region, "East")` is much clearer than cell reference notation.

5. **Test criteria independently:** If MINIFS returns unexpected results, use COUNTIFS with the same criteria to verify how many rows match.

6. **For "bottom N within category," combine with SMALL:** MINIFS gives only the single minimum. For second or third smallest within a category, use SMALL with FILTER: `=SMALL(FILTER(Range, Condition), 2)`.

7. **Watch for data type mismatches:** Text "100" won't match number 100. Numbers stored as text are a common source of "why doesn't this match?" confusion.

8. **Combine with MAXIFS for range analysis:** `MAXIFS(...) - MINIFS(...)` shows the spread within a category, useful for variability analysis.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MIN]] | Minimum without conditions | When you want the overall minimum, no filtering needed |
| [[MAXIFS]] | Maximum with conditions | When you need the conditional maximum, not minimum |
| [[SUMIFS]] | Sum with multiple conditions | When you need the total, not the smallest value |
| [[AVERAGEIFS]] | Average with conditions | When you need the mean, not the extreme |
| [[SMALL]] | Nth smallest value | When you need second, third, etc. smallest (unconditional) |

### Commonly Used Together

**[[MAXIFS]]** - Find both extremes

*Get range within category:*
```
=MAXIFS(Prices, Category, "A") - MINIFS(Prices, Category, "A")
```
Shows the price spread within a filtered category.

---

**[[COUNTIFS]]** - Verify matches exist

*Handle zero-match scenarios:*
```
=IF(COUNTIFS(Category,"Electronics",InStock,TRUE)>0, MINIFS(Price,Category,"Electronics",InStock,TRUE), "None available")
```
Critical for MINIFS since 0 return value is ambiguous.

---

**[[INDEX]]/[[MATCH]]** - Find what achieved the minimum

*Return associated data:*
```
=INDEX(Products, MATCH(MINIFS(Prices,Category,"A"), IF(Category="A",Prices), 0))
```
Locates the product with the conditional minimum price.

---

**[[FILTER]]** - Modern alternative

*More flexible filtering:*
```
=MIN(FILTER(Prices, (Category="Electronics")*(InStock=TRUE)))
```
FILTER with MIN offers more control, including OR logic with `+` instead of `*`.

---

**[[AVERAGEIFS]]** - Context for the minimum

*Compare minimum to average:*
```
=AVERAGEIFS(Prices, Category, "A") - MINIFS(Prices, Category, "A")
```
Shows how far below average the minimum falls within the category.

## Official Documentation

- **Microsoft Excel:** [MINIFS function](https://support.microsoft.com/en-us/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599)
- **Google Sheets:** [MINIFS function](https://support.google.com/docs/answer/7014761)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 2019 | 2019 | Initial release alongside MAXIFS |
| Microsoft 365 | Continuous | Available in all 365 versions |
| Excel 2016 | Not available | Use MIN/IF array formula instead |
| Google Sheets | ~2017 | Available before Excel implementation |

---

*Last updated: 2026-01-10*
