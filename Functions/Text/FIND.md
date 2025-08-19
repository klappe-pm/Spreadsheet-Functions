---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: text
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# FIND

## FIND Description

Locates the position of a specific text substring within a larger text string, returning the character position (1-based indexing). Case-sensitive search that enables dynamic text extraction and parsing operations.

> [!f(x)] FIND Syntax
>
> ```spreadsheets
> FIND(find_text, within_text, [start_num])
> ```
>
> **Parameters:**
> - `find_text` (required): The text you want to find
> - `within_text` (required): The text string to search within
> - `start_num` (optional): The character position to start searching from (defaults to 1)

> [!f(x)] FIND Examples
>
> ```spreadsheets
> // Find space position in name
> FIND(" ", "John Smith") → 5
> 
> // Find @ symbol in email
> FIND("@", "user@company.com") → 5
> 
> // Find file extension dot
> FIND(".", "document.pdf") → 9
> 
> // Case-sensitive search
> FIND("EXCEL", "excel worksheet") → #VALUE! (not found)
> 
> // Start search from position 3
> FIND("-", "555-123-4567", 3) → 8
> 
> // Find second occurrence of character
> FIND(" ", "First Middle Last", FIND(" ", "First Middle Last")+1) → 13
> ```

## Use Cases

### [[Dynamic text extraction]]
- **Name parsing operations**: Locate spaces and delimiters to extract first names, last names, and middle initials from full name fields
- **Email address parsing**: Find @ symbols and periods to separate usernames, domains, and extensions for contact management
- **File path processing**: Locate directory separators and periods to extract folder paths, filenames, and extensions from full file paths
- **URL component extraction**: Parse protocols, domains, and paths from web addresses for link analysis and validation

### [[Data validation and formatting]]
- **Format compliance checking**: Locate required characters and patterns to validate phone numbers, social security numbers, and other formatted data
- **Delimiter position validation**: Ensure proper placement of separators in structured data like CSV imports and standardized ID formats
- **Character existence verification**: Confirm presence of required characters before attempting extraction or manipulation operations
- **Pattern matching for data quality**: Identify malformed records by searching for expected formatting characters and patterns

### [[Advanced text processing]]
- **Multi-delimiter parsing**: Locate multiple separators to extract complex data structures like addresses, product codes, and hierarchical identifiers
- **Conditional text operations**: Enable dynamic LEFT, RIGHT, and MID operations based on found character positions rather than fixed positions
- **Text cleaning coordination**: Identify unwanted characters and formatting for removal or replacement in data standardization workflows
- **Template field location**: Find placeholder positions in templates for dynamic content insertion and document generation

## Related

### Similar Functions

- [[SEARCH]] - Case-insensitive text search, supports wildcards, alternative to FIND for flexible searching
- [[LEFT]] - Extracts characters from beginning, uses FIND results for dynamic extraction positions
- [[RIGHT]] - Extracts characters from end, combined with FIND for sophisticated text parsing
- [[MID]] - Extracts characters from middle, relies on FIND for start position calculations
- [[SUBSTITUTE]] - Replaces text characters, often used with FIND to locate replacement positions

## Text Extraction Functions

### [[LEFT]]
Essential partnership where FIND provides dynamic extraction positions for LEFT operations. FIND locates delimiters and markers, enabling LEFT to extract variable-length prefixes based on content structure.

```spreadsheets
// Extract text before first space using FIND
=LEFT(A1, FIND(" ", A1)-1)
// Example: "John Smith" → "John"

// Extract username from email address
=LEFT(B1, FIND("@", B1)-1)
// Example: "user@company.com" → "user"

// Extract filename without extension
=LEFT(C1, FIND(".", C1)-1)
// Example: "document.pdf" → "document"
```

### [[MID]]
Critical combination where FIND provides both start positions and length calculations for precise MID extractions. Together they enable sophisticated parsing of structured data with variable delimiters.

```spreadsheets
// Extract middle name using two FIND operations
=MID(A1, FIND(" ", A1)+1, FIND(" ", A1, FIND(" ", A1)+1)-FIND(" ", A1)-1)
// Example: "John Michael Smith" → "Michael"

// Extract domain from email without extension
=MID(B1, FIND("@", B1)+1, FIND(".", B1)-FIND("@", B1)-1)
// Example: "user@company.com" → "company"

// Extract text between delimiters
=MID(C1, FIND("-", C1)+1, FIND("-", C1, FIND("-", C1)+1)-FIND("-", C1)-1)
// Example: "DEPT-LAPTOP-001" → "LAPTOP"
```

## String Manipulation Functions

### [[SUBSTITUTE]]
Works with FIND to locate and replace specific text portions. FIND identifies exact positions for targeted substitutions, enabling precise text modifications and data standardization operations.

```spreadsheets
// Replace text after specific position found by FIND
=SUBSTITUTE(A1, MID(A1, FIND("@", A1), LEN(A1)), "@newdomain.com")
// Changes email domain while preserving username

// Count occurrences using FIND and SUBSTITUTE
=(LEN(B1)-LEN(SUBSTITUTE(B1, "a", "")))/LEN("a")
// Counts how many times "a" appears in text

// Replace text between found positions
=SUBSTITUTE(C1, MID(C1, FIND("[", C1), FIND("]", C1)-FIND("[", C1)+1), "[REPLACED]")
// Replaces text within brackets
```

### [[IF]]
Essential for error handling with FIND operations. IF manages cases where search text isn't found (FIND returns #VALUE! error) and provides alternative processing paths.

