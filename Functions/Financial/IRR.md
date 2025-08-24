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

# IRR

## IRR Description

IRR calculates financial metrics including payments, returns, and valuations.

> [!f(x)] IRR Syntax
>
> ```spreadsheets
> IRR(input_value, [options])
> ```
>
> **Parameters:**
> - `input_value` (required): Primary input for the calculation
> - `options` (optional): Additional parameters or settings

> [!f(x)] IRR Examples
>
> ```spreadsheets
> IRR(A1) → result // Basic calculation
> 
> IRR(A1:A10) → range_result // Process entire range
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

*Use IF with IRR for conditional logic and decision making:*
```spreadsheets
=IF(IRR(A1:A10)>threshold_value,"Condition Met","Condition Not Met")
```
This formula applies IRR to a range and compares the result to a threshold, returning different text based on the condition

**[[SUM]]** - Aggregate values for total calculations

*Use SUM with IRR for aggregate calculations across multiple results:*
```spreadsheets
=SUM(IRR(A1:A5),IRR(B1:B5),IRR(C1:C5))
```
This formula calculates IRR for multiple ranges and sums the results together

**[[AVERAGE]]** - Calculate arithmetic mean for central tendency analysis

*Use AVERAGE with IRR for enhanced analytical workflows:*
```spreadsheets
=AVERAGE(IRR(A1:A10))
```
This formula combines AVERAGE and IRR for comprehensive data analysis
