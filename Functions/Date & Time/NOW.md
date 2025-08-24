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

# NOW

## NOW Description

NOW returns the current date and time as a serial number. Updates automatically with worksheet recalculation.

> [!f(x)] NOW Syntax
>
> ```spreadsheets
> NOW()
> ```
>
> **Parameters:**


> [!f(x)] NOW Examples
>
> ```spreadsheets
> NOW() → current_datetime // Current date and time
> 
> NOW()-A1 → time_elapsed // Time since datetime in A1
> 
> INT(NOW()) → today_date // Extract just the date part
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

- [[TODAY]] - Related date & time function for analytical calculations
- [[TIME]] - Related date & time function for analytical calculations
- [[HOUR]] - Related date & time function for analytical calculations
- [[MINUTE]] - Related date & time function for analytical calculations
- [[SECOND]] - Related date & time function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with NOW for conditional logic and decision making:*
```spreadsheets
=IF(NOW(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies NOW to a range and compares the result to a threshold, returning different text based on the condition

**[[INT]]** - Related function for analytical workflows

*Use INT with NOW for enhanced analytical workflows:*
```spreadsheets
=INT(NOW(A1:A10))
```
This formula combines INT and NOW for comprehensive data analysis

**[[TIME]]** - Related function for analytical workflows

*Use TIME with NOW for enhanced analytical workflows:*
```spreadsheets
=TIME(NOW(A1:A10))
```
This formula combines TIME and NOW for comprehensive data analysis
