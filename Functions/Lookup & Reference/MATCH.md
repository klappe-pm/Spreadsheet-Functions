---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics:
- position-lookup
- array-search
- index-match
- approximate-match
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Position Lookup
- Value Position
- Array Position
- Find Position
tags:
- lookup
- reference
- position
- search
- index-match
---

# MATCH

## Description

**MATCH** searches for a specified value in a range and returns the relative position of that value within the range. It answers the question "where is this value?"—not what the value is, but which row or column number it occupies. If you're looking for "Apple" in a list of fruits and it's the 5th item, MATCH returns 5. This seemingly simple capability becomes extraordinarily powerful when combined with other functions, particularly INDEX, to create flexible lookup systems that surpass VLOOKUP in virtually every dimension.

The function offers three distinct **match types** that dramatically change its behavior. Match type 0 performs an exact match—the value must exist precisely in the range, or you get #N/A. Match type 1 (the default, surprisingly) finds the largest value that is less than or equal to your lookup value, perfect for tax brackets, pricing tiers, and grading scales. Match type -1 does the opposite, finding the smallest value greater than or equal to your lookup value. Most users need exact match (0) most of the time, so **always explicitly specify 0** to avoid the approximate-match trap that catches countless beginners.

**MATCH is half of the legendary INDEX+MATCH combination** that professional spreadsheet users have relied on for decades as their primary lookup tool. While VLOOKUP directly returns a value, MATCH only returns a position—which might seem less useful at first glance. But this separation of concerns is precisely what makes INDEX+MATCH so powerful. MATCH finds where the data lives; INDEX retrieves what you want from any column. This two-step approach allows you to look in any direction (VLOOKUP can only look right), use any column as your lookup column, and create formulas that don't break when columns are inserted or reordered.

**Platform behavior:** MATCH works identically in Excel and Google Sheets for most use cases. Both platforms support the three match types, wildcard characters (* and ?) in exact match mode, and case-insensitive searching. The main consideration is that approximate matching (match_type 1 or -1) requires your data to be sorted in the correct order—ascending for type 1, descending for type -1. Neither platform will warn you if your data isn't sorted; you'll simply get wrong results. Excel 365 and 2019+ introduced XMATCH as a modern replacement with additional features like search modes and binary search, but MATCH remains essential for compatibility and for use in Google Sheets where XMATCH doesn't exist.

## Syntax

