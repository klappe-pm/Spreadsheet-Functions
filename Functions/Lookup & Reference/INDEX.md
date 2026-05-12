---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics:
- data-retrieval
- array-lookup
- dynamic-reference
- index-match
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Array Index
- Cell Index
- Range Index
- Array Reference
tags:
- lookup
- reference
- data-retrieval
- array
- index-match
---

# INDEX

## Description

**INDEX** is one of the most versatile and powerful functions in Excel and Google Sheets, returning a value or reference from within a table or range based on row and column numbers you specify. Think of it as pointing to a specific cell in a grid and saying "give me what's there." If you have a 10x5 table and you want the value in row 3, column 4, INDEX delivers it instantly. Unlike VLOOKUP, which is constrained to searching leftmost columns and returning values to the right, INDEX can retrieve any value from any position in any range—making it the ultimate building block for flexible data retrieval.

The true power of INDEX reveals itself when paired with the **MATCH** function—a combination that has been the professional spreadsheet user's secret weapon for decades. While VLOOKUP requires you to count columns manually and breaks when columns are inserted or deleted, INDEX+MATCH dynamically calculates positions. The MATCH function finds the row (and optionally column) position of your lookup value, and INDEX uses those positions to fetch the result. This separation of "finding" and "fetching" makes INDEX+MATCH more robust, more flexible, and often faster than VLOOKUP, especially in large datasets.

**INDEX has two forms:** the **array form** (most common) returns a value from a single range, while the **reference form** returns a reference from one of several specified areas. The array form handles 99% of use cases—you provide a range, a row number, and optionally a column number. The reference form is more advanced, allowing you to choose among multiple non-contiguous ranges using an area_num parameter. Most users never need the reference form, but it's invaluable for building dynamic dashboards where users select which data range to display.

**Platform considerations:** INDEX works identically in Excel and Google Sheets, with one important nuance. In modern Excel (365 and 2019+), INDEX can return entire rows or columns when you specify 0 for the row or column number, enabling powerful array operations. Google Sheets also supports this behavior. However, when using INDEX as part of a range reference (like `INDEX(A:A,1):INDEX(A:A,10)`), behavior can vary slightly between platforms. Always test dynamic range constructions in your target platform. For most standard INDEX+MATCH lookups, both platforms behave identically.

## Syntax

