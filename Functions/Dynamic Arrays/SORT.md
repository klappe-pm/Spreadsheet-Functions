---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - dynamic arrays
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# SORT

## SORT Description

Sorts the contents of a range or array by specified columns in ascending or descending order. Returns a dynamic array that automatically resizes based on the sorted data, supporting multi-column sorting with individual sort orders and custom sort keys.

> [!f(x)] SORT Syntax
>
> ```spreadsheets
> SORT(array, [sort_index], [sort_order], [by_col])
> ```
>
> **Parameters:**
> - `array` (required): The range or array to sort
> - `sort_index` (optional): Column or row number to sort by (default: 1)
> - `sort_order` (optional): 1 for ascending, -1 for descending (default: 1)
> - `by_col` (optional): TRUE to sort by columns, FALSE to sort by rows (default: FALSE)

> [!f(x)] SORT Examples
>
> ```spreadsheets
> // Basic ascending sort by first column
> SORT(A1:C10) → sorts data range by column A ascending
> 
> // Sort by specific column descending
> SORT(sales_data, 3, -1) → sorts by third column (amounts) descending
> 
> // Multi-column sort with different orders
> SORT(employee_data, {2,3}, {1,-1}) → sorts by name ascending, then salary descending
> 
> // Sort by calculated values
> SORT(inventory, MAP(inventory[Stock]*inventory[Price], LAMBDA(x,x)), -1) → sorts by inventory value
> 
> // Dynamic sort based on current date
> SORT(FILTER(tasks, tasks[Due_Date] >= TODAY()), 4, 1) → sorts filtered tasks by due date
> ```

## Use Cases

### [[Report generation]]
- **Top performer lists**: Create ranked lists of sales representatives, products, or customers based on performance metrics like revenue, units sold, or customer satisfaction
- **Financial reporting**: Sort account balances, expense categories, or budget line items for clear presentation in financial statements and management reports
- **Inventory management**: Organize product lists by stock levels, reorder points, or sales velocity to prioritize purchasing and warehouse management decisions
- **Customer analytics**: Rank customers by lifetime value, purchase frequency, or account balance for targeted marketing and relationship management strategies

### [[Data organization]]
- **Database management**: Maintain sorted master lists of employees, products, customers, or locations for easy reference and data integrity verification
- **Compliance reporting**: Organize regulatory data, audit trails, or quality metrics in required sort orders for submission to regulatory bodies
- **Project management**: Sort tasks by priority, deadline, resource requirements, or completion status to optimize workflow and resource allocation
- **Educational records**: Arrange student data by grades, attendance, or performance metrics for academic analysis and reporting

### [[Data analysis]]
- **Trend identification**: Sort time-series data to identify patterns, seasonal variations, or performance trends across different periods or categories
- **Outlier detection**: Organize data by values to easily identify extreme values, anomalies, or data quality issues requiring investigation
- **Comparative analysis**: Sort competing options, benchmark data, or alternative scenarios to facilitate decision-making and strategy development
- **Statistical preparation**: Arrange data in proper order for percentile calculations, quartile analysis, or other order-dependent statistical operations

## Related

### Similar Functions

- [[FILTER]] - Extracts data meeting criteria, often combined with SORT for filtered sorted results
- [[UNIQUE]] - Removes duplicates from arrays, frequently paired with SORT for organized unique lists
- [[RANK]] - Returns rank of values without rearranging data, complementary to SORT's reordering
- [[LARGE]] - Returns nth largest value, similar to SORT but returns single values
- [[SMALL]] - Returns nth smallest value, alternative to SORT for single value extraction

## Data Organization Functions

### [[FILTER]]
Frequently combined with SORT to create organized, filtered datasets that meet specific criteria and maintain proper sort order.

```spreadsheets
// Top 10 customers by revenue this year
=SORT(FILTER(customer_data, YEAR(customer_data[Last_Purchase])=YEAR(TODAY())), 3, -1)[ROWS<=10]
// Filters current year customers and sorts by revenue descending

// Active employees sorted by hire date
=SORT(FILTER(employee_list, employee_list[Status]="Active"), 4, 1)
// Shows only active employees ordered by seniority

// Products with low inventory sorted by reorder priority
=SORT(FILTER(inventory, inventory[Stock] < inventory[Reorder_Point]), 
     MAP(inventory[Stock]/inventory[Reorder_Point], LAMBDA(x,x)), 1)
// Sorts low-stock items by urgency (lowest stock/reorder ratio first)
```

