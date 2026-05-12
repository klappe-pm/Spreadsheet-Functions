---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics:
- horizontal-lookup
- table-lookup
- data-retrieval
- row-search
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Horizontal Lookup
- H Lookup
- Row Lookup
- Horizontal Search
tags:
- lookup
- reference
- data-retrieval
- horizontal
- table
---

# HLOOKUP

## Description

**HLOOKUP (Horizontal Lookup)** searches for a value in the first row of a table and returns a value from another row in the same column. It is the horizontal counterpart to VLOOKUP, designed for data organized in rows rather than columns. Think of it as scanning across a row of headers, finding your target, then dropping down to retrieve the corresponding value. If you have a table where months, product codes, or categories run across the top row, HLOOKUP is your tool for extracting data from any row below.

The "H" stands for horizontal because it searches **across** a row. The function looks in the topmost row of your table range, finds your search value, then moves down to the row number you specify and returns that value. This top-to-bottom limitation is HLOOKUP's key constraint—your lookup row must be the first row in your range, and you can only retrieve values from rows below it, never above.

**The approximate vs. exact match parameter:** Like VLOOKUP, HLOOKUP's fourth parameter (range_lookup) causes frequent confusion. TRUE (or omitted) performs an approximate match—useful for finding ranges like grade thresholds or tax brackets arranged horizontally. FALSE (or 0) performs an exact match—what you need 90% of the time when looking up specific identifiers, dates, or codes. **Always use FALSE unless you specifically need approximate matching**, and remember that approximate matching requires your first row to be sorted in ascending order from left to right.

**HLOOKUP is less common than VLOOKUP** because most spreadsheet data is organized vertically (records in rows, fields in columns). However, HLOOKUP remains essential for certain data layouts: cross-tabulation reports, monthly data arranged in columns, survey responses with questions as column headers, or transposed data from external systems. While INDEX+MATCH provides more flexibility for horizontal lookups, HLOOKUP offers simplicity and readability when your data naturally fits the horizontal structure. In modern Excel (365/2019+), XLOOKUP can handle both vertical and horizontal lookups, but Google Sheets still relies on HLOOKUP for horizontal searches.

## Syntax

