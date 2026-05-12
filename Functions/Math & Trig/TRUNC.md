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

# TRUNC

## TRUNC Description

TRUNC calculates mathematical and trigonometric values for scientific and engineering applications.

> [!f(x)] TRUNC Syntax
>
> ```spreadsheets
> TRUNC(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] TRUNC Examples
>
> ```spreadsheets
> TRUNC(A1) → result // Basic calculation
> 
> TRUNC(A1:A10) → range_result // Process entire range
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
- [[IFERROR]] - Related math & trig function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with TRUNC for conditional logic and decision making:*
```spreadsheets
=IF(TRUNC(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies TRUNC to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with TRUNC for aggregate calculations across multiple results:*
```spreadsheets
=SUM(TRUNC(A1:A5),TRUNC(B1:B5),TRUNC(C1:C5))
```
This formula calculates TRUNC for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with TRUNC for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(TRUNC(A1:A10))
```
This formula combines AVERAGE and TRUNC for comprehensive data analysis
