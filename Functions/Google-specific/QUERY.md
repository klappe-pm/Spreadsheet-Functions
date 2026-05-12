---
categories:
- spreadsheet-functions
subCategories:
- sheets
topics:
- google-specific
subTopics:
- data-analysis
- sql-like-queries
- filtering
- aggregation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Google Sheets Query
- SQL for Spreadsheets
- GViz Query Language
tags:
- data-analysis
- filtering
- aggregation
- google-sheets-only
---

# QUERY

## Description

**QUERY** is Google Sheets' most powerful function—it lets you run SQL-like queries directly on your spreadsheet data. Think of it as having a database query engine built into your spreadsheet. You can select specific columns, filter rows based on conditions, sort results, group and aggregate data, perform calculations, and even pivot data—all with a single formula. If you've ever wished you could write `SELECT * FROM data WHERE status = 'Active'` in a spreadsheet, QUERY is exactly that.

The QUERY function uses **Google Visualization API Query Language**, which is similar to SQL but designed specifically for spreadsheet data. While it doesn't support every SQL feature (no JOINs between different ranges, for example), it handles the most common data manipulation tasks elegantly. The key advantage over traditional spreadsheet functions like FILTER, SORT, and SUMIF is that QUERY combines all these operations in one function with a readable syntax—and it automatically expands to fill multiple cells with the results.

**Why QUERY is a game-changer:** Traditional spreadsheet analysis often requires multiple helper columns, complex nested formulas, or pivot tables. QUERY replaces all of that. Need to find all sales over $10,000 from Q4, sorted by date, showing only customer name and amount? That's one QUERY formula. Need to sum revenue by product category where quantity is greater than 100? Also one formula. The learning curve is real, but once you master QUERY, you'll wonder how you ever worked without it.

**Important: QUERY is Google Sheets only.** Microsoft Excel does not have this function. The closest Excel equivalents are combinations of FILTER, SORT, and SUMIFS functions (in Excel 365), or Power Query for more complex transformations. If you're building spreadsheets that need to work in both platforms, avoid QUERY or provide Excel-compatible alternatives.

## Syntax

