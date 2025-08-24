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
# SORT

## SORT Description

Sorts the contents of a range or array by one or multiple columns in ascending or descending order. Returns a dynamic array that automatically updates when source data changes, making it essential for real-time data organization and analysis.

> [!f(x)] SORT Syntax
>
> ```spreadsheets
> SORT(array, [sort_index], [sort_order], [by_col])
> ```
>
> **Parameters:**
> - `array` (required): The range or array to be sorted
> - `sort_index` (optional): Column or row index number to sort by (default: 1)
> - `sort_order` (optional): 1 for ascending (default), -1 for descending
> - `by_col` (optional): TRUE to sort by columns, FALSE to sort by rows (default: FALSE)

> [!f(x)] SORT Examples
>
> ```spreadsheets
> // Basic ascending sort by first column
> SORT(A1:C10) → sorts entire range by column A values ascending
> 
> // Sort by specific column in descending order
> SORT(A1:D20, 3, -1) → sorts by column 3 (C) in descending order
> 
> // Sort by multiple columns using array syntax
> SORT(A1:E15, {2, 5}, {1, -1}) → sort by column 2 ascending, then column 5 descending
> 
> // Sort names alphabetically
> SORT({"John"; "Alice"; "Bob"; "Carol"}) → {"Alice"; "Bob"; "Carol"; "John"}
> 
> // Sort sales data by revenue descending
> SORT(sales_range, 4, -1) → sorts sales data by 4th column (revenue) highest to lowest
> ```

## Use Cases

### [[Data organization]]
- **Sales reporting**: Sort customer data by revenue, purchase frequency, or geographic region to identify top performers and market opportunities
- **Employee management**: Organize staff records by department, hire date, salary, or performance ratings for HR analysis and reporting
- **Inventory tracking**: Arrange product data by stock levels, reorder points, or sales velocity to optimize inventory management and procurement
- **Financial analysis**: Order transactions by date, amount, or category to track spending patterns and budget performance over time

### [[Dynamic reporting]]
- **Real-time dashboards**: Create automatically updating reports where data refreshes and re-sorts when source information changes
- **Top N analysis**: Generate dynamic lists of best performers, highest values, or most critical items that adjust automatically with new data
- **Trend analysis**: Sort time-series data to identify patterns, seasonal variations, and performance trends across different periods
- **Comparative analysis**: Organize competitive data, benchmarks, or performance metrics to facilitate easy comparison and decision-making

### [[Data preparation]]
- **Analysis preprocessing**: Prepare datasets for statistical analysis by organizing data in logical order for trend identification and pattern recognition
- **Lookup optimization**: Sort reference tables and lookup data to improve formula performance and create more efficient data retrieval systems
- **Data validation**: Organize data to identify duplicates, outliers, or inconsistencies that may require cleaning or correction
- **Report formatting**: Structure data in presentation-ready order for charts, pivot tables, and executive summaries

## Related

### Similar Functions

- [[SORTBY]] - Sorts an array by values in corresponding arrays, more flexible for complex sorting criteria
- [[FILTER]] - Extracts data meeting criteria, often combined with SORT for ordered filtered results
- [[UNIQUE]] - Removes duplicates from arrays, frequently used with SORT to create unique sorted lists
- [[RANK]] - Assigns rank numbers to values, provides positional information but doesn't rearrange data
- [[LARGE]] - Returns nth largest value, useful for extracting top values from sorted data

## Array Manipulation Functions

### [[FILTER]]
Often combined with SORT to create sorted subsets of data based on specific criteria, enabling dynamic reports that show only relevant sorted information.

```spreadsheets
// Sort filtered sales data by performance
=SORT(FILTER(sales_data, sales_data[Region]="West"), 3, -1)
// Shows West region sales sorted by performance descending

// Create top performers list with filtering and sorting
=SORT(FILTER(employee_data, employee_data[Department]="Sales"), 5, -1)
// Sales department employees sorted by performance score

// Dynamic date range with sorted results
=SORT(FILTER(transaction_data, 
  (transaction_data[Date]>=start_date)*(transaction_data[Date]<=end_date)), 2, 1)
// Transactions in date range sorted by amount ascending
```

