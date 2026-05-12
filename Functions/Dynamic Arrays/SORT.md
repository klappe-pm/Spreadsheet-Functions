---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics:
- data-sorting
- array-ordering
- ranking
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Array Sort
- Dynamic Sort
- Sort Array
tags:
- dynamic-array
- sorting
- ordering
- ranking
- spill
---

# SORT

## Description

**SORT** is a dynamic array function that returns a sorted version of a range or array. Unlike the traditional Sort feature that rearranges your source data in place, SORT creates a new sorted output that spills into adjacent cells while leaving your original data untouched. This is transformative for reporting—your raw data stays in entry order while sorted views update automatically wherever you need them.

The function offers remarkable flexibility: sort by any column (not just the first), sort ascending or descending, and even sort by multiple columns for hierarchical ordering. `=SORT(A2:D100, 3, -1)` sorts by the third column in descending order. `=SORT(A2:D100, {2,3}, {1,-1})` sorts first by column 2 ascending, then by column 3 descending for ties—like a SQL ORDER BY clause.

**Understanding sort order:** The sort_order parameter uses 1 for ascending (A-Z, smallest-to-largest) and -1 for descending (Z-A, largest-to-smallest). This is intuitive once learned, but differs from some functions that use TRUE/FALSE. Remember: 1 = ascending (the "first" way, natural order), -1 = descending (the opposite). When omitted, SORT defaults to ascending order.

**Cross-platform parity:** SORT works nearly identically in Excel 365/2021 and Google Sheets. The main consideration is that Google Sheets has had SORT since its early days while Excel only added it with dynamic arrays in 2018-2019. Formulas transfer seamlessly between platforms. The by_col parameter for sorting columns (horizontal sorting) works the same on both platforms but is rarely used—most data is arranged with records in rows.

## Syntax

