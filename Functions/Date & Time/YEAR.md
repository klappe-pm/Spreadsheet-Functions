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
---

# YEAR

## YEAR Description

YEAR extracts the year from a date as a four-digit number.

> [!f(x)] YEAR Syntax
>
> ```spreadsheets
> YEAR(serial_number)
> ```
>
> **Parameters:**
> - `serial_number` (required): Date from which to extract the year

> [!f(x)] YEAR Examples
>
> ```spreadsheets
> YEAR(TODAY()) → current_year // Current year
> 
> YEAR(A1) → year_value // Year from date in A1
> 
> YEAR("12/25/2023") → 2023 // Year from text date
> ```

## Use Cases

### [[Time Analysis]]
- **Implementation**: Calculate time intervals, aging analysis, and temporal patterns for business insights
- **Business Application**: Track project timelines, analyze seasonal patterns, and manage time-based processes
- **Technical Details**: Handle different date formats, account for time zones, and implement proper date arithmetic

### [[Scheduling]]
- **Implementation**: Calculate dates for scheduling, deadlines, and time-based planning activities
- **Business Application**: Manage project schedules, track milestones, and coordinate time-sensitive activities
- **Technical Details**: Account for business days, holidays, and working hours in calculations

### [[Performance Tracking]]
- **Implementation**: Measure performance over time periods and track trends for continuous improvement
- **Business Application**: Monitor KPIs, track progress against goals, and identify performance trends
- **Technical Details**: Implement proper time period calculations, handle data aggregation, and ensure accurate trending

## Related

### Similar Functions

- [[MONTH]] - Related date & time function for analytical calculations
- [[DAY]] - Related date & time function for analytical calculations
- [[DATE]] - Related date & time function for analytical calculations
- [[YEARFRAC]] - Related date & time function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with YEAR for conditional logic and decision making:*
```spreadsheets
=IF(YEAR(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies YEAR to a range and compares the result to a threshold, returning different text based on the condition

**[[TODAY]]** - Get current date for time-based calculations

*Use TODAY with YEAR for enhanced analytical workflows:*
```spreadsheets
=TODAY(YEAR(A1:A10))
```
This formula combines TODAY and YEAR for comprehensive data analysis

**[[DATE]]** - Related function for analytical workflows

*Use DATE with YEAR for enhanced analytical workflows:*
```spreadsheets
=DATE(YEAR(A1:A10))
```
This formula combines DATE and YEAR for comprehensive data analysis
