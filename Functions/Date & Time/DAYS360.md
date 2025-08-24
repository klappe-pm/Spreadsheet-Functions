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

# DAYS360

## DAYS360 Description

DAYS360 performs specialized calculations for analytical applications.

> [!f(x)] DAYS360 Syntax
>
> ```spreadsheets
> DAYS360(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] DAYS360 Examples
>
> ```spreadsheets
> DAYS360(A1) → result // Basic calculation
> 
> DAYS360(A1:A10) → range_result // Process entire range
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

- [[IF]] - Related date & time function for analytical calculations
- [[IFERROR]] - Related date & time function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with DAYS360 for conditional logic and decision making:*
```spreadsheets
=IF(DAYS360(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies DAYS360 to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with DAYS360 for aggregate calculations across multiple results:*
```spreadsheets
=SUM(DAYS360(A1:A5),DAYS360(B1:B5),DAYS360(C1:C5))
```
This formula calculates DAYS360 for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with DAYS360 for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(DAYS360(A1:A10))
```
This formula combines AVERAGE and DAYS360 for comprehensive data analysis
