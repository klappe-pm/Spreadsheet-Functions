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
# WORKDAY.INTL

## WORKDAY.INTL Description

Returns a date that is a specified number of working days before or after a start date, using custom weekend definitions and holiday exclusions. WORKDAY.INTL enables international scheduling with flexible weekend patterns.

> [!f(x)] WORKDAY.INTL Syntax
>
> ```spreadsheets
> WORKDAY.INTL(start_date, days, [weekend], [holidays])
> ```
>
> **Parameters:**
> - `start_date` (required): Starting date for the calculation
> - `days` (required): Number of working days to add (positive) or subtract (negative)
> - `weekend` (optional): Weekend pattern code or custom string defining non-working days
> - `holidays` (optional): Array or range of holiday dates to exclude from working days

> [!f(x)] WORKDAY.INTL Examples
>
> ```spreadsheets
> WORKDAY.INTL(DATE(2024,1,1), 10) → date 10 business days after Jan 1
> // Basic workday calculation
> 
> WORKDAY.INTL(TODAY(), 5, 2) → 5 working days ahead with Sun-Mon weekends
> // Custom weekend pattern
> 
> WORKDAY.INTL(A1, -3, "0000001") → 3 working days before with Sunday-only weekend
> // Backward calculation with custom weekend
> 
> WORKDAY.INTL(A1, 7, 1, B1:B5) → 7 working days ahead excluding holidays
> // Forward calculation with holiday exclusions
>
> ```

## Use Cases

### [[International deadline management]]
- **Implementation**: Calculate project deadlines and milestones respecting global business calendars

### [[Cross-cultural scheduling]]
- **Implementation**: Schedule meetings, deliveries, and events across different international weekend patterns

### [[Global contract management]]
- **Implementation**: Calculate contract terms, payment dates, and delivery schedules for international agreements

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
