---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics:
- conditional-counting
- criteria-matching
- wildcard-patterns
- data-filtering
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Count If
- Conditional Count
- Count With Criteria
- Count Matching
tags:
- statistical
- counting
- conditional
- criteria
- wildcards
- pattern-matching
---

# COUNTIF

## Description

**COUNTIF** counts the number of cells in a range that meet a specified criterion. It is the conditional counting workhorse of spreadsheets, answering questions like: "How many orders are from California?" "How many scores are above 90?" "How many entries contain the word 'urgent'?" COUNTIF bridges the gap between simple counting (COUNT/COUNTA) and full database queries, providing powerful filtering without complex formulas.

The function accepts a single criterion that can include comparison operators (>, <, >=, <=, <>), exact matches, and wildcard characters (* and ?). This flexibility makes COUNTIF suitable for everything from simple category counts to pattern matching in text data. The criterion is always specified as a string, even for numeric comparisons - you write `">100"` not `>100`.

**Wildcard power:** COUNTIF supports two wildcards: `*` (asterisk) matches any sequence of characters, and `?` (question mark) matches exactly one character. To count cells starting with "A", use `"A*"`. To count 5-digit codes starting with "1", use `"1????"`. To find a literal asterisk or question mark, escape it with a tilde: `"~*"` matches an actual asterisk. Wildcards only work with text criteria, not numeric comparisons.

**Platform behavior:** Excel and Google Sheets implement COUNTIF identically for standard use cases. Both support the same comparison operators and wildcards. The primary consideration is case sensitivity in text matching: both platforms treat text comparisons as case-insensitive ("APPLE" matches "apple"). For case-sensitive counting, you need to use SUMPRODUCT with EXACT.

## Syntax