> [!f(x)] QUERY Syntax
>
> ```
> =QUERY(data, query, [headers])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `data` | Yes | The range of cells to query. Can be a direct range (A1:E100), a named range, or the result of another function like IMPORTRANGE. Column letters in your query correspond to columns in this data range (first column = Col A, second = Col B, etc.). |
| `query` | Yes | A text string written in Google Visualization API Query Language. Must be enclosed in quotes. Supports SELECT, WHERE, GROUP BY, PIVOT, ORDER BY, LIMIT, OFFSET, LABEL, FORMAT, and OPTIONS clauses. |
| `headers` | No | The number of header rows in your data. Default is -1 (auto-detect), 0 means no headers, 1+ specifies exact header row count. Headers are used for column labels in output and affect how data types are detected. |

### Return Value

Returns an array of cells containing the query results. The output automatically spills into adjacent cells (dynamic array behavior). If the query returns no results, returns #N/A unless you handle it with IFERROR. Column headers from your source data are included in output by default.

## Examples

> [!f(x)] QUERY Examples

### Example 1: Select All Data (Basic)
```
=QUERY(A1:D100, "SELECT *")
```
**Result:** Returns all rows and columns from the range A1:D100

**Explanation:** The asterisk (*) means "all columns." This is useful as a starting point or when you want to filter rows without removing columns. Think of it as copying your data but with the ability to add conditions.

---

### Example 2: Select Specific Columns
```
=QUERY(A1:E100, "SELECT A, C, E")
```
**Result:** Returns only columns A, C, and E from the data

**Explanation:** Select only the columns you need. Columns are referenced by their position in the data range (A = first column, B = second, etc.), NOT by their spreadsheet column letters. If your data starts in column D, column D is still "A" in the query.

---

### Example 3: Filter with WHERE Clause
```
=QUERY(A1:D100, "SELECT * WHERE B = 'Active'")
```
**Result:** Returns all columns, but only rows where column B equals "Active"

**Explanation:** The WHERE clause filters rows. Text values must be enclosed in single quotes inside the query string. This is case-sensitive—'Active' won't match 'active'. Use LOWER() in the query for case-insensitive matching.

---

### Example 4: Numeric Comparisons
```
=QUERY(A1:E100, "SELECT A, B, E WHERE E > 10000 AND C < 50")
```
**Result:** Returns columns A, B, E where column E exceeds 10,000 AND column C is less than 50

**Explanation:** Numeric comparisons don't need quotes. You can use AND, OR, and NOT for complex conditions. Operators include: =, !=, <, <=, >, >=, CONTAINS, STARTS WITH, ENDS WITH, MATCHES, LIKE.

---

### Example 5: Dynamic Filtering with Cell References
```
=QUERY(A1:E100, "SELECT * WHERE B = '"&G1&"'")
```
Where G1 contains the value to filter by

**Result:** Returns rows where column B matches whatever value is in cell G1

**Explanation:** To use cell values in your query, concatenate them into the query string. For text: use `"...= '"&CELL&"'"` (single quotes around the value). For numbers: use `"...= "&CELL&""` (no quotes needed). This pattern enables interactive filtering.

---

### Example 6: Sorting Results
```
=QUERY(A1:D100, "SELECT * ORDER BY C DESC")
```
**Result:** Returns all data sorted by column C in descending order

**Explanation:** ORDER BY sorts results. Use ASC for ascending (default), DESC for descending. You can sort by multiple columns: `ORDER BY C DESC, A ASC`. This is far cleaner than nesting SORT functions.

---

### Example 7: Aggregation with GROUP BY
```
=QUERY(A1:D100, "SELECT A, SUM(D), AVG(D), COUNT(A) GROUP BY A")
```
**Result:** Returns one row per unique value in column A, with sum, average, and count of column D

**Explanation:** GROUP BY aggregates data like a pivot table. Aggregate functions include: SUM, AVG, COUNT, MAX, MIN. Every non-aggregated column in SELECT must appear in GROUP BY. This replaces complex SUMIF/COUNTIF formulas.

---

### Example 8: Filtering Aggregated Results with HAVING
```
=QUERY(A1:D100, "SELECT A, SUM(D) GROUP BY A HAVING SUM(D) > 50000")
```
**Result:** Returns grouped totals, but only groups where the sum exceeds 50,000

**Explanation:** WHERE filters individual rows BEFORE grouping. HAVING filters groups AFTER aggregation. Use HAVING when you want to filter based on aggregate values.

---

### Example 9: Limiting Results
```
=QUERY(A1:D100, "SELECT * ORDER BY D DESC LIMIT 10")
```
**Result:** Returns the top 10 rows by column D value

**Explanation:** LIMIT restricts output to first N rows. Combined with ORDER BY, this creates "Top N" queries easily. OFFSET skips rows: `LIMIT 10 OFFSET 5` returns rows 6-15.

---

### Example 10: Working with Dates
```
=QUERY(A1:D100, "SELECT * WHERE A > date '2024-01-01'")
```
**Result:** Returns rows where the date in column A is after January 1, 2024

**Explanation:** Dates in QUERY require special format: `date 'YYYY-MM-DD'`. For dynamic dates, convert cell values: `"...WHERE A > date '"&TEXT(G1,"yyyy-mm-dd")&"'"`. Date comparisons only work if the column contains actual date values, not text that looks like dates.

---

### Example 11: Text Pattern Matching
```
=QUERY(A1:D100, "SELECT * WHERE B CONTAINS 'Smith'")
=QUERY(A1:D100, "SELECT * WHERE B STARTS WITH 'A'")
=QUERY(A1:D100, "SELECT * WHERE B MATCHES '.*@gmail.com'")
```
**Result:** Rows containing 'Smith', starting with 'A', or matching email pattern

**Explanation:** CONTAINS finds substrings anywhere. STARTS WITH and ENDS WITH check prefixes/suffixes. MATCHES uses regular expressions for complex patterns. LIKE uses SQL wildcards: % for any characters, _ for single character.

---

### Example 12: PIVOT for Cross-Tabulation
```
=QUERY(A1:D100, "SELECT A, SUM(D) GROUP BY A PIVOT B")
```
**Result:** Creates a pivot table with column A values as rows, column B values as new columns, and sums of column D as values

**Explanation:** PIVOT transforms row values into columns—like a pivot table in one formula. The aggregated value goes into cells at the intersection of row and column values. This is incredibly powerful for creating summary matrices.

---

### Example 13: Renaming Columns with LABEL
```
=QUERY(A1:D100, "SELECT A, SUM(D) GROUP BY A LABEL A 'Category', SUM(D) 'Total Sales'")
```
**Result:** Same as grouping example, but columns are labeled 'Category' and 'Total Sales'

**Explanation:** LABEL renames output column headers. Useful for creating presentation-ready output or when aggregate function names (like "sum Amount") look ugly.

---

### Example 14: Formatting Output
```
=QUERY(A1:D100, "SELECT A, SUM(D) GROUP BY A FORMAT SUM(D) '$#,##0.00'")
```
**Result:** Grouped data with the sum column formatted as currency

**Explanation:** FORMAT applies number/date formats to output columns. Uses standard spreadsheet format codes. Note: Formatting converts numbers to text, which can affect downstream calculations.

---

### Example 15: Combining with IMPORTRANGE
```
=QUERY(IMPORTRANGE("spreadsheet_url", "Sheet1!A:E"), "SELECT Col1, Col2 WHERE Col3 > 100")
```
**Result:** Queries data from another spreadsheet

**Explanation:** When querying IMPORTRANGE (or arrays from other functions), use Col1, Col2, Col3 instead of A, B, C. This syntax refers to column positions in the array, not spreadsheet columns. Powerful for consolidating data across multiple spreadsheets.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Syntax error in query string | Check for missing quotes, typos in keywords (SELECT, WHERE), or mismatched parentheses |
| `#N/A` | Query returned no results | Add IFERROR wrapper, or check your WHERE conditions |
| `#REF!` | Referenced column doesn't exist | If data has 4 columns, you can't reference Col E. Check your data range |
| `Unable to parse query string` | Common with cell references | Ensure proper concatenation: `"...'"&CELL&"'"` for text, `"..."&CELL&""` for numbers |
| `#ERROR!` | Data type mismatch | Column has mixed types (text and numbers). Ensure consistent data types, or use TOTEXT/VALUE |
| Dates not filtering correctly | Date format wrong or text dates | Use `date 'YYYY-MM-DD'` format. Ensure column contains real dates, not text |

