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

# IFERROR

## IFERROR Description

Evaluates an expression and returns the result if no error occurs, or returns a specified alternative value if any error is detected. Essential for creating robust spreadsheets that handle calculation failures gracefully without displaying error messages.

> [!f(x)] IFERROR Syntax
>
> ```spreadsheets
> IFERROR(value, value_if_error)
> ```
>
> **Parameters:**
> - `value` (required): Expression or formula to evaluate
> - `value_if_error` (required): Value returned if the first argument produces an error

> [!f(x)] IFERROR Examples
>
> ```spreadsheets
> // Safe division with custom error message
> IFERROR(A1/B1, "Cannot divide") → Result of A1/B1 or "Cannot divide" if B1 is zero
> 
> // Lookup with fallback value
> IFERROR(VLOOKUP(C2, Table1, 2, 0), "Not Found") → Lookup result or "Not Found" if no match
> 
> // Mathematical calculation protection
> IFERROR(SQRT(D3), 0) → Square root of D3 or 0 if D3 is negative
> 
> // Text parsing with error handling
> IFERROR(VALUE(E4), "Invalid Number") → Converts E4 to number or shows error message
> 
> // Complex formula protection
> IFERROR((F5*G5)/(H5+I5), "Calculation Error") → Formula result or error message if issues occur
> ```

## Use Cases

### [[Error handling]]
- **Formula protection**: Prevent #DIV/0!, #VALUE!, #N/A, and other errors from breaking spreadsheet calculations
- **User experience**: Display friendly error messages instead of cryptic error codes for better usability
- **Data validation**: Handle invalid inputs gracefully while maintaining calculation integrity
- **Report cleanup**: Ensure professional-looking reports without error displays that confuse stakeholders

### [[Graceful degradation]]
- **Lookup failures**: Provide meaningful alternatives when VLOOKUP, INDEX/MATCH, or other lookups fail to find data
- **Missing data handling**: Continue calculations even when some input data is unavailable or corrupted
- **Division by zero**: Handle mathematical operations that might encounter zero denominators
- **Data type conversion**: Safely convert text to numbers or dates with appropriate fallback values

### [[Robust calculations]]
- **Financial modeling**: Protect complex financial formulas from input errors that could cascade through models
- **Statistical analysis**: Handle edge cases in statistical calculations where standard functions might fail
- **Dashboard creation**: Ensure dashboard metrics display properly even with incomplete or problematic data
- **Automated reporting**: Build self-healing reports that continue functioning despite data quality issues

### [[Data processing]]
- **Import validation**: Handle errors when importing data from external sources with inconsistent formats
- **Bulk calculations**: Process large datasets while isolating and handling individual calculation failures
- **Cross-system integration**: Manage data inconsistencies when combining information from multiple systems
- **Dynamic formulas**: Create adaptive formulas that adjust behavior based on data availability and quality

## Related

### Similar Functions

- [[IFNA]] - Specifically handles #N/A errors, more targeted than IFERROR
- [[ISERROR]] - Tests for errors but doesn't provide alternative values
- [[IF]] - Conditional logic, can be combined with error testing functions
- [[TRY]] - Modern alternative in some spreadsheet applications
- [[ISBLANK]] - Tests for empty cells, often used with IFERROR for comprehensive validation

## Error Handling Functions

### [[VLOOKUP]] and [[INDEX/MATCH]]
IFERROR is most commonly used with lookup functions to handle cases where no match is found.

```spreadsheets
// Safe VLOOKUP with meaningful fallback
=IFERROR(VLOOKUP(A2, CustomerData, 3, 0), "Customer Not Found")
// Returns customer info or clear message if not found

// INDEX/MATCH with error protection
=IFERROR(INDEX(PriceList, MATCH(B3, ProductCodes, 0)), "Price Unavailable")
// Finds price or shows unavailable message

// Multiple lookup attempt with cascading fallbacks
=IFERROR(VLOOKUP(C4, CurrentPrices, 2, 0), IFERROR(VLOOKUP(C4, ArchivePrices, 2, 0), "No Price Data"))
// Try current prices, then archive prices, then show message
```

### [[Mathematical Operations]]
Protects division, square roots, logarithms, and other operations that can produce mathematical errors.

