---
categories:
  - spreadsheet-functions
subCategories:
  - excel
  - sheets
topics:
  - text-manipulation
  - string-functions
subTopics:
  - text-joining
  - string-concatenation
  - data-combination
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - CONCAT
  - text-join
  - string-join
  - combine-text
tags:
  - text
  - concatenation
  - string-manipulation
  - data-merging
  - excel
  - google-sheets
---

# CONCATENATE

## Description

CONCATENATE is one of the most fundamental and widely-used text functions in spreadsheet applications, designed to join two or more text strings into a single continuous string. At its core, the function takes multiple arguments, whether they are literal text values enclosed in quotation marks, cell references containing text or numbers, or a combination of both, and combines them sequentially from left to right into one unified text string. The function preserves the exact order of the arguments as they are provided, making the sequence of inputs critically important for achieving the desired output. When working with CONCATENATE, each argument is treated as a text value, meaning that numbers, dates, and other data types are automatically converted to their text representations before being joined together.

The CONCATENATE function is particularly valuable when you need to combine data from multiple cells into a single cell for reporting, labeling, or data preparation purposes. Common use cases include creating full names from separate first name and last name columns, building complete addresses from street, city, state, and zip code fields, generating unique identifiers by combining product codes with serial numbers, constructing dynamic file paths or URLs, and preparing data for export to other systems that require specific text formats. The function is also frequently used in creating concatenated keys for VLOOKUP or INDEX/MATCH operations when matching on multiple criteria, as well as in generating dynamic text for labels, reports, and dashboards that combine static descriptive text with dynamic cell values.

There are several important gotchas and limitations to be aware of when using CONCATENATE. First, the function does not automatically insert spaces, commas, or any other separators between the joined text strings; you must explicitly include these as additional arguments or within the text strings themselves. Second, CONCATENATE treats empty cells as empty strings rather than generating errors, which can lead to unexpected results when some source cells are blank. Third, the function has a limit on the number of arguments it can accept: in Excel, you can include up to 255 arguments, while Google Sheets has a similar practical limit. Fourth, when concatenating numbers, be aware that numeric formatting such as currency symbols, percentage signs, or decimal places is lost because the underlying numeric value is converted to text, not the displayed formatted value. Fifth, CONCATENATE cannot accept a range reference as a single argument and concatenate all values within that range; each cell must be specified as a separate argument, which is a significant limitation that led to the creation of newer functions like CONCAT and TEXTJOIN.

Regarding platform differences, CONCATENATE is available in both Microsoft Excel and Google Sheets with essentially identical syntax and behavior, making it highly portable across platforms. However, Microsoft has marked CONCATENATE as a legacy function in newer versions of Excel (2016 and later), recommending the use of CONCAT or TEXTJOIN instead, though CONCATENATE remains fully functional for backward compatibility. The ampersand (&) operator provides an alternative method for concatenation that many users prefer for its brevity and readability, and it works identically in both Excel and Google Sheets. Google Sheets users should also be aware of the JOIN function, which is similar to TEXTJOIN but has been available in Sheets for longer. Both platforms support the use of CONCATENATE within array formulas and with other functions, though the specific behavior with dynamic arrays differs between Excel 365 (which has full dynamic array support) and Google Sheets (which handles arrays differently).

## Syntax

> [!f(x)] CONCATENATE Syntax
>
> ```excel
> =CONCATENATE(text1, [text2], [text3], ...)
> ```
>
> **Parameters:**
>
> | Parameter | Description | Required |
> |-----------|-------------|----------|
> | `text1` | The first text string, cell reference, or value to join. This is the starting point of the concatenated result and appears first in the output. Can be a literal text string in quotes, a cell reference, a number, or an expression that returns a value. | Yes |
> | `text2` | The second text string, cell reference, or value to join. This appears immediately after text1 in the result with no automatic spacing. | No |
> | `text3, ...` | Additional text strings, cell references, or values to join. Excel supports up to 255 total arguments; Google Sheets has similar limits. Each additional argument is appended to the end of the growing concatenated string. | No |

## Alternative Methods: The & Operator, CONCAT, and TEXTJOIN

### The Ampersand (&) Operator

The ampersand operator provides a more concise syntax for concatenation and is often preferred by experienced users:

```excel
=A1 & B1 & C1
=A1 & " " & B1          // With space separator
="Total: " & SUM(A1:A10)  // Combining text with formula results
```

The & operator is functionally equivalent to CONCATENATE but offers several advantages: shorter formulas, easier readability for simple concatenations, and the ability to use inline without function parentheses. However, for very complex concatenations with many elements, CONCATENATE or TEXTJOIN may be more readable.

### CONCAT Function (Excel 2016+, Google Sheets)

CONCAT is the modern replacement for CONCATENATE in Excel, with the key advantage of accepting range references:

```excel
=CONCAT(A1:A10)         // Joins all values in the range
=CONCAT(A1, B1, C1)     // Works like CONCATENATE
```

### TEXTJOIN Function (Excel 2016+, Google Sheets)

TEXTJOIN is the most powerful concatenation function, offering delimiter insertion and empty cell handling:

```excel
=TEXTJOIN(", ", TRUE, A1:A10)    // Joins with comma-space, ignores empty cells
=TEXTJOIN("-", FALSE, A1:C1)      // Joins with hyphen, includes empty cells
```

## Examples

### Example 1: Basic Text Concatenation
```excel
=CONCATENATE("Hello", "World")
```
**Result:** `HelloWorld`

**Explanation:** This most basic example demonstrates how CONCATENATE joins two literal text strings. Notice that the function does not automatically add any space or separator between the strings, resulting in them being directly adjacent. Both arguments are enclosed in double quotation marks because they are literal text values rather than cell references.

---

### Example 2: Adding a Space Separator
```excel
=CONCATENATE("Hello", " ", "World")
```
**Result:** `Hello World`

**Explanation:** To include a space between concatenated values, you must explicitly add it as a separate argument. Here, the middle argument is a space character enclosed in quotation marks. This is one of the most common patterns in CONCATENATE usage, as forgetting the separator is a frequent mistake.

---

### Example 3: Combining Cell References
```excel
=CONCATENATE(A1, B1, C1)
```
Where A1="John", B1=" ", C1="Smith"

**Result:** `John Smith`

**Explanation:** When using cell references, you do not use quotation marks around the reference. The function retrieves the value from each cell and joins them in order. Here, cell B1 contains the space character, though it is more common to include the space as a literal string argument.

---

### Example 4: Creating Full Names from Separate Columns
```excel
=CONCATENATE(A2, " ", B2)
```
Where A2="Jane", B2="Doe"

**Result:** `Jane Doe`

**Explanation:** This is the classic use case for CONCATENATE, combining first and last names with a space separator. The space is provided as a literal text argument between the two cell references. This pattern is used millions of times daily across spreadsheets worldwide.

---

### Example 5: Building Complete Addresses
```excel
=CONCATENATE(A2, ", ", B2, ", ", C2, " ", D2)
```
Where A2="123 Main St", B2="Springfield", C2="IL", D2="62701"

**Result:** `123 Main St, Springfield, IL 62701`

**Explanation:** Address concatenation demonstrates using multiple separator styles within a single formula. The street and city are separated by comma-space, city and state by comma-space, and state and zip code by just a space. This matches standard US address formatting conventions.

---

### Example 6: Concatenating Numbers
```excel
=CONCATENATE(2024, "-", 1, "-", 15)
```
**Result:** `2024-1-15`

**Explanation:** CONCATENATE automatically converts numeric values to text. Notice that the number 1 becomes "1" without leading zeros. If you need formatted numbers (like "01" for January), you must either use TEXT function to format first or store the values as text.

---

### Example 7: Combining Text with Formula Results
```excel
=CONCATENATE("Total Sales: $", SUM(B2:B100))
```
Where SUM(B2:B100) equals 15750

**Result:** `Total Sales: $15750`

**Explanation:** You can embed other functions as arguments within CONCATENATE. The SUM function is evaluated first, and its numeric result is then converted to text and concatenated. Note that no comma formatting is applied to the number; for formatted output, wrap the SUM in a TEXT function.

---

### Example 8: Creating Unique Identifiers
```excel
=CONCATENATE(A2, "-", TEXT(B2, "0000"), "-", C2)
```
Where A2="PROD", B2=42, C2="A"

**Result:** `PROD-0042-A`

