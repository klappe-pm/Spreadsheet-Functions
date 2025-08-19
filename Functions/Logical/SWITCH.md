---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: logical
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# SWITCH

## SWITCH Description

Compares an expression against multiple values and returns the corresponding result for the first match found. Cleaner alternative to nested IF statements for exact value matching scenarios.

> [!f(x)] SWITCH Syntax
>
> ```spreadsheets
> SWITCH(expression, value1, result1, [value2, result2], ..., [default])
> ```
>
> **Parameters:**
> - `expression` (required): Value to compare against the list
> - `value1, result1` (required): First value-result pair
> - `value2, result2, ...` (optional): Additional value-result pairs (up to 126 pairs)
> - `default` (optional): Value returned if no matches found

> [!f(x)] SWITCH Examples
>
> ```spreadsheets
> // Grade letter assignment
> SWITCH(A1, "A", "Excellent", "B", "Good", "C", "Average", "D", "Poor", "F", "Fail", "Invalid Grade")
> 
> // Department code translation
> SWITCH(B2, "HR", "Human Resources", "IT", "Information Technology", "FN", "Finance", "Unknown")
> 
> // Pricing tier calculation
> SWITCH(C3, "Basic", 100, "Standard", 200, "Premium", 500, 0)
> 
> // Day of week conversion
> SWITCH(WEEKDAY(D4), 1, "Sunday", 2, "Monday", 3, "Tuesday", 4, "Wednesday", 5, "Thursday", 6, "Friday", 7, "Saturday")
> 
> // Status code interpretation
> SWITCH(E5, 200, "Success", 404, "Not Found", 500, "Server Error", "Unknown Status")
> ```

## Use Cases

### [[Value mapping]]
- **Code translation**: Convert abbreviations, codes, or IDs to full descriptions or names
- **Category assignment**: Map input values to standardized categories or classifications
- **Status interpretation**: Translate numeric or coded status values to user-friendly descriptions
- **Reference data lookup**: Replace lookup tables with inline value mapping for small datasets

### [[Conditional calculations]]
- **Tiered pricing**: Apply different rates or prices based on category, region, or customer type
- **Commission structures**: Calculate different commission rates based on product type or sales level
- **Tax calculations**: Apply different tax rates based on location, product category, or customer status
- **Scoring systems**: Assign different point values based on performance levels or achievement categories

### [[Data transformation]]
- **Format standardization**: Convert various input formats to standardized output formats
- **Unit conversion**: Apply different conversion factors based on unit types or measurement systems
- **Localization**: Display different text, formats, or values based on language or region codes
- **Business rule implementation**: Apply different business logic based on account types, user roles, or system states

## Related

### Similar Functions

- [[IFS]] - Tests multiple conditions with ranges, while SWITCH matches exact values
- [[IF]] - Single condition testing, SWITCH replaces nested IF for multiple exact matches
- [[CHOOSE]] - Index-based selection, similar to SWITCH but uses position numbers
- [[VLOOKUP]] - Table-based lookup, alternative to SWITCH for larger datasets
- [[CASE]] - SQL-style conditional logic (where available)

## Commonly Used With Functions Examples

### SWITCH with Mathematical Operations
Applies different calculations, rates, or multipliers based on category or type matching.

```spreadsheets
// Commission rate calculation
=F2 * SWITCH(G2, "Electronics", 0.15, "Clothing", 0.12, "Books", 0.08, "Food", 0.05, 0.1)
// Multiplies sales by category-specific commission rate

// Tax calculation by state
=H3 * SWITCH(I3, "CA", 0.08, "NY", 0.07, "TX", 0.06, "FL", 0.05, 0.04)
// Applies state-specific tax rates

// Shipping cost by method
=SWITCH(J4, "Express", K4*0.2, "Standard", 15, "Economy", 10, 25)
// Different shipping calculations by method
```

### SWITCH with Text Functions
Formats, concatenates, or processes text differently based on matching criteria.

```spreadsheets
// Dynamic greeting by language
=SWITCH(L5, "EN", "Hello " & M5, "ES", "Hola " & M5, "FR", "Bonjour " & M5, "Hi " & M5)
// Creates localized greetings

// Email format by department
=LOWER(N6) & SWITCH(O6, "Sales", "@sales.com", "Support", "@help.com", "HR", "@hr.com", "@company.com")
// Generates department-specific email addresses

// Document title formatting
=SWITCH(P7, "Report", UPPER(Q7), "Memo", PROPER(Q7), "Draft", LOWER(Q7), Q7)
// Applies different text formatting by document type
```

### SWITCH with Date Functions
Applies different date calculations or formats based on type or category matching.

```spreadsheets
// Payment terms by customer type
=R8 + SWITCH(S8, "Net30", 30, "Net15", 15, "COD", 0, "Net45", 45, 30)
// Adds different day periods based on payment terms

// Holiday bonus calculation
=SWITCH(MONTH(T9), 12, U9*1.5, 6, U9*1.2, 3, U9*1.1, U9)
// Applies seasonal multipliers by month

// Workday calculation by urgency
=WORKDAY(V10, SWITCH(W10, "Critical", 1, "High", 3, "Medium", 7, "Low", 14))
// Calculates deadlines based on priority levels
```

### SWITCH with Lookup Functions
Selects different lookup tables or methods based on category or type matching.

```spreadsheets
// Multi-table pricing lookup
=VLOOKUP(X11, SWITCH(Y11, "Retail", RetailTable, "Wholesale", WholesaleTable, "Corporate", CorpTable, DefaultTable), 2, 0)
// Uses different price tables based on customer type

// Dynamic reference selection
=INDEX(SWITCH(Z12, "Sales", SalesData, "Marketing", MktgData, "Finance", FinData, AllData), AA12, BB12)
// Selects data range based on department

// Conditional lookup with SWITCH table selection
=IFERROR(VLOOKUP(CC13, SWITCH(DD13, "A", Table1, "B", Table2, "C", Table3, MainTable), 3, 0), "Not Found")
// Combines SWITCH table selection with error handling
```

### SWITCH with Conditional Functions
Combines exact value matching with conditional logic for sophisticated decision trees.

```spreadsheets
// Nested conditional logic
=IF(EE14>1000, SWITCH(FF14, "Premium", GG14*1.2, "Standard", GG14*1.1, GG14), SWITCH(FF14, "Premium", GG14*0.9, "Standard", GG14*0.95, GG14*0.8))
// Different SWITCH logic based on amount threshold

// Complex eligibility determination
=AND(HH15>18, SWITCH(II15, "US", TRUE, "CA", TRUE, "UK", TRUE, FALSE), JJ15="Active")
// Uses SWITCH within AND for country eligibility checking

// Status-dependent processing
=IFS(KK16="New", "Processing", LL16="Active", SWITCH(MM16, "A", "Priority", "B", "Standard", "C", "Low", "Review"), TRUE, "Hold")
// Combines IFS and SWITCH for complex status logic
```
