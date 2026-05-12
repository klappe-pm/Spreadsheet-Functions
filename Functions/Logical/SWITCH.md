---
categories:
  - spreadsheet-functions
subCategories:
  - excel
  - sheets
topics:
  - logical
subTopics:
  - value-matching
  - case-statement
  - code-translation
  - lookup-alternative
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - case-statement
  - select-case
  - value-switch
  - code-mapper
tags:
  - logical
  - conditional
  - value-matching
  - case-switch
  - code-translation
  - lookup-alternative
  - excel
  - google-sheets
---

# SWITCH

## Description

The **SWITCH function** evaluates an expression against a list of values and returns the result corresponding to the first matching value, functioning like a "case statement" or "select case" structure found in programming languages. Unlike IFS, which evaluates multiple independent conditions, SWITCH compares a single expression against multiple possible values, returning the corresponding result when a match is found. This makes SWITCH ideal for scenarios where you're mapping specific values to specific outputs, such as translating status codes into descriptions, converting department numbers into department names, or mapping abbreviations to full text. The function takes an expression to evaluate, followed by pairs of value-result arguments, with an optional default value at the end.

SWITCH provides a dramatically cleaner syntax than nested IF statements when you need to match against specific values. Consider translating a department code: using IF, you'd write `=IF(A1=1,"Sales",IF(A1=2,"Marketing",IF(A1=3,"Engineering",IF(A1=4,"Finance","Unknown"))))`. With SWITCH, this becomes `=SWITCH(A1,1,"Sales",2,"Marketing",3,"Engineering",4,"Finance","Unknown")`. The SWITCH version is not only shorter but also clearer—the value-result pairs are visually aligned, making it immediately obvious what each code maps to. This readability advantage grows with more values; a 10-option nested IF becomes nearly unreadable while a 10-option SWITCH remains perfectly clear.

There are several important gotchas to understand when working with SWITCH. First, SWITCH performs exact matching only—it cannot do pattern matching, wildcards, or range comparisons. If you need to test whether a value is greater than 10 or falls within a range, use IFS instead. Second, SWITCH matches the FIRST value that matches and ignores subsequent matching pairs, so the order of your value-result pairs matters if you accidentally include duplicates. Third, if no values match and no default is provided, SWITCH returns #N/A error. Always provide a default value as the final argument unless you specifically want #N/A to indicate unhandled cases. Fourth, SWITCH evaluates the expression argument only once, then compares it against each value—this is more efficient than nested IFs that might re-evaluate the expression multiple times. Fifth, SWITCH uses the same comparison rules as the equality operator (=), meaning text comparisons are case-insensitive by default.

Platform support for SWITCH is similar to IFS: Excel introduced SWITCH in Excel 2016, so it's unavailable in Excel 2013 and earlier. Google Sheets has supported SWITCH since early in its development. Both platforms implement SWITCH identically with the same syntax and behavior. For backward compatibility with older Excel versions, you can use nested IF or create a lookup table with VLOOKUP. SWITCH supports up to 126 value-result pairs (253 arguments total including the expression and optional default), which is more than enough for any practical use case. Performance is excellent on both platforms since SWITCH's single-expression-evaluation model is inherently efficient.

## Syntax

