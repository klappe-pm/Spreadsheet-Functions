---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics:
- multi-criteria-counting
- advanced-filtering
- wildcard-patterns
- data-analysis
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Count If Multiple Conditions
- Multi-Criteria Count
- Count With Multiple Criteria
- Conditional Count AND
tags:
- statistical
- counting
- conditional
- multi-criteria
- wildcards
- filtering
- AND-logic
---

# COUNTIFS

## Description

**COUNTIFS** counts the number of cells that meet multiple criteria across one or more ranges. It extends COUNTIF's single-criterion capability to handle complex, multi-dimensional filtering using AND logic - all specified conditions must be true for a cell to be counted. COUNTIFS answers questions like: "How many orders are from California AND over $500?" "How many employees are in Sales AND started after 2020?" "How many products are red AND in stock AND under $50?"

The function takes pairs of criteria_range and criteria arguments, and you can specify up to 127 such pairs. Each range must have the same dimensions (same number of rows and columns), and COUNTIFS counts rows where ALL conditions are simultaneously satisfied. This is inherently AND logic - use multiple COUNTIF additions for OR logic instead.

**Wildcard support:** Like COUNTIF, COUNTIFS supports wildcards in text criteria. The asterisk (*) matches any sequence of characters, and the question mark (?) matches exactly one character. You can use wildcards in any or all of your criteria. To match a literal asterisk or question mark, escape it with a tilde (~). Wildcards work only with text criteria, not numeric comparisons.

**Key distinction from COUNTIF:** COUNTIF handles one condition; COUNTIFS handles multiple conditions with AND logic. If you need OR logic ("California OR Oregon"), sum separate COUNTIFs or use SUMPRODUCT. COUNTIFS requires all conditions to be true for counting.

## Syntax