> [!f(x)] MATCH Syntax
>
> ```
> =MATCH(lookup_value, lookup_array, [match_type])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `lookup_value` | Yes | The value you want to find in lookup_array. Can be a number, text, logical value, cell reference, or formula result. For exact matching with text, wildcards (* and ?) are supported. |
| `lookup_array` | Yes | A single row or column of cells to search. Must be a one-dimensional range (e.g., A1:A100 or A1:Z1), not a two-dimensional table. The position returned is relative to this range. |
| `match_type` | No | Specifies how to match: **1** (default) = largest value <= lookup_value (data must be ascending); **0** = exact match; **-1** = smallest value >= lookup_value (data must be descending). |

### Match Type Details

| Match Type | Description | Data Requirement | Use Case |
|------------|-------------|------------------|----------|
| **1** (or omitted) | Finds largest value <= lookup_value | Data MUST be sorted ascending | Tax brackets, price tiers, grade scales |
| **0** | Finds exact match only | No sorting required | Looking up IDs, codes, names—most common |
| **-1** | Finds smallest value >= lookup_value | Data MUST be sorted descending | Reverse tier lookups (rare) |

### Return Value

Returns the relative position (as an integer starting from 1) of the matched value within lookup_array. The first item is position 1, second is position 2, etc. Returns #N/A if no match is found (exact match mode) or if lookup_value is out of range (approximate match modes).

## Examples

> [!f(x)] MATCH Examples

### Example 1: Basic Exact Match
```
=MATCH("Apple", A2:A10, 0)
```
**Result:** Returns the position of "Apple" in the range A2:A10 (e.g., 3 if Apple is in A4)

**Explanation:** The most common use of MATCH—finding exactly where a value is located. The 0 specifies exact match, meaning "Apple" must appear exactly (though case-insensitively—"apple" and "APPLE" also match). If Apple is the 3rd item in the range A2:A10 (cell A4), MATCH returns 3.

---

### Example 2: Exact Match with Cell Reference
```
=MATCH(B2, A:A, 0)
```
**Result:** Returns the row number where B2's value appears in column A

**Explanation:** Instead of hardcoding "Apple", we reference cell B2. This pattern is essential for copying formulas down—each row looks up its own value. Using the entire column (A:A) as lookup_array means you don't need to know where the data ends.

---

### Example 3: Approximate Match for Tax Brackets (Less Than or Equal)
```
=MATCH(75000, A2:A7, 1)
```
Where A2:A7 contains sorted tax thresholds: 0, 10000, 40000, 85000, 165000, 215000

**Result:** Returns 3 (the position of 40000, which is the largest value <= 75000)

**Explanation:** Match type 1 finds the largest value that doesn't exceed your lookup value. An income of $75,000 exceeds $40,000 but not $85,000, so it falls into the $40,000 bracket (position 3). CRITICAL: The data MUST be sorted in ascending order for this to work correctly.

---

### Example 4: Approximate Match for Grading Scale
```
=MATCH(87, ScoreThresholds, 1)
```
Where ScoreThresholds is: 0, 60, 70, 80, 90 (named range)

**Result:** Returns 4 (the position of 80, since 87 >= 80 but < 90)

**Explanation:** A score of 87 matches the 80 threshold (position 4). Combined with INDEX pointing to a grades column (F, D, C, B, A), you can convert scores to letter grades without nested IFs: `=INDEX(GradeLetters, MATCH(B2, ScoreThresholds, 1))`.

---

### Example 5: Finding Position of Maximum Value
```
=MATCH(MAX(B2:B100), B2:B100, 0)
```
**Result:** Returns the position of the highest value in B2:B100

**Explanation:** MAX finds the largest value in the range. MATCH then finds its position. This is how you answer "which row has the highest sales?" When combined with INDEX, you can return the corresponding product name, date, or any other related data.

---

### Example 6: Finding Position of Minimum Value
```
=MATCH(MIN(C:C), C:C, 0)
```
**Result:** Returns the position of the lowest value in column C

**Explanation:** Same pattern as above but using MIN. Combined with INDEX: `=INDEX(A:A, MATCH(MIN(C:C), C:C, 0))` returns the value from column A corresponding to the minimum in column C.

---

### Example 7: Using MATCH with INDEX for Left Lookup
```
=INDEX(A2:A100, MATCH("ProductCode123", C2:C100, 0))
```
**Result:** Returns the value from column A where "ProductCode123" appears in column C

**Explanation:** This is the "reverse lookup" that VLOOKUP cannot do. MATCH finds the position in column C (the lookup column), and INDEX uses that position to return the value from column A (which is to the LEFT). The lookup column and return column can be anywhere—they don't even need to be adjacent.

---

### Example 8: Two-Way Lookup with Two MATCH Functions
```
=INDEX(B2:F10, MATCH("East", A2:A10, 0), MATCH("Q3", B1:F1, 0))
```
**Result:** Returns the value at the intersection of "East" row and "Q3" column

**Explanation:** When your data is a matrix with headers on both rows and columns, use two MATCH functions. The first finds the row position in the row headers (column A). The second finds the column position in the column headers (row 1). INDEX uses both positions to pinpoint the exact cell.

---

### Example 9: Wildcard Matching with Asterisk
```
=MATCH("John*", A2:A100, 0)
```
**Result:** Returns the position of the first value starting with "John"

**Explanation:** In exact match mode (0), wildcards are supported. The asterisk (*) matches any sequence of characters. This finds "John", "John Smith", "Johnson", etc.—whichever appears first. Use ? for single-character wildcards.

---

### Example 10: Wildcard Matching with Question Mark
```
=MATCH("A?C", A2:A50, 0)
```
**Result:** Returns the position of any three-letter value matching A_C pattern

**Explanation:** The question mark matches exactly one character. This finds "ABC", "ADC", "A1C", etc., but not "ABBC" or "AC". Useful for matching part numbers or codes with fixed patterns.

---

### Example 11: Finding Column Position in Headers
```
=MATCH("Revenue", 1:1, 0)
```
**Result:** Returns the column number where "Revenue" appears in row 1

**Explanation:** MATCH works horizontally too. When lookup_array is a row (like 1:1), MATCH returns the column position. This is commonly used with VLOOKUP or INDEX to dynamically determine which column to retrieve based on a header name.

---

### Example 12: Handling Missing Values with IFERROR
```
=IFERROR(MATCH(B2, A:A, 0), 0)
```
**Result:** Returns position if found, 0 if not found

**Explanation:** When MATCH can't find a value (exact match mode), it returns #N/A. Wrapping in IFERROR provides a fallback. Common fallbacks: 0 (for calculations), "" (for display), or "Not Found" (for clarity).

---

### Example 13: Multiple Criteria Matching (Array Formula)
```
=MATCH(1, (A2:A100="East")*(B2:B100="Q3"), 0)
```
**Result:** Returns the position where column A is "East" AND column B is "Q3"

**Explanation:** This array formula multiplies two Boolean arrays. Where both conditions are TRUE (1*1=1), the result is 1; otherwise 0. MATCH finds the first 1. In older Excel, requires Ctrl+Shift+Enter; Excel 365 and Sheets handle it automatically.

---

### Example 14: Finding the Last Occurrence (Array Formula)
```
=MATCH(2, 1/(A:A="Target"))
```
**Result:** Returns the position of the LAST occurrence of "Target"

**Explanation:** This clever formula divides 1 by a Boolean array. Where "Target" exists, you get 1/1=1; elsewhere, 1/0=#DIV/0. MATCH with no match_type (defaulting to 1, approximate) finds the last valid number. Note: this is an advanced technique with performance implications.

---

### Example 15: Checking If Value Exists (Boolean Result)
```
=NOT(ISNA(MATCH(B2, A:A, 0)))
```
**Result:** Returns TRUE if B2 exists in column A, FALSE if not

**Explanation:** Sometimes you just need to know if a value exists, not where it is. MATCH returns #N/A if not found; ISNA detects this; NOT flips the logic. TRUE means "value exists." Alternative: `=ISNUMBER(MATCH(...))` works similarly.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | Value not found in lookup_array (exact match mode) | Check spelling, data types (text vs. number), leading/trailing spaces. Use TRIM on both lookup_value and lookup_array if needed. |
| `#N/A` | lookup_value is smaller than smallest value (match_type 1) | With approximate match ascending, the lookup value must be >= the smallest value in the range. |
| `#N/A` | lookup_value is larger than largest value (match_type -1) | With approximate match descending, the lookup value must be <= the largest value in the range. |
| `#VALUE!` | lookup_array is not a single row or column | MATCH requires a one-dimensional range. A2:D10 won't work; use A2:A10 or A2:D2. |
| `Wrong result` | Data not sorted correctly for approximate match | Match type 1 requires ascending sort; match type -1 requires descending. If data isn't sorted, use exact match (0) instead. |
| `Wrong result` | Omitted match_type defaulting to 1 (approximate) | Always explicitly specify 0 for exact matches. The default of 1 catches many users off guard. |
| `Wrong result` | Case sensitivity confusion | MATCH is case-insensitive: "ABC" matches "abc". For case-sensitive matching, use MATCH with EXACT in an array formula. |
| `Finding wrong duplicate` | Multiple values exist, wrong one matched | MATCH always returns the FIRST match. For last match or Nth match, use array formulas with MAX or SMALL. |