> [!f(x)] SORT Syntax
>
> ```
> =SORT(array, [sort_index], [sort_order], [by_col])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `array` | Yes | The range or array to sort. Can be a column, row, or multi-column/row range. This entire array is returned in sorted order. |
| `sort_index` | No | The column number (or row number if by_col is TRUE) to sort by. Default is 1 (first column). Use an array like {2,3} to sort by multiple columns. |
| `sort_order` | No | 1 for ascending (default), -1 for descending. Use an array like {1,-1} to specify different orders for multi-column sorts. Must match the size of sort_index if arrays are used. |
| `by_col` | No | FALSE (default) to sort rows based on column values. TRUE to sort columns based on row values (horizontal sort). Rarely used since most data is organized in rows. |

### Return Value

Returns a dynamic array containing all elements of the input array, rearranged according to the specified sort criteria. The output has the same dimensions as the input and spills automatically into adjacent cells. Original data remains unchanged.

## Examples

> [!f(x)] SORT Examples

### Example 1: Basic Ascending Sort
```
=SORT(A2:A20)
```
**Result:** Returns all values from A2:A20 in ascending order (A-Z or smallest-to-largest)

**Explanation:** The simplest SORT—one column, default ascending order. Numbers sort numerically, text sorts alphabetically. The result spills downward from the cell containing the formula.

---

### Example 2: Descending Sort
```
=SORT(B2:B100, 1, -1)
```
**Result:** Returns column B values sorted from largest to smallest (or Z-A for text)

**Explanation:** The -1 in the third parameter specifies descending order. Use this for top-to-bottom rankings like highest sales, most recent dates, or reverse alphabetical listings.

---

### Example 3: Multi-Column Data Sorted by Specific Column
```
=SORT(A2:D50, 3, 1)
```
**Result:** Returns all four columns sorted by the values in column 3 (ascending)

**Explanation:** When sorting multi-column data, specify which column determines the order. Here, column 3 (perhaps "Amount" or "Date") controls the sort while columns 1, 2, and 4 stay associated with their original rows.

---

### Example 4: Multi-Level Sort (Two Columns)
```
=SORT(A2:E100, {2,4}, {1,-1})
```
**Result:** Sorted by column 2 ascending first, then column 4 descending for ties

**Explanation:** The array constants {2,4} and {1,-1} create hierarchical sorting. Perhaps sort by Department (column 2, A-Z), then by Salary (column 4, highest first) within each department. This mirrors the multi-level sort dialog but in formula form.

---

### Example 5: Sort by Multiple Columns (Three Levels)
```
=SORT(SalesData, {1,3,5}, {1,1,-1})
```
**Result:** Sorted by column 1, then 3, then 5, with the last one descending

**Explanation:** Three-level sorting: Region (ascending), Product (ascending), Revenue (descending). Essential for detailed reports where you need consistent grouping with ranked values within each group.

---

### Example 6: Sort Filtered Data
```
=SORT(FILTER(A2:D100, C2:C100="Active"), 2, -1)
```
**Result:** Active records sorted by column 2 in descending order

**Explanation:** Combine SORT with FILTER for filtered, sorted output in one formula. FILTER extracts matching rows, then SORT arranges them. This chain is foundational for dynamic reports.

---

### Example 7: Sort Unique Values
```
=SORT(UNIQUE(B2:B500))
```
**Result:** Alphabetically sorted list of unique values from column B

**Explanation:** UNIQUE extracts distinct values, SORT orders them. Perfect for generating sorted dropdown lists, category inventories, or clean reference data from messy source columns.

---

### Example 8: Sort by Text Length
```
=SORT(A2:A50, LEN(A2:A50), 1)
```
**Result:** Text values sorted from shortest to longest

**Explanation:** The sort_index can be an array of values, not just a column number. LEN(A2:A50) creates an array of text lengths, and SORT uses that for ordering. Creative use of calculated sort keys enables custom sort orders.

---

### Example 9: Random Sort (Shuffle)
```
=SORT(A2:D20, RANDARRAY(19), 1)
```
**Result:** Rows in random order (reshuffles on each recalculation)

**Explanation:** RANDARRAY generates random numbers that SORT uses as the sort key. Each recalc produces a new random order—useful for shuffling quiz questions, randomizing assignments, or sampling. Note: the RANDARRAY size must match the number of rows.

---

### Example 10: Sort by Absolute Values
```
=SORT(A2:B30, ABS(B2:B30), -1)
```
**Result:** Sorted by absolute value of column B, largest magnitude first

**Explanation:** For financial data with positive and negative values, sorting by absolute value puts the largest impacts (regardless of sign) first. ABS() creates the sort key, original signed values remain in the output.

---

### Example 11: Horizontal Sort (Sort Columns)
```
=SORT(A1:E5, 1, 1, TRUE)
```
**Result:** Columns rearranged based on values in row 1

**Explanation:** The by_col parameter (TRUE) sorts columns instead of rows. Row 1 values determine the column order. Use this for transposed data where headers are in the first row and you want columns sorted alphabetically by header.

---

### Example 12: Sort with Custom Order Using Helper Column
```
=SORT(A2:C100, MATCH(B2:B100, {"High","Medium","Low"}, 0), 1)
```
**Result:** Sorted with "High" first, "Medium" second, "Low" last

**Explanation:** For custom sort orders (like priority levels), MATCH against an array returns position numbers (1, 2, 3). SORT uses these as the sort key. "High" becomes 1 (first), "Low" becomes 3 (last).

---

### Example 13: Sort Dates by Month Regardless of Year
```
=SORT(A2:C100, MONTH(A2:A100), 1)
```
**Result:** Data sorted by month (January first through December), ignoring year

**Explanation:** MONTH() extracts the month number from dates. Sorting by this groups all January records together, all February records together, etc., regardless of what year they're from.

---

### Example 14: Nested SORT for Stable Secondary Sort
```
=SORT(SORT(A2:D100, 3, -1), 2, 1)
```
**Result:** Sorted by column 2 ascending; within each column 2 group, by column 3 descending

**Explanation:** While array syntax {2,3} is preferred, nesting SORT functions also achieves multi-level sorts. The inner SORT runs first, then the outer SORT runs on that result. Order matters: the last SORT applied is the primary sort.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Sort_index exceeds the number of columns (or rows) in array | Ensure sort_index refers to a column that exists in your array. A 3-column array can only use sort_index 1, 2, or 3. |
| `#VALUE!` | Mismatched array sizes in multi-level sort | When using {2,3} and {1,-1}, both arrays must have the same number of elements. |
| `#SPILL!` (Excel) | Spill range is blocked by existing data or merged cells | Clear cells below/right of formula. Unmerge any merged cells in the spill range. |
| `#REF!` | Spill range extends beyond worksheet boundaries | Move the formula or reduce the source data size. Very large sorts may need pagination. |
| `#NAME?` | SORT function not available in your Excel version | SORT requires Excel 365, Excel 2021, or Google Sheets. Not available in Excel 2019 or earlier. |
| `Unexpected order` | Mixing text and numbers in sort column | Numbers sort before/after text depending on platform. Ensure consistent data types in sort column. |
| `Case sensitivity` | Text sorting case handling | Both platforms are case-insensitive in sorting. "apple" and "Apple" sort together. |