### [[UNIQUE]]
Pairs with SORT to create clean, organized lists without duplicates, essential for creating reference lists and data validation ranges.

```spreadsheets
// Create sorted list of unique customers
=SORT(UNIQUE(customer_data[Customer_Name]))
// Alphabetical list of all customers without duplicates

// Generate unique product categories in order
=SORT(UNIQUE(product_data[Category]))
// Sorted list of all product categories for dropdown lists

// Combine multiple sources for unique sorted list
=SORT(UNIQUE(VSTACK(Q1_customers, Q2_customers, Q3_customers, Q4_customers)))
// Unique customers from all quarters in alphabetical order
```

## Data Analysis Functions

### [[SORTBY]]
Extends SORT functionality by allowing sorting based on different arrays or complex criteria, providing more sophisticated sorting options.

```spreadsheets
// Sort products by calculated profit margin
=SORTBY(product_data, (product_data[Price]-product_data[Cost])/product_data[Price], -1)
// Products sorted by highest profit margin

// Multi-criteria sorting with SORTBY
=SORTBY(employee_data, employee_data[Department], 1, employee_data[Salary], -1)
// Employees sorted by department, then by salary descending within department

// Sort by external ranking array
=SORTBY(competitor_data, ranking_scores, -1)
// Sort competitors by externally calculated ranking scores
```

### [[RANK]]
Works with SORT to understand positional relationships in data, helping identify where specific values fall in ordered datasets.

```spreadsheets
// Show sorted data with original ranks
=HSTACK(SORT(sales_data, 2, -1), 
        MAP(SORT(sales_data, 2, -1)[Sales], LAMBDA(sale, RANK(sale, sales_data[Sales], 0))))
// Sorted sales with original rank positions

// Create ranking report with sorted presentation
=LET(sorted_data, SORT(performance_data, 3, -1),
     HSTACK("Rank", SEQUENCE(ROWS(sorted_data)), sorted_data))
// Performance data sorted with new sequential rankings

// Compare sorted vs original rankings
=HSTACK(SORT(data_range, 1), "Original Rank", 
        MAP(SORT(data_range, 1), LAMBDA(val, RANK(val, data_range[Values], 1))))
// Shows how sorting changes positional rankings
```

## Statistical Functions

### [[LARGE]]
Combines with SORT to extract and analyze top values, providing both individual top performers and their context within sorted datasets.

```spreadsheets
// Show top 5 values with full sorted context
=SORT(FILTER(sales_data, sales_data[Amount]>=LARGE(sales_data[Amount], 5)), 2, -1)
// Complete records for top 5 sales amounts

// Create percentile analysis with sorting
=LET(sorted_values, SORT(revenue_data),
     top_10_percent, LARGE(revenue_data, ROUNDUP(ROWS(revenue_data)*0.1, 0)),
     FILTER(sorted_values, sorted_values>=top_10_percent))
// Sorted data showing only top 10% of values

// Dynamic threshold sorting
=SORT(FILTER(customer_data, customer_data[Lifetime_Value]>=LARGE(customer_data[Lifetime_Value], threshold_count)), 3, -1)
// Customers above dynamic threshold sorted by value
```

### [[PERCENTILE]]
Uses SORT to understand data distribution and identify cutoff points within ordered datasets for analysis and reporting.

```spreadsheets
// Sort data by percentile ranges
=LET(sorted_data, SORT(test_scores),
     percentile_75, PERCENTILE(test_scores, 0.75),
     percentile_25, PERCENTILE(test_scores, 0.25),
     HSTACK(sorted_data, 
            MAP(sorted_data, LAMBDA(score, 
                IF(score>=percentile_75, "Top 25%", 
                   IF(score<=percentile_25, "Bottom 25%", "Middle 50%"))))))
// Sorted scores with percentile classifications

// Create performance bands with sorting
=SORT(HSTACK(employee_data, 
             MAP(employee_data[Rating], LAMBDA(rating,
                 IF(rating>=PERCENTILE(employee_data[Rating], 0.9), "Top 10%",
                    IF(rating>=PERCENTILE(employee_data[Rating], 0.7), "Above Average", 
                       IF(rating>=PERCENTILE(employee_data[Rating], 0.3), "Average", "Below Average")))))), 
      5, -1)
// Employees sorted by rating with performance bands
```

