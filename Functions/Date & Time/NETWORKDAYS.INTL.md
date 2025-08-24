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
# NETWORKDAYS.INTL

## NETWORKDAYS.INTL Description

Calculates the number of working days between two dates using custom weekend definitions and holiday exclusions. NETWORKDAYS.INTL provides international flexibility for business day calculations with customizable weekend patterns.

> [!f(x)] NETWORKDAYS.INTL Syntax
>
> ```spreadsheets
> NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
> ```
>
> **Parameters:**
> - `start_date` (required): Starting date for the calculation period
> - `end_date` (required): Ending date for the calculation period
> - `weekend` (optional): Weekend pattern code or custom string defining non-working days
> - `holidays` (optional): Array or range of holiday dates to exclude from working days

> [!f(x)] NETWORKDAYS.INTL Examples
>
> ```spreadsheets
> NETWORKDAYS.INTL(DATE(2024,1,1), DATE(2024,1,31)) → 23
> // January 2024 business days
> 
> NETWORKDAYS.INTL(A1, B1, 2) → working days with Sunday-Monday weekends
> // Custom weekend pattern
> 
> NETWORKDAYS.INTL(A1, B1, "0000001") → working days with Sunday only weekend
> // Custom weekend string
> 
> NETWORKDAYS.INTL(A1, B1, 1, C1:C10) → working days excluding holidays
> // Business days with holiday exclusions
>
> ```

## Use Cases

### [[International project management]]
- **Implementation**: Calculate project timelines respecting different cultural weekend patterns and holidays

### [[Payroll calculations]]
- **Implementation**: Compute working days for salary, overtime, and benefit calculations across different regions

### [[Service level agreements]]
- **Implementation**: Calculate response times and delivery dates considering international business calendars

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