### [[UNIQUE]]
Often paired with SORT to create clean, organized lists of unique values for analysis, reporting, and data validation.

```spreadsheets
// Alphabetical list of unique product categories
=SORT(UNIQUE(product_master[Category]))
// Creates sorted dropdown list of unique categories

// Top unique customers by total purchases
=SORT(MAP(UNIQUE(transactions[Customer_ID]), LAMBDA(cust,
   HSTACK(cust, SUM(FILTER(transactions[Amount], transactions[Customer_ID]=cust))))), 2, -1)
// Lists unique customers with total spend, sorted by amount

// Unique suppliers sorted by average delivery time
=SORT(MAP(UNIQUE(purchase_orders[Supplier]), LAMBDA(sup,
   HSTACK(sup, AVERAGE(FILTER(purchase_orders[Delivery_Days], purchase_orders[Supplier]=sup))))), 2, 1)
// Ranks suppliers by delivery performance
```

## Analytical Functions

### [[RANK]]
Complements SORT by providing positional information without rearranging data, useful for creating rankings alongside sorted lists.

```spreadsheets
// Add rank numbers to sorted sales data
=HSTACK(SORT(sales_data, 3, -1), 
        SEQUENCE(ROWS(SORT(sales_data, 3, -1))))
// Sorted sales data with sequential ranking numbers

// Performance ranking with percentile information
=LET(sorted_performance, SORT(employee_metrics, 5, -1),
     ranks, SEQUENCE(ROWS(sorted_performance)),
     percentiles, ranks / ROWS(sorted_performance),
     HSTACK(sorted_performance, ranks, percentiles))
// Employee performance with rank and percentile

// Comparative ranking across multiple metrics
=MAP(SORT(product_data, 4, -1), LAMBDA(row,
   HSTACK(row, RANK(INDEX(row,1,4), product_data[Revenue], 0),
              RANK(INDEX(row,1,5), product_data[Profit_Margin], 0))))
// Products sorted by revenue with rankings in multiple categories
```

### [[TOP]] / [[LARGE]] / [[SMALL]]
Work with SORT to identify extreme values and create focused reports on best and worst performers.

```spreadsheets
// Top 5 performers with full details
=SORT(sales_data, 3, -1)[ROWS<=5]
// Alternative to LARGE for getting complete records of top performers

// Bottom performers needing attention
=SORT(FILTER(performance_data, performance_data[Score] < AVERAGE(performance_data[Score])), 2, 1)
// Identifies and sorts below-average performers

// Quarterly performance extremes analysis
=LET(sorted_by_performance, SORT(quarterly_data, 4, -1),
     top_quartile, sorted_by_performance[ROWS<=ROUNDUP(ROWS(sorted_by_performance)*0.25,0)],
     bottom_quartile, sorted_by_performance[ROWS>=ROUNDUP(ROWS(sorted_by_performance)*0.75,0)],
     VSTACK("Top Quartile:", top_quartile, "", "Bottom Quartile:", bottom_quartile))
// Identifies and displays top and bottom performing quartiles
```

## Statistical Analysis Functions

### [[PERCENTILE]]
Uses SORT functionality internally and pairs well with sorted data for statistical analysis and threshold determination.

```spreadsheets
// Create percentile-based performance bands
=LET(sorted_scores, SORT(test_scores),
     p25, PERCENTILE(sorted_scores, 0.25),
     p50, PERCENTILE(sorted_scores, 0.5),
     p75, PERCENTILE(sorted_scores, 0.75),
     MAP(sorted_scores, LAMBDA(score,
       HSTACK(score, IF(score >= p75, "Top 25%",
                       IF(score >= p50, "Upper Middle",
                         IF(score >= p25, "Lower Middle", "Bottom 25%")))))))
// Categorizes sorted scores into performance bands

// Sales territory performance with percentile rankings
=LET(territory_performance, SORT(MAP(UNIQUE(sales[Territory]), LAMBDA(territory,
       HSTACK(territory, SUM(FILTER(sales[Amount], sales[Territory]=territory))))), 2, -1),
     performance_values, territory_performance[Performance],
     percentile_ranks, MAP(performance_values, LAMBDA(val,
       PERCENTRANK(performance_values, val))),
     HSTACK(territory_performance, percentile_ranks))
// Territory rankings with percentile positions

// Distribution analysis with sorted quartile breakdown
=LET(sorted_data, SORT(revenue_data[Monthly_Revenue]),
     quartile_boundaries, {QUARTILE(sorted_data,1), QUARTILE(sorted_data,2), QUARTILE(sorted_data,3)},
     quartile_analysis, MAP({1,2,3,4}, LAMBDA(q,
       HSTACK("Q" & q, COUNTIFS(sorted_data, ">" & IF(q=1,0,INDEX(quartile_boundaries,q-1)),
                               sorted_data, "<=" & INDEX(quartile_boundaries,MIN(q,3)))))),
     VSTACK("Quartile Distribution Analysis:", quartile_analysis))
// Analyzes sorted data distribution across quartiles
```

