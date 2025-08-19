---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: excel
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# MAKEARRAY

## MAKEARRAY Description

Creates an array by applying a LAMBDA function to each cell position, enabling custom array generation with dynamic content based on row and column coordinates. Generates arrays where each element is calculated using custom logic rather than predetermined values.

> [!f(x)] MAKEARRAY Syntax
>
> ```spreadsheets
> MAKEARRAY(rows, cols, lambda)
> ```
>
> **Parameters:**
> - `rows` (required): Number of rows for the array
> - `cols` (required): Number of columns for the array 
> - `lambda` (required): LAMBDA function that takes (row, col) parameters and returns a value for each position

> [!f(x)] MAKEARRAY Examples
>
> ```spreadsheets
> // Create multiplication table
> MAKEARRAY(5, 5, LAMBDA(r, c, r * c)) → 5x5 multiplication table
> 
> // Generate coordinate grid
> MAKEARRAY(3, 3, LAMBDA(r, c, "(" & r & "," & c & ")")) → grid with coordinate labels
> 
> // Create random data array
> MAKEARRAY(10, 3, LAMBDA(r, c, RANDBETWEEN(1, 100))) → 10x3 array of random numbers
> 
> // Build date sequence array
> MAKEARRAY(7, 1, LAMBDA(r, c, DATE(2024, 1, 1) + r - 1)) → 7 sequential dates
> 
> // Generate pattern-based array
> MAKEARRAY(4, 4, LAMBDA(r, c, IF(r = c, 1, 0))) → identity matrix with 1s on diagonal
> ```

## Use Cases

### [[Mathematical operations]]
- **Matrix generation**: Create identity matrices, correlation matrices, or transformation matrices for linear algebra calculations and mathematical modeling
- **Coordinate systems**: Build coordinate grids, polar coordinate arrays, or spatial reference systems for geometric calculations and mapping applications
- **Pattern matrices**: Generate mathematical patterns like Pascal's triangle, Fibonacci sequences, or geometric progressions arranged in array format
- **Statistical arrays**: Create probability distribution tables, lookup matrices, or sampling arrays for statistical analysis and research

### [[Data simulation]]
- **Test data generation**: Create realistic test datasets with controlled patterns, relationships, and distributions for testing formulas and business logic
- **Monte Carlo simulations**: Generate arrays of random samples for risk analysis, financial modeling, or decision-making under uncertainty
- **Scenario analysis**: Build arrays representing different business scenarios, sensitivity parameters, or what-if analysis conditions
- **Performance testing**: Create large arrays with specific characteristics to test formula performance, memory usage, and calculation speed

### [[Custom calculations]]
- **Dynamic formulas**: Build arrays where each cell contains different formulas based on position, enabling complex calculation structures
- **Conditional arrays**: Create arrays with position-dependent logic, such as seasonal adjustments, regional variations, or time-based modifications
- **Lookup table generation**: Generate custom lookup tables with calculated values, interpolated data, or algorithmic transformations
- **Report templates**: Create structured report arrays with headers, formatting, and calculated fields based on array position

## Related

### Similar Functions

- [[SEQUENCE]] - Generates sequential number arrays, simpler than MAKEARRAY for basic patterns
- [[RANDARRAY]] - Creates arrays of random values, less control than MAKEARRAY with LAMBDA
- [[LAMBDA]] - Defines custom functions, essential component used within MAKEARRAY
- [[MAP]] - Applies functions to existing arrays, while MAKEARRAY creates new arrays from scratch
- [[REDUCE]] - Processes arrays iteratively, complementary to MAKEARRAY's creation capability

## Array Generation Functions

### [[SEQUENCE]]
Often combined with MAKEARRAY to provide incremental indices or coordinates for complex array generation patterns.