## Commonly Used With Functions Examples

### Comprehensive Sales Analytics Dashboard
```spreadsheets
// Create a multi-dimensional sales analysis with dynamic sorting
=LET(
   base_data, sales_transactions,
   
   // Sort by different criteria for various views
   by_revenue, SORT(base_data, 4, -1),  // Sort by revenue descending
   by_date, SORT(base_data, 1, -1),     // Sort by most recent first
   by_customer, SORT(base_data, 2, 1),  // Sort by customer alphabetically
   
   // Create filtered and sorted top performers
   revenue_threshold, PERCENTILE(base_data[Revenue], 0.8),
   top_performers, SORT(FILTER(base_data, base_data[Revenue] >= revenue_threshold), 4, -1),
   
   // Generate summary statistics from sorted data
   top_10_customers, SORT(
     GROUPBY(base_data[Customer], base_data[Revenue], SUM), 2, -1)[ROWS<=10],
   
   monthly_trends, SORT(
     GROUPBY(TEXT(base_data[Date], "yyyy-mm"), base_data[Revenue], SUM), 1, 1),
   
   // Create comprehensive dashboard layout
   dashboard, VSTACK(
     HSTACK("=== SALES DASHBOARD ===", "", "", ""),
     HSTACK("Top 10 Customers", "Monthly Trends", "Recent Transactions", "Top Performers"),
     HSTACK(
       VSTACK("Customer", top_10_customers[Customer][ROWS<=5]),
       VSTACK("Month", monthly_trends[Month][ROWS<=5]), 
       VSTACK("Date", by_date[Date][ROWS<=5]),
       VSTACK("Revenue", top_performers[Revenue][ROWS<=5]))),
   
   dashboard)
```

### Dynamic Employee Performance Management System
```spreadsheets
// Build comprehensive employee ranking and development system
=LAMBDA(employee_data, evaluation_period, department_filter,
   LET(
     // Filter data for specific period and department
     filtered_data, FILTER(employee_data, 
       (employee_data[Period] = evaluation_period) * 
       (employee_data[Department] = department_filter)),
     
     // Create multiple sorted views
     by_overall_score, SORT(filtered_data, 5, -1),  // Overall performance descending
     by_improvement, SORT(filtered_data, 6, -1),    // Improvement rate descending
     by_tenure, SORT(filtered_data, 3, 1),          // By years of service
     
     // Calculate percentile rankings
     performance_scores, filtered_data[Overall_Score],
     top_10_threshold, PERCENTILE(performance_scores, 0.9),
     improvement_needed_threshold, PERCENTILE(performance_scores, 0.2),
     
     // Create development categories with sorting
     development_categories, SORT(HSTACK(
       filtered_data[Employee], 
       filtered_data[Overall_Score],
       MAP(filtered_data[Overall_Score], LAMBDA(score,
         IF(score >= top_10_threshold, "High Performer - Mentor",
            IF(score <= improvement_needed_threshold, "Development Focus", 
               "Core Performer - Growth Ready"))))), 2, -1),
     
     // Generate succession planning data
     succession_candidates, SORT(FILTER(filtered_data, 
       (filtered_data[Overall_Score] >= top_10_threshold) * 
       (filtered_data[Leadership_Score] >= PERCENTILE(filtered_data[Leadership_Score], 0.8))), 5, -1),
     
     // Create final comprehensive report
     performance_report, VSTACK(
       HSTACK("Employee", "Score", "Category", "Rank", "Development Plan"),
       HSTACK(
         development_categories[Employee],
         development_categories[Overall_Score], 
         development_categories[Category],
         SEQUENCE(ROWS(development_categories)),
         MAP(development_categories[Category], LAMBDA(cat,
           SWITCH(cat, 
             "High Performer - Mentor", "Leadership Development",
             "Development Focus", "Performance Improvement Plan",
             "Core Performer - Growth Ready", "Skill Enhancement")))),
       "",
       HSTACK("=== SUCCESSION CANDIDATES ===", "", "", "", ""),
       HSTACK("Employee", "Score", "Leadership", "Ready", "Timeline"),
       HSTACK(
         succession_candidates[Employee],
         succession_candidates[Overall_Score],
         succession_candidates[Leadership_Score],
         "Yes",
         "6-12 months")),
     
     performance_report))
```

