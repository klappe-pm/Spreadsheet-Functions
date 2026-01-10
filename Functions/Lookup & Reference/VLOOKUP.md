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
- table-lookup
- reference
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Vertical Lookup
- V Lookup
- Table Lookup
tags:
- lookup
- reference
- data-retrieval
- table
---

# VLOOKUP

## Description

**VLOOKUP (Vertical Lookup)** searches for a value in the first column of a table and returns a value from another column in the same row. It's the classic "find and fetch" function—give it an ID, get back the name; give it a product code, get back the price; give it an employee number, get back their department. For decades, VLOOKUP was the go-to function for connecting data across spreadsheets.

The "V" stands for vertical because it searches **down** a column. The function looks in the leftmost column of your table range, finds your search value, then moves right to the column number you specify and returns that value. This left-to-right limitation is VLOOKUP's most significant constraint—your lookup column must be the first column in your range.

**The approximate vs. exact match confusion:** VLOOKUP's fourth parameter (range_lookup) trips up countless users. TRUE (or omitted) means approximate match—useful for tax brackets and grade scales where you want "the closest value without going over." FALSE (or 0) means exact match—what you need 90% of the time for looking up IDs, codes, and specific values. **Always use FALSE unless you specifically need approximate matching.**

**VLOOKUP is being superseded.** Microsoft introduced XLOOKUP in 2019, which eliminates VLOOKUP's limitations: XLOOKUP can look left, handle missing values gracefully, and doesn't require column numbers. Google Sheets doesn't have XLOOKUP yet, but INDEX/MATCH has always been more flexible than VLOOKUP. That said, VLOOKUP remains the most widely-used lookup function—you'll encounter it in virtually every workplace spreadsheet, and understanding it is essential.

## Syntax