> [!f(x)] INDEX Syntax
>
> **Array Form (most common):**
> ```
> =INDEX(array, row_num, [column_num])
> ```
>
> **Reference Form (advanced):**
> ```
> =INDEX(reference, row_num, [column_num], [area_num])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `array` | Yes | The range of cells or array constant from which to return a value. If array contains only one row or column, the corresponding row_num or column_num argument is optional. |
| `row_num` | Yes* | The row number in the array from which to return a value. If row_num is 0, INDEX returns the entire column (as an array). If omitted, column_num is required. |
| `column_num` | No | The column number in the array from which to return a value. If column_num is 0, INDEX returns the entire row (as an array). If omitted, defaults to 1. |
| `reference` | Yes | A reference to one or more cell ranges. Used in the reference form when working with multiple areas. |
| `area_num` | No | Used with the reference form. Selects which range in reference to use. First area = 1, second = 2, etc. Defaults to 1 if omitted. |

*row_num is required if column_num is not specified for a multi-column array.

### Return Value

Returns the value at the intersection of the specified row and column within the given array or reference. If row_num or column_num is 0, returns an array of values (the entire row or column). Returns #REF! error if row_num or column_num is out of bounds, or if area_num references a non-existent area.

## Examples

> [!f(x)] INDEX Examples

### Example 1: Basic Single-Column Lookup
```
=INDEX(A2:A10, 5)
```
**Result:** Returns the value from the 5th cell in the range A2:A10 (which is A6)

**Explanation:** When working with a single-column range, you only need to specify the row number. This is the simplest form of INDEX—it counts down 5 rows from the start of the range and returns that value. The range A2:A10 has 9 cells; row 5 refers to the 5th cell within that range (A6 in absolute terms).

---

### Example 2: Two-Dimensional Array Lookup
```
=INDEX(B2:E20, 7, 3)
```
**Result:** Returns the value at row 7, column 3 of the range B2:E20 (cell D8)

**Explanation:** For a two-dimensional range, specify both row and column numbers. Row 7 means the 7th row within the range (not row 7 of the spreadsheet), and column 3 means the 3rd column of the range (column D, since B is 1, C is 2, D is 3). This is how you pinpoint any cell in a table.

---

### Example 3: INDEX with MATCH for Dynamic Row Lookup
```
=INDEX(C2:C100, MATCH("Product X", A2:A100, 0))
```
**Result:** Returns the value in column C for the row where "Product X" appears in column A

**Explanation:** This is the classic INDEX+MATCH pattern that often replaces VLOOKUP. MATCH finds which row contains "Product X" in A2:A100 (let's say row 15), and INDEX uses that position to return the corresponding value from C2:C100 (C16 in absolute terms). Unlike VLOOKUP, this can look in any direction—column C could be to the left of column A.

---

### Example 4: Two-Way Lookup with INDEX and Two MATCH Functions
```
=INDEX(B2:F20, MATCH("Q3", A2:A20, 0), MATCH("Revenue", B1:F1, 0))
```
**Result:** Returns the value at the intersection of the "Q3" row and "Revenue" column

**Explanation:** This powerful pattern dynamically locates both row and column positions. The first MATCH finds which row contains "Q3" in the row headers (column A). The second MATCH finds which column contains "Revenue" in the column headers (row 1). INDEX then returns the cell at that intersection. This is ideal for matrix-style reports where you need to look up both dimensions.

---

### Example 5: Returning an Entire Row
```
=INDEX(A2:E10, 3, 0)
```
**Result:** Returns all values in the 3rd row of the range as an array: {A4, B4, C4, D4, E4}

**Explanation:** Using 0 for column_num tells INDEX to return the entire row. In Excel 365 and Google Sheets, this spills across multiple cells automatically. In older Excel versions, you would need to enter this as an array formula (Ctrl+Shift+Enter) or use it within another function that expects an array. This is powerful for extracting complete records.

---

### Example 6: Returning an Entire Column
```
=INDEX(B2:F10, 0, 3)
```
**Result:** Returns all values in the 3rd column of the range as an array

**Explanation:** Using 0 for row_num returns the entire column. This is useful when you need to pass a whole column to functions like SUM, AVERAGE, or SUMPRODUCT. Combined with MATCH, you can dynamically select which column to aggregate: `=SUM(INDEX(B2:F100, 0, MATCH("Sales", B1:F1, 0)))`.

---

### Example 7: INDEX as Part of a Dynamic Range
```
=SUM(A1:INDEX(A:A, 10))
```
**Result:** Sums A1 through A10

**Explanation:** INDEX returns a reference, not just a value—so you can use it to build dynamic ranges. Here, `INDEX(A:A, 10)` returns a reference to A10, and the formula sums A1:A10. This is powerful for creating ranges whose endpoints change based on formulas: `=SUM(A1:INDEX(A:A, COUNTA(A:A)))` sums all non-empty cells.

---

### Example 8: Looking Up the Last Value in a Column
```
=INDEX(A:A, COUNTA(A:A))
```
**Result:** Returns the last non-empty value in column A

**Explanation:** COUNTA counts all non-empty cells in column A. If there are 50 filled cells (starting from row 1), COUNTA returns 50, and INDEX retrieves the 50th cell. This is a common pattern for finding the latest entry in a list. Note: this assumes no empty cells in the middle of your data.

---

### Example 9: Reverse Lookup (Looking Left)
```
=INDEX(A2:A100, MATCH("XYZ-123", C2:C100, 0))
```
**Result:** Returns the value in column A for the row where "XYZ-123" appears in column C

**Explanation:** This is something VLOOKUP cannot do—looking up a value in column C and returning the corresponding value from column A (which is to the left). INDEX+MATCH doesn't care about left or right; you specify exactly which column to search and which column to return. This flexibility is why INDEX+MATCH is preferred by power users.

---

### Example 10: Reference Form with Multiple Areas
```
=INDEX((A1:B5, D1:E5, G1:H5), 2, 1, 3)
```
**Result:** Returns the value at row 2, column 1 of the 3rd area (G1:H5), which is cell G2

**Explanation:** The reference form allows INDEX to work with multiple non-contiguous ranges. The ranges are enclosed in parentheses and separated by commas. The area_num parameter (3) selects which range to use. This is useful for dashboards where users select a data category and you need to pull from different tables.

---

### Example 11: INDEX+MATCH with Multiple Criteria (Array Formula)
```
=INDEX(D2:D100, MATCH(1, (A2:A100="East")*(B2:B100="Q4"), 0))
```
**Result:** Returns the value in column D where column A is "East" AND column B is "Q4"

**Explanation:** This array formula (Ctrl+Shift+Enter in older Excel) handles multiple criteria. The expression `(A2:A100="East")*(B2:B100="Q4")` creates an array of 1s (TRUE*TRUE) where both conditions are met and 0s elsewhere. MATCH finds the position of the first 1, and INDEX returns the corresponding value. In Excel 365, this works without Ctrl+Shift+Enter.

---

### Example 12: Finding the Position of the Maximum Value
```
=INDEX(A2:A100, MATCH(MAX(B2:B100), B2:B100, 0))
```
**Result:** Returns the value in column A that corresponds to the maximum value in column B

**Explanation:** MAX finds the largest value in B2:B100. MATCH finds its position. INDEX retrieves the corresponding value from column A. This is perfect for answering questions like "Which product had the highest sales?" or "Which employee has the most experience?"

---

### Example 13: Case-Sensitive Lookup with INDEX+MATCH+EXACT
```
=INDEX(B2:B100, MATCH(TRUE, EXACT(A2:A100, "ABC"), 0))
```
**Result:** Returns the value in column B where column A contains exactly "ABC" (case-sensitive)

**Explanation:** Standard lookups are case-insensitive. EXACT performs a case-sensitive comparison, returning TRUE only for exact case matches. MATCH finds the first TRUE in the resulting array. This requires Ctrl+Shift+Enter in older Excel or works automatically in Excel 365/Sheets.

---

### Example 14: Using INDEX with SMALL for Nth Match
```
=INDEX(B:B, SMALL(IF(A:A="Category", ROW(A:A)), 3))
```
**Result:** Returns the value from column B for the 3rd occurrence of "Category" in column A

**Explanation:** When you need the 2nd, 3rd, or Nth match (not just the first), combine IF to find all matching rows, SMALL to get the Nth smallest row number, and INDEX to retrieve the value. This is an array formula in older Excel. Change the 3 to 1, 2, etc., for different occurrences.

---

### Example 15: Creating a Dynamic Named Range with INDEX
```
Named Range "SalesData" = A1:INDEX(A:C, COUNTA(A:A), 3)
```
**Result:** Creates a named range that automatically expands as data is added

**Explanation:** In Name Manager, you can define ranges using INDEX. This formula starts at A1 and extends to the row containing the last non-empty cell in column A, spanning 3 columns. As you add rows, the named range automatically includes them. This eliminates the need to manually update ranges.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#REF!` | row_num or column_num exceeds the dimensions of the array | If your range has 10 rows and you request row 15, you get #REF!. Verify your range size and position calculations. |
| `#REF!` | area_num references a non-existent area in reference form | If you have 3 areas but request area 5, you get #REF!. Ensure area_num is valid. |
| `#VALUE!` | row_num or column_num is non-numeric or negative | Row and column numbers must be positive integers or 0. Check that MATCH isn't returning an error. |
| `#N/A` | Not directly from INDEX, but from MATCH within the formula | The MATCH function couldn't find the lookup value. Check spelling, data types, and leading/trailing spaces. |
| `Unexpected array` | Used row_num=0 or column_num=0 in older Excel without array context | In older Excel, returning entire rows/columns requires Ctrl+Shift+Enter or use within an array-aware function. |
| `Wrong value returned` | Confusion between absolute rows and relative rows within range | INDEX(A5:A20, 3) returns the 3rd row of the range (A7), not spreadsheet row 3. Always think in terms of position within the specified range. |

