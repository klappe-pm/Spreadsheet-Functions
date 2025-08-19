---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: excel
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# SCAN

## SCAN Description

Scans through an array and produces intermediate accumulated results by applying a LAMBDA function at each step. Unlike REDUCE which returns only the final result, SCAN returns an array showing the progression of values at each stage, enabling running totals, cumulative calculations, and step-by-step transformations.

> [!f(x)] SCAN Syntax
>
> ```spreadsheets
> SCAN(initial_value, array, lambda_function)
> ```
>
> **Parameters:**
> - `initial_value` (required): Starting value for the scanning process
> - `array` (required): Array of values to scan through
> - `lambda_function` (required): LAMBDA function that takes (accumulator, current_value) and returns the next accumulated value

> [!f(x)] SCAN Examples
>
> ```spreadsheets
> // Running sum (cumulative total)
> SCAN(0, {10,20,30,40}, LAMBDA(acc, val, acc + val)) → {10,30,60,100}
> 
> // Running product
> SCAN(1, {2,3,4,5}, LAMBDA(acc, val, acc * val)) → {2,6,24,120}
> 
> // Running maximum
> SCAN(0, {5,2,8,3,9,1}, LAMBDA(acc, val, MAX(acc, val))) → {5,5,8,8,9,9}
> 
> // Progressive text concatenation
> SCAN("", {"A","B","C","D"}, LAMBDA(acc, val, acc & val)) → {"A","AB","ABC","ABCD"}
> 
> // Compound interest progression
> SCAN(1000, {0.05,0.05,0.05}, LAMBDA(acc, rate, acc * (1 + rate))) → {1050,1102.5,1157.625}
> ```

## Use Cases

### [[Running calculations]]
- **Cumulative totals**: Create running sums, running averages, or progressive calculations for financial statements and dashboards
- **Progress tracking**: Monitor step-by-step progress through processes, showing intermediate milestones and achievement levels
- **Growth analysis**: Track compound growth, cumulative returns, or progressive changes over time periods
- **Performance monitoring**: Generate running performance metrics, efficiency ratios, or quality scores throughout periods

### [[Time series analysis]]
- **Moving calculations**: Build moving averages, running standard deviations, or progressive trend analysis for forecasting
- **Seasonal adjustments**: Apply cumulative seasonal factors, trend corrections, or progressive normalizations
- **Index calculations**: Create cumulative index values, progressive benchmarking, or relative performance tracking
- **Forecast progression**: Generate step-by-step forecasts showing how predictions evolve with each new data point

### [[State management]]
- **Workflow progression**: Track state changes through business processes, approval workflows, or multi-stage operations
- **Inventory tracking**: Monitor running inventory levels, cumulative consumption, or progressive stock adjustments
- **Budget tracking**: Create running budget balances, cumulative spending, or progressive variance analysis
- **Resource allocation**: Track progressive resource utilization, cumulative assignments, or step-by-step distribution

### [[Financial modeling]]
- **Cash flow analysis**: Generate running cash balances, cumulative cash flows, or progressive liquidity analysis
- **Investment growth**: Track progressive portfolio values, cumulative returns, or step-by-step performance evolution
- **Loan amortization**: Calculate running principal balances, cumulative interest payments, or progressive equity building
- **Risk assessment**: Build progressive risk accumulation, cumulative exposure analysis, or step-by-step risk evaluation

## Related

### Similar Functions

- [[REDUCE]] - Returns only final accumulated value, SCAN shows all intermediate results
- [[SUM]] - Static total, SCAN shows progressive summation at each step
- [[CUMULATIVE]] - Basic running totals, SCAN enables custom accumulation logic
- [[LAMBDA]] - Defines custom accumulation logic used within SCAN operations
- [[MAP]] - Transforms arrays, SCAN accumulates transformations progressively

## Mathematical Functions

### [[SUM]]
SCAN extends SUM to show the progressive accumulation rather than just the final total.

```spreadsheets
// Running sum progression
=SCAN(0, monthly_sales, LAMBDA(acc, sale, acc + sale))
// Shows cumulative sales at each month: {Jan, Jan+Feb, Jan+Feb+Mar, ...}

// Conditional running sum
=SCAN(0, sales_data, LAMBDA(acc, sale,
   acc + IF(sale > target, sale * 1.1, sale)))
// Progressive sum with bonus multiplier for exceeding targets

// Weighted running sum
=SCAN(0, MAP(values, weights, LAMBDA(v, w, v * w)),
      LAMBDA(acc, weighted_val, acc + weighted_val))
// Cumulative weighted total showing progressive contribution
```

### [[AVERAGE]]
Combines with SCAN to create running averages and progressive statistical analysis.

```spreadsheets
// Running average calculation
=SCAN({0, 0}, data_array, LAMBDA(acc, val,
   LET(sum, INDEX(acc, 1, 1) + val,
       count, INDEX(acc, 1, 2) + 1,
       {sum, count})))
// Returns array of {sum, count} pairs for calculating running average

// Quality score progression
=SCAN(0, quality_scores, LAMBDA(acc, score,
   (acc * (ROW(score) - 1) + score) / ROW(score)))
// Running average quality score at each measurement

// Progressive variance tracking
=SCAN({0, 0, 0}, measurements, LAMBDA(acc, val,
   LET(count, INDEX(acc, 1, 1) + 1,
       sum, INDEX(acc, 1, 2) + val,
       sum_sq, INDEX(acc, 1, 3) + val^2,
       {count, sum, sum_sq})))
// Accumulates data needed for progressive variance calculation
```

