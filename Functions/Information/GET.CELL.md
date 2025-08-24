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
# GET.CELL

## GET.CELL Description

Returns detailed formatting and property information about a specific cell, including formatting attributes, protection status, and display characteristics. GET.CELL provides comprehensive cell metadata for advanced formatting analysis.

> [!f(x)] GET.CELL Syntax
>
> ```spreadsheets
> GET.CELL(info_type, reference)
> ```
>
> **Parameters:**
> - `info_type` (required): Numeric code specifying the type of cell information to return
> - `reference` (required): Cell reference to analyze for property information

> [!f(x)] GET.CELL Examples
>
> ```spreadsheets
> GET.CELL(1, A1) → absolute reference
> // Get absolute cell reference
> 
> GET.CELL(3, A1) → column number
> // Extract column number
> 
> GET.CELL(4, A1) → row number
> // Extract row number
> 
> GET.CELL(6, A1) → TRUE if cell is locked
> // Check protection status
> 
> GET.CELL(11, A1) → number format
> // Get number format code
> 
> GET.CELL(19, A1) → font size
> // Get font size information
>
> ```

## Use Cases

### [[Format validation]]
- **Implementation**: Verify cell formatting matches required standards and specifications

### [[Dynamic formatting analysis]]
- **Implementation**: Analyze and report on formatting consistency across ranges and worksheets

### [[Protection audit]]
- **Implementation**: Review cell protection settings and security configurations

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
