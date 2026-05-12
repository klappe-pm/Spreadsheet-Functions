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
- criteria-matching
- data-filtering
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Conditional Sum
- Sum If Condition
- Criteria Sum
tags:
- conditional
- aggregation
- criteria
- filtering
- wildcards
---

# SUMIF

## Description

**SUMIF** sums values based on a single condition. It examines each cell in a criteria range, checks if it matches your criterion, and if so, adds the corresponding value from the sum range to the total. This function is the workhorse of conditional aggregation—when you need totals for specific categories, regions, products, or any other single criterion.

The function has a quirky argument order that trips up many users: the criteria range comes first, then the criterion, then optionally the sum range. If you omit the sum range, SUMIF sums the criteria range itself (useful when you want to sum numbers that match a condition, like "sum all values greater than 100"). The criterion can be a number, text, cell reference, expression with operators (">50"), or wildcard pattern ("*East").

**Wildcard support is powerful but subtle.** Use `*` to match any sequence of characters and `?` to match any single character. `"*Smith"` matches "John Smith" and "Jane Smith". `"Sales?"` matches "Sales1" through "Sales9" but not "Sales10". To search for literal asterisks or question marks, prefix with a tilde: `"~*"` finds actual asterisks. Wildcards only work with text criteria—they have no effect on numeric comparisons.

**SUMIF vs SUMIFS:** SUMIF handles one condition; SUMIFS handles multiple. Confusingly, their argument order differs—SUMIFS puts the sum range first. If you're working with multiple criteria, SUMIFS is more powerful. For a single criterion, SUMIF is slightly more concise and works in older Excel versions. Both functions are case-insensitive for text matching.

## Syntax

