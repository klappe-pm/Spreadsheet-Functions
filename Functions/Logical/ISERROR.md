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

# ISERROR

## ISERROR Description

Tests whether a value is any type of error (#N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, #NULL!) and returns TRUE if an error is detected, FALSE otherwise. Essential for error detection in data validation and quality control processes.

> [!f(x)] ISERROR Syntax
>
> ```spreadsheets
> ISERROR(value)
> ```
>
> **Parameters:**
> - `value` (required): Value or expression to test for errors

> [!f(x)] ISERROR Examples
>
> ```spreadsheets
> // Test calculation for any error
> ISERROR(A1/B1) → TRUE if division by zero or other math error, FALSE if valid result
> 
> // Check lookup function for errors
> ISERROR(VLOOKUP(C2, Table1, 2, 0)) → TRUE if lookup fails with any error
> 
> // Validate text conversion
> ISERROR(VALUE(D3)) → TRUE if D3 cannot be converted to number
> 
> // Test array formula for errors
> ISERROR(INDEX(E4:E10, F4)) → TRUE if index position is invalid
> 
> // Check date calculation
> ISERROR(DATE(G5, H5, I5)) → TRUE if invalid date components provided
> ```

## Use Cases

### [[Error detection]]
- **Data quality validation**: Identify cells containing calculation errors before processing or reporting
- **Formula auditing**: Systematically check complex workbooks for any formula failures or inconsistencies
- **Import validation**: Verify that data imported from external sources doesn't contain error values
- **Bulk error checking**: Scan entire ranges to find and flag any cells with error conditions

### [[Conditional processing]]
- **Error-based branching**: Create different processing paths based on whether calculations produce errors
- **Data cleaning workflows**: Skip or handle rows containing errors differently in data processing pipelines
- **Report filtering**: Exclude records with errors from summary reports and analytics
- **Alert systems**: Trigger notifications when error counts exceed acceptable thresholds

### [[Quality control]]
- **Dashboard health monitoring**: Ensure dashboard calculations are error-free before presentation
- **Model validation**: Verify financial or analytical models don't contain hidden calculation errors
- **Automated testing**: Build test suites that verify formulas work correctly across different scenarios
- **Production monitoring**: Continuously check operational spreadsheets for emerging error conditions

## Related

### Similar Functions

- [[ISERR]] - Tests for errors except #N/A, more specific than ISERROR
- [[ISNA]] - Tests specifically for #N/A errors only
- [[IFERROR]] - Tests for errors and provides alternative values
- [[IFNA]] - Tests for #N/A errors and provides alternatives
- [[ERROR.TYPE]] - Returns specific error type numbers for classification

## Error Testing Functions

### [[IF]] with ISERROR
The most common combination, using error detection to control formula behavior and provide user-friendly alternatives.

```spreadsheets
// Safe division with error checking
=IF(ISERROR(A2/B2), "Cannot calculate", A2/B2)
// Performs division or shows message if error occurs

// Lookup with error handling
=IF(ISERROR(VLOOKUP(C3, Table1, 2, 0)), "Not found", VLOOKUP(C3, Table1, 2, 0))
// Returns lookup result or friendly message

// Complex calculation protection
=IF(ISERROR(SQRT(D4)*LOG(E4)), "Invalid inputs", SQRT(D4)*LOG(E4))
// Protects against negative square roots or invalid logarithms
```

### [[SUMPRODUCT]] and [[COUNTIF]] with Error Detection
Uses ISERROR in array operations for sophisticated error analysis across ranges.

```spreadsheets
// Count errors in range
=SUMPRODUCT(--ISERROR(F2:F20))
// Counts how many cells in range contain errors

// Conditional operations excluding errors
=SUMPRODUCT((NOT(ISERROR(G2:G20)))*(G2:G20))
// Sums only non-error values in range

// Error percentage calculation
=SUMPRODUCT(--ISERROR(H2:H100))/COUNT(H2:H100)*100
// Calculates percentage of cells with errors
```

## Commonly Used With Functions Examples

### ISERROR with Mathematical Functions
Protects mathematical operations and provides error-aware calculations.

```spreadsheets
// Safe percentage calculation
=IF(ISERROR((I5-J5)/J5), "Cannot calculate change", (I5-J5)/J5)
// Calculates percentage change with division error protection

// Compound interest with error checking
=IF(OR(ISERROR(K6), K6<=0, L6<=0), "Invalid inputs", K6*(1+L6)^M6)
// Validates inputs before compound interest calculation

// Statistical calculation protection
=IF(ISERROR(STDEV(N7:N20)), "Insufficient data", STDEV(N7:N20))
// Calculates standard deviation with error handling
```

### ISERROR with Lookup Functions
Provides comprehensive error checking for all types of lookup operations.

```spreadsheets
// Multi-table lookup with error detection
=IF(ISERROR(VLOOKUP(O8, Table1, 2, 0)), IF(ISERROR(VLOOKUP(O8, Table2, 2, 0)), "Not found anywhere", VLOOKUP(O8, Table2, 2, 0)), VLOOKUP(O8, Table1, 2, 0))
// Tries primary table, then secondary, handles all errors

// INDEX/MATCH with comprehensive error checking
=IF(ISERROR(INDEX(P9:P50, MATCH(Q9, R9:R50, 0))), "Lookup failed", INDEX(P9:P50, MATCH(Q9, R9:R50, 0)))
// Handles both MATCH failures and INDEX out-of-range errors

// Dynamic reference with error protection
=IF(ISERROR(INDIRECT(S10&"!A1")), "Invalid sheet reference", INDIRECT(S10&"!A1"))
// Tests dynamic sheet references for validity
```

### ISERROR with Text Functions
Handles text processing errors and format validation comprehensively.

```spreadsheets
// Safe text extraction
=IF(ISERROR(MID(T11, FIND("@", T11)+1, 10)), "Invalid format", MID(T11, FIND("@", T11)+1, 10))
// Extracts text after @ symbol with error protection

// Number format validation
=IF(ISERROR(VALUE(U12)), "Not a number", VALUE(U12))
// Converts text to number with format error checking

// Date parsing with error detection
=IF(ISERROR(DATEVALUE(V13)), "Invalid date format", DATEVALUE(V13))
// Parses date text with comprehensive error handling
```

### ISERROR with Array and Advanced Functions
Provides error detection for complex array operations and modern spreadsheet functions.

```spreadsheets
// Array formula error checking
=IF(ISERROR(SUMPRODUCT((W14:W20>X14)*(Y14:Y20))), "Array calculation failed", SUMPRODUCT((W14:W20>X14)*(Y14:Y20)))
// Protects complex array calculations

// FILTER function with error handling
=IF(ISERROR(FILTER(Z15:Z25, AA15:AA25>BB15)), "No matching records", FILTER(Z15:Z25, AA15:AA25>BB15))
// Handles empty filter results and other errors

// Dynamic range with error protection
=IF(ISERROR(AVERAGE(INDIRECT(CC16&":"&DD16))), "Invalid range", AVERAGE(INDIRECT(CC16&":"&DD16)))
// Validates dynamic range references before calculation
```
