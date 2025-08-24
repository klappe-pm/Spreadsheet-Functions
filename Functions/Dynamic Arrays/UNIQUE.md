---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- dynamic-arrays
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- dynamic arrays
- excel
- sheets
---
# UNIQUE

## UNIQUE Description

Returns unique values from a range or array by removing duplicates. Supports both extracting unique values that appear once and distinct values that appear at least once, with options to compare by columns or rows for comprehensive data deduplication.

> [!f(x)] UNIQUE Syntax
>
> ```spreadsheets
> UNIQUE(array, [by_col], [occurs_once])
> ```
>
> **Parameters:**
> - `array` (required): The range or array to extract unique values from
> - `by_col` (optional): TRUE to compare by columns, FALSE to compare by rows (default: FALSE)
> - `occurs_once` (optional): TRUE to return values that appear exactly once, FALSE to return distinct values (default: FALSE)

> [!f(x)] UNIQUE Examples
>
> ```spreadsheets
> // Basic unique values extraction
> UNIQUE(A1:A10) → removes duplicate values from A1:A10
> 
> // Get values that appear only once
> UNIQUE(customer_list, , TRUE) → returns customers mentioned exactly once
> 
> // Unique rows from multi-column data
> UNIQUE(A1:C10) → returns unique combinations across all three columns
> 
> // Unique names from list
> UNIQUE({"John"; "Mary"; "John"; "Bob"; "Mary"}) → {"John"; "Mary"; "Bob"}
> 
> // Extract unique product categories
> UNIQUE(product_data[Category]) → distinct categories without duplicates
> ```

## Use Cases

### [[Data cleaning]]
- **Remove duplicate records**: Clean customer databases, inventory lists, or transaction records by eliminating duplicate entries based on single or multiple column criteria
- **Consolidate mailing lists**: Merge multiple contact lists while ensuring no duplicate email addresses or customer entries for marketing campaigns
- **Standardize reference data**: Create clean master lists of products, departments, locations, or categories from various data sources with inconsistent entries
- **Quality assurance**: Identify and remove duplicate test results, survey responses, or data collection entries to ensure data integrity for analysis

### [[List creation]]
- **Dynamic dropdown lists**: Generate automatically updating dropdown lists for data validation containing only unique values from source data
- **Category extraction**: Create lists of unique product categories, customer segments, geographic regions, or classification codes for reporting and filtering
- **Reference table building**: Build lookup tables with unique keys for VLOOKUP, XLOOKUP, or other reference operations without duplicate key conflicts
- **Menu and selection lists**: Generate unique option lists for user interfaces, forms, or dashboard controls that reflect current data without redundancy

### [[Data analysis]]
- **Distinct count analysis**: Identify the number of unique customers, products, transactions, or other entities for statistical analysis and reporting
- **Segmentation studies**: Extract unique combinations of attributes to understand customer segments, market categories, or behavioral patterns
- **Data profiling**: Analyze data quality by examining unique values, identifying patterns, and detecting anomalies or inconsistencies in datasets
- **Frequency analysis preparation**: Create unique value lists as the foundation for counting occurrences and building frequency distributions

## Related

### Similar Functions

- [[FILTER]] - Extracts data meeting criteria, often combined with UNIQUE for filtered unique results
- [[SORT]] - Sorts arrays, frequently paired with UNIQUE to create ordered unique lists
- [[COUNTUNIQUE]] - Counts unique values without extracting them (Google Sheets function)
- [[REMOVEDUPS]] - Similar concept in older Excel versions, less flexible than UNIQUE
- [[DISTINCT]] - SQL equivalent for unique value extraction in database contexts

## Data Cleaning Functions

### [[FILTER]]
Frequently combined with UNIQUE to extract unique values that also meet specific criteria, creating filtered unique lists for targeted analysis.

```spreadsheets
// Unique customers from specific region
=UNIQUE(FILTER(customer_data[Name], customer_data[Region]="West"))
// Returns unique customers from West region only

// Unique high-value transactions
=UNIQUE(FILTER(transactions[Customer_ID], transactions[Amount]>=1000))
// Unique customers with transactions over $1000

// Unique products sold this month
=UNIQUE(FILTER(sales_data[Product], 
  MONTH(sales_data[Date])=MONTH(TODAY())))
// Products sold in current month, no duplicates
```