**Explanation:** This example shows creating a product code by combining a category prefix, a zero-padded number, and a variant letter. The TEXT function is nested within CONCATENATE to format the number with leading zeros. This is a common pattern for generating SKUs, serial numbers, or reference codes.

---

### Example 9: Building Dynamic File Paths
```excel
=CONCATENATE("C:\Reports\", A2, "\", B2, "_Report.xlsx")
```
Where A2="2024", B2="Q1"

**Result:** `C:\Reports\2024\Q1_Report.xlsx`

**Explanation:** CONCATENATE excels at building file paths or URLs dynamically. The backslash characters are part of the literal text strings. Be careful with special characters; in this case, backslashes work fine, but other characters might require different handling depending on how the path will be used.

---

### Example 10: Concatenating with Line Breaks (Excel)
```excel
=CONCATENATE(A2, CHAR(10), B2, CHAR(10), C2)
```
Where A2="Line 1", B2="Line 2", C2="Line 3"

**Result:**
```
Line 1
Line 2
Line 3
```

**Explanation:** Using CHAR(10) inserts a line break character (newline) in Excel. For this to display properly, the cell must have "Wrap Text" formatting enabled. This technique is useful for creating multi-line labels or address blocks within a single cell. In Google Sheets, CHAR(10) works the same way.

---

### Example 11: Handling Empty Cells
```excel
=CONCATENATE(A2, " ", B2, " ", C2)
```
Where A2="John", B2="" (empty), C2="Doe"

**Result:** `John  Doe`

**Explanation:** When a referenced cell is empty, CONCATENATE treats it as an empty string, not an error. This results in double spaces in the output where the empty cell value would have appeared. To handle this gracefully, consider using IF statements or the TEXTJOIN function with its ignore_empty parameter.

---

### Example 12: Creating Email Addresses
```excel
=CONCATENATE(LOWER(LEFT(A2,1)), LOWER(B2), "@company.com")
```
Where A2="John", B2="Smith"

**Result:** `jsmith@company.com`

**Explanation:** This formula generates email addresses in the common first initial + last name format. The LEFT function extracts the first character, LOWER converts both parts to lowercase, and all pieces are concatenated with the domain. This demonstrates nesting multiple functions within CONCATENATE.

---

### Example 13: Using the Ampersand Alternative
```excel
=A2 & " " & B2 & " (" & C2 & ")"
```
Where A2="John", B2="Smith", C2="Manager"

**Result:** `John Smith (Manager)`

**Explanation:** The ampersand operator achieves the same result as CONCATENATE but with more compact syntax. Many users find this more readable, especially for simple concatenations. The formula is equivalent to =CONCATENATE(A2, " ", B2, " (", C2, ")") but requires less typing.

---

### Example 14: Concatenating Dates
```excel
=CONCATENATE("Report Date: ", TEXT(A2, "MMMM D, YYYY"))
```
Where A2 contains the date 1/15/2024

**Result:** `Report Date: January 15, 2024`

**Explanation:** When concatenating dates, always use the TEXT function to control the date format. Without TEXT, the date would display as its underlying serial number (e.g., 45306). The TEXT function converts the date to a formatted text string before concatenation.

---

### Example 15: Building SQL-Style Conditions
```excel
=CONCATENATE("WHERE ", A2, " = '", B2, "'")
```
Where A2="CustomerID", B2="CUST001"

**Result:** `WHERE CustomerID = 'CUST001'`

**Explanation:** CONCATENATE is useful for building dynamic query strings or code snippets. This example creates a SQL WHERE clause by combining a field name and value with proper SQL syntax including single quotes around the string value.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Attempting to concatenate an error value from another cell | Use IFERROR to handle source cell errors before concatenation: `=CONCATENATE(IFERROR(A1,""), B1)` |
| `#NAME?` | Misspelling the function name or missing quotation marks around text | Verify spelling as CONCATENATE and ensure all literal text is enclosed in double quotes |
| `No error, but missing spaces` | Forgetting to add separator characters between arguments | Explicitly add space or delimiter arguments: `=CONCATENATE(A1, " ", B1)` |
| `Numbers display without formatting` | Numeric values lose their cell formatting when converted to text | Use TEXT function to preserve formatting: `=CONCATENATE("$", TEXT(A1, "#,##0.00"))` |
| `#REF!` | Referenced cell has been deleted | Update the formula to reference existing cells or use INDIRECT for dynamic references |
| `Dates display as numbers` | Date values show as serial numbers instead of formatted dates | Wrap date values in TEXT function: `=CONCATENATE(TEXT(A1, "MM/DD/YYYY"))` |
| `Double spaces or extra delimiters` | Empty cells in the source data create gaps | Use TEXTJOIN with ignore_empty=TRUE, or add IF conditions to check for empty cells |
| `Formula too long/complex` | Exceeding practical formula length limits or 255 argument maximum | Break into multiple cells with intermediate concatenations, or use TEXTJOIN with ranges |
| `Circular reference error` | Formula references a cell that depends on the formula cell | Restructure the formula to avoid self-referencing chains |
| `Text truncated at 32,767 characters` | Excel/Sheets cell character limit exceeded | Split the result across multiple cells or reconsider the data structure |