> [!f(x)] COUNTIFS Syntax
>
> ```
> =COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `criteria_range1` | Yes | The first range to evaluate against the corresponding criterion. Must be a contiguous range. |
| `criteria1` | Yes | The condition for the first range. Supports numbers, text, expressions, cell references, and wildcards. |
| `criteria_range2, criteria2, ...` | No | Additional range-criteria pairs. Up to 127 pairs (254 arguments) supported. All ranges must have the same dimensions. |

### Return Value

Returns an integer representing the count of rows where ALL specified criteria are met. Returns 0 if no rows satisfy all conditions. Never returns an error for valid range and criteria combinations.

## Examples

> [!f(x)] COUNTIFS Examples

### Example 1: Two Text Criteria
```
=COUNTIFS(A1:A100, "Sales", B1:B100, "Active")
```
**Result:** Count of rows where column A is "Sales" AND column B is "Active"

**Explanation:** Both conditions must be true. Counts active sales employees, for example. If a row has "Sales" but "Inactive", it does NOT count.

---

### Example 2: Text and Numeric Criteria
```
=COUNTIFS(A1:A100, "California", B1:B100, ">500")
```
**Result:** Count of California orders over $500

**Explanation:** Combines exact text match with numeric comparison. The row must be California AND have value >500 to count.

---

### Example 3: Date Range - Between Two Dates
```
=COUNTIFS(A1:A100, ">="&DATE(2024,1,1), A1:A100, "<="&DATE(2024,12,31))
```
**Result:** Count of dates within the year 2024

**Explanation:** Uses the same range twice with different criteria to create a "between" condition. The date must be >= Jan 1 AND <= Dec 31 to count.

---

### Example 4: Number Range - Between Values
```
=COUNTIFS(B1:B100, ">=50", B1:B100, "<=100")
```
**Result:** Count of values between 50 and 100 (inclusive)

**Explanation:** Applies two conditions to the same range. Value must be at least 50 AND at most 100. Classic pattern for range filtering.

---

### Example 5: Three Criteria
```
=COUNTIFS(A1:A100, "Electronics", B1:B100, "In Stock", C1:C100, "<100")
```
**Result:** Count of electronics products in stock under $100

**Explanation:** All three conditions must be met. Demonstrates COUNTIFS scaling to three (or more) criteria. Each additional pair further filters the results.

---

### Example 6: Wildcard with Multiple Criteria
```
=COUNTIFS(A1:A100, "John*", B1:B100, "Sales", C1:C100, ">=2020")
```
**Result:** Count of Sales people named John (any last name) hired 2020 or later

**Explanation:** "John*" matches "John", "Johnson", "John Smith", etc. Wildcards combine freely with other criteria types.

---

### Example 7: Multiple Wildcards
```
=COUNTIFS(A1:A100, "*error*", B1:B100, "Critical*")
```
**Result:** Count of entries containing "error" where status starts with "Critical"

**Explanation:** Both criteria use wildcards. Finds critical errors, critical issues, etc., where the description mentions "error."

---

### Example 8: Not Equal Combined with Other Criteria
```
=COUNTIFS(A1:A100, "<>Pending", B1:B100, ">0", C1:C100, "West")
```
**Result:** Count of non-pending West region entries with positive values

**Explanation:** <> (not equal) works in COUNTIFS. Counts West region items that are not pending and have value greater than 0.

---

### Example 9: Cell References as Criteria
```
=COUNTIFS(A1:A100, E1, B1:B100, ">"&F1, C1:C100, G1)
```
Where E1="California", F1=500, G1="Active"

**Result:** Dynamic count based on values in E1, F1, G1

**Explanation:** All criteria reference cells rather than hardcoded values. Perfect for dashboards where users select filter values from dropdowns.

---

### Example 10: Counting Unique Combinations
```
=COUNTIFS(A:A, A1, B:B, B1)
```
**Result:** Count of rows matching both A1 and B1 values

**Explanation:** When copied down, this counts how many times each row's combination of A and B appears. Useful for duplicate detection: if result >1, it's a duplicate combination.

---

### Example 11: Same Column, Multiple Conditions
```
=COUNTIFS(A1:A100, ">=A", A1:A100, "<=M")
```
**Result:** Count of text values starting with letters A through M

**Explanation:** Text comparisons work alphabetically. Counts entries where the text value falls in the first half of the alphabet.

---

### Example 12: Excluding Blanks
```
=COUNTIFS(A1:A100, "Sales", B1:B100, "<>")
```
**Result:** Count of Sales entries where column B is not blank

**Explanation:** "<>" means "not empty." Ensures you count only rows where Sales has a corresponding non-blank value in column B.

---

### Example 13: Counting Blanks with Other Criteria
```
=COUNTIFS(A1:A100, "Active", B1:B100, "")
```
**Result:** Count of Active entries where column B is blank

**Explanation:** Empty string "" matches blank cells. Finds Active items that are missing data in column B.

---

### Example 14: Four Criteria - Complex Filter
```
=COUNTIFS(Region, "East", Status, "Active", Amount, ">1000", Date, ">="&TODAY()-30)
```
**Result:** Count of active East region accounts with amount >$1000 and recent activity (last 30 days)

**Explanation:** Demonstrates four simultaneous conditions. Named ranges make the formula readable. All four must be true.

---

### Example 15: Question Mark Wildcard
```
=COUNTIFS(A1:A100, "??-???", B1:B100, "Valid")
```
**Result:** Count of valid codes matching format XX-XXX

**Explanation:** Question marks match exact character counts. Finds valid entries with 2 chars, hyphen, 3 chars format (like "AB-123").

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE! error` | Ranges have different dimensions (row/column counts) | All criteria ranges must have identical dimensions. Check that A1:A100 pairs with B1:B100, not B1:B50. |
| `Returns 0 unexpectedly` | AND logic not matching any rows | All conditions must be true simultaneously. Review each criterion separately with COUNTIF to see which is filtering out data. |
| `Returns 0 unexpectedly` | Criteria syntax error (e.g., >50 instead of ">50") | Comparison operators must be in quotes: `">50"` not `>50`. |
| `Count too low` | Forgetting that COUNTIFS uses AND logic | For OR logic, sum separate COUNTIFs or use SUMPRODUCT. COUNTIFS only counts when ALL conditions match. |
| `Wildcards not working` | Using wildcards with numeric comparisons | Wildcards only work with text. Use comparison operators for numbers. |
| `Unexpected matches` | Criteria matching more than intended | Be specific with wildcards. "A*" matches anything starting with A. Use exact matches or more specific patterns when needed. |

## Use Cases

### [[Sales Performance Segmentation]]

**Scenario:** Sales leadership needs to segment deals by multiple dimensions - region, size, and stage - to analyze pipeline health and forecast accuracy.

**Implementation:**
```
Enterprise Deals in West: =COUNTIFS(Region, "West", DealSize, "Enterprise", Stage, "Negotiation")
Small Deals Won This Quarter: =COUNTIFS(DealSize, "Small", Stage, "Won", CloseDate, ">="&QuarterStart, CloseDate, "<="&QuarterEnd)
Lost Deals Over $100K: =COUNTIFS(Stage, "Lost", Amount, ">100000")
Active Pipeline by Rep: =COUNTIFS(SalesRep, RepName, Stage, "<>Won", Stage, "<>Lost")
```

**Business Application:** Enables granular pipeline analysis beyond simple totals. Supports territory planning by showing opportunity distribution. Identifies patterns in wins/losses by segment for coaching.

