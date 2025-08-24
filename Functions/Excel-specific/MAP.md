---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- excel-specific
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- excel specific
- excel
- sheets
---
# MAP

## MAP Description

Applies a LAMBDA function to each element in one or more arrays and returns an array of results. Enables functional programming patterns by transforming array elements through custom logic, supporting both single-array transformations and multi-array operations with corresponding elements.

> [!f(x)] MAP Syntax
>
> ```spreadsheets
> MAP(array1, [array2, ...], lambda_function)
> ```
>
> **Parameters:**
> - `array1` (required): First array to process with the LAMBDA function
> - `array2, ...` (optional): Additional arrays to process simultaneously with array1
> - `lambda_function` (required): LAMBDA function that takes values from each array and returns transformed results

> [!f(x)] MAP Examples
>
> ```spreadsheets
> // Transform single array with calculation
> MAP({1,2,3,4,5}, LAMBDA(x, x * x)) → {1,4,9,16,25}
> 
> // Apply text transformation to array
> MAP({"apple","banana","cherry"}, LAMBDA(x, UPPER(x))) → {"APPLE","BANANA","CHERRY"}
> 
> // Process two arrays simultaneously
> MAP({10,20,30}, {2,3,4}, LAMBDA(x, y, x * y)) → {20,60,120}
> 
> // Complex transformation with multiple operations
> MAP({1,2,3,4}, LAMBDA(x, IF(x > 2, x^2, x))) → {1,2,9,16}
> 
> // Multi-column data transformation
> MAP(sales_data, LAMBDA(x, x * 1.08)) → adds 8% tax to all sales values
> ```

## Use Cases

### [[Array transformations]]
- **Data cleansing**: Apply consistent formatting, trimming, or standardization rules across entire datasets
- **Unit conversions**: Convert measurements, currencies, or scales across arrays of values simultaneously
- **Mathematical operations**: Apply complex calculations to every element in large datasets efficiently
- **Text processing**: Transform text arrays with consistent formatting, case conversion, or pattern replacement

### [[Functional programming patterns]]
- **Pure functions**: Create predictable transformations that don't modify original data, supporting immutable programming styles
- **Higher-order functions**: Combine MAP with other LAMBDA-based functions for complex data processing pipelines
- **Function composition**: Chain multiple MAP operations to build sophisticated data transformation workflows
- **Declarative processing**: Express data transformations as what should happen rather than how to iterate

### [[Performance optimization]]
- **Bulk operations**: Process large arrays more efficiently than iterative cell-by-cell formulas
- **Vectorized calculations**: Leverage Excel's array calculation engine for faster processing of repetitive operations
- **Memory efficiency**: Reduce formula complexity and improve calculation speed through single-operation array processing
- **Dynamic calculations**: Create responsive spreadsheets where entire datasets recalculate instantly when parameters change

### [[Data analysis workflows]]
- **Statistical transformations**: Apply normalization, standardization, or scaling operations to entire datasets
- **Conditional processing**: Use complex logic to transform different elements based on their values or positions
- **Multi-dimensional analysis**: Process corresponding elements from multiple arrays for correlation analysis
- **Report preparation**: Transform raw data into presentation-ready formats through consistent formatting rules

## Related

### Similar Functions

- [[LAMBDA]] - Defines custom functions used within MAP operations
- [[REDUCE]] - Aggregates array values using custom logic, complementary to MAP's transformation
- [[SCAN]] - Accumulates transformations across arrays, building running totals or progressive calculations
- [[MAKEARRAY]] - Creates arrays from scratch, while MAP transforms existing arrays
- [[FILTER]] - Selects array elements, often used with MAP to transform filtered results

## Array Processing Functions

### [[LAMBDA]]
Essential partnership where LAMBDA defines the transformation logic that MAP applies to arrays.