## Use Cases

### [[Dynamic Column Selection in Reports]]

**Scenario:** A financial analyst creates reports where users select which metric to display (Revenue, Expenses, Profit, etc.) from a dropdown. The selected column needs to be dynamically extracted from a large data table without hardcoding column positions.

**Implementation:**
```
Metric Selector Dropdown (Cell G1): "Revenue" (data validation list from header row)

Data Table: A1:F100 with headers in row 1 (Region, Month, Revenue, Expenses, Profit, Margin)

Column Position: =MATCH($G$1, $A$1:$F$1, 0)
Result: 3 (if "Revenue" is selected, since it's the 3rd column)

Dynamic Data Extraction: =INDEX($A$2:$F$100, ROW()-1, MATCH($G$1, $A$1:$F$1, 0))
```

**Business Application:** This pattern enables self-service reporting where end users can explore different metrics without requiring the analyst to create separate reports for each metric. Finance teams use this for budget vs. actual analysis, sales teams for territory performance, and operations for KPI dashboards. The single MATCH function powers the entire column selection logic.

**Technical Details:** The MATCH finds which column contains the selected header. Store this in a helper cell if multiple formulas need it. The INDEX formula uses this position to extract the entire column of data. For charts, you can reference this dynamic column to create visualizations that update based on user selection. Consider naming the MATCH result ("SelectedColumn") for clearer formulas.

---

### [[Tiered Pricing and Commission Calculation]]

