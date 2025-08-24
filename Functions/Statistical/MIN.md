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

# MIN

## MIN Description

MIN returns the smallest numeric value in a set of values. Text and logical values are ignored unless typed directly as arguments.

> [!f(x)] MIN Syntax
>
> ```spreadsheets
> MIN(value1, [value2], ...)
> ```
>
> **Parameters:**
> - `value1` (required): First number, reference, or range
> - `value2` (optional): Additional numbers, references, or ranges

> [!f(x)] MIN Examples
>
> ```spreadsheets
> MIN(10, 25, 5, 30) → 5 // Smallest value
> 
> MIN(A1:A20) → min_value // Minimum in range
> 
> MIN(B:B, D:D) → overall_min // Minimum across columns
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

- [[MAX]] - Related statistical function for analytical calculations
- [[SMALL]] - Related statistical function for analytical calculations
- [[MINA]] - Related statistical function for analytical calculations
- [[MINIFS]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with MIN for conditional logic and decision making:*
```spreadsheets
=IF(MIN(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies MIN to a range and compares the result to a threshold, returning different text based on the condition

**[[INDEX]]** - Retrieve values by position for flexible lookups

*Use INDEX with MIN for enhanced analytical workflows:*
```spreadsheets
=INDEX(MIN(A1:A10))
```
This formula combines INDEX and MIN for comprehensive data analysis

**[[MATCH]]** - Find position of values for dynamic references

*Use MATCH with MIN for enhanced analytical workflows:*
```spreadsheets
=MATCH(MIN(A1:A10))
```
This formula combines MATCH and MIN for comprehensive data analysis
