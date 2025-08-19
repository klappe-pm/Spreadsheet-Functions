---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: cube
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# CUBESET

## CUBESET Description

Defines a calculated set of members or tuples from a cube using MDX (Multidimensional Expressions) syntax. This function creates dynamic groups of related members that can be used in other cube functions for advanced analytics, rankings, filtering, and complex business calculations.

> [!f(x)] CUBESET Syntax
>
> ```spreadsheets
> CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])
> ```
>
> **Parameters:**
> - `connection` (required): Text string of the name of the connection to the cube
> - `set_expression` (required): Text string of a set expression in MDX syntax that defines the members to include
> - `caption` (optional): Text string to display in the cell instead of the set name
> - `sort_order` (optional): Integer specifying sort direction (0=natural, 1=ascending, 2=descending)
> - `sort_by` (optional): Text string of MDX expression to sort the set by

> [!f(x)] CUBESET Examples
>
> ```spreadsheets
> // Top 5 products by sales
> CUBESET("Sales", "TopCount([Product].[Product Name].Members, 5, [Measures].[Sales Amount])") → {Top 5 Products}
> 
> // Specific geographic regions set
> CUBESET("Geography", "{[Geography].[North America], [Geography].[Europe], [Geography].[Asia]}") → {3 Regions}
> 
> // Bottom 10 customers by profit
> CUBESET("Customer", "BottomCount([Customer].[Customer Name].Members, 10, [Measures].[Profit])") → {Bottom 10 Customers}
> 
> // Year-to-date time periods
> CUBESET("Time", "YTD([Time].[Month].[March 2023])") → {Jan-Mar 2023}
> 
> // Dynamic set using cell reference
> CUBESET("Products", "Filter([Product].[Category].Members, [Measures].[Inventory] > "&A1) → dynamic set based on A1 threshold
> ```

## Use Cases

### [[Advanced analytics]]
- **Top/bottom analysis**: Create dynamic rankings of products, customers, or regions based on performance metrics like sales, profit, or growth rates
- **Pareto analysis**: Generate 80/20 reports by identifying the top 20% of items that contribute to 80% of results across any business dimension
- **Comparative analysis**: Build sets for period comparisons (current vs prior year), segment analysis (high vs low performers), or regional benchmarking
- **Trend analysis**: Create rolling time period sets for moving averages, seasonal comparisons, and growth trend identification
- **Exception reporting**: Define sets of outliers, underperformers, or items exceeding thresholds for focused management attention

### [[Dynamic filtering]]
- **Conditional member selection**: Filter dimension members based on measure values, creating sets that automatically adjust as underlying data changes
- **Multi-criteria filtering**: Combine multiple conditions to create complex member sets (e.g., high-value customers in specific regions during certain time periods)
- **Threshold-based grouping**: Create sets of items above or below specific performance thresholds for targeted analysis
- **Cross-dimensional filtering**: Build sets that span multiple dimensions with interdependent criteria
- **User-driven filtering**: Enable interactive reporting where users can modify filter criteria and see sets automatically update

### [[Set operations]]
- **Union operations**: Combine multiple member sets to create comprehensive analysis groups (e.g., all high-performing products across different categories)
- **Intersection analysis**: Find common members across different sets to identify items meeting multiple criteria simultaneously
- **Difference analysis**: Create sets showing what's unique to specific groups or what's changed between time periods
- **Hierarchical set manipulation**: Navigate organizational, product, or geographic hierarchies to create meaningful business groupings
- **Custom business groupings**: Define sets based on business logic that doesn't follow standard dimensional hierarchies

## Related

### Similar Functions

- [[CUBEVALUE]] - Uses CUBESET results to perform calculations across the defined set of members
- [[CUBERANKEDMEMBER]] - Returns specific ranked members from CUBESET results
- [[CUBESETCOUNT]] - Counts the number of members in a CUBESET for validation and analysis
- [[CUBEMEMBER]] - Defines individual members that can be combined into CUBESET expressions
- [[CUBEKPIMEMBER]] - Works with CUBESET to analyze KPI performance across member groups

## Cube Integration Functions

### [[CUBEVALUE]]
Primary function for retrieving aggregated values from CUBESET results. CUBESET defines the member groups while CUBEVALUE calculates totals, averages, or other measures across those groups.

