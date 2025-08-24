---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - sheets
  - - topics
    - - google-specific
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
# ARRAYFORMULA

## ARRAYFORMULA Description

Enables array formulas in Google Sheets by applying a single formula to an entire range, automatically expanding results across rows and columns. Transforms non-array functions into array-capable functions, eliminating the need to copy formulas manually and enabling dynamic calculations across variable-sized datasets.

> [!f(x)] ARRAYFORMULA Syntax
>
> ```spreadsheets
> ARRAYFORMULA(array_formula)
> ```
>
> **Parameters:**
> - `array_formula` (required): The formula to apply to a range or array, which will automatically expand to match the size of the input data

> [!f(x)] ARRAYFORMULA Examples
>
> ```spreadsheets
> // Basic array calculation
> ARRAYFORMULA(A2:A10 * B2:B10) → multiplies corresponding values in two ranges
> 
> // Array IF statement
> ARRAYFORMULA(IF(C2:C100>0, C2:C100, 0)) → replaces negative values with 0
> 
> // Text manipulation across range
> ARRAYFORMULA(UPPER(D2:D50)) → converts entire range to uppercase
> 
> // Complex array formula with multiple conditions
> ARRAYFORMULA(IF(E2:E100<>"", E2:E100*F2:F100, "")) → multiply only non-empty cells
> 
> // Dynamic array with ROW function
> ARRAYFORMULA(IF(ROW(A2:A1000)<=COUNT(B:B)+1, INDEX(B:B, ROW(A2:A1000)), "")) → creates dynamic expanding list
> ```

## Use Cases

### [[Data processing]]
- **Bulk data transformation**: Apply text functions like UPPER, LOWER, or TRIM to thousands of cells simultaneously without copying formulas
- **Dynamic calculations**: Create formulas that automatically expand when new data is added, perfect for growing datasets and reports
- **Conditional formatting data**: Use ARRAYFORMULA with IF to create conditional calculations across entire columns based on criteria
- **Data cleaning operations**: Remove duplicates, standardize formats, and validate data integrity across large ranges efficiently

### [[Performance optimization]]  
- **Reduced file size**: Single ARRAYFORMULA replaces hundreds of individual formulas, significantly reducing file size and complexity
- **Faster calculations**: Array processing is more efficient than individual cell calculations, especially for large datasets over 1000 rows
- **Memory efficiency**: Reduces memory usage by consolidating multiple formulas into single array operations
- **Improved collaboration**: Fewer formulas mean less conflict when multiple users edit the same spreadsheet simultaneously

### [[Dynamic reporting]]
- **Auto-expanding reports**: Create reports that grow automatically as new data is added, without manual formula copying
- **Cross-sheet references**: Use ARRAYFORMULA with IMPORTRANGE to create dynamic connections between multiple spreadsheets
- **Dashboard calculations**: Build dynamic dashboards where all calculations update automatically when source data changes
- **Template creation**: Design reusable templates that work with variable amounts of data without manual adjustment

## Related

### Similar Functions

- [[MAP]] - Applies a formula to each element in arrays, newer alternative to ARRAYFORMULA for complex transformations
- [[MAKEARRAY]] - Creates arrays with custom functions, complementary to ARRAYFORMULA for array generation  
- [[BYROW]] - Applies functions row-by-row, alternative approach to ARRAYFORMULA for row-wise operations
- [[BYCOL]] - Applies functions column-by-column, alternative approach to ARRAYFORMULA for column-wise operations
- [[LET]] - Defines variables in array formulas, can be combined with ARRAYFORMULA for complex calculations

## Array Processing Functions

### [[IF]]
Most commonly used with ARRAYFORMULA for conditional array operations. Enables complex logical tests across entire ranges with automatic expansion for dynamic filtering and data transformation.

```spreadsheets
// Conditional calculations across arrays
=ARRAYFORMULA(IF(A2:A100<>"", B2:B100*C2:C100, ""))
// Only multiplies non-empty rows, leaves empty cells blank

// Multi-condition array logic
=ARRAYFORMULA(IF(D2:D1000="", "", IF(E2:E1000>1000, "High", "Low")))
// Creates tiered categories only for rows with data

// Array-based data validation
=ARRAYFORMULA(IF(ISNUMBER(F2:F500), F2:F500, "Invalid"))
// Validates numeric data across entire range
```

### [[SUM]]  
Frequently paired with ARRAYFORMULA for dynamic aggregations and running totals. Creates powerful array-based summations that automatically adjust to data size changes.

```spreadsheets
// Running total with ARRAYFORMULA
=ARRAYFORMULA(IF(A2:A1000="", "", SUM(INDIRECT("B2:B"&ROW(A2:A1000)))))
// Creates running sum that expands automatically

// Conditional sum arrays
=ARRAYFORMULA(IF(C2:C500<>"", SUMIF($D$2:$D$500, D2:D500, $E$2:$E$500), ""))
// Dynamic SUMIF across multiple rows

// Group totals with array processing
=ARRAYFORMULA(IF(F2:F200="", "", SUMIFS($G$2:$G$1000, $F$2:$F$1000, F2:F200)))
// Creates category totals for each row
```

## Text Processing Functions

### [[CONCATENATE]]
Combined with ARRAYFORMULA for bulk text operations across ranges. Essential for creating dynamic text combinations, formatted strings, and data merging operations.