```spreadsheets
// Create reusable transformation logic
=LET(tax_calculator, LAMBDA(amount, rate, amount * (1 + rate)),
     MAP(revenue_array, tax_rate_array, tax_calculator))
// Applies consistent tax calculation across revenue data

// Complex business logic transformation
=LET(performance_scorer, LAMBDA(sales, target, 
       IF(sales >= target, 100 + (sales - target) / target * 50, 
          sales / target * 100)),
     MAP(actual_sales, sales_targets, performance_scorer))
// Calculates performance scores with bonus scaling

// Multi-step data cleaning
=LET(data_cleaner, LAMBDA(text_value,
       TRIM(UPPER(SUBSTITUTE(text_value, "  ", " ")))),
     MAP(raw_text_array, data_cleaner))
// Standardizes text data with multiple cleaning operations
```

### [[REDUCE]]
Complements MAP by aggregating transformed results into single values or summary statistics.

```spreadsheets
// Transform then aggregate in pipeline
=REDUCE(0, MAP(sales_array, LAMBDA(x, x * 1.08)), LAMBDA(acc, val, acc + val))
// Adds tax to all sales, then sums total

// Statistical analysis pipeline
=LET(normalized_values, MAP(data_array, LAMBDA(x, (x - mean_value) / std_dev)),
     variance, REDUCE(0, normalized_values, LAMBDA(acc, val, acc + val^2)) / COUNT(data_array))
// Normalizes data then calculates variance

// Complex scoring aggregation
=REDUCE(0, MAP(scores_array, weights_array, LAMBDA(score, weight, score * weight)),
        LAMBDA(total, weighted_score, total + weighted_score))
// Applies weights to scores then sums weighted total
```

## Mathematical Functions

### [[SUM]]
Frequently used with MAP to aggregate transformed values, enabling sophisticated calculations on array data.

```spreadsheets
// Calculate total with transformation
=SUM(MAP(quantities, unit_prices, LAMBDA(qty, price, qty * price)))
// Multiplies quantities by prices then sums total

// Weighted average calculation
=SUM(MAP(values_array, weights_array, LAMBDA(val, weight, val * weight))) / 
 SUM(weights_array)
// Applies weights then calculates weighted average

// Complex financial calculation
=SUM(MAP(principal_array, rate_array, years_array, 
         LAMBDA(p, r, y, p * (1 + r)^y)))
// Calculates compound interest for multiple investments then sums
```

### [[AVERAGE]]
Combines with MAP for statistical analysis of transformed data and performance metrics calculation.

```spreadsheets
// Performance rating calculation
=AVERAGE(MAP(raw_scores, max_possible, LAMBDA(score, max_val, score / max_val * 100)))
// Converts raw scores to percentages then averages

// Trend analysis
=AVERAGE(MAP(current_period, previous_period, 
             LAMBDA(curr, prev, (curr - prev) / prev)))
// Calculates growth rates then averages for overall trend

// Quality score normalization
=AVERAGE(MAP(quality_metrics, target_values, 
             LAMBDA(actual, target, MIN(100, actual / target * 100))))
// Normalizes quality metrics to percentage of target, caps at 100%
```

## Text Processing Functions

### [[CONCAT]]
Partners with MAP for bulk text processing and formatted string generation across arrays.

```spreadsheets
// Generate formatted labels
=MAP(product_codes, descriptions, prices,
     LAMBDA(code, desc, price, 
       CONCAT(code, ": ", desc, " ($", TEXT(price, "#,##0.00"), ")")))
// Creates formatted product labels from multiple arrays

// Build email addresses
=MAP(first_names, last_names, LAMBDA(first, last,
     CONCAT(LOWER(first), ".", LOWER(last), "@company.com")))
// Generates email addresses from name components

// Create report headers
=MAP(department_names, quarter_data, LAMBDA(dept, data,
     CONCAT(dept, " Q", TEXT(MONTH(TODAY())/3, "0"), " Performance")))
// Builds dynamic report headers with current quarter
```

### [[SUBSTITUTE]]
Works with MAP for bulk text replacement and data standardization operations.

```spreadsheets
// Standardize data formats
=MAP(phone_numbers, LAMBDA(phone,
     SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(phone, "(", ""), ")", ""), "-", "")))
// Removes formatting from phone numbers

// Clean imported data
=MAP(text_array, LAMBDA(text,
     SUBSTITUTE(SUBSTITUTE(TRIM(text), "  ", " "), "N/A", "")))
// Cleans up imported text with multiple substitutions

// Format currency data
=MAP(currency_strings, LAMBDA(curr,
     SUBSTITUTE(SUBSTITUTE(curr, "$", ""), ",", "")))
// Strips currency formatting for calculations
```