### [[MEDIAN]] / [[MODE]]
Work with sorted data to identify central tendencies and most common values within organized datasets.

```spreadsheets
// Find median performers and their characteristics
=LET(sorted_employees, SORT(employee_data, 6, -1),  // Sort by performance score
     median_position, ROUNDUP(ROWS(sorted_employees)/2, 0),
     median_performers, sorted_employees[ROWS=median_position-2:median_position+2],
     median_score, MEDIAN(sorted_employees[Performance_Score]),
     VSTACK("Median Performance Analysis:", "Median Score: " & median_score, "", median_performers))
// Identifies median performers from sorted employee data

// Most common values in sorted categorical data
=LET(sorted_categories, SORT(customer_data[Segment]),
     unique_segments, UNIQUE(sorted_categories),
     segment_counts, MAP(unique_segments, LAMBDA(segment,
       HSTACK(segment, COUNTIF(sorted_categories, segment)))),
     most_common_segment, INDEX(SORT(segment_counts, 2, -1), 1, 1),
     VSTACK("Customer Segment Distribution (Sorted):", SORT(segment_counts, 2, -1),
            "", "Most Common Segment: " & most_common_segment))
// Analyzes distribution of sorted categorical data

// Trend analysis using sorted time series data
=LET(time_sorted_data, SORT(monthly_sales, 1, 1),  // Sort by month
     monthly_medians, MAP(UNIQUE(time_sorted_data[Month]), LAMBDA(month,
       HSTACK(month, MEDIAN(FILTER(time_sorted_data[Sales], time_sorted_data[Month]=month))))),
     sorted_medians, SORT(monthly_medians, 1, 1),
     median_trend, TREND(sorted_medians[Median_Sales], SEQUENCE(ROWS(sorted_medians))),
     HSTACK(sorted_medians, median_trend))
// Creates trend analysis using median values from time-sorted data
```

## Commonly Used With Functions Examples