**Technical Details:** Use named ranges for readability. Build a segmentation matrix with COUNTIFS in each cell. Create dropdown selectors that feed into criteria references for interactive dashboards.

---

### [[Inventory Management with Multiple Constraints]]

**Scenario:** Warehouse manager needs to identify products requiring action based on combinations of stock level, age, and category.

**Implementation:**
```
Reorder Needed (Active + Low Stock): =COUNTIFS(Status, "Active", StockQty, "<"&ReorderPoint)
Overstock (Active + High Stock + Slow Moving): =COUNTIFS(Status, "Active", StockQty, ">"&MaxStock, TurnoverRate, "<2")
Clearance Candidates: =COUNTIFS(Age, ">"&365, Category, "<>Seasonal", StockQty, ">0")
Priority Restock: =COUNTIFS(Category, "Fast Mover", StockQty, "<=0", Status, "Active")
```

**Business Application:** Automates identification of inventory requiring action. Balances multiple business rules that cannot be captured with single conditions. Supports lean inventory management.

**Technical Details:** Define threshold values in named cells for easy adjustment. Create a dashboard summarizing each category count. Use conditional formatting to highlight concerning counts.

---

### [[HR Compliance and Reporting]]

**Scenario:** HR needs to count employees meeting specific combinations of criteria for compliance reporting, diversity metrics, and workforce planning.

**Implementation:**
```
Full-Time Engineers Over 5 Years: =COUNTIFS(EmploymentType, "Full-Time", Department, "Engineering", StartDate, "<="&DATE(YEAR(TODAY())-5, MONTH(TODAY()), DAY(TODAY())))
Remote Managers: =COUNTIFS(Title, "*Manager*", WorkLocation, "Remote")
New Hires in Protected Classes: =COUNTIFS(StartDate, ">="&YearStart, DiversityCategory, "<>Not Specified")
Eligible for Review: =COUNTIFS(LastReview, "<="&DATE(YEAR(TODAY())-1, MONTH(TODAY()), DAY(TODAY())), Status, "Active", EmploymentType, "<>Contractor")
```

**Business Application:** Generates accurate compliance metrics automatically. Supports diversity reporting with multiple demographic filters. Enables workforce analysis for succession planning.

**Technical Details:** Build comprehensive reporting templates with COUNTIFS for each metric. Validate results against system of record. Document criteria definitions for audit purposes.

---

### [[Customer Segmentation and Targeting]]

**Scenario:** Marketing team segments customers by behavior, demographics, and engagement for targeted campaign creation.

**Implementation:**
```
High-Value Active Customers: =COUNTIFS(LifetimeValue, ">1000", LastPurchase, ">="&DATE(YEAR(TODAY()), MONTH(TODAY())-3, DAY(TODAY())), Status, "Active")
Lapsed VIPs: =COUNTIFS(Segment, "VIP", LastPurchase, "<"&DATE(YEAR(TODAY()), MONTH(TODAY())-12, DAY(TODAY())))
New High-Potential: =COUNTIFS(FirstPurchase, ">="&DATE(YEAR(TODAY()), 1, 1), OrderCount, ">=3", AvgOrderValue, ">100")
At-Risk Premium: =COUNTIFS(Segment, "Premium", EngagementScore, "<50", Tenure, ">365")
```

**Business Application:** Identifies precise customer segments for targeted marketing. Finds at-risk high-value customers for retention efforts. Discovers emerging high-value customers for nurturing.

**Technical Details:** Calculate date thresholds dynamically using TODAY() for always-current segments. Create segment size dashboards that auto-update. Export segment counts for marketing automation system integration.

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 2007 and later
- **Maximum criteria pairs:** 127 range-criteria pairs (254 total arguments)
- **Case sensitivity:** Case-INSENSITIVE for text comparisons
- **Wildcards:** Full support for * and ? in text criteria
- **Range size limit:** All ranges must have identical dimensions
- **Array behavior:** Not needed for standard COUNTIFS usage

### Google Sheets
- **Availability:** All versions since launch
- **Maximum criteria pairs:** Similar to Excel (127+ pairs)
- **Case sensitivity:** Case-INSENSITIVE (same as Excel)
- **Wildcards:** Full support for * and ? (same as Excel)
- **Range size limit:** Same requirement - identical dimensions
- **Array behavior:** Native support without special entry

### Key Difference Alert
COUNTIFS behaves identically in Excel and Google Sheets for standard use cases. Key considerations:
- Both require all criteria ranges to have the same dimensions
- Both use AND logic (all conditions must be met)
- Wildcard behavior is identical
- Date handling relies on proper date values (use DATE function for cross-platform reliability)

