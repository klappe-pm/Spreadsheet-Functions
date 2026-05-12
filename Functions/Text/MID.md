---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- text
subTopics:
- string-extraction
- text-parsing
- character-manipulation
- substring-extraction
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Middle Characters
- Mid Extract
- Extract Middle
- Substring
- Mid String
tags:
- text
- extraction
- parsing
- substring
- mid-characters
- positional-extraction
---

# MID

## Description

**MID** extracts a specified number of characters from any position within a text string. While LEFT works from the beginning and RIGHT works from the end, MID gives you surgical precision to pull characters from anywhere in between. Specify where to start and how many characters to grab, and MID delivers exactly that slice of text. This makes it indispensable for parsing structured data like fixed-width files, extracting components from formatted strings, and isolating specific segments of text.

The function requires three parameters: the text, the starting position (1-based, meaning the first character is position 1), and the number of characters to extract. Unlike LEFT and RIGHT which have optional character counts defaulting to 1, MID requires all three arguments. This explicitness makes MID formulas self-documenting, clearly communicating what portion of the text is being extracted.

**Critical gotcha:** MID uses 1-based positioning, not 0-based like many programming languages. The first character is position 1, not position 0. This trips up users coming from programming backgrounds. Also, if your start_num exceeds the string length, MID returns an empty string (not an error), and if start_num plus num_chars exceeds the string length, MID returns all characters from start_num to the end. These forgiving behaviors are usually helpful but can mask data issues.

**Platform consistency:** Excel and Google Sheets implement MID identically. Excel offers MIDB for byte-based extraction in double-byte character languages, while Sheets handles this transparently. For standard text processing, expect identical behavior across platforms.

## Syntax

> [!f(x)] MID Syntax
>
> ```
> =MID(text, start_num, num_chars)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `text` | Yes | The text string containing the characters you want to extract. Can be a literal string in quotes, a cell reference, or a formula that returns text. |
| `start_num` | Yes | The position of the first character to extract. The first character in text is position 1. Must be at least 1. |
| `num_chars` | Yes | The number of characters to extract. Must be zero or positive. If zero, returns empty string. |

### Return Value

Returns a text string containing the specified number of characters starting from the specified position. Returns text type even if the extracted content appears numeric. Returns empty string if start_num exceeds text length.

## Examples

> [!f(x)] MID Examples

### Example 1: Basic Middle Extraction
```
=MID("Hello World", 7, 5)
```
**Result:** "World"

**Explanation:** Starts at position 7 (the "W") and extracts 5 characters. This demonstrates the fundamental MID operation for extracting known segments from fixed positions.

---

### Example 2: Extracting Month from Date String
```
=MID("2025-08-17", 6, 2)
```
**Result:** "08"

**Explanation:** Extracts the month portion from an ISO date string. Position 6 is the first digit after "2025-", and we take 2 characters for the month.

---

### Example 3: Extracting Middle Initial from Name
```
=MID("John Q. Smith", 6, 1)
```
**Result:** "Q"

**Explanation:** Extracts just the middle initial from a formatted name. When data follows consistent formatting, MID enables precise character extraction.

---

### Example 4: Parsing Fixed-Width Data
```
=MID(A1, 11, 8)
```
Where A1 contains "CUS0001234SMITH   JOHN    2025"

**Result:** "SMITH   "

**Explanation:** Fixed-width file parsing where columns are defined by character positions. Last name starts at position 11 and occupies 8 characters including padding.

---

### Example 5: Extracting Phone Extension
```
=MID("1-800-555-1234 x567", 18, 3)
```
**Result:** "567"

**Explanation:** Extracts the extension number from a formatted phone string. When format is consistent, MID directly targets the extension portion.

---

### Example 6: Using FIND to Determine Start Position
```
=MID(A1, FIND("-", A1)+1, 5)
```
Where A1 contains "SKU-12345-BLUE"

**Result:** "12345"

**Explanation:** FIND locates the first hyphen, then MID starts one position after it. This pattern enables extraction relative to delimiters rather than fixed positions.

---

### Example 7: Extracting Domain from Email
```
=MID(A1, FIND("@", A1)+1, FIND(".", A1, FIND("@", A1))-FIND("@", A1)-1)
```
Where A1 contains "user@example.com"

**Result:** "example"

**Explanation:** Complex nested formula: finds @, then finds the dot after @, calculates the length between them. Extracts just the domain name portion.

---

### Example 8: Handling Start Position Beyond Text Length
```
=MID("Hello", 10, 3)
```
**Result:** "" (empty string)

**Explanation:** When start_num exceeds text length, MID returns empty string, not an error. This forgiving behavior is useful but can mask data problems.

---

### Example 9: Num_chars Exceeds Remaining Characters
```
=MID("Hello", 3, 100)
```
**Result:** "llo"

**Explanation:** If num_chars extends beyond the text end, MID returns all remaining characters without error. Useful when you want "everything from position X onward."

---

### Example 10: Zero Characters Requested
```
=MID("Hello", 3, 0)
```
**Result:** "" (empty string)

**Explanation:** Requesting zero characters returns an empty string. This can be useful in conditional formulas where you sometimes want no extraction.

---

### Example 11: Extracting Area Code (Without Parentheses)
```
=MID("(555) 123-4567", 2, 3)
```
**Result:** "555"

**Explanation:** Skips the opening parenthesis (position 1) and extracts just the 3-digit area code. Demonstrates skipping known prefix characters.

---

### Example 12: Parsing CSV Values (Second Field)
```
=MID(A1, FIND(",", A1)+1, FIND(",", A1, FIND(",", A1)+1)-FIND(",", A1)-1)
```
Where A1 contains "John,Smith,25"

**Result:** "Smith"

**Explanation:** Finds first comma, then finds second comma, calculates length between them. Extracts the second field from comma-separated data.

---

### Example 13: Combining with SUBSTITUTE for Complex Parsing
```
=MID(SUBSTITUTE(A1, "-", REPT(" ", 100)), 101, 100)
```
Where A1 contains "Part1-Part2-Part3"

**Result:** "Part2" (with spaces that can be TRIMmed)

**Explanation:** Advanced technique replacing delimiters with 100 spaces, then using fixed-width extraction. Gets the second segment regardless of segment lengths.

---

### Example 14: Extracting from Variable Position with LEN
```
=MID(A1, LEN(A1)-5, 3)
```
Where A1 contains "ProductCode123ABC"

**Result:** "3AB"

**Explanation:** Calculates start position relative to the end using LEN. Extracts 3 characters starting 6 positions from the end (position LEN-5 = character 6th from last).

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | start_num is less than 1 | Start position must be 1 or greater. Check formula logic that calculates start position. |
| `#VALUE!` | start_num or num_chars is non-numeric | Both arguments must be numbers. Check for text or errors feeding into these parameters. |
| `#VALUE!` | num_chars is negative | Number of characters must be 0 or positive. Use MAX(0, calculation) if dynamically computing. |
| `Empty result unexpected` | start_num exceeds text length | Verify text length with LEN() and ensure start position is valid. |
| `Wrong characters extracted` | Off-by-one error in position calculation | Remember MID is 1-based. The first character is position 1, not 0. |