> [!f(x)] HLOOKUP Syntax
>
> ```
> =HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `lookup_value` | Yes | The value to search for in the first row of table_array. Can be a cell reference, text (in quotes), number, or formula result. |
| `table_array` | Yes | The table range to search. The first row of this range is where HLOOKUP looks for lookup_value. Subsequent rows contain the data you want to retrieve. |
| `row_index_num` | Yes | The row number (starting at 1) in table_array from which to return a value. 1 = first row (lookup row itself), 2 = second row, etc. |
| `range_lookup` | No | TRUE (default) for approximate match, FALSE for exact match. Use FALSE for most lookups. TRUE requires the first row to be sorted ascending left to right. |

### Return Value

Returns the value from the specified row in the column where the lookup value was found. Returns #N/A if no match is found (exact match mode) or if lookup_value is smaller than the smallest value in the lookup row (approximate match mode). Returns #REF! if row_index_num exceeds the number of rows in the table.

## Examples

> [!f(x)] HLOOKUP Examples

### Example 1: Basic Exact Match Lookup
```
=HLOOKUP("Q2", A1:E5, 3, FALSE)
```
**Result:** Returns the value from row 3 where "Q2" is found in row 1

**Explanation:** Searches the first row (A1:E1) for "Q2", finds it, then drops down to row 3 of the range and returns that value. FALSE ensures an exact match. This is the standard HLOOKUP pattern for retrieving data from a table with column headers in the first row.

---

### Example 2: Using a Cell Reference as Lookup Value
```
=HLOOKUP(B1, Data!$A$1:$L$20, 5, FALSE)
```
**Result:** Looks up whatever value is in B1, returns row 5 from the Data sheet

**Explanation:** Instead of hardcoding "Q2", we reference cell B1 containing the quarter to look up. The formula can be reused by simply changing B1. Note the $ signs making the table range absolute—essential when copying formulas to prevent the range from shifting.

---

### Example 3: Looking Up Monthly Sales Data
```
=HLOOKUP("March", $A$1:$M$10, MATCH("Revenue", $A$1:$A$10, 0), FALSE)
```
**Result:** Returns the Revenue value for March

**Explanation:** Instead of hardcoding row number 4, MATCH finds which row contains "Revenue" in column A. If someone inserts a row, the formula still works. The months run across the top (Jan, Feb, March...), and metrics run down the left side (Revenue, Costs, Profit...).

---

### Example 4: Approximate Match for Score Ranges
```
=HLOOKUP(B2, GradeScale, 2, TRUE)
```
Where GradeScale row 1 has: 0, 60, 70, 80, 90 (score thresholds)
Where GradeScale row 2 has: F, D, C, B, A (letter grades)

**Result:** Returns the letter grade for the score in B2

**Explanation:** TRUE (approximate match) finds the largest value less than or equal to lookup_value. A score of 75 matches the 70 column (returning "C"), not 80. The lookup row MUST be sorted in ascending order (left to right) for approximate matching to work correctly.

---

### Example 5: Handling #N/A with IFERROR
```
=IFERROR(HLOOKUP(A2, DataTable, 3, FALSE), "Not Found")
```
**Result:** Returns row 3 value if found, "Not Found" if lookup fails

**Explanation:** HLOOKUP returns #N/A when it cannot find a match. Wrapping in IFERROR provides a graceful fallback. Use 0, "", "N/A", or a custom message depending on what makes sense for downstream calculations and reporting.

---

### Example 6: Looking Up Product Specifications
```
=HLOOKUP($A$2, Products!$B$1:$Z$15, 4, FALSE)
```
Where Products sheet has product codes in row 1 and specifications in rows below

**Result:** Returns specification from row 4 for the product code in A2

**Explanation:** Product catalogs sometimes arrange product codes horizontally with various specifications (weight, dimensions, price, etc.) in rows below. HLOOKUP fetches any specification row by changing the row_index_num parameter.

---

### Example 7: Two-Way Lookup (HLOOKUP + MATCH)
```
=HLOOKUP(B1, DataTable, MATCH(A2, RowHeaders, 0), FALSE)
```
**Result:** Finds column by B1, row by A2, returns intersection

**Explanation:** When you need to look up both column and row dynamically, combine HLOOKUP with MATCH. HLOOKUP finds the column using B1, and MATCH determines which row number contains the value in A2. Alternative: use INDEX with two MATCH functions.

---

### Example 8: Looking Up Across Workbooks
```
=HLOOKUP(A2, '[Budget.xlsx]Q1Data'!$A$1:$Z$50, 3, FALSE)
```
**Result:** Looks up A2 in the Q1Data sheet of Budget.xlsx file

**Explanation:** Reference external workbooks using [Filename.xlsx]SheetName! syntax. Both files must be open for real-time updates. When the source file is closed, Excel converts the reference to a full file path string.

---

### Example 9: Using Wildcards for Partial Matching
```
=HLOOKUP("*2024*", A1:Z5, 3, FALSE)
```
**Result:** Finds any header containing "2024" and returns row 3 value

**Explanation:** Use * (any characters) and ? (single character) wildcards for partial matching. This finds "Jan 2024" or "FY2024-Q1" in the header row. Only works with exact match mode (FALSE). Wildcards enable flexible matching without knowing exact header text.

---

### Example 10: Looking Up the First Row Value Itself
```
=HLOOKUP(A2, B1:Z3, 1, FALSE)
```
**Result:** Returns the matched header value from row 1

**Explanation:** Using row_index_num = 1 returns the value from the lookup row itself. This is useful for validating that a lookup value exists in the header row, or for normalizing variations (finding "Q1" when searching for "q1" since HLOOKUP is case-insensitive).

---

### Example 11: Combining HLOOKUP with INDIRECT for Dynamic Tables
```
=HLOOKUP(A2, INDIRECT(B2&"!A1:Z20"), 5, FALSE)
```
**Result:** Looks up A2 in the sheet named in B2

**Explanation:** INDIRECT converts the text in B2 (like "Sales" or "Marketing") into a sheet reference. This allows users to select which department's data to query without modifying the formula. Useful for dashboards with sheet selectors.

---

### Example 12: Returning Multiple Rows with Single Lookup
```
Row 2: =HLOOKUP($B$1, DataTable, 2, FALSE)
Row 3: =HLOOKUP($B$1, DataTable, 3, FALSE)
Row 4: =HLOOKUP($B$1, DataTable, 4, FALSE)
```
**Result:** Retrieves rows 2, 3, and 4 for the column found in B1

**Explanation:** To pull multiple rows for the same column lookup, use multiple HLOOKUP formulas with different row_index_num values. The $ on $B$1 keeps the lookup value fixed when copying. Each formula searches once, so consider INDEX+MATCH for better performance.

---

### Example 13: Date-Based Column Lookup
```
=HLOOKUP(DATE(2024, MONTH(TODAY()), 1), DateHeaders, 3, FALSE)
```
**Result:** Returns row 3 value for the current month's column

**Explanation:** When column headers are dates, you can construct lookup dates dynamically. This formula finds the first day of the current month in the header row and returns the corresponding row 3 value. Ensure header dates are actual date values, not text.

---

### Example 14: Case-Sensitive HLOOKUP Workaround
```
=INDEX(3:3, MATCH(TRUE, EXACT(1:1, "ABC"), 0))
```
**Result:** Finds "ABC" exactly (case-sensitive), not "abc" or "Abc"

**Explanation:** Standard HLOOKUP is case-insensitive. For case-sensitive horizontal lookups, use INDEX+MATCH with EXACT. This array formula finds the exact case match in row 1 and returns the corresponding value from row 3.

---

### Example 15: HLOOKUP in Data Validation Dependent Dropdown
```
Named Range "Categories" = Category headers in row 1
Data Validation Source: =OFFSET(HLOOKUP(A1, Products!A:Z, 1, FALSE), 1, 0, COUNTA(HLOOKUP(A1, Products!A:Z, 0, FALSE))-1, 1)
```
**Result:** Creates a dropdown showing items under the selected category

**Explanation:** HLOOKUP finds the category column, then OFFSET creates a dynamic range of items below it. This advanced technique creates cascading dropdowns where selecting "Electronics" shows electronic products, "Clothing" shows clothing items, etc.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | Value not found in lookup row | Check spelling, data types (text vs number), and leading/trailing spaces. Use TRIM on lookup value. Verify value exists in first row. |
| `#REF!` | row_index_num exceeds the number of rows in table_array | If table has 5 rows, row_index_num cannot be 6. Expand your table range or reduce row number. |
| `#VALUE!` | row_index_num is less than 1, or invalid parameter types | Row number must be >= 1. Ensure lookup_value is not an error. Check for circular references. |
| `Wrong result` | Approximate match finding wrong column | Using TRUE when you meant FALSE. Use FALSE for exact matching. If using TRUE, ensure first row is sorted ascending left to right. |
| `Wrong result` | Duplicate values in lookup row | HLOOKUP returns the FIRST (leftmost) match only. Restructure data or use FILTER/INDEX for handling duplicates. |
| `#NAME?` | Function misspelled or named range undefined | Check spelling of HLOOKUP. Verify any named ranges used in parameters exist. |
| `Unexpected #N/A` | Date/number stored as text | If headers look like dates but are text, the lookup fails. Convert text to proper dates with DATEVALUE or numbers with VALUE. |

