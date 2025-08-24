---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- google-specific
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- google specific
- excel
- sheets
---
# SPLIT

## SPLIT Description

Splits text around a specified character or string and returns the parts in separate cells. SPLIT enables text parsing and data extraction from delimited strings.

> [!f(x)] SPLIT Syntax
>
> ```spreadsheets
> SPLIT(text, delimiter, [split_by_each], [remove_empty_text])
> ```
>
> **Parameters:**
> - `text` (required): The text to split into separate parts
> - `delimiter` (required): Character or string to split by
> - `split_by_each` (optional): TRUE to split by each character in delimiter, FALSE to split by entire delimiter string
> - `remove_empty_text` (optional): TRUE to remove empty text entries from results

> [!f(x)] SPLIT Examples
>
> ```spreadsheets
> SPLIT("apple,banana,cherry", ",") → three cells: apple, banana, cherry
> // Basic comma splitting
> 
> SPLIT("John Doe", " ") → two cells: John, Doe
> // Space delimiter
> 
> SPLIT("data|more|info", "|") → three cells with pipe delimiter
> // Custom delimiter
> 
> SPLIT(A1, ",", FALSE, TRUE) → split by comma, remove empty entries
> // Advanced options
>
> ```

## Use Cases

### [[Data import processing]]
- **Implementation**: Parse imported CSV data and delimited text files into structured columns

### [[Name and address parsing]]
- **Implementation**: Split full names into first/last names and addresses into components

### [[Tag and category processing]]
- **Implementation**: Extract and organize tags, categories, or keywords from delimited strings

## Related

### Similar Functions

- [[RELATED1]] - Description of relationship
- [[RELATED2]] - Description of relationship
- [[RELATED3]] - Description of relationship

### Commonly Used With Functions

- [[IF]] - Conditional logic and error handling
- [[IFERROR]] - Error handling and validation
- [[INDEX]] - Data retrieval and reference operations
- [[MATCH]] - Lookup and positioning functions
