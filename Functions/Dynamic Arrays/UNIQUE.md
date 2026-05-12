---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics:
- deduplication
- distinct-values
- data-cleaning
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Distinct Values
- Remove Duplicates
- Dedupe
tags:
- dynamic-array
- unique
- deduplication
- distinct
- spill
---

# UNIQUE

## Description

**UNIQUE** extracts distinct values from a range or array, returning a dynamic array with duplicates removed. Before this function existed, getting a unique list required either the Remove Duplicates feature (which modifies source data) or complex array formulas with COUNTIF. UNIQUE solves this elegantly: `=UNIQUE(A2:A100)` instantly produces a list of distinct values that updates automatically as your source data changes.

The function offers two modes: by default, it returns values that appear one or more times (deduplication). With the optional exactly_once parameter set to TRUE, it returns only values that appear exactly once—no duplicates in either direction. This second mode is useful for finding outliers or items that haven't been matched/reconciled.

**Multi-column uniqueness:** UNIQUE can evaluate uniqueness across multiple columns simultaneously. `=UNIQUE(A2:C100)` returns rows where the combination of columns A, B, and C is unique—even if individual columns have duplicates. This is essential for removing duplicate records where "duplicate" means matching on multiple fields, like Name + Date or ProductID + Location.

**Platform considerations:** UNIQUE is available in Excel 365, Excel 2021, and Google Sheets. The Excel version includes the exactly_once parameter, which Google Sheets lacks as of this writing. In Sheets, you'd need to combine UNIQUE with COUNTIF to achieve the "exactly once" behavior. Both platforms handle the by_col parameter for column-wise uniqueness (useful for transposed data), though this is rarely needed.

## Syntax

