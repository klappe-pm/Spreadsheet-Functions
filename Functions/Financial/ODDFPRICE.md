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
# ODDFPRICE

## ODDFPRICE Description

Calculates the price per $100 face value of a security with an odd (short or long) first coupon period. ODDFPRICE handles bonds and securities where the first interest payment period doesn't align with the regular coupon schedule, essential for accurate pricing of newly issued or mid-cycle bond purchases.

> [!f(x)] ODDFPRICE Syntax
>
> ```spreadsheets
> ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])
> ```
>
> **Parameters:**
> - `settlement` (required): Settlement date when security is traded
> - `maturity` (required): Maturity date when security expires
> - `issue` (required): Issue date when security was originally issued
> - `first_coupon` (required): First coupon date after issue
> - `rate` (required): Annual coupon rate as decimal (e.g., 0.05 for 5%)
> - `yld` (required): Annual yield as decimal (e.g., 0.045 for 4.5%)
> - `redemption` (required): Redemption value per $100 face value (typically 100)
> - `frequency` (required): Coupon payments per year (1=annual, 2=semi-annual, 4=quarterly)
> - `basis` (optional): Day count basis (0=30/360, 1=actual/actual, 2=actual/360, 3=actual/365, 4=30/360 European)

> [!f(x)] ODDFPRICE Examples
>
> ```spreadsheets
> // Corporate bond with odd first period
> ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1) → 105.23
> // Bond issued Nov 1 with first coupon Jan 15, settled Mar 15
> 
> // Treasury note with short first period
> ODDFPRICE(DATE(2024,2,1), DATE(2029,2,15), DATE(2023,12,15), DATE(2024,2,15), 0.0425, 0.039, 100, 2, 1) → 102.85
> // T-note with 2-month first period instead of normal 6 months
> 
> // Municipal bond with long first period
> ODDFPRICE(DATE(2024,4,1), DATE(2034,6,1), DATE(2023,8,1), DATE(2024,6,1), 0.0375, 0.041, 100, 2, 0) → 97.65
> // Muni bond with 10-month first period
> 
> // International bond with different basis
> ODDFPRICE(DATE(2024,5,15), DATE(2027,11,15), DATE(2024,1,15), DATE(2024,5,15), 0.0625, 0.058, 100, 2, 2) → 101.47
> // Euro bond using actual/360 day count
> 
> // High-yield corporate with quarterly coupons
> ODDFPRICE(DATE(2024,6,30), DATE(2027,9,30), DATE(2024,3,1), DATE(2024,6,30), 0.085, 0.092, 100, 4, 1) → 97.82
> // Junk bond with 4-month first period
> ```

## Use Cases

### [[Bond portfolio management]]
- **New issue evaluation**: Price newly issued bonds with irregular first coupon periods for portfolio inclusion decisions
- **Mid-cycle bond purchases**: Calculate accurate pricing for bonds purchased between issue and first coupon dates
- **Portfolio rebalancing**: Evaluate odd-first-period bonds for portfolio optimization and duration matching
- **Yield comparison analysis**: Compare bonds with different first-period structures on equivalent basis

### [[Fixed income trading]]
- **Market making activities**: Price bonds with odd first periods for bid-ask spread determination and inventory valuation
- **Arbitrage opportunity identification**: Find pricing discrepancies in bonds with irregular first periods versus comparable securities
- **Client order execution**: Calculate fair value pricing for institutional and retail bond trades
- **Settlement risk management**: Price bonds accurately for trade settlement and counterparty risk assessment

### [[Investment analysis]]
- **Duration and convexity calculations**: Use accurate pricing as input for portfolio risk management and hedging strategies
- **Credit spread analysis**: Evaluate corporate bonds with odd periods versus Treasury benchmarks for credit risk assessment
- **Total return projections**: Calculate expected returns incorporating accurate pricing of irregular coupon structures
- **Performance attribution**: Analyze portfolio returns considering proper valuation of odd-period securities

## Related

### Similar Functions

- [[ODDLPRICE]] - Calculates price for securities with odd last periods
- [[PRICE]] - Calculates price for securities with regular coupon periods
- [[ODDFYIELD]] - Calculates yield for securities with odd first periods
- [[YIELD]] - Calculates yield for securities with regular periods
- [[DURATION]] - Calculates modified duration for bonds

## Odd Period Bond Functions

### [[ODDLPRICE]]
ODDLPRICE handles odd last periods while ODDFPRICE handles odd first periods. Both essential for complete irregular bond pricing.