```spreadsheets
// Safe name extraction with error handling
=IF(ISERROR(FIND(" ", A1)), A1, LEFT(A1, FIND(" ", A1)-1))
// Returns full text if no space found, otherwise extracts first name

// Conditional processing based on character presence
=IF(ISERROR(FIND("@", B1)), "Not an email", "Valid email format")
// Validates email format by checking for @ symbol

// Multi-condition text parsing
=IF(ISERROR(FIND(".", C1)), "No extension", RIGHT(C1, LEN(C1)-FIND(".", C1)))
// Extracts file extension if present, otherwise indicates no extension
```

## Commonly Used With Functions Examples

### Email Processing System
```spreadsheets
// Process email: "john.smith@company.subdomain.com"

// Extract username portion
=LEFT(A1, FIND("@", A1)-1)
// Result: "john.smith"

// Extract complete domain
=RIGHT(A1, LEN(A1)-FIND("@", A1))
// Result: "company.subdomain.com"

// Extract main domain only
=MID(A1, FIND("@", A1)+1, FIND(".", A1, FIND("@", A1))-FIND("@", A1)-1)
// Result: "company"

// Validate email has both @ and .
=IF(AND(NOT(ISERROR(FIND("@", A1))), NOT(ISERROR(FIND(".", A1)))), "Valid format", "Invalid")
// Checks for required email components
```

### Name Parsing Workflow
```spreadsheets
// Process name: "Dr. John Michael Smith Jr."

// Extract title if present
=IF(ISERROR(FIND(".", B1)), "", LEFT(B1, FIND(".", B1)))
// Result: "Dr."

// Extract first name (after title, before second space)
=MID(B1, FIND(" ", B1)+1, FIND(" ", B1, FIND(" ", B1)+1)-FIND(" ", B1)-1)
// Result: "John"

// Extract middle name
=MID(B1, FIND(" ", B1, FIND(" ", B1)+1)+1, FIND(" ", B1, FIND(" ", B1, FIND(" ", B1)+1)+1)-FIND(" ", B1, FIND(" ", B1)+1)-1)
// Result: "Michael"

// Extract last name (before final space or end)
=IF(ISERROR(FIND(" Jr.", B1)), MID(B1, FIND(" ", B1, FIND(" ", B1)+1)+1, LEN(B1)), LEFT(MID(B1, FIND(" ", B1, FIND(" ", B1)+1)+1, LEN(B1)), FIND(" ", MID(B1, FIND(" ", B1, FIND(" ", B1)+1)+1, LEN(B1)))-1))
// Result: "Smith"
```

### File Path Analysis
```spreadsheets
// Process path: "C:\\Users\\Documents\\Reports\\Q1_2024.xlsx"

// Extract drive letter
=LEFT(C1, FIND(":", C1)-1)
// Result: "C"

// Extract filename with extension
=RIGHT(C1, LEN(C1)-FIND("", SUBSTITUTE(C1, "\\", "", LEN(C1)-LEN(SUBSTITUTE(C1, "\\", "")))))
// Result: "Q1_2024.xlsx"

// Extract filename without extension
=LEFT(RIGHT(C1, LEN(C1)-FIND("", SUBSTITUTE(C1, "\\", "", LEN(C1)-LEN(SUBSTITUTE(C1, "\\", ""))))), FIND(".", RIGHT(C1, LEN(C1)-FIND("", SUBSTITUTE(C1, "\\", "", LEN(C1)-LEN(SUBSTITUTE(C1, "\\", ""))))))-1)
// Result: "Q1_2024"

// Extract file extension
=RIGHT(C1, LEN(C1)-FIND(".", SUBSTITUTE(C1, ".", "", LEN(C1)-LEN(SUBSTITUTE(C1, ".", ""))-1)))
// Result: "xlsx"
```

### Product SKU Parsing
```spreadsheets
// Process SKU: "ELECTRONICS-LAPTOP-HP-PAVILION-15-2024-001"

// Count number of delimiters
=(LEN(D1)-LEN(SUBSTITUTE(D1, "-", "")))
// Result: 6 (six hyphens)

// Extract first segment (department)
=LEFT(D1, FIND("-", D1)-1)
// Result: "ELECTRONICS"

// Extract second segment (category)
=MID(D1, FIND("-", D1)+1, FIND("-", D1, FIND("-", D1)+1)-FIND("-", D1)-1)
// Result: "LAPTOP"

// Extract last segment (sequence)
=RIGHT(D1, LEN(D1)-FIND("-", SUBSTITUTE(D1, "-", REPT("-", 100), LEN(D1)-LEN(SUBSTITUTE(D1, "-", ""))))/100)
// Result: "001"

// Extract year (second to last segment)
=MID(D1, FIND("-", SUBSTITUTE(D1, "-", REPT("-", 100), LEN(D1)-LEN(SUBSTITUTE(D1, "-", ""))-1))/100+1, 4)
// Result: "2024"
```

### Phone Number Validation
```spreadsheets
// Process phone: "(555) 123-4567 ext. 890"

// Find opening parenthesis position
=FIND("(", E1)
// Result: 1

// Extract area code
=MID(E1, FIND("(", E1)+1, FIND(")", E1)-FIND("(", E1)-1)
// Result: "555"

// Extract main number
=MID(E1, FIND(") ", E1)+2, FIND(" ext", E1)-FIND(") ", E1)-2)
// Result: "123-4567"

// Extract extension if present
=IF(ISERROR(FIND("ext", E1)), "No extension", RIGHT(E1, LEN(E1)-FIND("ext. ", E1)-4))
// Result: "890"

// Validate phone format
=IF(AND(NOT(ISERROR(FIND("(", E1))), NOT(ISERROR(FIND(")", E1))), NOT(ISERROR(FIND("-", E1)))), "Valid format", "Invalid format")
// Checks for required phone number components
```