```spreadsheets
// Create array with sequential row and column indices
=MAKEARRAY(5, 5, LAMBDA(r, c, INDEX(SEQUENCE(5), r) + INDEX(SEQUENCE(5), c)))
// Each cell contains sum of its row and column numbers

// Generate date array with business day logic
=MAKEARRAY(20, 1, LAMBDA(r, c, WORKDAY(start_date, INDEX(SEQUENCE(20), r) - 1)))
// 20 consecutive business days using SEQUENCE for counting

// Build multiplication table with SEQUENCE
=MAKEARRAY(10, 10, LAMBDA(r, c, 
   INDEX(SEQUENCE(10), r) * INDEX(SEQUENCE(10), c)))
// Classic multiplication table using SEQUENCE for factors
```

### [[RANDARRAY]]
Pairs with MAKEARRAY to create controlled random arrays where randomness is applied selectively based on position or conditions.

```spreadsheets
// Random values with position-based constraints
=MAKEARRAY(10, 5, LAMBDA(r, c, 
   IF(c <= 2, INDEX(RANDARRAY(1, 1, 1, 100), 1, 1), 
      INDEX(RANDARRAY(1, 1, 1000, 10000), 1, 1))))
// First 2 columns: 1-100, remaining columns: 1000-10000

// Conditional randomness based on array position
=MAKEARRAY(8, 8, LAMBDA(r, c,
   IF(ABS(r - c) <= 1, INDEX(RANDARRAY(1, 1, 0.8, 1.2), 1, 1), 0)))
// Random values only near diagonal, zeros elsewhere

// Random data with realistic relationships
=MAKEARRAY(100, 3, LAMBDA(r, c,
   SWITCH(c, 
     1, INDEX(RANDARRAY(1, 1, 18, 65), 1, 1),  // Age
     2, INDEX(RANDARRAY(1, 1, 25000, 100000), 1, 1),  // Salary
     3, INDEX(RANDARRAY(1, 1, 1, 5), 1, 1))))  // Rating
// Structured random data with different ranges per column
```

## Mathematical Functions

### [[SUM]]
Uses MAKEARRAY to create summation arrays, running totals, or cumulative calculation structures across array positions.

```spreadsheets
// Create cumulative sum array
=MAKEARRAY(10, 1, LAMBDA(r, c, SUM(INDEX(SEQUENCE(r), 0, 1))))
// Each row contains sum of all numbers from 1 to current row

// Build compound interest array
=MAKEARRAY(20, 1, LAMBDA(r, c, 
   principal * (1 + annual_rate)^(r-1)))
// 20-year compound interest projection

// Generate running balance array
=MAKEARRAY(12, 1, LAMBDA(r, c,
   starting_balance + SUM(INDEX(monthly_changes, SEQUENCE(r), 1))))
// Monthly running balance with cumulative changes
```

### [[IF]]
Combines with MAKEARRAY to create conditional arrays where cell values depend on position-based logic or complex criteria.

```spreadsheets
// Create checkerboard pattern
=MAKEARRAY(8, 8, LAMBDA(r, c, IF(MOD(r + c, 2) = 0, "Black", "White")))
// Alternating pattern based on sum of row and column

// Conditional formatting array
=MAKEARRAY(5, 10, LAMBDA(r, c,
   IF(r = 1, "Header", 
      IF(c <= 3, "ID-" & ((r-2)*3 + c), 
         INDEX(RANDARRAY(1, 1, 100, 1000), 1, 1)))))
// Headers in first row, IDs in first 3 cols, random data elsewhere

// Risk assessment matrix
=MAKEARRAY(5, 5, LAMBDA(r, c,
   LET(impact, r, probability, c, risk_score, r * c,
       IF(risk_score >= 20, "High Risk",
          IF(risk_score >= 10, "Medium Risk", "Low Risk")))))
// Risk matrix based on impact (rows) and probability (columns)
```

## Text Processing Functions

### [[TEXT]]
Works with MAKEARRAY to create formatted arrays, labels, or structured text content based on array position and calculations.

