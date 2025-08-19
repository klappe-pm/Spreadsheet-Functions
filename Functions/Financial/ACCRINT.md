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

# ACCRINT

## ACCRINT Description

Calculates the accrued interest for a security that pays periodic interest payments. Returns the total interest that has accumulated between the issue date and the settlement date for bonds, treasury notes, and other interest-bearing securities with regular payment schedules.

> [!f(x)] ACCRINT Syntax
>
> ```spreadsheets
> ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis], [calc_method])
> ```
>
> **Parameters:**
> - `issue` (required): Issue date of the security
> - `first_interest` (required): Date of first interest payment
> - `settlement` (required): Settlement date (when interest is calculated to)
> - `rate` (required): Annual coupon rate as decimal or percentage
> - `par` (required): Par value of the security
> - `frequency` (required): Number of coupon payments per year (1, 2, or 4)
> - `basis` (optional): Day count basis (0=30/360, 1=Actual/Actual, 2=Actual/360, 3=Actual/365, 4=30/360 European)
> - `calc_method` (optional): Calculation method (TRUE=use days from issue, FALSE=use maturity)

> [!f(x)] ACCRINT Examples
>
> ```spreadsheets
> // Corporate bond accrued interest
> ACCRINT(DATE(2023,1,15), DATE(2023,7,15), DATE(2023,4,1), 0.05, 1000, 2) → 41.67
> // Bond issued Jan 15, first payment July 15, settled April 1, 5% rate
> 
> // Treasury note with quarterly payments
> ACCRINT(DATE(2023,3,1), DATE(2023,6,1), DATE(2023,5,15), 0.045, 10000, 4) → 337.50
> // T-note with 4.5% rate and quarterly coupons
> 
> // Municipal bond with 30/360 day count
> ACCRINT(DATE(2023,2,1), DATE(2023,8,1), DATE(2023,6,15), 0.04, 5000, 2, 0) → 91.67
> // Municipal bond using 30/360 basis calculation
> 
> // High-yield corporate bond
> ACCRINT(DATE(2023,6,15), DATE(2023,12,15), DATE(2023,10,1), 0.085, 25000, 2) → 656.25
> // Corporate bond with 8.5% coupon rate
> 
> // Zero-coupon calculation with actual/actual basis
> ACCRINT(DATE(2023,1,1), DATE(2024,1,1), DATE(2023,9,1), 0.03, 1000, 1, 1) → 20.00
> // Annual payment bond with actual day count
> ```

## Use Cases

### [[Bond portfolio management]]
- **Accrued interest tracking**: Calculate precise accrued interest amounts for individual bonds in investment portfolios to determine accurate market values and yield calculations
- **Settlement calculations**: Determine the total amount buyers must pay sellers when purchasing bonds between interest payment dates, including both principal and accrued interest
- **Portfolio valuation**: Compute total accrued interest across all bond holdings for accurate daily portfolio valuation and performance reporting to investors
- **Interest income forecasting**: Project future accrued interest amounts for budgeting and cash flow planning in fixed-income investment strategies

### [[Financial reporting]]
- **Balance sheet preparation**: Record accrued interest receivable on corporate balance sheets for bonds held as investments, ensuring compliance with accounting standards
- **Income statement accuracy**: Calculate precise interest income recognition for bonds purchased or sold during interest periods, matching revenue to appropriate reporting periods
- **Regulatory compliance**: Generate accurate accrued interest reports for regulatory filings, tax calculations, and audit documentation requirements
- **Mark-to-market valuations**: Incorporate accrued interest into daily mark-to-market calculations for trading portfolios and investment fund reporting

### [[Trading operations]]
- **Trade settlement**: Calculate exact amounts for bond trades occurring between coupon payment dates, ensuring accurate pricing for both institutional and retail transactions
- **Arbitrage analysis**: Identify pricing discrepancies in bond markets by comparing quoted prices plus accrued interest against theoretical fair values
- **Risk management**: Monitor interest rate exposure and duration of bond positions including accrued interest components for comprehensive portfolio risk assessment
- **Market making**: Provide accurate bid-ask spreads for bonds by incorporating real-time accrued interest calculations into pricing algorithms

## Related

### Similar Functions