```spreadsheets
// Revenue for top 10 products
=CUBEVALUE("Sales", "[Measures].[Revenue]", 
          CUBESET("Sales", "TopCount([Product].[Product Name].Members, 10, [Measures].[Sales Amount])"))
// Calculates total revenue for best-selling products

// Profit analysis for underperforming regions
=CUBEVALUE("Regional", "[Measures].[Profit Margin]", 
          CUBESET("Regional", "BottomCount([Geography].[Region].Members, 3, [Measures].[Profit])"))
// Analyzes profit margins for lowest-profit regions

// Year-over-year growth for filtered products
=CUBEVALUE("Growth", "[Measures].[YoY Growth %]", 
          CUBESET("Growth", "Filter([Product].[Category].Members, [Measures].[Revenue] > 100000)"))
// Calculates growth for high-revenue product categories
```

### [[CUBERANKEDMEMBER]]
Extracts specific ranked members from CUBESET results for detailed analysis. CUBESET creates the ranked list while CUBERANKEDMEMBER picks individual items from that list.

```spreadsheets
// Get the #1 performer from top performers set
=CUBERANKEDMEMBER("Sales", 
                 CUBESET("Sales", "TopCount([Salesperson].Members, 20, [Measures].[Revenue])"), 
                 1)
// Returns the top salesperson from the top 20 performers

// Identify 3rd worst performing product
=CUBERANKEDMEMBER("Products", 
                 CUBESET("Products", "BottomCount([Product].Members, 10, [Measures].[Profit])"), 
                 3)
// Gets the 3rd item from bottom 10 products by profit

// Find median performer in filtered set
=CUBERANKEDMEMBER("Customers", 
                 CUBESET("Customers", "Filter([Customer].Members, [Measures].[Orders] >= 5)"), 
                 CUBESETCOUNT(CUBESET("Customers", "Filter([Customer].Members, [Measures].[Orders] >= 5)"))/2)
// Finds middle-ranked customer in filtered set
```

### [[CUBESETCOUNT]]
Counts members in CUBESET results for validation, percentage calculations, and set size analysis. Essential for understanding the scope of analysis and creating proportional reports.

```spreadsheets
// Count products above threshold
=CUBESETCOUNT(CUBESET("Inventory", "Filter([Product].Members, [Measures].[Stock Level] < 50)"))
// Counts products with low inventory

// Percentage analysis with set counting
=CUBESETCOUNT(CUBESET("Performance", "Filter([Employee].Members, [Measures].[Rating] >= 4)")) / 
 CUBESETCOUNT(CUBESET("Performance", "[Employee].Members")) * 100 & "% high performers"
// Calculates percentage of high-performing employees

// Validation of set size before processing
=IF(CUBESETCOUNT(CUBESET("Sales", "TopCount([Product].Members, 5, [Measures].[Revenue])")) >= 5,
    "Full analysis available",
    "Limited data - only " & CUBESETCOUNT(CUBESET("Sales", "TopCount([Product].Members, 5, [Measures].[Revenue])")) & " products")
// Validates sufficient data for top 5 analysis
```

## Data Analysis Functions

### [[RANK]]
Combined with CUBESET to provide additional ranking context and validation for set-based analysis. Works alongside cube ranking functions for comprehensive performance analysis.

```spreadsheets
// Compare cube ranking with traditional ranking
=RANK(CUBEVALUE("Sales", "[Measures].[Revenue]", A1), 
     CUBEVALUE("Sales", "[Measures].[Revenue]", 
              CUBESET("Sales", "[Product].Members")), 0) & 
 " (Cube rank: " & 
 CUBERANKEDMEMBER("Sales", CUBESET("Sales", "[Product].Members"), A1) & ")"
// Shows both traditional and cube-based rankings

// Percentile ranking within filtered sets
=RANK(CUBEVALUE("Performance", "[Measures].[Score]", B1),
     CUBEVALUE("Performance", "[Measures].[Score]",
              CUBESET("Performance", "Filter([Employee].Members, [Measures].[Department] = 'Sales')"))) /
 CUBESETCOUNT(CUBESET("Performance", "Filter([Employee].Members, [Measures].[Department] = 'Sales')")) * 100
// Calculates percentile rank within department

// Ranking validation across multiple sets
=IF(RANK(C1, CUBEVALUE("Analysis", "[Measures].[Value]", CUBESET("Analysis", "[Items].Members"))) <= 10,
    "Top 10: Rank " & RANK(C1, CUBEVALUE("Analysis", "[Measures].[Value]", CUBESET("Analysis", "[Items].Members"))),
    "Not in top 10")
// Validates top performer status
```