> [!f(x)] COUNTIF Syntax
>
> ```
> =COUNTIF(range, criteria)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `range` | Yes | The range of cells to evaluate against the criteria. Must be a contiguous range reference. |
| `criteria` | Yes | The condition that determines which cells to count. Can be a number, text, expression, cell reference, or wildcard pattern. Comparison operators must be enclosed in quotes with the value. |

### Return Value

Returns an integer representing the count of cells that meet the specified criterion. Returns 0 if no cells match. Never returns an error for valid range and criteria combinations.

## Examples

> [!f(x)] COUNTIF Examples

### Example 1: Exact Text Match
```
=COUNTIF(A1:A10, "Apple")
```
Where A1:A10 contains various fruit names

**Result:** Count of cells containing exactly "Apple"

**Explanation:** Counts cells that match "Apple" exactly (case-insensitive). "apple", "APPLE", and "Apple" all match. "Apples" or "Green Apple" do NOT match - only exact matches count.

---

### Example 2: Numeric Comparison - Greater Than
```
=COUNTIF(B1:B100, ">50")
```
**Result:** Count of cells with values greater than 50

**Explanation:** The comparison operator and value are combined in quotes. Counts all numeric values exceeding 50. Note: ">50" is text, but COUNTIF interprets it as a numeric comparison.

---

### Example 3: Numeric Comparison - Less Than or Equal
```
=COUNTIF(C1:C100, "<=100")
```
**Result:** Count of cells with values 100 or less

**Explanation:** Combines <= operator with the value. Counts cells where the numeric value is 100 or below.

---

### Example 4: Not Equal To
```
=COUNTIF(A1:A50, "<>Pending")
```
**Result:** Count of cells NOT containing "Pending"

**Explanation:** The <> operator means "not equal to." Counts all cells except those containing exactly "Pending". Empty cells are also counted as not equal to "Pending".

---

### Example 5: Cell Reference as Criteria
```
=COUNTIF(A1:A100, E1)
```
Where E1 contains "California"

**Result:** Count of cells matching the value in E1

**Explanation:** Instead of hardcoding criteria, reference a cell. Makes formulas dynamic - change E1 and the count updates. Useful for dropdown-driven dashboards.

---

### Example 6: Wildcard - Starts With
```
=COUNTIF(A1:A100, "A*")
```
**Result:** Count of cells starting with the letter "A"

**Explanation:** The asterisk (*) matches any sequence of characters. "Apple", "Arizona", "A", and "A123" all match. Case-insensitive, so "apple" also matches.

---

### Example 7: Wildcard - Ends With
```
=COUNTIF(A1:A100, "*ing")
```
**Result:** Count of cells ending with "ing"

**Explanation:** Asterisk before the pattern matches anything followed by "ing". "Running", "Pending", "ing" all match. "Inger" does NOT match (pattern must be at the end).

---

### Example 8: Wildcard - Contains
```
=COUNTIF(A1:A100, "*error*")
```
**Result:** Count of cells containing "error" anywhere

**Explanation:** Asterisks on both sides match any text containing "error". "Error occurred", "No errors found", "error" all match. The most flexible wildcard pattern.

---

### Example 9: Wildcard - Single Character (?)
```
=COUNTIF(A1:A100, "???-????")
```
**Result:** Count of cells matching format XXX-XXXX (like phone area code-number)

**Explanation:** Each question mark matches exactly one character. Counts cells with exactly 3 characters, a hyphen, then exactly 4 characters.

---

### Example 10: Counting Numbers in Text Column
```
=COUNTIF(A1:A100, ">0")
```
Where A1:A100 contains mixed text and numbers

**Result:** Count of numeric values greater than 0

**Explanation:** Numeric criteria applied to ranges with mixed content only match numeric cells. Text is ignored. Counts positive numbers only.

---

### Example 11: Counting Blanks with COUNTIF
```
=COUNTIF(A1:A100, "")
```
**Result:** Count of empty cells

**Explanation:** Empty string as criteria matches blank cells. Equivalent to COUNTBLANK for truly empty cells, but may differ for formula-generated empty strings.

---

### Example 12: Dynamic Comparison with Cell Reference
```
=COUNTIF(A1:A100, ">"&B1)
```
Where B1 contains a threshold value like 50

**Result:** Count of cells greater than the value in B1

**Explanation:** Concatenate the operator with a cell reference using &. Creates dynamic thresholds that update when B1 changes. Essential for interactive dashboards.

---

### Example 13: Escaping Wildcards
```
=COUNTIF(A1:A100, "~*")
```
**Result:** Count of cells containing a literal asterisk character

**Explanation:** The tilde (~) escapes the wildcard meaning. Searches for actual asterisk characters. Use ~? for literal question marks.

---

### Example 14: Date Comparison
```
=COUNTIF(A1:A100, ">="&DATE(2024,1,1))
```
**Result:** Count of dates on or after January 1, 2024

**Explanation:** Dates are numbers internally. Concatenate operator with DATE function for date-based criteria. Counts all dates in 2024 and beyond.

---

### Example 15: Counting Specific Number
```
=COUNTIF(A1:A100, 100)
```
**Result:** Count of cells containing exactly 100

**Explanation:** For exact numeric matches, no quotes needed around the number. Counts cells with value 100 precisely.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Returns 0 unexpectedly` | Text case mismatch when case matters | COUNTIF is case-insensitive. For case-sensitive: `=SUMPRODUCT((EXACT(A1:A100,"Apple"))*1)` |
| `Returns 0 unexpectedly` | Criteria syntax wrong (e.g., >50 instead of ">50") | Comparison operators must be in quotes: `">50"` not `>50` |
| `Wildcards not working` | Using wildcards with numeric comparisons | Wildcards only work with text. Cannot use `">10*"` for numbers. |
| `Count includes partial matches` | Expected exact match but got wildcard behavior | Wildcards are automatic for text. For exact match of text with * or ?, escape with ~. |
| `Wrong count with cell reference` | Cell reference contains leading/trailing spaces | TRIM the referenced cell: `=COUNTIF(A1:A100, TRIM(E1))` |
| `#VALUE! error` | Range and criteria are swapped | Ensure range comes first, criteria second. |

## Use Cases

### [[Sales Territory Analysis]]

**Scenario:** A sales manager needs to count orders by region to allocate resources and set targets appropriately.

**Implementation:**
```
California Orders: =COUNTIF(RegionColumn, "California")
West Coast: =COUNTIF(RegionColumn, "California")+COUNTIF(RegionColumn, "Oregon")+COUNTIF(RegionColumn, "Washington")
Alternative West Coast: =SUMPRODUCT(COUNTIF(RegionColumn, {"California","Oregon","Washington"}))
Dynamic Count: =COUNTIF(RegionColumn, SelectedRegion)
```