- [[ACCRINTM]] - Calculates accrued interest for securities that pay interest at maturity
- [[PRICE]] - Returns the price per $100 face value of a security that pays periodic interest
- [[YIELD]] - Returns the yield on a security that pays periodic interest payments
- [[DURATION]] - Returns the Macaulay duration for an assumed par value of $100
- [[COUPDAYS]] - Returns the number of days in the coupon period containing the settlement date

## Bond Pricing Functions

### [[PRICE]]
Works with ACCRINT to provide complete bond valuation, combining clean price calculations with accrued interest amounts.

```spreadsheets
// Complete bond purchase price calculation
=LET(clean_price, PRICE(DATE(2023,6,15), DATE(2028,6,15), 0.05, 0.055, 100, 2),
     accrued_interest, ACCRINT(DATE(2023,1,15), DATE(2023,6,15), DATE(2023,4,1), 0.05, 100, 2),
     total_price, clean_price + accrued_interest,
     HSTACK("Clean Price:", clean_price, "Accrued Interest:", accrued_interest, "Total Price:", total_price))
// Shows breakdown of bond pricing components

// Bond yield analysis with accrued interest
=MAP(bond_portfolio, LAMBDA(bond,
  LET(settlement_date, TODAY(),
      clean_price, PRICE(INDEX(bond,1,2), INDEX(bond,1,3), INDEX(bond,1,4), INDEX(bond,1,5), 100, 2),
      accrued_int, ACCRINT(INDEX(bond,1,1), INDEX(bond,1,6), settlement_date, INDEX(bond,1,4), 100, 2),
      dirty_price, clean_price + accrued_int,
      HSTACK(INDEX(bond,1,1), clean_price, accrued_int, dirty_price))))
// Portfolio analysis with clean and dirty prices

// Monthly bond valuation report
=LET(month_end_date, EOMONTH(TODAY(), 0),
     bond_valuations, MAP(bond_holdings, LAMBDA(holding,
       LET(bond_id, INDEX(holding,1,1),
           par_value, INDEX(holding,1,7),
           accrued, ACCRINT(INDEX(holding,1,2), INDEX(holding,1,6), month_end_date, 
                           INDEX(holding,1,4), par_value, INDEX(holding,1,8)),
           market_price, PRICE(INDEX(holding,1,2), INDEX(holding,1,3), INDEX(holding,1,4), 
                              INDEX(holding,1,5), 100, INDEX(holding,1,8)) * par_value / 100,
           total_value, market_price + accrued,
           HSTACK(bond_id, par_value, market_price, accrued, total_value)))),
     VSTACK("Bond Valuations as of " & TEXT(month_end_date, "mmm dd, yyyy"),
            HSTACK("Bond ID", "Par Value", "Market Value", "Accrued Interest", "Total Value"),
            bond_valuations))
```

### [[DURATION]]
Combines with ACCRINT for comprehensive bond risk analysis, measuring price sensitivity to interest rate changes alongside accrued interest.