## Use Cases

### [[Fixed-Width File Parsing]]

**Scenario:** Legacy systems export data in fixed-width format where each field occupies specific character positions. Parse customer records where ID is positions 1-6, name is 7-26, and balance is 27-36.

**Implementation:**
```
Customer ID: =TRIM(MID(A2, 1, 6))
Customer Name: =TRIM(MID(A2, 7, 20))
Account Balance: =VALUE(TRIM(MID(A2, 27, 10)))
```

**Business Application:** Enables spreadsheet-based processing of mainframe exports, EDI files, and legacy system data without specialized parsing tools. Critical for financial services and healthcare with legacy infrastructure.

**Technical Details:** TRIM removes padding spaces common in fixed-width formats. VALUE converts the balance to a number for calculations. Document column positions in a reference table for maintainability.

---

### [[VIN Number Decoding]]

**Scenario:** Vehicle Identification Numbers (VINs) encode manufacturer, model, and year in specific positions. Extract these components for fleet analysis.

**Implementation:**
```
Manufacturer: =MID(A2, 1, 3)
Vehicle Type: =MID(A2, 4, 5)
Check Digit: =MID(A2, 9, 1)
Model Year: =MID(A2, 10, 1)
Plant Code: =MID(A2, 11, 1)
Serial Number: =MID(A2, 12, 6)
```

**Business Application:** Fleet management, insurance processing, and automotive analytics. Enables filtering vehicles by manufacturer, identifying model years, and validating VIN authenticity via check digit.

**Technical Details:** VIN structure is standardized (ISO 3779). Position 10 encodes model year using letters and numbers representing years. Create a lookup table to convert the year code to an actual year value.

---

### [[Parsing Composite Keys]]

**Scenario:** Database exports use composite keys like "REGION-STORE-REGISTER-TRANS" (e.g., "NE-0047-03-12345"). Extract each component for hierarchical reporting.

**Implementation:**
```
Region: =LEFT(A2, FIND("-", A2)-1)
Store: =MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
Register: =MID(A2, FIND("-", A2, FIND("-", A2)+1)+1, 2)
Transaction: =RIGHT(A2, LEN(A2)-FIND("-", A2, FIND("-", A2, FIND("-", A2)+1)+1))
```

**Business Application:** Enable drill-down reporting from regional to store to register level. Identify high-performing stores, analyze transaction patterns by register, and support operational audits.

**Technical Details:** Multiple nested FIND calls locate successive delimiters. For complex parsing like this, consider TEXTSPLIT in modern Excel or helper columns that build progressively.

---

### [[Credit Card Number Formatting]]

**Scenario:** Credit card numbers are stored as 16-digit strings. Display them in standard 4-group format (XXXX-XXXX-XXXX-XXXX) for readability.

**Implementation:**
```
=MID(A2,1,4) & "-" & MID(A2,5,4) & "-" & MID(A2,9,4) & "-" & MID(A2,13,4)
```

