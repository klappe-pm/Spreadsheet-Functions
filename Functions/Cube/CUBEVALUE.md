---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - cube
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
# CUBEVALUE

## CUBEVALUE Description

Returns an aggregated value from a cube by specifying the cube connection, member expressions, and optional filters. This function retrieves calculated values like sales totals, averages, counts, or other measures from OLAP cubes based on the specified criteria.

> [!f(x)] CUBEVALUE Syntax
>
> ```spreadsheets
> CUBEVALUE(connection, [member_expression1], [member_expression2], ...)
> ```
>
> **Parameters:**
> - `connection` (required): Text string of the name of the connection to the cube
> - `member_expression1, member_expression2, ...` (optional): Text strings of multidimensional expressions (MDX) that evaluate to members or tuples within the cube (up to 255 member expressions)

> [!f(x)] CUBEVALUE Examples
>
> ```spreadsheets
> // Basic sales total from cube
> CUBEVALUE("Sales", "[Measures].[Total Sales]", "[Time].[2023]") → 1500000
> 
> // Product sales for specific region and time
> CUBEVALUE("Sales", "[Measures].[Revenue]", "[Product].[Bikes]", "[Geography].[North America]", "[Time].[Q1 2023]") → 245000
> 
> // Count of transactions with multiple filters
> CUBEVALUE("Transactions", "[Measures].[Transaction Count]", "[Customer Type].[Premium]", "[Channel].[Online]") → 1247
> 
> // Average order value calculation
> CUBEVALUE("Orders", "[Measures].[Average Order Value]", "[Product Category].[Electronics]", "[Time].[2023]") → 387.50
> 
> // Using cell references for dynamic queries
> CUBEVALUE("Inventory", "[Measures].[Units In Stock]", "[Product].["&A1&"]", "[Location].["&B1&"]") → dynamic result based on A1 and B1 values
> ```

## Use Cases

### [[OLAP reporting]]
- **Executive dashboards**: Display key business metrics like total revenue, profit margins, and growth rates from multidimensional data cubes for C-level decision making
- **Financial consolidation**: Aggregate financial data across multiple dimensions (time, geography, business units) to create consolidated financial statements and variance reports
- **Sales performance analysis**: Retrieve sales totals, quotas, and achievements by salesperson, territory, product line, and time period for performance evaluation
- **Budget vs actual reporting**: Compare planned versus actual expenses across departments, projects, and time periods using cube aggregations
- **KPI monitoring**: Pull key performance indicators from cubes to create real-time dashboards showing metrics like customer satisfaction, productivity, and quality measures

### [[Multidimensional analysis]]
- **Product profitability analysis**: Calculate profit margins and contribution margins across product hierarchies, customer segments, and sales channels
- **Customer segmentation reporting**: Analyze customer behavior patterns, lifetime value, and purchasing trends by demographic and geographic dimensions
- **Inventory optimization**: Track inventory levels, turnover rates, and stockout incidents across locations, products, and time to optimize supply chain
- **Market basket analysis**: Examine purchase patterns and product affinities across different customer segments and time periods
- **Campaign effectiveness**: Measure marketing campaign ROI, conversion rates, and customer acquisition costs across channels and demographics

### [[Data aggregation]]
- **Time series aggregation**: Roll up daily transactions to monthly, quarterly, and yearly summaries while maintaining drill-down capability
- **Geographic consolidation**: Aggregate performance metrics from store level to district, region, and national levels for hierarchical reporting
- **Cross-functional analytics**: Combine data from sales, marketing, finance, and operations cubes to create integrated business intelligence reports
- **Comparative analysis**: Generate period-over-period comparisons, variance analysis, and trend identification across multiple business dimensions
- **Exception reporting**: Identify outliers and anomalies in business performance by comparing actual values against historical averages and targets

## Related

### Similar Functions

- [[CUBEMEMBER]] - Returns a member or tuple from the cube, used to define the member expressions for CUBEVALUE
- [[CUBESET]] - Defines a calculated set of members or tuples that can be referenced in CUBEVALUE calculations
- [[CUBEKPIMEMBER]] - Returns key performance indicator properties, often used alongside CUBEVALUE for KPI reporting
- [[CUBERANKEDMEMBER]] - Returns ranked members from a set, useful for top/bottom analysis with CUBEVALUE
- [[CUBESETCOUNT]] - Returns the number of items in a set, complementing CUBEVALUE for count-based analysis

