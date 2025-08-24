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

# TODAY

## TODAY Description

TODAY returns the current date as a serial number. The date updates automatically when the worksheet recalculates.

> [!f(x)] TODAY Syntax
>
> ```spreadsheets
> TODAY()
> ```
>
> **Parameters:**


> [!f(x)] TODAY Examples
>
> ```spreadsheets
> TODAY() → current_date // Today's date
> 
> TODAY()+30 → future_date // 30 days from today
> 
> TODAY()-A1 → days_since // Days since date in A1
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

- [[NOW]] - Related date & time function for analytical calculations
- [[DATE]] - Related date & time function for analytical calculations
- [[YEAR]] - Related date & time function for analytical calculations
- [[MONTH]] - Related date & time function for analytical calculations
- [[DAY]] - Related date & time function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with TODAY for conditional logic and decision making:*
```spreadsheets
=IF(TODAY(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies TODAY to a range and compares the result to a threshold, returning different text based on the condition

**[[YEAR]]** - Extract year component from dates

*Use YEAR with TODAY for enhanced analytical workflows:*
```spreadsheets
=YEAR(TODAY(A1:A10))
```
This formula combines YEAR and TODAY for comprehensive data analysis

**[[MONTH]]** - Extract month component from dates

*Use MONTH with TODAY for enhanced analytical workflows:*
```spreadsheets
=MONTH(TODAY(A1:A10))
```
This formula combines MONTH and TODAY for comprehensive data analysis