> [!f(x)] UNIQUE Syntax
>
> ```
> =UNIQUE(array, [by_col], [exactly_once])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `array` | Yes | The range or array from which to extract unique values. Can be a single column, single row, or multi-column/row range. For multi-column ranges, uniqueness is evaluated across all columns together. |
| `by_col` | No | FALSE (default) compares rows for uniqueness. TRUE compares columns for uniqueness (horizontal data). Most data is row-based, so FALSE is almost always correct. |
| `exactly_once` | No | FALSE (default) returns all distinct values. TRUE returns only values that appear exactly once in the array—useful for finding unmatched or unrepeated items. Excel only; not available in Google Sheets. |

### Return Value

Returns a dynamic array containing unique values (or rows) from the input array. The result spills automatically into adjacent cells. The order of results matches the order of first occurrence in the source data.

## Examples

> [!f(x)] UNIQUE Examples

### Example 1: Basic Unique List from Single Column
```
=UNIQUE(A2:A100)
```
**Result:** Returns each distinct value from column A once, in order of first appearance

**Explanation:** The simplest UNIQUE pattern. If column A contains "Apple", "Banana", "Apple", "Cherry", "Banana", the result is "Apple", "Banana", "Cherry". Order matches first occurrence, not alphabetical.

---

### Example 2: Unique Values Sorted Alphabetically
```
=SORT(UNIQUE(B2:B500))
```
**Result:** Distinct values from column B, sorted A-Z

**Explanation:** UNIQUE alone preserves source order. Wrap in SORT for alphabetical ordering. This combo is perfect for generating sorted dropdown lists or clean reference data.

---

### Example 3: Unique Rows from Multiple Columns
```
=UNIQUE(A2:C100)
```
**Result:** Rows where the combination of columns A, B, and C is unique

**Explanation:** With multi-column input, UNIQUE compares entire rows. A row is duplicate only if ALL specified columns match another row exactly. Perfect for removing true record duplicates, not just single-column matches.

---

### Example 4: Count of Unique Values
```
=ROWS(UNIQUE(A2:A100))
```
**Result:** The number of distinct values in column A

**Explanation:** ROWS counts how many results UNIQUE returns. If you had 50 entries but only 12 unique values, this returns 12. Use COUNTA on the UNIQUE result for the same effect.

---

### Example 5: Unique Values with FILTER
```
=UNIQUE(FILTER(B2:B100, A2:A100="2024"))
```
**Result:** Distinct values from column B where column A equals "2024"

**Explanation:** First FILTER extracts rows matching the year, then UNIQUE deduplicates column B from those rows. Find unique products sold in 2024, unique customers in a specific region, etc.

---

### Example 6: Exactly Once Mode (Unmatched Items)
```
=UNIQUE(A2:A100, FALSE, TRUE)
```
**Result:** Values that appear exactly once—no duplicates (Excel only)

**Explanation:** The exactly_once parameter (TRUE) returns only items with a single occurrence. Use this to find orphan records, unmatched transactions, or items missing from a reconciliation.

---

### Example 7: Finding Unmatched Records Between Two Lists
```
=UNIQUE(VSTACK(List1, List2), , TRUE)
```
**Result:** Items appearing in one list but not both (Excel only)

**Explanation:** Stack both lists together, then find items appearing exactly once. These are the unmatched items—present in one list but missing from the other. Powerful for reconciliation.

---

### Example 8: Unique Combinations for Pivot-Style Summary
```
=UNIQUE(CHOOSECOLS(SalesData, 2, 3))
```
**Result:** Unique Region/Product combinations from the data

**Explanation:** Extract specific columns with CHOOSECOLS, then find unique combinations. This creates the row structure for a manual pivot table or summary without using actual pivot tables.

---

### Example 9: Dynamic Dropdown List Source
```
=SORT(UNIQUE(Products!B2:B1000))
```
**Result:** Sorted unique product list for Data Validation dropdown

**Explanation:** Create a named range pointing to this formula, then use it in Data Validation. The dropdown updates automatically as new products are added—no manual list maintenance.

---

### Example 10: Unique by Column (Horizontal Uniqueness)
```
=UNIQUE(A1:Z1, TRUE)
```
**Result:** Distinct values across the row (columns compared)

**Explanation:** The by_col parameter (TRUE) treats columns as the unit of comparison instead of rows. Useful for transposed data where records run horizontally. Most users never need this.

---

### Example 11: Unique with Multiple Columns and Sorting
```
=SORT(UNIQUE(A2:B100), 2, -1)
```
**Result:** Unique Name/Department pairs, sorted by Department descending

**Explanation:** Extract unique multi-column combinations, then sort by the second column descending. Chain functions for complex data processing in a single formula.

---

### Example 12: Counting Occurrences of Each Unique Value
```
=LET(
  unique_list, UNIQUE(A2:A100),
  HSTACK(unique_list, COUNTIF(A2:A100, unique_list))
)
```
**Result:** Two-column result: unique values and their occurrence counts

**Explanation:** LET names the UNIQUE result, then COUNTIF counts each unique value in the original data. HSTACK combines them side-by-side. This creates a frequency table dynamically.

---

### Example 13: Unique Non-Blank Values
```
=UNIQUE(FILTER(A2:A100, A2:A100<>""))
```
**Result:** Distinct values excluding blank cells

**Explanation:** UNIQUE includes blank as a "unique value" if blanks exist. FILTER first removes blanks, then UNIQUE deduplicates. Cleaner results for data with gaps.

---

### Example 14: First N Unique Values
```
=TAKE(UNIQUE(A2:A100), 5)
```
**Result:** First 5 unique values (in order of first occurrence)

**Explanation:** TAKE limits the UNIQUE result to the first 5 values. Useful for "Top 5 categories" type displays where you want the most common or first-seen items only.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#SPILL!` (Excel) | Spill range is blocked by data or merged cells | Clear cells below/right of formula. Unmerge any merged cells in the spill range. |
| `#REF!` | Spill range extends beyond worksheet boundaries | Move the formula or reduce source data size. |
| `#NAME?` | Function not available in your Excel version | UNIQUE requires Excel 365, Excel 2021, or Google Sheets. Not available in Excel 2019 or earlier. |
| `Blanks in results` | Source data contains empty cells | Use FILTER to remove blanks first: `=UNIQUE(FILTER(range, range<>""))` |
| `Too many results` | Multi-column UNIQUE on wrong columns | Check that you're including only the columns that define uniqueness, not extra columns that vary per row. |
| `exactly_once not working` | Parameter not supported in Google Sheets | In Sheets, use FILTER with COUNTIF to find values appearing exactly once. |
| `Case duplicates` | "ABC" and "abc" treated as different | UNIQUE is case-insensitive in both platforms, but data may have mixed case that looks duplicated. |

## Use Cases

### [[Dynamic Category Lists for Dropdowns]]