## Use Cases

### [[Monthly Financial Reporting Dashboard]]

**Scenario:** A finance team maintains a spreadsheet where months run across the top (Jan through Dec) and financial metrics run down the rows (Revenue, COGS, Gross Profit, Operating Expenses, Net Income). Executives need to select any month and see all metrics for that month in a summary panel.

**Implementation:**
```
Month Selector (B2): Dropdown with Jan, Feb, Mar... Dec

Revenue: =HLOOKUP($B$2, FinancialData!$B$1:$N$20, MATCH("Revenue", FinancialData!$A$1:$A$20, 0), FALSE)
COGS: =HLOOKUP($B$2, FinancialData!$B$1:$N$20, MATCH("COGS", FinancialData!$A$1:$A$20, 0), FALSE)
Gross Profit: =HLOOKUP($B$2, FinancialData!$B$1:$N$20, MATCH("Gross Profit", FinancialData!$A$1:$A$20, 0), FALSE)
Net Income: =HLOOKUP($B$2, FinancialData!$B$1:$N$20, MATCH("Net Income", FinancialData!$A$1:$A$20, 0), FALSE)
```

**Business Application:** Monthly P&L analysis, budget vs actual comparisons, trend reporting. Finance teams frequently organize data with time periods as columns, making HLOOKUP the natural choice for period-based lookups.

