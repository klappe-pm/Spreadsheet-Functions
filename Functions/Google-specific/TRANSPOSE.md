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
# TRANSPOSE

## TRANSPOSE Description

Converts rows to columns and columns to rows in an array or range, enabling data restructuring and analysis from different perspectives.

> [!f(x)] TRANSPOSE Syntax
>
> ```spreadsheets
> TRANSPOSE(array_or_range)
> ```
>
> **Parameters:**
> - `array_or_range` (required): The array or range to transpose

> [!f(x)] TRANSPOSE Examples
>
> ```spreadsheets
> TRANSPOSE(A1:C3) → converts 3x3 range from rows to columns
> // Basic matrix transpose
> 
> TRANSPOSE(A1:A5) → converts vertical list to horizontal
> // Vertical to horizontal
> 
> TRANSPOSE(1:1) → converts horizontal row to vertical column
> // Row to column conversion
>
> ```

## Use Cases

### [[Data restructuring]]
- **Implementation**: Convert data layouts between row-based and column-based structures for different analysis needs

### [[Report formatting]]
- **Implementation**: Transform data organization to match specific reporting and presentation requirements

### [[Matrix operations]]
- **Implementation**: Perform mathematical matrix operations and transformations for statistical analysis

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