## Commonly Used With Functions Examples

### Advanced Financial Portfolio Analysis
```spreadsheets
// Create comprehensive investment analysis with MAP transformations
=LET(
  portfolios, {100000, 150000, 200000, 75000, 300000},  // Investment amounts
  returns, {0.08, 0.12, 0.06, 0.15, 0.10},             // Annual returns
  years, {5, 3, 7, 2, 10},                             // Investment periods
  risk_factors, {0.15, 0.25, 0.10, 0.30, 0.20},       // Risk adjustments
  
  // Calculate future values with MAP
  future_values, MAP(portfolios, returns, years,
    LAMBDA(principal, rate, period, principal * (1 + rate)^period)),
  
  // Apply risk adjustments to returns
  risk_adjusted_returns, MAP(returns, risk_factors,
    LAMBDA(return_rate, risk, return_rate - risk)),
  
  // Calculate risk-adjusted future values
  conservative_values, MAP(portfolios, risk_adjusted_returns, years,
    LAMBDA(principal, adj_rate, period, 
      principal * (1 + MAX(0, adj_rate))^period)),
  
  // Generate performance analysis
  performance_analysis, MAP(future_values, conservative_values, portfolios,
    LAMBDA(optimistic, conservative, original,
      LET(opt_gain, optimistic - original,
          cons_gain, conservative - original,
          opt_return, opt_gain / original,
          cons_return, cons_gain / original,
          CONCAT("Gain Range: $", TEXT(cons_gain, "#,##0"), " - $", TEXT(opt_gain, "#,##0"),
                 " (", TEXT(cons_return, "0.0%"), " - ", TEXT(opt_return, "0.0%"), ")")))),
  
  // Create investment ranking system
  investment_scores, MAP(future_values, risk_factors, years,
    LAMBDA(future_val, risk, period,
      LET(time_factor, 1 / period,     // Favor shorter periods
          risk_penalty, 1 - risk,      // Penalize high risk
          growth_factor, future_val / MAX(portfolios),  // Normalize by largest investment
          score, (time_factor + risk_penalty + growth_factor) / 3 * 100,
          ROUND(score, 1)))),
  
  // Final comprehensive report
  investment_summary, MAP(SEQUENCE(ROWS(portfolios)), LAMBDA(row,
    CONCAT("Investment ", TEXT(row, "0"), ": ",
           TEXT(INDEX(portfolios, row, 1), "$#,##0"), " → ",
           TEXT(INDEX(future_values, row, 1), "$#,##0"), 
           " | Score: ", TEXT(INDEX(investment_scores, row, 1), "0.0"),
           " | ", INDEX(performance_analysis, row, 1)))),
  
  VSTACK("=== PORTFOLIO ANALYSIS REPORT ===",
         "",
         "Investment Performance Summary:",
         TRANSPOSE(investment_summary),
         "",
         CONCAT("Total Investment: ", TEXT(SUM(portfolios), "$#,##0")),
         CONCAT("Projected Total: ", TEXT(SUM(future_values), "$#,##0")),
         CONCAT("Conservative Total: ", TEXT(SUM(conservative_values), "$#,##0")),
         CONCAT("Overall Return Range: ", 
                TEXT((SUM(conservative_values) - SUM(portfolios))/SUM(portfolios), "0.0%"),
                " - ",
                TEXT((SUM(future_values) - SUM(portfolios))/SUM(portfolios), "0.0%"))))
```

