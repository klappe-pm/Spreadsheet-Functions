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

# RSQ

## RSQ Description

RSQ performs statistical analysis and calculations for data summarization and insights.

> [!f(x)] RSQ Syntax
>
> ```spreadsheets
> RSQ(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] RSQ Examples
>
> ```spreadsheets
> RSQ(A1) → result // Basic calculation
> 
> RSQ(A1:A10) → range_result // Process entire range
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
- [[IFERROR]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with RSQ for conditional logic and decision making:*
```spreadsheets
=IF(RSQ(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies RSQ to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with RSQ for aggregate calculations across multiple results:*
```spreadsheets
=SUM(RSQ(A1:A5),RSQ(B1:B5),RSQ(C1:C5))
```
This formula calculates RSQ for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with RSQ for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(RSQ(A1:A10))
```
This formula combines AVERAGE and RSQ for comprehensive data analysis
