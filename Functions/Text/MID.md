---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - text
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
# MID

## MID Description

Extracts a specified number of characters from any position within a text string, starting at a designated character position. Essential for parsing structured data, extracting middle portions of identifiers, and isolating specific segments from formatted text strings.

> [!f(x)] MID Syntax
>
> ```spreadsheets
> MID(text, start_num, num_chars)
> ```
>
> **Parameters:**
> - `text` (required): The text string from which to extract characters
> - `start_num` (required): The position of the first character to extract (1-based indexing)
> - `num_chars` (required): The number of characters to extract from the starting position

> [!f(x)] MID Examples
>
> ```spreadsheets
> // Extract middle name from full name
> MID("John Michael Smith", 6, 7) → "Michael"
> 
> // Extract month from date string
> MID("2024-03-15", 6, 2) → "03"
> 
> // Extract area code from formatted phone
> MID("(555) 123-4567", 2, 3) → "555"
> 
> // Extract product code from SKU
> MID("ELEC-LAPTOP-001", 6, 6) → "LAPTOP"
> 
> // Extract time from timestamp
> MID("2024-03-15 14:30:25", 12, 8) → "14:30:25"
> 
> // Extract substring from position 3, length 4
> MID("ABCDEFGH", 3, 4) → "CDEF"
> ```

## Use Cases

### [[Structured data extraction]]
- **Social Security parsing**: Extract specific segments from SSN formats for validation and partial display while maintaining privacy
- **Credit card processing**: Parse card number segments for validation, type identification, and secure masked display operations
- **ISBN analysis**: Extract publisher codes, title codes, and check digits from book identification numbers for library systems
- **Serial number validation**: Parse manufacturing codes, date codes, and sequence numbers from product serial identifiers

### [[Date and time processing]]
- **Date component isolation**: Extract specific date parts (year, month, day) from various date string formats for temporal analysis
- **Time parsing operations**: Isolate hour, minute, and second components from timestamp strings for time-based calculations
- **Fiscal period extraction**: Parse quarter and year information from financial date codes for accounting and reporting cycles
- **Log timestamp analysis**: Extract specific time components from system logs for performance monitoring and troubleshooting

### [[Geographic and coordinate data]]
- **Coordinate precision parsing**: Extract degrees, minutes, and seconds from GPS coordinate strings for mapping applications
- **ZIP+4 code processing**: Parse standard ZIP and extended codes from postal addresses for shipping and geographic analysis
- **Geolocation data extraction**: Extract latitude and longitude components from combined coordinate strings for GIS processing
- **Address component isolation**: Parse street numbers, unit numbers, and directional indicators from standardized address formats

## Related

### Similar Functions

- [[LEFT]] - Extracts characters from the beginning of a text string, used with MID for complete string parsing
- [[RIGHT]] - Extracts characters from the end of a text string, complements MID for full string analysis
- [[SUBSTRING]] - Alternative function for extracting text portions with similar functionality to MID
- [[FIND]] - Locates character positions within text, essential for dynamic MID operations
- [[SEARCH]] - Case-insensitive position finding, frequently used with MID for flexible extraction

## Text Processing Functions

### [[FIND]]
Critical partner to MID for dynamic text extraction. FIND locates specific characters or substrings, providing the start position for MID operations based on content structure rather than fixed positions.

```spreadsheets
// Extract text between two spaces
=MID(A1, FIND(" ", A1)+1, FIND(" ", A1, FIND(" ", A1)+1)-FIND(" ", A1)-1)
// Example: "John Michael Smith" → "Michael"

// Extract domain from email without extension
=MID(B1, FIND("@", B1)+1, FIND(".", B1)-FIND("@", B1)-1)
// Example: "user@company.com" → "company"

// Extract filename without path and extension
=MID(C1, FIND("\\", SUBSTITUTE(C1, "\\", REPT("\\", 100)))/100+1, FIND(".", C1)-FIND("\\", SUBSTITUTE(C1, "\\", REPT("\\", 100)))/100-1)
// Extracts filename from full file path
```