```spreadsheets
// Bond risk assessment with accrued interest impact
=MAP(fixed_income_portfolio, LAMBDA(bond,
  LET(settlement, TODAY(),
      bond_duration, DURATION(INDEX(bond,1,2), INDEX(bond,1,3), INDEX(bond,1,4), INDEX(bond,1,5), 2),
      accrued_int, ACCRINT(INDEX(bond,1,1), INDEX(bond,1,6), settlement, INDEX(bond,1,4), INDEX(bond,1,7), 2),
      price_sensitivity, bond_duration * INDEX(bond,1,7) / 100,  // Duration times par value
      interest_component, accrued_int / INDEX(bond,1,7),  // Accrued as % of par
      HSTACK(INDEX(bond,1,1), bond_duration, accrued_int, price_sensitivity, interest_component))))
// Risk analysis combining duration and accrued interest

// Interest rate scenario analysis
=LET(rate_scenarios, {-0.02, -0.01, 0, 0.01, 0.02},
     base_settlement, TODAY(),
     scenario_analysis, MAP(rate_scenarios, LAMBDA(rate_change,
       LET(scenario_yield, bond_yield + rate_change,
           new_price, PRICE(bond_issue, bond_maturity, bond_coupon, scenario_yield, 100, 2),
           accrued, ACCRINT(bond_issue, bond_first_payment, base_settlement, bond_coupon, 100, 2),
           total_value, new_price + accrued,
           duration_estimate, DURATION(bond_issue, bond_maturity, bond_coupon, scenario_yield, 2),
           HSTACK(rate_change, scenario_yield, new_price, accrued, total_value, duration_estimate)))),
     VSTACK("Interest Rate Scenario Analysis",
            HSTACK("Rate Change", "New Yield", "Clean Price", "Accrued Int", "Total Value", "Duration"),
            scenario_analysis))
// Comprehensive scenario analysis including accrued interest

// Portfolio duration and accrued interest summary
=LET(portfolio_analysis, MAP(bond_positions, LAMBDA(position,
       LET(market_value, INDEX(position,1,8),
           bond_duration, DURATION(INDEX(position,1,2), INDEX(position,1,3), 
                                  INDEX(position,1,4), INDEX(position,1,5), 2),
           accrued, ACCRINT(INDEX(position,1,1), INDEX(position,1,6), TODAY(), 
                           INDEX(position,1,4), INDEX(position,1,7), 2),
           duration_contribution, bond_duration * market_value,
           accrued_contribution, accrued * INDEX(position,1,9),  // Number of bonds
           HSTACK(INDEX(position,1,1), market_value, bond_duration, accrued, 
                  duration_contribution, accrued_contribution)))),
     total_market_value, SUM(portfolio_analysis[Market_Value]),
     weighted_duration, SUM(portfolio_analysis[Duration_Contribution]) / total_market_value,
     total_accrued, SUM(portfolio_analysis[Accrued_Total]),
     VSTACK("Portfolio Duration and Accrued Interest Analysis",
            portfolio_analysis,
            "",
            HSTACK("Portfolio Totals:", total_market_value, weighted_duration, total_accrued, "", "")))
```

## Interest Calculation Functions

### [[YIELD]]
Pairs with ACCRINT to provide complete yield analysis, calculating effective yields while accounting for accrued interest in bond transactions.

```spreadsheets
// Bond purchase decision analysis
=LET(purchase_price, 98.50,  // Quoted clean price
     settlement_date, TODAY(),
     accrued_interest, ACCRINT(bond_issue_date, first_coupon_date, settlement_date, coupon_rate, 100, 2),
     total_cost, purchase_price + accrued_interest,
     effective_yield, YIELD(bond_issue_date, maturity_date, coupon_rate, total_cost, 100, 2),
     yield_to_call, IF(call_date<>"", YIELD(bond_issue_date, call_date, coupon_rate, total_cost, 100, 2), "N/A"),
     VSTACK("Bond Purchase Analysis",
            HSTACK("Clean Price:", purchase_price),
            HSTACK("Accrued Interest:", accrued_interest),
            HSTACK("Total Cost:", total_cost),
            HSTACK("Yield to Maturity:", TEXT(effective_yield, "0.00%")),
            HSTACK("Yield to Call:", yield_to_call)))
// Complete purchase analysis with yield calculations

// Comparative yield analysis across bonds
=MAP(bond_opportunities, LAMBDA(bond,
  LET(clean_price, INDEX(bond,1,8),
      settlement, TODAY(),
      accrued, ACCRINT(INDEX(bond,1,2), INDEX(bond,1,6), settlement, INDEX(bond,1,4), 100, 2),
      dirty_price, clean_price + accrued,
      ytm, YIELD(INDEX(bond,1,2), INDEX(bond,1,3), INDEX(bond,1,4), dirty_price, 100, 2),
      current_yield, INDEX(bond,1,4) / dirty_price * 100,
      HSTACK(INDEX(bond,1,1), clean_price, accrued, dirty_price, 
             TEXT(ytm, "0.00%"), TEXT(current_yield, "0.00%")))))
// Comparative yield analysis including accrued interest

// Monthly yield tracking with accrued interest
=LET(monthly_dates, MAP(SEQUENCE(12), LAMBDA(month, EOMONTH(DATE(2023,1,1), month-1))),
     yield_analysis, MAP(monthly_dates, LAMBDA(month_end,
       LET(accrued_at_month, ACCRINT(bond_issue, first_payment, month_end, coupon_rate, 100, 2),
           market_price_clean, INDEX(historical_prices, MATCH(month_end, historical_prices[Date], 1), 2),
           dirty_price, market_price_clean + accrued_at_month,
           monthly_yield, YIELD(bond_issue, maturity, coupon_rate, dirty_price, 100, 2),
           HSTACK(TEXT(month_end, "mmm-yy"), market_price_clean, accrued_at_month, 
                  dirty_price, TEXT(monthly_yield, "0.00%"))))),
     VSTACK("Monthly Bond Yield Analysis",
            HSTACK("Month", "Clean Price", "Accrued Int", "Dirty Price", "YTM"),
            yield_analysis))
```

