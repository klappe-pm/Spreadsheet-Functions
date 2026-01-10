---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics:
- aggregation
- extremes
- descriptive-statistics
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Minimum
- Smallest Value
- Min Function
tags:
- minimum
- aggregation
- extremes
- statistics
- comparison
---

# MIN

## Description

**MIN** returns the smallest numeric value from a set of numbers. It's the counterpart to MAX—give it a range or list of values, and it returns the single smallest number. From finding the lowest price to identifying the earliest date, MIN is fundamental to any analysis involving minimum thresholds, floor values, or worst-case scenarios.

Like MAX, MIN ignores text values and empty cells within cell references. This makes it safe to use on ranges containing mixed data without preprocessing. The function scans through all provided values and returns only the single smallest one. For finding multiple small values (second smallest, third smallest), use the SMALL function instead.

**MIN returns 0 when given an empty range or all non-numeric values.** This is a critical gotcha—0 might look like a valid minimum when your range actually contained no numbers. In contexts where 0 is a plausible minimum, this can mask data issues. Consider wrapping with IF and COUNT to detect empty ranges: `=IF(COUNT(Range)>0, MIN(Range), "No data")`.

**For conditional minimums, use MINIFS.** Standard MIN evaluates the entire range unconditionally. When you need "the smallest value WHERE condition is met" (like the minimum price in the Electronics category), you need MINIFS or a MIN/IF array formula combination.

## Syntax

> [!f(x)] MIN Syntax
>
> ```
> =MIN(number1, [number2], [number3], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number1` | Yes | First number, cell reference, or range to evaluate. Can be a single value (42), a cell (A1), a range (A1:A100), or a named range (PriceData). |
| `number2, number3, ...` | No | Additional numbers, cells, or ranges to include. Up to 255 arguments in Excel, practically unlimited in Google Sheets. Mix ranges with individual values as needed. |

### Return Value

Returns a single numeric value representing the smallest number among all arguments. Returns 0 if all arguments are empty, text, or logical values. Returns an error if any argument is an error value.

## Examples

> [!f(x)] MIN Examples

### Example 1: Minimum of a Range
```
=MIN(A1:A100)
```
**Result:** The smallest value in cells A1 through A100

**Explanation:** The standard MIN pattern. Scans all 100 cells and returns the single smallest number. Text and blanks are ignored—only numeric values are compared.

---

### Example 2: Minimum of Listed Values
```
=MIN(50, 12, 87, 3, 45)
```
**Result:** 3

**Explanation:** Direct value comparison. The function evaluates all five numbers and returns the smallest.

---

### Example 3: Minimum Across Multiple Ranges
```
=MIN(A1:A50, C1:C50, E1:E50)
```
**Result:** Smallest value across all three ranges

**Explanation:** MIN accepts multiple range arguments. Finds the overall minimum across three non-contiguous columns—useful for consolidated analysis across departments or categories.

---

### Example 4: Minimum of Entire Column
```
=MIN(B:B)
```
**Result:** Smallest value in column B

**Explanation:** Full-column reference includes all values. Be aware this includes row 1—if your header is a number (like a year), it might become the minimum. Use `=MIN(B2:B)` to skip headers.

---

### Example 5: Minimum with Mixed Arguments
```
=MIN(A1:A20, 0, B5, C1:C10)
```
**Result:** Smallest among range A1:A20, zero, cell B5, and range C1:C10

**Explanation:** Including a literal 0 guarantees the result won't exceed 0. Useful when you want to cap values at zero (though MAX with 0 is more common for that).

---

### Example 6: Handling Text in Range
```
=MIN(A1:A5) where A1:A5 contains [50, "Low", 30, "", 75]
```
**Result:** 30

**Explanation:** MIN ignores "Low" (text) and the empty cell. Only compares 50, 30, and 75, returning 30. Safe for ranges with labels or missing data.

---

### Example 7: Finding Earliest Date
```
=MIN(DateColumn)
```
**Result:** The earliest (smallest) date

**Explanation:** Since dates are numbers internally (days since epoch), MIN finds the earliest date. Format the result cell as a date to see it properly.

---

### Example 8: Minimum of Negative Numbers
```
=MIN(-5, -10, -3, -8)
```
**Result:** -10

**Explanation:** MIN works correctly with negatives. -10 is the smallest because it's furthest from zero (most negative).

---