**Business Application:** Provides instant visibility into regional distribution of sales activity. Supports territory planning and sales force allocation. Enables comparison of performance across regions.

**Technical Details:** For many regions, create a reference table and use SUMPRODUCT with COUNTIF array: `=SUMPRODUCT(COUNTIF(RegionColumn, RegionList))`. This counts all regions in the list with a single formula.

---

### [[Survey Response Categorization]]

**Scenario:** After a customer satisfaction survey, categorize responses into satisfaction levels to generate summary statistics.

**Implementation:**
```
Highly Satisfied (5): =COUNTIF(RatingColumn, 5)
Satisfied (4): =COUNTIF(RatingColumn, 4)
Neutral (3): =COUNTIF(RatingColumn, 3)
Dissatisfied (1-2): =COUNTIF(RatingColumn, "<=2")
Promoters: =COUNTIF(NPSColumn, ">=9")
Detractors: =COUNTIF(NPSColumn, "<=6")
```

**Business Application:** Generates satisfaction distribution for reporting. Calculates Net Promoter Score components. Identifies trends in customer sentiment over time.

**Technical Details:** For rating scales, use COUNTIF for each level and calculate percentages. For NPS: Promoters (9-10), Passives (7-8), Detractors (0-6). NPS = % Promoters - % Detractors.

---

### [[Quality Control - Defect Tracking]]

**Scenario:** Manufacturing quality team tracks defect types to prioritize improvement efforts using Pareto analysis.

**Implementation:**
```
Scratch Defects: =COUNTIF(DefectType, "Scratch*")
Dent Defects: =COUNTIF(DefectType, "*dent*")
Paint Issues: =COUNTIF(DefectType, "Paint*")
Critical Defects: =COUNTIF(SeverityColumn, "Critical")
Above Threshold: =COUNTIF(MeasurementColumn, ">"&UpperLimit)
```

**Business Application:** Identifies most frequent defect types for root cause analysis. Supports Pareto prioritization (fix the 20% of causes creating 80% of defects). Tracks defect rates against targets.

**Technical Details:** Wildcards handle variations in defect descriptions (e.g., "Scratch", "Scratched", "Light Scratch" all match "Scratch*"). Combine with date ranges for trend analysis over time periods.

---

### [[HR - Employee Data Analysis]]

**Scenario:** HR department analyzes workforce composition for compliance reporting and planning.

**Implementation:**
```
Full-Time Employees: =COUNTIF(EmploymentType, "Full-Time")
Remote Workers: =COUNTIF(WorkLocation, "*Remote*")
Engineering Dept: =COUNTIF(Department, "Engineering")
Managers: =COUNTIF(Title, "*Manager*")
High Performers: =COUNTIF(Rating, ">=4")
Tenure 5+ Years: =COUNTIF(StartDate, "<="&DATE(YEAR(TODAY())-5, MONTH(TODAY()), DAY(TODAY())))
```

**Business Application:** Generates headcount reports by category. Supports diversity reporting and compliance. Enables workforce planning and succession analysis.

**Technical Details:** For complex categorizations, build helper columns with IF statements first, then COUNTIF the helper column. This separates logic from counting and makes formulas maintainable.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 2000 onward)
- **Case sensitivity:** Case-INSENSITIVE for text comparisons
- **Wildcards:** Full support for * and ? in text criteria
- **Maximum characters in criteria:** 255 characters
- **Array formula:** Not needed for basic COUNTIF; for counting multiple criteria in one formula, use SUMPRODUCT with COUNTIF array

### Google Sheets
- **Availability:** All versions since launch
- **Case sensitivity:** Case-INSENSITIVE for text comparisons (same as Excel)
- **Wildcards:** Full support for * and ? (same as Excel)
- **Maximum characters:** Similar limits to Excel
- **Array formula:** Native support for array operations without special entry

### Key Difference Alert
COUNTIF behaves identically in Excel and Google Sheets for standard use cases. The main considerations when moving between platforms:
- Both are case-insensitive for text matching
- Both support identical wildcard syntax
- Date handling may differ if date formats are interpreted differently (use DATE function for reliability)
- Very long criteria strings (>255 chars) may behave differently

## Tips and Best Practices

1. **Quote your comparison operators:** Always write `">100"` not `>100`. The entire criterion including operator must be a string. For cell references: `">"&B1` concatenates the operator with the cell value.

