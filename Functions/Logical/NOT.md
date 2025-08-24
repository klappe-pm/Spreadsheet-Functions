---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - logical
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# NOT

## NOT Description

Reverses the logical value of its argument, returning TRUE when the argument is FALSE and FALSE when the argument is TRUE. Essential for exclusion logic, negative conditions, and creating opposite boolean results.

> [!f(x)] NOT Syntax
>
> ```spreadsheets
> NOT(logical)
> ```
>
> **Parameters:**
> - `logical` (required): Value or expression that evaluates to TRUE or FALSE

> [!f(x)] NOT Examples
>
> ```spreadsheets
> // Basic logical reversal
> NOT(TRUE) → FALSE, NOT(FALSE) → TRUE
> 
> // Invert comparison results
> NOT(A1>50) → TRUE if A1 is 50 or less, FALSE if A1 is greater than 50
> 
> // Exclude specific values
> NOT(B2="Inactive") → TRUE if B2 is anything except "Inactive"
> 
> // Weekend exclusion logic
> NOT(WEEKDAY(C3,2)>5) → TRUE if C3 is a weekday (Monday-Friday)
> 
> // Empty cell detection (reverse)
> NOT(ISBLANK(D4)) → TRUE if D4 contains data, FALSE if empty
> ```

## Use Cases

### [[Exclusion logic]]
- **Access control**: Grant permissions to users who are NOT in restricted groups or departments
- **Product filtering**: Display items that are NOT discontinued, expired, or out of stock
- **Employee eligibility**: Qualify staff who are NOT in probationary status or under review
- **Quality control**: Process items that are NOT defective, recalled, or flagged for inspection

### [[Negative conditions]]
- **Alert systems**: Trigger warnings when systems are NOT operating normally or within parameters
- **Validation rules**: Flag records that do NOT meet required standards or formatting criteria
- **Business rules**: Apply special handling for customers who are NOT in preferred status tiers
- **Data cleaning**: Identify records that do NOT conform to expected patterns or ranges

### [[Boolean inversion]]
- **Status toggles**: Switch between active/inactive states by inverting current boolean values
- **Permission reversal**: Create opposite permission sets for different user groups or roles
- **Condition simplification**: Simplify complex logical expressions by inverting instead of using multiple comparisons
- **Default behavior**: Implement default actions when conditions are NOT met or satisfied

### [[Data validation]]
- **Input verification**: Ensure entered data does NOT contain invalid characters or formats
- **Range checking**: Validate that values do NOT exceed maximum limits or fall below minimums
- **Completeness validation**: Verify that required fields are NOT empty or missing
- **Consistency checking**: Confirm that related data fields do NOT contradict each other

## Related

### Similar Functions

- [[IF]] - Uses NOT results for conditional logic and decision-making processes
- [[AND]] - Combines with NOT for complex multi-criteria exclusion logic
- [[OR]] - Works with NOT to create sophisticated inclusion/exclusion patterns
- [[ISNOT]] - Excel's newer function for specific data type negation (if available)
- [[XOR]] - Exclusive OR logic, returns TRUE when exactly one condition is true

## Conditional Logic Functions

### [[IF]]
NOT is frequently used within IF statements to create exclusion logic and handle negative conditions elegantly.

```spreadsheets
// Access control with exclusion
=IF(NOT(A2="Restricted"), "Access Granted", "Access Denied")
// Grant access unless status is "Restricted"

// Processing eligibility with multiple exclusions
=IF(NOT(OR(B3="Inactive", C3="Suspended", D3="Terminated")), "Eligible", "Not Eligible")
// Eligible unless inactive, suspended, or terminated

// Working day validation
=IF(NOT(OR(WEEKDAY(E4,2)>5, F4="Holiday")), "Business Day", "Non-Business Day")
// Business day unless weekend or holiday
```

### [[AND]]
Combines with NOT to create sophisticated multi-criteria exclusion logic where multiple negative conditions must be satisfied.

```spreadsheets
// Comprehensive eligibility check
=AND(NOT(G5="Probation"), NOT(H5<18), NOT(I5="Inactive"))
// Eligible if NOT on probation AND NOT under 18 AND NOT inactive

// Quality control verification
=AND(NOT(J6="Defective"), NOT(K6="Recalled"), L6>0)
// Acceptable if NOT defective AND NOT recalled AND quantity positive

// System health monitoring
=AND(NOT(M7>95), NOT(N7<5), NOT(O7="Error"))
// System healthy if CPU NOT >95% AND disk space NOT <5% AND no errors
```

### [[OR]]
Works with NOT to implement flexible exclusion patterns and complex negative condition handling.

```spreadsheets
// Flexible access denial
=OR(NOT(P8="Active"), Q8="Suspended", R8<TODAY()-365)
// Deny if NOT active OR suspended OR account too old

// Product availability exclusions
=NOT(OR(S9="Discontinued", T9="Out of Stock", U9="Recalled"))
// Available if NOT (discontinued OR out of stock OR recalled)

// Employee processing exceptions
=OR(NOT(V10="Regular"), W10="Executive", X10>100000)
// Special processing if NOT regular employee OR executive OR high salary
```

## Data Validation Functions