## Use Cases

### [[Sales Reporting: Top Performers by Region]]

**Scenario:** A sales manager needs a dynamic report showing top 10 sales reps by revenue for a selected region.

**Implementation:**
```
=QUERY(SalesData!A:F, "SELECT B, C, SUM(F) WHERE A = '"&$H$1&"' GROUP BY B, C ORDER BY SUM(F) DESC LIMIT 10 LABEL B 'Sales Rep', C 'Territory', SUM(F) 'Total Revenue'")
```
Where H1 contains the selected region name.

**Business Application:** Creates an interactive dashboard where changing H1 instantly updates the leaderboard. Eliminates need for multiple pivot tables or manual filtering. Can be combined with data validation dropdown for region selection.

**Technical Details:** The query groups by rep and territory, sums revenue, filters by region, sorts descending, and takes top 10—all in one formula. LABEL makes output presentation-ready without additional formatting.

---

### [[Inventory Management: Low Stock Alerts]]

**Scenario:** Warehouse manager needs automated list of products below reorder threshold, sorted by urgency.

**Implementation:**
```
=QUERY(Inventory!A:G, "SELECT A, B, D, E, F WHERE D < E ORDER BY (E-D) DESC LABEL A 'SKU', B 'Product', D 'Current Stock', E 'Reorder Point', F 'Supplier'")
```

**Business Application:** Automatically generates actionable reorder list without manual filtering. Sorting by (E-D) DESC puts most urgent items first. Can be emailed daily via Google Apps Script for proactive inventory management.

**Technical Details:** The WHERE clause compares two columns (current stock vs reorder point). Calculated columns can be used in ORDER BY. Consider adding LIMIT if you only want top priorities.

---

### [[HR Analytics: Employee Demographics Summary]]

**Scenario:** HR needs a breakdown of employee count by department and employment type for annual reporting.

**Implementation:**
```
=QUERY(Employees!A:H, "SELECT C, COUNT(A), SUM(G) GROUP BY C PIVOT D LABEL C 'Department', COUNT(A) 'Headcount', SUM(G) 'Total Salary'")
```

**Business Application:** Creates a cross-tabulation instantly—departments as rows, employment types (Full-time, Part-time, Contract) as columns, with counts at intersections. Replaces manual pivot tables that need refreshing.

**Technical Details:** PIVOT creates new columns dynamically based on unique values in column D. If a new employment type is added, it automatically appears. Be cautious with PIVOT on columns with many unique values—creates many columns.

---

### [[Financial Consolidation: Monthly Revenue by Category]]

**Scenario:** Finance team needs to aggregate transaction data into monthly revenue by product category.

**Implementation:**
```
=QUERY(Transactions!A:F, "SELECT MONTH(A)+1, C, SUM(E) WHERE A >= date '2024-01-01' AND A < date '2025-01-01' GROUP BY MONTH(A)+1, C PIVOT MONTH(A)+1 LABEL C 'Category'")
```

