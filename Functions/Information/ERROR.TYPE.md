---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- information
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- information
- excel
- sheets
---
# ERROR.TYPE

## ERROR.TYPE Description

Returns a numeric code corresponding to different Excel error values, enabling programmatic error handling and validation. ERROR.TYPE converts error values to numbers for conditional logic and error categorization.

> [!f(x)] ERROR.TYPE Syntax
>
> ```spreadsheets
> ERROR.TYPE(error_val)
> ```
>
> **Parameters:**
> - `error_val` (required): The error value to analyze and convert to numeric code

> [!f(x)] ERROR.TYPE Examples
>
> ```spreadsheets
> ERROR.TYPE(#NULL!) → 1
> // Null error detection
> 
> ERROR.TYPE(#DIV/0!) → 2
> // Division by zero error
> 
> ERROR.TYPE(#VALUE!) → 3
> // Value error identification
> 
> ERROR.TYPE(#REF!) → 4
> // Reference error detection
> 
> ERROR.TYPE(#NAME?) → 5
> // Name error recognition
> 
> ERROR.TYPE(#NUM!) → 6
> // Number error identification
> 
> ERROR.TYPE(#N/A) → 7
> // Not available error detection
>
> ```

## Use Cases

### [[Error handling automation]]
- **Implementation**: Create sophisticated error handling routines with specific responses to different error types

### [[Data validation systems]]
- **Implementation**: Build comprehensive validation systems that categorize and respond to different error conditions

### [[Quality control reporting]]
- **Implementation**: Generate detailed error reports categorizing issues by type and severity

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