## Use Cases

### [[Employee Performance Dashboard]]

**Scenario:** An HR dashboard allows managers to select an employee name from a dropdown and instantly view their performance metrics including rating, bonus percentage, tenure, and department—all stored in different columns of an employee database.

**Implementation:**
```
Employee Name Dropdown: Cell B2 (data validation list from A column of database)

Performance Rating: =INDEX(Employees!$D$2:$D$500, MATCH($B$2, Employees!$A$2:$A$500, 0))
Bonus Percentage: =INDEX(Employees!$E$2:$E$500, MATCH($B$2, Employees!$A$2:$A$500, 0))
Years of Service: =INDEX(Employees!$F$2:$F$500, MATCH($B$2, Employees!$A$2:$A$500, 0))
Department: =INDEX(Employees!$C$2:$C$500, MATCH($B$2, Employees!$A$2:$A$500, 0))
```

**Business Application:** This dashboard pattern is used across HR, sales, and operations for instant data retrieval based on user selection. Managers can quickly review employee information without scrolling through large datasets. The same MATCH result drives multiple INDEX lookups, and because INDEX+MATCH can retrieve columns in any order (including those to the left of the lookup column), the database layout doesn't constrain the dashboard design.

**Technical Details:** All formulas reference the same MATCH lookup, so consider storing the MATCH result in a helper cell to improve performance: `Helper Cell: =MATCH($B$2, Employees!$A$2:$A$500, 0)`, then `=INDEX(Employees!$D$2:$D$500, $C$2)`. Use absolute references ($) on ranges to prevent shifting when copying formulas. Add IFERROR wrapper if the dropdown might be empty.

