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
# UPPER

## UPPER Description

Converts all letters in a text string to uppercase. Essential for data standardization, case-insensitive comparisons, and creating consistent text formatting in business applications.

> [!f(x)] UPPER Syntax
>
> ```spreadsheets
> UPPER(text)
> ```
>
> **Parameters:**
> - `text` (required): The text string to convert to uppercase

> [!f(x)] UPPER Examples
>
> ```spreadsheets
> // Convert mixed case to uppercase
> UPPER("John Smith") → "JOHN SMITH"
> 
> // Standardize status codes
> UPPER("active") → "ACTIVE"
> 
> // Format product codes
> UPPER("abc-123-xyz") → "ABC-123-XYZ"
> 
> // Clean user input for comparison
> UPPER("Yes") → "YES"
> 
> // Numbers and symbols unchanged
> UPPER("Price: $123.45") → "PRICE: $123.45"
> ```

## Use Cases

### [[Data standardization]]
- **Database consistency**: Standardize text fields for consistent storage and accurate querying
- **User input normalization**: Convert form inputs to uppercase for validation and comparison
- **Code standardization**: Ensure consistent formatting of product codes, SKUs, and identifiers

### [[Text comparison]]
- **Case-insensitive matching**: Enable accurate comparisons regardless of original case
- **Search optimization**: Standardize search terms for better matching results
- **Duplicate detection**: Identify duplicates that differ only in case

### [[Report formatting]]
- **Headers and labels**: Create consistent uppercase formatting for report headers
- **Status displays**: Standardize status indicators and category labels
- **Professional presentation**: Apply consistent case formatting for business documents

## Related

### Similar Functions

- [[LOWER]] - Converts text to lowercase, opposite of UPPER for alternative standardization
- [[PROPER]] - Converts text to title case, alternative formatting option to UPPER
- [[TRIM]] - Removes extra spaces, frequently combined with UPPER for complete text cleaning
- [[SUBSTITUTE]] - Replaces specific text, often used with UPPER for advanced text standardization
- [[EXACT]] - Case-sensitive text comparison, used to verify UPPER conversion results

### Commonly Used With Functions Examples

```spreadsheets
// Standardize and compare text
=IF(UPPER(TRIM(A1))=UPPER(TRIM(B1)), "Match", "No Match")
// Performs case-insensitive comparison with space cleaning

// Create formatted product codes
=CONCATENATE(UPPER(C1), "-", TEXT(D1, "000"))
// Example: "widget" + 123 → "WIDGET-123"

// Clean and standardize user input
=UPPER(SUBSTITUTE(TRIM(E1), " ", ""))
// Removes spaces and converts to uppercase for codes
```