### [[LEN]]
Works with MID to calculate dynamic extraction lengths and validate text boundaries. LEN provides string length information for proportional extractions and prevents MID operations from exceeding available characters.

```spreadsheets
// Extract middle portion of text (skip first and last 2 characters)
=MID(A1, 3, LEN(A1)-4)
// Example: "ABCDEFGH" → "CDEF"

// Extract last half of text using MID
=MID(B1, LEN(B1)/2+1, LEN(B1)/2)
// Dynamically extracts second half of string

// Safe extraction with length validation
=IF(LEN(C1)>=10, MID(C1, 3, 5), "Too short")
// Ensures string has sufficient length before extraction
```

## String Manipulation Functions

### [[SUBSTITUTE]]
Prepares text for consistent MID operations by normalizing formats and removing unwanted characters. SUBSTITUTE standardizes text before MID extraction, ensuring reliable positioning and clean results.

```spreadsheets
// Extract phone number middle after removing formatting
=MID(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), 4, 3)
// Example: "(555) 123-4567" → "123"

// Extract clean product code after standardizing separators
=MID(SUBSTITUTE(B1, "_", "-"), FIND("-", SUBSTITUTE(B1, "_", "-"))+1, 6)
// Handles mixed separator formats consistently

// Extract text segment after removing spaces
=MID(SUBSTITUTE(C1, " ", ""), 3, 4)
// Example: "AB CD EF GH" → "CDEF"
```

### [[CONCATENATE]]
Combines MID extraction results with other text elements for reformatting and data presentation. Together they enable sophisticated text restructuring and standardized output formatting.

```spreadsheets
// Format phone number using MID extractions
=CONCATENATE("(", MID(A1, 1, 3), ") ", MID(A1, 4, 3), "-", MID(A1, 7, 4))
// Example: "5551234567" → "(555) 123-4567"

// Build formatted date from components
=CONCATENATE(MID(B1, 6, 2), "/", MID(B1, 9, 2), "/", MID(B1, 1, 4))
// Example: "2024-03-15" → "03/15/2024"

// Create masked account number
=CONCATENATE(MID(C1, 1, 4), "-****-", MID(C1, 9, 4))
// Example: "123456789012" → "1234-****-9012"
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional MID operations and error handling. IF enables safe extraction with validation, handles variable formats, and provides fallback results when extraction conditions aren't met.

```spreadsheets
// Safe middle name extraction with validation
=IF(LEN(A1)-LEN(SUBSTITUTE(A1, " ", ""))>=2, MID(A1, FIND(" ", A1)+1, FIND(" ", A1, FIND(" ", A1)+1)-FIND(" ", A1)-1), "No middle name")
// Only extracts if at least two spaces exist

// Conditional extraction based on string length
=IF(LEN(B1)>=12, MID(B1, 5, 4), MID(B1, 3, 2))
// Adjusts extraction position and length based on content

// Safe date component extraction with error handling
=IF(ISERROR(MID(C1, 6, 2)), "Invalid date", MID(C1, 6, 2))
// Handles malformed date strings gracefully
```

## Commonly Used With Functions Examples

### Social Security Number Processing
```spreadsheets
// Process SSN format: "123-45-6789"

// Extract area number (first 3 digits)
=MID(A1, 1, 3)
// Result: "123"

// Extract group number (middle 2 digits)
=MID(A1, 5, 2)
// Result: "45"

// Extract serial number (last 4 digits)
=MID(A1, 8, 4)
// Result: "6789"

// Create masked display
=CONCATENATE("***-**-", MID(A1, 8, 4))
// Result: "***-**-6789"