```spreadsheets
// Safe division operations
=IFERROR(D5/E5, 0)
// Returns division result or 0 if denominator is zero

// Protected percentage calculations
=IFERROR((F6-G6)/G6, "N/A")
// Calculate percentage change with error protection

// Square root with negative number handling
=IFERROR(SQRT(H7), "Invalid Input")
// Returns square root or error message for negative numbers
```

### [[TEXT]] and [[VALUE]] Functions
Handles text-to-number conversion errors and text manipulation failures gracefully.

```spreadsheets
// Safe text to number conversion
=IFERROR(VALUE(I8), 0)
// Converts text to number or returns 0 if conversion fails

// Protected text extraction
=IFERROR(MID(J9, FIND(",", J9)+1, 10), "Format Error")
// Extracts text after comma or shows format error

// Date parsing with error handling
=IFERROR(DATEVALUE(K10), "Invalid Date")
// Converts text to date or shows invalid date message
```

## Commonly Used With Functions Examples

### IFERROR with Conditional Logic
Combines error handling with IF statements for sophisticated decision-making.

```spreadsheets
// Conditional calculation with error protection
=IF(L11>0, IFERROR(M11/L11, "Division Error"), "No Data")
// Performs division only if denominator positive, handles division errors

// Complex business logic with error handling
=IFERROR(IF(N12="Premium", O12*1.2, IF(N12="Standard", O12, O12*0.8)), "Calculation Failed")
// Tiered pricing with comprehensive error protection

// Multi-condition validation with error safety
=IF(AND(NOT(ISBLANK(P13)), ISNUMBER(P13)), IFERROR(P13*1.1, "Math Error"), "Invalid Input")
// Validates input before calculation, handles both validation and math errors
```

### IFERROR with Date Functions
Protects date calculations from invalid dates, missing data, and format issues.

```spreadsheets
// Safe date difference calculation
=IFERROR(Q14-R14, "Date Error")
// Calculates difference or shows error for invalid dates

// Protected age calculation
=IFERROR(DATEDIF(S15, TODAY(), "Y"), "Invalid Birthdate")
// Returns age or error message for problematic dates

// Working day calculation with error handling
=IFERROR(NETWORKDAYS(T16, U16), "Invalid Date Range")
// Counts business days or shows error for invalid range
```

### IFERROR with Array Functions
Handles errors in array formulas and dynamic array operations.

```spreadsheets
// Protected array summation
=IFERROR(SUMPRODUCT(V17:V20, W17:W20), "Array Error")
// Multiplies arrays and sums or shows error for mismatched ranges

// Safe array lookup
=IFERROR(INDEX(X17:X100, MATCH(1, (Y17:Y100=Z21)*(AA17:AA100>BB21), 0)), "No Match")
// Complex array lookup with error protection

// Dynamic range calculation with error handling
=IFERROR(AVERAGE(INDIRECT(CC22&":"&DD22)), "Range Error")
// Uses dynamic range with error protection for invalid references
```

### IFERROR with Statistical Functions
Protects statistical calculations from insufficient data, invalid ranges, and edge cases.

```spreadsheets
// Safe statistical calculation
=IFERROR(STDEV(EE23:EE30), "Insufficient Data")
// Calculates standard deviation or shows message for insufficient data

// Protected percentile calculation
=IFERROR(PERCENTILE(FF24:FF50, 0.9), "Calculation Error")
// Returns 90th percentile or error message

// Robust correlation analysis
=IFERROR(CORREL(GG25:GG35, HH25:HH35), "Cannot Calculate Correlation")
// Calculates correlation or shows error for incompatible data
```

### IFERROR with Text Processing
Handles text manipulation errors, search failures, and format inconsistencies.

```spreadsheets
// Safe text extraction
=IFERROR(RIGHT(II26, LEN(II26)-FIND("@", II26)), "Invalid Email")
// Extracts domain from email or shows error for invalid format

// Protected string replacement
=IFERROR(SUBSTITUTE(JJ27, "old", "new"), "Substitution Failed")
// Replaces text or shows error message

// Robust text parsing
=IFERROR(TRIM(MID(KK28, FIND(",", KK28)+1, FIND(",", KK28, FIND(",", KK28)+1)-FIND(",", KK28)-1)), "Parse Error")
// Extracts middle value from CSV or shows parse error
```
