---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# SUMIFS

## SUMIFS Description

SUMIFS performs conditional calculations based on specified criteria, returning results when conditions are met.

> [!f(x)] SUMIFS Syntax
>
> ```spreadsheets
> SUMIFS(range, criteria, [sum_range])
> ```
>
> **Parameters:**
> - `range` (required): Range to evaluate against criteria
> - `criteria` (required): Condition to test
> - `sum_range` (optional): Range to sum when criteria is met

> [!f(x)] SUMIFS Examples
>
> ```spreadsheets
> SUMIFS(A1:A10,">10") → result // Count/sum values greater than 10
> 
> SUMIFS(B:B,"Yes",C:C) → conditional_result // Sum C where B="Yes"
> ```

## Use Cases

### [[Mathematical Calculations]]
- **Implementation**: Perform precise mathematical computations for engineering, scientific, and financial applications
- **Business Application**: Support complex calculations in modeling, analysis, and quantitative decision-making processes
- **Technical Details**: Ensure numerical accuracy, handle edge cases, and implement proper rounding and precision controls

### [[Engineering Analysis]]
- **Implementation**: Apply mathematical functions for engineering calculations, measurements, and technical analysis
- **Business Application**: Support product design, manufacturing processes, and quality engineering initiatives
- **Technical Details**: Consider measurement precision, unit conversions, and mathematical model validation

### [[Data Transformation]]
- **Implementation**: Transform and normalize data using mathematical operations for analysis and reporting
- **Business Application**: Prepare data for analysis, create derived metrics, and standardize measurements
- **Technical Details**: Implement data validation, handle boundary conditions, and ensure calculation consistency

## Related

### Similar Functions

- [[IF]] - Related math & trig function for analytical calculations
- [[SUMIF]] - Related math & trig function for analytical calculations
- [[COUNTIF]] - Related math & trig function for analytical calculations
- [[AVERAGEIF]] - Related math & trig function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with SUMIFS for conditional logic and decision making:*
```spreadsheets
=IF(SUMIFS(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies SUMIFS to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with SUMIFS for aggregate calculations across multiple results:*
```spreadsheets
=SUM(SUMIFS(A1:A5),SUMIFS(B1:B5),SUMIFS(C1:C5))
```
This formula calculates SUMIFS for multiple ranges and sums the results together

**[[COUNT]]** - Count numeric values for sample size validation

*Use COUNT with SUMIFS for enhanced analytical workflows:*
```spreadsheets
=COUNT(SUMIFS(A1:A10))
```
This formula combines COUNT and SUMIFS for comprehensive data analysis