### Customer Segmentation and Marketing Analytics
```spreadsheets
// Build comprehensive customer analysis using MAP transformations
=LET(
  customer_ids, SEQUENCE(100),  // 100 customers
  purchase_amounts, RANDARRAY(100, 1, 50, 5000),     // Random purchase amounts
  visit_frequency, RANDARRAY(100, 1, 1, 50),         // Visits per month
  tenure_months, RANDARRAY(100, 1, 1, 60),           // Customer tenure
  satisfaction_scores, RANDARRAY(100, 1, 1, 10),     // Satisfaction ratings
  
  // Calculate customer lifetime value
  clv_scores, MAP(purchase_amounts, visit_frequency, tenure_months,
    LAMBDA(amount, frequency, tenure,
      LET(monthly_value, amount * frequency / 12,
          projected_lifetime, tenure * 2,  // Assume double current tenure
          clv, monthly_value * projected_lifetime,
          ROUND(clv, 0)))),
  
  // Create customer segments based on value and engagement
  customer_segments, MAP(clv_scores, visit_frequency, satisfaction_scores,
    LAMBDA(clv, visits, satisfaction,
      LET(value_tier, IF(clv >= 10000, "High", IF(clv >= 5000, "Medium", "Low")),
          engagement_tier, IF(visits >= 20, "Frequent", IF(visits >= 10, "Regular", "Occasional")),
          satisfaction_tier, IF(satisfaction >= 8, "Satisfied", IF(satisfaction >= 6, "Neutral", "At Risk")),
          segment, CONCAT(value_tier, " Value - ", engagement_tier, " - ", satisfaction_tier),
          segment))),
  
  // Generate marketing recommendations
  marketing_actions, MAP(customer_segments, clv_scores,
    LAMBDA(segment, clv,
      IF(ISNUMBER(SEARCH("High Value", segment)),
         IF(ISNUMBER(SEARCH("At Risk", segment)), "URGENT: Personal retention call + premium offer",
            IF(ISNUMBER(SEARCH("Satisfied", segment)), "VIP program enrollment + exclusive offers",
               "Satisfaction survey + targeted improvement")),
         IF(ISNUMBER(SEARCH("Medium Value", segment)),
            IF(ISNUMBER(SEARCH("At Risk", segment)), "Discount offer + feedback survey",
               IF(ISNUMBER(SEARCH("Frequent", segment)), "Upsell campaign + loyalty rewards",
                  "Engagement campaign + value demonstration")),
            IF(ISNUMBER(SEARCH("At Risk", segment)), "Win-back campaign + deep discount",
               "Basic retention + value education"))))),
  
  // Calculate segment statistics
  segment_analysis, LET(
    unique_segments, UNIQUE(customer_segments),
    segment_stats, MAP(unique_segments, LAMBDA(seg,
      LET(segment_customers, FILTER(customer_ids, customer_segments = seg),
          segment_clv, FILTER(clv_scores, customer_segments = seg),
          segment_count, COUNT(segment_customers),
          avg_clv, ROUND(AVERAGE(segment_clv), 0),
          total_value, SUM(segment_clv),
          CONCAT(seg, " | Count: ", TEXT(segment_count, "0"), 
                     " | Avg CLV: $", TEXT(avg_clv, "#,##0"),
                     " | Total: $", TEXT(total_value, "#,##0"))))),
    segment_stats),
  
  // Create personalized customer communications
  customer_communications, MAP(customer_ids, customer_segments, clv_scores, purchase_amounts,
    LAMBDA(id, segment, clv, last_purchase,
      LET(name, CONCAT("Customer_", TEXT(id, "000")),
          value_message, IF(clv >= 10000, "valued premium customer",
                              IF(clv >= 5000, "important customer", "valued customer")),
          offer_amount, ROUND(last_purchase * 0.15, 0),
          message, CONCAT("Dear ", name, ", as our ", value_message, 
                         " with $", TEXT(clv, "#,##0"), " lifetime value, ",
                         "we're offering you $", TEXT(offer_amount, "#,##0"), " off your next purchase!"),
          message))),
  
  // Final comprehensive customer report
  customer_report, VSTACK(
    "=== CUSTOMER SEGMENTATION & MARKETING ANALYSIS ===",
    "",
    "Segment Distribution:",
    TRANSPOSE(segment_analysis),
    "",
    CONCAT("Total Customers: ", TEXT(ROWS(customer_ids), "#,##0")),
    CONCAT("Average CLV: $", TEXT(AVERAGE(clv_scores), "#,##0")),
    CONCAT("Total Portfolio Value: $", TEXT(SUM(clv_scores), "#,##0")),
    CONCAT("High Value Customers (>$10K): ", TEXT(SUMPRODUCT((clv_scores>=10000)*1), "0")),
    "",
    "Sample Personalized Messages:",
    customer_communications[{1;2;3;4;5}]),  // First 5 customer messages
  
  customer_report)
```