**Scenario:** A sales compensation system needs to determine commission rates based on sales volume tiers. Sales amounts don't match tier thresholds exactly—you need to find which tier applies. The same pattern applies to shipping cost calculators, volume discounts, and tax brackets.

**Implementation:**
```
Commission Tier Table (CommissionTiers sheet):
   A2:A6 (Thresholds): 0, 10000, 25000, 50000, 100000
   B2:B6 (Rates): 5%, 7%, 10%, 12%, 15%

Salesperson Sales (Cell C2 on main sheet): 67500

Tier Position: =MATCH(C2, CommissionTiers!$A$2:$A$6, 1)
Result: 4 (67500 falls in the 50000-99999 tier)

Commission Rate: =INDEX(CommissionTiers!$B$2:$B$6, MATCH(C2, CommissionTiers!$A$2:$A$6, 1))
Result: 12%

Commission Amount: =C2 * INDEX(CommissionTiers!$B$2:$B$6, MATCH(C2, CommissionTiers!$A$2:$A$6, 1))
Result: 8100
```

**Business Application:** Tiered structures are everywhere in business: tax brackets, volume discounts, shipping rates, employee bonus scales, usage-based pricing. Without MATCH's approximate matching capability, you'd need complex nested IF statements. With match_type 1, you simply list your thresholds in ascending order and MATCH finds the appropriate tier instantly.

**Technical Details:** CRITICAL: The threshold column MUST be sorted in ascending order for match_type 1 to work correctly. The formula finds the largest threshold that doesn't exceed the sales amount. For the inverse (smallest threshold greater than or equal), use match_type -1 with data sorted descending. Consider adding an upper limit check: `=IF(C2>MAX(Thresholds), "Exceeds Scale", INDEX(Rates, MATCH(C2, Thresholds, 1)))`.

---

### [[Multi-Criteria Lookup for Inventory Management]]

**Scenario:** An inventory system needs to find stock levels for a specific product at a specific warehouse. The data table has multiple rows per product (one for each warehouse), so a simple single-column lookup won't work. The system needs to match on both product code AND warehouse location.

**Implementation:**
```
Inventory Data (A2:E1000):
   A = Product Code, B = Warehouse, C = Stock Level, D = Reorder Point, E = Supplier

Lookup Parameters:
   Product Code (G2): "SKU-1234"
   Warehouse (G3): "Chicago"

Combined Lookup Key: =G2&"|"&G3
Result: "SKU-1234|Chicago"

Position in Data: =MATCH(G2&"|"&G3, A2:A1000&"|"&B2:B1000, 0)
Result: 47 (the row within the range where both criteria match)

Stock Level: =INDEX(C2:C1000, MATCH($G$2&"|"&$G$3, $A$2:$A$1000&"|"&$B$2:$B$1000, 0))
Result: 156 units

Alternative (Array Multiplication Method):
=INDEX(C2:C1000, MATCH(1, (A2:A1000=G2)*(B2:B1000=G3), 0))
```

**Business Application:** Real-world data often requires matching on multiple fields: product + location, employee + date, customer + product, region + quarter. The concatenation approach combines fields into a unique key. The array multiplication approach directly evaluates multiple conditions. Both are essential for inventory systems, HR records, sales tracking, and any database-style lookups.

**Technical Details:** The concatenation method (`A&"|"&B`) creates unique composite keys—use a delimiter (like "|") that won't appear in your data. The array multiplication method (`(A=x)*(B=y)`) multiplies Boolean arrays; only rows where both are TRUE yield 1. In older Excel, these are array formulas (Ctrl+Shift+Enter). Performance consideration: for very large datasets, consider adding a helper column with the concatenated key to avoid repeated calculation.

---

### [[Data Validation and Duplicate Detection]]

**Scenario:** A data entry form needs to check whether a new record already exists in the database before allowing it to be added. The system should display a warning if the ID or code is already in use, and highlight duplicate entries in existing data.

**Implementation:**
```
Existing Database IDs (Column A): A2:A5000 contains all current IDs
New Entry ID (Cell E2): User enters new ID to add

Validation Check:
=IF(ISNUMBER(MATCH(E2, A2:A5000, 0)), "ERROR: ID Already Exists", "OK to Add")

Conditional Formatting Rule for Duplicate Highlighting:
Formula: =COUNTIF($A$2:$A$5000, A2) > 1
(Applied to A2:A5000 to highlight any cell that has a duplicate)

Finding Duplicate Positions:
=IF(MATCH(A2, $A$2:$A$5000, 0) <> ROW()-1, "DUPLICATE of row "&MATCH(A2, $A$2:$A$5000, 0)+1, "")
(Shows "DUPLICATE of row X" if this isn't the first occurrence)
```

