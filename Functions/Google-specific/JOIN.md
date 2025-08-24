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
# JOIN

## JOIN Description

Concatenates elements of arrays or ranges with a specified delimiter, creating a single text string from multiple values.

> [!f(x)] JOIN Syntax
>
> ```spreadsheets
> JOIN(delimiter, value_or_array1, [value_or_array2, ...])
> ```
>
> **Parameters:**
> - `delimiter` (required): Text string to place between joined values
> - `value_or_array1` (required): First value, array, or range to join
> - `value_or_array2` (optional): Additional values, arrays, or ranges to join

> [!f(x)] JOIN Examples
>
> ```spreadsheets
> JOIN(",", A1:A5) → concatenates A1-A5 with commas
> // Range joining with commas
> 
> JOIN(" | ", "Name", B1, "Age", C1) → Name | John | Age | 25
> // Mixed value joining
> 
> JOIN("; ", A1:A3, D1:D3) → joins two ranges with semicolons
> // Multiple range joining
> 
> JOIN("", A1:A5) → concatenates without delimiter
> // No delimiter joining
>
> ```

## Use Cases

### [[Text construction]]
- **Implementation**: Build formatted text strings from multiple data sources and ranges

### [[Report generation]]
- **Implementation**: Create formatted summaries and descriptions by joining data elements

### [[Data export preparation]]
- **Implementation**: Prepare data for export by concatenating values with appropriate delimiters

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