## Use Cases

### [[Sales Leaderboard Dashboard]]

**Scenario:** Sales director needs a real-time leaderboard showing top performers, sorted by total sales descending, updated as new transactions are logged.

**Implementation:**
```
=SORT(
  FILTER(SalesReps!A2:E50, SalesReps!E2:E50>0),
  5, -1
)
```
Where column E contains total sales figures.

**Business Application:** Creates a dynamic leaderboard without manual updates. Post it on a shared dashboard and let SORT handle the ranking. Combine with conditional formatting to highlight top 3 performers with colors.

**Technical Details:** FILTER first excludes reps with zero sales (new or inactive), then SORT ranks by column 5 (sales total) descending. The result updates instantly as underlying sales data changes.

---

### [[Inventory Age Analysis]]

**Scenario:** Warehouse manager needs inventory sorted by receipt date to identify oldest stock for FIFO (First In, First Out) picking and to flag items at risk of expiration.

**Implementation:**
```
=SORT(Inventory!A2:F500, 4, 1)
```
Where column 4 contains the receipt date.

**Business Application:** Supports inventory rotation policies. Warehouse staff pick from the sorted list to ensure oldest stock moves first. Add a calculated age column and conditional formatting to highlight items approaching expiration.

**Technical Details:** Ascending date sort (1) puts oldest dates first. For most recent first (useful for reviewing new receipts), use -1. Combine with FILTER to focus on specific product categories or warehouse locations.

---

### [[Customer Prioritization for Outreach]]

**Scenario:** Account management team needs customer lists sorted by multiple criteria: first by assigned rep (alphabetically), then by account value (highest first) to prioritize outreach.

**Implementation:**
```
=SORT(Customers!A2:G300, {3,5}, {1,-1})
```
Where column 3 is account manager name and column 5 is annual account value.

**Business Application:** Each account manager sees their accounts grouped together, with highest-value customers at the top of their section. Enables focused outreach starting with the most important accounts.

**Technical Details:** Multi-level sort with {3,5} sorts by column 3 first, then column 5. The {1,-1} means column 3 ascending (A-Z by name) and column 5 descending (highest values first). Result is a hierarchically organized customer list.

---

### [[Project Timeline Sorting]]

**Scenario:** Project manager needs tasks sorted by due date (earliest first), but with overdue tasks highlighted at the very top regardless of how overdue they are.

**Implementation:**
```
=SORT(Tasks!A2:E100, IF(Tasks!D2:D100<TODAY(), 0, Tasks!D2:D100), 1)
```
Where column D contains due dates.

**Business Application:** Overdue tasks get artificial sort value of 0, putting them before any future dates. This ensures the PM addresses overdue items first, while upcoming tasks are still organized chronologically.

**Technical Details:** The IF expression replaces overdue dates with 0 (which sorts before any valid date serial number). Current and future tasks sort by their actual dates. This pattern—calculated sort keys—enables sophisticated custom ordering.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 365 (subscription), Excel 2021 (perpetual), Excel for web
- **Spill behavior:** Results spill automatically; #SPILL! error if blocked by data or merged cells
- **Performance:** Optimized for large datasets; handles tens of thousands of rows efficiently
- **Sort stability:** Stable sort—equal values maintain their original relative order
- **Case sensitivity:** Case-insensitive sorting (A = a)

### Google Sheets
- **Availability:** All versions (SORT available since early Google Sheets)
- **Spill behavior:** Results expand automatically into adjacent cells
- **Performance:** Excellent for typical datasets; very large ranges may slow calculation
- **Sort stability:** Stable sort—same behavior as Excel
- **Case sensitivity:** Case-insensitive sorting (same as Excel)

### Key Difference Alert
SORT behavior is highly consistent across platforms. The main practical difference is availability—Google Sheets has had SORT for much longer than Excel. Formulas transfer directly between platforms without modification. Both platforms handle the by_col parameter identically for the rare horizontal sorting use case.