### [[ISBLANK]], [[ISERROR]], [[ISNA]]
NOT reverses these IS functions to create positive validation conditions and streamlined error handling.

```spreadsheets
// Data completeness validation
=NOT(ISBLANK(Y11)) // TRUE if cell contains data
// Ensure required field is populated

// Error-free calculation verification
=NOT(ISERROR(Z12/AA12)) // TRUE if division is valid
// Confirm calculation will not produce errors

// Successful lookup validation
=NOT(ISNA(VLOOKUP(BB13, Table1, 2, 0))) // TRUE if lookup finds match
// Verify reference data exists
```

### [[ISNUMBER]], [[ISTEXT]], [[ISDATE]]
NOT inverts data type checking functions for comprehensive input validation and data quality assurance.

```spreadsheets
// Non-numeric data detection
=NOT(ISNUMBER(CC14)) // TRUE if cell contains non-numeric data
// Flag text entries in numeric fields

// Text field validation
=NOT(ISTEXT(DD15)) // TRUE if cell contains non-text data
// Identify numeric entries in text fields

// Date format verification
=NOT(ISDATE(EE16)) // TRUE if cell does not contain valid date
// Find invalid date entries
```

## String and Pattern Matching

### [[EXACT]], [[FIND]], [[SEARCH]]
NOT reverses string matching functions for flexible text validation and pattern exclusion logic.

```spreadsheets
// Case-sensitive mismatch detection
=NOT(EXACT(FF17, "EXACT MATCH")) // TRUE if not exactly "EXACT MATCH"
// Identify case or content differences

// Substring absence verification
=NOT(ISNUMBER(FIND("@", GG18))) // TRUE if "@" symbol not found
// Validate email format by checking for missing @ symbol

// Pattern exclusion matching
=NOT(ISNUMBER(SEARCH("test*", HH19))) // TRUE if "test" pattern not found
// Exclude items containing test patterns
```

## Commonly Used With Functions Examples

### NOT with Date Functions
NOT simplifies date range exclusions, business day logic, and temporal validation rules.

```spreadsheets
// Non-weekend day validation
=NOT(WEEKDAY(II20,2)>5) // TRUE for Monday-Friday
// Identify business days for processing

// Future date exclusion
=NOT(JJ21>TODAY()) // TRUE if date is today or earlier
// Process only current or past dates

// Holiday exclusion logic
=IF(NOT(OR(WEEKDAY(KK22,2)>5, LL22="Holiday")), "Process", "Skip")
// Process if NOT (weekend OR holiday)
```

### NOT with Mathematical Functions
NOT creates numerical exclusion conditions and validates ranges through logical inversion.

```spreadsheets
// Range exclusion validation
=NOT(AND(MM23>=10, MM23<=90)) // TRUE if value outside 10-90 range
// Flag values that fall outside acceptable range

// Zero division prevention
=IF(NOT(NN24=0), OO24/NN24, "Cannot divide by zero")
// Perform division only if denominator is NOT zero

// Performance threshold exclusion
=NOT(PP25>AVERAGE($PP$2:$PP$100)) // TRUE if below average performance
// Identify below-average performers
```

### NOT with Text Functions
NOT enables sophisticated text validation, format checking, and content exclusion logic.

```spreadsheets
// Email format validation
=NOT(AND(LEN(QQ26)>5, ISNUMBER(FIND("@", QQ26)), ISNUMBER(FIND(".", QQ26))))
// Invalid if NOT (length >5 AND contains @ AND contains .)

// Required field validation
=NOT(OR(RR27="", ISBLANK(RR27), RR27=" "))
// Valid if NOT (empty OR blank OR space only)

// Phone number format exclusion
=NOT(OR(LEN(SS28)=10, LEN(SS28)=12))
// Invalid format if NOT (10 digits OR 12 characters with formatting)
```

### NOT with Lookup Functions
NOT handles lookup failures gracefully and creates robust data validation with fallback logic.

```spreadsheets
// Reference validation
=IF(NOT(ISERROR(VLOOKUP(TT29, RefTable, 1, 0))), "Valid", "Invalid Reference")
// Valid if lookup does NOT produce error

// Multi-table lookup exclusion
=NOT(OR(ISNA(VLOOKUP(UU30, Table1, 1, 0)), ISNA(VLOOKUP(UU30, Table2, 1, 0))))
// Found if NOT (missing from table1 OR missing from table2)

// Conditional lookup execution
=IF(NOT(VV31=""), VLOOKUP(VV31, PriceList, 2, 0), 0)
// Perform lookup only if search value is NOT empty
```

### NOT with Error Handling Functions
NOT transforms error conditions into positive validation logic for cleaner spreadsheet design.

```spreadsheets
// Clean data validation
=AND(NOT(ISERROR(WW32)), NOT(ISBLANK(XX32)), YY32>0)
// Valid if NOT error AND NOT blank AND positive value

// Comprehensive input checking
=NOT(OR(ISERROR(ZZ33), ISNA(ZZ33), ZZ33=""))
// Valid if NOT (calculation error OR N/A OR empty)

// Formula integrity verification
=IF(NOT(ISERROR(AAA34/BBB34)), "Calculation OK", "Check Input Values")
// Proceed if division does NOT produce error
```