```spreadsheets
// Create formatted financial projection
=MAKEARRAY(10, 4, LAMBDA(r, c,
   LET(year, 2024 + r - 1,
       base_amount, 100000,
       growth_rate, 0.05,
       amount, base_amount * (1 + growth_rate)^(r-1),
       SWITCH(c,
         1, TEXT(year, "0000"),
         2, TEXT(amount, "$#,##0"),
         3, TEXT(amount * 0.08, "$#,##0"),
         4, TEXT(amount * 1.08, "$#,##0")))))
// Year, Revenue, Tax, Total columns with proper formatting

// Generate product code array
=MAKEARRAY(5, 5, LAMBDA(r, c, 
   "PROD-" & TEXT(r, "00") & "-" & TEXT(c, "00")))
// Structured product codes based on row and column position

// Create address label array
=MAKEARRAY(3, 2, LAMBDA(r, c,
   TEXT(1000 + (r-1)*2 + c, "0000") & " Main St"))
// Sequential street addresses in array format
```

### [[CONCAT]]
Pairs with MAKEARRAY to build arrays of concatenated strings, labels, or identifiers with position-dependent content.

```spreadsheets
// Build employee ID array
=MAKEARRAY(10, 1, LAMBDA(r, c,
   CONCAT("EMP", TEXT(2024, "0000"), TEXT(r, "000"))))
// Employee IDs with year and sequential number

// Create product description array
=MAKEARRAY(4, 3, LAMBDA(r, c,
   CONCAT("Product ", CHAR(64 + r), "-", TEXT(c, "0"))))
// Product names like "Product A-1", "Product B-2", etc.

// Generate report headers
=MAKEARRAY(1, 5, LAMBDA(r, c,
   CONCAT("Q", TEXT(c, "0"), " ", TEXT(YEAR(TODAY()), "0000"))))
// Quarterly headers for current year
```

## Commonly Used With Functions Examples

### Advanced Financial Modeling Dashboard
```spreadsheets
// Create comprehensive financial projection model
=LET(
   projection_years, 10,
   base_revenue, 1000000,
   growth_scenarios, {0.03, 0.05, 0.08},  // Conservative, Base, Optimistic
   
   // Build scenario analysis array
   scenario_projections, MAKEARRAY(projection_years + 1, 4, LAMBDA(r, c,
     IF(r = 1,
        // Header row
        SWITCH(c, 1, "Year", 2, "Conservative", 3, "Base Case", 4, "Optimistic"),
        // Data rows
        SWITCH(c,
          1, 2023 + r,  // Year column
          2, base_revenue * (1 + INDEX(growth_scenarios, 1, 1))^(r-1),  // Conservative
          3, base_revenue * (1 + INDEX(growth_scenarios, 1, 2))^(r-1),  // Base
          4, base_revenue * (1 + INDEX(growth_scenarios, 1, 3))^(r-1))))), // Optimistic
   
   // Create sensitivity analysis grid
   sensitivity_grid, MAKEARRAY(6, 6, LAMBDA(r, c,
     IF(r = 1,
        // Header row with growth rates
        IF(c = 1, "Growth Rate", INDEX(growth_scenarios, 1, c-1)),
        // Data rows with different discount rates
        IF(c = 1,
           0.08 + (r-2) * 0.01,  // Discount rates from 8% to 12%
           // NPV calculations
           LET(growth_rate, INDEX(growth_scenarios, 1, c-1),
               discount_rate, 0.08 + (r-2) * 0.01,
               cash_flows, MAKEARRAY(projection_years, 1, LAMBDA(yr, col,
                 base_revenue * (1 + growth_rate)^yr)),
               npv, SUM(MAP(cash_flows, SEQUENCE(projection_years), 
                       LAMBDA(cf, yr, cf / (1 + discount_rate)^yr))),
               npv))))),
   
   // Risk analysis matrix
   risk_matrix, MAKEARRAY(5, 5, LAMBDA(r, c,
     LET(probability, r * 0.2,  // 20%, 40%, 60%, 80%, 100%
         impact, c * 0.2,       // 20%, 40%, 60%, 80%, 100%
         risk_score, probability * impact,
         risk_level, IF(risk_score >= 0.64, "Critical",
                        IF(risk_score >= 0.36, "High",
                           IF(risk_score >= 0.16, "Medium", "Low"))),
         TEXT(risk_score, "0.0%") & " - " & risk_level))),
   
   // Final comprehensive dashboard
   financial_dashboard, VSTACK(
     HSTACK("=== FINANCIAL PROJECTION DASHBOARD ===", "", "", ""),
     "",
     HSTACK("Revenue Projections by Scenario:", "", "", ""),
     scenario_projections,
     "",
     HSTACK("NPV Sensitivity Analysis:", "", "", ""),
     HSTACK("Discount Rate vs Growth Rate", "", "", ""),
     sensitivity_grid,
     "",
     HSTACK("Risk Assessment Matrix:", "", "", ""),
     HSTACK("Probability (rows) vs Impact (columns)", "", "", ""),
     risk_matrix),
   
   financial_dashboard)
```