### [[SORT]]
Often paired with UNIQUE to create organized, duplicate-free lists that are easy to read and use in reports or dropdown menus.

```spreadsheets
// Alphabetically sorted unique names
=SORT(UNIQUE(employee_list[Name]))
// Unique employee names in alphabetical order

// Unique product categories by value
=SORT(UNIQUE(product_data[Category]), 
      MAP(UNIQUE(product_data[Category]), 
          LAMBDA(cat, SUM(FILTER(product_data[Value], 
                                product_data[Category]=cat)))), -1)
// Categories sorted by total value descending

// Chronologically sorted unique dates
=SORT(UNIQUE(transaction_dates))
// Unique transaction dates in chronological order
```

## Statistical Analysis Functions

### [[COUNTIFS]]
Works with UNIQUE to perform frequency analysis on unique values, counting occurrences and building comprehensive statistical summaries.

```spreadsheets
// Frequency analysis of unique values
=LET(unique_values, UNIQUE(data_range),
     frequencies, MAP(unique_values, LAMBDA(val, COUNTIFS(data_range, val))),
     HSTACK(unique_values, frequencies))
// Shows each unique value with its frequency count

// Customer purchase frequency analysis
=LET(unique_customers, UNIQUE(orders[Customer_ID]),
     purchase_counts, MAP(unique_customers, LAMBDA(cust,
       COUNTIFS(orders[Customer_ID], cust))),
     avg_order_values, MAP(unique_customers, LAMBDA(cust,
       AVERAGE(FILTER(orders[Amount], orders[Customer_ID]=cust)))),
     HSTACK(unique_customers, purchase_counts, avg_order_values))
// Customer analysis with purchase frequency and average order value

// Product performance by unique categories
=LET(unique_categories, UNIQUE(products[Category]),
     category_counts, MAP(unique_categories, LAMBDA(cat,
       COUNTIFS(products[Category], cat))),
     category_sales, MAP(unique_categories, LAMBDA(cat,
       SUM(FILTER(sales[Amount], 
                  XLOOKUP(sales[Product_ID], products[ID], products[Category])=cat)))),
     HSTACK(unique_categories, category_counts, category_sales))
// Analysis by unique product categories
```

### [[SUMIFS]]
Combines with UNIQUE to create aggregated summaries for each unique value, enabling comprehensive analysis across unique categories or segments.

```spreadsheets
// Revenue by unique sales rep
=LET(unique_reps, UNIQUE(sales_data[Sales_Rep]),
     rep_revenues, MAP(unique_reps, LAMBDA(rep,
       SUMIFS(sales_data[Revenue], sales_data[Sales_Rep], rep))),
     HSTACK(unique_reps, rep_revenues))
// Total revenue for each unique sales representative

// Monthly sales by unique product
=LET(unique_products, UNIQUE(monthly_sales[Product]),
     monthly_totals, MAP(unique_products, LAMBDA(prod,
       SUMIFS(monthly_sales[Amount], monthly_sales[Product], prod))),
     units_sold, MAP(unique_products, LAMBDA(prod,
       SUMIFS(monthly_sales[Quantity], monthly_sales[Product], prod))),
     HSTACK(unique_products, monthly_totals, units_sold))
// Product performance summary with revenue and units

// Geographic sales analysis
=LET(unique_regions, UNIQUE(customer_data[Region]),
     region_sales, MAP(unique_regions, LAMBDA(region,
       SUMIFS(sales_data[Amount], 
              XLOOKUP(sales_data[Customer_ID], customer_data[ID], customer_data[Region]), 
              region))),
     customer_counts, MAP(unique_regions, LAMBDA(region,
       COUNTIFS(customer_data[Region], region))),
     HSTACK(unique_regions, region_sales, customer_counts))
// Sales and customer count by unique regions
```

## Data Validation Functions

