---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- logical
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# IF

## IF Description

IF performs a logical test and returns one value if true and another if false. This is fundamental for conditional logic in spreadsheets.

> [!f(x)] IF Syntax
>
> ```spreadsheets
> IF(logical_test, value_if_true, [value_if_false])
> ```
>
> **Parameters:**
> - `logical_test` (required): Condition to evaluate
> - `value_if_true` (required): Value returned if condition is TRUE
> - `value_if_false` (optional): Value returned if condition is FALSE (default is FALSE)

> [!f(x)] IF Examples
>
> ```spreadsheets
> IF(A1>10, "High", "Low") → conditional_text // Simple condition
> 
> IF(B1="", "Empty", B1) → handle_blanks // Check for empty cells
> 
> IF(C1>100, C1*0.1, 0) → conditional_calculation // Conditional math
> ```

## Use Cases

### [[Conditional Logic]]
- **Implementation**: Implement business rules and decision trees using logical operators and conditional statements
- **Business Application**: Automate decision-making processes, implement approval workflows, and create rule-based systems
- **Technical Details**: Design clear logic flows, handle edge cases, and ensure comprehensive condition coverage

### [[Data Validation]]
- **Implementation**: Validate data integrity using logical tests and conditional checks for quality assurance
- **Business Application**: Ensure data accuracy, implement business rules, and prevent invalid data entry
- **Technical Details**: Create robust validation rules, implement error handling, and maintain audit trails

### [[Workflow Automation]]
- **Implementation**: Automate business processes using logical conditions to control workflow execution
- **Business Application**: Streamline operations, reduce manual effort, and ensure consistent process execution
- **Technical Details**: Design scalable logic patterns, implement proper error handling, and optimize performance

## Related

### Similar Functions

- [[IFS]] - Related logical function for analytical calculations
- [[IFERROR]] - Related logical function for analytical calculations
- [[AND]] - Related logical function for analytical calculations
- [[OR]] - Related logical function for analytical calculations

### Commonly Used With Functions

**[[AND]]** - Logical AND operations for multiple condition testing

*Use AND with IF for enhanced analytical workflows:*
```spreadsheets
=AND(IF(A1:A10))
```
This formula combines AND and IF for comprehensive data analysis

**[[OR]]** - Logical OR operations for alternative condition testing

*Use OR with IF for enhanced analytical workflows:*
```spreadsheets
=OR(IF(A1:A10))
```
This formula combines OR and IF for comprehensive data analysis

**[[IFERROR]]** - Error handling and data quality assurance for robust analytical workflows

*Combine IFERROR with IF to handle potential calculation errors:*
```spreadsheets
=IFERROR(IF(A1:A10),"Error in calculation")
```
This formula calculates IF but returns an error message if the calculation fails due to invalid data
