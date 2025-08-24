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
# SUBSTITUTE

## SUBSTITUTE Description

Replaces occurrences of specific text within a string with new text. Case-sensitive replacement function essential for data cleaning, standardization, and text preprocessing in data analysis workflows.

> [!f(x)] SUBSTITUTE Syntax
>
> ```spreadsheets
> SUBSTITUTE(text, old_text, new_text, [instance_num])
> ```
>
> **Parameters:**
> - `text` (required): The original text string to process
> - `old_text` (required): The text to be replaced
> - `new_text` (required): The replacement text
> - `instance_num` (optional): Which occurrence to replace (defaults to all occurrences)

> [!f(x)] SUBSTITUTE Examples
>
> ```spreadsheets
> // Replace all spaces with hyphens
> SUBSTITUTE("John Smith", " ", "-") → "John-Smith"
> 
> // Remove all spaces
> SUBSTITUTE("555 123 4567", " ", "") → "5551234567"
> 
> // Replace only first occurrence
> SUBSTITUTE("apple apple apple", "apple", "orange", 1) → "orange apple apple"
> 
> // Replace file extension
> SUBSTITUTE("document.txt", ".txt", ".pdf") → "document.pdf"
> 
> // Clean phone formatting
> SUBSTITUTE(SUBSTITUTE("(555) 123-4567", "(", ""), ")", "") → "555 123-4567"
> 
> // Count character occurrences
> LEN("hello")-LEN(SUBSTITUTE("hello", "l", "")) → 2
> ```

## Use Cases

### [[Data cleaning and standardization]]
- **Phone number formatting**: Remove or standardize separators in phone numbers for consistent database storage and validation
- **Address standardization**: Replace abbreviations with full words or standardize directional indicators in address fields
- **Name data cleaning**: Remove titles, extra spaces, and standardize name formats for matching and deduplication
- **ID format normalization**: Convert various ID formats to standard patterns for system integration and data consistency

### [[Character removal and replacement]]
- **Special character elimination**: Remove unwanted punctuation, symbols, and formatting characters from imported data
- **Case standardization preparation**: Replace characters before case conversion to ensure proper text formatting
- **Delimiter standardization**: Convert various separators (commas, semicolons, pipes) to consistent delimiters for parsing
- **Encoding cleanup**: Replace problematic characters that cause encoding issues in system transfers and exports

### [[Content preprocessing]]
- **Template variable replacement**: Substitute placeholder text with actual values in document templates and form letters
- **URL and path standardization**: Replace backslashes with forward slashes or standardize path separators for cross-platform compatibility
- **Data masking preparation**: Replace sensitive characters with asterisks or placeholder text for secure data display
- **Import format conversion**: Transform data formats during import processes to match target system requirements

## Related

### Similar Functions

- [[REPLACE]] - Replaces characters at specific positions, different from SUBSTITUTE which replaces by content
- [[FIND]] - Locates text positions, often used with SUBSTITUTE for conditional replacements
- [[SEARCH]] - Case-insensitive text location, alternative for SUBSTITUTE position calculations
- [[TRIM]] - Removes leading/trailing spaces, complementary to SUBSTITUTE for space management
- [[CLEAN]] - Removes non-printable characters, works alongside SUBSTITUTE for comprehensive text cleaning

## Text Processing Functions

### [[LEN]]
Essential partnership for measuring SUBSTITUTE effectiveness and counting character occurrences. LEN quantifies changes made by SUBSTITUTE operations and validates replacement success.

```spreadsheets
// Count occurrences of character
=LEN(A1)-LEN(SUBSTITUTE(A1, "a", ""))
// Counts how many "a" characters exist in text

// Measure replacement impact
=LEN(SUBSTITUTE(B1, "old", "replacement"))-LEN(B1)
// Shows character count change after substitution

// Validate substitution occurred
=IF(LEN(SUBSTITUTE(C1, "find", "replace"))!=LEN(C1), "Changed", "No change")
// Confirms whether replacement was made
```

### [[IF]]
Critical for conditional SUBSTITUTE operations and error handling. IF enables targeted replacements based on conditions and manages cases where substitution may not be appropriate.

```spreadsheets
// Conditional replacement based on content
=IF(ISERROR(FIND("@", A1)), A1, SUBSTITUTE(A1, "@", " AT "))
// Only replaces @ symbol if it exists in text

// Replace based on character count
=IF(LEN(B1)>10, SUBSTITUTE(B1, " ", ""), B1)
// Removes spaces only from long text strings

// Selective character removal
=IF(LEFT(C1, 1)="$", SUBSTITUTE(C1, "$", ""), C1)
// Removes dollar sign only if text starts with it
```

## String Manipulation Functions

### [[FIND]]
Works with SUBSTITUTE for position-aware text replacement. FIND locates specific characters, enabling SUBSTITUTE to make targeted replacements based on context and position.

```spreadsheets
// Replace text after specific position
=SUBSTITUTE(A1, MID(A1, FIND("@", A1)+1, LEN(A1)), "newdomain.com")
// Changes email domain while preserving username

// Conditional replacement based on position
=IF(FIND(".", A1)>5, SUBSTITUTE(A1, ".", "_"), A1)
// Only replaces periods that appear after position 5

// Replace between found delimiters
=SUBSTITUTE(B1, MID(B1, FIND("[", B1), FIND("]", B1)-FIND("[", B1)+1), "[REPLACED]")
// Replaces text within brackets
```