**Scenario:** A data entry form needs dropdown lists for Product Category, Region, and Status that automatically update as new values are added to the source data.

**Implementation:**
```
Category: =SORT(UNIQUE(Products!C2:C1000))
Region: =SORT(UNIQUE(Customers!D2:D5000))
Status: =SORT(UNIQUE(Orders!F2:F10000))
```

**Business Application:** Eliminates manual dropdown maintenance. When someone adds a new category to the products table, it automatically appears in the dropdown. No IT tickets, no forgotten updates, no "value not in list" complaints.

**Technical Details:** Create a named range pointing to each UNIQUE formula (e.g., `CategoryList`), then reference that name in Data Validation. The named range's size adjusts automatically as the UNIQUE result grows or shrinks.

---

### [[Customer Reconciliation and Matching]]

**Scenario:** Finance needs to reconcile customer lists from two systems—CRM and Billing—to find customers that exist in only one system.

**Implementation:**
```
=UNIQUE(VSTACK(CRM!A2:A500, Billing!A2:A500), , TRUE)
```

**Business Application:** Identifies data quality issues: customers in CRM but not Billing (maybe not being billed), or in Billing but not CRM (maybe churned but not recorded). Essential for accurate revenue reporting and customer counts.

**Technical Details:** VSTACK combines both lists vertically. The exactly_once parameter (TRUE) returns only customers appearing in exactly one list—the mismatches. For customers in both lists, they'd appear twice in the combined list and be excluded by exactly_once.

---

### [[Survey Response Analysis]]

**Scenario:** Analyze open-ended survey responses to identify unique themes mentioned by respondents, along with how often each theme appears.

**Implementation:**
```
=LET(
  themes, UNIQUE(FILTER(Responses!D2:D1000, Responses!D2:D1000<>"")),
  counts, COUNTIF(Responses!D2:D1000, themes),
  SORT(HSTACK(themes, counts), 2, -1)
)
```

**Business Application:** Quickly see what topics respondents mention most frequently. Instead of reading through hundreds of responses, get a ranked list of themes. Helps prioritize follow-up analysis.

**Technical Details:** FILTER removes blank responses, UNIQUE gets distinct themes, COUNTIF tallies each theme. LET organizes the logic, HSTACK combines theme and count columns, and SORT ranks by count descending.

---

### [[Inventory SKU Validation]]

**Scenario:** Warehouse needs to verify that all SKUs in receiving logs exist in the master product database, flagging any unknown SKUs for investigation.

**Implementation:**
```
=LET(
  received_skus, UNIQUE(Receiving!B2:B500),
  known_skus, Products!A2:A1000,
  FILTER(received_skus, ISNA(MATCH(received_skus, known_skus, 0)))
)
```

**Business Application:** Catches data entry errors (typos in SKUs), unauthorized products, or master data gaps before they cause inventory discrepancies. Run this daily as part of receiving verification.

