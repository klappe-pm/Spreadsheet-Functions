---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- dynamic-arrays
- excel
- sheets
---
# FILTER

## FILTER Description

Returns a filtered array based on criteria you define, showing only rows that meet specified conditions. FILTER enables dynamic data extraction without helper columns.

> [!f(x)] FILTER Syntax
>
> ```spreadsheets
> FILTER(array, include, [if_empty])
> ```
>
> **Parameters:**
> - `array` (required): The array or range to filter
> - `include` (required): Boolean array indicating which rows to include
> - `if_empty` (optional): Value to return if no items meet the criteria

> [!f(x)] FILTER Examples
>
> ```spreadsheets
> FILTER(A1:C10, B1:B10>100) → rows where column B > 100
> // Numeric filtering
> 
> FILTER(A1:C10, C1:C10="Active") → rows where column C equals Active
> // Text filtering
> 
> FILTER(A1:C10, (B1:B10>50)*(C1:C10<200)) → multiple conditions
> // Complex criteria
> 
> FILTER(A1:C10, B1:B10>100, "No results") → custom empty message
> // Error handling
>
> ```

## Use Cases

### [[Dynamic data analysis]]
- **Implementation**: Create live filtered views of data that automatically update when source data changes

### [[Conditional reporting]]
- **Implementation**: Generate reports showing only data that meets specific business criteria

### [[Data validation]]
- **Implementation**: Extract and analyze subsets of data for quality control and validation processes

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