> [!f(x)] SUMIF Syntax
>
> ```
> =SUMIF(range, criteria, [sum_range])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `range` | Yes | The range of cells to evaluate against the criteria. Must be the same size as sum_range if sum_range is specified. This is where your category labels, product names, dates, or other criteria values live. |
| `criteria` | Yes | The condition that determines which cells to sum. Can be a number (50), text ("Apples"), expression (">100", "<>Done"), cell reference (A1), or wildcard pattern ("*Corp"). Text criteria and expressions must be enclosed in quotes. |
| `sum_range` | No | The actual cells to sum when the corresponding criteria range cell matches. If omitted, SUMIF sums the range argument itself. Should be the same size as range; if smaller, SUMIF extends it to match (potentially causing unexpected results). |

### Return Value

Returns a single numeric value representing the sum of all cells in sum_range (or range if sum_range is omitted) where the corresponding cell in range matches the criteria. Returns 0 if no cells match the criteria. Returns an error if arguments are invalid.

## Examples

> [!f(x)] SUMIF Examples

### Example 1: Sum by Category
```
=SUMIF(A2:A10, "Apples", B2:B10)
```
**Result:** Sum of all values in B2:B10 where the corresponding cell in A2:A10 contains "Apples"

**Explanation:** The classic SUMIF use case. Column A contains product names, column B contains sales amounts. This totals sales for "Apples" only. The match is case-insensitive, so "apples", "APPLES", and "Apples" all match.

---

### Example 2: Sum Values Greater Than a Threshold
```
=SUMIF(B2:B20, ">1000")
```
**Result:** Sum of all values in B2:B20 that exceed 1000

**Explanation:** When you omit sum_range, SUMIF sums the criteria range itself. Here we're summing B2:B20 but only including values greater than 1000. The comparison operator goes inside quotes with the value.

---

### Example 3: Sum Values Not Equal to a Specific Value
```
=SUMIF(A2:A15, "<>Cancelled", C2:C15)
```
**Result:** Sum of C column values where A column is not "Cancelled"

**Explanation:** The `<>` operator means "not equal to." This sums order amounts for all orders except cancelled ones. Useful for excluding specific categories from totals.

---

### Example 4: Using Cell Reference as Criteria
```
=SUMIF(B2:B100, D1, C2:C100)
```
**Result:** Sum of C values where B matches the value in cell D1

**Explanation:** Instead of hardcoding the criterion, reference a cell. This makes your formula dynamic—change D1 and the sum updates. Perfect for dashboards and user-selectable reports.

---

### Example 5: Wildcard - Starts With Pattern
```
=SUMIF(A2:A50, "North*", B2:B50)
```
**Result:** Sum of B values where A starts with "North"

**Explanation:** The asterisk matches any characters. This matches "North", "Northeast", "Northwest", "North Region", etc. Case-insensitive, so "NORTHEAST" matches too.

---

### Example 6: Wildcard - Ends With Pattern
```
=SUMIF(C2:C100, "*Ltd", D2:D100)
```
**Result:** Sum for all companies ending in "Ltd"

**Explanation:** Place the asterisk at the start to match any prefix. Matches "Smith Ltd", "ABC Ltd", "International Trading Ltd", etc.

---

### Example 7: Wildcard - Contains Pattern
```
=SUMIF(A2:A200, "*consulting*", B2:B200)
```
**Result:** Sum for all entries containing "consulting" anywhere

**Explanation:** Asterisks on both ends match any text containing "consulting"—"ABC Consulting Inc", "consulting services", "Management Consulting Group", etc.

---

### Example 8: Single Character Wildcard
```
=SUMIF(A2:A30, "Product?", B2:B30)
```
**Result:** Sum for Product1, Product2, ... Product9

**Explanation:** The `?` matches exactly one character. "Product?" matches "ProductA", "Product1", "ProductX" but NOT "Product10" (two characters after "Product"). Use "Product??" for two characters.

---

### Example 9: Date Comparisons - Greater Than Date
```
=SUMIF(A2:A100, ">"&DATE(2025,1,1), B2:B100)
```
**Result:** Sum of B values where dates in A are after January 1, 2025

**Explanation:** For date comparisons, concatenate the operator with a DATE function. The `&` joins ">" with the date serial number. Also works with `">="&DATE(...)`, `"<"&DATE(...)`, etc.

---

### Example 10: Date Comparisons - Using Cell Reference
```
=SUMIF(A2:A100, ">="&E1, B2:B100)
```
**Result:** Sum of B values where dates in A are on or after the date in E1

**Explanation:** Combine operator with cell reference using `&`. If E1 contains a date, this sums all records from that date forward. Dynamic date filtering for reports.

---

### Example 11: Sum Negative Values Only
```
=SUMIF(C2:C50, "<0")
```
**Result:** Sum of all negative values in the range

**Explanation:** Sum only the losses, refunds, or debits. Since no sum_range is specified, it sums the criteria range itself where values are negative.

---

### Example 12: Finding Literal Asterisk or Question Mark
```
=SUMIF(A2:A20, "~*Special~*", B2:B20)
```
**Result:** Sum where A contains literal text "*Special*"

**Explanation:** The tilde `~` escapes wildcards. `~*` means literal asterisk, `~?` means literal question mark. Use when your data actually contains these characters.

---

### Example 13: Blank Cells Criteria
```
=SUMIF(A2:A100, "", B2:B100)
```
**Result:** Sum of B values where A is blank

**Explanation:** Empty quotes `""` match blank cells. This sums values that have no category assigned—useful for finding uncategorized data.

---

### Example 14: Non-Blank Cells Criteria
```
=SUMIF(A2:A100, "<>", B2:B100)
```
**Result:** Sum of B values where A is not blank

**Explanation:** `<>` alone (not equal to nothing) matches any non-blank cell. Sums all categorized values, excluding blanks.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Criteria range and sum_range are incompatible sizes in some contexts, or invalid criteria format | Ensure both ranges have the same dimensions. Check that criteria is properly formatted with quotes around text and operators. |
| `#NAME?` | Misspelled function or unquoted text in criteria | Ensure text criteria is in quotes: `"Apples"` not `Apples`. Check function spelling. |
| `0 unexpected` | No cells match the criteria, or criteria is case/format mismatch | Verify your criteria matches exactly (though case-insensitive). Check for leading/trailing spaces in data. Text "100" won't match number 100. |
| `Wrong sum` | Sum_range is smaller than criteria range | SUMIF extends smaller sum_range to match, which may include unintended cells. Always use equal-sized ranges. |
| `#REF!` | Referenced cells have been deleted | Check if any cells in your ranges have been removed. |
| `Dates not matching` | Date stored as text vs. actual date | Ensure dates are genuine date values, not text. Use DATEVALUE to convert text dates. |
| `Wildcards not working` | Trying to use wildcards with numbers | Wildcards only work with text criteria. For numeric conditions, use operators like ">", "<", etc. |