### [[COUPDAYS]]
Combines with ACCRINT to provide detailed coupon period analysis, essential for accurate accrued interest calculations.

```spreadsheets
// Detailed coupon period breakdown
=LET(settlement_date, TODAY(),
     total_days_in_period, COUPDAYS(bond_issue, maturity, settlement_date, 2),
     days_from_last_payment, COUPDAYBS(bond_issue, maturity, settlement_date, 2),
     accrued_interest, ACCRINT(bond_issue, first_payment, settlement_date, coupon_rate, par_value, 2),
     daily_accrual_rate, coupon_rate * par_value / 2 / total_days_in_period,  // Semi-annual
     calculated_accrued, daily_accrual_rate * days_from_last_payment,
     VSTACK("Coupon Period Analysis",
            HSTACK("Total Days in Period:", total_days_in_period),
            HSTACK("Days from Last Payment:", days_from_last_payment),
            HSTACK("Daily Accrual Rate:", TEXT(daily_accrual_rate, "$0.00")),
            HSTACK("ACCRINT Result:", TEXT(accrued_interest, "$0.00")),
            HSTACK("Manual Calculation:", TEXT(calculated_accrued, "$0.00")),
            HSTACK("Difference:", TEXT(accrued_interest - calculated_accrued, "$0.00"))))
// Verification of ACCRINT calculation methodology

// Bond trading day analysis
=MAP(trading_dates, LAMBDA(trade_date,
  LET(coupon_period_days, COUPDAYS(bond_issue, maturity, trade_date, 2),
      days_elapsed, COUPDAYBS(bond_issue, maturity, trade_date, 2),
      days_remaining, coupon_period_days - days_elapsed,
      accrued_to_date, ACCRINT(bond_issue, first_payment, trade_date, coupon_rate, 100, 2),
      accrued_percentage, accrued_to_date / (coupon_rate * 100 / 2) * 100,
      next_payment_date, COUPNCD(bond_issue, maturity, trade_date, 2),
      HSTACK(TEXT(trade_date, "mm/dd/yyyy"), coupon_period_days, days_elapsed, 
             days_remaining, accrued_to_date, TEXT(accrued_percentage, "0.0%"),
             TEXT(next_payment_date, "mm/dd/yyyy")))))
// Daily trading analysis with coupon period details

// Accrued interest verification across different day count conventions
=MAP({0,1,2,3,4}, LAMBDA(basis,
  LET(basis_name, CHOOSE(basis+1, "30/360", "Actual/Actual", "Actual/360", "Actual/365", "30/360 EU"),
      coupon_days, COUPDAYS(bond_issue, maturity, settlement_date, 2, basis),
      accrued_calc, ACCRINT(bond_issue, first_payment, settlement_date, coupon_rate, 100, 2, basis),
      HSTACK(basis_name, coupon_days, TEXT(accrued_calc, "$0.0000")))))
// Compare accrued interest across day count conventions
```

## Commonly Used With Functions Examples

