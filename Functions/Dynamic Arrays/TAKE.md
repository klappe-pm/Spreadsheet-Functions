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
- dynamic arrays
- excel
- sheets
---
# TAKE

## TAKE Description

Returns a specified number of rows or columns from the start or end of an array. TAKE enables precise array extraction for dynamic data analysis and reporting.

> [!f(x)] TAKE Syntax
>
> ```spreadsheets
> TAKE(array, rows, [columns])
> ```
>
> **Parameters:**
> - `array` (required): The array or range from which to extract data
> - `rows` (required): Number of rows to return (positive from start, negative from end)
> - `columns` (optional): Number of columns to return (positive from start, negative from end)

> [!f(x)] TAKE Examples
>
> ```spreadsheets
> TAKE(A1:E10, 5) → first 5 rows of the range
> // Extract top rows
> 
> TAKE(A1:E10, -3) → last 3 rows of the range
> // Extract bottom rows
> 
> TAKE(A1:E10, 5, 2) → first 5 rows and 2 columns
> // Extract top-left subset
> 
> TAKE(A1:E10, -2, -1) → last 2 rows and last column
> // Extract bottom-right subset
>
> ```

## Use Cases

### [[Dynamic reporting]]
- **Implementation**: Create reports showing top or bottom performers, recent entries, or key metrics

### [[Data sampling]]
- **Implementation**: Extract representative samples from large datasets for analysis or testing

### [[Dashboard creation]]
- **Implementation**: Build dynamic dashboards showing latest data points or trending information

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