```spreadsheets
// Compare bonds with different odd periods
="Odd first: $" & ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1) & " vs Odd last: $" & ODDLPRICE(DATE(2024,3,15), DATE(2029,3,10), DATE(2024,3,15), 0.055, 0.048, 100, 2, 1)
// Compare pricing of different irregular structures

// Portfolio odd-period bond analysis
=ODDFPRICE(A2, B2, C2, D2, E2, F2, 100, 2, 1) + ODDLPRICE(A3, B3, C3, E3, F3, 100, 2, 1)
// Total value of bonds with different odd periods

// Yield curve positioning
=IF(ODDFPRICE(A1, B1, C1, D1, 0.05, G1, 100, 2, 1)>ODDLPRICE(A1, H1, A1, 0.05, G1, 100, 2, 1), "Odd first premium", "Odd last premium")
// Compare odd period structures at same yield
```

### [[PRICE]]
PRICE handles regular period bonds while ODDFPRICE handles irregular first periods. Use together for comprehensive bond analysis.

```spreadsheets
// Bond structure comparison
="Regular bond: $" & PRICE(DATE(2024,3,15), DATE(2029,3,15), 0.055, 0.048, 100, 2, 1) & " vs Odd first: $" & ODDFPRICE(DATE(2024,3,15), DATE(2029,3,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1)
// Compare regular versus irregular first period pricing

// Portfolio valuation
=PRICE(A2, B2, C2, D2, 100, 2, 1) + ODDFPRICE(E2, F2, G2, H2, I2, J2, 100, 2, 1)
// Mixed portfolio with regular and odd-first bonds

// Risk-adjusted pricing
=IF(ODDFPRICE(A1, B1, C1, D1, E1, F1+0.001, 100, 2, 1)<PRICE(A1, B1, E1, F1, 100, 2, 1), "Odd first sensitive", "Regular more sensitive")
// Compare yield sensitivity between structures
```

### [[ODDFYIELD]]
ODDFPRICE and ODDFYIELD are complementary for odd-first-period bond analysis. ODDFPRICE calculates price given yield, ODDFYIELD calculates yield given price.

```spreadsheets
// Price-yield validation
="Price: $" & ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1) & " yields: " & ODDFYIELD(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1), 100, 2, 1)*100 & "%"
// Verify price and yield calculations match

// Bond screening analysis
=IF(ODDFYIELD(A1, B1, C1, D1, E1, ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1), 100, 2, 1)>0.05, "High yield", "Investment grade")
// Screen bonds using price-yield relationship

// Market opportunity identification
=ODDFPRICE(A2, B2, C2, D2, E2, ODDFYIELD(A2, B2, C2, D2, E2, G2, 100, 2, 1), 100, 2, 1) - G2
// Compare theoretical price with market price
```

## Bond Valuation Functions

### [[YIELD]]
YIELD works with regular periods while ODDFPRICE works with irregular first periods. Both needed for comprehensive bond yield analysis.

```spreadsheets
// Yield comparison analysis
="Regular yield: " & YIELD(DATE(2024,3,15), DATE(2029,3,15), 0.055, 102.5, 100, 2, 1)*100 & "% vs Odd first yield: " & ODDFYIELD(DATE(2024,3,15), DATE(2029,3,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 102.5, 100, 2, 1)*100 & "%"
// Compare yields for different period structures

// Credit spread calculation
=ODDFYIELD(A1, B1, C1, D1, E1, ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1), 100, 2, 1) - YIELD(A2, B2, G2, H2, 100, 2, 1)
// Credit spread using odd-first corporate vs regular Treasury

// Relative value analysis
=IF(YIELD(A3, B3, C3, D3, 100, 2, 1)>ODDFYIELD(A1, B1, C4, D4, E4, ODDFPRICE(A1, B1, C4, D4, E4, F4, 100, 2, 1), 100, 2, 1), "Regular bond attractive", "Odd first better")
// Compare investment alternatives
```

### [[DURATION]]
DURATION and ODDFPRICE work together for bond risk management. ODDFPRICE provides accurate pricing input for duration calculations.

```spreadsheets
// Duration-adjusted pricing
="Duration: " & DURATION(DATE(2024,3,15), DATE(2029,1,15), 0.055, 0.048, 2, 1) & " Price: $" & ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1)
// Show duration and price for risk management

// Interest rate sensitivity
=ODDFPRICE(A1, B1, C1, D1, E1, F1+0.01, 100, 2, 1) - ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)
// Price change for 1% yield increase

// Portfolio hedging calculation
=DURATION(A2, B2, C2, D2, 2, 1) * ODDFPRICE(A1, B1, C1, D1, C2, D2, 100, 2, 1) / 100
// Dollar duration using odd-first price
```