The most common "difference" users encounter is actually operator error - forgetting to match range sizes or mixing up AND vs. OR logic requirements.

## Tips and Best Practices

1. **Match your range dimensions:** All criteria ranges MUST have the same number of rows and columns. `=COUNTIFS(A1:A100, "X", B1:B50, "Y")` will error because ranges differ in size.

2. **Remember: COUNTIFS = AND logic:** Every condition must be true for a row to count. For OR logic, sum individual COUNTIFs: `=COUNTIF(A:A,"X")+COUNTIF(A:A,"Y")`.

3. **Use the same range twice for "between":** To count values between 50 and 100: `=COUNTIFS(A:A, ">=50", A:A, "<=100")`. Both conditions apply to the same column.

4. **Debug with individual COUNTIFs:** If COUNTIFS returns 0 unexpectedly, test each criterion separately with COUNTIF to see which one filters out all data.

5. **Leverage wildcards for flexible text matching:**
   - "John*" = starts with John
   - "*error*" = contains error
   - "???-????" = format XXX-XXXX
   - "~*" = literal asterisk

6. **Use cell references for dynamic dashboards:** `=COUNTIFS(A:A, $G$1, B:B, ">"&$H$1)` lets users change G1 and H1 to filter interactively without editing formulas.

7. **Exclude blanks when needed:** Add `<>""` or `<>` as a criterion to ensure blank cells do not corrupt your counts: `=COUNTIFS(Category, "Sales", Amount, "<>")`.

8. **Consider SUMPRODUCT for complex OR logic:** When you need OR with AND combinations, SUMPRODUCT offers more flexibility: `=SUMPRODUCT(((A:A="X")+(A:A="Y"))*(B:B>50))` counts where A is X OR Y AND B>50.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[COUNTIF]] | Counts cells meeting single criterion | When you only have one condition to apply |
| [[SUMIFS]] | Sums values meeting multiple criteria | When you need to sum values, not count rows |
| [[AVERAGEIFS]] | Averages values meeting multiple criteria | When you need conditional averaging |
| [[MINIFS]] / [[MAXIFS]] | Min/max of values meeting criteria | When you need conditional min or max |
| [[FILTER]] | Returns matching rows (dynamic array) | When you need the actual matching rows, not just a count |

### Commonly Used Together

**[[COUNTIF]]** - Single criterion counting

*Use together for OR logic:*
```
Either condition: =COUNTIF(A:A,"Red") + COUNTIF(A:A,"Blue")
With additional AND: Use SUMPRODUCT for complex logic
```
COUNTIF handles individual conditions; sum them for OR logic.

---

**[[SUMIFS]]** - Multi-criteria summing

*Combine for conditional statistics:*
```
Average for segment: =SUMIFS(Amount, Region, "East", Status, "Active") / COUNTIFS(Region, "East", Status, "Active")
```
Calculates average by dividing conditional sum by conditional count.

---

**[[SUMPRODUCT]]** - Array calculations

*Handle complex OR with AND:*
```
=SUMPRODUCT(((A1:A100="Red")+(A1:A100="Blue"))*(B1:B100>50)*1)
```
Counts rows where color is Red OR Blue AND value >50. COUNTIFS cannot do this directly.

---

**[[IF]]** - Conditional logic

*Use COUNTIFS results in decisions:*
```
=IF(COUNTIFS(Status, "Open", Priority, "High")>10, "Overloaded", "OK")
```
Takes action based on multi-criteria counts.

---

**[[MATCH]] / [[INDEX]]** - Lookup functions

*Validate complex criteria before lookup:*
```
=IF(COUNTIFS(IDColumn, SearchID, StatusColumn, "Active")>0, INDEX(...), "Not Found or Inactive")
```
Ensures lookup target exists AND meets additional criteria.

---

**[[UNIQUE]] / [[FILTER]]** - Dynamic array functions (Excel 365/Sheets)

*Count unique combinations:*
```
Unique combos: =ROWS(UNIQUE(FILTER(A:B, A:A<>"")))
Each combo count: =COUNTIFS(A:A, UniqueA, B:B, UniqueB)
```
Modern approach to counting distinct multi-column combinations.

## Official Documentation

- **Microsoft Excel:** [COUNTIFS function](https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)
- **Google Sheets:** [COUNTIFS function](https://support.google.com/docs/answer/3256550)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2007 | Introduced as part of "IFS" function family |
| Excel 2010+ | All subsequent versions | No changes to core functionality |
| Excel 2016 | MAXIFS/MINIFS added | Complementary functions expanded |
| Excel 365 | Continuous updates | Performance improvements for large datasets |
| Google Sheets | Original launch (2006) | Full compatibility with Excel syntax |

---

*Last updated: 2026-01-10*