```spreadsheets
// Bulk text concatenation
=ARRAYFORMULA(IF(A2:A100<>"", CONCATENATE(A2:A100, " - ", B2:B100), ""))
// Combines two columns with separator

// Dynamic text formatting
=ARRAYFORMULA(IF(C2:C500="", "", "Order #" & C2:C500 & " - " & TEXT(D2:D500, "mm/dd/yyyy")))
// Creates formatted order strings with dates

// Multi-column text merging
=ARRAYFORMULA(IF(E2:E300<>"", E2:E300&" "&F2:F300&" "&G2:G300&" "&H2:H300, ""))
// Combines multiple columns into full names/addresses
```

### [[SPLIT]]
Works with ARRAYFORMULA to process delimited text across entire columns. Enables bulk parsing of CSV data, names, addresses, and other structured text formats.

```spreadsheets
// Array text splitting
=ARRAYFORMULA(IF(A2:A200="", "", SPLIT(A2:A200, ",")))
// Splits comma-delimited text across entire range

// Dynamic name parsing
=ARRAYFORMULA(IF(B2:B150<>"", INDEX(SPLIT(B2:B150, " "), 0, 1), ""))
// Extracts first names from full names

// Structured data extraction
=ARRAYFORMULA(IF(C2:C400="", "", SPLIT(C2:C400, " | ", TRUE, TRUE)))
// Parses pipe-delimited data with empty handling
```

## Lookup Functions

### [[INDEX]]
Essential companion to ARRAYFORMULA for dynamic lookups and array navigation. Creates powerful array-based lookup systems that automatically expand with data growth.

```spreadsheets
// Dynamic array lookup
=ARRAYFORMULA(IF(A2:A100="", "", INDEX($E$2:$E$500, MATCH(A2:A100, $D$2:$D$500, 0))))
// Performs VLOOKUP equivalent across arrays

// Multi-column array extraction
=ARRAYFORMULA(IF(B2:B200<>"", INDEX($F$2:$H$1000, MATCH(B2:B200, $F$2:$F$1000, 0), {2;3}), ""))
// Extracts multiple columns based on lookup values

// Dynamic data validation lookup
=ARRAYFORMULA(IF(C2:C300="", "", IF(ISERROR(MATCH(C2:C300, $ValidList, 0)), "Invalid", C2:C300)))
// Validates data against lookup list
```

### [[MATCH]]
Powers array-based lookups when combined with ARRAYFORMULA and INDEX. Essential for creating dynamic position finding and data validation across large datasets.

```spreadsheets
// Array position finding
=ARRAYFORMULA(IF(A2:A100<>"", MATCH(A2:A100, $Reference$2:$Reference$1000, 0), ""))
// Finds positions of values in reference list

// Dynamic ranking system
=ARRAYFORMULA(IF(B2:B200="", "", MATCH(B2:B200, SORT(B2:B200, 1, FALSE), 0)))
// Creates ranking based on sorted values

// Data validation with position
=ARRAYFORMULA(IF(C2:C150<>"", IF(ISNUMBER(MATCH(C2:C150, $Categories, 0)), "Valid", "Check"), ""))
// Validates against predefined categories
```

## Commonly Used With Functions Examples

### Dynamic Data Processing Pipeline
```spreadsheets
// Complete data processing chain
=ARRAYFORMULA(IF(A2:A1000="", "", 
    UPPER(TRIM(A2:A1000)) & " | " & 
    TEXT(B2:B1000, "mm/dd/yyyy") & " | " & 
    IF(C2:C1000>1000, "Priority", "Standard")
))
// Cleans text, formats dates, adds priority flags in single formula
```

### Advanced Conditional Calculations
```spreadsheets
// Multi-tier commission calculation
=ARRAYFORMULA(IF(D2:D500="", "", 
    IF(E2:E500>=10000, E2:E500*0.15,
    IF(E2:E500>=5000, E2:E500*0.10, 
    IF(E2:E500>=1000, E2:E500*0.05, 0)))
))
// Applies tiered commission rates based on sales amounts
```

### Dynamic Report Generation
```spreadsheets
// Auto-expanding monthly summary
=ARRAYFORMULA(IF(MONTH(A2:A2000)=MONTH(TODAY()), 
    SUMIFS($B$2:$B$2000, $A$2:$A$2000, ">="&EOMONTH(TODAY(),-1)+1, 
           $A$2:$A$2000, "<="&EOMONTH(TODAY(),0), 
           $C$2:$C$2000, C2:C2000), 
    ""
))
// Creates current month totals by category automatically
```

### Cross-Sheet Data Integration
```spreadsheets
// Dynamic multi-sheet lookup
=ARRAYFORMULA(IF(A2:A100<>"", 
    IFERROR(INDEX(IMPORTRANGE("sheet-id", "Data!B:C"), 
                  MATCH(A2:A100, IMPORTRANGE("sheet-id", "Data!A:A"), 0), 2), 
            "Not Found"), 
    ""
))
// Performs lookups across external spreadsheets with error handling
```

### Performance-Optimized Array Operations
```spreadsheets
// Efficient large dataset processing
=ARRAYFORMULA(IF(ROW(A2:A)<=COUNTA(ImportedData!A:A), 
    IF(INDEX(ImportedData!A:A, ROW(A2:A))<>"", 
       INDEX(ImportedData!B:B, ROW(A2:A)) * 
       INDEX(ImportedData!C:C, ROW(A2:A)), 
       ""), 
    ""
))
// Processes imported data efficiently with automatic size adjustment
```
