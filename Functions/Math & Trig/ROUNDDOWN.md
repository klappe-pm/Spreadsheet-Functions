---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# ROUNDDOWN

## ROUNDDOWN Description

Rounds a number down toward zero to a specified number of decimal places. Always rounds down regardless of the digit being rounded, making it ideal for conservative calculations, floor pricing, and situations requiring guaranteed minimums.

> [!f(x)] ROUNDDOWN Syntax
>
> ```spreadsheets
> ROUNDDOWN(number, num_digits)
> ```
>
> **Parameters:**
> - `number` (required): The real number to round down
> - `num_digits` (required): Number of decimal places (positive for decimals, negative for whole numbers)

> [!f(x)] ROUNDDOWN Examples
>
> ```spreadsheets
> // Round down to 2 decimal places
> ROUNDDOWN(3.14159, 2) → 3.14
> 
> // Round down to nearest integer
> ROUNDDOWN(7.89, 0) → 7
> 
> // Round down to nearest ten
> ROUNDDOWN(156, -1) → 150
> 
> // Conservative pricing
> ROUNDDOWN(99.95, 0) → 99
> 
> // Negative number rounding (toward zero)
> ROUNDDOWN(-3.7, 0) → -3
> ```

## Use Cases

### [[Financial calculations]]
- **Conservative budgeting**: Round down revenue projections and round up expense estimates for safer financial planning
- **Discount pricing**: Create psychological pricing points by rounding down to attractive price levels
- **Tax calculations**: Ensure compliance by rounding down deductions and rounding up liabilities
- **Investment analysis**: Use conservative return estimates by rounding down optimistic projections

### [[Inventory management]]  
- **Stock levels**: Round down available quantities to prevent overselling and maintain safety margins
- **Batch calculations**: Determine complete production runs by rounding down to available raw materials
- **Packaging optimization**: Calculate maximum complete packages without exceeding container limits
- **Resource allocation**: Distribute resources conservatively to ensure all commitments can be fulfilled

### [[Engineering precision]]
- **Manufacturing tolerances**: Round down measurements to ensure parts fit within specified dimensional limits
- **Safety calculations**: Apply conservative factors by rounding down load capacities and performance metrics
- **Quality control**: Set minimum acceptable standards by rounding down from ideal specifications
- **Material planning**: Calculate material requirements conservatively to prevent shortages

## Related

### Similar Functions

- [[ROUNDUP]] - Rounds numbers up away from zero, complementary to ROUNDDOWN for different rounding strategies
- [[ROUND]] - Rounds to nearest value using standard rounding rules, more balanced than directional rounding
- [[FLOOR]] - Rounds down to nearest multiple or integer, similar to ROUNDDOWN but with multiple options
- [[TRUNC]] - Removes decimal places without rounding, related to ROUNDDOWN for integer conversion
- [[INT]] - Returns integer portion of number, similar to ROUNDDOWN(number, 0) for positive numbers

## Rounding Functions

### [[ROUNDUP]]
Complementary function providing opposite rounding direction, useful for paired conservative and aggressive calculations.

```spreadsheets
// Conservative range estimation
=ROUNDDOWN(A1*0.9, 0) & " to " & ROUNDUP(A1*1.1, 0)
// Creates conservative range with 10% margins

// Budget planning with safety margins
=ROUNDDOWN(B1, -2) & " (conservative) vs " & ROUNDUP(B1, -2) & " (optimistic)"
// Shows rounded-down and rounded-up budget estimates

// Inventory planning comparison
=ROUNDDOWN(C1/D1, 0) & " guaranteed vs " & ROUNDUP(C1/D1, 0) & " maximum"
// Compares conservative vs optimistic inventory calculations
```

### [[ROUND]]
Provides standard rounding rules as alternative to directional rounding, useful for balanced calculations.

```spreadsheets
// Compare rounding strategies
="Down: " & ROUNDDOWN(A1, 2) & ", Standard: " & ROUND(A1, 2) & ", Up: " & ROUNDUP(A1, 2)
// Shows all three rounding approaches for comparison

// Conditional rounding strategy
=IF(B1>0, ROUNDDOWN(B1, 1), ROUND(B1, 1))
// Uses conservative rounding for positive values, standard for others

// Precision analysis
=ABS(ROUNDDOWN(C1, 2) - ROUND(C1, 2))
// Calculates difference between rounding methods
```

## Financial Functions

### [[PMT]]
Combines with ROUNDDOWN for conservative loan and payment calculations, ensuring affordability and cash flow safety.

```spreadsheets
// Conservative monthly payment calculation
=ROUNDDOWN(PMT(A1/12, B1, C1), 2)
// Rounds down payment to conservative affordable amount

// Budget-safe payment planning
=ROUNDDOWN(D1*0.28, -1)
// Rounds down 28% income rule to nearest $10 for safety

// Loan affordability analysis
=ROUNDDOWN(PMT(E1/12, F1*12, G1)*-1, 0)
// Conservative monthly payment with safety margin
```

### [[NPV]]
Works with ROUNDDOWN for conservative investment analysis and financial decision-making.

```spreadsheets
// Conservative NPV calculation
=ROUNDDOWN(NPV(H1, I2:I11), -3)
// Rounds down NPV to nearest thousand for conservative analysis

// Investment threshold analysis
=IF(ROUNDDOWN(NPV(J1, K2:K10), 0)>0, "Invest", "Pass")
// Uses conservative NPV for investment decisions

// Risk-adjusted valuation
=ROUNDDOWN(NPV(L1*1.1, M2:M6), -2)
// Applies risk premium and conservative rounding
```

## Commonly Used With Functions Examples

### ROUNDDOWN with Pricing Strategy
```spreadsheets
// Psychological pricing ($X.99)
=ROUNDDOWN(A1, 0) - 0.01
// Creates prices ending in .99 for marketing appeal

// Volume discount calculation
=ROUNDDOWN(B1*0.85, 2)
// Conservative 15% discount with exact pricing
```

### ROUNDDOWN with Resource Planning
```spreadsheets
// Team capacity planning
=ROUNDDOWN(C1/8, 0) & " full days available"
// Calculates complete work days from total hours

// Production batch sizing
=ROUNDDOWN(D1/E1, 0) & " complete batches possible"
// Determines maximum complete production runs
```

### ROUNDDOWN with Safety Calculations
```spreadsheets
// Load capacity with safety factor
=ROUNDDOWN(F1*0.8, 1) & " lbs safe capacity"
// Applies 20% safety margin with conservative rounding

// Conservative time estimation
=ROUNDDOWN(G1*1.2, 0) & " minutes with buffer"
// Adds 20% time buffer and rounds down for scheduling
```