2. **Master wildcard patterns:**
   - `"*text*"` = contains "text"
   - `"text*"` = starts with "text"
   - `"*text"` = ends with "text"
   - `"???"` = exactly 3 characters
   - `"A?B*"` = starts with A, any char, B, then anything

3. **Use cell references for dynamic criteria:** Instead of `=COUNTIF(A:A, "California")`, use `=COUNTIF(A:A, F1)` where F1 contains the state. Makes dashboards interactive without formula changes.

4. **Escape special characters with tilde:** To match literal * or ?, prefix with ~. `"~*"` matches an asterisk; `"~?"` matches a question mark.

5. **For multiple criteria, consider COUNTIFS:** COUNTIF handles one criterion. For AND logic (A>10 AND B="Yes"), use COUNTIFS. For OR logic, sum multiple COUNTIFs or use SUMPRODUCT.

6. **COUNTIF for data validation:** Count matching values to find duplicates: `=COUNTIF(A:A, A1)>1` returns TRUE if A1 has duplicates in column A.

7. **Handle blanks explicitly:** Counting blanks with `=COUNTIF(range, "")` differs from counting non-blanks with `=COUNTIF(range, "<>")`. Be explicit about whether you want to include or exclude blanks.

8. **Case-sensitive counting:** For case-sensitive matches, use SUMPRODUCT with EXACT: `=SUMPRODUCT((EXACT(A1:A100, "Apple"))*1)` counts only "Apple", not "apple" or "APPLE".

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[COUNTIFS]] | Counts cells meeting multiple criteria | When you need AND logic across multiple conditions |
| [[SUMIF]] | Sums values meeting a criterion | When you need to sum (not count) conditional values |
| [[AVERAGEIF]] | Averages values meeting a criterion | When you need conditional averaging |
| [[COUNT]] | Counts numeric values | When you just need to count numbers, no condition |
| [[COUNTA]] | Counts non-empty cells | When you need all non-empty cells, no condition |

### Commonly Used Together

**[[COUNTIFS]]** - Multiple criteria counting

*Use together for complex logic:*
```
Either condition (OR): =COUNTIF(A:A,"Red")+COUNTIF(A:A,"Blue")
Both conditions (AND): =COUNTIFS(A:A,"Red",B:B,">100")
```
COUNTIF for OR logic (sum individual counts); COUNTIFS for AND logic.

---

**[[SUMIF]]** - Conditional sum

*Combine for conditional ratios:*
```
=SUMIF(Region,"East",Sales)/COUNTIF(Region,"East")
```
Calculates average sales for East region using conditional sum and count.

---

**[[IF]]** - Conditional logic

*Create counting flags:*
```
=IF(COUNTIF(ProductList, A1)>0, "In Stock", "Not Available")
```
Uses COUNTIF to test existence and IF to display result.

---

**[[SUMPRODUCT]]** - Array calculations

*Case-sensitive or complex counting:*
```
=SUMPRODUCT((EXACT(A1:A100,"Apple"))*(B1:B100>50)*1)
```
Counts "Apple" (case-sensitive) where column B > 50.

---

**[[UNIQUE]]** - Get unique values (Sheets/Excel 365)

*Count distinct values:*
```
Unique items: =COUNTA(UNIQUE(A1:A100))
Each unique: =COUNTIF(A:A, UniqueValue)
```
UNIQUE gets distinct values; COUNTIF counts each one.

---

**[[VLOOKUP]] / [[INDEX/MATCH]]** - Lookup functions

*Validate before lookup:*
```
=IF(COUNTIF(LookupRange, SearchValue)>0, VLOOKUP(...), "Not Found")
```
Check if value exists before attempting lookup to avoid #N/A.

## Official Documentation

- **Microsoft Excel:** [COUNTIF function](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)
- **Google Sheets:** [COUNTIF function](https://support.google.com/docs/answer/3093480)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2000 | Original introduction with full wildcard support |
| Excel 2007 | COUNTIFS introduced | Multi-criteria version added |
| Excel 2010+ | All subsequent versions | No changes to COUNTIF functionality |
| Excel 365 | Continuous updates | Performance improvements for large datasets |
| Google Sheets | Original launch (2006) | Full compatibility with Excel syntax |

---

*Last updated: 2026-01-10*
