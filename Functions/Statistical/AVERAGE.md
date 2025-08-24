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

# AVERAGE

## AVERAGE Description

AVERAGE calculates the arithmetic mean of a set of numbers by adding all values and dividing by the count. This is the most common measure of central tendency.

> [!f(x)] AVERAGE Syntax
>
> ```spreadsheets
> AVERAGE(value1, [value2], ...)
> ```
>
> **Parameters:**
> - `value1` (required): First number, cell reference, or range
> - `value2` (optional): Additional numbers, references, or ranges

> [!f(x)] AVERAGE Examples
>
> ```spreadsheets
> AVERAGE(1, 2, 3, 4, 5) → 3 // Simple arithmetic mean
> 
> AVERAGE(A1:A10) → mean_value // Average of range
> 
> AVERAGE(B2:B20, D5:D15) → combined_avg // Multiple ranges
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

- [[MEDIAN]] - Related statistical function for analytical calculations
- [[MODE]] - Related statistical function for analytical calculations
- [[GEOMEAN]] - Related statistical function for analytical calculations
- [[HARMEAN]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Combine IF with AVERAGE for conditional mean calculations:*
```spreadsheets
=IF(AVERAGE(A1:A10)>50,"Above target","Below target")
```
This formula calculates the average and compares it to a target value of 50, returning status text

**[[COUNT]]** - Count numeric values for sample size validation

*Use COUNT with AVERAGE to validate data completeness before calculating mean:*
```spreadsheets
=IF(COUNT(A1:A10)>=5,AVERAGE(A1:A10),"Insufficient data")
```
This formula only calculates the average if there are at least 5 numeric values, ensuring statistical validity

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with AVERAGE for aggregate calculations across multiple results:*
```spreadsheets
=SUM(AVERAGE(A1:A5),AVERAGE(B1:B5),AVERAGE(C1:C5))
```
This formula calculates AVERAGE for multiple ranges and sums the results together