**Business Application:** Data quality is critical for any database. Preventing duplicates at entry time is far more efficient than cleaning them later. This pattern applies to customer IDs, product codes, invoice numbers, employee IDs, and any field that should be unique. The instant feedback helps users correct errors immediately.

**Technical Details:** ISNUMBER(MATCH(...)) is a common idiom for "does this exist?" because MATCH returns a number if found, #N/A if not. For duplicate detection within existing data, comparing `MATCH(value, range, 0)` to the current row position reveals whether this is the first occurrence or a duplicate. COUNTIF > 1 is simpler for highlighting but doesn't tell you which row is the original.

## Platform Differences

### Microsoft Excel

- **Availability:** All versions from Excel 97 onward
- **Case sensitivity:** Always case-insensitive (abc = ABC = AbC)
- **Wildcards:** Supported in exact match mode (match_type 0): * for any characters, ? for single character
- **Array formulas:** Older versions require Ctrl+Shift+Enter for array MATCH formulas; Excel 365 handles automatically
- **XMATCH alternative:** Excel 2019/365 includes XMATCH with additional features: search modes (first/last), binary search, and if-not-found parameter
- **Performance:** Binary search (match_type 1 or -1 on sorted data) is faster than exact match on large datasets

### Google Sheets

- **Availability:** All versions from Sheets' inception
- **Case sensitivity:** Always case-insensitive (matches Excel)
- **Wildcards:** Supported in exact match mode (matches Excel)
- **Array formulas:** Handles arrays natively without special entry; may need ARRAYFORMULA wrapper for spilling results
- **No XMATCH:** XMATCH is not available in Google Sheets; MATCH remains the only option
- **Performance:** Efficient with full-column references (A:A); scales well with large datasets

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| XMATCH alternative | Available (2019/365) | Not available |
| Array entry method | Ctrl+Shift+Enter (legacy) / Auto (365) | Auto |
| Full-column performance | Can slow in very large workbooks | Generally efficient |
| Wildcard support | Yes (match_type 0) | Yes (match_type 0) |
| Case-sensitive matching | Requires EXACT in array formula | Requires EXACT in array formula |

### Behavioral Consistency

Both platforms are identical in:
- Match type behavior (0, 1, -1)
- Return values (1-based position)
- Error conditions (#N/A for not found)
- Sorting requirements for approximate match
- Wildcard characters (* and ?)

## Tips and Best Practices

1. **Always specify match_type explicitly:** The default of 1 (approximate match) surprises most users who expect exact matching. Make `=MATCH(..., 0)` your standard pattern. Only use 1 or -1 when you specifically need tiered/threshold matching.

2. **Remember that MATCH returns position, not value:** MATCH tells you WHERE something is, not WHAT it is. Combine with INDEX to retrieve actual values: `=INDEX(ReturnColumn, MATCH(LookupValue, LookupColumn, 0))`.

3. **Pair MATCH with INDEX for flexible lookups:** INDEX+MATCH can look in any direction (including left), doesn't break when columns are inserted, and handles complex multi-criteria scenarios. It's more versatile than VLOOKUP in virtually every way.

4. **Store MATCH results when used multiple times:** If you're looking up the same value to retrieve multiple columns, calculate MATCH once in a helper cell: `Helper: =MATCH(A2, LookupColumn, 0)`, then `=INDEX(Column1, Helper)`, `=INDEX(Column2, Helper)`, etc. This improves performance and maintainability.

5. **Use wildcards for partial matching:** In exact match mode, * matches any sequence and ? matches single characters. `=MATCH("*smith*", Names, 0)` finds any name containing "smith". Escape literal asterisks with ~.

6. **For sorted data, approximate match is faster:** Match_type 1 or -1 uses binary search (O(log n)) while exact match uses linear search (O(n)). For very large datasets that are already sorted, approximate matching can be significantly faster.

7. **Handle #N/A errors gracefully:** Wrap MATCH in IFERROR for production formulas: `=IFERROR(MATCH(...), DefaultValue)`. Choose appropriate defaults: 0 for calculations, "" for display, or specific error messages for debugging.

8. **Watch for data type mismatches:** "123" (text) will not match 123 (number). If lookups fail unexpectedly, check whether both the lookup value and the lookup array contain the same data type. Use VALUE() or TEXT() to convert if needed.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[XMATCH]] | Modern MATCH with more features | Excel 365/2019 only. Offers search modes (first/last/binary), if-not-found parameter, and cleaner syntax. Use when available. |
| [[SEARCH]] | Find text position within a string | When you need to find where one text string appears WITHIN another (e.g., "cat" in "category"). MATCH finds array positions, SEARCH finds string positions. |
| [[FIND]] | Case-sensitive text position in string | Like SEARCH but case-sensitive. For in-string searching, not array position finding. |
| [[LOOKUP]] | Legacy lookup function | Rarely needed. LOOKUP is an older function with quirky behavior. Use MATCH for position finding, INDEX+MATCH or VLOOKUP for value retrieval. |