### Supply Chain Optimization and Demand Forecasting
```spreadsheets
// Create sophisticated supply chain analysis with MAP-driven calculations
=LET(
  products, {"Widget A", "Widget B", "Widget C", "Gadget X", "Gadget Y"},
  current_inventory, {150, 200, 75, 300, 125},
  monthly_demand, {80, 120, 45, 180, 90},
  lead_times, {14, 21, 10, 28, 16},           // Days
  unit_costs, {25.50, 45.75, 15.25, 85.00, 35.25},
  storage_costs_per_unit, {2.50, 3.75, 1.25, 6.50, 2.75},  // Monthly
  
  // Calculate inventory metrics
  days_of_supply, MAP(current_inventory, monthly_demand,
    LAMBDA(inventory, demand, 
      ROUND(inventory / (demand / 30), 1))),  // Convert monthly to daily demand
  
  // Determine reorder points with safety stock
  reorder_points, MAP(monthly_demand, lead_times,
    LAMBDA(demand, lead_time,
      LET(daily_demand, demand / 30,
          lead_time_demand, daily_demand * lead_time,
          safety_stock, lead_time_demand * 0.5,  // 50% safety stock
          reorder_point, ROUND(lead_time_demand + safety_stock, 0),
          reorder_point))),
  
  // Calculate optimal order quantities (simplified EOQ)
  optimal_order_qty, MAP(monthly_demand, unit_costs, storage_costs_per_unit,
    LAMBDA(demand, cost, storage,
      LET(annual_demand, demand * 12,
          ordering_cost, 50,  // Fixed ordering cost
          holding_cost, storage * 12,  // Annual holding cost
          eoq, SQRT(2 * annual_demand * ordering_cost / holding_cost),
          ROUND(eoq, 0)))),
  
  // Generate inventory status and actions
  inventory_actions, MAP(current_inventory, reorder_points, optimal_order_qty, days_of_supply,
    LAMBDA(current, reorder, optimal, days,
      IF(current <= reorder, 
         CONCAT("ORDER NOW: ", TEXT(optimal, "#,##0"), " units (", TEXT(days, "0.0"), " days left)"),
         IF(days > 90, 
            "EXCESS INVENTORY: Consider reducing orders",
            CONCAT("NORMAL: Reorder when below ", TEXT(reorder, "#,##0"), " units"))))),
  
  // Calculate financial impact
  carrying_costs, MAP(current_inventory, storage_costs_per_unit,
    LAMBDA(inventory, storage_cost, inventory * storage_cost)),
  
  inventory_values, MAP(current_inventory, unit_costs,
    LAMBDA(inventory, cost, inventory * cost)),
  
  // Create ABC analysis based on value
  abc_classification, MAP(inventory_values, LAMBDA(value,
    LET(total_value, SUM(inventory_values),
        value_percentage, value / total_value,
        IF(value_percentage >= 0.15, "A - Critical",
           IF(value_percentage >= 0.05, "B - Important", "C - Standard"))))),
  
  // Generate demand forecasting
  demand_forecast, MAP(monthly_demand, SEQUENCE(12), 
    LAMBDA(base_demand, month,
      LET(seasonal_factor, 1 + 0.2 * SIN(month / 12 * 2 * PI()),  // Seasonal variation
          growth_factor, 1 + 0.05,  // 5% annual growth
          trend_factor, 1 + (month - 6) * 0.01,  // Monthly trend
          forecasted_demand, ROUND(base_demand * seasonal_factor * growth_factor * trend_factor, 0),
          forecasted_demand))),
  
  // Create comprehensive supply chain dashboard
  supply_dashboard, MAP(SEQUENCE(ROWS(products)), LAMBDA(row,
    LET(product, INDEX(products, row, 1),
        current, INDEX(current_inventory, row, 1),
        reorder, INDEX(reorder_points, row, 1),
        days, INDEX(days_of_supply, row, 1),
        action, INDEX(inventory_actions, row, 1),
        classification, INDEX(abc_classification, row, 1),
        value, INDEX(inventory_values, row, 1),
        CONCAT(product, " | Current: ", TEXT(current, "#,##0"),
               " | Days: ", TEXT(days, "0.0"),
               " | Value: $", TEXT(value, "#,##0"),
               " | ", classification,
               " | Action: ", action)))),
  
  // Calculate key performance indicators
  total_inventory_value, SUM(inventory_values),
  total_carrying_cost, SUM(carrying_costs),
  avg_days_supply, AVERAGE(days_of_supply),
  items_needing_reorder, SUMPRODUCT((current_inventory <= reorder_points) * 1),
  
  // Final supply chain report
  supply_report, VSTACK(
    "=== SUPPLY CHAIN OPTIMIZATION REPORT ===",
    "",
    "Inventory Status by Product:",
    TRANSPOSE(supply_dashboard),
    "",
    "Key Performance Indicators:",
    CONCAT("Total Inventory Value: $", TEXT(total_inventory_value, "#,##0")),
    CONCAT("Monthly Carrying Costs: $", TEXT(total_carrying_cost, "#,##0")),
    CONCAT("Average Days of Supply: ", TEXT(avg_days_supply, "0.0"), " days"),
    CONCAT("Items Requiring Reorder: ", TEXT(items_needing_reorder, "0"), " of ", TEXT(ROWS(products), "0")),
    "",
    "Next 3 Months Demand Forecast:",
    MAP(products, LAMBDA(product,
      LET(product_index, MATCH(product, products, 0),
          month1, INDEX(INDEX(demand_forecast, product_index, 0), 1, 1),
          month2, INDEX(INDEX(demand_forecast, product_index, 0), 1, 2),
          month3, INDEX(INDEX(demand_forecast, product_index, 0), 1, 3),
          CONCAT(product, ": ", TEXT(month1, "#,##0"), " | ", TEXT(month2, "#,##0"), " | ", TEXT(month3, "#,##0")))))),
  
  supply_report)
```

