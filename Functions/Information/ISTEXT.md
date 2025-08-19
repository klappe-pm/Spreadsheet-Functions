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

# ISTEXT

## ISTEXT Description

Returns TRUE if a cell contains text data, and FALSE if the cell contains numbers, logical values, dates, errors, or is empty. Essential for text processing, data validation, and content-specific operations in spreadsheets.

> [!f(x)] ISTEXT Syntax
>
> ```spreadsheets
> ISTEXT(value)
> ISTEXT(cell_reference)
> ```
>
> **Parameters:**
> - `value` (required): The cell reference or value to test for text data type

> [!f(x)] ISTEXT Examples
>
> ```spreadsheets
> // Test text value
> ISTEXT("Hello") → TRUE
> 
> // Test number as text
> ISTEXT("123") → TRUE (text representation of number)
> 
> // Test actual number
> ISTEXT(123) → FALSE (numeric value)
> 
> // Test empty cell
> ISTEXT("") → TRUE (empty string is text)
> 
> // Test formula result
> ISTEXT(A1&"") → TRUE (concatenation creates text)
> ```

## Use Cases

### [[Text processing]]
- **Content categorization**: Identify text fields in mixed data for appropriate string manipulation and formatting operations
- **Data export preparation**: Separate text content from numeric data when exporting to systems requiring specific data type handling
- **String function validation**: Ensure text functions like LEN, LEFT, RIGHT operate only on valid text data to prevent errors
- **Language processing**: Validate text input for translation, spell-checking, or natural language processing workflows

### [[Data import validation]]
- **File import quality control**: Verify that text columns contain only text data after importing from external sources
- **Database field validation**: Check that name, description, and comment fields contain text before database operations
- **CSV processing**: Validate data types during CSV import to prevent numeric operations on text fields
- **API data verification**: Confirm incoming API data matches expected text format specifications before processing

### [[Report formatting]]
- **Dynamic formatting**: Apply text-specific formatting like alignment, case conversion, or truncation only to text cells
- **Content-aware display**: Show different formatting for text versus numeric content in reports and dashboards
- **Template processing**: Conditionally process text fields in document templates while preserving numeric calculations
- **Multi-format output**: Generate reports with appropriate formatting based on whether content is text or numbers

## Related

### Similar Functions

- [[ISNUMBER]] - Tests if a cell contains numeric data, complementary to ISTEXT for complete data type identification
- [[ISBLANK]] - Checks if a cell is empty, used with ISTEXT to distinguish between empty cells and empty strings
- [[ISLOGICAL]] - Detects boolean values, combined with ISTEXT for comprehensive data type analysis
- [[TYPE]] - Returns numeric codes for different data types, providing more detailed information than ISTEXT
- [[ISNONTEXT]] - Returns opposite of ISTEXT, identifying non-text values in datasets

## Text Processing Functions

### [[LEN]]
ISTEXT validates input before LEN calculates character count, ensuring string length functions operate only on valid text data and preventing calculation errors.

```spreadsheets
// Safe text length calculation
=IF(ISTEXT(A2), LEN(A2), "Not text")
// Only calculates length if cell contains text

// Content length validation
=IF(ISTEXT(B3), IF(LEN(B3)>50, "Too long", "OK"), "Enter text")
// Validates both data type and content length

// Character count summary
=IF(ISTEXT(C4), "Text: " & LEN(C4) & " characters", "No text to count")
// Provides character count with data type confirmation
```

### [[CONCATENATE]]
Works with ISTEXT to safely combine text values, ensuring concatenation operations only occur with valid text input and handle mixed data types appropriately.

```spreadsheets
// Safe text concatenation
=IF(AND(ISTEXT(D5), ISTEXT(E5)), D5&" "&E5, "Invalid text inputs")
// Concatenates only if both cells contain text

// Mixed data type handling
=IF(ISTEXT(F6), F6, TEXT(F6,"0")) & " processed"
// Converts numbers to text before concatenation

// Dynamic string building
=IF(ISTEXT(G7), "Name: " & G7, "Please enter name")
// Creates formatted strings only with valid text input
```

## Data Validation Functions

### [[IF]]
ISTEXT combined with IF enables text-specific processing, conditional formatting, and data validation based on content type identification.

```spreadsheets
// Text-specific processing
=IF(ISTEXT(H8), UPPER(H8), "Enter text for conversion")
// Applies text functions only to text values

// Data type routing
=IF(ISTEXT(I9), I9 & " (text)", TEXT(I9,"0") & " (converted)")
// Handles text and numeric values differently

// Content validation
=IF(ISTEXT(J10), IF(LEN(J10)>0, J10, "Text required"), "Not text")
// Validates both data type and content presence
```

### [[COUNTIF]]
Combines with ISTEXT to count text entries in ranges, essential for data quality assessment and content analysis in large datasets.

