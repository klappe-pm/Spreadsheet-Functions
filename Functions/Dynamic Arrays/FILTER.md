---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics:
- data-filtering
- conditional-extraction
- array-manipulation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Array Filter
- Data Filter
- Conditional Filter
tags:
- dynamic-array
- filtering
- conditional
- data-extraction
- spill
---

# FILTER

## Description

**FILTER** is one of the most powerful dynamic array functions available in modern spreadsheets. It extracts rows (or columns) from a range that meet criteria you specify, returning a dynamic array that automatically spills into adjacent cells. Think of it as a programmable version of Excel's AutoFilter feature—instead of hiding rows, FILTER extracts matching data into a new location that updates automatically when your source data or criteria change.

Before FILTER existed, extracting matching records required complex array formulas with INDEX/MATCH combinations or helper columns with IF statements. FILTER simplifies this dramatically: `=FILTER(A2:D100, B2:B100="Sales")` instantly extracts all Sales department rows. The function accepts multiple conditions using AND/OR logic through multiplication (*) and addition (+), making sophisticated filtering possible in a single formula.

**The empty result problem:** FILTER's most common gotcha is what happens when no rows match your criteria. By default, it returns a #CALC! error in Excel or #N/A in Google Sheets. This is rarely what you want—a blank or "No results" message is usually preferable. The optional `if_empty` parameter lets you specify what to return when nothing matches: `=FILTER(data, criteria, "No matches found")`. Always use this parameter for production formulas.

**Platform availability note:** FILTER is available in Excel 365, Excel 2021, Excel for web, and Google Sheets. It's not available in Excel 2019 or earlier perpetual license versions. In Google Sheets, FILTER has been available since the early days and works identically to Excel's implementation, making cross-platform formulas straightforward. The main difference is error handling—Excel returns #CALC! for empty results while Sheets returns #N/A—but both accept the if_empty parameter to handle this gracefully.

## Syntax