### [[INDEX]]
Uses UNIQUE to create dynamic reference lists and extract specific unique values based on position or criteria for validation and lookup purposes.

```spreadsheets
// Dynamic dropdown with unique values
=INDEX(UNIQUE(SORT(product_categories)), dropdown_selection)
// Returns specific unique category based on user selection

// Extract nth unique customer
=INDEX(UNIQUE(SORT(customer_list)), customer_position)
// Gets unique customer at specified position

// First unique value meeting criteria
=INDEX(UNIQUE(FILTER(data_range, criteria_range=criteria)), 1)
// Returns first unique value that meets the specified criteria
```

### [[MATCH]]
Pairs with UNIQUE to find positions of specific values within unique lists, enabling validation and position-based logic.

```spreadsheets
// Validate if value exists in unique list
=IF(ISNUMBER(MATCH(lookup_value, UNIQUE(reference_list), 0)), 
    "Valid", "Invalid")
// Checks if lookup value exists in unique reference list

// Position of value in unique sorted list
=MATCH(search_value, UNIQUE(SORT(data_array)), 0)
// Finds position of value in alphabetically sorted unique list

// Create ranking within unique values
=MAP(data_values, LAMBDA(val,
    MATCH(val, UNIQUE(SORT(data_values, , -1)), 0)))
// Ranks each value within the unique value set
```

## Commonly Used With Functions Examples

### Dynamic Data Validation System
```spreadsheets
// Create a comprehensive cascading dropdown system
=LET(
   all_data, product_master,
   
   // Level 1: Unique categories
   unique_categories, SORT(UNIQUE(all_data[Category])),
   selected_category, category_dropdown_value,
   
   // Level 2: Unique subcategories for selected category
   filtered_by_category, FILTER(all_data, all_data[Category] = selected_category),
   unique_subcategories, SORT(UNIQUE(filtered_by_category[Subcategory])),
   selected_subcategory, subcategory_dropdown_value,
   
   // Level 3: Unique brands for selected category and subcategory
   filtered_by_subcat, FILTER(filtered_by_category, 
     filtered_by_category[Subcategory] = selected_subcategory),
   unique_brands, SORT(UNIQUE(filtered_by_subcat[Brand])),
   selected_brand, brand_dropdown_value,
   
   // Final filtered unique products
   final_filtered, FILTER(filtered_by_subcat, filtered_by_subcat[Brand] = selected_brand),
   unique_products, SORT(UNIQUE(final_filtered[Product_Name])),
   
   // Create validation lists for each level
   validation_ranges, VSTACK(
     HSTACK("Category Options:", TRANSPOSE(unique_categories)),
     HSTACK("Subcategory Options:", TRANSPOSE(unique_subcategories)),
     HSTACK("Brand Options:", TRANSPOSE(unique_brands)),
     HSTACK("Product Options:", TRANSPOSE(unique_products))),
   
   validation_ranges)
```