### Dynamic Project Management and Resource Allocation
```spreadsheets
// Build comprehensive project management system with MAP-driven analysis
=LET(
  projects, {"Website Redesign", "Mobile App", "Database Migration", "Marketing Campaign", "Training Program"},
  durations, {90, 120, 45, 60, 30},           // Days
  budgets, {150000, 250000, 80000, 100000, 40000},
  team_sizes, {8, 12, 4, 6, 3},
  completion_percentages, {0.75, 0.40, 0.90, 0.60, 0.25},
  priority_scores, {9, 10, 8, 7, 6},         // 1-10 scale
  
  // Calculate project health metrics
  days_elapsed, MAP(durations, completion_percentages,
    LAMBDA(duration, completion, ROUND(duration * completion, 0))),
  
  days_remaining, MAP(durations, days_elapsed,
    LAMBDA(total_days, elapsed, total_days - elapsed)),
  
  budget_spent, MAP(budgets, completion_percentages,
    LAMBDA(budget, completion, ROUND(budget * completion, 0))),
  
  budget_remaining, MAP(budgets, budget_spent,
    LAMBDA(total_budget, spent, total_budget - spent)),
  
  // Analyze project performance
  schedule_performance, MAP(completion_percentages, days_elapsed, durations,
    LAMBDA(completion, elapsed, total_duration,
      LET(expected_completion, elapsed / total_duration,
          performance_ratio, completion / expected_completion,
          IF(performance_ratio >= 1.1, "Ahead of Schedule",
             IF(performance_ratio >= 0.9, "On Schedule", "Behind Schedule"))))),
  
  budget_performance, MAP(budget_spent, budgets, completion_percentages,
    LAMBDA(spent, total_budget, completion,
      LET(expected_spend, total_budget * completion,
          variance_ratio, spent / expected_spend,
          IF(variance_ratio <= 0.9, "Under Budget",
             IF(variance_ratio <= 1.1, "On Budget", "Over Budget"))))),
  
  // Calculate resource utilization
  daily_resource_cost, MAP(team_sizes, budgets, durations,
    LAMBDA(team_size, budget, duration,
      ROUND(budget / duration / team_size, 2))),
  
  // Generate risk assessment
  risk_levels, MAP(days_remaining, budget_remaining, priority_scores, schedule_performance,
    LAMBDA(days_left, budget_left, priority, schedule_status,
      LET(time_risk, IF(days_left < 10, 3, IF(days_left < 30, 2, 1)),
          budget_risk, IF(budget_left < 5000, 3, IF(budget_left < 20000, 2, 1)),
          schedule_risk, IF(schedule_status = "Behind Schedule", 3, 
                           IF(schedule_status = "On Schedule", 2, 1)),
          overall_risk, (time_risk + budget_risk + schedule_risk + (11 - priority)) / 4,
          IF(overall_risk >= 3, "High Risk",
             IF(overall_risk >= 2.5, "Medium Risk", "Low Risk"))))),
  
  // Create project recommendations
  project_actions, MAP(schedule_performance, budget_performance, risk_levels, days_remaining,
    LAMBDA(schedule, budget, risk, days_left,
      IF(risk = "High Risk",
         IF(days_left < 15, "CRITICAL: Daily standup + resource reallocation",
            IF(schedule = "Behind Schedule", "Add resources or reduce scope",
               "Budget review + timeline adjustment")),
         IF(risk = "Medium Risk",
            IF(budget = "Over Budget", "Cost control measures + scope review",
               "Monitor closely + prepare contingency"),
            "Continue current approach + regular monitoring")))),
  
  // Calculate portfolio metrics
  total_budget, SUM(budgets),
  total_spent, SUM(budget_spent),
  portfolio_completion, AVERAGE(completion_percentages),
  high_risk_projects, SUMPRODUCT((risk_levels = "High Risk") * 1),
  
  // Generate executive summary
  project_summary, MAP(SEQUENCE(ROWS(projects)), LAMBDA(row,
    LET(project, INDEX(projects, row, 1),
        completion, INDEX(completion_percentages, row, 1),
        days_left, INDEX(days_remaining, row, 1),
        budget_left, INDEX(budget_remaining, row, 1),
        risk, INDEX(risk_levels, row, 1),
        schedule, INDEX(schedule_performance, row, 1),
        action, INDEX(project_actions, row, 1),
        CONCAT(project, " | ", TEXT(completion, "0%"), " complete",
               " | ", TEXT(days_left, "0"), " days left",
               " | $", TEXT(budget_left, "#,##0"), " budget remaining",
               " | ", risk, " | ", schedule,
               " | Action: ", action)))),
  
  // Create resource reallocation recommendations
  resource_optimization, MAP(team_sizes, daily_resource_cost, risk_levels, priority_scores,
    LAMBDA(current_team, daily_cost, risk, priority,
      LET(efficiency_score, priority / daily_cost * 10,  // Value per dollar
          IF(risk = "High Risk" AND priority >= 8, 
             CONCAT("Increase team by 2-3 members (Current: ", TEXT(current_team, "0"), ")"),
             IF(risk = "Low Risk" AND priority <= 6,
                CONCAT("Consider reducing team by 1 member (Current: ", TEXT(current_team, "0"), ")"),
                CONCAT("Maintain current team size (", TEXT(current_team, "0"), ")")))))),
  
  // Final comprehensive project report
  project_report, VSTACK(
    "=== PROJECT PORTFOLIO MANAGEMENT DASHBOARD ===",
    "",
    "Project Status Overview:",
    TRANSPOSE(project_summary),
    "",
    "Portfolio Key Metrics:",
    CONCAT("Total Portfolio Budget: $", TEXT(total_budget, "#,##0")),
    CONCAT("Total Spent to Date: $", TEXT(total_spent, "#,##0")),
    CONCAT("Portfolio Completion: ", TEXT(portfolio_completion, "0.0%")),
    CONCAT("High Risk Projects: ", TEXT(high_risk_projects, "0"), " of ", TEXT(ROWS(projects), "0")),
    "",
    "Resource Optimization Recommendations:",
    TRANSPOSE(resource_optimization)),
  
  project_report)
```