## Tips and Best Practices

1. **Use array constants for multi-level sorts:** `=SORT(data, {2,4}, {1,-1})` is cleaner and more performant than nested SORT functions. It clearly shows the sort hierarchy in one place.

2. **Remember: 1 = ascending, -1 = descending:** If you can't remember, think "1 is the natural order, -1 is the opposite." Or just try both and see which output you want.

3. **Combine with FILTER for powerful data processing:** `=SORT(FILTER(...))` is a fundamental pattern. Filter first to reduce data, then sort for presentation. The combination replaces complex database queries.

4. **Use calculated sort keys for custom orders:** When alphabetical/numerical order isn't what you need, create a sort key with MATCH, IF, or other functions. `=SORT(data, MATCH(status, {"Critical","High","Normal"}, 0))` enables custom priority sorting.

5. **Leave room for spill growth:** Your sorted output may have more rows tomorrow than today. Position SORT formulas with ample empty space below to avoid #SPILL! errors as source data grows.

6. **SORT preserves all columns:** Unlike some approaches, SORT returns the entire row. You don't lose data—if you input 5 columns, you get 5 columns back, just reordered.

7. **For stable random ordering, use a helper column:** RANDARRAY recalculates constantly. If you need a persistent random order, paste RANDARRAY values, then SORT by that static column.

8. **Test edge cases:** What happens with blank cells in the sort column? Duplicate values? Mixed data types? Understanding these behaviors prevents surprises in production.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[SORTBY]] | Sort by separate array(s) not in the output | When sort criteria are in columns you don't want to include in results |
| [[RANK]] | Return rank of each value (not reorder data) | When you need ranking numbers added to data rather than reordering |
| [[LARGE]] / [[SMALL]] | Return nth largest/smallest values | When you only need specific ranked values, not the full sorted list |
| [[INDEX/MATCH with sorting]] | Pre-dynamic array sorting approach | When working in Excel 2019 or earlier without SORT function |

### Commonly Used Together

**[[FILTER]]** - Extract matching rows before sorting

*Combined with SORT for filtered, ordered output:*
```
=SORT(FILTER(A2:D100, B2:B100="Active"), 3, -1)
```
First filter for active records, then sort by column 3 descending. Foundation of most dynamic reports.

---

**[[UNIQUE]]** - Get distinct values then sort

*Combined with SORT for clean, ordered lists:*
```
=SORT(UNIQUE(C2:C500))
```
Extract unique categories/names, then alphabetize. Perfect for dynamic dropdown lists or reference tables.

---

**[[TAKE]]** / **[[DROP]]** - Get top/bottom N from sorted results

*Combined with SORT for top N analysis:*
```
=TAKE(SORT(A2:D100, 3, -1), 10)
```
Sort by column 3 descending, then take the top 10 rows. Creates "Top 10" lists that update automatically.

---

**[[SEQUENCE]]** - Add rank numbers to sorted output

*Combined with SORT for ranked lists:*
```
=HSTACK(SEQUENCE(ROWS(sorted_data)), sorted_data)
```
After sorting, add a sequence column for rank numbers. HSTACK combines the rank with the sorted data.

---

**[[CHOOSECOLS]]** - Select specific columns from sorted output

*Combined with SORT to limit output columns:*
```
=CHOOSECOLS(SORT(A2:F100, 3, -1), 1, 2, 3)
```
Sort the full data, then return only columns 1, 2, and 3 from the sorted result.

---

**[[LAMBDA]]** - Create reusable sort functions

*Create named sort patterns:*
```
=LAMBDA(data, SORT(data, 2, -1))(A2:D100)
```
Define complex sort operations once, reuse across the workbook with named LAMBDA functions.

## Official Documentation

- **Microsoft Excel:** [SORT function](https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c)
- **Google Sheets:** [SORT function](https://support.google.com/docs/answer/3093150)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Google Sheets | 2006 (original) | Available since early Google Sheets; slightly different original syntax |
| Excel 365 | 2018 (Insider), 2019 (general) | Part of dynamic array rollout |
| Excel 2021 | 2021 | First perpetual license version with SORT |
| Excel for web | 2019 | Full support in browser version |
| Excel 2019 and earlier | Not available | Use helper columns with INDEX/MATCH or VBA for sorting |

---

*Last updated: 2026-01-10*