## Use Cases

### [[Sales Analysis by Product Category]]

**Scenario:** Calculate total revenue for each product category from a transaction log.

**Implementation:**
```
=SUMIF(C2:C5000, "Electronics", E2:E5000)
=SUMIF(C2:C5000, "Furniture", E2:E5000)
=SUMIF(C2:C5000, "Clothing", E2:E5000)
```
Where C contains category names and E contains sale amounts.

**Business Application:** Product performance analysis, category-level P&L statements, inventory planning by category, category manager reporting.

**Technical Details:** For dynamic reports, put category names in cells and reference them: `=SUMIF(C:C, G5, E:E)` where G5 contains the category. Build a summary table with categories in one column and SUMIF formulas pulling totals.

---

### [[Regional Sales Rollup]]

**Scenario:** Sum sales figures for each region using wildcard patterns to handle varying naming conventions.

**Implementation:**
```
=SUMIF(B2:B1000, "West*", D2:D1000)
=SUMIF(B2:B1000, "East*", D2:D1000)
=SUMIF(B2:B1000, "*Central*", D2:D1000)
```
Where B contains region names like "West Coast", "Eastern Division", "South Central".

**Business Application:** Regional performance comparison, territory management, sales rep assignment, geographic expansion analysis.

**Technical Details:** Wildcards provide flexibility when naming conventions vary. "West*" catches "West", "Western", "West Coast", "West Region". Consider creating a region mapping table for complex hierarchies.

---

### [[Accounts Receivable Aging]]

**Scenario:** Sum outstanding invoices by status or age category.

**Implementation:**
```
=SUMIF(D2:D500, "Overdue", F2:F500)
=SUMIF(D2:D500, "Current", F2:F500)
=SUMIF(D2:D500, "<>Paid", F2:F500)
```
Where D contains payment status and F contains invoice amounts.

**Business Application:** Cash flow forecasting, collections prioritization, credit risk assessment, working capital management.

**Technical Details:** Combine with date comparisons for aging buckets: `=SUMIF(E2:E500,"<"&TODAY()-30,F2:F500)` sums invoices dated more than 30 days ago.

---

### [[Expense Tracking by Department]]

**Scenario:** Calculate departmental expense totals for budget vs. actual reporting.

**Implementation:**
```
=SUMIF(Expenses[Department], "Marketing", Expenses[Amount])
=SUMIF(Expenses[Department], D3, Expenses[Amount])
```
Using structured table references for clarity.

**Business Application:** Departmental budget tracking, cost center analysis, variance reporting, resource allocation decisions.

**Technical Details:** Using Excel Tables or Named Ranges makes formulas self-documenting. The table automatically expands as you add data, keeping your SUMIF current.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 2003+)
- **Wildcards:** Full support for `*`, `?`, and `~` escape character
- **Performance:** Optimized for large datasets; handles millions of rows efficiently
- **Criteria flexibility:** Supports all comparison operators and text patterns
- **Case sensitivity:** Always case-insensitive for text matching

