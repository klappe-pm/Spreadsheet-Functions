---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: information
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# TYPE

## TYPE Description

Returns a numeric code indicating the data type of a value: 1 for number, 2 for text, 4 for logical (TRUE/FALSE), 16 for error values, and 64 for arrays. Essential for detailed data type analysis and conditional processing based on specific value types.

> [!f(x)] TYPE Syntax
>
> ```spreadsheets
> TYPE(value)
> TYPE(cell_reference)
> ```
>
> **Parameters:**
> - `value` (required): The cell reference or value to analyze for data type identification

> [!f(x)] TYPE Examples
>
> ```spreadsheets
> // Test number value
> TYPE(42) → 1 (number)
> 
> // Test text value
> TYPE("Hello") → 2 (text)
> 
> // Test logical value
> TYPE(TRUE) → 4 (logical/boolean)
> 
> // Test error value
> TYPE(1/0) → 16 (error - #DIV/0!)
> 
> // Test array reference
> TYPE(A1:A5) → 64 (array range)
> ```

## Use Cases

### [[Data type analysis]]
- **Mixed data identification**: Categorize data types in imported datasets to apply appropriate processing and validation rules
- **Data structure analysis**: Understand data composition in complex datasets to design optimal processing workflows
- **Quality control assessment**: Identify unexpected data types that may indicate import errors or data corruption
- **Template validation**: Ensure data entry templates receive expected data types in designated fields

### [[Conditional processing]]
- **Type-specific operations**: Route different data types to appropriate processing functions and formatting routines
- **Dynamic formula behavior**: Modify formula behavior based on input data types to handle diverse data sources
- **Error prevention**: Prevent type-related errors by validating data types before mathematical or text operations
- **Multi-format handling**: Process files with mixed data types by applying type-appropriate transformations

### [[Data conversion workflows]]
- **Import data standardization**: Convert various data types to standardized formats for consistent downstream processing
- **Database preparation**: Ensure data types match database field requirements before import operations
- **Report formatting**: Apply different formatting rules based on whether values are numbers, text, or other types
- **API data processing**: Validate and convert API response data types to match application requirements

## Related

### Similar Functions

- [[ISNUMBER]] - Returns TRUE/FALSE for numbers, simpler than TYPE for basic numeric validation
- [[ISTEXT]] - Returns TRUE/FALSE for text, more straightforward than TYPE for text identification
- [[ISBLANK]] - Returns TRUE/FALSE for empty cells, complementing TYPE for complete data analysis
- [[ISERROR]] - Returns TRUE/FALSE for errors, alternative to TYPE=16 for error detection
- [[CELL]] - Returns detailed information about cell formatting and properties beyond data type

## Data Type Classification Functions

### [[IF]]
TYPE combined with IF enables sophisticated data type routing and conditional processing based on specific numeric type codes.

```spreadsheets
// Data type routing
=IF(TYPE(A2)=1, "Number: " & A2, 
   IF(TYPE(A2)=2, "Text: " & A2, 
      IF(TYPE(A2)=4, "Boolean: " & A2, "Other type")))
// Routes processing based on specific data type

// Type-specific formatting
=IF(TYPE(B3)=1, TEXT(B3,"#,##0.00"), 
   IF(TYPE(B3)=2, UPPER(B3), 
      "Cannot format"))
// Applies appropriate formatting based on data type

// Multi-type validation
=IF(TYPE(C4)=16, "Error detected", 
   IF(OR(TYPE(C4)=1, TYPE(C4)=2), "Valid data", 
      "Unexpected type"))
// Validates for errors and acceptable data types
```

### [[CHOOSE]]
Works with TYPE to create lookup-based processing where different data types trigger different operations or formatting approaches.

```spreadsheets
// Type-based processing lookup
=CHOOSE(TYPE(D5), "Number processing", "Text processing", "", "Boolean processing")
// Index 1=number, 2=text, 4=boolean (adjusted for CHOOSE indexing)

// Dynamic processing based on type
=IF(TYPE(E6)<=4, 
   CHOOSE(IF(TYPE(E6)=1,1,IF(TYPE(E6)=2,2,IF(TYPE(E6)=4,3,4))), 
          E6*100, 
          UPPER(E6), 
          IF(E6,"TRUE","FALSE"), 
          "Unknown"), 
   "Error or array")
// Comprehensive type-based processing

// Type-specific validation messages
=CHOOSE(MIN(TYPE(F7),4), 
        "✓ Number accepted", 
        "✓ Text accepted", 
        "", 
        "⚠ Boolean - convert to number?")
// Provides type-appropriate feedback
```

## Data Conversion Functions

### [[VALUE]]
TYPE validates data before VALUE attempts conversion, ensuring text-to-number conversion only occurs on appropriate data types.

```spreadsheets
// Safe text-to-number conversion
=IF(TYPE(G8)=2, 
   IF(ISERROR(VALUE(G8)), "Cannot convert to number", VALUE(G8)), 
   IF(TYPE(G8)=1, G8, "Not text or number"))
// Converts text to numbers with comprehensive validation

// Data cleaning pipeline
=IF(TYPE(H9)=1, H9, 
   IF(AND(TYPE(H9)=2, ISNUMBER(VALUE(H9))), VALUE(H9), 
      "Invalid for numeric processing"))
// Standardizes mixed data types to numbers

// Import data processing
=IF(OR(TYPE(I10)=1, AND(TYPE(I10)=2, ISNUMBER(VALUE(I10)))), 
   VALUE(I10&""), 
   "Type: " & TYPE(I10) & " - Cannot process")
// Handles various numeric representations from imports
```

### [[TEXT]]
Combines with TYPE to apply text conversion only when appropriate and avoid errors from incompatible data types.