> [!f(x)] VLOOKUP Syntax
>
> ```
> =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `lookup_value` | Yes | The value to search for in the first column of table_array. Can be a cell reference, text (in quotes), number, or formula result. |
| `table_array` | Yes | The table range to search. The first column of this range is where VLOOKUP looks for lookup_value. Subsequent columns contain the data you want to retrieve. |
| `col_index_num` | Yes | The column number (starting at 1) in table_array from which to return a value. 1 = first column (lookup column itself), 2 = second column, etc. |
| `range_lookup` | No | TRUE (default) for approximate match, FALSE for exact match. Use FALSE for most lookups. TRUE requires the first column to be sorted ascending. |

### Return Value

Returns the value from the specified column in the row where the lookup value was found. Returns #N/A if no match is found (exact match mode) or if lookup_value is smaller than the smallest value in the lookup column (approximate match mode).

## Examples

> [!f(x)] VLOOKUP Examples

### Example 1: Basic Exact Match Lookup
```
=VLOOKUP("P001", A2:D100, 3, FALSE)
```
**Result:** Returns the value from column 3 where "P001" is found in column 1

**Explanation:** Searches column A for "P001", finds it, returns the value from the 3rd column of the range (column C). FALSE ensures exact match. This is the most common VLOOKUP pattern—finding a specific record by ID.

---

### Example 2: Using a Cell Reference as Lookup Value
```
=VLOOKUP(A2, Products!$A$2:$D$500, 2, FALSE)
```
**Result:** Looks up whatever value is in A2, returns column 2 from Products sheet

**Explanation:** Instead of hardcoding "P001", we reference cell A2. The formula can now be dragged down to look up different values for each row. Note the $ signs making the table range absolute—essential when copying formulas.

---

### Example 3: Lookup with Column Name Using MATCH
```
=VLOOKUP(A2, $B$1:$F$100, MATCH("Price", $B$1:$F$1, 0), FALSE)
```
**Result:** Returns the Price column for the item in A2

**Explanation:** Instead of hardcoding column number 3, MATCH finds which column "Price" is in. If someone inserts a column, the formula still works. This VLOOKUP+MATCH combo is a classic pattern for resilient formulas.

---

### Example 4: Approximate Match for Tax Brackets
```
=VLOOKUP(B2, TaxTable!$A$2:$B$7, 2, TRUE)
```
Where TaxTable has: 0→10%, 10000→15%, 40000→22%, 85000→24%, 165000→32%, 215000→35%

**Result:** Returns the tax rate for income in B2

**Explanation:** TRUE (approximate match) finds the largest value ≤ lookup_value. Income of $50,000 matches the $40,000 bracket (returning 22%), not $85,000. The lookup column MUST be sorted ascending for this to work correctly.

---

### Example 5: Handling #N/A with IFERROR
```
=IFERROR(VLOOKUP(A2, DataTable, 3, FALSE), "Not Found")
```
**Result:** Returns column 3 value if found, "Not Found" if lookup fails

**Explanation:** VLOOKUP returns #N/A when it can't find a match. Wrapping in IFERROR provides a graceful fallback. Common alternatives: 0, "", or "N/A" depending on what makes sense for your data.

---

### Example 6: Looking Up from Another Workbook
```
=VLOOKUP(A2, '[Inventory.xlsx]Products'!$A$2:$D$1000, 4, FALSE)
```
**Result:** Looks up A2 in the Products sheet of Inventory.xlsx file

**Explanation:** Reference external workbooks with [Filename.xlsx]SheetName! syntax. Both files must be open for real-time updates. When the source file is closed, the path becomes a full file path string.

---

### Example 7: Case-Sensitive VLOOKUP (Workaround)
```
=INDEX(C2:C100, MATCH(TRUE, EXACT(A2:A100, "ABC"), 0))
```
**Result:** Finds "ABC" exactly, not "abc" or "Abc"

**Explanation:** Standard VLOOKUP is case-insensitive. For case-sensitive lookups, use INDEX/MATCH with EXACT. This array formula (Ctrl+Shift+Enter in older Excel) finds the exact case match.

---

### Example 8: Returning Multiple Columns
```
Column D: =VLOOKUP($A2, Products!$A:$E, 2, FALSE)
Column E: =VLOOKUP($A2, Products!$A:$E, 3, FALSE)
Column F: =VLOOKUP($A2, Products!$A:$E, 4, FALSE)
```
**Result:** Retrieves columns 2, 3, and 4 for the item in A2

**Explanation:** To pull multiple columns, you need multiple VLOOKUPs. The $ on $A2 keeps the lookup value fixed while copying across. This is inefficient—consider INDEX/MATCH or XLOOKUP which can return arrays.

---

### Example 9: Two-Way Lookup (VLOOKUP + MATCH)
```
=VLOOKUP(A2, DataTable, MATCH(B1, HeaderRow, 0), FALSE)
```
**Result:** Finds row by A2, column by B1, returns intersection

**Explanation:** When you need to look up both row and column dynamically, combine VLOOKUP with MATCH. MATCH finds which column number corresponds to the header in B1. Alternative: use INDEX with two MATCH functions.

---

### Example 10: Looking Up with Wildcards
```
=VLOOKUP("*"&A2&"*", B:D, 2, FALSE)
```
**Result:** Finds any cell in column B containing the text in A2

**Explanation:** Use * (any characters) and ? (single character) wildcards for partial matching. This finds "John" within "John Smith" or "Dr. John". Only works with exact match (FALSE). Wildcards are powerful for fuzzy matching.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | Value not found in lookup column | Check spelling, leading/trailing spaces (use TRIM), data types (text vs number). Verify value exists in table. |
| `#REF!` | col_index_num exceeds the number of columns in table_array | If table has 4 columns, col_index_num can't be 5. Expand your table range or reduce column number. |
| `#VALUE!` | col_index_num is less than 1, or invalid parameter types | Column number must be ≥1. Ensure lookup_value isn't an error. |
| `Wrong result` | Approximate match finding wrong row | Using TRUE when you meant FALSE. Use FALSE for exact matching. If using TRUE, ensure column is sorted ascending. |
| `Wrong result` | Duplicate values in lookup column | VLOOKUP returns the FIRST match only. Use FILTER or INDEX/MATCH for handling duplicates. |
| `#NAME?` | Function spelled wrong or named range undefined | Check spelling. Verify named ranges exist if used. |

## Use Cases

### [[Employee Information Lookup]]

**Scenario:** Given an employee ID in a timesheet, pull in their name, department, and hourly rate from the master employee database.

**Implementation:**
```
Name: =VLOOKUP($A2, Employees!$A:$F, 2, FALSE)
Dept: =VLOOKUP($A2, Employees!$A:$F, 4, FALSE)
Rate: =VLOOKUP($A2, Employees!$A:$F, 6, FALSE)
```

**Business Application:** Time tracking, payroll processing, HR reporting. Eliminates manual data entry and ensures consistency with master records.

**Technical Details:** Use $ on the lookup cell ($A2) to allow copying across columns. Make the table range absolute ($A:$F) to prevent shifting when copying down. Consider XLOOKUP or INDEX/MATCH for better performance.

---

### [[Price List Integration]]

**Scenario:** Sales orders contain product codes; automatically pull in current prices from the master price list.

**Implementation:**
```
=VLOOKUP(B2, PriceList!$A:$D, MATCH("Unit Price", PriceList!$1:$1, 0), FALSE)
```

**Business Application:** Quote generation, invoice creation, inventory valuation. Ensures pricing consistency and enables instant price updates when the master list changes.

**Technical Details:** Using MATCH for column number makes the formula resilient to column insertions in the price list. Consider caching the MATCH result in a separate cell for performance.

---

### [[Grade Assignment System]]

**Scenario:** Convert numeric scores to letter grades using a grading scale.

**Implementation:**
```
=VLOOKUP(B2, GradeScale, 2, TRUE)
```
Where GradeScale is: 0→F, 60→D, 70→C, 80→B, 90→A

**Business Application:** Educational grading, performance rating systems, any tiered classification based on thresholds.

