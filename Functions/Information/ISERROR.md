---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - information
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# ISERROR

## ISERROR Description

Returns TRUE if a cell contains any type of error value (#DIV/0!, #N/A, #NAME?, #NULL!, #NUM!, #REF!, #VALUE!), and FALSE for all other values including numbers, text, blanks, and logical values. Essential for error detection and data quality validation in spreadsheets.

> [!f(x)] ISERROR Syntax
>
> ```spreadsheets
> ISERROR(value)
> ISERROR(cell_reference)
> ```
>
> **Parameters:**
> - `value` (required): The cell reference or value to test for error conditions

> [!f(x)] ISERROR Examples
>
> ```spreadsheets
> // Test division by zero error
> ISERROR(1/0) → TRUE (#DIV/0! error)
> 
> // Test lookup error
> ISERROR(VLOOKUP("X", A1:B10, 2, FALSE)) → TRUE (if "X" not found)
> 
> // Test valid calculation
> ISERROR(10*2) → FALSE (valid result)
> 
> // Test invalid function name
> ISERROR(INVALIDFUNC(A1)) → TRUE (#NAME? error)
> 
> // Test text conversion error
> ISERROR(VALUE("abc")) → TRUE (#VALUE! error)
> ```

## Use Cases

### [[Error handling]]
- **Formula error prevention**: Identify calculation errors before they propagate through dependent formulas and reports
- **Data quality assurance**: Detect and flag invalid data entries that cause formula errors during processing
- **Robust calculation design**: Build formulas that gracefully handle error conditions and provide meaningful alternatives
- **User interface improvement**: Replace error displays with user-friendly messages and guidance

### [[Data validation]]
- **Import data verification**: Validate that imported data doesn't contain errors that could break downstream calculations
- **Real-time validation**: Check formula results as users enter data to provide immediate feedback on errors
- **Batch processing quality control**: Identify problematic records in large datasets before running bulk operations
- **Template validation**: Ensure spreadsheet templates function correctly before distribution to users

### [[Report generation]]
- **Clean report output**: Remove or replace error values in reports to maintain professional appearance and clarity
- **Data completeness tracking**: Monitor error rates across datasets to identify data quality issues requiring attention
- **Conditional reporting**: Generate different report sections based on whether calculations completed successfully
- **Error logging and tracking**: Document and track error occurrences for troubleshooting and process improvement

## Related

### Similar Functions

- [[ISNA]] - Tests specifically for #N/A errors, more targeted than ISERROR for lookup function validation
- [[ERROR.TYPE]] - Returns numeric codes identifying specific error types, providing more detailed error information
- [[IFERROR]] - Combines error checking with replacement values, offering more efficient error handling than IF+ISERROR
- [[ISBLANK]] - Checks for empty cells, used with ISERROR to distinguish between missing data and calculation errors
- [[TYPE]] - Returns data type codes, complementing ISERROR for comprehensive data type and error analysis

## Error Handling Functions

### [[IF]]
ISERROR combined with IF provides comprehensive error handling, enabling custom responses to error conditions and maintaining formula functionality.

```spreadsheets
// Basic error replacement
=IF(ISERROR(A2/B2), "Cannot calculate", A2/B2)
// Shows calculation result or friendly message if division error

// Conditional error handling
=IF(ISERROR(VLOOKUP(C3, Table1, 2, FALSE)), "Not found", VLOOKUP(C3, Table1, 2, FALSE))
// Handles lookup errors with custom message

// Error-resistant calculations
=IF(ISERROR(D4*E4), 0, D4*E4)
// Uses zero when multiplication produces error
```

### [[IFERROR]]
ISERROR logic is built into IFERROR function, providing more efficient error handling with cleaner syntax for common error replacement scenarios.

```spreadsheets
// IFERROR equivalent to IF(ISERROR())
=IFERROR(F5/G5, "Division error")
// More concise than IF(ISERROR(F5/G5), "Division error", F5/G5)

// Nested error handling comparison
=IFERROR(IFERROR(H6/I6, H6), "No valid data")
// Handles multiple potential error sources efficiently

// Complex error handling with ISERROR verification
=IF(ISERROR(J7), "Error detected", IFERROR(J7*2, "Calculation failed"))
// Uses ISERROR to detect errors before attempting further calculations
```

## Mathematical Functions

### [[SUM]]
ISERROR helps create error-resistant SUM formulas and validates individual cell values before including them in mathematical aggregations.

```spreadsheets
// Error-resistant sum with validation
=IF(SUMPRODUCT(--(ISERROR(K2:K10)))=0, SUM(K2:K10), "Errors in data")
// Only sums if no errors are present in range

// Sum excluding error values
=SUMPRODUCT((NOT(ISERROR(L2:L20)))*(L2:L20))
// Sums only non-error values in range

// Quality-controlled aggregation
=IF(SUMPRODUCT(--(ISERROR(M2:M15)))/COUNT(M2:M15)<0.1, 
   SUM(M2:M15), 
   "Too many errors for reliable sum")
// Only calculates sum if error rate is below 10%
```

### [[AVERAGE]]
Works with ISERROR to create robust averaging calculations that exclude or account for error values in datasets, ensuring statistical accuracy.

```spreadsheets
// Average excluding errors
=IF(SUMPRODUCT(--(NOT(ISERROR(N2:N25))))>0,
   SUMPRODUCT((NOT(ISERROR(N2:N25)))*(N2:N25))/SUMPRODUCT(--(NOT(ISERROR(N2:N25)))),
   "No valid data for average")
// Calculates average of only non-error values

// Quality threshold averaging
=IF(SUMPRODUCT(--(ISERROR(O2:O30)))<5, 
   AVERAGE(O2:O30), 
   "Too many errors for reliable average")
// Only averages if fewer than 5 errors in dataset

// Error rate reporting with average
="Valid average: " & IFERROR(AVERAGE(P2:P20), "Cannot calculate") & 
 " | Error rate: " & SUMPRODUCT(--(ISERROR(P2:P20)))/COUNTA(P2:P20)*100 & "%"
// Reports both average and error percentage
```

## Lookup Functions

### [[VLOOKUP]]
ISERROR validates VLOOKUP results and enables graceful handling of lookup failures, improving user experience and data integrity.

```spreadsheets
// Safe lookup with error handling
=IF(ISERROR(VLOOKUP(Q21, Table2, 2, FALSE)), 
   "Product not found", 
   VLOOKUP(Q21, Table2, 2, FALSE))
// Provides user-friendly message for failed lookups

// Conditional lookup processing
=IF(ISERROR(VLOOKUP(R22, Table3, 3, FALSE)), 
   "Please check product code", 
   "Price: $" & VLOOKUP(R22, Table3, 3, FALSE))
// Formats successful lookups and handles failures

// Multiple lookup validation
=IF(AND(NOT(ISERROR(VLOOKUP(S23, Table4, 2, FALSE))), 
        NOT(ISERROR(VLOOKUP(S23, Table4, 3, FALSE)))), 
   VLOOKUP(S23, Table4, 2, FALSE) & " - " & VLOOKUP(S23, Table4, 3, FALSE), 
   "Incomplete data")
// Only proceeds if all required lookups succeed
```

### [[MATCH]]
Combines with ISERROR to validate search operations and handle cases where search criteria don't exist in lookup ranges.

```spreadsheets
// Position finding with error handling
=IF(ISERROR(MATCH(T24, U2:U50, 0)), 
   "Item not found in list", 
   "Found at position " & MATCH(T24, U2:U50, 0))
// Reports position or failure message

// Conditional processing based on match success
=IF(ISERROR(MATCH(V25, W2:W100, 0)), 
   "Add to list", 
   "Item already exists")
// Different actions for found vs not found items

// Dynamic range validation
=IF(ISERROR(MATCH(X26, Y2:Y200, 0)), 
   "Expand search range", 
   INDEX(Z2:Z200, MATCH(X26, Y2:Y200, 0)))
// Suggests action when match fails
```

## Commonly Used With Functions Examples

### Data Quality Assessment
```spreadsheets
// Comprehensive data quality report
="Total cells: " & COUNTA(AA2:AA100) & 
 " | Errors: " & SUMPRODUCT(--(ISERROR(AA2:AA100))) &
 " | Error rate: " & ROUND(SUMPRODUCT(--(ISERROR(AA2:AA100)))/COUNTA(AA2:AA100)*100,1) & "%" &
 " | Valid data: " & (COUNTA(AA2:AA100)-SUMPRODUCT(--(ISERROR(AA2:AA100))))
// Complete data quality summary with error statistics

// Quality threshold validation
=IF(SUMPRODUCT(--(ISERROR(BB2:BB50)))/COUNTA(BB2:BB50)<0.05,
   "Data quality: GOOD (Error rate < 5%)",
   "Data quality: POOR (Error rate ≥ 5%) - Review required")
// Categorizes data quality based on error threshold
```

### Financial Calculation Error Prevention
```spreadsheets
// Safe financial calculations with validation
=IF(OR(ISERROR(CC27), ISERROR(DD27), CC27<=0, DD27<=0),
   "Invalid price or quantity data",
   TEXT(CC27*DD27, "$#,##0.00") & " total")
// Validates inputs before financial calculations

// Portfolio calculation with error handling
=IF(SUMPRODUCT(--(ISERROR(EE2:EE20)))=0,
   "Portfolio value: " & TEXT(SUM(EE2:EE20), "$#,##0.00"),
   "Portfolio contains " & SUMPRODUCT(--(ISERROR(EE2:EE20))) & " invalid positions")
// Reports portfolio value or error count
```

### Automated Error Reporting
```spreadsheets
// Error location reporting
=IF(SUMPRODUCT(--(ISERROR(FF2:FF30)))>0,
   "Errors found in cells: " & 
   TEXTJOIN(", ", TRUE, IF(ISERROR(FF2:FF30), "FF"&ROW(FF2:FF30), "")),
   "No errors detected")
// Lists specific cells containing errors for troubleshooting

// Multi-column error analysis
="Column A errors: " & SUMPRODUCT(--(ISERROR(GG2:GG25))) &
 " | Column B errors: " & SUMPRODUCT(--(ISERROR(HH2:HH25))) &
 " | Total error rate: " & 
 ROUND((SUMPRODUCT(--(ISERROR(GG2:GG25)))+SUMPRODUCT(--(ISERROR(HH2:HH25))))/(2*24)*100,1) & "%"
// Analyzes error distribution across multiple data columns
```