### Bond Portfolio Management System
```spreadsheets
// Comprehensive bond portfolio analysis combining multiple financial functions
=LET(
  bond_portfolio, bond_holdings_data,
  analysis_date, TODAY(),
  
  // Enhanced portfolio analysis with ACCRINT and related functions
  portfolio_analysis, MAP(bond_portfolio, LAMBDA(bond,
    LET(
      bond_id, INDEX(bond,1,1),
      issue_date, INDEX(bond,1,2),
      maturity_date, INDEX(bond,1,3),
      coupon_rate, INDEX(bond,1,4),
      current_yield_market, INDEX(bond,1,5),
      first_payment_date, INDEX(bond,1,6),
      par_value, INDEX(bond,1,7),
      quantity, INDEX(bond,1,8),
      frequency, 2,  // Semi-annual payments
      
      // Price and interest calculations
      clean_price, PRICE(issue_date, maturity_date, coupon_rate, current_yield_market, 100, frequency),
      accrued_interest, ACCRINT(issue_date, first_payment_date, analysis_date, coupon_rate, 100, frequency),
      dirty_price, clean_price + accrued_interest,
      
      // Duration and risk metrics
      bond_duration, DURATION(issue_date, maturity_date, coupon_rate, current_yield_market, frequency),
      modified_duration, MDURATION(issue_date, maturity_date, coupon_rate, current_yield_market, frequency),
      
      // Portfolio position calculations
      position_market_value, dirty_price * par_value * quantity / 100,
      position_accrued_interest, accrued_interest * par_value * quantity / 100,
      position_clean_value, clean_price * par_value * quantity / 100,
      
      // Next payment analysis
      next_payment_date, COUPNCD(issue_date, maturity_date, analysis_date, frequency),
      days_to_next_payment, next_payment_date - analysis_date,
      next_payment_amount, coupon_rate * par_value * quantity / frequency,
      
      HSTACK(bond_id, clean_price, accrued_interest, dirty_price, bond_duration, 
             modified_duration, position_market_value, position_accrued_interest,
             next_payment_date, days_to_next_payment, next_payment_amount)))),
  
  // Portfolio summary calculations
  total_market_value, SUM(portfolio_analysis[Position_Market_Value]),
  total_accrued_interest, SUM(portfolio_analysis[Position_Accrued_Interest]),
  total_clean_value, SUM(portfolio_analysis[Position_Clean_Value]),
  weighted_avg_duration, SUMPRODUCT(portfolio_analysis[Bond_Duration], 
                                   portfolio_analysis[Position_Market_Value]) / total_market_value,
  weighted_modified_duration, SUMPRODUCT(portfolio_analysis[Modified_Duration],
                                        portfolio_analysis[Position_Market_Value]) / total_market_value,
  
  // Cash flow projections
  upcoming_payments, SORT(FILTER(portfolio_analysis, 
                                portfolio_analysis[Days_To_Next_Payment] <= 90), 
                         10, 1),  // Sort by days to payment
  quarterly_cash_flow, SUM(upcoming_payments[Next_Payment_Amount]),
  
  // Risk analysis
  duration_risk, weighted_modified_duration * total_market_value / 100,  // DV01 approximation
  
  // Final comprehensive report
  portfolio_dashboard, VSTACK(
    HSTACK("=== BOND PORTFOLIO ANALYSIS ===", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Analysis Date:", TEXT(analysis_date, "mm/dd/yyyy"), "Total Holdings:", ROWS(bond_portfolio), "", "", "", "", "", "", "", ""),
    "",
    HSTACK("=== PORTFOLIO SUMMARY ===", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Total Market Value:", TEXT(total_market_value, "$#,##0,K"), 
           "Clean Value:", TEXT(total_clean_value, "$#,##0,K"),
           "Total Accrued:", TEXT(total_accrued_interest, "$#,##0"), "", "", "", "", "", "", ""),
    HSTACK("Weighted Avg Duration:", ROUND(weighted_avg_duration, 2),
           "Modified Duration:", ROUND(weighted_modified_duration, 2),
           "Duration Risk (DV01):", TEXT(duration_risk, "$#,##0"), "", "", "", "", "", "", ""),
    "",
    HSTACK("=== INDIVIDUAL BOND ANALYSIS ===", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Bond ID", "Clean Price", "Accrued Int", "Dirty Price", "Duration", 
           "Mod Duration", "Market Value", "Accrued $", "Next Payment", "Days", "Payment $"),
    portfolio_analysis,
    "",
    HSTACK("=== UPCOMING PAYMENTS (Next 90 Days) ===", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Total Payments Due:", TEXT(quarterly_cash_flow, "$#,##0"), "", "", "", "", "", "", "", "", ""),
    upcoming_payments[{1,9,10,11}]  // Show bond ID, payment date, days, amount
  ),
  
  portfolio_dashboard)
```