### Customer Segmentation and Analysis Engine
```spreadsheets
// Build comprehensive customer analysis using unique segmentation
=LET(
   customer_transactions, transaction_history,
   
   // Create unique customer analysis
   unique_customers, UNIQUE(customer_transactions[Customer_ID]),
   
   customer_profiles, MAP(unique_customers, LAMBDA(cust_id,
     LET(
       customer_data, FILTER(customer_transactions, 
         customer_transactions[Customer_ID] = cust_id),
       
       total_spent, SUM(customer_data[Amount]),
       transaction_count, ROWS(customer_data),
       avg_transaction, total_spent / transaction_count,
       first_purchase, MIN(customer_data[Date]),
       last_purchase, MAX(customer_data[Date]),
       customer_lifetime, last_purchase - first_purchase + 1,
       
       // Unique products purchased by this customer
       unique_products, UNIQUE(customer_data[Product_ID]),
       product_diversity, ROWS(unique_products),
       
       // Unique categories purchased
       product_categories, MAP(unique_products, LAMBDA(prod_id,
         XLOOKUP(prod_id, product_master[ID], product_master[Category]))),
       unique_categories, UNIQUE(product_categories),
       category_diversity, ROWS(unique_categories),
       
       HSTACK(cust_id, total_spent, transaction_count, avg_transaction,
              customer_lifetime, product_diversity, category_diversity)))),
   
   // Customer segmentation based on behavior
   spending_segments, MAP(customer_profiles, LAMBDA(profile,
     LET(total_spent, INDEX(profile, 1, 2),
         transaction_count, INDEX(profile, 1, 3),
         segment, IF(total_spent >= 5000, 
                    IF(transaction_count >= 20, "VIP Frequent", "VIP Occasional"),
                    IF(total_spent >= 1000,
                       IF(transaction_count >= 15, "Regular Frequent", "Regular Occasional"),
                       IF(transaction_count >= 10, "Budget Frequent", "Budget Occasional"))),
         HSTACK(profile, segment)))),
   
   // Unique segment analysis
   unique_segments, UNIQUE(spending_segments[Segment]),
   segment_summary, MAP(unique_segments, LAMBDA(segment,
     LET(segment_customers, FILTER(spending_segments, 
           spending_segments[Segment] = segment),
         customer_count, ROWS(segment_customers),
         avg_spent, AVERAGE(segment_customers[Total_Spent]),
         avg_transactions, AVERAGE(segment_customers[Transaction_Count]),
         avg_product_diversity, AVERAGE(segment_customers[Product_Diversity]),
         
         HSTACK(segment, customer_count, avg_spent, avg_transactions, 
                avg_product_diversity)))),
   
   // Final comprehensive report
   customer_analysis, VSTACK(
     HSTACK("=== CUSTOMER SEGMENTATION ANALYSIS ===", "", "", "", ""),
     HSTACK("Total Unique Customers:", ROWS(unique_customers), "", "", ""),
     HSTACK("Unique Segments:", ROWS(unique_segments), "", "", ""),
     "",
     HSTACK("Segment", "Customer Count", "Avg Spent", "Avg Transactions", "Avg Product Diversity"),
     segment_summary,
     "",
     HSTACK("=== TOP CUSTOMERS BY SEGMENT ===", "", "", "", ""),
     MAP(unique_segments, LAMBDA(seg,
       LET(seg_customers, FILTER(spending_segments, 
             spending_segments[Segment] = seg),
           top_customers, SORT(seg_customers, 2, -1)[ROWS<=3],
           VSTACK(
             HSTACK(seg & " - Top 3 Customers:", "", "", "", ""),
             HSTACK("Customer ID", "Total Spent", "Transactions", "Avg Transaction", ""),
             top_customers[{1,2,3,4}]))))),
   
   customer_analysis)
```