```spreadsheets
// Count text entries manually
=SUMPRODUCT(--(ISTEXT(K2:K100)))
// Counts cells containing text in the range

// Text vs numeric distribution
="Text: " & SUMPRODUCT(--(ISTEXT(L2:L50))) & 
 " | Numbers: " & SUMPRODUCT(--(ISNUMBER(L2:L50)))
// Shows distribution of data types

// Content completeness for text fields
=SUMPRODUCT(--(ISTEXT(M2:M25)))/COUNTA(M2:M25)*100 & "% text entries"
// Calculates percentage of text values in data
```

## String Manipulation Functions

### [[LEFT]]
ISTEXT validates input before LEFT extracts characters from the beginning of text strings, preventing errors when processing mixed data types.

```spreadsheets
// Safe text extraction
=IF(ISTEXT(N11), LEFT(N11,5), "No text to extract")
// Extracts first 5 characters only from text

// Prefix extraction with validation
=IF(ISTEXT(O12), "Code: " & LEFT(O12,3), "Enter valid text")
// Creates formatted output with text prefix extraction

// Conditional text parsing
=IF(ISTEXT(P13), IF(LEN(P13)>=10, LEFT(P13,10), P13), "Invalid input")
// Extracts substring with length validation
```

### [[FIND]]
Works with ISTEXT to locate substrings within text values, ensuring search operations only occur on valid text data and handle missing or invalid content.

```spreadsheets
// Safe text search
=IF(ISTEXT(Q14), FIND("@",Q14), "Not text - cannot search")
// Searches for "@" symbol only in text values

// Email validation with text check
=IF(ISTEXT(R15), IF(ISERROR(FIND("@",R15)), "Invalid email", "Valid"), "Not text")
// Validates email format after confirming text data type

// Position-based text parsing
=IF(ISTEXT(S16), LEFT(S16,FIND("-",S16)-1), "No text to parse")
// Extracts text before dash character with validation
```

## Data Analysis Functions

### [[COUNTA]]
ISTEXT works with COUNTA to provide comprehensive cell counting analysis, distinguishing between text content and other data types for complete data inventory.

```spreadsheets
// Text content analysis
="Total entries: " & COUNTA(T2:T30) & 
 " | Text: " & SUMPRODUCT(--(ISTEXT(T2:T30))) & 
 " | Numbers: " & SUMPRODUCT(--(ISNUMBER(T2:T30)))
// Complete data type breakdown for range

// Text field completion rate
=SUMPRODUCT(--(ISTEXT(U2:U20)))/20*100 & "% text completion rate"
// Shows percentage of cells containing text content

// Data quality scorecard
=IF(SUMPRODUCT(--(ISTEXT(V2:V15)))>0, 
   "Text data available", 
   "No text entries found")
// Validates presence of text data in range
```

## Commonly Used With Functions Examples

### Data Import and Type Checking
```spreadsheets
// Comprehensive data type analysis
=IF(ISBLANK(W17), "Empty", 
   IF(ISTEXT(W17), "Text: " & LEN(W17) & " chars", 
      IF(ISNUMBER(W17), "Number: " & W17, "Other type")))
// Categorizes data by type with relevant details

// Import validation with type conversion
=IF(ISTEXT(X18), 
   IF(ISNUMBER(VALUE(X18)), VALUE(X18), X18), 
   X18)
// Converts text numbers to actual numbers, preserves other text
```

### Content Management and Formatting
```spreadsheets
// Dynamic content formatting
=IF(ISTEXT(Y19), 
   IF(LEN(Y19)>30, LEFT(Y19,30) & "...", Y19), 
   TEXT(Y19,"0"))
// Truncates long text, formats numbers as text

// Data cleanup and standardization  
=IF(ISTEXT(Z20), 
   PROPER(TRIM(Z20)), 
   "Non-text: " & TEXT(Z20,"0"))
// Applies text cleaning only to text values, handles others appropriately
```

### Report Generation and Analytics
```spreadsheets
// Content-aware report generation
=IF(SUMPRODUCT(--(ISTEXT(AA2:AA25)))>0,
   "Text Analysis: " & SUMPRODUCT(--(ISTEXT(AA2:AA25))) & " text entries found" &
   " | Average length: " & 
   SUMPRODUCT((ISTEXT(AA2:AA25))*(LEN(AA2:AA25)))/SUMPRODUCT(--(ISTEXT(AA2:AA25))),
   "No text data for analysis")
// Generates text analytics report with average character length

// Multi-criteria data summary
="Data Summary: " & COUNTA(BB2:BB30) & " total | " &
 SUMPRODUCT(--(ISTEXT(BB2:BB30))) & " text | " &
 SUMPRODUCT(--(ISNUMBER(BB2:BB30))) & " numeric | " &
 SUMPRODUCT(--(ISBLANK(BB2:BB30))) & " empty"
// Complete data composition analysis for quality assessment
```