## Portfolio Management Functions

### [[NPV]]
NPV and ODDFPRICE together enable complete bond portfolio cash flow analysis incorporating irregular first periods.

```spreadsheets
// Bond investment NPV analysis
=NPV(0.045, ODDFPRICE(DATE(2024,3,15), DATE(2029,1,15), DATE(2023,11,1), DATE(2024,1,15), 0.055, 0.048, 100, 2, 1)/100*A1) + A2:A61
// NPV of bond investment including purchase price

// Portfolio optimization
=IF(NPV(B1, C2:C21)*ODDFPRICE(A1, D1, E1, F1, G1, H1, 100, 2, 1)>I1, "Include bond", "Exclude bond")
// Portfolio inclusion decision using NPV and price

// Total return analysis
=NPV(J1, K2:K61) + ODDFPRICE(A1, D1, E1, F1, G1, L1, 100, 2, 1) - ODDFPRICE(A1, D1, E1, F1, G1, H1, 100, 2, 1)
// Total return including price appreciation
```

### [[PMT]]
PMT and ODDFPRICE work together for bond ladder construction and cash flow matching strategies.

```spreadsheets
// Bond ladder cash flow
="Annual income: $" & PMT(0, 1, -ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1/100, 0, 0) & " from coupon plus principal"
// Cash flow from odd-first bond in ladder

// Pension liability matching
=ODDFPRICE(A2, B2, C2, D2, E2, PMT(F2, G2, H2, 0, 0)/I2, 100, 2, 1)
// Bond price needed to generate required pension payments

// Income planning validation
=IF(E1*ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)/100*G1>PMT(H1, I1, J1, 0, 0), "Adequate income", "Need more bonds")
// Check if bond generates sufficient income
```

## Commonly Used With Functions Examples

### Comprehensive Bond Analysis
```spreadsheets
// Complete odd-first bond evaluation
="Bond: " & A1 & " | Price: $" & ODDFPRICE(B1, C1, D1, E1, F1, G1, 100, 2, 1) & " | Yield: " & ODDFYIELD(B1, C1, D1, E1, F1, ODDFPRICE(B1, C1, D1, E1, F1, G1, 100, 2, 1), 100, 2, 1)*100 & "% | Duration: " & DURATION(B1, C1, F1, G1, 2, 1)
// Complete bond profile with price, yield, and duration

// Portfolio risk assessment
="Position: $" & ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1/100 & " | Risk: $" & ODDFPRICE(A1, B1, C1, D1, E1, F1+0.01, 100, 2, 1)*G1/100-ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1/100 & " per 1% yield rise"
// Position size and interest rate risk quantification
```

### Fixed Income Trading Analysis
```spreadsheets
// Bid-ask spread calculation
="Bid: $" & ODDFPRICE(A1, B1, C1, D1, E1, F1+G1/10000, 100, 2, 1) & " | Ask: $" & ODDFPRICE(A1, B1, C1, D1, E1, F1-H1/10000, 100, 2, 1) & " | Spread: " & (ODDFPRICE(A1, B1, C1, D1, E1, F1-H1/10000, 100, 2, 1)-ODDFPRICE(A1, B1, C1, D1, E1, F1+G1/10000, 100, 2, 1))*32 & "/32nds"
// Market making spread in traditional bond pricing format

// Arbitrage opportunity analysis
="Theoretical: $" & ODDFPRICE(A1, B1, C1, D1, E1, YIELD(I1, J1, E1, K1, 100, 2, 1), 100, 2, 1) & " vs Market: $" & K1 & " | Arb: $" & ODDFPRICE(A1, B1, C1, D1, E1, YIELD(I1, J1, E1, K1, 100, 2, 1), 100, 2, 1)-K1 & " per $100"
// Identify mispriced bonds using comparable yield relationships
```

### Investment Strategy Implementation
```spreadsheets
// Asset allocation optimization
="Bond allocation: " & ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1/SUM(H1:H10)*100 & "% | Expected return: " & (E1*100+100-ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1))/ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*(365/(B1-TODAY()))*100 & "% annualized"
// Portfolio weight and expected return calculation

// Liability-driven investing
=IF(ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1+(E1*G1*(B1-TODAY())/365)>=H1, "Liability matched for " & TEXT(B1,"mm/dd/yyyy"), "Need $" & H1-(ODDFPRICE(A1, B1, C1, D1, E1, F1, 100, 2, 1)*G1+(E1*G1*(B1-TODAY())/365)) & " more")
// Liability matching adequacy check including coupon income
```