### Example 9: Combining with MAX for Range Calculation
```
=MAX(A1:A10) - MIN(A1:A10)
```
**Result:** The range (difference between highest and lowest)

**Explanation:** MAX minus MIN gives the spread of values—a basic measure of variability. Larger range indicates more variation in the data.

---

### Example 10: Minimum with IF for Conditional Logic (Legacy)
```
=MIN(IF(A1:A100="Active", B1:B100))
```
(Enter with Ctrl+Shift+Enter in older Excel)

**Result:** Smallest value in B where corresponding A equals "Active"

**Explanation:** Pre-MINIFS approach for conditional minimum. Modern Excel/Sheets evaluate automatically; older versions need CSE entry. Use MINIFS for cleaner syntax.

---

### Example 11: Minimum Across Sheets
```
=MIN(Jan!C:C, Feb!C:C, Mar!C:C)
```
**Result:** Smallest value across column C of three sheets

**Explanation:** Cross-sheet references work within MIN. Useful for finding the lowest monthly figure, worst performance, etc., across time-based sheets.

---

### Example 12: Empty Range Behavior
```
=MIN(D1:D10) where D1:D10 is empty or all text
```
**Result:** 0

**Explanation:** When no numeric values exist, MIN returns 0—not an error. This can be misleading since 0 might look like a valid minimum. Use `=IF(COUNT(D1:D10)>0, MIN(D1:D10), "No data")` to handle gracefully.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `0 unexpected` | Range is empty or contains only text/blanks | Verify range contains numeric data. 0 from empty range is a common gotcha. |
| `#VALUE!` | Direct text argument like `=MIN("text", 5)` | Only use numbers in direct arguments. Text in cell references is ignored, but direct text causes errors. |
| `#REF!` | Referenced cells have been deleted | Check if any cells in your range have been removed. |
| `#NAME?` | Misspelled function or undefined named range | Verify spelling. Check named range definitions. |
| `Wrong date` | Dates stored as text don't compare | Ensure dates are actual date values. Use DATEVALUE to convert text dates. |
| `Positive when expecting negative` | Range has no negative values | MIN returns the smallest value present. If all values are positive, the minimum is positive. |

## Use Cases

### [[Price and Cost Analysis]]

**Scenario:** Find the lowest price point, minimum cost, or floor value for budgeting and pricing decisions.

**Implementation:**
```
=MIN(Products[Price])
```
With condition:
```
=MINIFS(Products[Price], Products[InStock], TRUE)
```

**Business Application:** Competitive pricing analysis, minimum viable pricing, cost floor identification, budget baseline establishment.

**Technical Details:** Combine with conditional formatting to highlight minimum values. Use `=A1=MIN(A:A)` as a conditional format formula to mark the cell(s) containing the minimum.

---

### [[Date Tracking - Earliest Records]]

**Scenario:** Find the earliest date in a dataset—first order, oldest record, start of a period.

**Implementation:**
```
=MIN(Orders[OrderDate])
```
Formatted result shows: 1/15/2020

**Business Application:** Customer tenure calculation, project timeline determination, data freshness assessment, historical analysis starting points.

**Technical Details:** Subtract MIN from MAX to find the span of dates: `=MAX(Dates)-MIN(Dates)` gives days between earliest and latest records.

---

### [[Performance Threshold Analysis]]

**Scenario:** Identify minimum performance levels, worst-case scenarios, or floor values for risk assessment.

**Implementation:**
```
=MIN(MonthlyRevenue)
```
Or for specific segment:
```
=MINIFS(Sales[Revenue], Sales[Region], "West")
```

**Business Application:** Worst-case scenario planning, minimum acceptable performance identification, risk quantification, warranty reserve calculations.

**Technical Details:** Use MIN in conjunction with percentiles for robust analysis. The minimum might be an outlier; PERCENTILE(Range, 0.05) shows the 5th percentile which may be more representative of "low" values.

---

### [[Inventory and Stock Management]]

**Scenario:** Find minimum stock levels, lowest inventory counts, or shortest lead times.

**Implementation:**
```
=MIN(Inventory[Quantity])
```
To find products below reorder point:
```
=IF(MIN(Inventory[Quantity]) < ReorderPoint, "Restock needed", "OK")
```

**Business Application:** Inventory monitoring, reorder point triggers, supply chain bottleneck identification, safety stock analysis.

