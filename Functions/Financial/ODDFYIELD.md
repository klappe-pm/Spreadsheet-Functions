---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - financial
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# ODDFYIELD

## ODDFYIELD Description

Calculates the yield to maturity for a security with an odd (short or long) first coupon period. ODDFYIELD determines the effective annual yield for bonds and securities where the first interest payment period doesn't align with regular coupon schedules, essential for accurate yield analysis of newly issued or irregular-period bonds.

> [!f(x)] ODDFYIELD Syntax
>
> ```spreadsheets
> ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])
> ```
>
> **Parameters:**
> - `settlement` (required): Settlement date when security is traded
> - `maturity` (required): Maturity date when security expires  
> - `issue` (required): Issue date when security was originally issued
> - `first_coupon` (required): First coupon date after issue
> - `rate` (required): Annual coupon rate as decimal (e.g., 0.05 for 5%)
> - `pr` (required): Security price per $100 face value
> - `redemption` (required): Redemption value per $100 face value (typically 100)
> - `frequency` (required): Coupon payments per year (1=annual, 2=semi-annual, 4=quarterly)
> - `basis` (optional): Day count basis (0=30/360, 1=actual/actual, 2=actual/360, 3=actual/365, 4=30/360 European)

> [!f(x)] ODDFYIELD Examples
>
> ```spreadsheets
> // Corporate bond yield with odd first period
> ODDFYIELD(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 105.23, 100, 2, 1) → 0.048
> // Bond purchased at $105.23 yields 4.8% to maturity
> 
> // Treasury note yield analysis
> ODDFYIELD(DATE(2024,2,1), DATE(2029,2,15), DATE(2023,12,15), DATE(2024,2,15), 0.0425, 102.85, 100, 2, 1) → 0.0385
> // T-note with short first period yields 3.85%
> 
> // Municipal bond yield calculation
> ODDFYIELD(DATE(2024,4,1), DATE(2034,6,1), DATE(2023,8,1), DATE(2024,6,1), 0.0375, 97.65, 100, 2, 0) → 0.0395
> // Muni bond with long first period yields 3.95%
> 
> // High-yield corporate analysis
> ODDFYIELD(DATE(2024,6,30), DATE(2027,9,30), DATE(2024,3,1), DATE(2024,6,30), 0.085, 97.82, 100, 4, 1) → 0.092
> // Junk bond yields 9.2% with irregular first period
> 
> // International bond yield
> ODDFYIELD(DATE(2024,5,15), DATE(2027,11,15), DATE(2024,1,15), DATE(2024,5,15), 0.0625, 101.47, 100, 2, 2) → 0.0598
> // Euro bond yields 5.98% with actual/360 basis
> ```

## Use Cases

### [[Bond yield analysis]]
- **Investment decision making**: Calculate yields on newly issued bonds with irregular first periods for portfolio inclusion decisions
- **Comparative analysis**: Compare yields across bonds with different coupon structures and period alignments
- **Performance measurement**: Evaluate bond portfolio returns considering accurate yields from irregular period securities
- **Risk-return assessment**: Analyze yield spreads and risk premiums for bonds with odd first periods

### [[Fixed income research]]
- **Credit analysis**: Calculate yields for corporate bonds to determine credit spreads versus benchmark securities
- **Market efficiency studies**: Identify yield discrepancies in bonds with irregular periods for arbitrage opportunities
- **Duration matching**: Use accurate yields for duration calculations in immunization strategies
- **Yield curve analysis**: Analyze yield relationships across bonds with different structures and maturities

### [[Portfolio optimization]]
- **Asset allocation modeling**: Calculate expected returns using accurate yields for portfolio optimization algorithms
- **Benchmark comparison**: Compare portfolio yields against indices considering irregular bond structures
- **Risk budgeting**: Allocate risk based on accurate yield and spread analysis of odd-period bonds
- **Performance attribution**: Analyze portfolio performance considering proper yield calculations for all holdings

## Related

### Similar Functions

- [[ODDFPRICE]] - Calculates price for securities with odd first periods, complementary function
- [[ODDLYIELD]] - Calculates yield for securities with odd last periods
- [[YIELD]] - Calculates yield for securities with regular coupon periods
- [[YIELDMAT]] - Calculates yield for securities that pay interest at maturity
- [[YIELDDISC]] - Calculates yield for discounted securities

## Commonly Used With Functions Examples

### Comprehensive Bond Analysis
```spreadsheets
// Complete bond evaluation with all metrics
="Bond: " & A1 & " | Price: $" & F1 & " | Yield: " & ODDFYIELD(B1, C1, D1, E1, G1, F1, 100, 2, 1)*100 & "% | Duration: " & DURATION(B1, C1, G1, ODDFYIELD(B1, C1, D1, E1, G1, F1, 100, 2, 1), 2, 1) & " | Credit Spread: " & (ODDFYIELD(B1, C1, D1, E1, G1, F1, 100, 2, 1)-H1)*100 & "bps"
// Complete bond analysis with yield, duration, and spread

// Risk-return profile
="Risk-adjusted return: " & ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1)/DURATION(A1, B1, E1, ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1), 2, 1)*100 & "% per duration unit"
```

### Portfolio Optimization Analysis
```spreadsheets
// Multi-bond portfolio yield calculation
="Portfolio yield: " & (ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1 + YIELD(A2, B2, E2, F2, 100, 2, 1)*G2 + ODDLYIELD(A3, B3, C3, E3, F3, 100, 2, 1)*G3)/SUM(G1:G3)*100 & "%"
// Portfolio-level yield calculation

// Relative value ranking
="Best value: " & INDEX({"Odd First";"Regular";"Odd Last"}, MATCH(MAX(ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1), YIELD(A2, B2, E2, F2, 100, 2, 1), ODDLYIELD(A3, B3, C3, E3, F3, 100, 2, 1)), {ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1);YIELD(A2, B2, E2, F2, 100, 2, 1);ODDLYIELD(A3, B3, C3, E3, F3, 100, 2, 1)}, 0)) & " at " & MAX(ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1), YIELD(A2, B2, E2, F2, 100, 2, 1), ODDLYIELD(A3, B3, C3, E3, F3, 100, 2, 1))*100 & "%"
```

### Trading and Strategy Implementation
```spreadsheets
// Arbitrage opportunity analysis
="Fair value: $" & ODDFPRICE(A1, B1, C1, D1, E1, YIELD(H1, I1, E1, J1, 100, 2, 1), 100, 2, 1) & " vs Market: $" & F1 & " | Arb profit: $" & (ODDFPRICE(A1, B1, C1, D1, E1, YIELD(H1, I1, E1, J1, 100, 2, 1), 100, 2, 1)-F1)*G1/100
// Comprehensive arbitrage analysis with profit calculation

// Asset-liability matching
=IF(ODDFYIELD(A1, B1, C1, D1, E1, F1, 100, 2, 1)*F1*G1/100 >= PMT(H1, I1, J1, 0, 0), "Liability matched", "Need more")
// Liability-driven investment adequacy analysis
```