> [!f(x)] SWITCH Syntax
>
> ```
> =SWITCH(expression, value1, result1, [value2, result2], ..., [default])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `expression` | Yes | The value or formula to evaluate and compare against the value arguments. Can be a cell reference, formula result, or literal value. This is evaluated once and compared against each value in sequence. |
| `value1` | Yes | The first value to compare against the expression. If expression equals value1, the function returns result1. Comparison is exact match and case-insensitive for text. |
| `result1` | Yes | The value to return if expression equals value1. Can be any value: number, text, cell reference, formula, or even an error value. |
| `value2, result2` | No | Additional value-result pairs. Each pair is tested in order if previous values don't match. You can include up to 126 pairs. |
| `default` | No | The value to return if no value matches the expression. If omitted and no match is found, SWITCH returns #N/A. Strongly recommended to always include a default. |

### Return Value

Returns the result corresponding to the first value that matches the expression. If no value matches and a default is provided, returns the default. If no value matches and no default is provided, returns #N/A error. The function stops comparing as soon as it finds a match.

### Comparison Behavior

| Expression Type | Value Type | Matching Behavior |
|----------------|------------|-------------------|
| Number | Number | Exact numeric match |
| Text | Text | Case-insensitive match ("ABC" = "abc") |
| Boolean | Boolean | TRUE matches TRUE, FALSE matches FALSE |
| Date | Date | Exact date serial number match |
| Error | Error | Errors can be matched (e.g., #N/A) |
| Mixed types | Mixed types | Different types never match (1 does not equal "1") |

## Examples

> [!f(x)] SWITCH Examples

### Example 1: Department Code Translation
```
=SWITCH(A1, 1, "Sales", 2, "Marketing", 3, "Engineering", 4, "Finance", "Unknown")
```
**Result:** Returns department name based on numeric code (e.g., 2 returns "Marketing")

**Explanation:** This is the classic SWITCH use case. The expression A1 is compared against each value (1, 2, 3, 4) in order. When a match is found, the corresponding result is returned. "Unknown" at the end is the default value returned if A1 contains a value not in the list (like 5 or 99).

---

### Example 2: Nested IF vs SWITCH Comparison
```
Nested IF (hard to read and maintain):
=IF(A1="R","Red",IF(A1="G","Green",IF(A1="B","Blue",IF(A1="Y","Yellow","Unknown"))))

SWITCH equivalent (clean and readable):
=SWITCH(A1, "R", "Red", "G", "Green", "B", "Blue", "Y", "Yellow", "Unknown")
```
**Result:** Both return color names based on single-letter codes

**Explanation:** This comparison demonstrates why SWITCH was created. The nested IF requires tracking parentheses and understanding the nested structure. SWITCH reads linearly: if R then Red, if G then Green, etc. The logic is identical but SWITCH is dramatically easier to read, write, and modify.

---

### Example 3: Day Number to Day Name
```
=SWITCH(WEEKDAY(A1), 1, "Sunday", 2, "Monday", 3, "Tuesday", 4, "Wednesday", 5, "Thursday", 6, "Friday", 7, "Saturday")
```
**Result:** Returns day name for a date (e.g., "Tuesday" for a Tuesday date)

**Explanation:** SWITCH works with formula results as the expression. WEEKDAY returns a number 1-7, and SWITCH maps each to the corresponding day name. Note that no default is needed here because WEEKDAY always returns 1-7, so all cases are covered.

---

### Example 4: Month Number to Quarter
```
=SWITCH(MONTH(A1), 1, "Q1", 2, "Q1", 3, "Q1", 4, "Q2", 5, "Q2", 6, "Q2", 7, "Q3", 8, "Q3", 9, "Q3", 10, "Q4", 11, "Q4", 12, "Q4")
```
**Result:** Returns fiscal quarter based on month (e.g., March returns "Q1")

**Explanation:** Multiple values can map to the same result. This formula maps all 12 months to their respective quarters. While this could also be done with IFS using range comparisons, SWITCH is cleaner when you want explicit mapping of each value.

---

### Example 5: Grade Letter to Points
```
=SWITCH(B1, "A+", 4.0, "A", 4.0, "A-", 3.7, "B+", 3.3, "B", 3.0, "B-", 2.7, "C+", 2.3, "C", 2.0, "C-", 1.7, "D+", 1.3, "D", 1.0, "F", 0.0, "Invalid Grade")
```
**Result:** Converts letter grade to GPA points (e.g., "B+" returns 3.3)

**Explanation:** Academic systems often need to convert letter grades to numeric GPA values. SWITCH handles this cleanly with exact string matching. Text comparisons are case-insensitive, so "b+" matches "B+". The default "Invalid Grade" catches typos or unexpected inputs.

---

### Example 6: Status Code with Formula Results
```
=SWITCH(A1, "P", "Pending Review", "A", "Approved", "R", "Rejected", "H", "On Hold") & " since " & TEXT(B1, "MM/DD/YYYY")
```
**Result:** "Approved since 01/15/2024" (combining SWITCH with text concatenation)

**Explanation:** SWITCH can be part of larger expressions. This formula translates a status code, then appends the date. The entire SWITCH result is concatenated with additional text. Note: if A1 doesn't match any value, SWITCH returns #N/A which causes the whole concatenation to error.

---

### Example 7: Country Code to Region
```
=SWITCH(CountryCode,
  "US", "North America",
  "CA", "North America",
  "MX", "North America",
  "UK", "Europe",
  "DE", "Europe",
  "FR", "Europe",
  "JP", "Asia Pacific",
  "CN", "Asia Pacific",
  "AU", "Asia Pacific",
  "Other")