**Technical Details:** Using MATCH for the row number makes formulas resilient to row insertions or reordering. All formulas reference the same lookup value ($B$2), so changing the month selector updates the entire dashboard instantly. Consider caching the HLOOKUP column position if performance becomes an issue with large datasets.

---

### [[Survey Results Analysis]]

**Scenario:** A market research team has survey data where questions are column headers (Q1, Q2, Q3...) and different analysis metrics are in rows (Response Count, Average Score, Std Deviation, Top Box %, Bottom Box %). Analysts need to quickly pull metrics for any selected question.

**Implementation:**
```
Question Selector (A2): Dropdown with Q1, Q2, Q3... Q50

Response Count: =HLOOKUP($A$2, SurveyData!$A$1:$BA$10, 2, FALSE)
Average Score: =HLOOKUP($A$2, SurveyData!$A$1:$BA$10, 3, FALSE)
Std Deviation: =HLOOKUP($A$2, SurveyData!$A$1:$BA$10, 4, FALSE)
Top Box %: =HLOOKUP($A$2, SurveyData!$A$1:$BA$10, 5, FALSE)

Comparison Question (D2): Second dropdown
Comparison Average: =HLOOKUP($D$2, SurveyData!$A$1:$BA$10, 3, FALSE)
Difference: =B3-E3
```

**Business Application:** Survey analysis, customer feedback processing, NPS score tracking. Surveys often have many questions (columns) with standardized metrics calculated for each, making HLOOKUP ideal for ad-hoc question analysis.

**Technical Details:** Survey data often has 50+ questions as columns. HLOOKUP handles wide tables efficiently. For comparing multiple questions side-by-side, duplicate the HLOOKUP pattern with different selectors. Add conditional formatting to highlight significant differences between questions.

---

### [[Employee Schedule Matrix Lookup]]

**Scenario:** A retail store manager maintains a weekly schedule where employee names are in the first row and days of the week are in rows below (Monday through Sunday). Each cell contains the shift assignment (Morning, Afternoon, Evening, Off). The manager needs to quickly check any employee's schedule for any day.

**Implementation:**
```
Employee Selector (B2): Dropdown with employee names
Day Selector (B3): Dropdown with Monday, Tuesday... Sunday

Schedule Matrix:
          John    Sarah   Mike    Lisa    Tom
Monday    Morning Evening Off     Morning Afternoon
Tuesday   Evening Morning Morning Off     Morning
...

Shift Assignment: =HLOOKUP($B$2, Schedule!$A$1:$Z$8, MATCH($B$3, Schedule!$A$1:$A$8, 0), FALSE)

Full Week View:
Monday: =HLOOKUP($B$2, Schedule!$A$1:$Z$8, 2, FALSE)
Tuesday: =HLOOKUP($B$2, Schedule!$A$1:$Z$8, 3, FALSE)
Wednesday: =HLOOKUP($B$2, Schedule!$A$1:$Z$8, 4, FALSE)
...
```

**Business Application:** Workforce scheduling, resource allocation, room booking systems. Any scenario where entities (people, rooms, equipment) are columns and time slots or categories are rows benefits from HLOOKUP.