### Advanced Inventory Management with Multi-Criteria Sorting
```spreadsheets
// Create sophisticated inventory analysis with multiple sorting dimensions
=LET(
   inventory_data, current_inventory,
   
   // Calculate key metrics for sorting decisions
   days_of_supply, inventory_data[Current_Stock] / inventory_data[Daily_Usage],
   reorder_priority, (inventory_data[Reorder_Point] - inventory_data[Current_Stock]) / inventory_data[Reorder_Point],
   value_concentration, inventory_data[Unit_Cost] * inventory_data[Current_Stock],
   
   // Create enhanced dataset with calculated fields
   enhanced_data, HSTACK(
     inventory_data,
     days_of_supply,
     reorder_priority, 
     value_concentration),
   
   // Sort by different business priorities
   critical_reorder, SORT(FILTER(enhanced_data, reorder_priority > 0.8), 8, -1),  // Urgent reorders
   high_value_items, SORT(enhanced_data, 9, -1),  // By inventory value
   fast_movers, SORT(enhanced_data, 6, -1),       // By daily usage rate
   slow_movers, SORT(FILTER(enhanced_data, days_of_supply > 90), 7, -1),  // Excess inventory
   
   // Create ABC classification with sorting
   abc_analysis, SORT(HSTACK(
     enhanced_data[Product],
     value_concentration,
     MAP(value_concentration, LAMBDA(value,
       LET(percentile_80, PERCENTILE(value_concentration, 0.8),
           percentile_95, PERCENTILE(value_concentration, 0.95),
           IF(value >= percentile_95, "A - Critical",
              IF(value >= percentile_80, "B - Important", "C - Standard")))))), 2, -1),
   
   // Generate procurement recommendations
   procurement_plan, SORT(FILTER(enhanced_data, 
     (reorder_priority > 0.5) + (days_of_supply < 30) > 0), 8, -1),
   
   recommended_orders, HSTACK(
     procurement_plan[Product],
     procurement_plan[Current_Stock],
     procurement_plan[Reorder_Point],
     MAP(procurement_plan, LAMBDA(row,
       MAX(0, INDEX(row, 4) - INDEX(row, 3)))),  // Recommended order quantity
     MAP(procurement_plan, LAMBDA(row,
       INDEX(row, 5) * MAX(0, INDEX(row, 4) - INDEX(row, 3))))),  // Order value
   
   // Final comprehensive inventory report
   inventory_report, VSTACK(
     HSTACK("=== INVENTORY MANAGEMENT DASHBOARD ===", "", "", "", ""),
     "",
     HSTACK("Critical Reorders (Top 10)", "", "High Value Items (Top 10)", "", "ABC Classification"),
     HSTACK(
       VSTACK("Product", critical_reorder[Product][ROWS<=10]),
       "",
       VSTACK("Product", high_value_items[Product][ROWS<=10]), 
       "",
       VSTACK("Category", abc_analysis[Classification][ROWS<=15])),
     "",
     HSTACK("=== PROCUREMENT RECOMMENDATIONS ===", "", "", "", ""),
     HSTACK("Product", "Current", "Reorder Point", "Order Qty", "Order Value"),
     recommended_orders),
   
   inventory_report)
```