### Advanced Performance Dashboard System
```spreadsheets
// Comprehensive employee performance analysis with multi-dimensional sorting
=LET(
   employee_base, employee_master,
   performance_data, quarterly_metrics,
   
   // Create comprehensive employee analysis
   employee_analysis, MAP(employee_base[Employee_ID], LAMBDA(emp_id,
     LET(
       emp_info, XLOOKUP(emp_id, employee_base[Employee_ID], employee_base),
       emp_name, INDEX(emp_info, 1, 2),
       emp_dept, INDEX(emp_info, 1, 3),
       emp_role, INDEX(emp_info, 1, 4),
       
       // Performance metrics for this employee
       emp_performance, FILTER(performance_data, performance_data[Employee_ID] = emp_id),
       
       avg_performance, AVERAGE(emp_performance[Performance_Score]),
       sales_total, SUM(emp_performance[Sales_Amount]),
       customer_satisfaction, AVERAGE(emp_performance[Customer_Rating]),
       projects_completed, SUM(emp_performance[Projects_Completed]),
       
       // Calculate composite score
       composite_score, (avg_performance * 0.4) + 
                       (PERCENTRANK(employee_base[Employee_ID], sales_total) * 40 * 0.3) + 
                       (customer_satisfaction * 10 * 0.2) + 
                       (projects_completed * 0.1),
       
       HSTACK(emp_id, emp_name, emp_dept, emp_role, avg_performance, 
              sales_total, customer_satisfaction, projects_completed, composite_score)))),
   
   // Multi-level sorting analysis
   top_overall_performers, SORT(employee_analysis, 9, -1)[ROWS<=10],
   top_by_department, MAP(UNIQUE(employee_analysis[Department]), LAMBDA(dept,
     LET(dept_employees, FILTER(employee_analysis, employee_analysis[Department] = dept),
         top_dept_performer, SORT(dept_employees, 9, -1)[ROWS<=3],
         VSTACK(HSTACK(dept & " - Top Performers", "", "", "", "", "", "", "", ""), top_dept_performer)))),
   
   // Performance tier analysis
   performance_tiers, LET(
     sorted_by_composite, SORT(employee_analysis, 9, -1),
     total_employees, ROWS(sorted_by_composite),
     tier1_count, ROUNDUP(total_employees * 0.2, 0),
     tier2_count, ROUNDUP(total_employees * 0.3, 0),
     
     tier1_employees, sorted_by_composite[ROWS<=tier1_count],
     tier2_employees, sorted_by_composite[ROWS=tier1_count+1:tier1_count+tier2_count],
     tier3_employees, sorted_by_composite[ROWS>=tier1_count+tier2_count+1],
     
     VSTACK(
       HSTACK("TIER 1 - TOP 20% PERFORMERS", "", "", "", "", "", "", "", ""),
       tier1_employees,
       "",
       HSTACK("TIER 2 - SOLID PERFORMERS (Next 30%)", "", "", "", "", "", "", "", ""),
       tier2_employees[ROWS<=5],  // Show top 5 from tier 2
       "",
       HSTACK("TIER 3 - DEVELOPMENT NEEDED (Bottom 50%)", "", "", "", "", "", "", "", ""),
       tier3_employees[ROWS<=5])),  // Show bottom 5 from tier 3
   
   // Final comprehensive dashboard
   performance_dashboard, VSTACK(
     HSTACK("=== EMPLOYEE PERFORMANCE DASHBOARD ===", "", "", "", "", "", "", "", ""),
     HSTACK("Total Employees:", ROWS(employee_analysis), "Analysis Date:", TEXT(TODAY(), "yyyy-mm-dd"), "", "", "", "", ""),
     "",
     HSTACK("=== TOP 10 OVERALL PERFORMERS ===", "", "", "", "", "", "", "", ""),
     HSTACK("ID", "Name", "Department", "Role", "Avg Score", "Sales", "Cust Rating", "Projects", "Composite"),
     top_overall_performers,
     "",
     performance_tiers),
   
   performance_dashboard)
```