## Use Cases

### [[Customer Data Management]]
- **Implementation**: Combine customer first names, last names, titles, and suffixes into properly formatted full names for mail merge, reports, and CRM systems. Use conditional logic to handle missing middle names or suffixes gracefully. Implement name formatting that respects cultural naming conventions by adjusting the order of name components.
- **Business Application**: Customer service teams need properly formatted names for personalized communications. Marketing departments require consistent name formatting for campaign materials. Legal and compliance teams need accurately combined names for official documents. Sales teams benefit from professional name displays in proposals and contracts.
- **Technical Details**: Handle edge cases such as single-name individuals, hyphenated surnames, generational suffixes (Jr., III), and professional titles (Dr., Prof.). Use TRIM to remove excess spaces when some fields are empty. Consider using PROPER function to ensure consistent capitalization. Implement logic to handle maiden names or alternate names in parentheses when required.

### [[Address Standardization]]
- **Implementation**: Concatenate street address, apartment/suite numbers, city, state, and postal code into properly formatted mailing addresses. Include appropriate punctuation and line breaks for label printing. Handle international addresses with varying format requirements including country names and different postal code formats.
- **Business Application**: Shipping departments need correctly formatted addresses for label printing and carrier systems. Accounts receivable requires standardized addresses for invoice generation. Marketing teams need properly formatted addresses for direct mail campaigns. Compliance teams need consistent address formatting for regulatory filings.
- **Technical Details**: Use CHAR(10) for line breaks within a single cell when creating multi-line address blocks. Apply UPPER function to state abbreviations and postal codes where appropriate. Implement validation to ensure all required address components are present before concatenation. Handle special cases like PO boxes, military APO/FPO addresses, and international formats with country-specific rules.

### [[Product Code Generation]]
- **Implementation**: Generate standardized product codes, SKUs, or serial numbers by combining category codes, sequential numbers, date stamps, and variant identifiers. Use TEXT function to ensure consistent number formatting with leading zeros. Implement validation to prevent duplicate code generation.
- **Business Application**: Inventory management systems require unique, meaningful product identifiers. Warehouse operations need scannable codes that convey product information. Purchasing departments need standardized part numbers for ordering. Quality control requires traceable serial numbers linking products to manufacturing batches.
- **Technical Details**: Design code structure to encode meaningful information (e.g., first two characters for category, four digits for sequence, two characters for year). Use TEXT(number, "0000") to ensure consistent digit counts with leading zeros. Implement check digits using MOD calculations for code validation. Create lookup tables for category abbreviations and ensure codes meet barcode scanner requirements.

### [[Dynamic Report Generation]]
- **Implementation**: Build dynamic titles, headers, and labels for reports by combining static text with cell values for dates, periods, department names, and metric descriptions. Create flexible templates where concatenated text automatically updates when source data changes. Generate context-appropriate labels based on report parameters.
- **Business Application**: Financial reporting requires period-specific titles like "Q3 2024 Revenue Report". Departmental dashboards need dynamic headers showing the selected department and date range. Executive summaries require labels that automatically reflect the most recent data period. Audit trails need timestamped labels for version control.
- **Technical Details**: Combine CONCATENATE with TEXT for formatted dates and numbers in labels. Use cell references for department names and periods to enable single-source updates. Implement named ranges for commonly concatenated values to simplify formula maintenance. Create template cells that combine multiple data points into presentation-ready text strings. Use CHAR(10) for multi-line headers when needed.