```spreadsheets
// Type-aware text conversion
=IF(TYPE(J11)=1, TEXT(J11,"#,##0.00"), 
   IF(TYPE(J11)=2, J11, 
      IF(TYPE(J11)=4, IF(J11,"TRUE","FALSE"), "Cannot convert")))
// Converts different types to appropriate text representations

// Number formatting with type check
=IF(TYPE(K12)=1, TEXT(K12,"0.0%"), 
   "Type " & TYPE(K12) & " - not a number")
// Only formats numbers as percentages

// Universal text conversion
=IF(TYPE(L13)=16, "ERROR", 
   IF(TYPE(L13)=1, TEXT(L13,"0"), 
      IF(TYPE(L13)=2, L13, 
         IF(TYPE(L13)=4, IF(L13,"TRUE","FALSE"), "Array"))))
// Converts all data types to text equivalents
```

## Data Analysis Functions

### [[SUMPRODUCT]]
TYPE works with SUMPRODUCT to count and analyze data types across ranges, providing comprehensive data composition analysis.

```spreadsheets
// Count by data type
="Numbers: " & SUMPRODUCT(--(TYPE(M2:M100)=1)) & 
 " | Text: " & SUMPRODUCT(--(TYPE(M2:M100)=2)) & 
 " | Errors: " & SUMPRODUCT(--(TYPE(M2:M100)=16))
// Comprehensive data type distribution

// Data quality metrics
=SUMPRODUCT(--(TYPE(N2:N50)=1))/COUNTA(N2:N50)*100 & "% numeric data"
// Calculates percentage of numeric values in dataset

// Type-based conditional calculations
=SUMPRODUCT((TYPE(O2:O25)=1)*(O2:O25))
// Sums only the numeric values in range
```

### [[FREQUENCY]]
Combines with TYPE to create data type distribution analysis, showing how different data types are distributed across datasets.

```spreadsheets
// Data type frequency analysis
=FREQUENCY(TYPE(P2:P30), {1;2;4;16;64})
// Returns array showing count of each data type

// Type distribution summary
="Type distribution: " & 
 SUMPRODUCT(--(TYPE(Q2:Q40)=1)) & " numbers, " &
 SUMPRODUCT(--(TYPE(Q2:Q40)=2)) & " text values, " &
 SUMPRODUCT(--(TYPE(Q2:Q40)=16)) & " errors"
// Comprehensive type composition report

// Data consistency validation
=IF(SUMPRODUCT(--(TYPE(R2:R20)=TYPE(R2)))=COUNTA(R2:R20), 
   "All same type: " & TYPE(R2), 
   "Mixed types detected")
// Validates data type consistency across range
```

## Commonly Used With Functions Examples

### Data Import Quality Control
```spreadsheets
// Comprehensive import validation
=IF(COUNTA(S2:S50)>0,
   "Import analysis: " & COUNTA(S2:S50) & " records | " &
   "Types: " & SUMPRODUCT(--(TYPE(S2:S50)=1)) & " numbers, " &
   SUMPRODUCT(--(TYPE(S2:S50)=2)) & " text, " &
   SUMPRODUCT(--(TYPE(S2:S50)=16)) & " errors | " &
   "Quality: " & IF(SUMPRODUCT(--(TYPE(S2:S50)=16))=0, "Good", "Issues detected"),
   "No data imported")
// Complete import quality assessment

// Type-specific data cleaning
=IF(TYPE(T51)=2, 
   IF(ISNUMBER(VALUE(T51)), VALUE(T51), PROPER(TRIM(T51))), 
   IF(TYPE(T51)=1, T51, 
      IF(TYPE(T51)=16, "CLEANING_REQUIRED", T51)))
// Applies appropriate cleaning based on data type
```

### Dynamic Data Processing
```spreadsheets
// Adaptive data processing
=IF(TYPE(U52)=1, 
   IF(U52>1000, TEXT(U52/1000,"#,##0.0") & "K", TEXT(U52,"#,##0")), 
   IF(TYPE(U52)=2, 
      IF(LEN(U52)>20, LEFT(U52,20) & "...", U52), 
      "Type " & TYPE(U52) & " not supported"))
// Processes numbers and text differently with appropriate formatting

// Multi-type aggregation
="Summary: " & 
 IF(SUMPRODUCT(--(TYPE(V2:V30)=1))>0, 
    "Avg: " & ROUND(SUMPRODUCT((TYPE(V2:V30)=1)*(V2:V30))/SUMPRODUCT(--(TYPE(V2:V30)=1)),2), 
    "No numbers") & 
 " | Text entries: " & SUMPRODUCT(--(TYPE(V2:V30)=2)) &
 " | Data quality: " & IF(SUMPRODUCT(--(TYPE(V2:V30)=16))=0, "Clean", "Has errors")
// Comprehensive summary handling multiple data types
```

### Database Preparation and Validation
```spreadsheets
// Database field type validation
=IF(TYPE(W53)=1, "NUMBER", 
   IF(TYPE(W53)=2, "VARCHAR(" & LEN(W53) & ")", 
      IF(TYPE(W53)=4, "BOOLEAN", 
         IF(TYPE(W53)=16, "ERROR_FIELD", "UNKNOWN_TYPE"))))
// Suggests appropriate database field types

// Multi-field record validation
=IF(AND(TYPE(X54)=2, TYPE(Y54)=1, TYPE(Z54)=1), 
   "✓ Record format correct: Name(text), Age(number), Score(number)", 
   "✗ Format error - Expected: Text, Number, Number | Got: " & 
   TYPE(X54) & ", " & TYPE(Y54) & ", " & TYPE(Z54))
// Validates record structure matches expected database schema
```