> [!f(x)] FILTER Syntax
>
> ```
> =FILTER(array, include, [if_empty])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `array` | Yes | The range or array to filter. Can be a single column, single row, or multi-column/row range. This is the data that will be returned for matching records. |
| `include` | Yes | A Boolean array (TRUE/FALSE values) the same height or width as array. Rows/columns where include is TRUE are returned. Typically created with comparison operators: `B2:B100="Sales"` generates an array of TRUE/FALSE. |
| `if_empty` | No | Value to return when no rows match the criteria. Can be text ("No results"), a number (0), or an array. If omitted, returns #CALC! (Excel) or #N/A (Sheets) when filter returns nothing. |

### Return Value

Returns a dynamic array containing the rows (or columns) from array where the corresponding include value is TRUE. The result spills into adjacent cells automatically. If no values match, returns the if_empty value or an error if if_empty is not specified.

## Examples

> [!f(x)] FILTER Examples

### Example 1: Basic Single-Column Filter
```
=FILTER(A2:A100, B2:B100="Active")
```
**Result:** Returns all values from column A where the corresponding column B value is "Active"

**Explanation:** The simplest FILTER pattern. The include array `B2:B100="Active"` creates a column of TRUE/FALSE values. Only A2:A100 values where the corresponding position is TRUE are returned. The result spills vertically into as many cells as needed.

---

### Example 2: Filtering Multiple Columns
```
=FILTER(A2:D100, E2:E100>1000)
```
**Result:** Returns all four columns (A through D) for rows where column E exceeds 1000

**Explanation:** FILTER returns the entire array width you specify. If you want multiple columns, include them all in the first parameter. Here, sales records over $1000 are extracted with all their detail columns intact.

---

### Example 3: Handling Empty Results with if_empty
```
=FILTER(A2:C100, B2:B100="Platinum", "No Platinum customers found")
```
**Result:** Matching rows, or the message if none exist

**Explanation:** The third parameter prevents the ugly #CALC! error when no rows match. For user-facing spreadsheets, always include if_empty. You can return text, a number, or even an array like `{"No","Results","Found"}` to match your column count.

---

### Example 4: Multiple Conditions with AND Logic (*)
```
=FILTER(A2:D100, (B2:B100="Sales")*(C2:C100>50000))
```
**Result:** Rows where department is Sales AND amount exceeds 50,000

**Explanation:** Multiply conditions for AND logic. TRUE=1, FALSE=0, so TRUE*TRUE=1 (included), TRUE*FALSE=0 (excluded). Both conditions must be TRUE. Note the parentheses around each condition—they're essential for correct evaluation.

---

### Example 5: Multiple Conditions with OR Logic (+)
```
=FILTER(A2:D100, (B2:B100="Urgent")+(B2:B100="Critical"))
```
**Result:** Rows where status is either "Urgent" OR "Critical"

**Explanation:** Add conditions for OR logic. TRUE+TRUE=2 (truthy), TRUE+FALSE=1 (truthy), FALSE+FALSE=0 (excluded). Any non-zero result includes the row. This extracts high-priority items regardless of which specific priority level.

---

### Example 6: Combining AND and OR Conditions
```
=FILTER(A2:E100, ((B2:B100="East")+(B2:B100="West"))*(D2:D100>=1000))
```
**Result:** Rows where region is East OR West, AND amount is at least 1000

**Explanation:** Combine AND (*) and OR (+) for complex criteria. The parentheses group the OR conditions together, then multiply by the AND condition. This finds high-value transactions from either coast region.

---

### Example 7: Filtering with Cell Reference Criteria
```
=FILTER(A2:D100, C2:C100=G1)
```
**Result:** Rows where column C matches the value in cell G1

**Explanation:** Instead of hardcoding criteria, reference cells for dynamic filtering. Users can type different values in G1 to filter for different categories. This pattern creates interactive dashboards without VBA or complex setups.

---

### Example 8: Date Range Filtering
```
=FILTER(A2:E100, (C2:C100>=DATE(2024,1,1))*(C2:C100<=DATE(2024,12,31)))
```
**Result:** All rows where the date in column C falls within year 2024

**Explanation:** Dates are numbers in spreadsheets, so comparison operators work directly. This extracts an entire year's transactions. Use cell references for start/end dates to make the filter adjustable.

---

### Example 9: Filtering with Wildcards Using SEARCH (Partial Match)
```
=FILTER(A2:D100, ISNUMBER(SEARCH("corp", B2:B100)))
```
**Result:** Rows where column B contains "corp" anywhere in the text

**Explanation:** FILTER doesn't support wildcards directly, but SEARCH/FIND return numbers for matches and errors for non-matches. ISNUMBER converts this to TRUE/FALSE. This finds "Acme Corp", "Corporation Inc", etc. SEARCH is case-insensitive; use FIND for case-sensitive.

---

### Example 10: Filtering with NOT Condition
```
=FILTER(A2:D100, B2:B100<>"Cancelled")
```
**Result:** All rows except those where column B is "Cancelled"

**Explanation:** The `<>` operator means "not equal to." This excludes cancelled orders, terminated employees, or any other specific value you want to filter out.

---

### Example 11: Top N Filter Using LARGE
```
=FILTER(A2:C100, B2:B100>=LARGE(B2:B100, 10))
```
**Result:** Rows with the 10 highest values in column B

**Explanation:** LARGE(range, 10) returns the 10th largest value. Filtering for values >= this threshold returns the top 10 rows. Note: if there are ties at the cutoff point, you may get more than 10 rows.

---

### Example 12: Nested FILTER for Complex Extraction
```
=FILTER(FILTER(A2:E100, C2:C100="Completed"), B2:B100>1000)
```
**Result:** Completed transactions over $1000

**Explanation:** Nest FILTER functions for step-by-step filtering. The inner FILTER extracts completed items, the outer FILTER then filters those for amounts over $1000. Note: the outer filter's column references (B2:B100) still refer to original data positions—this can be tricky to manage.

---

### Example 13: Filtering and Sorting Together
```
=SORT(FILTER(A2:D100, C2:C100="Priority"), 2, -1)
```
**Result:** Priority rows sorted by column 2 in descending order

**Explanation:** Combine FILTER with SORT to both extract and organize data in one formula. FILTER extracts priority items, then SORT arranges them by the second column (descending). This creates dynamic, self-updating ranked lists.

---

### Example 14: FILTER with UNIQUE for Distinct Filtered Values
```
=UNIQUE(FILTER(B2:B100, A2:A100="2024"))
```
**Result:** Unique values from column B where column A is "2024"

**Explanation:** Chain FILTER with UNIQUE to get distinct values from a filtered subset. This finds all unique product names sold in 2024, or all unique customers in a specific region—without duplicates.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#CALC!` (Excel) / `#N/A` (Sheets) | No rows match the filter criteria | Add the if_empty parameter: `=FILTER(data, criteria, "No results")` |
| `#VALUE!` | Include array size doesn't match array size | Ensure the include condition range has the same number of rows (or columns) as the array being filtered. |
| `#REF!` | Filtered result has no room to spill | Clear cells below/right of the formula to allow the dynamic array to expand. |
| `#SPILL!` (Excel only) | Spill range contains data or merged cells | Remove data or unmerge cells in the spill range. Excel needs empty cells for results. |
| `Wrong results` | Parentheses missing in compound conditions | Always wrap each condition in parentheses: `(A="X")*(B>10)` not `A="X"*B>10` |
| `#NAME?` | Function not available in your Excel version | FILTER requires Excel 365, Excel 2021, or Google Sheets. Not available in Excel 2019 or earlier. |