**Technical Details:** UNIQUE gets distinct received SKUs, MATCH checks each against the master list (returning #N/A for misses), ISNA identifies the non-matches, and FILTER extracts only the unknown SKUs. These need investigation.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 365 (subscription), Excel 2021 (perpetual), Excel for web
- **exactly_once parameter:** Available and fully functional
- **Spill behavior:** Results spill automatically; #SPILL! error if blocked
- **Case sensitivity:** Case-insensitive ("ABC" = "abc" for uniqueness)
- **Performance:** Optimized for large datasets

### Google Sheets
- **Availability:** All versions (UNIQUE available since early Google Sheets)
- **exactly_once parameter:** NOT available; use workarounds with COUNTIF and FILTER
- **Spill behavior:** Results expand automatically
- **Case sensitivity:** Case-insensitive (same as Excel)
- **Performance:** Good for typical datasets

### Key Difference Alert
The biggest functional difference is the exactly_once parameter. In Excel, `=UNIQUE(data, , TRUE)` easily finds unmatched items. In Google Sheets, you need a workaround:
```
=FILTER(UNIQUE(data), COUNTIF(data, UNIQUE(data))=1)
```
This achieves the same result but is more complex. If cross-platform compatibility is important, avoid exactly_once and use the FILTER/COUNTIF pattern.

## Tips and Best Practices

1. **Combine UNIQUE with SORT for usable lists:** Raw UNIQUE output follows source order, which is often not useful. `=SORT(UNIQUE(...))` gives alphabetized results suitable for dropdowns and reference.

2. **Filter blanks before UNIQUE:** `=UNIQUE(FILTER(range, range<>""))` prevents blank cells from appearing as a "unique value" in your results. Essential for clean output.

3. **Use multi-column UNIQUE for record-level deduplication:** When "duplicate" means matching on multiple fields, include all those columns: `=UNIQUE(A2:D100)` compares entire rows, not just one column.

4. **ROWS(UNIQUE(...)) counts distinct values:** Need to know how many unique items exist? Wrap UNIQUE in ROWS. This is more efficient than SUMPRODUCT/COUNTIF tricks.

5. **Create named ranges from UNIQUE results:** Name your UNIQUE formula result (like `ProductList`), then reference it in Data Validation, charts, or other formulas. One formula maintains the list for many uses.

6. **For exactly_once in Sheets, use FILTER+COUNTIF:** `=FILTER(UNIQUE(range), COUNTIF(range, UNIQUE(range))=1)` replicates Excel's exactly_once parameter for cross-platform work.

7. **Watch spill range conflicts:** UNIQUE results grow as source data diversity increases. Leave plenty of room below the formula to avoid #SPILL! errors when new unique values appear.

8. **Combine with LET for frequency tables:** `=LET(u, UNIQUE(range), HSTACK(u, COUNTIF(range, u)))` creates a value-count table dynamically—no pivot table needed.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[Remove Duplicates]] | Excel feature that deletes duplicate rows in place | When you want to permanently clean source data (not formula-based) |
| [[DISTINCT]] | SQL-like distinct (some platforms) | If using database connections or Power Query |
| [[COUNTIF/COUNTIFS]] | Count occurrences of values | When you need to count duplicates rather than remove them |
| [[Advanced Filter]] | Copy unique records to another location | Legacy Excel approach; UNIQUE is more flexible |

### Commonly Used Together

**[[SORT]]** - Alphabetize unique results

*Combined with UNIQUE for sorted distinct lists:*
```
=SORT(UNIQUE(A2:A100))
```
UNIQUE extracts, SORT orders. Standard pattern for generating dropdown source lists.

---

**[[FILTER]]** - Remove blanks or filter before deduplicating

*Combined with UNIQUE for clean results:*
```
=UNIQUE(FILTER(A2:A100, A2:A100<>""))
```
Filter out blanks first, then get unique values from the non-blank data.

---

**[[COUNTIF]]** - Count occurrences of each unique value

*Combined with UNIQUE for frequency analysis:*
```
=HSTACK(UNIQUE(A2:A100), COUNTIF(A2:A100, UNIQUE(A2:A100)))
```
Create a frequency table showing each unique value and its count.

---

**[[VSTACK]]** / **[[HSTACK]]** - Combine data before finding unique values

*Combined with UNIQUE for cross-list analysis:*
```
=UNIQUE(VSTACK(List1, List2))
```
Stack multiple lists together, then find distinct values across all of them.

---

**[[ROWS]]** - Count unique values

*Combined with UNIQUE for distinct count:*
```
=ROWS(UNIQUE(A2:A100))
```
Returns how many distinct values exist—equivalent to COUNT(DISTINCT) in SQL.

---

**[[LET]]** - Name UNIQUE results for reuse in formula

*Combined with UNIQUE for complex calculations:*
```
=LET(uniq, UNIQUE(A2:A100), HSTACK(uniq, COUNTIF(A2:A100, uniq)))
```
LET prevents recalculating UNIQUE multiple times in the same formula.

## Official Documentation

- **Microsoft Excel:** [UNIQUE function](https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e)
- **Google Sheets:** [UNIQUE function](https://support.google.com/docs/answer/3093198)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Google Sheets | 2006 (original) | Available since early Google Sheets; no exactly_once parameter |
| Excel 365 | 2018 (Insider), 2019 (general) | Part of dynamic array rollout; includes exactly_once |
| Excel 2021 | 2021 | First perpetual license version with UNIQUE |
| Excel for web | 2019 | Full support including exactly_once |
| Excel 2019 and earlier | Not available | Use Remove Duplicates feature or helper column with COUNTIF |

---

*Last updated: 2026-01-10*
