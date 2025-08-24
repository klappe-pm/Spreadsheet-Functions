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

# MAX

## MAX Description

MAX returns the largest numeric value in a set of values. Text and logical values are ignored unless typed directly as arguments.

> [!f(x)] MAX Syntax
>
> ```spreadsheets
> MAX(value1, [value2], ...)
> ```
>
> **Parameters:**
> - `value1` (required): First number, reference, or range
> - `value2` (optional): Additional numbers, references, or ranges

> [!f(x)] MAX Examples
>
> ```spreadsheets
> MAX(10, 25, 5, 30) → 30 // Largest value
> 
> MAX(A1:A20) → max_value // Maximum in range
> 
> MAX(B:B, D:D) → overall_max // Maximum across columns
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

- [[MIN]] - Related statistical function for analytical calculations
- [[LARGE]] - Related statistical function for analytical calculations
- [[MAXA]] - Related statistical function for analytical calculations
- [[MAXIFS]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with MAX for conditional logic and decision making:*
```spreadsheets
=IF(MAX(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies MAX to a range and compares the result to a threshold, returning different text based on the condition

**[[INDEX]]** - Retrieve values by position for flexible lookups

*Use INDEX with MAX for enhanced analytical workflows:*
```spreadsheets
=INDEX(MAX(A1:A10))
```
This formula combines INDEX and MAX for comprehensive data analysis

**[[MATCH]]** - Find position of values for dynamic references

*Use MATCH with MAX for enhanced analytical workflows:*
```spreadsheets
=MATCH(MAX(A1:A10))
```
This formula combines MATCH and MAX for comprehensive data analysis