### Google Sheets
- **Availability:** All versions
- **Wildcards:** Full support matching Excel behavior
- **Performance:** May slow on very large datasets compared to Excel
- **Regular expressions:** Can use REGEXMATCH with SUMPRODUCT for regex patterns (SUMIF doesn't support regex)
- **Case sensitivity:** Always case-insensitive for text matching

### Both Platforms
- Text and empty cells in sum_range are treated as 0
- Dates can be compared using operators with DATE function or cell references
- Criteria is limited to one condition (use SUMIFS for multiple)
- Logical values (TRUE/FALSE) in sum_range are ignored
- The sum_range should match the size of the criteria range

## Tips and Best Practices

1. **Always use equal-sized ranges:** If sum_range is smaller than range, SUMIF extends it downward, potentially including unintended cells. Make ranges match exactly: `=SUMIF(A2:A100, "X", B2:B100)` not `=SUMIF(A2:A100, "X", B2:B50)`.

2. **Use cell references for dynamic criteria:** Instead of hardcoding `"Apples"`, reference a cell: `=SUMIF(A:A, F1, B:B)`. This enables interactive dashboards and what-if analysis.

3. **Concatenate operators with cell references:** For dynamic thresholds, use `">"&G1` where G1 contains your threshold value. Same pattern works for dates: `">="&DateCell`.

4. **Remember wildcards are text-only:** `"*"` and `"?"` work only for text matching, not numbers. For numeric ranges, use operators like `">100"` or use multiple SUMIF calls.

5. **Watch for text-formatted numbers:** If your sum range contains numbers stored as text, they'll be treated as 0. Look for green triangles in cell corners indicating this issue, and convert using VALUE or Paste Special.

6. **Use structured table references:** In Excel Tables, `=SUMIF(Sales[Region], "East", Sales[Revenue])` is clearer than `=SUMIF(B:B, "East", D:D)` and automatically adjusts as the table grows.

7. **For multiple criteria, switch to SUMIFS:** SUMIF handles one condition. For two or more criteria (e.g., region AND product), use SUMIFS. Don't nest SUMIFs—it won't work as expected.

8. **Trim spaces from criteria:** Leading or trailing spaces prevent matches. Use TRIM on your data or in your criteria: `=SUMIF(A:A, TRIM(F1), B:B)`.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[SUMIFS]] | Sum based on multiple conditions | When you need two or more criteria (AND logic) |
| [[COUNTIF]] | Count cells matching criteria | When you need the count, not the sum |
| [[AVERAGEIF]] | Average values matching criteria | When you need the average, not the sum |
| [[SUMPRODUCT]] | Sum of products with flexible conditions | When you need OR logic or complex array operations |
| [[DSUM]] | Database sum with structured criteria | When using a criteria range for complex queries |

### Commonly Used Together

**[[IF]]** - Add conditional logic around SUMIF results

*Check if category sales exceed target:*
```
=IF(SUMIF(A:A, "Electronics", B:B) > 10000, "Target Met", "Below Target")
```
Wraps SUMIF result in conditional logic for status indicators.

---

**[[IFERROR]]** - Handle potential errors gracefully

*Provide default value if SUMIF fails:*
```
=IFERROR(SUMIF(A:A, D1, B:B), 0)
```
Returns 0 instead of an error if something goes wrong.

---

**[[SUMIFS]]** - Add more conditions

*When single criterion isn't enough:*
```
=SUMIFS(C:C, A:A, "East", B:B, "Electronics")
```
SUMIFS handles multiple criteria with AND logic.

---

**[[MATCH]]** - Find what matched

*Locate first matching row:*
```
=MATCH("Apples", A:A, 0)
```
Use with INDEX to retrieve other data from matching rows.

---

**[[COUNTIF]]** - Count alongside sum

*Combined for weighted analysis:*
```
=SUMIF(A:A, "East", B:B) / COUNTIF(A:A, "East")
```
Calculates average (same as AVERAGEIF) by dividing sum by count.

## Official Documentation

- **Microsoft Excel:** [SUMIF function](https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)
- **Google Sheets:** [SUMIF function](https://support.google.com/docs/answer/3093583)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2003 | Original introduction |
| Excel 2007+ | All subsequent | Performance improvements, larger range support |
| Excel 2016+ | Office 365 | Dynamic array compatibility |
| Google Sheets | Original launch | Full compatibility with Excel syntax |

---

*Last updated: 2026-01-10*
