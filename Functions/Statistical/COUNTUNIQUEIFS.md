---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# COUNTUNIQUEIFS

## COUNTUNIQUEIFS Description

COUNTUNIQUEIFS performs conditional calculations based on specified criteria, returning results when conditions are met.

> [!f(x)] COUNTUNIQUEIFS Syntax
>
> ```spreadsheets
> COUNTUNIQUEIFS(range, criteria, [sum_range])
> ```
>
> **Parameters:**
> - `range` (required): Range to evaluate against criteria
> - `criteria` (required): Condition to test
> - `sum_range` (optional): Range to sum when criteria is met

> [!f(x)] COUNTUNIQUEIFS Examples
>
> ```spreadsheets
> COUNTUNIQUEIFS(A1:A10,">10") → result // Count/sum values greater than 10
> 
> COUNTUNIQUEIFS(B:B,"Yes",C:C) → conditional_result // Sum C where B="Yes"
> ```

## Use Cases

### [[Statistical Analysis]]
- **Implementation**: Perform comprehensive statistical analysis including descriptive statistics, hypothesis testing, and data summarization
- **Business Application**: Analyze business performance, quality metrics, survey data, and operational statistics for data-driven insights
- **Technical Details**: Handle missing values, validate data types, and ensure statistical significance in calculations

### [[Quality Control]]
- **Implementation**: Apply statistical methods for process control, variation monitoring, and quality assurance programs
- **Business Application**: Monitor manufacturing quality, service levels, and performance standards against specifications
- **Technical Details**: Implement control limits, statistical process control, and automated alerting systems

### [[Risk Assessment]]
- **Implementation**: Use statistical measures for risk modeling, uncertainty quantification, and probability analysis
- **Business Application**: Assess financial risk, operational risk, and support strategic decision-making processes
- **Technical Details**: Consider distribution assumptions, validate models with backtesting, and implement sensitivity analysis

## Related

### Similar Functions

- [[IF]] - Related statistical function for analytical calculations
- [[SUMIF]] - Related statistical function for analytical calculations
- [[COUNTIF]] - Related statistical function for analytical calculations
- [[AVERAGEIF]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with COUNTUNIQUEIFS for conditional logic and decision making:*
```spreadsheets
=IF(COUNTUNIQUEIFS(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies COUNTUNIQUEIFS to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with COUNTUNIQUEIFS for aggregate calculations across multiple results:*
```spreadsheets
=SUM(COUNTUNIQUEIFS(A1:A5),COUNTUNIQUEIFS(B1:B5),COUNTUNIQUEIFS(C1:C5))
```
This formula calculates COUNTUNIQUEIFS for multiple ranges and sums the results together

**[[COUNT]]** - Count numeric values for sample size validation

*Use COUNT with COUNTUNIQUEIFS for enhanced analytical workflows:*
```spreadsheets
=COUNT(COUNTUNIQUEIFS(A1:A10))
```
This formula combines COUNT and COUNTUNIQUEIFS for comprehensive data analysis