**Technical Details:** Combine with MINIFS for location-specific analysis: `=MINIFS(Stock, Warehouse, "Main")`. Consider SMALL for seeing the lowest few values, not just the absolute minimum.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (original function from Excel 1.0)
- **Argument limit:** 255 arguments maximum
- **Performance:** Highly optimized for large ranges
- **Array context:** In Excel 365, MIN works within dynamic array formulas
- **MINIFS:** Available in Excel 2019 and Microsoft 365

### Google Sheets
- **Availability:** All versions
- **Argument limit:** Practically unlimited (30,000+ cells per argument)
- **Performance:** Efficient for typical use; may slow on massive datasets
- **MINIFS:** Fully supported
- **Array behavior:** Works with ARRAYFORMULA for expanded results

### Both Platforms
- Text and empty cells in ranges are ignored
- Returns 0 for empty/all-text ranges (not an error)
- Errors propagate (one error cell causes MIN to error)
- Dates are compared correctly (smaller date = earlier)
- Logical values in cell references are ignored

## Tips and Best Practices

1. **Use MINIFS for conditional minimums:** `=MINIFS(Values, Category, "Active")` is cleaner and faster than `=MIN(IF(Category="Active", Values))` array formulas.

2. **Handle the "0 for empty" behavior:** MIN returns 0 when ranges are empty or all text. Use `=IF(COUNT(Range)>0, MIN(Range), "No data")` to show meaningful results.

3. **Combine with INDEX/MATCH to find the source:** `=INDEX(A:A, MATCH(MIN(B:B), B:B, 0))` returns the value from column A in the row where column B has its minimum.

4. **For "bottom N" values, use SMALL:** MIN only returns the single smallest. `=SMALL(Range, 2)` returns the second smallest, `=SMALL(Range, 3)` the third, etc.

5. **Watch out for zero vs. blank:** A cell with 0 is different from an empty cell. MIN treats actual zeros as valid minimums but ignores blanks. Know your data.

6. **Be careful with full-column references:** `=MIN(A:A)` includes row 1. If your header could be a number, use `=MIN(A2:A)` in Sheets or `=MIN(A2:A1048576)` in Excel.

7. **Use MINA if logical values matter:** Standard MIN ignores TRUE/FALSE in cell references. MINA treats TRUE as 1 and FALSE as 0, which can affect the minimum.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MAX]] | Returns largest value | When you need the maximum, not minimum |
| [[SMALL]] | Returns nth smallest value | When you need second-smallest, third-smallest, etc. |
| [[MINA]] | MIN including text and logical values | When TRUE/FALSE should be counted (as 1/0) |
| [[MINIFS]] | Minimum with conditions | When you need minimum within a subset matching criteria |
| [[AGGREGATE]] | Flexible aggregation with options | When you need to ignore errors or hidden rows |

### Commonly Used Together

**[[MAX]]** - Find the range of values

*Calculate data range:*
```
=MAX(A1:A100) - MIN(A1:A100)
```
The difference shows the total spread of your data.

---

**[[INDEX]]/[[MATCH]]** - Find what achieved the minimum

*Return the name/ID associated with lowest value:*
```
=INDEX(Names, MATCH(MIN(Prices), Prices, 0))
```
Locates the row with the minimum and returns corresponding data.

---

**[[IF]]** - Conditional logic with minimum

*Compare values to minimum:*
```
=IF(A1=MIN(A:A), "Lowest", "Not lowest")
```
Identify which cell contains the minimum value.

---

**[[AVERAGE]]** - Context for the minimum

*Show how far min is from average:*
```
=AVERAGE(A:A) - MIN(A:A)
```
Measures how far below average the minimum falls.

---

**[[MINIFS]]** - Conditional minimum

*Minimum with criteria:*
```
=MINIFS(Prices, Category, "Electronics", InStock, TRUE)
```
Finds smallest value only among rows matching all criteria.

## Official Documentation

- **Microsoft Excel:** [MIN function](https://support.microsoft.com/en-us/office/min-function-61635d12-920f-4ce2-a9ab-8f0f88e1b56f)
- **Google Sheets:** [MIN function](https://support.google.com/docs/answer/3094017)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function |
| Excel 2019/365 | 2019+ | MINIFS function added as companion |
| Google Sheets | Original launch | Full compatibility with Excel |

---

*Last updated: 2026-01-10*