### Advanced Inventory Optimization System
```spreadsheets
// Create sophisticated inventory analysis using unique categorization
=LET(
   inventory_base, current_inventory,
   sales_history, transaction_data,
   
   // Unique product analysis
   unique_products, UNIQUE(inventory_base[Product_ID]),
   
   product_analysis, MAP(unique_products, LAMBDA(prod_id,
     LET(
       // Basic inventory info
       current_stock, XLOOKUP(prod_id, inventory_base[Product_ID], inventory_base[Stock]),
       reorder_point, XLOOKUP(prod_id, inventory_base[Product_ID], inventory_base[Reorder_Point]),
       unit_cost, XLOOKUP(prod_id, inventory_base[Product_ID], inventory_base[Unit_Cost]),
       
       // Sales analysis for this product
       product_sales, FILTER(sales_history, sales_history[Product_ID] = prod_id),
       sales_last_90_days, FILTER(product_sales, product_sales[Date] >= TODAY()-90),
       
       total_sold_90d, SUM(sales_last_90_days[Quantity]),
       daily_velocity, total_sold_90d / 90,
       days_of_supply, IF(daily_velocity > 0, current_stock / daily_velocity, 999),
       
       // Unique customers who bought this product
       product_customers, UNIQUE(product_sales[Customer_ID]),
       customer_breadth, ROWS(product_customers),
       
       // Revenue metrics
       total_revenue_90d, SUM(sales_last_90_days[Revenue]),
       avg_selling_price, IF(total_sold_90d > 0, total_revenue_90d / total_sold_90d, 0),
       gross_margin, IF(avg_selling_price > 0, (avg_selling_price - unit_cost) / avg_selling_price, 0),
       
       HSTACK(prod_id, current_stock, reorder_point, daily_velocity, 
              days_of_supply, customer_breadth, gross_margin, total_revenue_90d)))),
   
   // Categorize products by performance
   performance_categories, MAP(product_analysis, LAMBDA(row,
     LET(daily_velocity, INDEX(row, 1, 4),
         days_supply, INDEX(row, 1, 5),
         customer_breadth, INDEX(row, 1, 6),
         gross_margin, INDEX(row, 1, 7),
         
         // Multi-dimensional categorization
         velocity_cat, IF(daily_velocity >= 5, "Fast Moving",
                          IF(daily_velocity >= 1, "Medium Moving", "Slow Moving")),
         inventory_cat, IF(days_supply <= 30, "Low Stock",
                           IF(days_supply <= 90, "Normal Stock", "Excess Stock")),
         customer_cat, IF(customer_breadth >= 20, "Broad Appeal",
                          IF(customer_breadth >= 5, "Moderate Appeal", "Niche Product")),
         margin_cat, IF(gross_margin >= 0.4, "High Margin",
                        IF(gross_margin >= 0.2, "Medium Margin", "Low Margin")),
         
         combined_category, velocity_cat & " | " & inventory_cat & " | " & 
                           customer_cat & " | " & margin_cat,
         
         HSTACK(row, combined_category)))),
   
   // Unique category combinations analysis
   unique_category_combinations, UNIQUE(performance_categories[Combined_Category]),
   category_analysis, MAP(unique_category_combinations, LAMBDA(category,
     LET(category_products, FILTER(performance_categories, 
           performance_categories[Combined_Category] = category),
         product_count, ROWS(category_products),
         total_inventory_value, SUM(category_products[Current_Stock] * 
                                  category_products[Unit_Cost]),
         total_revenue, SUM(category_products[Total_Revenue_90d]),
         avg_margin, AVERAGE(category_products[Gross_Margin]),
         
         HSTACK(category, product_count, total_inventory_value, 
                total_revenue, avg_margin)))),
   
   // Action recommendations by unique categories
   action_recommendations, MAP(unique_category_combinations, LAMBDA(category,
     LET(
       action, SWITCH(TRUE(),
         AND(ISNUMBER(SEARCH("Fast Moving", category)), 
             ISNUMBER(SEARCH("Low Stock", category))), "URGENT REORDER",
         AND(ISNUMBER(SEARCH("Slow Moving", category)), 
             ISNUMBER(SEARCH("Excess Stock", category))), "DISCOUNT/LIQUIDATE",
         AND(ISNUMBER(SEARCH("High Margin", category)), 
             ISNUMBER(SEARCH("Broad Appeal", category))), "PROMOTE/EXPAND",
         ISNUMBER(SEARCH("Low Stock", category)), "REORDER",
         ISNUMBER(SEARCH("Excess Stock", category)), "REDUCE ORDERS",
         "MONITOR"),
       
       HSTACK(category, action)))),
   
   // Final comprehensive inventory report
   inventory_dashboard, VSTACK(
     HSTACK("=== INVENTORY OPTIMIZATION DASHBOARD ===", "", "", "", ""),
     HSTACK("Total Unique Products:", ROWS(unique_products), "", "", ""),
     HSTACK("Unique Category Combinations:", ROWS(unique_category_combinations), "", "", ""),
     "",
     HSTACK("=== CATEGORY PERFORMANCE ANALYSIS ===", "", "", "", ""),
     HSTACK("Category", "Product Count", "Inventory Value", "90d Revenue", "Avg Margin"),
     SORT(category_analysis, 4, -1),
     "",
     HSTACK("=== RECOMMENDED ACTIONS ===", "", "", "", ""),
     HSTACK("Category", "Recommended Action", "", "", ""),
     action_recommendations),
   
   inventory_dashboard)
```