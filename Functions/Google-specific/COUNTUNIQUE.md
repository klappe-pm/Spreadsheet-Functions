---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- google-specific
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# COUNTUNIQUE

## COUNTUNIQUE Description

COUNTUNIQUE performs specialized calculations for analytical applications.

> [!f(x)] COUNTUNIQUE Syntax
>
> ```spreadsheets
> COUNTUNIQUE(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] COUNTUNIQUE Examples
>
> ```spreadsheets
> COUNTUNIQUE(A1) → result // Basic calculation
> 
> COUNTUNIQUE(A1:A10) → range_result // Process entire range
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

- [[IF]] - Related google-specific function for analytical calculations
- [[IFERROR]] - Related google-specific function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with COUNTUNIQUE for conditional logic and decision making:*
```spreadsheets
=IF(COUNTUNIQUE(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies COUNTUNIQUE to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with COUNTUNIQUE for aggregate calculations across multiple results:*
```spreadsheets
=SUM(COUNTUNIQUE(A1:A5),COUNTUNIQUE(B1:B5),COUNTUNIQUE(C1:C5))
```
This formula calculates COUNTUNIQUE for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with COUNTUNIQUE for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(COUNTUNIQUE(A1:A10))
```
This formula combines AVERAGE and COUNTUNIQUE for comprehensive data analysis