**Business Application:** Format payment data for invoices, receipts, and customer statements. Improves readability while maintaining full card number for processing.

**Technical Details:** Each MID extracts a 4-digit group, and concatenation with "&" joins them with hyphens. For security, combine with masking: first group + "-XXXX-XXXX-" + last group.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 onward)
- **MIDB function:** Excel provides MIDB for byte-based extraction in DBCS (double-byte character set) languages like Japanese, Chinese, and Korean
- **Behavior with numbers:** Automatically converts numbers to text before extraction
- **Maximum length:** Limited by cell character limit (32,767 characters)

### Google Sheets
- **Availability:** All versions
- **No MIDB equivalent:** Sheets handles multi-byte characters automatically without needing a separate function
- **Array formula support:** Works natively with ARRAYFORMULA for processing ranges
- **Behavior:** Identical to Excel for standard text operations

### Key Difference Alert
MIDB extracts by byte position rather than character position, important for languages where characters occupy multiple bytes. Google Sheets has no MIDB because it treats all text uniformly by character. When converting Excel MIDB formulas to Sheets, replace with MID and verify correct behavior with your specific multi-byte data.

## Tips and Best Practices

1. **Remember 1-based indexing:** The first character is position 1, not 0. If coming from programming, adjust your mental model accordingly.

2. **Use FIND or SEARCH for dynamic positions:** When data is not fixed-width, calculate start positions relative to delimiters: `=MID(A1, FIND("-", A1)+1, ...)`.

3. **Combine with LEN for end-relative extraction:** To start from a position relative to the end, use `=MID(A1, LEN(A1)-n, ...)` where n is how far from the end to start.

4. **Handle variable-length extractions:** Need everything from position X to the end? Use a large num_chars value like 9999, since MID returns remaining text if num_chars exceeds availability.

5. **Debug with LEN and manual verification:** When MID returns unexpected results, use LEN to verify text length and manually count character positions to find errors.

6. **Consider TEXTSPLIT for delimiter-based parsing:** Modern Excel and Sheets offer TEXTSPLIT, which is cleaner for delimiter-separated data than complex nested MID/FIND formulas.

7. **Document your position mappings:** When parsing fixed-width data, create a reference table showing field names, start positions, and lengths. This aids maintenance and debugging.

8. **Use helper columns for complex parsing:** Rather than cramming everything into one formula, use intermediate columns for each FIND result. Clearer, debuggable, and often faster.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[LEFT]] | Extracts characters from the beginning of text | When you always need the first N characters |
| [[RIGHT]] | Extracts characters from the end of text | When you always need the last N characters |
| [[TEXTAFTER]] | Extracts text after a specified delimiter | When parsing relative to a delimiter (cleaner syntax) |
| [[TEXTBEFORE]] | Extracts text before a specified delimiter | When extracting up to a delimiter |
| [[MIDB]] | Byte-based extraction (Excel only) | When working with double-byte character sets in Excel |

### Commonly Used Together

**[[FIND]]** - Locates position of a substring (case-sensitive)

*Combine with MID for delimiter-based extraction:*
```
=MID(A1, FIND("-", A1)+1, FIND("-", A1, FIND("-", A1)+1)-FIND("-", A1)-1)
```
Extracts text between the first and second hyphens. FIND provides the dynamic positions for MID.

---

**[[SEARCH]]** - Locates position of a substring (case-insensitive)

*Combine with MID when delimiter case varies:*
```
=MID(A1, SEARCH("id:", A1)+3, 6)
```
Finds "ID:" or "id:" or "Id:" and extracts the 6 characters following it.

---

**[[LEN]]** - Returns the length of a text string

*Combine with MID for end-relative positioning:*
```
=MID(A1, LEN(A1)-7, 4)
```
Calculates position relative to text end. Extracts 4 characters starting 8 positions from the end.

---

**[[TRIM]]** - Removes extra spaces from text

*Combine with MID when parsing padded fixed-width data:*
```
=TRIM(MID(A1, 20, 15))
```
Extracts a fixed-width field and removes padding spaces. Essential for clean data from legacy systems.

---

**[[VALUE]]** - Converts text to a number

*Combine with MID when extracting numeric data:*
```
=VALUE(MID(A1, 10, 8))
```
Extracts numeric text and converts to an actual number for calculations.

---

**[[SUBSTITUTE]]** - Replaces specific text within a string

*Combine with MID for advanced parsing:*
```
=TRIM(MID(SUBSTITUTE(A1, "-", REPT(" ", 50)), 51, 50))
```
Replaces delimiters with spaces to enable fixed-width extraction of variable-length segments.

## Official Documentation

- **Microsoft Excel:** [MID, MIDB functions](https://support.microsoft.com/en-us/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028)
- **Google Sheets:** [MID function](https://support.google.com/docs/answer/3094129)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2.0 (1987) | Original function, one of the earliest text functions |
| Excel 2007+ | All subsequent versions | No changes to core functionality |
| Excel 365 | Continuous updates | Works with dynamic arrays and spill ranges |
| Google Sheets | Original launch (2006) | Identical implementation to Excel |

---

*Last updated: 2026-01-10*