## Cube Integration Functions

### [[CUBEMEMBER]]
Used with CUBEVALUE to define and validate member expressions before retrieving values. CUBEMEMBER ensures proper member syntax and provides member properties that enhance CUBEVALUE queries.

```spreadsheets
// Define member first, then use in CUBEVALUE
=CUBEMEMBER("Sales", "[Product].[Bikes]")
=CUBEVALUE("Sales", "[Measures].[Revenue]", A1) // A1 contains the CUBEMEMBER result
// Ensures member exists before querying values

// Dynamic member selection with validation
=CUBEVALUE("Inventory", "[Measures].[Stock Level]", CUBEMEMBER("Inventory", "[Product].["&B2&"]"))
// Validates product exists before retrieving stock level

// Member hierarchy navigation
=CUBEVALUE("Sales", "[Measures].[Total Sales]", CUBEMEMBER("Sales", "[Geography].[Country].[USA].[California]"))
// Uses CUBEMEMBER to navigate geographic hierarchy
```

### [[CUBESET]]
Combined with CUBEVALUE to perform calculations over sets of members. CUBESET defines groups of members that CUBEVALUE can aggregate across, enabling complex analytical queries.

```spreadsheets
// Aggregate sales across top 5 products
=CUBEVALUE("Sales", "[Measures].[Revenue]", CUBESET("Sales", "TopCount([Product].[Product Name].Members, 5, [Measures].[Sales Amount])"))
// Calculates total revenue for best-selling products

// Regional performance for specific countries
=CUBEVALUE("Performance", "[Measures].[Profit]", CUBESET("Performance", "{[Geography].[USA], [Geography].[Canada], [Geography].[Mexico]}"))
// Aggregates profit across North American countries

// Time period analysis using sets
=CUBEVALUE("Financial", "[Measures].[Revenue]", CUBESET("Financial", "[Time].[Q1 2023]:[Time].[Q4 2023]"))
// Calculates annual revenue by defining quarterly range
```

## Conditional Logic Functions

### [[IF]]
Essential for error handling, conditional cube queries, and data validation with CUBEVALUE. IF enables graceful handling of missing data, member validation, and conditional reporting logic.

```spreadsheets
// Error-resistant cube queries
=IF(ISERROR(CUBEVALUE("Sales", "[Measures].[Revenue]", "[Product].["&A1&"]")), "Product not found", CUBEVALUE("Sales", "[Measures].[Revenue]", "[Product].["&A1&"]"))
// Handles invalid product names gracefully

// Conditional KPI reporting
=IF(CUBEVALUE("Performance", "[Measures].[Sales]", "[Time].[Current Month]")>CUBEVALUE("Performance", "[Measures].[Target]", "[Time].[Current Month]"), "Above Target", "Below Target")
// Compares actual vs target performance

// Hierarchical data validation
=IF(CUBEVALUE("Inventory", "[Measures].[Stock Count]", "[Product].["&B1&"]")<10, "Reorder Required", "Stock Adequate")
// Inventory management alerts based on stock levels
```

### [[IFERROR]]
Combined with CUBEVALUE to provide clean error handling for cube connection issues, invalid members, or data unavailability. IFERROR ensures reports remain professional when cube data has problems.

```spreadsheets
// Clean error handling for missing data
=IFERROR(CUBEVALUE("Sales", "[Measures].[Revenue]", "[Product].["&A2&"]", "[Time].["&B2&"]"), "Data unavailable")
// Shows friendly message instead of error codes

// Fallback to alternative measures
=IFERROR(CUBEVALUE("Performance", "[Measures].[Actual Sales]", C1), CUBEVALUE("Performance", "[Measures].[Estimated Sales]", C1))
// Uses estimated values when actual data missing

// Connection validation
=IFERROR(CUBEVALUE("MainCube", "[Measures].[Test]"), "Cube connection failed")
// Tests cube connectivity with graceful failure message
```

## Text Processing Functions

### [[CONCATENATE]]
Used with CUBEVALUE to build dynamic member expressions and create flexible cube queries. CONCATENATE enables parameterized reporting where member paths are constructed from user inputs.