// Validate SSN format
=IF(AND(LEN(A1)=11, MID(A1, 4, 1)="-", MID(A1, 7, 1)="-"), "Valid", "Invalid")
// Checks proper SSN formatting
```

### Credit Card Processing System
```spreadsheets
// Process card number: "4532-1234-5678-9012"

// Extract first 4 digits (issuer identification)
=MID(B1, 1, 4)
// Result: "4532"

// Extract middle 8 digits (account identifier)
=MID(B1, 6, 9)
// Result: "1234-5678" (includes hyphen)

// Extract last 4 digits for display
=MID(B1, 16, 4)
// Result: "9012"

// Create masked display
=CONCATENATE(MID(B1, 1, 4), "-****-****-", MID(B1, 16, 4))
// Result: "4532-****-****-9012"

// Determine card type by first digit
=IF(MID(B1, 1, 1)="4", "Visa", IF(MID(B1, 1, 1)="5", "MasterCard", "Other"))
// Identifies card issuer
```

### Date and Time Analysis
```spreadsheets
// Process timestamp: "2024-03-15 14:30:25"

// Extract date components
=MID(C1, 1, 4) & " Year: " & MID(C1, 6, 2) & " Month: " & MID(C1, 9, 2) & " Day"
// Result: "2024 Year: 03 Month: 15 Day"

// Extract time components  
=MID(C1, 12, 2) & " Hour: " & MID(C1, 15, 2) & " Min: " & MID(C1, 18, 2) & " Sec"
// Result: "14 Hour: 30 Min: 25 Sec"

// Create time period identifier
=IF(VALUE(MID(C1, 12, 2))<12, "AM", "PM")
// Result: "PM"

// Extract fiscal quarter from date
=CONCATENATE("Q", IF(VALUE(MID(C1, 6, 2))<=3, "1", IF(VALUE(MID(C1, 6, 2))<=6, "2", IF(VALUE(MID(C1, 6, 2))<=9, "3", "4"))), "-", MID(C1, 1, 4))
// Result: "Q1-2024"
```

### Product SKU Analysis System
```spreadsheets
// Process SKU: "ELEC-LAPTOP-HP-PAVILION-15-2024-001"

// Extract department (first segment)
=MID(D1, 1, FIND("-", D1)-1)
// Result: "ELEC"

// Extract product category (second segment)
=MID(D1, FIND("-", D1)+1, FIND("-", D1, FIND("-", D1)+1)-FIND("-", D1)-1)
// Result: "LAPTOP"

// Extract brand (third segment)
=MID(D1, FIND("-", D1, FIND("-", D1)+1)+1, FIND("-", D1, FIND("-", D1, FIND("-", D1)+1)+1)-FIND("-", D1, FIND("-", D1)+1)-1)
// Result: "HP"

// Extract year from end portion
=MID(D1, LEN(D1)-7, 4)
// Result: "2024"

// Create short identifier
=CONCATENATE(MID(D1, 1, 2), MID(D1, FIND("-", D1)+1, 3), MID(D1, LEN(D1)-2, 3))
// Result: "ELLAP001"
```

### Geographic Coordinate Processing
```spreadsheets
// Process coordinates: "40.7128,-74.0060" (lat,lng)

// Extract latitude
=MID(E1, 1, FIND(",", E1)-1)
// Result: "40.7128"

// Extract longitude
=MID(E1, FIND(",", E1)+1, LEN(E1))
// Result: "-74.0060"

// Extract latitude degrees (whole number part)
=MID(E1, 1, FIND(".", E1)-1)
// Result: "40"

// Extract precision (decimal places)
=MID(E1, FIND(".", E1)+1, FIND(",", E1)-FIND(".", E1)-1)
// Result: "7128"

// Format for display
=CONCATENATE("Lat: ", MID(E1, 1, FIND(",", E1)-1), "°, Lng: ", MID(E1, FIND(",", E1)+1, LEN(E1)), "°")
// Result: "Lat: 40.7128°, Lng: -74.0060°"
```
