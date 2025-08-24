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
# GET.WORKBOOK

## GET.WORKBOOK Description

Returns information about the current workbook's structure, properties, and metadata. GET.WORKBOOK provides comprehensive workbook details including worksheet names, cell references, and file properties for dynamic workbook analysis.

> [!f(x)] GET.WORKBOOK Syntax
>
> ```spreadsheets
> GET.WORKBOOK(type_num, [reference])
> ```
>
> **Parameters:**
> - `type_num` (required): Numeric code specifying the type of workbook information to return
> - `reference` (optional): Specific cell or range reference for detailed information

> [!f(x)] GET.WORKBOOK Examples
>
> ```spreadsheets
> GET.WORKBOOK(1) → workbook name
> // Basic workbook name retrieval
> 
> GET.WORKBOOK(4) → array of all worksheet names
> // Get all sheet names
> 
> GET.WORKBOOK(12, A1) → cell contents and formatting
> // Detailed cell information
> 
> GET.WORKBOOK(35) → current workbook file path
> // Full file path retrieval
>
> ```

## Use Cases

### [[Dynamic worksheet navigation]]
- **Implementation**: Create dynamic references to worksheets and cells based on workbook structure

### [[File management automation]]
- **Implementation**: Build automated file processing systems using workbook metadata

### [[Template validation]]
- **Implementation**: Verify workbook structure matches expected templates and standards

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
