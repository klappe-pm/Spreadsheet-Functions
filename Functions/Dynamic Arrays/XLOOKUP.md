---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: - dynamic-arrays
subTopics: []
dateCreated: 2025-08-17
dateRevised: 2025-08-17
aliases: []
tags: []
---

# XLOOKUP

## XLOOKUP Description

Modern lookup function that searches for a value in one array and returns a corresponding value from another array. Replaces VLOOKUP, HLOOKUP, INDEX/MATCH with more flexible functionality including exact/approximate matches, left-to-right or right-to-left searches, and better error handling.

> [!f(x)] XLOOKUP Syntax
>
> ```spreadsheets
> XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
> ```
>
> **Parameters:**
> - `lookup_value` (required): Value to search for
> - `lookup_array` (required): Array or range to search in
> - `return_array` (required): Array or range to return values from
> - `if_not_found` (optional): Value to return if no match found (default: #N/A error)
> - `match_mode` (optional): 0=exact match (default), -1=exact or next smallest, 1=exact or next largest, 2=wildcard match
> - `search_mode` (optional): 1=first to last (default), -1=last to first, 2=binary search ascending, -2=binary search descending

> [!f(x)] XLOOKUP Examples
>
> ```spreadsheets
> // Basic exact match lookup
> XLOOKUP("John", A1:A10, B1:B10) → finds "John" in A1:A10, returns corresponding B value
> 
> // Lookup with custom error message
> XLOOKUP("Product123", products, prices, "Not Found") → returns price or "Not Found"
> 
> // Approximate match for closest smaller value
> XLOOKUP(85, grade_cutoffs, letter_grades, , -1) → finds grade for score of 85
> 
> // Wildcard match using pattern
> XLOOKUP("Smi*", names, phone_numbers, , 2) → finds names starting with "Smi"
> 
> // Return multiple columns
> XLOOKUP("EMP001", employee_ids, employee_data) → returns entire row for employee
> ```

## Use Cases

### [[Data lookups]]
- **Customer information retrieval**: Look up customer details, purchase history, or contact information from customer databases using customer ID or name
- **Product catalog management**: Find product specifications, pricing, inventory levels, or supplier information based on product codes or descriptions
- **Employee records**: Retrieve employee data including salary, department, manager, or performance metrics using employee ID or name as lookup key
- **Financial data analysis**: Look up account balances, transaction details, exchange rates, or investment performance using account numbers or ticker symbols

### [[Report automation]]
- **Dynamic dashboard creation**: Automatically populate reports with current data by looking up the latest values from source databases or data feeds
- **Performance scorecards**: Create automated performance reports that pull key metrics and benchmarks based on department, region, or time period
- **Budget vs actual analysis**: Compare budget figures with actual spending by looking up corresponding values from different time periods or categories
- **Compliance reporting**: Generate regulatory reports by looking up required data points from operational systems based on compliance requirements

### [[Data validation]]
- **Reference data checking**: Validate transaction codes, account numbers, or product IDs against master reference tables to ensure data integrity
- **Price verification**: Cross-reference quoted prices with standard price lists or contract terms to identify discrepancies or exceptions
- **Inventory reconciliation**: Verify stock levels across different systems by comparing warehouse data with accounting records
- **Quality control**: Check product specifications or test results against established standards to identify items requiring attention

## Related

### Similar Functions

- [[VLOOKUP]] - Vertical lookup function, predecessor to XLOOKUP with more limitations
- [[HLOOKUP]] - Horizontal lookup function for row-based searches, less flexible than XLOOKUP  
- [[INDEX]] - Returns value at specific position, often combined with MATCH
- [[MATCH]] - Finds position of lookup value, typically paired with INDEX
- [[FILTER]] - Returns multiple matching records instead of first match only

## Lookup Enhancement Functions

### [[INDEX]]
Often combined with XLOOKUP for complex multi-dimensional lookups where XLOOKUP provides the row and INDEX provides the column selection.

```spreadsheets
// Two-dimensional lookup with XLOOKUP and INDEX
=INDEX(data_table, XLOOKUP(row_key, row_headers, SEQUENCE(ROWS(row_headers))), 
       XLOOKUP(col_key, col_headers, SEQUENCE(COLUMNS(col_headers))))
// Finds intersection of specific row and column in data table

// Dynamic column selection with XLOOKUP
=INDEX(XLOOKUP(employee_id, emp_ids, emp_data), 1, column_number)
// Gets specific column from employee record found by XLOOKUP

// Multi-criteria lookup using INDEX with XLOOKUP array result
=INDEX(XLOOKUP(criteria1&criteria2, lookup1&lookup2, return_array), position)
// Combines multiple criteria for lookup, then selects specific position from result
```

### [[MATCH]]
Pairs with XLOOKUP to determine positions and create more sophisticated lookup logic, especially for ranking and positional analysis.

```spreadsheets
// Find position of XLOOKUP result in another array
=MATCH(XLOOKUP(lookup_val, lookup_arr, return_arr), ranking_array, 0)
// Determines where the looked-up value ranks in a different list

// Use MATCH to validate XLOOKUP search scope
=IF(MATCH(lookup_value, lookup_array, 0) > 0, 
    XLOOKUP(lookup_value, lookup_array, return_array), "Not in scope")
// Ensures lookup value exists before attempting XLOOKUP

// Position-based validation with XLOOKUP and MATCH
=XLOOKUP(lookup_val, lookup_arr, return_arr) & " (Position: " & 
 MATCH(lookup_val, lookup_arr, 0) & ")"
// Returns both the lookup result and its position
```

## Data Processing Functions

### [[FILTER]]
Complements XLOOKUP by returning all matching records instead of just the first match, enabling comprehensive data extraction.

```spreadsheets
// Use XLOOKUP for single match, FILTER for all matches
=IF(return_all, FILTER(data_range, lookup_column=lookup_value), 
    XLOOKUP(lookup_value, lookup_column, return_column))
// Conditional logic to return single match or all matches

// Combine XLOOKUP categories with FILTER details
=FILTER(transaction_data, transaction_data[Category] = 
    XLOOKUP(account_id, accounts[ID], accounts[Category]))
// Filter transactions by category found through account lookup

// Multi-step lookup and filter process
=FILTER(product_data, product_data[Supplier] = 
    XLOOKUP(region_code, regions[Code], regions[Preferred_Supplier]))
// Filter products by supplier determined from region lookup
```

### [[UNIQUE]]
Works with XLOOKUP to create clean lookup tables and eliminate duplicate results from lookup operations.

```spreadsheets
// Create unique lookup reference from XLOOKUP results
=UNIQUE(XLOOKUP(category_list, products[Category], products[Supplier]))
// Gets unique list of suppliers for each product category

// Build dynamic dropdown lists with XLOOKUP and UNIQUE
=UNIQUE(XLOOKUP(selected_region, regions[Name], regions[Countries]))
// Creates list of unique countries for selected region

// Combine multiple XLOOKUP results and get unique values
=UNIQUE(VSTACK(
    XLOOKUP(criteria1, lookup1, return1),
    XLOOKUP(criteria2, lookup2, return2),
    XLOOKUP(criteria3, lookup3, return3)))
// Merges multiple lookup results and removes duplicates
```

## Error Handling Functions

### [[IFERROR]]
Essential with XLOOKUP for graceful error handling when lookup values might not exist or lookup arrays might be empty.

```spreadsheets
// Graceful error handling with custom messages
=IFERROR(XLOOKUP(customer_id, customers[ID], customers[Name]), 
         "Customer " & customer_id & " not found")
// Provides informative error message instead of #N/A

// Cascading lookup with error handling
=IFERROR(XLOOKUP(primary_key, primary_table, return_col),
         IFERROR(XLOOKUP(primary_key, backup_table, return_col), "No data available"))
// Tries primary lookup, falls back to backup, then error message

// Validation before lookup with IFERROR
=IFERROR(IF(lookup_value="", "Please enter lookup value", 
            XLOOKUP(lookup_value, lookup_array, return_array)), "Lookup failed")
// Validates input before attempting lookup
```

### [[ISNA]]
Works with XLOOKUP to detect missing values and implement custom logic for handling lookup failures.

```spreadsheets
// Custom logic based on lookup success/failure
=IF(ISNA(XLOOKUP(item_code, inventory[Code], inventory[Stock])),
    "Item not in inventory - check code",
    "Stock: " & XLOOKUP(item_code, inventory[Code], inventory[Stock]))
// Different actions based on whether lookup succeeds

// Count successful vs failed lookups
=SUMPRODUCT(--(ISNA(XLOOKUP(lookup_list, reference_table[Key], reference_table[Value]))))
// Counts how many lookups failed in a list

// Create status indicators for lookups
=MAP(lookup_values, LAMBDA(val, 
    IF(ISNA(XLOOKUP(val, master_list, master_list)), "Missing", "Found")))
// Shows which lookup values are found vs missing
```

## Commonly Used With Functions Examples

### Comprehensive Customer Relationship Management System
```spreadsheets
// Build a complete customer analysis system with multiple lookups
=LAMBDA(customer_identifier, analysis_date,
   LET(
     // Primary customer lookup
     customer_record, XLOOKUP(customer_identifier, customers[ID], customers),
     customer_name, INDEX(customer_record, 1, 2),
     customer_segment, INDEX(customer_record, 1, 5),
     
     // Purchase history analysis
     purchase_history, FILTER(transactions, 
       (transactions[Customer_ID] = customer_identifier) * 
       (transactions[Date] >= analysis_date - 365)),
     
     total_purchases, SUM(purchase_history[Amount]),
     purchase_count, ROWS(purchase_history),
     avg_purchase, total_purchases / purchase_count,
     
     // Product preference analysis
     product_purchases, GROUPBY(purchase_history[Product_ID], purchase_history[Amount], SUM),
     top_product_id, INDEX(SORT(product_purchases, 2, -1), 1, 1),
     top_product_name, XLOOKUP(top_product_id, products[ID], products[Name]),
     
     // Segment benchmarking
     segment_peers, FILTER(customers, customers[Segment] = customer_segment),
     segment_avg_spend, AVERAGE(
       MAP(segment_peers[ID], LAMBDA(id, 
         SUM(FILTER(transactions[Amount], transactions[Customer_ID] = id))))),
     
     // Loyalty status determination
     loyalty_tier, XLOOKUP(total_purchases, loyalty_thresholds[Min_Spend], 
       loyalty_thresholds[Tier], "Bronze", 1),
     
     // Next best action recommendation
     recommended_products, XLOOKUP(customer_segment, 
       segment_recommendations[Segment], segment_recommendations[Products]),
     
     // Comprehensive customer profile
     customer_profile, VSTACK(
       HSTACK("Customer Analysis Report", "", "", ""),
       HSTACK("Customer Name:", customer_name, "Segment:", customer_segment),
       HSTACK("Total Purchases:", TEXT(total_purchases, "$#,##0"), "Purchase Count:", purchase_count),
       HSTACK("Average Purchase:", TEXT(avg_purchase, "$#,##0"), "Loyalty Tier:", loyalty_tier),
       HSTACK("Top Product:", top_product_name, "Segment Avg:", TEXT(segment_avg_spend, "$#,##0")),
       "",
       HSTACK("Recommended Products:", "", "", ""),
       recommended_products),
     
     customer_profile))
```

### Advanced Financial Reporting and Analysis System  
```spreadsheets
// Create sophisticated financial analysis with multiple data sources
=LET(
   reporting_period, DATE(2024, 12, 31),
   
   // Account classification and details
   chart_of_accounts, account_master,
   account_classifications, MAP(chart_of_accounts[Account_Code], LAMBDA(code,
     XLOOKUP(LEFT(code, 1), account_types[Type_Code], account_types[Classification]))),
   
   // Trial balance with account details
   trial_balance_raw, general_ledger,
   account_balances, GROUPBY(trial_balance_raw[Account], trial_balance_raw[Amount], SUM),
   
   enhanced_trial_balance, HSTACK(
     account_balances[Account],
     account_balances[Amount],
     MAP(account_balances[Account], LAMBDA(acc,
       XLOOKUP(acc, chart_of_accounts[Account_Code], chart_of_accounts[Account_Name]))),
     MAP(account_balances[Account], LAMBDA(acc,
       XLOOKUP(LEFT(acc, 1), account_types[Type_Code], account_types[Classification]))),
     MAP(account_balances[Account], LAMBDA(acc,
       XLOOKUP(LEFT(acc, 1), account_types[Type_Code], account_types[Statement_Section])))),
   
   // Financial statement preparation
   revenue_accounts, FILTER(enhanced_trial_balance, 
     INDEX(enhanced_trial_balance, 0, 4) = "Revenue"),
   expense_accounts, FILTER(enhanced_trial_balance,
     INDEX(enhanced_trial_balance, 0, 4) = "Expense"),
   asset_accounts, FILTER(enhanced_trial_balance,
     INDEX(enhanced_trial_balance, 0, 4) = "Asset"),
   liability_accounts, FILTER(enhanced_trial_balance,
     INDEX(enhanced_trial_balance, 0, 4) = "Liability"),
   equity_accounts, FILTER(enhanced_trial_balance,
     INDEX(enhanced_trial_balance, 0, 4) = "Equity"),
   
   // Key financial metrics calculation
   total_revenue, SUM(revenue_accounts[Amount]),
   total_expenses, SUM(expense_accounts[Amount]),
   net_income, total_revenue + total_expenses,  // Expenses are negative
   total_assets, SUM(asset_accounts[Amount]),
   total_liabilities, SUM(liability_accounts[Amount]),
   
   // Industry benchmarking
   industry_code, XLOOKUP(company_id, company_master[ID], company_master[Industry]),
   industry_benchmarks, XLOOKUP(industry_code, benchmark_data[Industry], benchmark_data),
   
   revenue_vs_benchmark, total_revenue / INDEX(industry_benchmarks, 1, 2),
   margin_vs_benchmark, (net_income/total_revenue) / INDEX(industry_benchmarks, 1, 3),
   
   // Final financial dashboard
   financial_report, VSTACK(
     HSTACK("=== FINANCIAL ANALYSIS DASHBOARD ===", "", "", ""),
     HSTACK("Reporting Period:", TEXT(reporting_period, "yyyy-mm-dd"), "", ""),
     "",
     HSTACK("Income Statement Summary", "", "", ""),
     HSTACK("Total Revenue:", TEXT(total_revenue, "$#,##0,K"), "vs Industry:", TEXT(revenue_vs_benchmark, "0.0x")),
     HSTACK("Total Expenses:", TEXT(total_expenses, "$#,##0,K"), "Net Margin:", TEXT(net_income/total_revenue, "0.0%")),
     HSTACK("Net Income:", TEXT(net_income, "$#,##0,K"), "vs Industry:", TEXT(margin_vs_benchmark, "0.0x")),
     "",
     HSTACK("Balance Sheet Summary", "", "", ""),
     HSTACK("Total Assets:", TEXT(total_assets, "$#,##0,K"), "Total Liabilities:", TEXT(total_liabilities, "$#,##0,K")),
     HSTACK("Equity:", TEXT(total_assets - total_liabilities, "$#,##0,K"), "Debt Ratio:", TEXT(total_liabilities/total_assets, "0.0%")),
     "",
     HSTACK("Top Revenue Accounts", "Top Expense Accounts", "", ""),
     HSTACK(
       VSTACK("Account", SORT(revenue_accounts, 2, -1)[Account_Name][ROWS<=5]),
       VSTACK("Account", SORT(expense_accounts, 2, 1)[Account_Name][ROWS<=5]), "", "")),
   
   financial_report)
```

### Multi-Dimensional Inventory Management System
```spreadsheets
// Comprehensive inventory analysis with cross-referencing multiple data sources
=LET(
   analysis_date, TODAY(),
   
   // Base inventory data with enhanced information
   inventory_base, current_inventory,
   enhanced_inventory, MAP(inventory_base[Product_Code], LAMBDA(code,
     LET(
       product_info, XLOOKUP(code, product_master[Code], product_master),
       supplier_info, XLOOKUP(INDEX(product_info, 1, 4), supplier_master[ID], supplier_master),
       category_info, XLOOKUP(INDEX(product_info, 1, 3), category_master[ID], category_master),
       
       HSTACK(
         code,
         INDEX(product_info, 1, 2),  // Product Name
         INDEX(category_info, 1, 2),  // Category Name
         INDEX(supplier_info, 1, 2),  // Supplier Name
         XLOOKUP(code, inventory_base[Product_Code], inventory_base[Current_Stock]),
         XLOOKUP(code, inventory_base[Product_Code], inventory_base[Reorder_Point]),
         INDEX(product_info, 1, 5),  // Unit Cost
         INDEX(supplier_info, 1, 4)  // Lead Time
       )))),
   
   // Sales velocity analysis
   recent_sales, FILTER(sales_history, sales_history[Date] >= analysis_date - 90),
   velocity_analysis, GROUPBY(recent_sales[Product_Code], recent_sales[Quantity], SUM),
   daily_velocity, MAP(velocity_analysis, LAMBDA(row, 
     HSTACK(INDEX(row, 1, 1), INDEX(row, 1, 2) / 90))),  // Daily average
   
   // Combine inventory with sales velocity
   complete_analysis, MAP(enhanced_inventory, LAMBDA(inv_row,
     LET(
       product_code, INDEX(inv_row, 1, 1),
       daily_sales, XLOOKUP(product_code, daily_velocity[Product], daily_velocity[Daily_Avg], 0),
       days_of_supply, IF(daily_sales > 0, INDEX(inv_row, 1, 5) / daily_sales, 999),
       reorder_status, IF(INDEX(inv_row, 1, 5) <= INDEX(inv_row, 1, 6), "REORDER NEEDED", 
                          IF(days_of_supply < 30, "LOW STOCK", "OK")),
       
       HSTACK(inv_row, daily_sales, days_of_supply, reorder_status)))),
   
   // ABC Analysis based on sales value
   abc_analysis, LET(
     sales_value, MAP(complete_analysis, LAMBDA(row, 
       INDEX(row, 1, 7) * INDEX(row, 1, 9))),  // Cost * Daily Sales
     sorted_by_value, SORT(HSTACK(complete_analysis, sales_value), 11, -1),
     total_value, SUM(sales_value),
     running_pct, SCAN(0, sorted_by_value[Sales_Value], LAMBDA(acc, val, (acc + val) / total_value)),
     
     HSTACK(sorted_by_value, running_pct,
            MAP(running_pct, LAMBDA(pct,
              IF(pct <= 0.8, "A - High Value", 
                 IF(pct <= 0.95, "B - Medium Value", "C - Low Value")))))),
   
   // Critical actions summary
   reorder_needed, FILTER(abc_analysis, INDEX(abc_analysis, 0, 10) = "REORDER NEEDED"),
   low_stock_items, FILTER(abc_analysis, INDEX(abc_analysis, 0, 10) = "LOW STOCK"),
   overstocked_items, FILTER(abc_analysis, INDEX(abc_analysis, 0, 9) > 180),  // >6 months supply
   
   // Final comprehensive report
   inventory_report, VSTACK(
     HSTACK("=== INVENTORY MANAGEMENT DASHBOARD ===", "", "", "", "", "", "", ""),
     HSTACK("Analysis Date:", TEXT(analysis_date, "yyyy-mm-dd"), "Total SKUs:", ROWS(abc_analysis), "", "", "", ""),
     "",
     HSTACK("CRITICAL ACTIONS REQUIRED", "", "", "", "", "", "", ""),
     HSTACK("Reorder Needed:", ROWS(reorder_needed), "Low Stock:", ROWS(low_stock_items), "Overstocked:", ROWS(overstocked_items), "", "", ""),
     "",
     HSTACK("TOP REORDER PRIORITIES", "", "", "", "", "", "", ""),
     HSTACK("Product", "Category", "Supplier", "Stock", "Daily Sales", "Days Supply", "Lead Time", "ABC"),
     SORT(reorder_needed, 9, 1)[ROWS<=10][{1,3,4,5,9,9,8,12}],
     "",
     HSTACK("ABC ANALYSIS SUMMARY", "", "", "", "", "", "", ""),
     HSTACK("Category", "Count", "% of Total", "Value %", "", "", "", ""),
     GROUPBY(abc_analysis[ABC_Category], abc_analysis[ABC_Category], COUNTA)),
   
   inventory_report)
```