### Dynamic Inventory Optimization System
```spreadsheets
// Comprehensive inventory management with multi-criteria sorting
=LET(
   inventory_raw, current_inventory,
   sales_velocity, sales_history,
   supplier_data, supplier_master,
   
   // Enhanced inventory analysis with sorting
   inventory_enhanced, MAP(inventory_raw[Product_ID], LAMBDA(prod_id,
     LET(
       // Basic inventory info
       product_info, XLOOKUP(prod_id, inventory_raw[Product_ID], inventory_raw),
       current_stock, INDEX(product_info, 1, 2),
       unit_cost, INDEX(product_info, 1, 3),
       reorder_point, INDEX(product_info, 1, 4),
       
       // Sales analysis
       product_sales, FILTER(sales_velocity, sales_velocity[Product_ID] = prod_id),
       last_90_days, FILTER(product_sales, product_sales[Date] >= TODAY()-90),
       
       daily_velocity, SUM(last_90_days[Quantity]) / 90,
       days_of_supply, IF(daily_velocity > 0, current_stock / daily_velocity, 999),
       
       // Supplier information
       supplier_id, INDEX(product_info, 1, 5),
       supplier_info, XLOOKUP(supplier_id, supplier_data[Supplier_ID], supplier_data),
       lead_time, INDEX(supplier_info, 1, 3),
       supplier_rating, INDEX(supplier_info, 1, 4),
       
       // Risk and priority calculations
       stockout_risk, IF(days_of_supply <= lead_time, "HIGH",
                         IF(days_of_supply <= lead_time * 2, "MEDIUM", "LOW")),
       
       inventory_value, current_stock * unit_cost,
       velocity_rank, RANK(daily_velocity, FILTER(sales_velocity[Quantity], 
                          sales_velocity[Date] >= TODAY()-90), 0),
       
       // Priority score (lower = higher priority)
       priority_score, SWITCH(stockout_risk,
                             "HIGH", 1,
                             "MEDIUM", 2,
                             "LOW", 3) + 
                      (velocity_rank / ROWS(UNIQUE(inventory_raw[Product_ID]))) * 2,
       
       HSTACK(prod_id, current_stock, unit_cost, reorder_point, daily_velocity,
              days_of_supply, lead_time, supplier_rating, stockout_risk, 
              inventory_value, priority_score)))),
   
   // Multiple sorting perspectives
   by_urgency, SORT(FILTER(inventory_enhanced, inventory_enhanced[Stockout_Risk] <> "LOW"), 11, 1),
   by_value, SORT(inventory_enhanced, 10, -1),
   by_velocity, SORT(inventory_enhanced, 5, -1),
   by_supplier_performance, SORT(inventory_enhanced, 8, -1),
   
   // ABC Analysis with sorting
   abc_analysis, LET(
     value_sorted, SORT(inventory_enhanced, 10, -1),
     total_value, SUM(value_sorted[Inventory_Value]),
     running_percentage, SCAN(0, value_sorted[Inventory_Value], 
                             LAMBDA(acc, val, (acc + val) / total_value)),
     
     abc_categories, MAP(running_percentage, LAMBDA(pct,
       IF(pct <= 0.8, "A - High Value (80%)",
          IF(pct <= 0.95, "B - Medium Value (15%)", "C - Low Value (5%)")))),
     
     HSTACK(value_sorted, abc_categories)),
   
   // Action matrix based on multiple sorts
   action_matrix, LET(
     high_priority, FILTER(by_urgency, by_urgency[Priority_Score] <= 2),
     medium_priority, FILTER(inventory_enhanced, 
                            (inventory_enhanced[Priority_Score] > 2) * 
                            (inventory_enhanced[Priority_Score] <= 4)),
     low_priority, FILTER(inventory_enhanced, inventory_enhanced[Priority_Score] > 4),
     
     VSTACK(
       HSTACK("IMMEDIATE ACTION REQUIRED (Sort by urgency)", "", "", "", "", "", "", "", "", "", ""),
       HSTACK("Product ID", "Stock", "Cost", "Reorder Pt", "Velocity", "Days Supply", "Lead Time", "Risk", "Value", "Action", ""),
       MAP(high_priority[ROWS<=10], LAMBDA(row, 
         HSTACK(row[{1,2,3,4,5,6,7,9}], INDEX(row,1,10), 
                IF(INDEX(row,1,6) <= INDEX(row,1,7), "URGENT REORDER", "MONITOR CLOSELY")))),
       "",
       HSTACK("HIGH VALUE ITEMS (Sort by inventory value)", "", "", "", "", "", "", "", "", "", ""),
       HSTACK("Product ID", "Current Stock", "Unit Cost", "Inventory Value", "ABC Category", "Velocity", "Supplier Rating", "", "", "", ""),
       by_value[ROWS<=10][{1,2,3,10,12,5,8}],
       "",
       HSTACK("FAST MOVING ITEMS (Sort by sales velocity)", "", "", "", "", "", "", "", "", "", ""),
       by_velocity[ROWS<=10][{1,2,5,6,9,10}])),
   
   // Executive summary with key metrics
   executive_summary, LET(
     total_items, ROWS(inventory_enhanced),
     high_risk_count, COUNTIF(inventory_enhanced[Stockout_Risk], "HIGH"),
     medium_risk_count, COUNTIF(inventory_enhanced[Stockout_Risk], "MEDIUM"),
     total_inventory_value, SUM(inventory_enhanced[Inventory_Value]),
     avg_days_supply, AVERAGE(inventory_enhanced[Days_of_Supply]),
     
     VSTACK(
       HSTACK("=== INVENTORY EXECUTIVE SUMMARY ===", "", "", "", "", "", "", "", "", "", ""),
       HSTACK("Total SKUs:", total_items, "Total Value:", TEXT(total_inventory_value, "$#,##0,K"), 
              "Avg Days Supply:", ROUND(avg_days_supply, 1), "", "", "", "", ""),
       HSTACK("High Risk Items:", high_risk_count & " (" & TEXT(high_risk_count/total_items, "0%") & ")",
              "Medium Risk:", medium_risk_count & " (" & TEXT(medium_risk_count/total_items, "0%") & ")", 
              "", "", "", "", "", "", ""),
       "")),
   
   // Final comprehensive report
   inventory_report, VSTACK(
     executive_summary,
     action_matrix),
   
   inventory_report)
```

