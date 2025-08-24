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

# COUNT

## COUNT Description

COUNT counts the number of cells in a range that contain numeric values. Empty cells, text, and error values are ignored.

> [!f(x)] COUNT Syntax
>
> ```spreadsheets
> COUNT(value1, [value2], ...)
> ```
>
> **Parameters:**
> - `value1` (required): First range or value to count
> - `value2` (optional): Additional ranges or values

> [!f(x)] COUNT Examples
>
> ```spreadsheets
> COUNT(A1:A10) → 7 // Count numeric cells in range
> 
> COUNT(1, 2, "text", 4) → 3 // Count only numbers
> 
> COUNT(B:B) → count // Count entire column
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

- [[COUNTA]] - Related statistical function for analytical calculations
- [[COUNTIF]] - Related statistical function for analytical calculations
- [[COUNTIFS]] - Related statistical function for analytical calculations
- [[COUNTBLANK]] - Related statistical function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with COUNT for conditional logic and decision making:*
```spreadsheets
=IF(COUNT(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies COUNT to a range and compares the result to a threshold, returning different text based on the condition

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with COUNT for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(COUNT(A1:A10))
```
This formula combines AVERAGE and COUNT for comprehensive data analysis

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with COUNT for aggregate calculations across multiple results:*
```spreadsheets
=SUM(COUNT(A1:A5),COUNT(B1:B5),COUNT(C1:C5))
```
This formula calculates COUNT for multiple ranges and sums the results together