### [[PERCENTILE]]
Used with CUBESET results to perform statistical analysis on cube data and identify performance thresholds within defined member groups.

```spreadsheets
// Calculate performance thresholds within sets
=PERCENTILE(CUBEVALUE("Metrics", "[Measures].[Performance Score]", 
                     CUBESET("Metrics", "[Employee].Members")), 0.9) & 
 " = 90th percentile threshold"
// Identifies top 10% performance threshold

// Set-based percentile analysis
=IF(CUBEVALUE("Sales", "[Measures].[Revenue]", D1) >= 
    PERCENTILE(CUBEVALUE("Sales", "[Measures].[Revenue]", 
                        CUBESET("Sales", "Filter([Customer].Members, [Measures].[Segment] = 'Premium')")), 0.75),
    "Top quartile premium customer",
    "Below top quartile")
// Identifies top quartile within customer segment

// Multi-set percentile comparison
=PERCENTILE(CUBEVALUE("Regional", "[Measures].[Growth]", 
                     CUBESET("Regional", "TopCount([Region].Members, 10, [Measures].[Revenue])")), 0.5) - 
 PERCENTILE(CUBEVALUE("Regional", "[Measures].[Growth]", 
                     CUBESET("Regional", "BottomCount([Region].Members, 10, [Measures].[Revenue])")), 0.5) & 
 " = median growth difference between top and bottom regions"
// Compares median growth between performance tiers
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional set creation, error handling, and dynamic set modification based on business logic and data conditions.

```spreadsheets
// Conditional set selection based on data availability
=IF(CUBESETCOUNT(CUBESET("Sales", "Filter([Product].Members, [Measures].[Revenue] > 50000)")) >= 5,
    CUBESET("Sales", "TopCount([Product].Members, 10, [Measures].[Revenue])"),
    CUBESET("Sales", "[Product].Members"))
// Uses top 10 if enough high-revenue products exist, otherwise uses all products

// Dynamic threshold adjustment
=CUBESET("Performance", 
         "Filter([Employee].Members, [Measures].[Score] > " & 
         IF(MONTH(TODAY()) <= 6, "75", "80") & ")")
// Uses different performance thresholds based on time of year

// Set validation with fallback logic
=IF(ISERROR(CUBESET("Custom", "Filter([Product].Members, [Measures].["&E1&"] > "&F1&")")),
    CUBESET("Custom", "[Product].Members"),
    CUBESET("Custom", "Filter([Product].Members, [Measures].["&E1&"] > "&F1&")"))
// Falls back to all products if custom filter fails
```

## Commonly Used With Functions Examples

### Top Performers Dashboard
```spreadsheets
// Complete top performers analysis with multiple metrics
=CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1) & 
 " leads with " & TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
                              CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1)), "$#,##0") & 
 " revenue (" & CUBESETCOUNT(CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])")) & 
 " top performers, " & 
 TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
               CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1)) / 
     CUBEVALUE("Sales", "[Measures].[Revenue]", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])")), "0.0%") & 
 " of top 10 total)"
// Example: "John Smith leads with $245,000 revenue (10 top performers, 18.5% of top 10 total)"
```

### Regional Performance Matrix
```spreadsheets
// Regional analysis with ranking and growth metrics
=IF(CUBESETCOUNT(CUBESET("Regional", "Filter([Geography].[Region].Members, [Measures].[Revenue] > 100000)")) > 0,
    "High-revenue regions (" & CUBESETCOUNT(CUBESET("Regional", "Filter([Geography].[Region].Members, [Measures].[Revenue] > 100000)")) & "): " &
    TEXT(CUBEVALUE("Regional", "[Measures].[Avg Growth %]", 
                  CUBESET("Regional", "Filter([Geography].[Region].Members, [Measures].[Revenue] > 100000)")), "0.0%") & 
    " avg growth vs " & 
    TEXT(CUBEVALUE("Regional", "[Measures].[Avg Growth %]", 
                  CUBESET("Regional", "Filter([Geography].[Region].Members, [Measures].[Revenue] <= 100000)")), "0.0%") & 
    " for smaller regions",
    "No high-revenue regions found")