### Customer Segmentation and Lifetime Value Analysis
```spreadsheets
// Advanced customer analysis using sophisticated sorting strategies
=LET(
   customer_master, customer_data,
   transaction_history, sales_transactions,
   product_master, product_catalog,
   
   // Customer lifetime value calculation with sorting
   customer_ltv_analysis, MAP(UNIQUE(customer_master[Customer_ID]), LAMBDA(cust_id,
     LET(
       // Basic customer info
       customer_info, XLOOKUP(cust_id, customer_master[Customer_ID], customer_master),
       customer_name, INDEX(customer_info, 1, 2),
       acquisition_date, INDEX(customer_info, 1, 3),
       customer_segment, INDEX(customer_info, 1, 4),
       
       // Transaction analysis
       customer_transactions, FILTER(transaction_history, 
                                   transaction_history[Customer_ID] = cust_id),
       
       total_revenue, SUM(customer_transactions[Amount]),
       transaction_count, ROWS(customer_transactions),
       avg_order_value, total_revenue / transaction_count,
       
       first_purchase, MIN(customer_transactions[Date]),
       last_purchase, MAX(customer_transactions[Date]),
       customer_lifespan, last_purchase - first_purchase + 1,
       recency_days, TODAY() - last_purchase,
       
       // Purchase behavior analysis
       unique_products, ROWS(UNIQUE(customer_transactions[Product_ID])),
       avg_days_between_purchases, customer_lifespan / transaction_count,
       
       // Product category diversity
       product_categories, MAP(customer_transactions[Product_ID], LAMBDA(prod_id,
         XLOOKUP(prod_id, product_master[Product_ID], product_master[Category]))),
       unique_categories, ROWS(UNIQUE(product_categories)),
       
       // CLV calculation (simplified)
       monthly_value, total_revenue / MAX(1, customer_lifespan / 30),
       predicted_lifespan_months, IF(recency_days <= 90, 24, 
                                    IF(recency_days <= 180, 12, 6)),
       customer_lifetime_value, monthly_value * predicted_lifespan_months,
       
       // RFM scoring components
       recency_score, IF(recency_days <= 30, 5,
                        IF(recency_days <= 60, 4,
                          IF(recency_days <= 90, 3,
                            IF(recency_days <= 180, 2, 1)))),
       
       frequency_score, IF(transaction_count >= 20, 5,
                          IF(transaction_count >= 10, 4,
                            IF(transaction_count >= 5, 3,
                              IF(transaction_count >= 2, 2, 1)))),
       
       monetary_score, IF(total_revenue >= 10000, 5,
                         IF(total_revenue >= 5000, 4,
                           IF(total_revenue >= 1000, 3,
                             IF(total_revenue >= 500, 2, 1)))),
       
       rfm_composite, recency_score + frequency_score + monetary_score,
       
       HSTACK(cust_id, customer_name, customer_segment, total_revenue, transaction_count,
              avg_order_value, recency_days, unique_products, unique_categories,
              customer_lifetime_value, recency_score, frequency_score, monetary_score, rfm_composite)))),
   
   // Multiple sorting perspectives for different business needs
   by_lifetime_value, SORT(customer_ltv_analysis, 10, -1),
   by_recency, SORT(customer_ltv_analysis, 7, 1),  // Most recent first
   by_frequency, SORT(customer_ltv_analysis, 5, -1),
   by_monetary, SORT(customer_ltv_analysis, 4, -1),
   by_rfm_score, SORT(customer_ltv_analysis, 14, -1),
   
   // Segment-based analysis with sorting
   segment_analysis, MAP(UNIQUE(customer_ltv_analysis[Customer_Segment]), LAMBDA(segment,
     LET(
       segment_customers, FILTER(customer_ltv_analysis, 
                                customer_ltv_analysis[Customer_Segment] = segment),
       segment_sorted, SORT(segment_customers, 10, -1),  // Sort by CLV within segment
       
       customer_count, ROWS(segment_customers),
       avg_clv, AVERAGE(segment_customers[Customer_Lifetime_Value]),
       total_revenue, SUM(segment_customers[Total_Revenue]),
       avg_recency, AVERAGE(segment_customers[Recency_Days]),
       top_customer, INDEX(segment_sorted, 1, 2),
       
       HSTACK(segment, customer_count, avg_clv, total_revenue, avg_recency, top_customer)))),
   
   // Customer lifecycle stage analysis
   lifecycle_analysis, LET(
     lifecycle_categories, MAP(customer_ltv_analysis, LAMBDA(row,
       LET(
         recency, INDEX(row, 1, 7),
         frequency, INDEX(row, 1, 5),
         monetary, INDEX(row, 1, 4),
         
         lifecycle_stage, IF(AND(recency <= 30, frequency >= 5), "Champions",
                            IF(AND(recency <= 60, frequency >= 3), "Loyal Customers",
                              IF(AND(recency <= 90, monetary >= 1000), "Potential Loyalists",
                                IF(recency <= 30, "New Customers",
                                  IF(AND(recency > 90, frequency >= 3), "At Risk",
                                    IF(recency > 180, "Can't Lose Them", "Need Attention")))))),
         
         HSTACK(row, lifecycle_stage)))),
     
     // Sort lifecycle categories for action prioritization
     lifecycle_priority_order, {"Can't Lose Them", "At Risk", "Champions", "Loyal Customers", 
                               "Potential Loyalists", "New Customers", "Need Attention"},
     
     lifecycle_sorted, SORT(lifecycle_categories, 
                           MAP(lifecycle_categories[Lifecycle_Stage], LAMBDA(stage,
                             IFERROR(MATCH(stage, lifecycle_priority_order, 0), 99))), 1)),
   
   // Action recommendations by sorted customer segments
   action_recommendations, VSTACK(
     HSTACK("=== HIGH-VALUE CUSTOMER RETENTION (Top 10% by CLV) ===", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
     HSTACK("Customer", "Segment", "CLV", "Revenue", "Recency", "Action", "", "", "", "", "", "", "", "", ""),
     MAP(by_lifetime_value[ROWS<=ROUNDUP(ROWS(by_lifetime_value)*0.1,0)], LAMBDA(row,
       HSTACK(INDEX(row,1,2), INDEX(row,1,3), TEXT(INDEX(row,1,10), "$#,##0"), 
              TEXT(INDEX(row,1,4), "$#,##0"), INDEX(row,1,7),
              IF(INDEX(row,1,7) > 60, "URGENT: Re-engagement Campaign", "VIP Program Invitation")))),
     "",
     HSTACK("=== AT-RISK CUSTOMER RECOVERY (High value, high recency) ===", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
     MAP(FILTER(lifecycle_sorted, 
               (lifecycle_sorted[Lifecycle_Stage] = "At Risk") + 
               (lifecycle_sorted[Lifecycle_Stage] = "Can't Lose Them"))[ROWS<=15], 
         LAMBDA(row,
           HSTACK(INDEX(row,1,2), TEXT(INDEX(row,1,4), "$#,##0"), INDEX(row,1,7), 
                  INDEX(row,1,15), "Win-back Campaign"))),
     "",
     HSTACK("=== NEW CUSTOMER DEVELOPMENT (Recent acquisitions) ===", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
     MAP(FILTER(lifecycle_sorted, lifecycle_sorted[Lifecycle_Stage] = "New Customers")[ROWS<=10],
         LAMBDA(row,
           HSTACK(INDEX(row,1,2), TEXT(INDEX(row,1,4), "$#,##0"), INDEX(row,1,5),
                  "Onboarding & Cross-sell")))),
   
   // Executive dashboard with key insights
   executive_dashboard, VSTACK(
     HSTACK("=== CUSTOMER LIFETIME VALUE ANALYSIS DASHBOARD ===", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
     HSTACK("Total Customers:", ROWS(customer_ltv_analysis), 
            "Total CLV:", TEXT(SUM(customer_ltv_analysis[Customer_Lifetime_Value]), "$#,##0,K"),
            "Avg CLV:", TEXT(AVERAGE(customer_ltv_analysis[Customer_Lifetime_Value]), "$#,##0"), "", "", "", "", "", "", "", "", "", "", ""),
     "",
     HSTACK("=== SEGMENT PERFORMANCE (Sorted by Average CLV) ===", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
     HSTACK("Segment", "Customers", "Avg CLV", "Total Revenue", "Avg Recency", "Top Customer", "", "", "", "", "", "", "", "", ""),
     SORT(segment_analysis, 3, -1),
     "",
     action_recommendations),
   
   executive_dashboard)
```