```
**Result:** Maps country codes to sales regions

**Explanation:** SWITCH excels at grouping specific values into categories. This formula maps country codes to sales regions. The multi-line format (allowed in both Excel and Sheets formula bar) improves readability for many mappings. The "Other" default catches countries not explicitly listed.

---

### Example 8: Priority Number to Color Name for Conditional Formatting
```
=SWITCH(A1, 1, "Red", 2, "Orange", 3, "Yellow", 4, "Green", "Gray")
```
**Result:** Returns color name for use in conditional formatting or VBA

**Explanation:** While you can't directly apply colors with SWITCH, you can return color names or codes that other systems use. This pattern is useful in dashboards where a helper column provides color information for conditional formatting rules or chart styling.

---

### Example 9: Boolean to Custom Text
```
=SWITCH(A1, TRUE, "Yes, Active", FALSE, "No, Inactive", "Unknown Status")
```
**Result:** Converts TRUE/FALSE to custom descriptive text

**Explanation:** SWITCH can match boolean values. This is cleaner than `=IF(A1=TRUE, "Yes, Active", IF(A1=FALSE, "No, Inactive", "Unknown Status"))`. The default handles cases where A1 might contain a non-boolean value due to data issues.

---

### Example 10: Handling Errors as Values
```
=SWITCH(A1, 0, "Zero", 1, "One", #N/A, "Not Available", #DIV/0!, "Division Error", "Other Error")
```
**Result:** Can match error values as switch cases

**Explanation:** SWITCH can compare against error values directly. This is useful for processing data that might contain errors, mapping each error type to a description. Note: This matches errors in the expression A1, not errors in the SWITCH function itself.

---

### Example 11: Fiscal Year Based on Month
```
=SWITCH(TRUE,
  MONTH(A1)>=7, "FY" & YEAR(A1)+1,
  TRUE, "FY" & YEAR(A1))
```
**Result:** Returns fiscal year (July-June fiscal calendar)

**Explanation:** The "SWITCH(TRUE, ...)" pattern mimics IFS behavior, allowing condition testing rather than exact value matching. Each "value" argument becomes a condition that evaluates to TRUE or FALSE. The first TRUE match wins. However, IFS is generally clearer for this pattern.

---

### Example 12: Unit Conversion Factors
```
=A1 * SWITCH(B1, "kg", 2.205, "lb", 1, "oz", 0.0625, "g", 0.002205, 0)
```
**Result:** Converts weight to pounds based on unit in B1

**Explanation:** SWITCH can return numbers for use in calculations. This formula multiplies a value by the conversion factor determined by the unit. If the unit isn't recognized, the 0 default makes the result 0 (potentially flagging data issues better than a random incorrect conversion).

---

### Example 13: Case-Insensitive Text Matching
```
=SWITCH(UPPER(A1), "YES", TRUE, "Y", TRUE, "TRUE", TRUE, "1", TRUE, FALSE)
```
**Result:** Interprets various "yes" representations as TRUE

**Explanation:** While SWITCH is already case-insensitive for text, using UPPER() ensures consistent matching even with unusual data. This formula treats "yes", "YES", "Yes", "y", "Y", "true", "TRUE", and "1" all as TRUE, with everything else as FALSE.

---

### Example 14: Error Handling with Default
```
=IFERROR(SWITCH(A1, "A", 100, "B", 200, "C", 300), "Invalid Input")
```
**Result:** Returns mapped value or "Invalid Input" if A1 doesn't match and would return #N/A

**Explanation:** Without a default, SWITCH returns #N/A for unmatched values. Wrapping in IFERROR provides a custom message. However, it's usually cleaner to just add a default to SWITCH: `=SWITCH(A1, "A", 100, "B", 200, "C", 300, "Invalid Input")`.

---

### Example 15: Nested SWITCH (Rarely Needed)
```
=SWITCH(A1,
  "Type1", SWITCH(B1, "Sub1", 10, "Sub2", 20, 0),
  "Type2", SWITCH(B1, "Sub1", 30, "Sub2", 40, 0),
  0)
```
**Result:** Two-level mapping based on type and subtype

**Explanation:** SWITCH can be nested when you need two-dimensional mapping. The outer SWITCH selects based on A1, and each result is itself a SWITCH based on B1. While this works, consider using a lookup table with INDEX+MATCH for complex multi-dimensional mappings—it's often more maintainable.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | No value matched and no default was provided | Add a default value as the final argument to handle unmatched cases |
| `#VALUE!` | Odd number of arguments without a default in unexpected position | Ensure value-result pairs are complete; the odd final argument is treated as default |
| `#NAME?` | Function not recognized (older Excel) | SWITCH requires Excel 2016+; use nested IF or CHOOSE for older versions |
| `No match when expected` | Text case mismatch (rare) or type mismatch | Verify expression and values are the same data type; "1" (text) does not match 1 (number) |
| `Wrong result returned` | Duplicate values in list (first match wins) | Review value-result pairs for duplicates; SWITCH stops at first match |
| `Formula too long` | Exceeded 253 arguments (126 pairs + expression + default) | Use lookup table with VLOOKUP/INDEX+MATCH for very large mappings |
| `#REF!` | Cell reference in result has been deleted | Fix broken references in result arguments |
| `Unexpected default returned` | Expression contains trailing spaces or hidden characters | Use TRIM on expression: `=SWITCH(TRIM(A1), ...)` |

## Use Cases

### [[Product Category Classification System]]

**Scenario:** A retail company needs to classify thousands of products into categories based on SKU prefixes. Each prefix (first 2-3 characters of SKU) maps to a specific category, and the system must handle new prefixes gracefully while flagging them for review.

**Implementation:**
```
Category Assignment:
=SWITCH(LEFT(SKU, 2),
  "EL", "Electronics",
  "AP", "Apparel",
  "HO", "Home & Garden",
  "SP", "Sports & Outdoors",
  "TO", "Toys & Games",
  "BE", "Beauty & Personal Care",
  "FO", "Food & Grocery",
  "BO", "Books & Media",
  "AU", "Automotive",
  "PE", "Pet Supplies",
  "NEW CATEGORY - Review SKU: " & SKU)

Subcategory (nested SWITCH):
=SWITCH(LEFT(SKU, 2),
  "EL", SWITCH(MID(SKU, 3, 1), "C", "Computers", "T", "TVs", "P", "Phones", "A", "Audio", "Other Electronics"),
  "AP", SWITCH(MID(SKU, 3, 1), "M", "Men's", "W", "Women's", "K", "Kids'", "Other Apparel"),
  "General")

Margin Tier:
=SWITCH(Category,
  "Electronics", "Tier1",
  "Apparel", "Tier2",
  "Home & Garden", "Tier2",
  "Food & Grocery", "Tier3",
  "Tier2")
```

**Business Application:** Retail and inventory systems frequently need to derive attributes from product codes. SWITCH provides a maintainable way to map code prefixes to categories without creating complex lookup tables for simple mappings. The clear value-result structure makes it easy for merchandising teams to review and update mappings when new product lines are added.

**Technical Details:** Using LEFT() or MID() to extract SKU components before SWITCH is a common pattern. The default value that includes the original SKU helps buyers identify which new prefixes need category assignment. For very large prefix lists (50+), consider moving the mapping to a lookup table and using XLOOKUP or INDEX+MATCH instead—it's easier to maintain and doesn't require formula changes when mappings change.

---

### [[Employee Compensation Calculations]]

**Scenario:** HR needs to calculate bonuses based on employee grade levels. Each grade (E1-E5 for employees, M1-M3 for managers, D1-D2 for directors) has a specific bonus percentage and eligibility rules. The system must handle all grades and flag invalid grade codes.

**Implementation:**
```
Bonus Percentage:
=SWITCH(GradeLevel,
  "E1", 0.05,
  "E2", 0.08,
  "E3", 0.10,
  "E4", 0.12,
  "E5", 0.15,
  "M1", 0.18,
  "M2", 0.22,
  "M3", 0.25,
  "D1", 0.30,
  "D2", 0.35,
  0)

Employee Category:
=SWITCH(LEFT(GradeLevel, 1),
  "E", "Individual Contributor",
  "M", "Manager",
  "D", "Director",
  "Unknown")

Stock Grant Multiple:
=SWITCH(GradeLevel,
  "E1", 0, "E2", 0, "E3", 0, "E4", 0.5, "E5", 1.0,
  "M1", 1.5, "M2", 2.0, "M3", 2.5,
  "D1", 3.0, "D2", 4.0,
  0)

Bonus Amount:
=IF(GradeLevel<>"", BaseSalary * BonusPercentage * PerformanceMultiplier, "No Grade")
```

**Business Application:** Compensation structures typically have discrete levels with specific benefits at each level. SWITCH creates a clear mapping that HR administrators can easily audit against compensation policies. Unlike lookup tables that might be accidentally modified, SWITCH formulas embed the compensation rules directly, making them visible and version-controllable alongside other spreadsheet logic.

**Technical Details:** When multiple attributes depend on the same grade level (bonus %, stock grants, benefits tier), calculate the grade-dependent values in helper columns using SWITCH, then reference those helper columns in other calculations. This avoids repeating the SWITCH mapping in multiple formulas. Consider data validation on the grade level input to prevent typos before they reach the SWITCH formulas.

---

### [[Customer Communication Template Selection]]

**Scenario:** A customer service system needs to select appropriate response templates based on issue type codes. Each code maps to a specific template, and the system must track which template was used while handling unknown codes gracefully.

**Implementation:**
```
Template Name:
=SWITCH(IssueCode,
  "PWD", "Password Reset Instructions",
  "ACC", "Account Access Help",
  "BIL", "Billing Inquiry Response",
  "REF", "Refund Request Process",
  "SHP", "Shipping Status Information",
  "RET", "Return Instructions",
  "PRD", "Product Information",
  "COM", "Complaint Acknowledgment",
  "ESC", "Escalation Notice",
  "GEN", "General Inquiry Response",
  "MANUAL RESPONSE REQUIRED")

Template ID for System:
=SWITCH(IssueCode,
  "PWD", 1001,
  "ACC", 1002,
  "BIL", 2001,
  "REF", 2002,
  "SHP", 3001,
  "RET", 3002,
  "PRD", 4001,
  "COM", 5001,
  "ESC", 9001,
  "GEN", 9999,
  0)

Expected Response Time:
=SWITCH(IssueCode,
  "PWD", "2 hours",
  "ACC", "2 hours",
  "BIL", "1 business day",
  "REF", "1 business day",
  "SHP", "4 hours",
  "RET", "1 business day",
  "PRD", "4 hours",
  "COM", "4 hours",
  "ESC", "1 hour",
  "GEN", "1 business day",
  "Review Required")
```

**Business Application:** Customer service operations rely on consistent responses driven by issue classification. SWITCH enables rapid template selection based on issue codes, improving response time and consistency. The clear code-to-template mapping also serves as documentation for training new customer service representatives.

**Technical Details:** The three SWITCH formulas all use the same issue code but return different attributes (name, ID, SLA). This is more maintainable than a single complex lookup because each attribute can be modified independently. For systems that track template usage metrics, the numeric Template ID is easier to aggregate than text names. Consider adding a validation SWITCH that returns "VALID" for known codes and "INVALID" for unknown codes to flag data entry issues before they affect customer communications.

---

### [[Financial Report Period Mapping]]

**Scenario:** A financial reporting system must map fiscal periods to various date-related attributes for report headers, comparative analysis, and time-series visualizations. Period codes follow the format "FYQQ" (e.g., "24Q1" for fiscal year 2024, quarter 1).

**Implementation:**
```
Quarter Display Name:
=SWITCH(RIGHT(PeriodCode, 2),
  "Q1", "First Quarter",
  "Q2", "Second Quarter",
  "Q3", "Third Quarter",
  "Q4", "Fourth Quarter",
  "Unknown Quarter")

Fiscal Year:
="FY20" & LEFT(PeriodCode, 2)

Period Start Month:
=SWITCH(RIGHT(PeriodCode, 2),
  "Q1", "January",
  "Q2", "April",
  "Q3", "July",
  "Q4", "October",
  "Unknown")

Prior Year Period:
=TEXT(VALUE("20" & LEFT(PeriodCode, 2)) - 1, "00") & RIGHT(PeriodCode, 2)

Report Header:
=SWITCH(RIGHT(PeriodCode, 2),
  "Q1", "January - March",
  "Q2", "April - June",
  "Q3", "July - September",
  "Q4", "October - December",
  "Full Year") & " FY20" & LEFT(PeriodCode, 2)
```

**Business Application:** Financial reporting requires consistent period naming across dozens of reports. SWITCH ensures that "Q3" always displays as "Third Quarter" everywhere, eliminating inconsistencies that could confuse stakeholders. The period code serves as a single source of truth, with SWITCH deriving all period-related text.

**Technical Details:** By parsing the period code with LEFT() and RIGHT() before applying SWITCH, you can handle any fiscal year without updating the formulas. The SWITCH only maps quarter numbers (Q1-Q4), which are constant, while the year is calculated dynamically. This pattern separates the fixed mappings (SWITCH) from the variable components (calculations), making the system more maintainable.

## Platform Differences

### Microsoft Excel

- **Availability:** Excel 2016 and later (desktop), Excel for Microsoft 365, Excel Online
- **Not available:** Excel 2013 and earlier versions
- **Argument limit:** Up to 254 arguments (126 value-result pairs + expression + default)
- **Array support:** Works with array formulas in Excel 365
- **Performance:** Single expression evaluation; efficient for many comparisons
- **Alternative for older versions:** Nested IF or CHOOSE (for numeric 1-29 values)

### Google Sheets

- **Availability:** All versions since early Sheets development
- **Argument limit:** Similar to Excel, effectively unlimited for practical use
- **Array support:** Works natively with arrays using ARRAYFORMULA
- **Performance:** Excellent; comparable to Excel
- **QUERY alternative:** For data transformation scenarios, QUERY may be more efficient

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Version requirement | 2016+ | All versions |
| Maximum value-result pairs | 126 pairs | Effectively unlimited |
| Array formula support | Native in 365 | Via ARRAYFORMULA |
| Backward compatibility | Requires nested IF for older Excel | No compatibility issues |
| Text comparison | Case-insensitive | Case-insensitive |
| Type coercion | Strict (number != text number) | Strict |
| Mobile support | Full support | Full support |
| Performance | Excellent | Excellent |

### Alternative for Excel 2013 and Earlier

```
Excel 2016+ (recommended):
=SWITCH(A1, "A", 100, "B", 200, "C", 300, 0)

Excel 2013 and earlier with CHOOSE (if values are 1-29):
=CHOOSE(MATCH(A1, {"A","B","C"}, 0), 100, 200, 300)

Excel 2013 and earlier with nested IF:
=IF(A1="A", 100, IF(A1="B", 200, IF(A1="C", 300, 0)))

Excel 2013 and earlier with VLOOKUP:
=IFNA(VLOOKUP(A1, {"A",100;"B",200;"C",300}, 2, FALSE), 0)
```

## Tips and Best Practices

1. **Always provide a default value:** SWITCH returns #N/A when no value matches. Always include a default as the final argument unless you specifically want #N/A to flag unhandled cases. The default is your safety net for unexpected data.

2. **Use SWITCH for exact value matching, IFS for conditions:** SWITCH is ideal when you're comparing against specific values (codes, categories, status). If you need range comparisons (>10, <=100) or complex conditions, use IFS instead. Choose the right tool for the job.

3. **Format SWITCH formulas for readability:** For formulas with many value-result pairs, use line breaks in the formula bar (Alt+Enter) to put each pair on its own line. This makes the mapping visually clear and easier to maintain: one value-result pair per line.

4. **Verify data types match:** SWITCH uses strict type comparison. The number 1 does not match the text "1". If your data might have type inconsistencies, use VALUE() to convert text numbers or TEXT() to convert numbers to text before the SWITCH expression.

5. **Consider lookup tables for large mappings:** While SWITCH handles up to 126 pairs, formulas with more than 15-20 pairs become hard to maintain. For large mappings, create a lookup table in a reference sheet and use XLOOKUP or INDEX+MATCH. Lookup tables are easier to update without modifying formulas.

6. **Use SWITCH(TRUE, ...) sparingly:** The pattern `=SWITCH(TRUE, condition1, result1, condition2, result2, default)` mimics IFS, but IFS is clearer for conditional logic. Use this pattern only in specific edge cases where SWITCH must be used.

7. **Document your mappings:** For business-critical SWITCH formulas, add a comment cell nearby listing the mappings, or maintain a reference table that mirrors the SWITCH values. This helps future maintainers understand the code-to-description mappings without decoding the formula.

8. **Test edge cases and the default:** Verify that all expected values return correct results AND that unexpected values hit the default appropriately. Pay special attention to empty cells, spaces, and case variations in text values.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[IFS]] | Evaluates multiple independent conditions | When you need range testing (>=10), complex conditions (AND/OR), or non-equality comparisons |
| [[IF]] | Single condition with true/false branches | For simple true/false decisions; single condition testing |
| [[CHOOSE]] | Returns value from list by index number | When you have numeric indices 1-254 and want to return corresponding values |
| [[VLOOKUP]] | Vertical lookup in table | When your value-result mapping is stored in a table rather than hardcoded in formula |
| [[XLOOKUP]] | Modern flexible lookup | When mappings are in a table; offers more flexibility than VLOOKUP |
| [[INDEX+MATCH]] | Flexible lookup combination | For complex lookups; when mappings are maintained in reference tables |

