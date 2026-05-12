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

# DATEDIF

## DATEDIF Description

DATEDIF performs conditional calculations based on specified criteria, returning results when conditions are met.

> [!f(x)] DATEDIF Syntax
>
> ```spreadsheets
> DATEDIF(range, criteria, [sum_range])
> ```
>
> **Parameters:**
> - `range` (required): Range to evaluate against criteria
> - `criteria` (required): Condition to test
> - `sum_range` (optional): Range to sum when criteria is met

> [!f(x)] DATEDIF Examples
>
> ```spreadsheets
> DATEDIF(A1:A10,">10") → result // Count/sum values greater than 10
> 
> DATEDIF(B:B,"Yes",C:C) → conditional_result // Sum C where B="Yes"
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
- [[SUMIF]] - Related date & time function for analytical calculations
- [[COUNTIF]] - Related date & time function for analytical calculations
- [[AVERAGEIF]] - Related date & time function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with DATEDIF for conditional logic and decision making:*
```spreadsheets
=IF(DATEDIF(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies DATEDIF to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with DATEDIF for aggregate calculations across multiple results:*
```spreadsheets
=SUM(DATEDIF(A1:A5),DATEDIF(B1:B5),DATEDIF(C1:C5))
```
This formula calculates DATEDIF for multiple ranges and sums the results together

**[[COUNT]]** - Count numeric values for sample size validation

*Use COUNT with DATEDIF for enhanced analytical workflows:*
```spreadsheets
=COUNT(DATEDIF(A1:A10))
```
This formula combines COUNT and DATEDIF for comprehensive data analysis
