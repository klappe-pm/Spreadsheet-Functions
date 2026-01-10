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
- Maximum
- Largest Value
- Max Function
tags:
- maximum
- aggregation
- extremes
- statistics
- comparison
---

# MAX

## Description

**MAX** returns the largest numeric value from a set of numbers. It's the fundamental "find the biggest" function—give it a range, a list of values, or any combination, and it returns the single largest number. From finding the highest sales figure to identifying peak performance metrics, MAX is essential for any analysis involving extremes.

The function ignores text values and empty cells within cell references, making it safe to use on ranges containing mixed data. However, there's an important nuance: if you type text or logical values directly as arguments (not cell references), the behavior differs. TRUE becomes 1, FALSE becomes 0, and text typically causes an error. This rarely matters in practice since most MAX calls use cell ranges.

**MAX returns 0 when given an empty range or all non-numeric values.** This can be misleading—if you expect a positive result but get 0, check whether your data actually contains numbers. For ranges that might be empty, consider wrapping with IF to show a more meaningful result. Also note that MAX only considers numeric values; to include logical and text representations of numbers, use MAXA instead.

**For conditional maximums, use MAXIFS.** Standard MAX ignores conditions—it simply finds the largest value in the entire range. When you need "the highest value WHERE condition is met" (like the maximum sale in the East region), MAXIFS or a MAX/IF array combination is required.

## Syntax

> [!f(x)] MAX Syntax
>
> ```
> =MAX(number1, [number2], [number3], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number1` | Yes | First number, cell reference, or range to evaluate. Can be a single value (42), a cell (A1), a range (A1:A100), or a named range (SalesData). |
| `number2, number3, ...` | No | Additional numbers, cells, or ranges to include. Up to 255 arguments in Excel, practically unlimited in Google Sheets. Mix ranges with individual values as needed. |

### Return Value

Returns a single numeric value representing the largest number among all arguments. Returns 0 if all arguments are empty, text, or logical values. Returns an error if any argument is an error value.

## Examples

> [!f(x)] MAX Examples

### Example 1: Maximum of a Range
```
=MAX(A1:A100)
```
**Result:** The largest value in cells A1 through A100

**Explanation:** The most common MAX pattern. Scans all 100 cells and returns the single largest number. Text and blanks are ignored.

---

### Example 2: Maximum of Listed Values
```
=MAX(10, 25, 5, 42, 18)
```
**Result:** 42

**Explanation:** Direct value comparison. Useful for quick calculations or when values come from different sources that aren't in a range.

---

### Example 3: Maximum Across Multiple Ranges
```
=MAX(A1:A50, C1:C50, E1:E50)
```
**Result:** Largest value across all three ranges

**Explanation:** MAX accepts multiple range arguments. This finds the overall maximum across three non-contiguous columns—useful for consolidated analysis.

---

### Example 4: Maximum of Entire Column
```
=MAX(B:B)
```
**Result:** Largest value in column B

**Explanation:** Full-column reference ensures all current and future values are included. Watch for headers—if row 1 contains a number, it's included. Consider `=MAX(B2:B)` to skip headers.

---

### Example 5: Maximum with Mixed Arguments
```
=MAX(A1:A20, 100, B5, C1:C10)
```
**Result:** Largest among range A1:A20, the number 100, cell B5, and range C1:C10

**Explanation:** Mix ranges, individual cells, and literal numbers freely. MAX compares all values regardless of source type.

---

### Example 6: Handling Text in Range
```
=MAX(A1:A5) where A1:A5 contains [50, "High", 30, "", 75]
```
**Result:** 75

**Explanation:** MAX ignores "High" (text) and the empty cell. Only compares 50, 30, and 75, returning 75. This makes MAX safe for ranges with labels or missing data.

---

### Example 7: Finding Maximum Date
```
=MAX(DateColumn)
```
**Result:** The most recent (largest) date

**Explanation:** Dates are numbers in Excel and Sheets, so MAX finds the most recent date. Result is a date serial number—format the result cell as a date to display properly.

---

### Example 8: Maximum of Negative Numbers
```
=MAX(-5, -10, -3, -8)
```
**Result:** -3

**Explanation:** MAX works correctly with negative numbers. -3 is the largest because it's closest to zero (least negative).

---

