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
# TRIM

## TRIM Description

Removes leading and trailing spaces from text and reduces multiple internal spaces to single spaces. Essential for data cleaning, standardization, and preparing imported text for accurate processing and comparison operations.

> [!f(x)] TRIM Syntax
>
> ```spreadsheets
> TRIM(text)
> ```
>
> **Parameters:**
> - `text` (required): The text string from which to remove extra spaces

> [!f(x)] TRIM Examples
>
> ```spreadsheets
> // Remove leading and trailing spaces
> TRIM("  John Smith  ") → "John Smith"
> 
> // Reduce multiple internal spaces to single
> TRIM("John    Smith") → "John Smith"
> 
> // Clean imported data with irregular spacing
> TRIM("  Product   Name  ") → "Product Name"
> 
> // Combine with other functions for data cleaning
> UPPER(TRIM("  mixed case  ")) → "MIXED CASE"
> 
> // No change needed for properly formatted text
> TRIM("Clean Text") → "Clean Text"
> 
> // Clean address data for matching
> TRIM("  123 Main St  ") → "123 Main St"
> ```

## Use Cases

### [[Data import and cleaning]]
- **CSV data standardization**: Clean irregularly spaced imported data for consistent processing and accurate comparisons
- **Form input normalization**: Remove accidental spaces from user input fields to prevent validation and matching errors
- **Database preparation**: Standardize text fields before database insertion to maintain data integrity and enable proper indexing
- **Legacy data migration**: Clean historical data with inconsistent spacing patterns for modern system compatibility

### [[Text comparison and matching]]
- **Duplicate detection**: Prepare text for accurate comparison by removing spacing variations that prevent proper matching
- **Search optimization**: Clean search terms and data to improve search accuracy and reduce false negatives
- **Data validation**: Ensure consistent formatting for validation rules and business logic that depend on exact text matches
- **Report standardization**: Create uniform text formatting for professional reports and consistent data presentation

### [[Integration with other text functions]]
- **Preprocessing for extraction**: Clean text before using LEFT, RIGHT, MID, and FIND functions for reliable positioning
- **Concatenation preparation**: Ensure clean inputs for CONCATENATE operations to prevent awkward spacing in output
- **Case conversion setup**: Prepare text for UPPER, LOWER, and PROPER functions by removing irregular spacing
- **Substitution accuracy**: Clean text before SUBSTITUTE operations to ensure consistent replacement patterns

## Related

### Similar Functions

- [[CLEAN]] - Removes non-printable characters, complementary to TRIM for comprehensive text cleaning
- [[SUBSTITUTE]] - Replaces specific characters, can target specific spacing patterns TRIM cannot handle
- [[LEFT]] - Often used with TRIM for clean text extraction from the beginning of strings
- [[RIGHT]] - Combined with TRIM for clean text extraction from the end of strings
- [[UPPER]] - Frequently paired with TRIM for complete text standardization workflows

## Commonly Used With Functions Examples

### Data Import Cleaning Pipeline
```spreadsheets
// Clean imported customer data: "  John  Smith  ,  Manager  ,  Active  "

// Step 1: Trim each field separately
=TRIM(LEFT(A1, FIND(",", A1)-1)) // Name: "John Smith"
=TRIM(MID(A1, FIND(",", A1)+1, FIND(",", A1, FIND(",", A1)+1)-FIND(",", A1)-1)) // Title: "Manager"
=TRIM(RIGHT(A1, LEN(A1)-FIND(",", A1, FIND(",", A1)+1))) // Status: "Active"

// Step 2: Combine cleaning with case standardization
=PROPER(TRIM(LEFT(A1, FIND(",", A1)-1))) // Result: "John Smith"
=UPPER(TRIM(RIGHT(A1, LEN(A1)-FIND(",", A1, FIND(",", A1)+1)))) // Result: "ACTIVE"
```

### Text Standardization System
```spreadsheets
// Standardize various text inputs for consistent processing

// Clean and standardize names
=PROPER(TRIM(SUBSTITUTE(B1, "  ", " "))) // Handles multiple spaces
// Input: "  john   SMITH  " → Output: "John Smith"

// Prepare addresses for geocoding
=TRIM(SUBSTITUTE(SUBSTITUTE(C1, CHAR(10), " "), CHAR(13), " "))
// Removes line breaks and trims spaces

// Standardize phone number text portions
=TRIM(SUBSTITUTE(SUBSTITUTE(D1, "(", ""), ")", ""))
// Input: "  ( 555 ) 123-4567  " → Output: "555  123-4567"
```