---

### [[Dynamic Financial Report Generator]]

**Scenario:** A financial analyst needs to build a report that shows revenue, expenses, and profit for any selected quarter and year combination, pulling from a large data table organized with year/quarter combinations as rows and financial metrics as columns.

**Implementation:**
```
Year Selector (C2): 2024 (dropdown)
Quarter Selector (C3): Q3 (dropdown)
Lookup Key (C4): =C2&"-"&C3 (creates "2024-Q3")

Revenue: =INDEX(FinancialData!$B$2:$F$100, MATCH($C$4, FinancialData!$A$2:$A$100, 0), MATCH("Revenue", FinancialData!$B$1:$F$1, 0))
Expenses: =INDEX(FinancialData!$B$2:$F$100, MATCH($C$4, FinancialData!$A$2:$A$100, 0), MATCH("Expenses", FinancialData!$B$1:$F$1, 0))
Net Profit: =INDEX(FinancialData!$B$2:$F$100, MATCH($C$4, FinancialData!$A$2:$A$100, 0), MATCH("Net Profit", FinancialData!$B$1:$F$1, 0))
```

**Business Application:** Finance teams use this pattern for dynamic reporting, allowing executives to explore data interactively without requiring new reports for each period. The two-way INDEX+MATCH lookup (using MATCH for both row and column positions) means the report automatically adapts if columns are reordered or new columns are added. This is significantly more robust than VLOOKUP with hardcoded column numbers.

**Technical Details:** The key pattern here is using two MATCH functions—one for the row header (year-quarter combination) and one for the column header (metric name). If the metric names might change, store them in a cell and reference that cell in the MATCH formula. For large financial datasets, consider caching MATCH results in helper cells to reduce calculation time.

---

### [[Inventory Reorder Alert System]]

**Scenario:** A warehouse manager needs a system that looks up current stock levels for any product, compares them against reorder points, and displays supplier contact information for items that need reordering. The supplier data is in a separate table where the supplier ID is to the left of the supplier name (requiring a leftward lookup).

**Implementation:**
```
Product Code Input (B2): User enters product code
Current Stock: =INDEX(Inventory!$C$2:$C$1000, MATCH($B$2, Inventory!$A$2:$A$1000, 0))
Reorder Point: =INDEX(Inventory!$D$2:$D$1000, MATCH($B$2, Inventory!$A$2:$A$1000, 0))
Supplier ID: =INDEX(Inventory!$E$2:$E$1000, MATCH($B$2, Inventory!$A$2:$A$1000, 0))
Reorder Needed: =IF(B5<B6, "YES - REORDER", "Stock OK")

Supplier Name: =INDEX(Suppliers!$A$2:$A$200, MATCH(B7, Suppliers!$C$2:$C$200, 0))
Supplier Phone: =INDEX(Suppliers!$B$2:$B$200, MATCH(B7, Suppliers!$C$2:$C$200, 0))
```

**Business Application:** Operations and supply chain teams rely on this pattern to connect transactional data (inventory levels) with reference data (supplier information). The ability to look left (supplier ID is in column C but we return data from columns A and B) is impossible with VLOOKUP but trivial with INDEX+MATCH. This eliminates the need to restructure data tables to accommodate lookup limitations.

**Technical Details:** Note how the Suppliers lookup searches column C (Supplier ID) but returns columns A and B (which are to the left). This is the "reverse lookup" capability that makes INDEX+MATCH essential for real-world data that wasn't designed with VLOOKUP's limitations in mind. Add IFERROR wrappers to handle missing products or suppliers gracefully.

---

### [[Sales Commission Calculator with Tiered Rates]]