## Platform Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| **Basic Functionality** | Fully supported in all versions | Fully supported |
| **Maximum Arguments** | 255 arguments | Similar practical limit |
| **Range as Single Argument** | Not supported; use CONCAT or TEXTJOIN | Not supported; use CONCAT, JOIN, or TEXTJOIN |
| **Function Status** | Marked as legacy; CONCAT/TEXTJOIN recommended | Fully supported alongside alternatives |
| **CONCAT Function** | Available in Excel 2016+ and Microsoft 365 | Available; accepts ranges |
| **TEXTJOIN Function** | Available in Excel 2016+ and Microsoft 365 | Available with full functionality |
| **JOIN Function** | Not available | Available; similar to TEXTJOIN but older |
| **Line Break Character** | CHAR(10) | CHAR(10) |
| **Array Formula Behavior** | Dynamic arrays in Excel 365; Ctrl+Shift+Enter in older versions | Automatic array expansion in many cases |
| **Maximum Result Length** | 32,767 characters per cell | 50,000 characters per cell |
| **Ampersand Operator** | Fully supported and commonly used | Fully supported and commonly used |
| **Performance** | Generally faster with local processing | Dependent on cloud processing; may be slower for large datasets |
| **Error Propagation** | Any error argument produces error result | Any error argument produces error result |

**Key Recommendations by Platform:**

For Excel 2016+ and Microsoft 365:
- Prefer CONCAT when you need to concatenate ranges
- Prefer TEXTJOIN when you need delimiters or empty cell handling
- Use CONCATENATE only for backward compatibility with older Excel versions
- The & operator remains excellent for simple, readable concatenations

For Google Sheets:
- CONCATENATE works well for explicit cell references
- Use TEXTJOIN for delimiter-separated lists with empty cell handling
- JOIN function is also available as an alternative
- The & operator is equally effective and often preferred for simplicity

## Tips and Best Practices

1. **Always Include Explicit Separators**: Never assume CONCATENATE will add spaces or other delimiters between values. Always include separator arguments exactly where needed, such as `=CONCATENATE(A1, " ", B1)` rather than hoping spaces will appear automatically. This is the most common mistake with CONCATENATE.

2. **Use TEXT for Formatted Numbers and Dates**: When concatenating numbers that need specific formatting (currency, percentages, decimal places) or dates that should display in a particular format, always wrap the value in a TEXT function first. For example, `=CONCATENATE("Total: ", TEXT(A1, "$#,##0.00"))` preserves currency formatting.

3. **Consider TEXTJOIN for Complex Scenarios**: If you find yourself writing long CONCATENATE formulas with many repeated delimiters or needing to skip empty cells, switch to TEXTJOIN. It handles delimiters automatically and can ignore empty cells, resulting in cleaner formulas and output.

4. **Handle Empty Cells Proactively**: Use IF statements to check for empty cells when their presence would create awkward results: `=CONCATENATE(A1, IF(B1="", "", " " & B1))`. This prevents double spaces or trailing delimiters when source data is incomplete.

5. **Use Named Ranges for Readability**: When concatenating values used across multiple formulas, consider using named ranges. `=CONCATENATE(FirstName, " ", LastName)` is much more readable than `=CONCATENATE(A1, " ", B1)`, especially in complex workbooks.

6. **Prefer the Ampersand for Simple Cases**: For straightforward concatenations with just a few values, the & operator is often more readable: `=A1 & " " & B1` instead of `=CONCATENATE(A1, " ", B1)`. Reserve CONCATENATE for cases where the function syntax improves clarity or when building formulas programmatically.

7. **Use TRIM to Clean Results**: When source data might have leading or trailing spaces, wrap your CONCATENATE in TRIM: `=TRIM(CONCATENATE(A1, " ", B1))`. This ensures clean output even if source cells have inconsistent spacing.

8. **Document Complex Formulas**: When building elaborate concatenation formulas for business-critical outputs like product codes or addresses, add a comment in an adjacent cell explaining the format structure. This helps future maintainers understand the expected output format.

## Related Functions

### Similar Functions