**Technical Details:** The schedule matrix naturally has employees as columns (limited number, easily viewed horizontally) and days as rows. HLOOKUP fetches the shift for any employee-day combination. Add COUNTIF formulas to summarize how many shifts each employee works.

---

### [[Product Feature Comparison Tool]]

**Scenario:** A sales team has a product comparison matrix where product names are column headers and features are rows (Price, Weight, Battery Life, Screen Size, Warranty). Sales reps need to quickly compare any two products side by side for customer presentations.

**Implementation:**
```
Product 1 Selector (B2): Dropdown with product names
Product 2 Selector (D2): Dropdown with product names

Feature Comparison Table:
Feature         Product 1           Product 2
Price           =HLOOKUP($B$2, Products!$A$1:$Z$20, MATCH("Price", Products!$A$1:$A$20, 0), FALSE)
                                    =HLOOKUP($D$2, Products!$A$1:$Z$20, MATCH("Price", Products!$A$1:$A$20, 0), FALSE)
Weight          =HLOOKUP($B$2, ..., MATCH("Weight", ..., 0), FALSE)
                                    =HLOOKUP($D$2, ..., MATCH("Weight", ..., 0), FALSE)
Battery         =HLOOKUP($B$2, ..., MATCH("Battery Life", ..., 0), FALSE)
                                    =HLOOKUP($D$2, ..., MATCH("Battery Life", ..., 0), FALSE)
```

**Business Application:** Product comparisons, competitive analysis, specification sheets. When products are columns and attributes are rows, HLOOKUP enables dynamic comparison tools.

**Technical Details:** Each row in the comparison fetches the same attribute from two different product columns. Using MATCH for row numbers means new features can be added without updating formulas. Add conditional formatting to highlight which product is better for each feature.

## Platform Differences

### Microsoft Excel

- **Availability:** All versions from Excel 97 onward
- **Case sensitivity:** Case-insensitive (abc = ABC = Abc)
- **Wildcards:** Fully supported (* and ?) in exact match mode
- **Performance:** Efficient for most use cases; very wide tables may slow down
- **XLOOKUP alternative:** Available in Excel 2019/365—handles horizontal lookups with cleaner syntax
- **Array formulas:** Legacy versions require Ctrl+Shift+Enter for array operations

### Google Sheets

- **Availability:** All versions from Sheets' inception
- **Case sensitivity:** Case-insensitive (same as Excel)
- **Wildcards:** Supported in exact match mode (FALSE)
- **Performance:** Generally efficient with wide tables and full-row references
- **No XLOOKUP:** Use HLOOKUP or INDEX+MATCH for horizontal lookups
- **QUERY alternative:** QUERY function can sometimes replace HLOOKUP for complex horizontal data retrieval

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Wildcard support | Full (* and ?) | Full (* and ?) |
| Array entry | Ctrl+Shift+Enter (legacy) / Auto (365) | Auto |
| XLOOKUP alternative | Available (365/2019+) | Not available |
| Full-row reference | Supported (1:1 syntax) | Supported |
| External workbook reference | [Book.xlsx]Sheet!Range | IMPORTRANGE required |
| Named range in table_array | Supported | Supported |

## Tips and Best Practices

1. **Always use FALSE for exact match:** TRUE (approximate) is rarely what you want for identifier lookups. Make it a habit: `=HLOOKUP(..., FALSE)` every time unless you specifically need threshold-based matching like grade scales or tax brackets.

2. **Lock your table reference with absolute references:** Use $ signs (`$A$1:$Z$20`) so the range does not shift when copying the formula. Even better, define a named range for the table and use that name in your formula.

3. **Use MATCH for row numbers instead of hardcoding:** `=HLOOKUP(A2, Table, MATCH("Row Label", RowLabels, 0), FALSE)` survives row insertions and makes formulas self-documenting. Hardcoded row numbers like "5" require manual updates when data structure changes.

4. **Wrap in IFERROR for clean output:** `=IFERROR(HLOOKUP(...), "")` prevents #N/A errors from cluttering your sheet and breaking downstream calculations that depend on the lookup result.