**Technical Details:** TRUE (approximate match) is correct here—a score of 85 should match the 80 row (B grade), not require an exact 85 entry. Lookup column MUST be sorted ascending.

---

### [[Inventory Management]]

**Scenario:** Track stock levels by looking up product details from a central inventory database.

**Implementation:**
```
=IFERROR(VLOOKUP(A2, Inventory!$A:$E, 3, FALSE), "Product Not Found")
```

**Business Application:** Warehouse management, reorder point monitoring, stock valuation. Connect transaction data to master product information.

**Technical Details:** IFERROR handles new products not yet in the system gracefully. For high-volume lookups, consider loading the entire lookup result into Power Query or using database connections.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 onward)
- **Case sensitivity:** Case-insensitive (abc = ABC = Abc)
- **Performance:** Can be slow with large datasets; consider INDEX/MATCH or XLOOKUP
- **Wildcards:** Fully supported (* and ?)
- **XLOOKUP alternative:** Available in Excel 2019, 365, and later

### Google Sheets
- **Availability:** All versions
- **Case sensitivity:** Case-insensitive (same as Excel)
- **Performance:** Generally efficient; full-column references (A:E) work well
- **Wildcards:** Supported with exact match (FALSE)
- **No XLOOKUP:** Use INDEX/MATCH for similar flexibility

### Both Platforms
- Searches the FIRST column of table_array only
- Cannot look left (lookup column must be leftmost)
- Returns first match only (doesn't handle duplicates)
- Approximate match requires sorted data

## Tips and Best Practices

1. **Always use FALSE for exact match:** TRUE (approximate) is rarely what you want. Make it a habit: `=VLOOKUP(..., FALSE)` every time unless you're doing tiered lookups.

2. **Lock your table reference:** Use $ signs (`$A$2:$D$100`) so the range doesn't shift when you copy the formula. Even better, use a named range.

3. **Use MATCH for column numbers:** `=VLOOKUP(A2, Table, MATCH("Column Name", Headers, 0), FALSE)` survives column insertions and is more readable.

4. **Wrap in IFERROR for clean output:** `=IFERROR(VLOOKUP(...), "")` prevents #N/A from cluttering your sheet and breaking downstream formulas.

5. **Consider INDEX/MATCH instead:** It's more flexible (can look left), often faster, and easier to audit. VLOOKUP is more readable for simple cases, but INDEX/MATCH handles complex scenarios better.

6. **Watch for data type mismatches:** "123" (text) ≠ 123 (number). If lookups fail inexplicably, check whether your lookup value and table column are the same type.

7. **Use TRIM to handle spaces:** Hidden leading/trailing spaces break lookups. Use `=VLOOKUP(TRIM(A2), ...)` to be safe.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[XLOOKUP]] | Modern replacement for VLOOKUP | When you need to look left, want default values, or prefer cleaner syntax (Excel 365/2019+) |
| [[HLOOKUP]] | Horizontal lookup (searches across rows) | When your table is arranged horizontally with headers on the left |
| [[INDEX]]+[[MATCH]] | Flexible lookup combination | When you need to look left, handle multiple criteria, or want better performance |
| [[LOOKUP]] | Simplified lookup (legacy) | Rarely—mostly for backward compatibility |

### Commonly Used Together

**[[MATCH]]** - Find position in range

*Combined with VLOOKUP for dynamic column selection:*
```
=VLOOKUP(A2, Table, MATCH("Header", HeaderRow, 0), FALSE)
```
MATCH finds which column number contains "Header", making the formula resilient to column changes.

---

**[[IFERROR]]** - Handle lookup failures

*Combined with VLOOKUP for graceful error handling:*
```
=IFERROR(VLOOKUP(A2, Table, 2, FALSE), "Not found")
```
Returns "Not found" instead of #N/A when lookup fails.

---

**[[INDIRECT]]** - Dynamic range references

*Combined with VLOOKUP for dynamic table selection:*
```
=VLOOKUP(A2, INDIRECT(B2&"!A:D"), 3, FALSE)
```
The table range is determined by the sheet name in B2.

---

**[[INDEX]]** - Return value at intersection

*Alternative to VLOOKUP with more flexibility:*
```
=INDEX(C:C, MATCH(A2, A:A, 0))
```
INDEX/MATCH can look in any direction and handles complex scenarios VLOOKUP can't.

---

**[[IF]]** - Conditional logic

*Combined with VLOOKUP for conditional lookups:*
```
=IF(A2<>"", VLOOKUP(A2, Table, 2, FALSE), "")
```
Only performs lookup if A2 has a value, avoiding unnecessary #N/A errors.

## Official Documentation

- **Microsoft Excel:** [VLOOKUP function](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1)
- **Google Sheets:** [VLOOKUP function](https://support.google.com/docs/answer/3093318)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation |
| Excel 2007 | Enhanced | Better performance with large datasets |
| Excel 2019/365 | XLOOKUP introduced | Modern alternative with more features |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