### Commonly Used Together

**[[LEFT]]/[[RIGHT]]/[[MID]]** - Extract portions of codes before SWITCH

*Use text functions to parse codes before matching:*
```
=SWITCH(LEFT(ProductCode, 2), "EL", "Electronics", "AP", "Apparel", "Other")
```
Extract meaningful portions of codes (prefixes, suffixes) before passing to SWITCH for category mapping.

---

**[[UPPER]]/[[LOWER]]/[[TRIM]]** - Normalize text before SWITCH

*Ensure consistent matching by normalizing input:*
```
=SWITCH(UPPER(TRIM(A1)), "YES", TRUE, "NO", FALSE, "INVALID")
```
TRIM removes leading/trailing spaces; UPPER/LOWER ensures consistent case. While SWITCH is case-insensitive, data might have unexpected variations.

---

**[[TEXT]]** - Format results from SWITCH

*Format SWITCH output for display:*
```
=TEXT(SWITCH(Grade, "A", 4.0, "B", 3.0, "C", 2.0, "F", 0.0), "0.00")
```
When SWITCH returns numbers that need formatting, wrap the SWITCH in TEXT for consistent display.

---

**[[IFERROR]]** - Handle unmatched cases (alternative to default)

*Wrap SWITCH when additional error handling is needed:*
```
=IFERROR(SWITCH(A1, "X", Value1, "Y", Value2), "Unknown")
```
While SWITCH has a built-in default, IFERROR can catch errors from the result expressions themselves, not just unmatched values.