## Financial Functions

### [[PMT]] and Loan Analysis
SCAN creates detailed amortization schedules and progressive loan analysis.

```spreadsheets
// Loan balance progression
=SCAN(loan_principal, SEQUENCE(loan_terms), LAMBDA(balance, period,
   LET(interest_payment, balance * monthly_rate,
       principal_payment, monthly_payment - interest_payment,
       new_balance, balance - principal_payment,
       new_balance)))
// Shows remaining balance after each payment

// Progressive interest accumulation
=SCAN(0, loan_balances, LAMBDA(acc_interest, balance,
   acc_interest + balance * monthly_rate))
// Cumulative interest paid over loan life

// Equity building progression
=SCAN(0, principal_payments, LAMBDA(acc_equity, payment,
   acc_equity + payment))
// Running total of equity built through principal payments
```

### Investment Growth Analysis
Tracks progressive investment performance and cumulative returns.

```spreadsheets
// Portfolio value progression
=SCAN(initial_investment, monthly_returns, LAMBDA(value, return,
   value * (1 + return)))
// Shows portfolio value after each month's return

// Cumulative return calculation
=SCAN(1, periodic_returns, LAMBDA(acc_return, period_return,
   acc_return * (1 + period_return)))
// Progressive total return multiplier

// Risk-adjusted performance tracking
=SCAN({initial_value, 0}, MAP(returns, volatilities, LAMBDA(ret, vol, {ret, vol})),
      LAMBDA(acc, metrics,
        LET(current_value, INDEX(acc, 1, 1),
            risk_adjustment, INDEX(metrics, 1, 2),
            period_return, INDEX(metrics, 1, 1),
            adjusted_return, period_return - risk_adjustment * 0.5,
            new_value, current_value * (1 + adjusted_return),
            {new_value, risk_adjustment})))
// Progressive risk-adjusted value calculation
```

## Text Processing Functions

### [[CONCATENATE]]
SCAN enables progressive text building and cumulative string construction.

```spreadsheets
// Progressive list building
=SCAN("", product_names, LAMBDA(acc, product,
   IF(acc = "", product, acc & ", " & product)))
// Builds progressive comma-separated lists

// Cumulative report generation
=SCAN("Report Summary:", data_points, LAMBDA(acc, data,
   acc & CHAR(10) & "• " & TEXT(data, "#,##0")))
// Progressive report building with line breaks

// Progressive SQL query construction
=SCAN("SELECT * FROM table WHERE 1=1", conditions, LAMBDA(acc, condition,
   acc & " AND " & condition))
// Builds SQL query progressively adding conditions
```

### Text Analysis Progression
Creates cumulative text analysis showing progressive statistics.

```spreadsheets
// Progressive word count
=SCAN(0, text_array, LAMBDA(acc, text,
   acc + LEN(text) - LEN(SUBSTITUTE(text, " ", "")) + 1))
// Running word count across text entries

// Cumulative character analysis
=SCAN({0, 0}, text_entries, LAMBDA(acc, text,
   LET(total_chars, INDEX(acc, 1, 1) + LEN(text),
       total_words, INDEX(acc, 1, 2) + LEN(text) - LEN(SUBSTITUTE(text, " ", "")) + 1,
       {total_chars, total_words})))
// Progressive text statistics accumulation
```

## Commonly Used With Functions Examples