### [[CONCATENATE]]
Combines SUBSTITUTE results with other text elements for comprehensive text reconstruction. Together they enable complex text transformation and reformatting operations.

```spreadsheets
// Build formatted output after substitution
=CONCATENATE("Clean: ", SUBSTITUTE(A1, " ", ""), " | Original: ", A1)
// Shows both cleaned and original versions

// Chain multiple substitutions
=CONCATENATE(SUBSTITUTE(SUBSTITUTE(B1, " ", ""), "-", ""), "_formatted")
// Removes spaces and hyphens, adds suffix

// Create comparison display
=CONCATENATE("Before: ", C1, " | After: ", SUBSTITUTE(C1, "old", "new"))
// Shows before and after substitution results
```

## Commonly Used With Functions Examples

### Phone Number Standardization System
```spreadsheets
// Process various phone formats: "(555) 123-4567", "555.123.4567", "555 123 4567"

// Step 1: Remove all formatting characters
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", "")
// Result: "555-123-4567" or "555.123.4567" or "5551234567"

// Step 2: Remove remaining separators
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", ""), "-", ""), ".", "")
// Result: "5551234567"

// Step 3: Format consistently
=CONCATENATE("(", LEFT(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", ""), "-", ""), ".", ""), 3), ") ", MID(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", ""), "-", ""), ".", ""), 4, 3), "-", RIGHT(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", ""), "-", ""), ".", ""), 4))
// Result: "(555) 123-4567"

// Count cleaned digits for validation
=LEN(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), " ", ""), "-", ""), ".", ""))
// Should equal 10 for valid US phone number
```

### Data Import Cleaning Pipeline
```spreadsheets
// Clean imported text data: "  John,  Smith;  Manager  "

// Step 1: Replace semicolons with commas
=SUBSTITUTE(B1, ";", ",")
// Result: "  John,  Smith,  Manager  "

// Step 2: Replace multiple spaces with single spaces
=TRIM(SUBSTITUTE(SUBSTITUTE(B1, ";", ","), "  ", " "))
// Result: "John, Smith, Manager"

// Step 3: Remove all commas for single string
=SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(B1, ";", ","), "  ", " ")), ",", "")
// Result: "John Smith Manager"

// Step 4: Create structured format
=SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(B1, ";", ","), "  ", " ")), ", ", " | ")
// Result: "John | Smith | Manager"
```

### Email Address Processing
```spreadsheets
// Process email addresses: "User.Name@Company.Com"

// Convert to lowercase (combined with other functions)
=LOWER(C1)
// Result: "user.name@company.com"

// Replace dots in username with underscores
=SUBSTITUTE(C1, ".", "_", 1)
// Result: "User_Name@Company.Com" (only first dot)

// Standardize domain separator
=SUBSTITUTE(C1, "@", " AT ")
// Result: "User.Name AT Company.Com"

// Create masked version
=CONCATENATE(LEFT(C1, 2), SUBSTITUTE(MID(C1, 3, FIND("@", C1)-3), MID(C1, 3, FIND("@", C1)-3), "****"), RIGHT(C1, LEN(C1)-FIND("@", C1)+1))
// Result: "Us****@Company.Com"
```

### Content Template Processing
```spreadsheets
// Process template: "Dear [NAME], your order #[ORDER] is ready"

// Replace name placeholder
=SUBSTITUTE(D1, "[NAME]", "John Smith")
// Result: "Dear John Smith, your order #[ORDER] is ready"

// Replace order number placeholder  
=SUBSTITUTE(SUBSTITUTE(D1, "[NAME]", "John Smith"), "[ORDER]", "12345")
// Result: "Dear John Smith, your order #12345 is ready"

// Remove all placeholder brackets
=SUBSTITUTE(SUBSTITUTE(D1, "[", ""), "]", "")
// Result: "Dear NAME, your order #ORDER is ready"

// Replace multiple placeholders systematically
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(D1, "[NAME]", E1), "[ORDER]", F1), "[DATE]", G1)
// Uses values from other cells to replace all placeholders
```

### File Path Standardization
```spreadsheets
// Standardize file paths: "C:\\Users\\Name\\Documents\\file.txt"

// Convert backslashes to forward slashes
=SUBSTITUTE(E1, "\\", "/")
// Result: "C:/Users/Name/Documents/file.txt"

// Remove drive letter
=SUBSTITUTE(E1, LEFT(E1, 3), "")
// Result: "Users\\Name\\Documents\\file.txt"

// Replace spaces in path with underscores
=SUBSTITUTE(E1, " ", "_")
// Result: "C:\\Users\\Name\\Documents\\file.txt"

// Create web-friendly path
=LOWER(SUBSTITUTE(SUBSTITUTE(E1, "\\", "/"), " ", "_"))
// Result: "c:/users/name/documents/file.txt"

// Extract and clean filename
=SUBSTITUTE(RIGHT(E1, LEN(E1)-FIND("/", SUBSTITUTE(E1, "\\", "/"), LEN(SUBSTITUTE(E1, "\\", "/"))-LEN(SUBSTITUTE(SUBSTITUTE(E1, "\\", "/"), "/", ""))+1)), " ", "_")
// Extracts filename and replaces spaces with underscores
```
