---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- datetime
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- datetime
- excel
- sheets
---
# DAYS360

## DAYS360 Description

Calculates the number of days between two dates based on a 360-day year (30 days per month), commonly used in financial calculations for interest and bond calculations.

> [!f(x)] DAYS360 Syntax
>
> ```spreadsheets
> DAYS360(start_date, end_date, [method])
> ```
>
> **Parameters:**
> - `start_date` (required): Starting date for the calculation
> - `end_date` (required): Ending date for the calculation
> - `method` (optional): FALSE for US (NASD) method, TRUE for European method

> [!f(x)] DAYS360 Examples
>
> ```spreadsheets
> DAYS360(DATE(2024,1,1), DATE(2024,12,31)) → 360
> // Full year calculation
> 
> DAYS360(A1, B1, FALSE) → days using US method
> // US financial calculation method
> 
> DAYS360(A1, B1, TRUE) → days using European method
> // European calculation method
> 
> DAYS360(DATE(2024,1,15), DATE(2024,3,15)) → 60
> // Two-month period calculation
>
> ```

## Use Cases

### [[Financial interest calculations]]
- **Implementation**: Calculate interest periods for loans, bonds, and investment products using standardized 360-day years

### [[Bond trading and valuation]]
- **Implementation**: Determine accrued interest and pricing for fixed-income securities using financial market conventions

### [[Corporate finance analysis]]
- **Implementation**: Analyze cash flows, debt service, and financial obligations using standard financial calendar assumptions

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