### Progressive Financial Dashboard with Real-Time Metrics
```spreadsheets
// Create comprehensive financial tracking with SCAN showing progression over time
=LET(
  months, {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"},
  revenue, {125000, 132000, 128000, 145000, 138000, 155000, 162000, 158000, 170000, 175000, 168000, 185000},
  expenses, {95000, 98000, 102000, 108000, 105000, 112000, 118000, 115000, 125000, 128000, 122000, 135000},
  targets, {120000, 125000, 130000, 135000, 140000, 145000, 150000, 155000, 160000, 165000, 170000, 175000},
  
  // Progressive revenue analysis using SCAN
  cumulative_revenue, SCAN(0, revenue, LAMBDA(acc, monthly_rev, acc + monthly_rev)),
  running_avg_revenue, SCAN({0, 0}, revenue, LAMBDA(acc, monthly_rev,
    LET(total, INDEX(acc, 1, 1) + monthly_rev,
        count, INDEX(acc, 1, 2) + 1,
        {total, count}))),
  
  // Progressive profitability tracking
  monthly_profit, MAP(revenue, expenses, LAMBDA(rev, exp, rev - exp)),
  cumulative_profit, SCAN(0, monthly_profit, LAMBDA(acc, profit, acc + profit)),
  profit_margin_progression, MAP(cumulative_revenue, cumulative_profit, 
    LAMBDA(cum_rev, cum_profit, IF(cum_rev > 0, cum_profit / cum_rev, 0))),
  
  // Target achievement progression
  target_achievement, SCAN({0, 0, 0}, MAP(revenue, targets, LAMBDA(rev, target, {rev, target, IF(rev >= target, 1, 0)})),
    LAMBDA(acc, metrics,
      LET(total_revenue, INDEX(acc, 1, 1) + INDEX(metrics, 1, 1),
          total_targets, INDEX(acc, 1, 2) + INDEX(metrics, 1, 2),
          achievements, INDEX(acc, 1, 3) + INDEX(metrics, 1, 3),
          {total_revenue, total_targets, achievements}))),
  
  // Progressive performance scoring
  performance_scores, SCAN(100, MAP(revenue, targets, expenses, LAMBDA(rev, target, exp,
    LET(revenue_score, MIN(150, rev / target * 100),
        efficiency_score, MAX(50, 150 - (exp / rev * 100)),
        composite_score, (revenue_score + efficiency_score) / 2,
        composite_score))),
    LAMBDA(acc_score, monthly_score, (acc_score * 0.8) + (monthly_score * 0.2))),
  
  // Cash flow progression analysis
  initial_cash, 50000,
  cash_flow_progression, SCAN(initial_cash, monthly_profit, LAMBDA(cash_balance, profit,
    LET(new_balance, cash_balance + profit,
        minimum_balance, 25000,
        IF(new_balance < minimum_balance, 
           new_balance + 50000,  // Simulate line of credit draw
           new_balance)))),
  
  // Growth rate progression
  growth_rates, SCAN(0, MAP(SEQUENCE(ROWS(revenue)-1, 1, 2), LAMBDA(i, 
    (INDEX(revenue, i, 1) - INDEX(revenue, i-1, 1)) / INDEX(revenue, i-1, 1))),
    LAMBDA(acc_growth, monthly_growth, 
      IF(acc_growth = 0, monthly_growth, (acc_growth + monthly_growth) / 2))),
  
  // Create comprehensive dashboard report
  dashboard_metrics, MAP(SEQUENCE(ROWS(months)), LAMBDA(i,
    LET(month, INDEX(months, i, 1),
        monthly_rev, INDEX(revenue, i, 1),
        cum_rev, INDEX(cumulative_revenue, i, 1),
        running_avg, INDEX(running_avg_revenue, i, 1, 1) / INDEX(running_avg_revenue, i, 1, 2),
        monthly_prof, INDEX(monthly_profit, i, 1),
        cum_profit, INDEX(cumulative_profit, i, 1),
        profit_margin, INDEX(profit_margin_progression, i, 1),
        perf_score, INDEX(performance_scores, i, 1),
        cash_position, INDEX(cash_flow_progression, i, 1),
        
        dashboard_line, CONCAT(
          month, ": Rev $", TEXT(monthly_rev, "#,##0"), 
          " (Cum: $", TEXT(cum_rev, "#,##0"), 
          ", Avg: $", TEXT(running_avg, "#,##0"), ")",
          " | Profit $", TEXT(monthly_prof, "#,##0"), 
          " (Cum: $", TEXT(cum_profit, "#,##0"), 
          ", Margin: ", TEXT(profit_margin, "0.0%"), ")",
          " | Score: ", TEXT(perf_score, "0.0"),
          " | Cash: $", TEXT(cash_position, "#,##0")),
        dashboard_line))),
  
  // Calculate key performance indicators
  total_revenue, SUM(revenue),
  total_profit, SUM(monthly_profit),
  avg_monthly_revenue, AVERAGE(revenue),
  final_profit_margin, INDEX(profit_margin_progression, ROWS(profit_margin_progression), 1),
  months_above_target, INDEX(target_achievement, ROWS(target_achievement), 1, 3),
  final_performance_score, INDEX(performance_scores, ROWS(performance_scores), 1),
  
  // Final comprehensive dashboard
  financial_dashboard, VSTACK(
    "=== PROGRESSIVE FINANCIAL DASHBOARD ===",
    "",
    "Monthly Performance Progression:",
    TRANSPOSE(dashboard_metrics),
    "",
    "Key Performance Summary:",
    CONCAT("Total Revenue: $", TEXT(total_revenue, "#,##0")),
    CONCAT("Total Profit: $", TEXT(total_profit, "#,##0")),
    CONCAT("Average Monthly Revenue: $", TEXT(avg_monthly_revenue, "#,##0")),
    CONCAT("Final Profit Margin: ", TEXT(final_profit_margin, "0.0%")),
    CONCAT("Months Above Target: ", TEXT(months_above_target, "0"), " of ", TEXT(ROWS(months), "0")),
    CONCAT("Final Performance Score: ", TEXT(final_performance_score, "0.0")),
    CONCAT("Ending Cash Position: $", TEXT(INDEX(cash_flow_progression, ROWS(cash_flow_progression), 1), "#,##0"))),
  
  financial_dashboard)
```

