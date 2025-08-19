---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: lookup & reference
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# FILTER

## FILTER Description

Returns a dynamic array of rows from a dataset that meet specified logical criteria, creating an automatically updating filtered subset whenever source data changes. Unlike traditional lookup functions that return single values, FILTER returns entire matching records with all columns, making it essential for comprehensive data analysis, reporting, and dashboard creation.

> [!f(x)] FILTER Syntax
>
> ```spreadsheets
> FILTER(array, include, [if_empty])
> ```
>
> **Parameters:**
> - `array` (required): Source data range or array to filter (can be single column or multi-column dataset)
> - `include` (required): Boolean array or logical expression that evaluates to TRUE/FALSE for each row
> - `if_empty` (optional): Value to return when no rows match criteria (default: #CALC! error)

> [!f(x)] FILTER Examples
>
> ```spreadsheets
> // Basic single-criteria filter
> FILTER(A2:D100, C2:C100="Active") → returns all active records with all columns
> 
> // Multiple criteria with AND logic using multiplication
> FILTER(SalesData, (Region="West")*(Amount>1000)*(Quarter="Q1")) → West Q1 sales over $1000
> 
> // OR conditions using addition operator
> FILTER(Products, (Category="Electronics")+(Category="Software")+(Priority="High")) → multiple categories or high priority
> 
> // Date-based filtering with custom empty message
> FILTER(OrderHistory, OrderDate>=TODAY()-30, "No recent orders found") → last 30 days with fallback text
> 
> // Complex nested conditions with parentheses
> FILTER(EmployeeData, ((Department="Sales")*(Performance>8))+((Department="Marketing")*(Experience>5))) → high performers or experienced marketers
> 
> // Text pattern matching with wildcards
> FILTER(CustomerList, ISNUMBER(SEARCH("*Corp*", CompanyName))) → companies with "Corp" in name
> 
> // Numeric range filtering
> FILTER(InventoryData, (Stock>=50)*(Stock<=200)*(Category<>"Discontinued")) → optimal stock levels for active products
> 
> // Array formula with dynamic criteria
> FILTER(TransactionData, ISNUMBER(MATCH(AccountID, HighValueAccounts, 0))) → transactions from high-value account list
> ```

## Use Cases

### [[Dynamic dashboard creation]]
- **Real-time executive dashboards**: Create automatically updating reports showing KPIs filtered by department, region, or time period
- **Interactive data exploration**: Enable users to filter large datasets dynamically without complex formulas or pivot tables
- **Exception monitoring**: Automatically identify and highlight records exceeding thresholds, deadlines, or performance targets
- **Comparative analysis**: Filter and display data segments side-by-side for trend comparison and variance analysis

### [[Advanced data analysis]]
- **Customer behavior segmentation**: Filter customers by purchase patterns, demographics, lifetime value, or engagement metrics
- **Financial performance analysis**: Isolate revenue streams, cost centers, or profit margins by various business dimensions
- **Quality control monitoring**: Identify defective products, service failures, or process deviations from operational datasets
- **Market trend identification**: Filter sales, inventory, or customer data to reveal emerging patterns and opportunities

### [[Business intelligence workflows]]
- **Multi-dimensional filtering**: Apply complex logical combinations of criteria across multiple data attributes simultaneously
- **Data validation and cleansing**: Identify inconsistent, missing, or erroneous records in large datasets for data quality improvement
- **Regulatory compliance reporting**: Filter audit trails, transactions, or activities to meet specific compliance requirements
- **Resource optimization**: Identify underutilized assets, overstocked inventory, or inefficient processes through targeted filtering

### [[Operational reporting]]
- **Performance tracking systems**: Monitor employee productivity, project milestones, or operational metrics against targets
- **Inventory management**: Track stock levels, reorder requirements, supplier performance, and product lifecycle stages
- **Customer service analytics**: Filter support tickets, response times, satisfaction scores by various service quality metrics
- **Financial reconciliation**: Identify discrepancies, outstanding items, or unusual transactions in accounting datasets

## Related

### Similar Functions

- [[XLOOKUP]] - Returns single matching values with advanced lookup capabilities, while FILTER returns multiple matching rows
- [[VLOOKUP]] - Finds single matches in vertically arranged data, complemented by FILTER for multiple matching records
- [[SORT]] - Organizes filtered results by specified criteria, frequently combined with FILTER for ordered datasets  
- [[UNIQUE]] - Removes duplicates from filtered datasets, essential for creating clean lists from FILTER results
- [[LAMBDA]] - Creates custom filtering logic that can be reused across multiple FILTER operations

## Array Processing Functions

### [[SORT]]
Essential partnership for organizing filtered results by specific columns, creating ordered and filtered datasets for analysis and presentation.

```spreadsheets
// Filter and sort in single operation
=SORT(FILTER(SalesData, (Region="West")*(Amount>1000)), 4, FALSE)
// Filter Western sales over $1000, sort by amount descending

// Multi-level sorting of complex filtered data
=SORT(FILTER(EmployeeData, (Department="Sales")*(Performance>=8)), {2,5,3}, {TRUE,FALSE,TRUE})
// Filter high-performing sales staff, sort by name ascending, salary descending, hire date ascending

// Dynamic sorting with user-controlled parameters
=SORT(FILTER(ProductCatalog, (Category=UserCategory)*(InStock=TRUE)), SortColumnIndex, SortDirection)
// Filter by user-selected category and stock status, sort by user-selected criteria
```

### [[UNIQUE]]
Removes duplicates from filtered datasets, essential for creating clean lists and avoiding double-counting in analysis workflows.

```spreadsheets
// Extract unique customer list from filtered transactions
=UNIQUE(FILTER(CustomerData, (TransactionDate>=StartDate)*(TransactionAmount>500)))
// List unique high-value customers from specific period

// Create dynamic dropdown lists from filtered data
=UNIQUE(FILTER(ProductCategories, (Active=TRUE)*(HasInventory=TRUE)))
// Generate dropdown of active categories with available inventory

// Identify unique patterns in filtered results
=UNIQUE(FILTER(ErrorLogs, (Severity="Critical")*(ResolvedStatus=FALSE)))
// List unique unresolved critical error types
```

### [[SEQUENCE]]
Creates dynamic ranges for filtering operations and enables complex array-based filtering logic.

```spreadsheets
// Generate filtered month-over-month analysis
=FILTER(MonthlyData, ISNUMBER(MATCH(MONTH(DateColumn), SEQUENCE(3,1,MONTH(TODAY())-2), 0)))
// Filter data for current month and previous 2 months

// Create rolling period filters
=FILTER(DailySales, SalesDate >= TODAY()-SEQUENCE(7))
// Filter last 7 days with array-generated date range

// Multi-period comparative filtering
=FILTER(QuarterlyData, ISNUMBER(MATCH(Quarter, SEQUENCE(4,1,1), 0)))
// Filter all quarters using sequence for comparison
```

## Aggregation Functions

### [[SUM]]
Calculates totals from filtered datasets, enabling dynamic calculations that automatically update when filter criteria change.

```spreadsheets
// Calculate total revenue from filtered transactions
=SUM(FILTER(TransactionAmounts, (Region="North")*(ProductType="Premium")*(Date>=TODAY()-90)))
// Sum Northern premium sales from last 90 days

// Multi-dimensional aggregation with complex criteria
=SUM(FILTER(CommissionData, ((Department="Sales")*(Performance>8))+((Department="Marketing")*(ROI>15))))
// Sum commissions for high-performing sales or high-ROI marketing

// Dynamic period totals with date calculations
=SUM(FILTER(RevenueStream, (YEAR(OrderDate)=YEAR(TODAY()))*(MONTH(OrderDate)<=MONTH(TODAY()))))
// Sum current year revenue through current month
```

### [[AVERAGE]]
Computes statistical averages from filtered subsets, providing insights for specific data segments and performance metrics.

```spreadsheets
// Calculate average performance by filtered segment
=AVERAGE(FILTER(PerformanceScores, (TeamName=SelectedTeam)*(Quarter="Q1")*(Active=TRUE)))
// Average Q1 performance for selected active team

// Conditional averages with exclusions
=AVERAGE(FILTER(ResponseTimes, (ServiceType="Premium")*(Resolution="Success")*(ResponseTime<2000)))
// Average response time for successful premium services under 2 seconds

// Time-series average with dynamic periods
=AVERAGE(FILTER(DailyMetrics, (MetricDate>=TODAY()-30)*(MetricDate<=TODAY())*(BusinessDay=TRUE)))
// Average business day metrics for last 30 days
```

## Date and Time Functions

### [[TODAY]]
Enables dynamic date-based filtering that automatically updates daily, essential for current period analysis and rolling reports.

```spreadsheets
// Dynamic recent activity monitoring
=FILTER(ActivityLog, (ActivityDate>=TODAY()-14)*(Status="Completed")*(Priority="High"))
// High-priority completed activities from last 14 days

// Current period performance tracking
=FILTER(PerformanceData, (ReviewDate>=EOMONTH(TODAY(),-1)+1)*(ReviewDate<=EOMONTH(TODAY(),0)))
// Current month performance reviews

// Overdue item identification with grace periods
=FILTER(TaskList, (DueDate<TODAY()-GracePeriod)*(Status<>"Completed"))
// Overdue incomplete tasks beyond grace period
```

### [[WEEKDAY]]
Filters data by specific days of the week, useful for business pattern analysis and operational scheduling insights.

```spreadsheets
// Business hours transaction filtering
=FILTER(TransactionData, (WEEKDAY(TransactionDate,2)<=5)*(HOUR(TransactionTime)>=9)*(HOUR(TransactionTime)<=17))
// Weekday business hours transactions only

// Weekend vs weekday performance comparison
=FILTER(SalesData, ((WEEKDAY(SalesDate)=1)+(WEEKDAY(SalesDate)=7))*(SalesAmount>MinWeekendSale))
// Weekend sales above minimum threshold

// Day-specific operational analysis
=FILTER(StaffingData, (WEEKDAY(ShiftDate)=2)*(Department="Customer Service"))
// Monday customer service staffing data
```

## Text Processing Functions

### [[SEARCH]]
Enables pattern-based filtering using text matching, essential for content analysis and data classification workflows.

```spreadsheets
// Pattern-based customer filtering
=FILTER(CustomerData, ISNUMBER(SEARCH("Corp*",CompanyName))*(Status="Active"))
// Active corporate customers (companies with "Corp" in name)

// Content classification filtering
=FILTER(ProductDescriptions, (ISNUMBER(SEARCH("*Premium*",Description)))*(Category="Electronics"))
// Electronics products with "Premium" in description

// Error message pattern analysis
=FILTER(LogEntries, (ISNUMBER(SEARCH("ERROR*",Message)))*(Timestamp>=TODAY()-7))
// Error log entries from last 7 days
```

### [[LEN]]
Filters based on text length criteria, useful for data quality analysis and content validation workflows.

```spreadsheets
// Data quality validation filtering
=FILTER(CustomerPhones, (LEN(PhoneNumber)=10)*(LEFT(PhoneNumber,1)<>"0"))
// Valid 10-digit phone numbers not starting with 0

// Content length analysis
=FILTER(ProductDescriptions, (LEN(Description)>=50)*(LEN(Description)<=200)*(Quality="Approved"))
// Approved product descriptions within optimal length range

// Input validation filtering
=FILTER(UserInputs, (LEN(Password)>=8)*(ISNUMBER(SEARCH("*[0-9]*",Password))))
// Passwords meeting minimum length and digit requirements
```

## Commonly Used With Functions Examples

### Advanced Customer Intelligence Dashboard
```spreadsheets
// Create comprehensive customer analysis with multi-dimensional filtering
=LET(
  customer_data, A2:J1000,  // Customer dataset
  transaction_data, K2:Q5000,  // Transaction history
  current_quarter, ROUNDUP(MONTH(TODAY())/3, 0),
  
  // Filter high-value customers from current quarter
  high_value_customers, FILTER(customer_data, 
    (INDEX(customer_data,0,8) >= 10000) *  // Customer LTV >= $10,000
    (INDEX(customer_data,0,5) = "Active") *  // Active status
    (QUARTER(INDEX(customer_data,0,3)) = current_quarter)),  // Current quarter signup
  
  // Get their transaction patterns
  customer_transactions, FILTER(transaction_data,
    ISNUMBER(MATCH(INDEX(transaction_data,0,1), INDEX(high_value_customers,0,1), 0)) *
    (INDEX(transaction_data,0,4) >= TODAY()-90) *  // Last 90 days
    (INDEX(transaction_data,0,3) > 500)),  // Transactions over $500
  
  // Calculate customer segments with behavioral analysis
  customer_segments, MAP(INDEX(high_value_customers,0,1), LAMBDA(customer_id,
    LET(
      customer_txns, FILTER(customer_transactions, INDEX(customer_transactions,0,1) = customer_id),
      txn_count, COUNTA(customer_txns),
      avg_amount, IF(txn_count > 0, AVERAGE(INDEX(customer_txns,0,3)), 0),
      frequency, txn_count / 90 * 30,  // Monthly frequency
      
      // Segment classification
      segment, IF(AND(avg_amount >= 1000, frequency >= 3), "VIP Elite",
                 IF(AND(avg_amount >= 500, frequency >= 2), "High Value Regular",
                    IF(avg_amount >= 1000, "High Spender Low Frequency", "Standard Premium"))),
      
      VSTACK(customer_id, segment, TEXT(avg_amount, "$#,##0"), TEXT(frequency, "0.0"))
    )
  )),
  
  // Generate personalized recommendations
  recommendations, MAP(INDEX(customer_segments, SEQUENCE(ROWS(customer_segments)), 1), 
                      INDEX(customer_segments, SEQUENCE(ROWS(customer_segments)), 2),
                      LAMBDA(customer_id, segment,
    SWITCH(segment,
      "VIP Elite", "Exclusive early access + dedicated account manager + 15% loyalty discount",
      "High Value Regular", "Priority support + quarterly check-in + 10% bulk discount",
      "High Spender Low Frequency", "Engagement campaign + usage incentives + 12% comeback offer",
      "Standard Premium", "Value demonstration + feature education + 8% upgrade incentive"
    )
  )),
  
  // Create comprehensive customer intelligence report
  final_report, VSTACK(
    "=== CUSTOMER INTELLIGENCE DASHBOARD ===",
    "",
    HSTACK("Customer ID", "Segment", "Avg Transaction", "Monthly Frequency", "Recommended Action"),
    HSTACK(INDEX(customer_segments,0,1), INDEX(customer_segments,0,2), INDEX(customer_segments,0,3), 
           INDEX(customer_segments,0,4), recommendations),
    "",
    CONCAT("Total High-Value Customers: ", TEXT(ROWS(high_value_customers), "#,##0")),
    CONCAT("Total Recent Transactions: ", TEXT(ROWS(customer_transactions), "#,##0")),
    CONCAT("Average Transaction Value: ", TEXT(AVERAGE(INDEX(customer_transactions,0,3)), "$#,##0")),
    CONCAT("VIP Elite Customers: ", TEXT(SUMPRODUCT((INDEX(customer_segments,0,2)="VIP Elite")*1), "#,##0"))
  ),
  
  final_report
)
```

### Supply Chain Risk Assessment and Optimization
```spreadsheets
// Build comprehensive supply chain analysis with FILTER-driven risk management
=LET(
  inventory_data, A2:L1000,  // Product inventory data
  supplier_data, M2:T500,    // Supplier performance data
  demand_data, U2:Z2000,     // Historical demand data
  
  // Filter critical inventory items
  critical_inventory, FILTER(inventory_data,
    (INDEX(inventory_data,0,6) <= INDEX(inventory_data,0,7)) *  // Stock <= Reorder Point
    (INDEX(inventory_data,0,8) >= 8) *  // Criticality Score >= 8
    (INDEX(inventory_data,0,5) <> "Discontinued")),  // Not discontinued
  
  // Analyze supplier risk for critical items
  supplier_risk_analysis, MAP(INDEX(critical_inventory,0,9), LAMBDA(supplier_id,
    LET(
      supplier_info, FILTER(supplier_data, INDEX(supplier_data,0,1) = supplier_id),
      delivery_performance, INDEX(supplier_info,1,4),  // On-time delivery %
      quality_score, INDEX(supplier_info,1,5),         // Quality score
      financial_stability, INDEX(supplier_info,1,6),   // Financial rating
      
      // Calculate composite risk score
      risk_score, (100 - delivery_performance) * 0.4 + 
                  (100 - quality_score) * 0.3 + 
                  (10 - financial_stability) * 10 * 0.3,
      
      // Risk classification
      risk_level, IF(risk_score >= 40, "High Risk",
                     IF(risk_score >= 25, "Medium Risk", "Low Risk")),
      
      HSTACK(supplier_id, TEXT(risk_score, "0.0"), risk_level, 
             TEXT(delivery_performance, "0%"), TEXT(quality_score, "0.0"))
    )
  )),
  
  // Demand forecasting for critical items
  demand_forecasts, MAP(INDEX(critical_inventory,0,1), LAMBDA(product_id,
    LET(
      product_demand, FILTER(demand_data, 
        (INDEX(demand_data,0,1) = product_id) *
        (INDEX(demand_data,0,2) >= TODAY()-365)),  // Last 365 days
      
      monthly_avg, AVERAGE(INDEX(product_demand,0,3)) * 30,  // Monthly demand
      trend_factor, (INDEX(product_demand,ROWS(product_demand),3) / 
                     INDEX(product_demand,1,3))^(1/12),      // Monthly growth
      seasonality, 1 + 0.2 * SIN(MONTH(TODAY())/12 * 2 * PI()),  // Seasonal adjustment
      
      // 3-month forecast
      forecast_month1, monthly_avg * trend_factor * seasonality,
      forecast_month2, forecast_month1 * trend_factor,
      forecast_month3, forecast_month2 * trend_factor,
      
      HSTACK(product_id, TEXT(forecast_month1, "#,##0"), 
             TEXT(forecast_month2, "#,##0"), TEXT(forecast_month3, "#,##0"))
    )
  )),
  
  // Generate procurement recommendations
  procurement_actions, MAP(SEQUENCE(ROWS(critical_inventory)), LAMBDA(row,
    LET(
      product_id, INDEX(critical_inventory,row,1),
      current_stock, INDEX(critical_inventory,row,6),
      reorder_point, INDEX(critical_inventory,row,7),
      lead_time, INDEX(critical_inventory,row,10),
      
      // Get corresponding risk and forecast data
      supplier_risk, INDEX(supplier_risk_analysis,row,3),
      month1_forecast, VALUE(INDEX(demand_forecasts,row,2)),
      
      // Calculate emergency order quantity
      safety_multiplier, SWITCH(supplier_risk, "High Risk", 2.0, "Medium Risk", 1.5, 1.2),
      emergency_qty, CEILING(month1_forecast * (lead_time/30) * safety_multiplier, 10),
      
      // Determine action priority
      days_until_stockout, current_stock / (month1_forecast/30),
      priority, IF(days_until_stockout <= 7, "CRITICAL - Order Today",
                  IF(days_until_stockout <= 14, "HIGH - Order This Week",
                     IF(supplier_risk = "High Risk", "MEDIUM - Plan Alternative Supplier",
                        "LOW - Monitor Closely"))),
      
      HSTACK(product_id, TEXT(current_stock, "#,##0"), TEXT(emergency_qty, "#,##0"), 
             TEXT(days_until_stockout, "0.0"), priority)
    )
  )),
  
  // Create comprehensive supply chain dashboard
  supply_chain_dashboard, VSTACK(
    "=== SUPPLY CHAIN RISK ASSESSMENT & PROCUREMENT PLANNING ===",
    "",
    "Critical Inventory Items:",
    HSTACK("Product", "Current Stock", "Emergency Order Qty", "Days Until Stockout", "Action Required"),
    procurement_actions,
    "",
    "Supplier Risk Analysis:",
    HSTACK("Supplier ID", "Risk Score", "Risk Level", "Delivery %", "Quality Score"),
    supplier_risk_analysis,
    "",
    "Demand Forecasts (Next 3 Months):",
    HSTACK("Product ID", "Month 1", "Month 2", "Month 3"),
    demand_forecasts,
    "",
    "Key Performance Indicators:",
    CONCAT("Critical Items Requiring Action: ", TEXT(SUMPRODUCT((LEFT(INDEX(procurement_actions,0,5),8)="CRITICAL")*1), "#,##0")),
    CONCAT("High Risk Suppliers: ", TEXT(SUMPRODUCT((INDEX(supplier_risk_analysis,0,3)="High Risk")*1), "#,##0")),
    CONCAT("Total Emergency Order Value: $", TEXT(SUMPRODUCT(VALUE(INDEX(procurement_actions,0,3)) * 
                                                             XLOOKUP(INDEX(procurement_actions,0,1), INDEX(critical_inventory,0,1), INDEX(critical_inventory,0,11))), "#,##0"))
  ),
  
  supply_chain_dashboard
)
```

### Financial Performance Analytics and Budget Variance Analysis  
```spreadsheets
// Create sophisticated financial analysis with multi-dimensional filtering and variance calculations
=LET(
  financial_data, A2:M2000,    // P&L data with actuals and budget
  cost_center_data, N2:S200,  // Cost center information
  employee_data, T2:Z500,     // Employee and department data
  current_month, MONTH(TODAY()),
  current_year, YEAR(TODAY()),
  
  // Filter current year financial performance
  current_year_actuals, FILTER(financial_data,
    (YEAR(INDEX(financial_data,0,2)) = current_year) *           // Current year
    (INDEX(financial_data,0,3) = "Actual") *                    // Actual transactions
    (INDEX(financial_data,0,8) <> "Eliminated")),               // Exclude eliminations
  
  current_year_budget, FILTER(financial_data,
    (YEAR(INDEX(financial_data,0,2)) = current_year) *
    (INDEX(financial_data,0,3) = "Budget") *
    (INDEX(financial_data,0,8) <> "Eliminated")),
  
  // Calculate department-level variance analysis
  department_analysis, MAP(UNIQUE(INDEX(current_year_actuals,0,4)), LAMBDA(department,
    LET(
      dept_actuals, FILTER(current_year_actuals, INDEX(current_year_actuals,0,4) = department),
      dept_budget, FILTER(current_year_budget, INDEX(current_year_budget,0,4) = department),
      
      // YTD calculations
      ytd_revenue_actual, SUMIFS(INDEX(dept_actuals,0,6), INDEX(dept_actuals,0,5), "Revenue", 
                                INDEX(dept_actuals,0,2), "<="&EOMONTH(TODAY(),0)),
      ytd_revenue_budget, SUMIFS(INDEX(dept_budget,0,6), INDEX(dept_budget,0,5), "Revenue",
                                INDEX(dept_budget,0,2), "<="&EOMONTH(TODAY(),0)),
      
      ytd_expense_actual, SUMIFS(INDEX(dept_actuals,0,6), INDEX(dept_actuals,0,5), "Expense",
                                INDEX(dept_actuals,0,2), "<="&EOMONTH(TODAY(),0)) * -1,
      ytd_expense_budget, SUMIFS(INDEX(dept_budget,0,6), INDEX(dept_budget,0,5), "Expense",
                                INDEX(dept_budget,0,2), "<="&EOMONTH(TODAY(),0)) * -1,
      
      // Variance calculations
      revenue_variance, ytd_revenue_actual - ytd_revenue_budget,
      expense_variance, ytd_expense_budget - ytd_expense_actual,  // Positive = under budget
      
      // Performance indicators
      revenue_variance_pct, IF(ytd_revenue_budget <> 0, revenue_variance / ytd_revenue_budget, 0),
      expense_variance_pct, IF(ytd_expense_budget <> 0, expense_variance / ytd_expense_budget, 0),
      
      // Performance rating
      performance_rating, IF(AND(revenue_variance_pct >= 0.05, expense_variance_pct >= 0.05), "Exceeds Expectations",
                            IF(AND(revenue_variance_pct >= 0, expense_variance_pct >= 0), "Meets Expectations",
                              IF(OR(revenue_variance_pct < -0.1, expense_variance_pct < -0.1), "Below Expectations", 
                                 "Needs Improvement"))),
      
      VSTACK(department, TEXT(ytd_revenue_actual, "$#,##0"), TEXT(ytd_revenue_budget, "$#,##0"),
             TEXT(revenue_variance, "$#,##0"), TEXT(revenue_variance_pct, "0.0%"),
             TEXT(ytd_expense_actual, "$#,##0"), TEXT(ytd_expense_budget, "$#,##0"), 
             TEXT(expense_variance, "$#,##0"), TEXT(expense_variance_pct, "0.0%"), performance_rating)
    )
  )),
  
  // Identify top variance drivers
  variance_drivers, LET(
    all_transactions, VSTACK(current_year_actuals, current_year_budget),
    variance_analysis, MAP(UNIQUE(HSTACK(INDEX(all_transactions,0,4), INDEX(all_transactions,0,7))), 
                          LAMBDA(dept_account,
      LET(
        department, INDEX(dept_account,1,1),
        account, INDEX(dept_account,1,2),
        
        actual_amount, SUMIFS(INDEX(current_year_actuals,0,6), 
                             INDEX(current_year_actuals,0,4), department,
                             INDEX(current_year_actuals,0,7), account,
                             INDEX(current_year_actuals,0,2), "<="&EOMONTH(TODAY(),0)),
        
        budget_amount, SUMIFS(INDEX(current_year_budget,0,6),
                             INDEX(current_year_budget,0,4), department, 
                             INDEX(current_year_budget,0,7), account,
                             INDEX(current_year_budget,0,2), "<="&EOMONTH(TODAY(),0)),
        
        variance, actual_amount - budget_amount,
        variance_abs, ABS(variance),
        
        HSTACK(department, account, TEXT(variance, "$#,##0"), TEXT(variance_abs, "$#,##0"))
      )
    )),
    
    // Sort by absolute variance and return top 10
    top_variances, TAKE(SORT(variance_analysis, 4, FALSE), 10),
    top_variances
  ),
  
  // Generate executive summary with key insights
  executive_insights, LET(
    total_revenue_variance, SUM(VALUE(SUBSTITUTE(SUBSTITUTE(INDEX(department_analysis,0,4), "$", ""), ",", ""))),
    total_expense_variance, SUM(VALUE(SUBSTITUTE(SUBSTITUTE(INDEX(department_analysis,0,8), "$", ""), ",", ""))),
    best_performing_dept, INDEX(SORT(department_analysis, 10, FALSE), 1, 1),
    worst_performing_dept, INDEX(SORT(department_analysis, 10, TRUE), 1, 1),
    
    VSTACK(
      CONCAT("Total Revenue Variance: ", TEXT(total_revenue_variance, "$#,##0")),
      CONCAT("Total Expense Variance: ", TEXT(total_expense_variance, "$#,##0")),
      CONCAT("Net Favorable Variance: ", TEXT(total_revenue_variance + total_expense_variance, "$#,##0")),
      CONCAT("Best Performing Department: ", best_performing_dept),
      CONCAT("Department Needing Attention: ", worst_performing_dept),
      CONCAT("Departments Exceeding Expectations: ", TEXT(SUMPRODUCT((INDEX(department_analysis,0,10)="Exceeds Expectations")*1), "0"))
    )
  ),
  
  // Final comprehensive financial dashboard
  financial_dashboard, VSTACK(
    "=== FINANCIAL PERFORMANCE ANALYTICS & BUDGET VARIANCE REPORT ===",
    "",
    "Executive Summary:",
    executive_insights,
    "",
    "Department Performance Analysis (YTD):",
    HSTACK("Department", "Revenue Actual", "Revenue Budget", "Revenue Var", "Rev Var %",
           "Expense Actual", "Expense Budget", "Expense Var", "Exp Var %", "Performance"),
    department_analysis,
    "",
    "Top 10 Variance Drivers:",
    HSTACK("Department", "Account", "Variance", "Absolute Variance"),
    variance_drivers
  ),
  
  financial_dashboard
)
```

### Advanced HR Analytics and Workforce Optimization
```spreadsheets
// Build comprehensive workforce analysis with FILTER-driven performance and retention insights
=LET(
  employee_data, A2:P1000,      // Employee master data
  performance_data, Q2:X2000,   // Performance reviews and ratings
  compensation_data, Y2:AF1000, // Salary and benefits data
  attendance_data, AG2:AM5000,  // Attendance and time-off records
  
  // Filter active employees with recent performance data
  active_employees, FILTER(employee_data,
    (INDEX(employee_data,0,7) = "Active") *                    // Active status
    (INDEX(employee_data,0,6) >= TODAY()-90) *                 // Recent activity
    (ISNUMBER(XLOOKUP(INDEX(employee_data,0,1), INDEX(performance_data,0,1), 1)))),  // Has performance data
  
  // Calculate comprehensive employee analytics
  employee_analytics, MAP(INDEX(active_employees,0,1), LAMBDA(emp_id,
    LET(
      emp_info, FILTER(active_employees, INDEX(active_employees,0,1) = emp_id),
      emp_performance, FILTER(performance_data, INDEX(performance_data,0,1) = emp_id),
      emp_compensation, FILTER(compensation_data, INDEX(compensation_data,0,1) = emp_id),
      emp_attendance, FILTER(attendance_data, 
        (INDEX(attendance_data,0,1) = emp_id) *
        (INDEX(attendance_data,0,2) >= TODAY()-365)),
      
      // Basic employee information
      department, INDEX(emp_info,1,4),
      job_level, INDEX(emp_info,1,8),
      hire_date, INDEX(emp_info,1,5),
      tenure_years, (TODAY() - hire_date) / 365,
      
      // Performance metrics
      latest_rating, INDEX(SORT(emp_performance, 3, FALSE), 1, 4),  // Most recent rating
      avg_rating, AVERAGE(INDEX(emp_performance,0,4)),
      rating_trend, IF(ROWS(emp_performance) >= 2, 
                      INDEX(emp_performance,1,4) - INDEX(emp_performance,ROWS(emp_performance),4), 0),
      
      // Compensation analysis
      current_salary, INDEX(emp_compensation,1,3),
      market_rate, INDEX(emp_compensation,1,6),
      comp_ratio, IF(market_rate > 0, current_salary / market_rate, 1),
      
      // Attendance patterns
      total_days_available, NETWORKDAYS(TODAY()-365, TODAY()),
      days_absent, SUMIF(INDEX(emp_attendance,0,3), "Absent", 1),
      attendance_rate, (total_days_available - days_absent) / total_days_available,
      
      // Risk scoring for retention
      performance_risk, IF(avg_rating < 3, 30, IF(avg_rating < 3.5, 15, 0)),
      comp_risk, IF(comp_ratio < 0.9, 25, IF(comp_ratio < 0.95, 10, 0)),
      tenure_risk, IF(tenure_years < 1, 20, IF(tenure_years > 10, 15, 0)),
      attendance_risk, IF(attendance_rate < 0.9, 20, IF(attendance_rate < 0.95, 10, 0)),
      trend_risk, IF(rating_trend < -0.5, 25, IF(rating_trend < 0, 10, 0)),
      
      total_risk_score, performance_risk + comp_risk + tenure_risk + attendance_risk + trend_risk,
      
      // Risk categorization
      risk_category, IF(total_risk_score >= 60, "High Risk",
                       IF(total_risk_score >= 40, "Medium Risk", "Low Risk")),
      
      VSTACK(emp_id, department, job_level, TEXT(tenure_years, "0.0"), 
             TEXT(latest_rating, "0.0"), TEXT(avg_rating, "0.0"), TEXT(rating_trend, "+0.0;-0.0"), 
             TEXT(comp_ratio, "0.0%"), TEXT(attendance_rate, "0.0%"), 
             TEXT(total_risk_score, "0"), risk_category)
    )
  )),
  
  // Department-level workforce analysis
  department_summary, MAP(UNIQUE(INDEX(employee_analytics,0,2)), LAMBDA(dept,
    LET(
      dept_employees, FILTER(employee_analytics, INDEX(employee_analytics,0,2) = dept),
      
      headcount, ROWS(dept_employees),
      avg_tenure, AVERAGE(VALUE(INDEX(dept_employees,0,4))),
      avg_performance, AVERAGE(VALUE(INDEX(dept_employees,0,6))),
      avg_comp_ratio, AVERAGE(VALUE(SUBSTITUTE(INDEX(dept_employees,0,8), "%", "")) / 100),
      
      high_risk_count, SUMPRODUCT((INDEX(dept_employees,0,11) = "High Risk") * 1),
      medium_risk_count, SUMPRODUCT((INDEX(dept_employees,0,11) = "Medium Risk") * 1),
      
      high_performers, SUMPRODUCT((VALUE(INDEX(dept_employees,0,5)) >= 4.0) * 1),
      low_performers, SUMPRODUCT((VALUE(INDEX(dept_employees,0,5)) < 3.0) * 1),
      
      // Department health score
      health_score, ((avg_performance - 2.5) / 1.5 * 30) +          // Performance component
                   (MIN(avg_comp_ratio, 1.1) * 25) +                 // Compensation component  
                   ((1 - high_risk_count / headcount) * 25) +        // Retention component
                   (MIN(avg_tenure / 5, 1) * 20),                    // Stability component
      
      VSTACK(dept, TEXT(headcount, "0"), TEXT(avg_tenure, "0.0"), TEXT(avg_performance, "0.0"),
             TEXT(avg_comp_ratio, "0.0%"), TEXT(high_risk_count, "0"), TEXT(medium_risk_count, "0"),
             TEXT(high_performers, "0"), TEXT(low_performers, "0"), TEXT(health_score, "0.0"))
    )
  )),
  
  // Generate actionable workforce recommendations
  workforce_recommendations, MAP(UNIQUE(INDEX(employee_analytics,0,2)), LAMBDA(dept,
    LET(
      dept_data, FILTER(department_summary, INDEX(department_summary,0,1) = dept),
      health_score, VALUE(INDEX(dept_data,1,10)),
      high_risk_count, VALUE(INDEX(dept_data,1,6)),
      low_performers, VALUE(INDEX(dept_data,1,9)),
      avg_comp_ratio, VALUE(SUBSTITUTE(INDEX(dept_data,1,5), "%", "")) / 100,
      
      primary_action, IF(health_score < 60, "CRITICAL: Immediate intervention required",
                        IF(high_risk_count >= 3, "HIGH: Retention strategy needed",
                          IF(low_performers >= 2, "MEDIUM: Performance improvement plan",
                            IF(avg_comp_ratio < 0.95, "LOW: Compensation review recommended",
                               "GOOD: Monitor and maintain")))),
      
      specific_recommendations, SWITCH(TRUE,
        health_score < 60, "Conduct stay interviews, review compensation, implement retention bonuses",
        high_risk_count >= 3, "Identify flight risks, create individual retention plans, improve manager training",
        low_performers >= 2, "Implement PIP process, provide additional training, consider role realignment",
        avg_comp_ratio < 0.95, "Conduct market analysis, plan salary adjustments, communicate career paths",
        "Continue current practices, maintain engagement levels, plan succession"),
      
      HSTACK(dept, primary_action, specific_recommendations)
    )
  )),
  
  // Create comprehensive HR dashboard
  hr_dashboard, VSTACK(
    "=== ADVANCED HR ANALYTICS & WORKFORCE OPTIMIZATION DASHBOARD ===",
    "",
    "Individual Employee Risk Assessment:",
    HSTACK("Employee ID", "Department", "Job Level", "Tenure", "Latest Rating", 
           "Avg Rating", "Trend", "Comp Ratio", "Attendance", "Risk Score", "Risk Level"),
    employee_analytics,
    "",
    "Department Workforce Analysis:",
    HSTACK("Department", "Headcount", "Avg Tenure", "Avg Performance", "Avg Comp Ratio",
           "High Risk", "Medium Risk", "High Performers", "Low Performers", "Health Score"),
    department_summary,
    "",
    "Workforce Recommendations by Department:",
    HSTACK("Department", "Priority Level", "Recommended Actions"),
    workforce_recommendations,
    "",
    "Key Workforce Insights:",
    CONCAT("Total Active Employees: ", TEXT(ROWS(active_employees), "#,##0")),
    CONCAT("High Risk Employees: ", TEXT(SUMPRODUCT((INDEX(employee_analytics,0,11)="High Risk")*1), "#,##0")),
    CONCAT("Average Company Performance Rating: ", TEXT(AVERAGE(VALUE(INDEX(employee_analytics,0,6))), "0.00")),
    CONCAT("Departments Requiring Critical Attention: ", TEXT(SUMPRODUCT((LEFT(INDEX(workforce_recommendations,0,2),8)="CRITICAL")*1), "0")),
    CONCAT("Overall Workforce Health Score: ", TEXT(AVERAGE(VALUE(INDEX(department_summary,0,10))), "0.0"))
  ),
  
  hr_dashboard
)
```