### Example 9: Combining with Other Functions
```
=MAX(A1:A10) - MIN(A1:A10)
```
**Result:** The range (difference between highest and lowest)

**Explanation:** MAX and MIN together calculate the range of a dataset—a basic measure of variability. Useful for quality control and statistical analysis.

---

### Example 10: Maximum with IF for Conditional Logic (Legacy)
```
=MAX(IF(A1:A100="East", B1:B100))
```
(Enter with Ctrl+Shift+Enter in older Excel)

**Result:** Largest value in B where corresponding A equals "East"

**Explanation:** Before MAXIFS existed, this array formula provided conditional maximum. Modern Excel/Sheets evaluate this automatically; older versions need CSE entry.

---

### Example 11: Maximum Across Sheets
```
=MAX(Sheet1!A:A, Sheet2!A:A, Sheet3!A:A)
```
**Result:** Largest value across column A of three sheets

**Explanation:** Cross-sheet references work within MAX. Useful for finding overall maximum across monthly or regional data stored in separate sheets.

---

### Example 12: Empty Range Behavior
```
=MAX(D1:D10) where D1:D10 is empty or all text
```
**Result:** 0

**Explanation:** When no numeric values exist, MAX returns 0—not an error. This can be misleading if you expect positive values. Use IF to handle: `=IF(COUNT(D1:D10)>0, MAX(D1:D10), "No data")`.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `0 unexpected` | Range is empty or contains only text/blanks | Verify range contains numeric data. Check for numbers stored as text (green triangle indicator). |
| `#VALUE!` | Direct text argument like `=MAX("text", 5)` | Only use numbers in direct arguments. Text in cell references is ignored, but text as direct arguments causes errors. |
| `#REF!` | Referenced cells have been deleted | Check if any cells in your range have been removed. |
| `#NAME?` | Misspelled function or undefined named range | Verify spelling. If using named ranges, ensure they're defined. |
| `Dates not comparing correctly` | Dates stored as text | Ensure dates are actual date values. Use DATEVALUE to convert text dates. |
| `Wrong result` | Included header row with numeric value | Verify range doesn't include headers. Use A2:A100 instead of A:A if header might be numeric. |

## Use Cases

### [[Performance Benchmarking]]

**Scenario:** Find the highest sales figure, best production rate, or peak performance metric for comparison.

**Implementation:**
```
=MAX(SalesData[Revenue])
```
Or for specific time period:
```
=MAXIFS(SalesData[Revenue], SalesData[Year], 2025)
```

**Business Application:** Setting benchmarks, identifying top performers, establishing ceiling values for goals. "Our best month was X" statements come from MAX.

**Technical Details:** Combine with INDEX/MATCH to find WHO achieved the maximum, not just the value. `=INDEX(Names, MATCH(MAX(Scores), Scores, 0))` returns the name associated with the highest score.

---

### [[Data Validation and Quality Control]]

**Scenario:** Verify data falls within expected ranges by checking if maximum exceeds thresholds.

**Implementation:**
```
=IF(MAX(Measurements) > UpperLimit, "Out of Spec", "Within Spec")
```

**Business Application:** Manufacturing quality control, data entry validation, compliance monitoring. Automatically flag when any value exceeds acceptable limits.

**Technical Details:** Create alerts with conditional formatting based on MAX exceeding thresholds. Use for real-time monitoring dashboards.

---

### [[Financial Analysis - Peak Values]]

**Scenario:** Find the highest stock price, maximum daily transaction, or peak account balance.

**Implementation:**
```
=MAX(FILTER(StockPrices, Dates>=StartDate, Dates<=EndDate))
```
Or simpler:
```
=MAXIFS(StockPrices, Dates, ">="&StartDate, Dates, "<="&EndDate)
```

**Business Application:** Investment analysis, cash flow planning, credit limit assessment. Understanding peak values helps with risk management and capacity planning.

**Technical Details:** For time-series data, combine with date filtering to find peaks within specific periods. Use with LARGE for "top N" analysis.

---

### [[Scheduling and Resource Planning]]

**Scenario:** Determine peak demand, maximum concurrent users, or highest resource utilization.

**Implementation:**
```
=MAX(HourlyDemand)
```
With time-of-day analysis:
```
=MAXIFS(Demand, Hour, ">=9", Hour, "<=17")
```