### Customer Lifetime Value Progression and Retention Analysis
```spreadsheets
// Build progressive customer value analysis using SCAN for cumulative insights
=LET(
  customer_cohorts, {"Jan Cohort", "Feb Cohort", "Mar Cohort", "Apr Cohort", "May Cohort", "Jun Cohort"},
  initial_customers, {100, 125, 150, 175, 200, 180},
  monthly_churn_rates, {0.05, 0.04, 0.06, 0.05, 0.04, 0.05},  // Monthly churn rate per cohort
  monthly_revenue_per_customer, {45, 42, 48, 50, 46, 44},
  acquisition_costs, {75, 80, 70, 85, 78, 72},
  
  // Progressive customer retention using SCAN
  retention_progression, MAP(initial_customers, monthly_churn_rates, LAMBDA(initial, churn_rate,
    SCAN(initial, SEQUENCE(12), LAMBDA(remaining, month,
      remaining * (1 - churn_rate))))),
  
  // Progressive revenue per cohort
  cohort_revenue_progression, MAP(retention_progression, monthly_revenue_per_customer, 
    LAMBDA(retention_array, monthly_rev,
      SCAN(0, retention_array, LAMBDA(cum_revenue, customers,
        cum_revenue + customers * monthly_rev)))),
  
  // Progressive customer acquisition cost recovery
  cac_recovery_progression, MAP(cohort_revenue_progression, acquisition_costs, initial_customers,
    LAMBDA(revenue_array, acq_cost, initial_count,
      LET(total_acquisition_cost, acq_cost * initial_count,
          recovery_progression, SCAN(0, revenue_array, LAMBDA(recovered, monthly_revenue,
            MIN(1, (recovered + monthly_revenue) / total_acquisition_cost))),
          recovery_progression))),
  
  // Progressive lifetime value calculation
  clv_progression, MAP(cohort_revenue_progression, acquisition_costs, initial_customers,
    LAMBDA(revenue_array, acq_cost, initial_count,
      MAP(revenue_array, LAMBDA(cum_revenue,
        (cum_revenue / initial_count) - acq_cost)))),
  
  // Progressive cohort health scoring
  cohort_health_scores, MAP(retention_progression, clv_progression, LAMBDA(retention_array, clv_array,
    SCAN(100, MAP(retention_array, clv_array, LAMBDA(customers, clv, {customers, clv})),
      LAMBDA(acc_health, metrics,
        LET(customer_count, INDEX(metrics, 1, 1),
            current_clv, INDEX(metrics, 1, 2),
            retention_score, MIN(100, customer_count / INDEX(retention_array, 1, 1) * 100),
            clv_score, MAX(0, MIN(100, (current_clv + 100) * 0.5)),
            composite_health, (retention_score * 0.6) + (clv_score * 0.4),
            (acc_health * 0.7) + (composite_health * 0.3)))))),
  
  // Progressive market analysis
  market_penetration, SCAN({0, 0}, MAP(initial_customers, LAMBDA(cohort_size,
    {cohort_size, RANDBETWEEN(5000, 10000)})),  // Simulated market size
    LAMBDA(acc, metrics,
      LET(total_customers, INDEX(acc, 1, 1) + INDEX(metrics, 1, 1),
          total_market, INDEX(acc, 1, 2) + INDEX(metrics, 1, 2),
          {total_customers, total_market}))),
  
  // Create comprehensive cohort analysis
  cohort_analysis, MAP(SEQUENCE(ROWS(customer_cohorts)), LAMBDA(cohort_i,
    LET(cohort_name, INDEX(customer_cohorts, cohort_i, 1),
        initial_size, INDEX(initial_customers, cohort_i, 1),
        churn_rate, INDEX(monthly_churn_rates, cohort_i, 1),
        monthly_rev, INDEX(monthly_revenue_per_customer, cohort_i, 1),
        acq_cost, INDEX(acquisition_costs, cohort_i, 1),
        
        // Month 12 metrics
        month_12_customers, INDEX(INDEX(retention_progression, cohort_i, 0), 12, 1),
        month_12_revenue, INDEX(INDEX(cohort_revenue_progression, cohort_i, 0), 12, 1),
        month_12_clv, INDEX(INDEX(clv_progression, cohort_i, 0), 12, 1),
        cac_recovery, INDEX(INDEX(cac_recovery_progression, cohort_i, 0), 12, 1),
        health_score, INDEX(INDEX(cohort_health_scores, cohort_i, 0), 12, 1),
        
        retention_rate, month_12_customers / initial_size,
        revenue_per_surviving_customer, month_12_revenue / month_12_customers,
        
        cohort_summary, CONCAT(
          cohort_name, ": ",
          TEXT(retention_rate, "0.0%"), " retention (",
          TEXT(month_12_customers, "0"), " of ", TEXT(initial_size, "0"), ") | ",
          "CLV: $", TEXT(month_12_clv, "#,##0"), " | ",
          "CAC Recovery: ", TEXT(cac_recovery, "0.0%"), " | ",
          "Health: ", TEXT(health_score, "0.0"), " | ",
          "Rev/Customer: $", TEXT(revenue_per_surviving_customer, "#,##0")),
        cohort_summary))),
  
  // Calculate aggregate metrics using SCAN results
  total_customers_acquired, SUM(initial_customers),
  total_acquisition_investment, SUMPRODUCT(initial_customers, acquisition_costs),
  total_12_month_revenue, SUM(MAP(cohort_revenue_progression, LAMBDA(revenue_array,
    INDEX(revenue_array, 12, 1)))),
  average_retention_rate, AVERAGE(MAP(retention_progression, initial_customers, LAMBDA(retention_array, initial,
    INDEX(retention_array, 12, 1) / initial))),
  blended_clv, total_12_month_revenue / total_customers_acquired,
  overall_cac_recovery, total_12_month_revenue / total_acquisition_investment,
  
  // Final comprehensive retention and CLV report
  retention_report, VSTACK(
    "=== CUSTOMER LIFETIME VALUE PROGRESSION ANALYSIS ===",
    "",
    "Cohort Performance Summary (12-Month Progression):",
    TRANSPOSE(cohort_analysis),
    "",
    "Aggregate Business Metrics:",
    CONCAT("Total Customers Acquired: ", TEXT(total_customers_acquired, "#,##0")),
    CONCAT("Total Acquisition Investment: $", TEXT(total_acquisition_investment, "#,##0")),
    CONCAT("Total 12-Month Revenue: $", TEXT(total_12_month_revenue, "#,##0")),
    CONCAT("Average Customer Retention Rate: ", TEXT(average_retention_rate, "0.0%")),
    CONCAT("Blended Customer Lifetime Value: $", TEXT(blended_clv, "#,##0")),
    CONCAT("Overall CAC Recovery Ratio: ", TEXT(overall_cac_recovery, "0.0x")),
    "",
    "Market Penetration Progression:",
    CONCAT("Total Market Captured: ", TEXT(INDEX(market_penetration, ROWS(market_penetration), 1, 1), "#,##0"), " customers"),
    CONCAT("Estimated Total Market Size: ", TEXT(INDEX(market_penetration, ROWS(market_penetration), 1, 2), "#,##0"), " potential customers"),
    CONCAT("Market Penetration Rate: ", TEXT(INDEX(market_penetration, ROWS(market_penetration), 1, 1) / INDEX(market_penetration, ROWS(market_penetration), 1, 2), "0.0%"))),
  
  retention_report)
```