### Commonly Used Together

**[[INDEX]]** - Return value from a position

*The classic INDEX+MATCH combination for flexible lookups:*
```
=INDEX(C2:C100, MATCH(A2, B2:B100, 0))
```
MATCH finds the row position; INDEX returns the value from that position. This is the most important function pairing in spreadsheet work—more flexible than VLOOKUP and the foundation of professional lookup formulas.

---

**[[MAX]]/[[MIN]]** - Find extreme values

*Combined with MATCH to locate the position of maximum/minimum:*
```
=MATCH(MAX(B:B), B:B, 0)
```
MAX finds the largest value, MATCH finds where it is. Add INDEX to return related data: `=INDEX(A:A, MATCH(MAX(B:B), B:B, 0))` returns the name/ID associated with the highest value.

---

**[[VLOOKUP]]** - Traditional vertical lookup

*MATCH provides dynamic column selection for VLOOKUP:*
```
=VLOOKUP(A2, Table, MATCH("Revenue", Headers, 0), FALSE)
```
Instead of hardcoding column numbers in VLOOKUP, use MATCH to find which column contains the desired header. This makes VLOOKUP formulas resilient to column insertions.

---

**[[COUNTIF]]** - Count matching cells

*MATCH finds position; COUNTIF counts occurrences:*
```
=IF(COUNTIF(A:A, B2) > 0, "Exists", "Not Found")
```
For simple existence checks, COUNTIF > 0 is an alternative to ISNUMBER(MATCH(...)). COUNTIF is simpler but doesn't tell you WHERE the value is.

---

**[[IFERROR]]** - Handle lookup failures

*Wrap MATCH for graceful error handling:*
```
=IFERROR(INDEX(B:B, MATCH(A2, C:C, 0)), "Not Found")
```
When MATCH returns #N/A, IFERROR catches it and provides a fallback value instead of displaying an error.

---

**[[EXACT]]** - Case-sensitive comparison

*Combined with MATCH for case-sensitive lookups:*
```
=MATCH(TRUE, EXACT(A2:A100, "ABC"), 0)
```
EXACT compares case-sensitively, creating an array of TRUE/FALSE. MATCH finds the first TRUE. This array formula enables case-sensitive lookups that MATCH alone cannot do.

---

**[[SMALL]]/[[LARGE]]** - Nth smallest/largest

*Combined with MATCH for Nth occurrence:*
```
=MATCH(SMALL(IF(A:A="X", B:B), 2), B:B, 0)
```
Find the position of the 2nd smallest value in B where A equals "X". Complex but powerful for ranking and Nth-value problems.

---

**[[ROW]]/[[COLUMN]]** - Current position

*Used with MATCH for self-referential formulas:*
```
=IF(MATCH(A2, $A$2:$A$100, 0) = ROW()-1, "First", "Duplicate")
```
Compares MATCH result to current row position to detect if this is the first occurrence or a duplicate.

## Official Documentation

- **Microsoft Excel:** [MATCH function](https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a)
- **Google Sheets:** [MATCH function](https://support.google.com/docs/answer/3093378)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with all three match types |
| Excel 2007 | Enhanced | Improved performance and larger range support |
| Excel 2010 | Enhanced | Better array handling |
| Excel 2019/365 | XMATCH introduced | Modern alternative with search modes and if-not-found parameter |
| Google Sheets | Original launch (2006) | Full compatibility with Excel's MATCH function |
| Google Sheets | 2018+ | Improved array handling and performance |

---

*Last updated: 2026-01-10*