5. **Remember that HLOOKUP only searches the first row:** Your lookup value must be in the top row of table_array. If your headers are in row 2, start your range at row 2, not row 1.

6. **Consider INDEX+MATCH for more flexibility:** INDEX+MATCH can look up values and return data from any relative position—not just below. If you need to search row 3 and return row 1 (upward), HLOOKUP cannot help; use INDEX+MATCH instead.

7. **Watch for data type mismatches:** "2024" (text) does not equal 2024 (number). If lookups fail unexpectedly, check whether your lookup value and header row contain the same data type. Use VALUE() or TEXT() to convert as needed.

8. **Be cautious with approximate match:** When using TRUE for approximate matching, the first row MUST be sorted in ascending order from left to right. Unsorted data with approximate matching produces incorrect results without any error message.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[VLOOKUP]] | Vertical lookup (searches down columns) | When your data is organized vertically with row headers on the left and you need to search down and return right |
| [[XLOOKUP]] | Modern bi-directional lookup | Excel 365/2019 only. Can search horizontally or vertically with cleaner syntax and built-in error handling |
| [[INDEX]]+[[MATCH]] | Flexible lookup combination | When you need to look up (search any row) and return from any relative position, or for better performance on large tables |
| [[LOOKUP]] | Simplified lookup (legacy) | Rarely—mostly for backward compatibility. Less flexible than HLOOKUP |
| [[FILTER]] | Return multiple matching rows/columns | When you need all matches, not just the first one. Available in Excel 365 and Google Sheets |

### Commonly Used Together

**[[MATCH]]** - Find position in a row

*Combined with HLOOKUP for dynamic row selection:*
```
=HLOOKUP(A2, Table, MATCH("Sales", RowLabels, 0), FALSE)
```
MATCH finds which row number contains "Sales" in the row labels, making the formula resilient to row insertions and deletions.

---

**[[IFERROR]]** - Handle lookup failures

*Combined with HLOOKUP for graceful error handling:*
```
=IFERROR(HLOOKUP(A2, Table, 3, FALSE), "Not found")
```
Returns "Not found" instead of #N/A when the lookup value does not exist in the header row.

---

**[[INDIRECT]]** - Dynamic range references

*Combined with HLOOKUP for dynamic table selection:*
```
=HLOOKUP(A2, INDIRECT(B2&"Data"), 3, FALSE)
```
The table range is determined by the value in B2, enabling dashboard sheet selectors.

---

**[[INDEX]]** - Return value at intersection

*Alternative to HLOOKUP with more flexibility:*
```
=INDEX(3:3, MATCH(A2, 1:1, 0))
```
INDEX+MATCH can look in any direction and handle scenarios HLOOKUP cannot, such as returning values from rows above the search row.

---

**[[TRANSPOSE]]** - Convert rows to columns

*Used to reorganize data for VLOOKUP or HLOOKUP:*
```
=TRANSPOSE(A1:A10)
```
If your data is vertical but you prefer HLOOKUP, or horizontal but you prefer VLOOKUP, TRANSPOSE can reorient the data.

---

**[[ROW]]** - Return row numbers

*Combined with HLOOKUP for dynamic row index:*
```
=HLOOKUP(A$1, DataTable, ROW()-ROW($A$5)+2, FALSE)
```
Calculates row_index_num based on the formula's position, enabling formulas that auto-adjust as you copy them down.

## Official Documentation

- **Microsoft Excel:** [HLOOKUP function](https://support.microsoft.com/en-us/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f)
- **Google Sheets:** [HLOOKUP function](https://support.google.com/docs/answer/3093375)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation alongside VLOOKUP |
| Excel 2007 | Enhanced | Improved performance with large datasets |
| Excel 2010 | Enhanced | Better handling of array operations |
| Excel 2019/365 | XLOOKUP introduced | Modern alternative that handles both horizontal and vertical lookups |
| Google Sheets | Original launch (2006) | Full compatibility with Excel's implementation |
| Google Sheets | 2018+ | Improved array handling and performance |

---

*Last updated: 2026-01-10*