**Scenario:** A sales compensation system needs to look up commission rates from a tiered table (where exact matches don't exist—we need the rate for the bracket the sales amount falls into), then apply that rate to calculate commissions, and finally look up the salesperson's payment details.

**Implementation:**
```
Commission Tier Table (CommissionTiers):
   Sales Amount | Commission Rate
   0            | 5%
   10000        | 7%
   25000        | 10%
   50000        | 12%
   100000       | 15%

Salesperson (B2): John Smith
Monthly Sales (B3): 67500

Commission Rate: =INDEX(CommissionTiers!$B$2:$B$6, MATCH($B$3, CommissionTiers!$A$2:$A$6, 1))
Result: 12% (because 67500 falls in the 50000-99999 bracket)

Commission Amount: =B3*B4

Bank Account: =INDEX(Employees!$F$2:$F$100, MATCH($B$2, Employees!$A$2:$A$100, 0))
```

**Business Application:** Compensation, pricing, and tax calculations often require tiered lookups where you need to find "the highest value that doesn't exceed the target." The MATCH function with match_type=1 does exactly this (approximate match, less than or equal). Combined with INDEX, you can build sophisticated tiered systems without nested IF statements.

**Technical Details:** For approximate matching with MATCH (match_type=1), the lookup column MUST be sorted in ascending order. The formula finds the largest value that is less than or equal to the lookup value. For the inverse (smallest value greater than or equal), use match_type=-1 with data sorted descending. This replaces complex nested IFs: instead of `=IF(B3>=100000, 15%, IF(B3>=50000, 12%, IF(...)))`, you have a simple INDEX+MATCH.

## Platform Differences

### Microsoft Excel

- **Availability:** All versions from Excel 97 onward
- **Dynamic arrays (Excel 365/2019+):** INDEX with row_num=0 or column_num=0 spills automatically across cells
- **Legacy array formulas:** Older versions require Ctrl+Shift+Enter for array operations
- **Performance:** INDEX+MATCH is generally faster than VLOOKUP on large datasets because MATCH can use binary search on sorted data
- **Intersection operator:** Can use INDEX references with the intersection operator (space) for advanced range manipulation
- **Named ranges:** INDEX can be used in Name Manager to create dynamic named ranges

### Google Sheets

- **Availability:** All versions from Sheets' inception
- **Array handling:** Always handles arrays natively without special entry methods
- **Performance:** Excellent with full-column references (A:A); INDEX+MATCH scales well
- **ARRAYFORMULA:** Required for some array expansions; modern Sheets often auto-expands
- **Column/Row offset:** Identical behavior to Excel for row and column numbering
- **Query alternative:** For complex lookups, QUERY function can sometimes replace INDEX+MATCH

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Array entry | Ctrl+Shift+Enter (legacy) / Auto (365) | Auto |
| Dynamic arrays | Excel 365/2019+ | Always supported |
| XLOOKUP alternative | Available (365/2019+) | Not available |
| Full-column reference performance | Can slow in large files | Generally efficient |
| Reference form with multiple areas | Full support | Full support |

## Tips and Best Practices

1. **Always pair INDEX with MATCH for flexible lookups:** The INDEX+MATCH combination is more versatile than VLOOKUP because it can look in any direction, isn't limited by column order, and is more resilient to structural changes. Make `=INDEX(..., MATCH(...))` your default lookup pattern.

2. **Use absolute references on your ranges:** When copying INDEX+MATCH formulas, use $ signs (`$A$2:$A$100`) to prevent the ranges from shifting. The lookup value reference usually stays relative (`A2`) so it changes for each row.

3. **Cache MATCH results for multiple lookups:** If you're retrieving multiple columns for the same lookup, calculate MATCH once in a helper cell and reference it in multiple INDEX formulas. This improves performance and makes formulas easier to maintain.

4. **Remember that row/column numbers are relative to the range:** `INDEX(B5:D20, 3, 2)` returns the value at row 3, column 2 of that range (cell C7), not spreadsheet row 3. Always think in terms of position within the specified range.

5. **Use 0 to return entire rows or columns:** `INDEX(range, row, 0)` returns the entire row as an array; `INDEX(range, 0, col)` returns the entire column. This is powerful for aggregations: `=SUM(INDEX(Data, 0, MATCH("Sales", Headers, 0)))` sums the entire Sales column dynamically.

6. **Build dynamic ranges with INDEX:** Because INDEX returns a reference, you can use it as a range endpoint: `=SUM(A1:INDEX(A:A, COUNTA(A:A)))` sums all non-empty values without hardcoding the end row. This is essential for ranges that grow.

7. **Combine with SMALL or LARGE for Nth matches:** INDEX+MATCH returns the first match. For 2nd, 3rd, or Nth matches, use SMALL or LARGE with IF: `=INDEX(B:B, SMALL(IF(A:A="X", ROW(A:A)), 2))` returns the value for the 2nd occurrence of "X".

8. **Wrap in IFERROR for production formulas:** `=IFERROR(INDEX(..., MATCH(...)), "Not Found")` handles cases where the lookup value doesn't exist, preventing #N/A errors from cascading through your spreadsheet.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[VLOOKUP]] | Vertical lookup searching first column | When you need a simple left-to-right lookup and column positions won't change. Less flexible but more readable for simple cases. |
| [[HLOOKUP]] | Horizontal lookup searching first row | When your data is organized horizontally with headers on the left side rather than the top. |
| [[XLOOKUP]] | Modern lookup replacing VLOOKUP/HLOOKUP | Excel 365/2019 only. Cleaner syntax, built-in error handling, can look in any direction. Use when available. |
| [[OFFSET]] | Returns a reference offset from a starting cell | When you need to create dynamic ranges based on a starting position. Less efficient than INDEX for simple lookups. |
| [[INDIRECT]] | Returns a reference from a text string | When you need to construct references dynamically from text. More fragile than INDEX for most use cases. |
| [[CHOOSE]] | Returns a value from a list based on index number | When you have a small, fixed list of choices rather than a range. Simpler for 2-5 options. |

### Commonly Used Together

**[[MATCH]]** - Find position of a value in a range

*The classic INDEX+MATCH combination for flexible lookups:*
```
=INDEX(C2:C100, MATCH(A2, B2:B100, 0))
```
MATCH finds the row position of the lookup value, and INDEX returns the corresponding value from the result column. This is the fundamental pattern that makes INDEX+MATCH superior to VLOOKUP.

---

**[[COUNTA]]** - Count non-empty cells

*Combined with INDEX to find the last value in a column:*
```
=INDEX(A:A, COUNTA(A:A))
```
COUNTA counts filled cells, giving you the row number of the last entry. INDEX then retrieves that value. Perfect for finding the latest entry in a growing list.

---

**[[MAX]]/[[MIN]]** - Find maximum or minimum values

*Combined with INDEX+MATCH to return related data for the highest/lowest value:*
```
=INDEX(A2:A100, MATCH(MAX(B2:B100), B2:B100, 0))
```
Finds which row has the maximum value in column B, then returns the corresponding value from column A. Answer questions like "Which product had the highest sales?"

---

**[[ROW]]/[[COLUMN]]** - Return row or column numbers

*Combined with INDEX for dynamic row/column references:*
```
=INDEX(DataTable, ROW()-1, COLUMN()-4)
```
Use ROW() and COLUMN() to make INDEX formulas that automatically adjust based on their position, useful for creating matrix-style reports.

---

**[[IF]]** - Conditional logic

*Combined with INDEX+MATCH for conditional array lookups:*
```
=INDEX(C:C, MATCH(1, IF(A:A="Region1", IF(B:B="Product1", 1, 0), 0), 0))
```
Use IF within MATCH to create multi-criteria lookups. The IF generates an array of 1s and 0s, and MATCH finds the first 1.

---

**[[SMALL]]/[[LARGE]]** - Return Nth smallest/largest

*Combined with INDEX for Nth occurrence lookups:*
```
=INDEX(B:B, SMALL(IF(A:A="Target", ROW(A:A)), 2))
```
Returns the value from column B for the 2nd occurrence of "Target" in column A. Change the 2 to get 1st, 3rd, etc.

---

**[[IFERROR]]** - Handle errors gracefully

*Wrap INDEX+MATCH for production-ready formulas:*
```
=IFERROR(INDEX(C2:C100, MATCH(A2, B2:B100, 0)), "Not Found")
```
When the lookup value doesn't exist, returns "Not Found" instead of #N/A.

## Official Documentation

- **Microsoft Excel:** [INDEX function](https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)
- **Google Sheets:** [INDEX function](https://support.google.com/docs/answer/3098242)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with both array and reference forms |
| Excel 2007 | Enhanced | Improved performance with large datasets |
| Excel 2010 | Enhanced | Better array handling |
| Excel 2019/365 | Dynamic Arrays | Automatic spilling when returning rows/columns (row_num=0 or col_num=0) |
| Google Sheets | Original launch (2006) | Full compatibility with Excel's array form; reference form also supported |
| Google Sheets | 2018+ | Improved array handling and performance |

---

*Last updated: 2026-01-10*