## Use Cases

### [[Sales Pipeline Filtering]]

**Scenario:** A sales manager needs to see all open opportunities over $50,000 in their region, updated in real-time as the CRM data syncs to the spreadsheet.

**Implementation:**
```
=FILTER(Opportunities!A2:G500,
  (Opportunities!C2:C500="Open")*
  (Opportunities!E2:E500>50000)*
  (Opportunities!D2:D500=SalesRep!$B$2),
  "No qualifying opportunities")
```

**Business Application:** Replaces static report extracts with live, filtered views. Sales reps see their deals instantly without running reports. Combine with SORT to rank by expected close date or deal value.

**Technical Details:** The three conditions are multiplied for AND logic: Status must be "Open" AND Amount must exceed $50,000 AND Region must match the current user. The if_empty parameter provides a clean message instead of an error when the pipeline is empty.

---

### [[Inventory Reorder Alert System]]

**Scenario:** Warehouse manager needs a dynamic list of products below reorder point, showing item details and current stock levels.

**Implementation:**
```
=FILTER(Inventory!A2:F1000,
  Inventory!D2:D1000<Inventory!E2:E1000,
  "All items adequately stocked")
```
Where column D is current stock and E is reorder point.

**Business Application:** Creates a live reorder list that updates as inventory transactions are logged. Purchasing can export or print this list daily. Eliminates manual inventory checking and missed reorders.

**Technical Details:** The condition compares two columns—current stock vs. reorder threshold. Items where stock has fallen below the threshold appear in the filtered result. Add SORT to prioritize by days of supply remaining or criticality.

---

### [[Employee Directory Search]]

**Scenario:** HR department needs a searchable employee directory where typing a department name shows all employees in that department with their contact information.

**Implementation:**
```
=FILTER(Directory!A2:E500,
  (Directory!C2:C500=$H$1)+(ISNUMBER(SEARCH($H$1, Directory!B2:B500))),
  "No employees match your search")
```
Where H1 contains the search term, column B is employee name, column C is department.

**Business Application:** Creates an interactive lookup without requiring database skills. Works for exact department matches OR partial name matches. Combine with data validation dropdown for department selection.

**Technical Details:** The OR logic (+) allows matching either the department exactly OR finding the search term within employee names. SEARCH handles partial matching. The spilled result updates instantly as users type in the search cell.

---

### [[Financial Transaction Audit]]

**Scenario:** Auditors need to extract all transactions above a certain threshold or flagged for review from a large transaction log.

**Implementation:**
```
=FILTER(Transactions!A2:H10000,
  (Transactions!E2:E10000>=$K$1)+
  (Transactions!G2:G10000="FLAGGED"),
  "No transactions require review")
```
Where K1 contains the amount threshold and column G contains review flags.

**Business Application:** Enables rapid audit sampling without database queries. Auditors adjust the threshold in K1 to expand or narrow their sample. Flagged transactions always appear regardless of amount.

**Technical Details:** OR logic captures both high-value transactions AND any flagged items. The result can be further analyzed with SUM, COUNT, or exported for detailed testing. Real-time filtering beats static audit extracts that become stale.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 365 (subscription), Excel 2021 (perpetual), Excel for web
- **Empty result behavior:** Returns #CALC! when no matches (unique to dynamic array functions)
- **Spill behavior:** Results spill into adjacent cells automatically; #SPILL! error if blocked
- **Performance:** Optimized for large datasets; handles hundreds of thousands of rows efficiently
- **Case sensitivity:** Text comparisons are case-insensitive by default

### Google Sheets
- **Availability:** All versions (FILTER has been available since early Google Sheets)
- **Empty result behavior:** Returns #N/A when no matches
- **Spill behavior:** Results expand automatically; no specific spill error—overwrites or errors if blocked
- **Performance:** Excellent for typical datasets; may slow on very large ranges
- **Case sensitivity:** Text comparisons are case-insensitive (same as Excel)