**Business Application:** Transforms detailed transaction data into a summary matrix showing categories as rows, months as columns, and revenue as values. Essential for monthly financial reporting and trend analysis.

**Technical Details:** MONTH() returns 0-11, so +1 adjusts to 1-12. Date filtering ensures only current year data. PIVOT on months creates 12-column output automatically. Consider FORMAT for currency display.

## Platform Differences

### Microsoft Excel
- **Availability:** QUERY does not exist in Excel
- **Alternatives:**
  - Use FILTER + SORT functions (Excel 365)
  - Use Power Query (Get & Transform) for complex queries
  - Use pivot tables for aggregation
  - Use SUMIFS/COUNTIFS for conditional aggregation

### Google Sheets
- **Availability:** All versions since launch
- **Specific Behavior:** This is a Google Sheets exclusive function
- Uses Google Visualization API Query Language (similar to SQL)
- Results automatically spill into adjacent cells
- Can query data from other spreadsheets via IMPORTRANGE

## Tips and Best Practices

1. **Start simple, then add complexity:** Begin with `SELECT *` to verify your data range works, then add WHERE, GROUP BY, ORDER BY one at a time. Debugging complex queries is much harder than building up incrementally.

2. **Use Col1, Col2 for arrays:** When querying the output of IMPORTRANGE, ARRAYFORMULA, or other array-producing functions, use Col1, Col2, Col3 instead of A, B, C.

3. **Handle text carefully:** Text comparisons are case-sensitive. Use `LOWER(B) = 'active'` for case-insensitive matching. Always enclose text values in single quotes.

4. **Format dates properly:** Use `date 'YYYY-MM-DD'` format. For cell references: `"...date '"&TEXT(A1,"yyyy-mm-dd")&"'"`

5. **Test with IFERROR:** Wrap QUERY in IFERROR to handle empty results gracefully: `=IFERROR(QUERY(...), "No results found")`

6. **Use named ranges:** Instead of A1:Z1000, use named ranges like `=QUERY(SalesData, "...")`. Easier to read and maintain.

7. **Watch for data type issues:** If a column has mixed types (numbers and text), QUERY uses the majority type and ignores others. Clean your data first.

8. **Optimize large datasets:** QUERY on very large ranges can be slow. Use explicit end rows (A1:E5000) instead of entire columns (A:E) when possible.

## Related Functions

### Similar Functions (Excel Alternatives)
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[FILTER]] | Returns rows matching criteria (both platforms) | Simple filtering without aggregation, need Excel compatibility |
| [[SORT]] | Sorts a range (both platforms) | Simple sorting, need Excel compatibility |
| [[UNIQUE]] | Returns unique values (both platforms) | Deduplication without aggregation |
| [[SUMIFS]] | Sum with multiple conditions (both platforms) | Simple conditional aggregation, need Excel compatibility |

### Commonly Used Together

**[[IMPORTRANGE]]** - Import data from other spreadsheets

*Combined with QUERY for cross-spreadsheet analysis:*
```
=QUERY(IMPORTRANGE("url", "Sheet1!A:E"), "SELECT Col1, Col2 WHERE Col3 > 100")
```
Query data from another Google Sheets file without copying it. Note the Col1, Col2 syntax for arrays.

---

**[[ARRAYFORMULA]]** - Apply formula to entire range

*Combined with QUERY for preprocessing:*
```
=QUERY({A1:A100, ARRAYFORMULA(B1:B100*C1:C100)}, "SELECT * WHERE Col2 > 1000")
```
Create calculated columns to query against using array brackets {} to combine ranges.

---

**[[IFERROR]]** - Handle errors gracefully

*Combined with QUERY for empty result handling:*
```
=IFERROR(QUERY(A1:E100, "SELECT * WHERE B='Rare Value'"), "No matching records found")
```
Prevent #N/A errors when queries return no results.

---

**[[INDIRECT]]** - Dynamic range references

*Combined with QUERY for dynamic sheet selection:*
```
=QUERY(INDIRECT(A1&"!A:E"), "SELECT * WHERE B > 100")
```
Query different sheets based on a cell value. Powerful for multi-sheet consolidation.

## Official Documentation

- **Google Sheets:** [QUERY function](https://support.google.com/docs/answer/3093343)
- **Google Query Language Reference:** [Query Language Reference](https://developers.google.com/chart/interactive/docs/querylanguage)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Google Sheets | Original launch | Core function since inception |
| Updates | Ongoing | Regular improvements to query language capabilities |
| Excel | N/A | Not available—use FILTER, SORT, or Power Query |

---

*Last updated: 2026-01-10*