### Dynamic Product Catalog Management System
```spreadsheets
// Generate comprehensive product catalog with categorization
=LET(
   categories, {"Electronics", "Clothing", "Books", "Home", "Sports"},
   subcategories_per_cat, 4,
   products_per_subcat, 5,
   
   // Create hierarchical product structure
   product_catalog, MAKEARRAY(
     ROWS(categories) * subcategories_per_cat * products_per_subcat + 1, 7,
     LAMBDA(r, c,
       IF(r = 1,
          // Header row
          SWITCH(c, 1, "Product ID", 2, "Category", 3, "Subcategory", 
                 4, "Product Name", 5, "Price", 6, "Stock", 7, "Supplier"),
          // Data rows
          LET(data_row, r - 1,
              cat_index, ROUNDUP(data_row / (subcategories_per_cat * products_per_subcat), 0),
              subcat_index, ROUNDUP(MOD(data_row - 1, subcategories_per_cat * products_per_subcat) / products_per_subcat, 0) + 1,
              prod_index, MOD(data_row - 1, products_per_subcat) + 1,
              
              category, INDEX(categories, cat_index, 1),
              
              SWITCH(c,
                1, CONCAT(LEFT(category, 3), TEXT(subcat_index, "00"), TEXT(prod_index, "00")),  // Product ID
                2, category,  // Category
                3, category & " Sub" & TEXT(subcat_index, "0"),  // Subcategory
                4, category & " Product " & TEXT(subcat_index, "0") & "." & TEXT(prod_index, "0"),  // Product Name
                5, ROUND(50 + (cat_index * 30) + (subcat_index * 10) + (prod_index * 5) + RANDBETWEEN(-20, 50), 2),  // Price
                6, RANDBETWEEN(0, 100),  // Stock
                7, "Supplier " & CHAR(64 + MOD(cat_index + subcat_index, 5) + 1)))))), // Supplier
   
   // Create pricing analysis array
   pricing_analysis, MAKEARRAY(ROWS(categories), 6, LAMBDA(r, c,
     LET(category, INDEX(categories, r, 1),
         cat_products, FILTER(product_catalog, 
           (product_catalog[Category] = category) * (ROW(product_catalog[Category]) > 1)),
         
         SWITCH(c,
           1, category,
           2, ROWS(cat_products),  // Product count
           3, AVERAGE(cat_products[Price]),  // Average price
           4, MIN(cat_products[Price]),  // Min price
           5, MAX(cat_products[Price]),  // Max price
           6, SUM(cat_products[Stock]))))),  // Total stock
   
   // Inventory status dashboard
   inventory_dashboard, MAKEARRAY(6, 8, LAMBDA(r, c,
     IF(r = 1,
        // Header row
        SWITCH(c, 1, "Status", 2, "Count", 3, "% of Total", 4, "Avg Price", 
               5, "Total Value", 6, "Reorder Needed", 7, "Overstocked", 8, "Action"),
        // Data rows with inventory analysis
        LET(stock_ranges, {"Out of Stock", "Low (1-10)", "Medium (11-50)", "High (51-100)", "Excess (100+)"},
            status, INDEX(stock_ranges, r-1, 1),
            
            // Filter products by stock level
            status_products, SWITCH(r-1,
              1, FILTER(product_catalog, (product_catalog[Stock] = 0) * (ROW(product_catalog[Stock]) > 1)),
              2, FILTER(product_catalog, (product_catalog[Stock] >= 1) * (product_catalog[Stock] <= 10) * (ROW(product_catalog[Stock]) > 1)),
              3, FILTER(product_catalog, (product_catalog[Stock] >= 11) * (product_catalog[Stock] <= 50) * (ROW(product_catalog[Stock]) > 1)),
              4, FILTER(product_catalog, (product_catalog[Stock] >= 51) * (product_catalog[Stock] <= 100) * (ROW(product_catalog[Stock]) > 1)),
              5, FILTER(product_catalog, (product_catalog[Stock] > 100) * (ROW(product_catalog[Stock]) > 1))),
            
            product_count, IF(ROWS(status_products) > 0, ROWS(status_products), 0),
            total_products, ROWS(product_catalog) - 1,
            
            SWITCH(c,
              1, status,
              2, product_count,
              3, TEXT(IF(total_products > 0, product_count / total_products, 0), "0.0%"),
              4, IF(product_count > 0, AVERAGE(status_products[Price]), 0),
              5, IF(product_count > 0, SUM(status_products[Price] * status_products[Stock]), 0),
              6, IF(r-1 <= 2, "Yes", "No"),  // Reorder needed for out of stock and low
              7, IF(r-1 = 5, "Yes", "No"),   // Overstocked for excess
              8, SWITCH(r-1, 1, "URGENT REORDER", 2, "REORDER SOON", 3, "MONITOR", 4, "OK", 5, "REDUCE ORDERS")))))),
   
   // Final comprehensive catalog report
   catalog_report, VSTACK(
     HSTACK("=== PRODUCT CATALOG MANAGEMENT SYSTEM ===", "", "", "", "", "", ""),
     "",
     HSTACK("Category Performance Analysis:", "", "", "", "", "", ""),
     HSTACK("Category", "Products", "Avg Price", "Min Price", "Max Price", "Total Stock", ""),
     pricing_analysis,
     "",
     HSTACK("Inventory Status Dashboard:", "", "", "", "", "", ""),
     inventory_dashboard,
     "",
     HSTACK("Sample Products (First 20):", "", "", "", "", "", ""),
     product_catalog[ROWS<=21]),  // Header + 20 products
   
   catalog_report)
```