### Key Difference Alert
The primary difference is error handling. Excel's #CALC! and Sheets' #N/A for empty results can break downstream formulas differently. Always use the if_empty parameter for cross-platform compatibility. Also, Google Sheets has had FILTER much longer than Excel, so many Sheets-native formulas use FILTER patterns that older Excel users may not recognize.

## Tips and Best Practices

1. **Always include the if_empty parameter:** Production formulas should never show #CALC! or #N/A to users. Even if you expect results, data changes—handle the empty case gracefully with `"No results"` or an empty string `""`.

2. **Use parentheses around every condition in compound filters:** `(A="X")*(B>10)` is correct. `A="X"*B>10` evaluates incorrectly. This is the most common FILTER debugging issue.

3. **Combine FILTER with SORT and UNIQUE:** These functions chain beautifully. `=SORT(FILTER(...))` or `=UNIQUE(FILTER(...))` creates powerful data processing pipelines in a single formula.

4. **Reference cells for dynamic criteria:** Instead of hardcoding `"Sales"`, use `=FILTER(data, dept=G1)` where G1 contains "Sales". Users can change G1 to see different departments without editing the formula.

5. **Consider named ranges for readability:** `=FILTER(SalesData, Region="East")` is clearer than `=FILTER(Sheet2!A2:G10000, Sheet2!C2:C10000="East")`. Name your data ranges.

6. **Be mindful of spill range space:** FILTER results can grow as your source data grows. Leave ample empty cells below/right of the formula. In Excel, blocked spill ranges cause #SPILL! errors.

7. **For NOT conditions, use <>:** `=FILTER(data, status<>"Cancelled")` excludes cancelled items. Simpler than complex Boolean logic for single exclusions.

8. **Test with edge cases:** What happens when ALL rows match? When NONE match? When the source data is empty? Robust formulas handle these scenarios.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[QUERY]] | SQL-like filtering (Google Sheets only) | When you need GROUP BY, aggregation, or SQL-like syntax in Sheets |
| [[Advanced Filter]] | Excel's built-in filter feature | When you need in-place filtering with complex criteria ranges (Excel) |
| [[DGET]] | Database function for single value extraction | When you need exactly one value from filtered data, with error if multiple matches |
| [[INDEX/MATCH with IF]] | Pre-dynamic array filtering approach | When working in Excel 2019 or earlier without FILTER function |

### Commonly Used Together

**[[SORT]]** - Arrange filtered results

*Combined with FILTER for filtered, sorted output:*
```
=SORT(FILTER(A2:D100, B2:B100="Active"), 3, -1)
```
Filters for active records, then sorts by column 3 descending. Creates dynamic ranked lists.

---

**[[UNIQUE]]** - Remove duplicates from filtered data

*Combined with FILTER for distinct filtered values:*
```
=UNIQUE(FILTER(C2:C100, A2:A100="2024"))
```
Gets unique values from column C where column A is 2024. Perfect for dynamic dropdown lists.

---

**[[SORT]]** + **[[UNIQUE]]** - Filter, dedupe, and sort

*Triple combination for polished output:*
```
=SORT(UNIQUE(FILTER(B2:B100, A2:A100>0)))
```
Filters positive values, removes duplicates, then sorts alphabetically.

---

**[[SUMPRODUCT]]** - Count or sum filtered results

*Count matching rows:*
```
=ROWS(FILTER(A2:A100, B2:B100="Complete", ""))
```
ROWS counts the filtered result. Use IFERROR or if_empty to handle zero matches.

---

**[[IFERROR]]** - Wrap for legacy error handling

*Alternative to if_empty parameter:*
```
=IFERROR(FILTER(data, criteria), "No matches")
```
Older pattern before if_empty parameter was widely known. if_empty parameter is preferred.

---

**[[CHOOSECOLS]]** / **[[CHOOSEROWS]]** - Select specific columns from filtered results

*Extract specific columns from filtered data:*
```
=CHOOSECOLS(FILTER(A2:F100, G2:G100="Yes"), 1, 3, 5)
```
Filters rows, then returns only columns 1, 3, and 5 from those rows.

## Official Documentation

- **Microsoft Excel:** [FILTER function](https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759)
- **Google Sheets:** [FILTER function](https://support.google.com/docs/answer/3093197)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Google Sheets | 2006 (original) | Available since early Google Sheets |
| Excel 365 | 2018 (Insider), 2019 (general) | Part of dynamic array rollout |
| Excel 2021 | 2021 | First perpetual license version with FILTER |
| Excel for web | 2019 | Full support in browser version |
| Excel 2019 and earlier | Not available | Use INDEX/MATCH with array formulas as alternative |

---

*Last updated: 2026-01-10*