---

**[[CONCATENATE]] or &** - Build outputs combining SWITCH with text

*Create descriptive strings using SWITCH results:*
```
="Customer Type: " & SWITCH(CustCode, "R", "Retail", "W", "Wholesale", "D", "Distributor", "Unknown")
```
Combine SWITCH translations with other text to create meaningful labels and messages.

---

**[[WEEKDAY]]/[[MONTH]]/[[YEAR]]** - Extract date components for SWITCH

*Map date components to text:*
```
=SWITCH(WEEKDAY(A1,2), 1,"Monday", 2,"Tuesday", 3,"Wednesday", 4,"Thursday", 5,"Friday", 6,"Saturday", 7,"Sunday")
```
Date functions return numbers that SWITCH can map to names, descriptions, or other values.

---

**[[MATCH]]** - Alternative approach for many values

*For large mappings, consider MATCH with a results array:*
```
Using SWITCH (manageable for <15 values):
=SWITCH(A1, "A", 1, "B", 2, ..., "Z", 26, 0)

Using MATCH+INDEX (better for many values):
=INDEX({1,2,3,...,26}, MATCH(A1, {"A","B","C",...,"Z"}, 0))
```
MATCH with array constants can be more maintainable than SWITCH for large value sets.

## Official Documentation

- **Microsoft Excel:** [SWITCH function](https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e)
- **Google Sheets:** [SWITCH function](https://support.google.com/docs/answer/7014528)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 2016 | 2016 | Initial release alongside IFS as part of new logical functions |
| Excel 2019 | 2019 | Continued support, no changes |
| Excel 365 | 2016+ | Full support with dynamic array improvements |
| Excel Online | 2016+ | Full support in web version |
| Excel for Mac | 2016+ | Full support in Mac version |
| Google Sheets | ~2014 | Supported since early Sheets development |
| Google Sheets | 2018 | Performance improvements for large datasets |
| LibreOffice Calc | 5.2 (2016) | Added for Excel 2016 compatibility |
| Apple Numbers | Not supported | Use nested IF or CHOOSE instead |

### Comparison: SWITCH vs IFS

| Aspect | SWITCH | IFS |
|--------|--------|-----|
| Comparison type | Exact value matching | Condition evaluation |
| Expression evaluated | Once | Conditions evaluated until TRUE found |
| Best for | Discrete value mapping | Range testing, complex conditions |
| Example use | Code translation | Grade thresholds |
| Syntax | expression, value1, result1, ... | condition1, result1, condition2, ... |
| Programming analogy | switch/case statement | if/else if chain |

---

*Last updated: 2026-01-10*