### Supply Chain Resilience and Progressive Risk Assessment
```spreadsheets
// Create comprehensive supply chain risk progression analysis using SCAN
=LET(
  suppliers, {"Alpha Corp", "Beta Industries", "Gamma Solutions", "Delta Manufacturing", "Epsilon Supply"},
  risk_categories, {"Delivery", "Quality", "Financial", "Geopolitical", "Capacity"},
  monthly_risk_scores, {
    {2, 3, 1, 4, 2};  // Alpha Corp scores across categories
    {3, 2, 2, 3, 4};  // Beta Industries
    {1, 4, 3, 2, 3};  // Gamma Solutions
    {4, 1, 2, 5, 1};  // Delta Manufacturing
    {2, 3, 4, 1, 3}   // Epsilon Supply
  },
  supplier_volumes, {2500, 1800, 1200, 3000, 1500},  // Monthly volume
  recovery_times, {7, 14, 21, 5, 10},  // Days to recover from disruption
  
  // Progressive risk accumulation using SCAN
  cumulative_risk_progression, MAP(SEQUENCE(ROWS(suppliers)), LAMBDA(supplier_i,
    LET(supplier_risks, INDEX(monthly_risk_scores, supplier_i, 0),
        volume, INDEX(supplier_volumes, supplier_i, 1),
        recovery_time, INDEX(recovery_times, supplier_i, 1),
        
        // Progressive monthly risk accumulation
        monthly_risk_progression, SCAN(0, SEQUENCE(12), LAMBDA(acc_risk, month,
          LET(base_monthly_risk, AVERAGE(supplier_risks) * (1 + RANDBETWEEN(-20, 20) / 100),
              volume_weight, volume / SUM(supplier_volumes),
              time_factor, recovery_time / 30,  // Normalize to month fraction
              monthly_impact, base_monthly_risk * volume_weight * time_factor,
              progressive_risk, acc_risk + monthly_impact,
              progressive_risk))),
        monthly_risk_progression))),
  
  // Progressive supply chain diversification analysis
  diversification_progression, SCAN({0, 0}, MAP(supplier_volumes, LAMBDA(volume, {volume, volume^2})),
    LAMBDA(acc, metrics,
      LET(total_volume, INDEX(acc, 1, 1) + INDEX(metrics, 1, 1),
          sum_squares, INDEX(acc, 1, 2) + INDEX(metrics, 1, 2),
          hhi_index, sum_squares / (total_volume^2),  // Herfindahl-Hirschman Index
          diversification_score, 1 - hhi_index,
          {total_volume, diversification_score}))),
  
  // Progressive capacity utilization and bottleneck analysis
  capacity_progression, MAP(SEQUENCE(ROWS(suppliers)), LAMBDA(supplier_i,
    LET(base_volume, INDEX(supplier_volumes, supplier_i, 1),
        capacity_utilization, base_volume / (base_volume * 1.5),  // Assume 150% max capacity
        
        utilization_progression, SCAN(capacity_utilization, SEQUENCE(12), LAMBDA(acc_util, month,
          LET(seasonal_factor, 1 + 0.2 * SIN(month / 12 * 2 * PI()),
              demand_growth, 1 + (month - 1) * 0.01,  // 1% monthly growth
              new_utilization, acc_util * seasonal_factor * demand_growth,
              capped_utilization, MIN(1, new_utilization),
              capped_utilization))),
        utilization_progression))),
  
  // Progressive financial impact assessment
  financial_risk_progression, MAP(SEQUENCE(ROWS(suppliers)), LAMBDA(supplier_i,
    LET(supplier, INDEX(suppliers, supplier_i, 1),
        volume, INDEX(supplier_volumes, supplier_i, 1),
        risk_array, INDEX(cumulative_risk_progression, supplier_i, 0),
        
        // Progressive financial impact calculation
        financial_impact_progression, SCAN(0, risk_array, LAMBDA(acc_impact, monthly_risk,
          LET(disruption_probability, monthly_risk / 100,
              potential_loss, volume * 50 * disruption_probability,  // $50 per unit loss
              recovery_cost, disruption_probability * 10000,  // Fixed recovery costs
              total_monthly_impact, potential_loss + recovery_cost,
              cumulative_impact, acc_impact + total_monthly_impact,
              cumulative_impact))),
        financial_impact_progression))),
  
  // Progressive mitigation strategy effectiveness
  mitigation_effectiveness, SCAN({100, 0}, SEQUENCE(12), LAMBDA(acc, month,
    LET(current_effectiveness, INDEX(acc, 1, 1),
        cumulative_investment, INDEX(acc, 1, 2),
        monthly_investment, 5000 + month * 1000,  // Increasing monthly investment
        effectiveness_gain, SQRT(monthly_investment / 1000) * 2,  // Diminishing returns
        new_effectiveness, MIN(95, current_effectiveness + effectiveness_gain),
        new_investment, cumulative_investment + monthly_investment,
        {new_effectiveness, new_investment}))),
  
  // Create comprehensive supplier risk assessment
  supplier_risk_analysis, MAP(SEQUENCE(ROWS(suppliers)), LAMBDA(supplier_i,
    LET(supplier, INDEX(suppliers, supplier_i, 1),
        volume, INDEX(supplier_volumes, supplier_i, 1),
        recovery_time, INDEX(recovery_times, supplier_i, 1),
        final_risk, INDEX(INDEX(cumulative_risk_progression, supplier_i, 0), 12, 1),
        final_capacity, INDEX(INDEX(capacity_progression, supplier_i, 0), 12, 1),
        final_financial_impact, INDEX(INDEX(financial_risk_progression, supplier_i, 0), 12, 1),
        
        // Risk categorization
        risk_level, IF(final_risk > 50, "CRITICAL",
                      IF(final_risk > 30, "HIGH", 
                         IF(final_risk > 15, "MEDIUM", "LOW"))),
        
        capacity_status, IF(final_capacity > 0.9, "OVERUTILIZED",
                           IF(final_capacity > 0.7, "HIGH UTILIZATION", "NORMAL")),
        
        supplier_summary, CONCAT(
          supplier, ": ", risk_level, " risk (",
          TEXT(final_risk, "0.0"), ") | Volume: ",
          TEXT(volume, "#,##0"), " units | Capacity: ",
          TEXT(final_capacity, "0.0%"), " (", capacity_status, ") | ",
          "Recovery: ", TEXT(recovery_time, "0"), " days | ",
          "Financial Impact: $", TEXT(final_financial_impact, "#,##0")),
        supplier_summary))),
  
  // Calculate aggregate supply chain metrics
  total_supply_volume, SUM(supplier_volumes),
  average_recovery_time, AVERAGE(recovery_times),
  total_financial_risk, SUM(MAP(financial_risk_progression, LAMBDA(impact_array,
    INDEX(impact_array, 12, 1)))),
  final_diversification_score, INDEX(diversification_progression, ROWS(diversification_progression), 1, 2),
  final_mitigation_effectiveness, INDEX(mitigation_effectiveness, ROWS(mitigation_effectiveness), 1, 1),
  total_mitigation_investment, INDEX(mitigation_effectiveness, ROWS(mitigation_effectiveness), 1, 2),
  
  // High-risk suppliers count
  high_risk_suppliers, SUMPRODUCT(MAP(cumulative_risk_progression, LAMBDA(risk_array,
    IF(INDEX(risk_array, 12, 1) > 30, 1, 0)))),
  
  // Final comprehensive supply chain resilience report
  resilience_report, VSTACK(
    "=== SUPPLY CHAIN RESILIENCE & PROGRESSIVE RISK ASSESSMENT ===",
    "",
    "Supplier Risk Analysis (12-Month Progression):",
    TRANSPOSE(supplier_risk_analysis),
    "",
    "Supply Chain Resilience Metrics:",
    CONCAT("Total Supply Volume: ", TEXT(total_supply_volume, "#,##0"), " units/month"),
    CONCAT("Supply Base Diversification Score: ", TEXT(final_diversification_score, "0.0%")),
    CONCAT("Average Recovery Time: ", TEXT(average_recovery_time, "0.0"), " days"),
    CONCAT("High-Risk Suppliers: ", TEXT(high_risk_suppliers, "0"), " of ", TEXT(ROWS(suppliers), "0")),
    "",
    "Financial Risk Assessment:",
    CONCAT("Total Annual Financial Risk: $", TEXT(total_financial_risk * 12, "#,##0")),
    CONCAT("Risk per Unit of Supply: $", TEXT(total_financial_risk * 12 / (total_supply_volume * 12), "0.00")),
    "",
    "Mitigation Strategy Performance:",
    CONCAT("Current Mitigation Effectiveness: ", TEXT(final_mitigation_effectiveness, "0.0%")),
    CONCAT("Total Mitigation Investment: $", TEXT(total_mitigation_investment, "#,##0")),
    CONCAT("ROI on Mitigation: $", TEXT((total_financial_risk * 0.3) / (total_mitigation_investment / 10000), "0.00"), " risk reduced per $1,000 invested")),
  
  resilience_report)
```