### Bond Trading Settlement Calculator
```spreadsheets
// Complete bond trading settlement system with all cost components
=LET(
  trade_details, bond_trade_inputs,
  
  // Enhanced settlement calculations
  trade_settlement_analysis, MAP(trade_details, LAMBDA(trade,
    LET(
      trade_id, INDEX(trade,1,1),
      bond_cusip, INDEX(trade,1,2),
      trade_date, INDEX(trade,1,3),
      settlement_date, INDEX(trade,1,4),
      trade_price, INDEX(trade,1,5),  // Clean price
      quantity, INDEX(trade,1,6),
      trade_type, INDEX(trade,1,7),  // "BUY" or "SELL"
      
      // Bond characteristics lookup
      bond_info, XLOOKUP(bond_cusip, bond_master[CUSIP], bond_master),
      issue_date, INDEX(bond_info, 1, 2),
      maturity_date, INDEX(bond_info, 1, 3),
      coupon_rate, INDEX(bond_info, 1, 4),
      first_payment_date, INDEX(bond_info, 1, 5),
      par_value, 1000,  // Standard par value
      frequency, 2,     // Semi-annual
      
      // Price and interest calculations
      accrued_interest, ACCRINT(issue_date, first_payment_date, settlement_date, 
                               coupon_rate, par_value, frequency),
      dirty_price, (trade_price / 100 * par_value) + accrued_interest,
      
      // Settlement amount calculations
      principal_amount, trade_price / 100 * par_value * quantity,
      accrued_interest_total, accrued_interest * quantity,
      gross_settlement, principal_amount + accrued_interest_total,
      
      // Commission and fees
      commission_rate, 0.00125,  // 12.5 basis points
      commission_amount, MAX(25, gross_settlement * commission_rate),  // Minimum $25
      sec_fee, IF(trade_type="SELL", gross_settlement * 0.0000051, 0),  // SEC fee on sells
      other_fees, 5,  // Processing fee
      total_fees, commission_amount + sec_fee + other_fees,
      
      // Net settlement calculation
      net_settlement, IF(trade_type="BUY", 
                        gross_settlement + total_fees,
                        gross_settlement - total_fees),
      
      // Yield calculations
      current_yield, coupon_rate * par_value / dirty_price * 100,
      ytm, YIELD(issue_date, maturity_date, coupon_rate, dirty_price/par_value*100, 100, frequency),
      
      // Days and period information
      coupon_days, COUPDAYS(issue_date, maturity_date, settlement_date, frequency),
      days_accrued, COUPDAYBS(issue_date, maturity_date, settlement_date, frequency),
      next_coupon_date, COUPNCD(issue_date, maturity_date, settlement_date, frequency),
      
      HSTACK(trade_id, bond_cusip, TEXT(settlement_date, "mm/dd/yyyy"), 
             trade_type, quantity, trade_price, accrued_interest, dirty_price,
             principal_amount, accrued_interest_total, gross_settlement,
             commission_amount, sec_fee, other_fees, total_fees, net_settlement,
             TEXT(current_yield, "0.00%"), TEXT(ytm, "0.00%"),
             coupon_days, days_accrued, TEXT(next_coupon_date, "mm/dd/yyyy"))))),
  
  // Trade summary by type
  buy_trades, FILTER(trade_settlement_analysis, trade_settlement_analysis[Trade_Type] = "BUY"),
  sell_trades, FILTER(trade_settlement_analysis, trade_settlement_analysis[Trade_Type] = "SELL"),
  
  buy_summary, VSTACK("BUY TRADES SUMMARY:",
                     HSTACK("Number of Trades:", ROWS(buy_trades)),
                     HSTACK("Total Principal:", TEXT(SUM(buy_trades[Principal_Amount]), "$#,##0,K")),
                     HSTACK("Total Accrued Interest:", TEXT(SUM(buy_trades[Accrued_Interest_Total]), "$#,##0")),
                     HSTACK("Total Fees:", TEXT(SUM(buy_trades[Total_Fees]), "$#,##0")),
                     HSTACK("Net Cash Required:", TEXT(SUM(buy_trades[Net_Settlement]), "$#,##0,K"))),
  
  sell_summary, VSTACK("SELL TRADES SUMMARY:",
                      HSTACK("Number of Trades:", ROWS(sell_trades)),
                      HSTACK("Total Principal:", TEXT(SUM(sell_trades[Principal_Amount]), "$#,##0,K")),
                      HSTACK("Total Accrued Interest:", TEXT(SUM(sell_trades[Accrued_Interest_Total]), "$#,##0")),
                      HSTACK("Total Fees:", TEXT(SUM(sell_trades[Total_Fees]), "$#,##0")),
                      HSTACK("Net Cash Received:", TEXT(SUM(sell_trades[Net_Settlement]), "$#,##0,K"))),
  
  // Complete settlement report
  settlement_report, VSTACK(
    HSTACK("=== BOND TRADING SETTLEMENT REPORT ===", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Settlement Date Range:", TEXT(MIN(trade_settlement_analysis[Settlement_Date]), "mm/dd/yyyy"), 
           "to", TEXT(MAX(trade_settlement_analysis[Settlement_Date]), "mm/dd/yyyy"), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
    "",
    HSTACK("=== DETAILED TRADE ANALYSIS ===", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
    HSTACK("Trade ID", "CUSIP", "Settlement", "Type", "Quantity", "Clean Price", "Accrued Int", "Dirty Price",
           "Principal", "Accrued $", "Gross", "Commission", "SEC Fee", "Other", "Total Fees", "Net Settlement",
           "Current Yield", "YTM", "Period Days", "Accrued Days", "Next Coupon"),
    trade_settlement_analysis,
    "",
    buy_summary,
    "",
    sell_summary,
    "",
    HSTACK("NET CASH FLOW:", TEXT(SUM(sell_trades[Net_Settlement]) - SUM(buy_trades[Net_Settlement]), "$#,##0,K"), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
  ),
  
  settlement_report)
```