| Function | Description | Key Difference from CONCATENATE |
|----------|-------------|--------------------------------|
| [[CONCAT]] | Joins text strings; accepts ranges | Modern replacement that can accept a range like A1:A10 as a single argument instead of listing each cell |
| [[TEXTJOIN]] | Joins text with delimiter and empty cell handling | Most powerful option; automatically inserts delimiters and can ignore empty cells |
| [[JOIN]] | Joins array elements with delimiter (Google Sheets) | Sheets-specific function that predates TEXTJOIN; useful for array results |
| [[& Operator]] | Inline concatenation operator | Shorter syntax; `=A1 & B1` is equivalent to `=CONCATENATE(A1, B1)` |
| [[REPT]] | Repeats text a specified number of times | Creates repeated strings; useful for padding or visual elements |
| [[TEXT]] | Converts values to text with formatting | Formats numbers/dates as text for proper concatenation display |

### Commonly Used Together

**[[TEXT]]** - Format numbers and dates before concatenation

*Use TEXT with CONCATENATE to preserve number and date formatting:*
```excel
=CONCATENATE("Invoice Date: ", TEXT(A1, "MMMM D, YYYY"), " - Amount: ", TEXT(B1, "$#,##0.00"))
```
This formula creates a formatted string like "Invoice Date: January 15, 2024 - Amount: $1,234.56" by properly formatting the date and currency values before joining them.

**[[IF]]** - Conditional concatenation logic

*Use IF with CONCATENATE to handle optional or conditional values:*
```excel
=CONCATENATE(A1, " ", B1, IF(C1<>"", " " & C1, ""))
```
This formula creates a full name, but only adds the suffix in C1 if it is not empty, avoiding trailing spaces when no suffix exists.

**[[TRIM]]** - Clean up concatenation results

*Use TRIM with CONCATENATE to remove excess spaces:*
```excel
=TRIM(CONCATENATE(A1, " ", B1, " ", C1))
```
This formula joins three values with spaces, then removes any leading, trailing, or doubled spaces from the result caused by empty source cells.

**[[LEFT, RIGHT, MID]]** - Extract portions of text for concatenation

*Use text extraction functions with CONCATENATE to build new strings from parts of existing ones:*
```excel
=CONCATENATE(LEFT(A1, 3), "-", MID(A1, 4, 2), "-", RIGHT(A1, 4))
```
This formula reformats a 9-character string by inserting hyphens, creating output like "ABC-12-3456" from "ABC123456".

**[[LOWER, UPPER, PROPER]]** - Standardize text case before concatenation

*Use case functions with CONCATENATE for consistent formatting:*
```excel
=CONCATENATE(PROPER(A1), " ", PROPER(B1))
```
This formula combines first and last names while ensuring proper capitalization, producing "John Smith" even if source cells contain "JOHN" and "smith".

**[[IFERROR]]** - Handle errors in source cells

*Use IFERROR with CONCATENATE to prevent error propagation:*
```excel
=CONCATENATE(IFERROR(A1, "N/A"), " - ", IFERROR(B1, "N/A"))
```
This formula substitutes "N/A" for any error values in the source cells, ensuring the concatenation completes even when source data has issues.

## Official Documentation

- **Microsoft Excel**: [CONCATENATE function](https://support.microsoft.com/en-us/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d)
- **Microsoft Excel**: [CONCAT function](https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2)
- **Microsoft Excel**: [TEXTJOIN function](https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c9-0c076023f0ad)
- **Google Sheets**: [CONCATENATE function](https://support.google.com/docs/answer/3094123)
- **Google Sheets**: [TEXTJOIN function](https://support.google.com/docs/answer/7013992)
- **Google Sheets**: [JOIN function](https://support.google.com/docs/answer/3094077)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| Excel 2003 | 2003 | Original function with support for up to 30 arguments |
| Excel 2007 | 2007 | Argument limit increased to 255 |
| Excel 2016 | 2016 | CONCAT and TEXTJOIN introduced as modern alternatives; CONCATENATE marked as legacy |
| Excel 365 | 2018+ | Dynamic array support added; all concatenation functions work with spilled ranges |
| Google Sheets | 2006 | Original release with full CONCATENATE support |
| Google Sheets | 2016 | TEXTJOIN function added |
| Google Sheets | 2019 | Performance improvements for large-scale concatenation operations |
| Excel for Web | 2020 | Full parity with desktop CONCATENATE, CONCAT, and TEXTJOIN |
| Excel 365 | 2023 | Continued optimization for dynamic array scenarios |