### Dynamic Project Portfolio Optimization with Resource Allocation
```spreadsheets
// Build comprehensive project portfolio management using SCAN for progressive tracking
=LET(
  projects, {"Digital Platform", "Market Expansion", "Process Automation", "Product Development", "Infrastructure Upgrade"},
  project_durations, {18, 12, 8, 15, 10},  // Months
  project_budgets, {2500000, 1200000, 800000, 1800000, 1000000},
  monthly_burn_rates, {140000, 100000, 100000, 120000, 100000},
  success_probabilities, {0.75, 0.85, 0.90, 0.70, 0.95},
  expected_returns, {5000000, 2800000, 1500000, 4200000, 800000},  // 3-year returns
  resource_requirements, {25, 15, 12, 20, 8},  // FTE count
  
  // Progressive project completion and resource utilization
  project_completion_progression, MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
    LET(duration, INDEX(project_durations, project_i, 1),
        burn_rate, INDEX(monthly_burn_rates, project_i, 1),
        budget, INDEX(project_budgets, project_i, 1),
        
        // Progressive completion tracking
        completion_progression, SCAN(0, SEQUENCE(duration), LAMBDA(acc_progress, month,
          LET(planned_progress, month / duration,
              actual_progress_variance, RANDBETWEEN(-5, 10) / 100,  // Realistic variance
              actual_progress, MIN(1, MAX(0, planned_progress + actual_progress_variance)),
              actual_progress))),
        completion_progression))),
  
  // Progressive budget consumption and variance analysis
  budget_progression, MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
    LET(budget, INDEX(project_budgets, project_i, 1),
        burn_rate, INDEX(monthly_burn_rates, project_i, 1),
        completion_array, INDEX(project_completion_progression, project_i, 0),
        
        // Progressive budget tracking with efficiency factors
        budget_consumption, SCAN(0, MAP(completion_array, LAMBDA(completion,
          burn_rate * (1 + (completion * 0.1)))),  // Costs increase as complexity grows
          LAMBDA(acc_spent, monthly_spend, acc_spent + monthly_spend)),
        budget_consumption))),
  
  // Progressive risk assessment and mitigation
  risk_progression, MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
    LET(base_success_prob, INDEX(success_probabilities, project_i, 1),
        completion_array, INDEX(project_completion_progression, project_i, 0),
        
        // Progressive risk evolution
        risk_evolution, SCAN(1 - base_success_prob, completion_array, LAMBDA(acc_risk, completion,
          LET(complexity_risk, completion^2 * 0.1,  // Risk increases with complexity
              schedule_risk, IF(completion < (ROW(completion) - 1) / ROWS(completion_array), 0.05, -0.02),
              new_risk, MIN(0.5, MAX(0.1, acc_risk + complexity_risk + schedule_risk)),
              new_risk))),
        risk_evolution))),
  
  // Progressive portfolio value and optimization
  portfolio_value_progression, SCAN({0, 0, 0}, SEQUENCE(24), LAMBDA(acc, month,  // 24-month analysis
    LET(total_investment, INDEX(acc, 1, 1),
        cumulative_value, INDEX(acc, 1, 2),
        active_projects, INDEX(acc, 1, 3),
        
        // Calculate monthly portfolio metrics
        monthly_investment, SUMPRODUCT(MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
          LET(duration, INDEX(project_durations, project_i, 1),
              burn_rate, INDEX(monthly_burn_rates, project_i, 1),
              IF(month <= duration, burn_rate, 0))))),
        
        monthly_value_creation, SUMPRODUCT(MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
          LET(duration, INDEX(project_durations, project_i, 1),
              expected_return, INDEX(expected_returns, project_i, 1),
              success_prob, INDEX(success_probabilities, project_i, 1),
              IF(month = duration + 6, expected_return * success_prob, 0))))),  // Value realized 6 months post-completion
        
        current_active, SUMPRODUCT(MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
          LET(duration, INDEX(project_durations, project_i, 1),
              IF(month <= duration, 1, 0))))),
        
        new_total_investment, total_investment + monthly_investment,
        new_cumulative_value, cumulative_value + monthly_value_creation,
        
        {new_total_investment, new_cumulative_value, current_active}))),
  
  // Progressive resource allocation optimization
  resource_allocation_progression, SCAN({0, 100}, SEQUENCE(24), LAMBDA(acc, month,  // Assume 100 total FTE
    LET(allocated_resources, INDEX(acc, 1, 1),
        available_resources, INDEX(acc, 1, 2),
        
        monthly_resource_demand, SUMPRODUCT(MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
          LET(duration, INDEX(project_durations, project_i, 1),
              resource_req, INDEX(resource_requirements, project_i, 1),
              IF(month <= duration, resource_req, 0))))),
        
        resource_efficiency, MIN(1, available_resources / MAX(1, monthly_resource_demand)),
        new_allocated, MIN(available_resources, monthly_resource_demand),
        new_available, available_resources - new_allocated + 
                      SUMPRODUCT(MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
                        LET(duration, INDEX(project_durations, project_i, 1),
                            resource_req, INDEX(resource_requirements, project_i, 1),
                            IF(month = duration, resource_req, 0))))),  // Resources freed up on completion
        
        {new_allocated, new_available}))),
  
  // Create comprehensive project analysis
  project_analysis, MAP(SEQUENCE(ROWS(projects)), LAMBDA(project_i,
    LET(project, INDEX(projects, project_i, 1),
        duration, INDEX(project_durations, project_i, 1),
        budget, INDEX(project_budgets, project_i, 1),
        expected_return, INDEX(expected_returns, project_i, 1),
        success_prob, INDEX(success_probabilities, project_i, 1),
        resources, INDEX(resource_requirements, project_i, 1),
        
        final_completion, INDEX(INDEX(project_completion_progression, project_i, 0), duration, 1),
        final_budget_used, INDEX(INDEX(budget_progression, project_i, 0), duration, 1),
        final_risk, INDEX(INDEX(risk_progression, project_i, 0), duration, 1),
        
        budget_variance, (final_budget_used - budget) / budget,
        schedule_performance, final_completion,
        risk_adjusted_return, expected_return * (1 - final_risk),
        roi, (risk_adjusted_return - final_budget_used) / final_budget_used,
        
        // Project status assessment
        status, IF(final_completion < 0.95, "BEHIND SCHEDULE",
                  IF(budget_variance > 0.1, "OVER BUDGET",
                     IF(final_risk > 0.3, "HIGH RISK", "ON TRACK"))),
        
        project_summary, CONCAT(
          project, ": ", TEXT(final_completion, "0.0%"), " complete | ",
          "Budget: $", TEXT(final_budget_used, "#,##0"), 
          " (", TEXT(budget_variance, "+0.0%;-0.0%"), " variance) | ",
          "Risk: ", TEXT(final_risk, "0.0%"), " | ",
          "ROI: ", TEXT(roi, "0.0%"), " | ",
          "Status: ", status),
        project_summary))),
  
  // Calculate portfolio-level metrics
  total_portfolio_investment, INDEX(portfolio_value_progression, 24, 1, 1),
  total_portfolio_value, INDEX(portfolio_value_progression, 24, 1, 2),
  portfolio_roi, (total_portfolio_value - total_portfolio_investment) / total_portfolio_investment,
  peak_resource_utilization, MAX(MAP(resource_allocation_progression, LAMBDA(allocation,
    INDEX(allocation, 1, 1)))),
  
  // Final comprehensive portfolio report
  portfolio_report, VSTACK(
    "=== DYNAMIC PROJECT PORTFOLIO OPTIMIZATION ===",
    "",
    "Project Performance Analysis:",
    TRANSPOSE(project_analysis),
    "",
    "Portfolio-Level Metrics:",
    CONCAT("Total Portfolio Investment: $", TEXT(total_portfolio_investment, "#,##0")),
    CONCAT("Total Portfolio Value Created: $", TEXT(total_portfolio_value, "#,##0")),
    CONCAT("Portfolio ROI: ", TEXT(portfolio_roi, "0.0%")),
    CONCAT("Peak Resource Utilization: ", TEXT(peak_resource_utilization, "0"), " FTE"),
    "",
    "Resource Utilization Summary:",
    CONCAT("Average Monthly Resource Allocation: ", TEXT(AVERAGE(MAP(resource_allocation_progression, LAMBDA(allocation, INDEX(allocation, 1, 1)))), "0.0"), " FTE"),
    CONCAT("Resource Efficiency Score: ", TEXT(peak_resource_utilization / 100, "0.0%")),
    "",
    "Portfolio Success Indicators:",
    CONCAT("Projects Completed Successfully: ", TEXT(SUMPRODUCT(MAP(project_completion_progression, LAMBDA(completion_array, IF(INDEX(completion_array, ROWS(completion_array), 1) >= 0.95, 1, 0)))), "0"), " of ", TEXT(ROWS(projects), "0")),
    CONCAT("Average Project Success Probability: ", TEXT(AVERAGE(success_probabilities), "0.0%")),
    CONCAT("Portfolio Value-to-Investment Ratio: ", TEXT(total_portfolio_value / total_portfolio_investment, "0.0x"))),
  
  portfolio_report)
```