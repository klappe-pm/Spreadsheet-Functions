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

# SQRT

## SQRT Description

SQRT returns the positive square root of a number. The number must be positive; negative numbers return an error.

> [!f(x)] SQRT Syntax
>
> ```spreadsheets
> SQRT(number)
> ```
>
> **Parameters:**
> - `number` (required): A positive number for which you want the square root

> [!f(x)] SQRT Examples
>
> ```spreadsheets
> SQRT(25) → 5 // Square root of 25
> 
> SQRT(2) → 1.414 // Square root of 2
> 
> SQRT(A1) → root_value // Square root of cell value
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

- [[POWER]] - Related math & trig function for analytical calculations
- [[EXP]] - Related math & trig function for analytical calculations
- [[LOG]] - Related math & trig function for analytical calculations
- [[LN]] - Related math & trig function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with SQRT for conditional logic and decision making:*
```spreadsheets
=IF(SQRT(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies SQRT to a range and compares the result to a threshold, returning different text based on the condition

**[[ABS]]** - Related function for analytical workflows

*Use ABS with SQRT for enhanced analytical workflows:*
```spreadsheets
=ABS(SQRT(A1:A10))
```
This formula combines ABS and SQRT for comprehensive data analysis

**[[POWER]]** - Related function for analytical workflows

*Use POWER with SQRT for enhanced analytical workflows:*
```spreadsheets
=POWER(SQRT(A1:A10))
```
This formula combines POWER and SQRT for comprehensive data analysis