### Interest Income Recognition System
```spreadsheets
// Comprehensive interest income tracking and recognition system
=LET(
  portfolio_holdings, fixed_income_portfolio,
  reporting_period_start, DATE(2023,1,1),
  reporting_period_end, DATE(2023,12,31),
  
  // Monthly interest accrual analysis
  monthly_accruals, MAP(SEQUENCE(12), LAMBDA(month,
    LET(
      month_start, EOMONTH(reporting_period_start, month-2) + 1,
      month_end, EOMONTH(reporting_period_start, month-1),
      
      // Calculate accruals for each bond at month start and end
      month_accrual_detail, MAP(portfolio_holdings, LAMBDA(bond,
        LET(
          bond_id, INDEX(bond,1,1),
          issue_date, INDEX(bond,1,2),
          maturity_date, INDEX(bond,1,3),
          coupon_rate, INDEX(bond,1,4),
          first_payment_date, INDEX(bond,1,6),
          par_value, INDEX(bond,1,7),
          quantity, INDEX(bond,1,8),
          frequency, 2,
          
          // Accrued interest at start and end of month
          accrued_start, IF(month_start >= issue_date,
                           ACCRINT(issue_date, first_payment_date, month_start, coupon_rate, par_value, frequency),
                           0),
          accrued_end, IF(month_end <= maturity_date,
                         ACCRINT(issue_date, first_payment_date, month_end, coupon_rate, par_value, frequency),
                         0),
          
          // Monthly accrual (handling coupon payments)
          coupon_payments_in_month, MAP(SEQUENCE(frequency*2), LAMBDA(pmt,
            LET(payment_date, EDATE(first_payment_date, (pmt-1) * 12/frequency),
                payment_amount, IF(AND(payment_date >= month_start, payment_date <= month_end,
                                     payment_date <= maturity_date), 
                                  coupon_rate * par_value / frequency, 0),
                payment_amount * quantity))),
          total_coupon_payments, SUM(coupon_payments_in_month),
          
          monthly_interest_income, (accrued_end - accrued_start) * quantity + total_coupon_payments,
          
          HSTACK(bond_id, TEXT(month_start, "mm/dd"), TEXT(month_end, "mm/dd"),
                 accrued_start * quantity, accrued_end * quantity, total_coupon_payments,
                 monthly_interest_income)))),
      
      month_total, SUM(month_accrual_detail[Monthly_Interest_Income]),
      
      VSTACK(HSTACK("=== " & TEXT(month_end, "MMMM YYYY") & " INTEREST INCOME ===", "", "", "", "", "", ""),
             HSTACK("Bond ID", "Period Start", "Period End", "Accrued Start", "Accrued End", "Coupons Received", "Total Income"),
             month_accrual_detail,
             HSTACK("MONTHLY TOTAL:", "", "", "", "", "", TEXT(month_total, "$#,##0")),
             "")))),
  
  // Quarterly summary for financial reporting
  quarterly_summary, MAP({1,2,3,4}, LAMBDA(quarter,
    LET(
      q_start, DATE(YEAR(reporting_period_start), (quarter-1)*3+1, 1),
      q_end, EOMONTH(q_start, 2),
      
      quarter_detail, MAP(portfolio_holdings, LAMBDA(bond,
        LET(
          bond_id, INDEX(bond,1,1),
          issue_date, INDEX(bond,1,2),
          first_payment_date, INDEX(bond,1,6),
          coupon_rate, INDEX(bond,1,4),
          par_value, INDEX(bond,1,7),
          quantity, INDEX(bond,1,8),
          
          accrued_q_start, IF(q_start >= issue_date,
                             ACCRINT(issue_date, first_payment_date, q_start, coupon_rate, par_value, 2),
                             0),
          accrued_q_end, ACCRINT(issue_date, first_payment_date, q_end, coupon_rate, par_value, 2),
          
          quarterly_accrual, (accrued_q_end - accrued_q_start) * quantity,
          
          // Check for coupon payments in quarter
          coupon_payment_dates, MAP({1,2}, LAMBDA(pmt,
            EDATE(first_payment_date, (pmt-1) * 6))),  // Semi-annual payments
          coupons_in_quarter, SUMPRODUCT((coupon_payment_dates >= q_start) * 
                                       (coupon_payment_dates <= q_end) *
                                       (coupon_rate * par_value / 2 * quantity)),
          
          total_quarterly_income, quarterly_accrual + coupons_in_quarter,
          
          HSTACK(bond_id, TEXT(q_start, "mm/dd"), TEXT(q_end, "mm/dd"),
                 accrued_q_start * quantity, accrued_q_end * quantity,
                 coupons_in_quarter, total_quarterly_income)))),
      
      quarter_total, SUM(quarter_detail[Quarterly_Income]),
      
      VSTACK(HSTACK("Q" & quarter & " " & YEAR(q_start) & " SUMMARY", "", "", "", "", "", ""),
             quarter_detail,
             HSTACK("QUARTER TOTAL:", "", "", "", "", "", TEXT(quarter_total, "$#,##0")),
             "")))),
  
  // Annual interest income summary
  annual_summary, LET(
    total_interest_income, SUM(FLATTEN(monthly_accruals[Monthly_Interest_Income])),
    taxable_interest, total_interest_income,  // Assuming all taxable
    
    bond_level_annual, MAP(portfolio_holdings, LAMBDA(bond,
      LET(
        bond_id, INDEX(bond,1,1),
        coupon_rate, INDEX(bond,1,4),
        par_value, INDEX(bond,1,7),
        quantity, INDEX(bond,1,8),
        
        annual_coupon_income, coupon_rate * par_value * quantity,
        accrued_start_year, ACCRINT(INDEX(bond,1,2), INDEX(bond,1,6), reporting_period_start, 
                                   coupon_rate, par_value, 2) * quantity,
        accrued_end_year, ACCRINT(INDEX(bond,1,2), INDEX(bond,1,6), reporting_period_end, 
                                 coupon_rate, par_value, 2) * quantity,
        net_accrual_change, accrued_end_year - accrued_start_year,
        total_annual_income, annual_coupon_income + net_accrual_change,
        
        HSTACK(bond_id, TEXT(annual_coupon_income, "$#,##0"), 
               TEXT(net_accrual_change, "$#,##0"), TEXT(total_annual_income, "$#,##0"))))),
    
    VSTACK("=== ANNUAL INTEREST INCOME SUMMARY ===",
           HSTACK("Bond ID", "Coupon Income", "Accrual Change", "Total Income"),
           bond_level_annual,
           "",
           HSTACK("TOTAL ANNUAL INCOME:", TEXT(total_interest_income, "$#,##0,K")),
           HSTACK("TAXABLE AMOUNT:", TEXT(taxable_interest, "$#,##0,K")))),
  
  // Complete interest income report
  interest_income_report, VSTACK(
    HSTACK("=== FIXED INCOME INTEREST RECOGNITION REPORT ===", "", "", "", "", "", ""),
    HSTACK("Reporting Period:", TEXT(reporting_period_start, "mm/dd/yyyy"), 
           "to", TEXT(reporting_period_end, "mm/dd/yyyy"), "", "", ""),
    HSTACK("Number of Holdings:", ROWS(portfolio_holdings), "", "", "", "", ""),
    "",
    annual_summary,
    "",
    quarterly_summary,
    "",
    monthly_accruals),
  
  interest_income_report)
```