// Example: "High-revenue regions (7): 12.3% avg growth vs 8.1% for smaller regions"
```

### Product Portfolio Analysis
```spreadsheets
// Comprehensive product analysis with multiple performance tiers
=CONCATENATE(
  "Top tier (" & CUBESETCOUNT(CUBESET("Products", "TopCount([Product].Members, 20, [Measures].[Profit Margin])")) & " products): ",
  TEXT(CUBEVALUE("Products", "[Measures].[Avg Margin]", CUBESET("Products", "TopCount([Product].Members, 20, [Measures].[Profit Margin])")), "0.0%"),
  " | Bottom tier (" & CUBESETCOUNT(CUBESET("Products", "BottomCount([Product].Members, 20, [Measures].[Profit Margin])")) & " products): ",
  TEXT(CUBEVALUE("Products", "[Measures].[Avg Margin]", CUBESET("Products", "BottomCount([Product].Members, 20, [Measures].[Profit Margin])")), "0.0%"),
  " | Gap: ", TEXT(CUBEVALUE("Products", "[Measures].[Avg Margin]", CUBESET("Products", "TopCount([Product].Members, 20, [Measures].[Profit Margin])")) - 
                 CUBEVALUE("Products", "[Measures].[Avg Margin]", CUBESET("Products", "BottomCount([Product].Members, 20, [Measures].[Profit Margin])")), "0.0%"))
// Example: "Top tier (20 products): 23.5% | Bottom tier (20 products): 8.2% | Gap: 15.3%"
```

### Customer Segmentation Report
```spreadsheets
// Dynamic customer analysis with conditional segmentation
=IF(CUBESETCOUNT(CUBESET("Customer", "Filter([Customer].Members, [Measures].[Lifetime Value] > 10000)")) >= 50,
    "Premium segment analysis: " & CUBESETCOUNT(CUBESET("Customer", "Filter([Customer].Members, [Measures].[Lifetime Value] > 10000)")) & 
    " customers averaging " & TEXT(CUBEVALUE("Customer", "[Measures].[Avg LTV]", 
                                            CUBESET("Customer", "Filter([Customer].Members, [Measures].[Lifetime Value] > 10000)")), "$#,##0") &
    " LTV (Top customer: " & CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 1, [Measures].[Lifetime Value])"), 1) & 
    " at " & TEXT(CUBEVALUE("Customer", "[Measures].[Lifetime Value]", 
                           CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 1, [Measures].[Lifetime Value])"), 1)), "$#,##0") & ")",
    "Insufficient premium customers for segment analysis (" & CUBESETCOUNT(CUBESET("Customer", "Filter([Customer].Members, [Measures].[Lifetime Value] > 10000)")) & " found, need 50+)")
// Example: "Premium segment analysis: 127 customers averaging $15,750 LTV (Top customer: ABC Corp at $45,200)"
```

### Time-Based Trend Analysis
```spreadsheets
// Rolling performance analysis with trend identification
=CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
          CUBESET("Trends", "LastPeriods(12, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) & 
 "% rolling 12-month growth (" & 
 IF(CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
            CUBESET("Trends", "LastPeriods(3, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) > 
   CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
            CUBESET("Trends", "LastPeriods(12, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) * 1.1, 
   "Accelerating", 
   IF(CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
               CUBESET("Trends", "LastPeriods(3, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) < 
      CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
               CUBESET("Trends", "LastPeriods(12, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) * 0.9, 
      "Decelerating", "Stable")) & 
 " trend, Q3 avg: " & 
 TEXT(CUBEVALUE("Trends", "[Measures].[Revenue Growth %]", 
               CUBESET("Trends", "LastPeriods(3, [Time].[Month].[" & TEXT(TODAY(), "mmmm yyyy") & "])")) , "0.0%") & ")"
// Example: "8.5% rolling 12-month growth (Accelerating trend, Q3 avg: 12.3%)"
```