```spreadsheets
// Dynamic product and time selection
=CUBEVALUE("Sales", "[Measures].[Revenue]", CONCATENATE("[Product].[", A1, "]"), CONCATENATE("[Time].[", B1, "]"))
// Builds member expressions from cell references

// Hierarchical path construction
=CUBEVALUE("Geography", "[Measures].[Population]", CONCATENATE("[Geography].[Country].[USA].[State].[", C1, "].[City].[", D1, "])"))
// Creates geographic hierarchy path from state and city inputs

// Multi-level filtering with dynamic construction
=CUBEVALUE("Sales", "[Measures].[Units Sold]", CONCATENATE("[Customer].[Segment].[", E1, "]"), CONCATENATE("[Product].[Category].[", F1, "]"))
// Builds complex filter expressions from multiple criteria
```

## Commonly Used With Functions Examples

### Sales Performance Dashboard
```spreadsheets
// Current month sales with growth comparison
=CUBEVALUE("Sales", "[Measures].[Revenue]", "[Time].[Current Month]") & " (" & 
 IF(CUBEVALUE("Sales", "[Measures].[Revenue]", "[Time].[Current Month]") > 
    CUBEVALUE("Sales", "[Measures].[Revenue]", "[Time].[Previous Month]"), "+", "-") & 
 TEXT((CUBEVALUE("Sales", "[Measures].[Revenue]", "[Time].[Current Month]") / 
       CUBEVALUE("Sales", "[Measures].[Revenue]", "[Time].[Previous Month]")) - 1, "0.0%") & ")"
// Example: "$125,000 (+12.5%)"
```

### Regional Performance Analysis
```spreadsheets
// Top performing region with percentage of total
=CUBERANKEDMEMBER("Sales", CUBESET("Sales", "[Geography].[Region].Members"), 1, "[Measures].[Revenue]") & 
 " - " & TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
                      CUBERANKEDMEMBER("Sales", CUBESET("Sales", "[Geography].[Region].Members"), 1, "[Measures].[Revenue]")) /
              CUBEVALUE("Sales", "[Measures].[Revenue]"), "0.0%") & " of total"
// Example: "West Region - 34.2% of total"
```

### Inventory Management Alert
```spreadsheets
// Stock status with reorder recommendations
=IF(CUBEVALUE("Inventory", "[Measures].[Current Stock]", "[Product].["&A1&"]") < 
    CUBEVALUE("Inventory", "[Measures].[Reorder Point]", "[Product].["&A1&"]"),
    "REORDER: " & CUBEVALUE("Inventory", "[Measures].[Suggested Order Qty]", "[Product].["&A1&"]") & " units",
    "Stock OK: " & CUBEVALUE("Inventory", "[Measures].[Current Stock]", "[Product].["&A1&"]") & " units available")
// Example: "REORDER: 500 units" or "Stock OK: 1,250 units available"
```

### Executive Summary Report
```spreadsheets
// Comprehensive business metric with variance analysis
=CONCATENATE(
  "Revenue: ", TEXT(CUBEVALUE("Financial", "[Measures].[Revenue]", "[Time].[YTD]"), "$#,##0"),
  " | Profit: ", TEXT(CUBEVALUE("Financial", "[Measures].[Profit]", "[Time].[YTD]"), "$#,##0"),
  " | Margin: ", TEXT(CUBEVALUE("Financial", "[Measures].[Profit Margin]", "[Time].[YTD]"), "0.0%"),
  " | vs Target: ", IF(CUBEVALUE("Financial", "[Measures].[Variance %]", "[Time].[YTD]")>0, "+", ""),
  TEXT(CUBEVALUE("Financial", "[Measures].[Variance %]", "[Time].[YTD]"), "0.0%"))
// Example: "Revenue: $2,500,000 | Profit: $350,000 | Margin: 14.0% | vs Target: +2.5%"
```

### Customer Analysis Matrix
```spreadsheets
// Customer segment performance with rankings
=IFERROR(
  CUBERANKEDMEMBER("Customer", CUBESET("Customer", "[Customer].[Segment].Members"), 1, "[Measures].[Lifetime Value]") &
  " leads with " & TEXT(CUBEVALUE("Customer", "[Measures].[Lifetime Value]", 
                                CUBERANKEDMEMBER("Customer", CUBESET("Customer", "[Customer].[Segment].Members"), 1, "[Measures].[Lifetime Value]")), "$#,##0") &
  " avg LTV (" & CUBESETCOUNT(CUBESET("Customer", "[Customer].[Customer Name].Members")) & " customers)",
  "Customer data unavailable")
// Example: "Premium leads with $15,750 avg LTV (1,247 customers)"
```