**Business Application:** Capacity planning, staffing decisions, infrastructure sizing. Peak values drive resource requirements even if they occur briefly.

**Technical Details:** Consider using LARGE to see the top 5-10 values, not just the absolute maximum, for more robust capacity planning that accounts for outliers.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (original function from Excel 1.0)
- **Argument limit:** 255 arguments maximum
- **Performance:** Highly optimized for large ranges
- **Array context:** In Excel 365, MAX can work within dynamic array formulas
- **MAXIFS:** Available in Excel 2019 and Microsoft 365

### Google Sheets
- **Availability:** All versions
- **Argument limit:** Practically unlimited (30,000+ cells per argument)
- **Performance:** Efficient for typical use; may slow on very large datasets
- **MAXIFS:** Fully supported
- **Array behavior:** Works with ARRAYFORMULA for expanded results

### Both Platforms
- Text and empty cells in ranges are ignored
- Returns 0 for empty/all-text ranges
- Errors propagate (one error cell causes MAX to error)
- Dates are compared correctly (larger date = more recent)
- Logical values in cell references are ignored

## Tips and Best Practices

1. **Use MAXIFS for conditional maximums:** Don't struggle with MAX/IF array formulas. `=MAXIFS(Values, Category, "Electronics")` is cleaner and faster than `=MAX(IF(Category="Electronics", Values))`.

2. **Combine with INDEX/MATCH to find the source:** `=INDEX(A:A, MATCH(MAX(B:B), B:B, 0))` returns the value from column A in the row where column B has its maximum.

3. **Handle empty ranges gracefully:** MAX returns 0 for empty ranges, which can be misleading. Use `=IF(COUNT(Range)>0, MAX(Range), "No data")` for clarity.

4. **Be cautious with full-column references:** `=MAX(A:A)` includes row 1. If your header could be interpreted as a number, use `=MAX(A2:A)` in Sheets or `=MAX(A2:A1048576)` in Excel.

5. **For "top N" values, use LARGE:** MAX only returns the single largest. `=LARGE(Range, 2)` returns the second largest, `=LARGE(Range, 3)` the third, etc.

6. **Remember MAX is not conditional by default:** Unlike SUMIF which has built-in criteria, MAX requires MAXIFS or array formulas for conditional logic.

7. **Use MAXA if logical values matter:** Standard MAX ignores TRUE/FALSE in cell references. MAXA treats TRUE as 1 and FALSE as 0.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MIN]] | Returns smallest value | When you need the minimum, not maximum |
| [[LARGE]] | Returns nth largest value | When you need second-largest, third-largest, etc. |
| [[MAXA]] | MAX including text and logical values | When TRUE/FALSE should be counted (as 1/0) |
| [[MAXIFS]] | Maximum with conditions | When you need maximum within a subset matching criteria |
| [[AGGREGATE]] | Flexible aggregation with options | When you need to ignore errors or hidden rows |

### Commonly Used Together

**[[MIN]]** - Find the range of values

*Calculate data range:*
```
=MAX(A1:A100) - MIN(A1:A100)
```
The difference between max and min shows the spread of your data.

---

**[[INDEX]]/[[MATCH]]** - Find what achieved the maximum

*Return the name/ID associated with highest value:*
```
=INDEX(Names, MATCH(MAX(Scores), Scores, 0))
```
Locates the row with the maximum and returns corresponding data.

---

**[[IF]]** - Conditional logic with maximum

*Compare values to maximum:*
```
=IF(A1=MAX(A:A), "Highest", "Not highest")
```
Identify which cell contains the maximum value.

---

**[[AVERAGE]]** - Context for the maximum

*Show how far max is from average:*
```
=MAX(A:A) - AVERAGE(A:A)
```
Measures how exceptional the maximum is compared to typical values.

---

**[[MAXIFS]]** - Conditional maximum

*Maximum with criteria:*
```
=MAXIFS(Sales, Region, "East", Year, 2025)
```
Finds largest value only among rows matching all criteria.

## Official Documentation

- **Microsoft Excel:** [MAX function](https://support.microsoft.com/en-us/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098)
- **Google Sheets:** [MAX function](https://support.google.com/docs/answer/3094013)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function |
| Excel 2019/365 | 2019+ | MAXIFS function added as companion |
| Google Sheets | Original launch | Full compatibility with Excel |

---

*Last updated: 2026-01-10*
