---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: financial
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# YIELD

## YIELD Description

Calculates the yield to maturity for a security that pays periodic interest payments. YIELD determines the effective annual interest rate earned on bonds and other securities, essential for investment analysis, bond valuation, and portfolio management decisions.

> [!f(x)] YIELD Syntax
>
> ```spreadsheets
> YIELD(settlement, maturity, rate, pr, redemption, frequency, [basis])
> ```
>
> **Parameters:**
> - `settlement` (required): Settlement date when security is traded
> - `maturity` (required): Maturity date when security expires
> - `rate` (required): Annual coupon rate as decimal (e.g., 0.05 for 5%)
> - `pr` (required): Security price per $100 face value
> - `redemption` (required): Redemption value per $100 face value (typically 100)
> - `frequency` (required): Coupon payments per year (1=annual, 2=semi-annual, 4=quarterly)
> - `basis` (optional): Day count basis (0=30/360, 1=actual/actual, 2=actual/360, 3=actual/365, 4=30/360 European)

> [!f(x)] YIELD Examples
>
> ```spreadsheets
> // Corporate bond yield calculation
> YIELD(DATE(2024,3,15), DATE(2029,3,15), 0.055, 102.5, 100, 2, 1) → 0.0485
> // Bond trading at $102.50 yields 4.85% to maturity
> 
> // Treasury bond yield analysis
> YIELD(DATE(2024,1,15), DATE(2034,1,15), 0.0425, 98.75, 100, 2, 1) → 0.0456
> // 10-year Treasury yields 4.56% when purchased at discount
> 
> // Municipal bond tax-equivalent yield
> YIELD(DATE(2024,4,1), DATE(2029,4,1), 0.035, 101.25, 100, 2, 0) → 0.0325
> // Muni bond yields 3.25% tax-free
> 
> // High-yield corporate analysis
> YIELD(DATE(2024,6,30), DATE(2027,6,30), 0.085, 96.5, 100, 4, 1) → 0.0975
> // Junk bond yields 9.75% with quarterly coupons
> 
> // International bond with different basis
> YIELD(DATE(2024,2,1), DATE(2027,2,1), 0.0375, 99.85, 100, 2, 2) → 0.0379
> // Euro bond yields 3.79% with actual/360 basis
> ```

## Use Cases

### [[Bond investment analysis]]
- **Investment decision making**: Calculate yields to compare bonds with different prices, coupons, and maturities
- **Portfolio optimization**: Select bonds based on yield analysis to maximize portfolio income and returns
- **Credit spread analysis**: Compare corporate bond yields with Treasury yields to assess credit risk premiums
- **Yield curve construction**: Analyze yields across different maturities to understand interest rate environment

### [[Fixed income trading]]
- **Bond valuation**: Determine fair value yields for bond trading and market making activities
- **Arbitrage identification**: Find yield discrepancies between similar bonds for trading opportunities
- **Risk management**: Calculate yields for duration and convexity analysis in portfolio hedging strategies
- **Client advisory**: Provide yield analysis for institutional and retail fixed income investment recommendations

### [[Financial planning]]
- **Income planning**: Calculate expected income from bond investments for retirement and cash flow planning
- **Tax optimization**: Compare taxable versus tax-free yields for optimal after-tax investment decisions
- **Laddering strategies**: Analyze yields across different maturities for bond ladder construction
- **Asset allocation**: Use yield analysis for strategic asset allocation between bonds and other investments

## Related

### Similar Functions

- [[PRICE]] - Calculates bond price given yield, complementary to YIELD function
- [[DURATION]] - Calculates modified duration using bond yield for risk analysis
- [[YIELDMAT]] - Calculates yield for securities that pay interest at maturity only
- [[YIELDDISC]] - Calculates yield for discounted securities like Treasury bills
- [[ODDFYIELD]] - Calculates yield for securities with odd first coupon periods

## Commonly Used With Functions Examples

### Complete Bond Analysis
```spreadsheets
// Comprehensive bond evaluation
="Bond yield: " & YIELD(A1, B1, C1, D1, 100, 2, 1)*100 & "% | Price: $" & PRICE(A1, B1, C1, YIELD(A1, B1, C1, D1, 100, 2, 1), 100, 2, 1) & " | Duration: " & DURATION(A1, B1, C1, YIELD(A1, B1, C1, D1, 100, 2, 1), 2, 1) & " | Current yield: " & (C1*100/D1) & "%"
// Complete bond analysis with yield, price validation, duration, and current yield

// Credit spread analysis
="Corporate yield: " & YIELD(A1, B1, C1, D1, 100, 2, 1)*100 & "% | Treasury yield: " & E1*100 & "% | Credit spread: " & (YIELD(A1, B1, C1, D1, 100, 2, 1)-E1)*10000 & " bps | Risk premium: " & ((YIELD(A1, B1, C1, D1, 100, 2, 1)-E1)/E1)*100 & "%"
// Credit risk analysis with spread calculation
```

### Portfolio Management Analysis
```spreadsheets
// Multi-bond portfolio yield
="Portfolio yield: " & SUMPRODUCT(F1:F5, G1:G5*YIELD(A1:A5, B1:B5, C1:C5, D1:D5, 100, 2, 1))/SUM(F1:F5*G1:G5)*100 & "% | Average duration: " & SUMPRODUCT(F1:F5*G1:G5, DURATION(A1:A5, B1:B5, C1:C5, YIELD(A1:A5, B1:B5, C1:C5, D1:D5, 100, 2, 1), 2, 1))/SUM(F1:F5*G1:G5)
// Portfolio-weighted yield and duration calculation

// Yield curve analysis
="2Y yield: " & YIELD(TODAY(), TODAY()+730, A1, B1, 100, 2, 1)*100 & "% | 10Y yield: " & YIELD(TODAY(), TODAY()+3650, A2, B2, 100, 2, 1)*100 & "% | Curve slope: " & (YIELD(TODAY(), TODAY()+3650, A2, B2, 100, 2, 1)-YIELD(TODAY(), TODAY()+730, A1, B1, 100, 2, 1))*100 & " bps"
// Yield curve slope analysis
```

### Investment Strategy Implementation  
```spreadsheets
// Tax-equivalent yield comparison
="Muni yield: " & YIELD(A1, B1, C1, D1, 100, 2, 0)*100 & "% | Tax-equiv yield: " & YIELD(A1, B1, C1, D1, 100, 2, 0)/(1-E1)*100 & "% | Taxable yield: " & YIELD(A2, B2, C2, D2, 100, 2, 1)*100 & "% | " & IF(YIELD(A1, B1, C1, D1, 100, 2, 0)/(1-E1)>YIELD(A2, B2, C2, D2, 100, 2, 1), "Muni better", "Taxable better")
// Municipal vs taxable bond comparison with tax bracket consideration

// Ladder strategy optimization
="1Y yield: " & YIELD(TODAY(), TODAY()+365, A1, B1, 100, 2, 1)*100 & "% | 3Y yield: " & YIELD(TODAY(), TODAY()+1095, A2, B2, 100, 2, 1)*100 & "% | 5Y yield: " & YIELD(TODAY(), TODAY()+1825, A3, B3, 100, 2, 1)*100 & "% | Ladder avg: " & (YIELD(TODAY(), TODAY()+365, A1, B1, 100, 2, 1)+YIELD(TODAY(), TODAY()+1095, A2, B2, 100, 2, 1)+YIELD(TODAY(), TODAY()+1825, A3, B3, 100, 2, 1))/3*100 & "%"
// Bond ladder yield analysis across maturities
```