### Multi-Dimensional Performance Scorecard System
```spreadsheets
// Create comprehensive performance evaluation matrix
=LET(
   departments, {"Sales", "Marketing", "Operations", "Finance", "HR"},
   metrics, {"Revenue", "Efficiency", "Quality", "Innovation", "Satisfaction"},
   quarters, {"Q1", "Q2", "Q3", "Q4"},
   
   // Generate performance data array
   performance_scores, MAKEARRAY(ROWS(departments), ROWS(metrics) * ROWS(quarters) + 1, 
     LAMBDA(r, c,
       IF(c = 1,
          INDEX(departments, r, 1),  // Department name
          // Score data
          LET(metric_index, ROUNDUP((c-1) / ROWS(quarters), 0),
              quarter_index, MOD(c-2, ROWS(quarters)) + 1,
              
              // Generate realistic performance scores with trends
              base_score, 70 + RANDBETWEEN(-10, 20),
              seasonal_adj, SWITCH(quarter_index, 1, -5, 2, 0, 3, 5, 4, 10),
              dept_factor, SWITCH(r, 1, 10, 2, 5, 3, 0, 4, -5, 5, 8),
              metric_factor, SWITCH(metric_index, 1, 15, 2, 10, 3, 5, 4, 0, 5, 12),
              
              MIN(100, MAX(0, base_score + seasonal_adj + dept_factor + metric_factor)))))),
   
   // Create performance summary dashboard
   summary_dashboard, MAKEARRAY(ROWS(departments) + 2, 8, LAMBDA(r, c,
     IF(r <= 2,
        // Header rows
        IF(r = 1,
           SWITCH(c, 1, "Department", 2, "Q4 Overall", 3, "YTD Avg", 4, "Best Metric", 
                  5, "Worst Metric", 6, "Trend", 7, "Grade", 8, "Action"),
           ""), // Empty second header row
        // Data rows
        LET(dept_index, r - 2,
            dept_name, INDEX(departments, dept_index, 1),
            dept_scores, FILTER(performance_scores, ROW(performance_scores) = dept_index + 1),
            
            // Calculate metrics
            q4_scores, {INDEX(dept_scores, 1, 5), INDEX(dept_scores, 1, 9), 
                        INDEX(dept_scores, 1, 13), INDEX(dept_scores, 1, 17), INDEX(dept_scores, 1, 21)},
            ytd_avg, AVERAGE(q4_scores),
            best_metric_idx, MATCH(MAX(q4_scores), q4_scores, 0),
            worst_metric_idx, MATCH(MIN(q4_scores), q4_scores, 0),
            
            // Trend analysis (Q4 vs Q1)
            q1_avg, AVERAGE({INDEX(dept_scores, 1, 2), INDEX(dept_scores, 1, 6), 
                            INDEX(dept_scores, 1, 10), INDEX(dept_scores, 1, 14), INDEX(dept_scores, 1, 18)}),
            trend, ytd_avg - q1_avg,
            
            SWITCH(c,
              1, dept_name,
              2, ROUND(ytd_avg, 1),
              3, ROUND(ytd_avg, 1),
              4, INDEX(metrics, best_metric_idx, 1),
              5, INDEX(metrics, worst_metric_idx, 1),
              6, IF(trend > 5, "↑ Strong", IF(trend > 0, "↑ Improving", 
                    IF(trend > -5, "→ Stable", "↓ Declining"))),
              7, IF(ytd_avg >= 90, "A", IF(ytd_avg >= 80, "B", IF(ytd_avg >= 70, "C", "D"))),
              8, IF(ytd_avg >= 85, "Maintain Excellence", 
                    IF(ytd_avg >= 70, "Targeted Improvement", "Intensive Support")))))),
   
   // Risk assessment matrix
   risk_assessment, MAKEARRAY(6, 6, LAMBDA(r, c,
     IF(r = 1,
        // Header row
        IF(c = 1, "Impact/Probability", CONCAT("P", TEXT((c-1)*20, "0"), "%")),
        IF(c = 1,
           // Impact levels
           SWITCH(r-1, 1, "Very Low", 2, "Low", 3, "Medium", 4, "High", 5, "Very High"),
           // Risk scores
           LET(impact, r-1, probability, (c-1)*0.2,
               risk_score, impact * probability,
               risk_level, IF(risk_score >= 4, "Critical",
                             IF(risk_score >= 2.4, "High Risk",
                                IF(risk_score >= 1.2, "Medium Risk", "Low Risk"))),
               risk_level))))),
   
   // Final performance report
   performance_report, VSTACK(
     HSTACK("=== ORGANIZATIONAL PERFORMANCE SCORECARD ===", "", "", "", "", "", "", ""),
     "",
     HSTACK("Department Performance Summary:", "", "", "", "", "", "", ""),
     summary_dashboard,
     "",
     HSTACK("Detailed Quarterly Scores by Department and Metric:", "", "", "", "", "", "", ""),
     HSTACK("Department", "Rev-Q1", "Rev-Q2", "Rev-Q3", "Rev-Q4", "Eff-Q1", "Eff-Q2", "Eff-Q3"),
     performance_scores[{1,2,3,4,5,6,7,8}],  // First 8 columns
     "",
     HSTACK("Risk Assessment Matrix:", "", "", "", "", "", "", ""),
     risk_assessment),
   
   performance_report)
```