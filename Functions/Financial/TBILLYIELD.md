---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- financial
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
---

# TBILLYIELD

## TBILLYIELD Description

TBILLYIELD calculates financial metrics including payments, returns, and valuations.

> [!f(x)] TBILLYIELD Syntax
>
> ```spreadsheets
> TBILLYIELD(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] TBILLYIELD Examples
>
> ```spreadsheets
> TBILLYIELD(A1) → result // Basic calculation
> 
> TBILLYIELD(A1:A10) → range_result // Process entire range
> ```

## Use Cases

### [[Financial Analysis]]
- **Implementation**: Calculate financial metrics including NPV, IRR, loan payments, and investment returns
- **Business Application**: Support investment decisions, loan analysis, and financial planning processes
- **Technical Details**: Ensure accurate interest calculations, handle different compounding periods, and validate assumptions

### [[Investment Planning]]
- **Implementation**: Evaluate investment opportunities using time value of money calculations and risk analysis
- **Business Application**: Support capital budgeting, retirement planning, and investment portfolio management
- **Technical Details**: Consider cash flow timing, discount rates, and sensitivity analysis for robust planning

### [[Loan Analysis]]
- **Implementation**: Calculate loan payments, amortization schedules, and debt service requirements
- **Business Application**: Support lending decisions, borrowing analysis, and debt management strategies
- **Technical Details**: Handle different payment frequencies, variable rates, and loan structure complexity

## Related

### Similar Functions

- [[IF]] - Related financial function for analytical calculations
- [[IFERROR]] - Related financial function for analytical calculations

### Commonly Used With Functions

**[[IF]]** - Conditional logic for implementing business rules and decision-making criteria

*Use IF with TBILLYIELD for conditional logic and decision making:*
```spreadsheets
=IF(TBILLYIELD(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies TBILLYIELD to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with TBILLYIELD for aggregate calculations across multiple results:*
```spreadsheets
=SUM(TBILLYIELD(A1:A5),TBILLYIELD(B1:B5),TBILLYIELD(C1:C5))
```
This formula calculates TBILLYIELD for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with TBILLYIELD for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(TBILLYIELD(A1:A10))
```
This formula combines AVERAGE and TBILLYIELD for comprehensive data analysis
