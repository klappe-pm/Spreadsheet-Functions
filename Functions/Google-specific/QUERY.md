---
categories: spreadsheets
subCategories: 
  - sheets
topics: google-specific
subTopics: []
dateCreated: 2025-08-17
dateRevised: 2025-08-19
aliases: []
tags: []
---

# QUERY

## QUERY Description

Runs Google Visualization API Query Language queries across data ranges using SQL-like syntax. The most powerful data manipulation function in Google Sheets, enabling complex filtering, aggregation, sorting, and grouping operations that would require multiple formulas or pivot tables.

> [!f(x)] QUERY Syntax
>
> ```spreadsheets
> QUERY(data, query, [headers])
> ```
>
> **Parameters:**
> - `data` (required): Range of data to query (A1:Z1000 format)
> - `query` (required): SQL-like query string using SELECT, WHERE, GROUP BY, ORDER BY, etc.
> - `headers` (optional): Number of header rows to skip (default is -1 for auto-detection)

> [!f(x)] QUERY Examples
>
> ```spreadsheets
> // Basic SELECT query
> QUERY(A1:E100, "SELECT A, B, C WHERE D > 500") → returns columns A,B,C where column D > 500
> 
> // Aggregation with GROUP BY
> QUERY(A1:D1000, "SELECT A, SUM(C) GROUP BY A ORDER BY SUM(C) DESC") → sums column C by groups in column A
> 
> // Complex filtering with multiple conditions
> QUERY(Data!A:Z, "SELECT B, E, G WHERE H = 'Active' AND I >= date '2024-01-01'") → filters by status and date
> 
> // Calculate percentages and format
> QUERY(A1:C500, "SELECT A, B, (C/SUM(C))*100 WHERE B IS NOT NULL LABEL (C/SUM(C))*100 'Percentage'") → adds percentage column
> 
> // Cross-sheet data consolidation
> QUERY({Sheet1!A:D;Sheet2!A:D;Sheet3!A:D}, "SELECT Col1, SUM(Col4) GROUP BY Col1") → combines multiple sheets
> ```

## Use Cases

### [[Data analysis]]
- **Business intelligence reporting**: Create comprehensive reports combining filtering, grouping, and calculations in single formulas
- **Sales performance analysis**: Track revenue by region, product, or time period with automatic aggregation and sorting
- **Customer segmentation**: Analyze customer behavior patterns using complex multi-criteria filtering and statistical functions
- **Trend identification**: Use date filtering and grouping to identify seasonal patterns and business trends across time periods

### [[Database operations]]  
- **Data filtering and extraction**: Extract specific records based on multiple criteria without manual filtering or helper columns
- **Join operations**: Combine data from multiple ranges or sheets using QUERY's ability to work with concatenated arrays
- **Data validation and cleaning**: Identify duplicate records, missing values, and data inconsistencies using SQL-like syntax
- **Dynamic reporting**: Create reports that automatically update when source data changes, eliminating manual report generation

### [[Advanced calculations]]
- **Statistical analysis**: Calculate means, counts, sums, and other aggregates across grouped data with single formulas
- **Pivot table alternatives**: Create custom pivot-like reports with more flexibility than standard pivot table functionality
- **Time-series analysis**: Analyze data across date ranges with built-in date functions and filtering capabilities
- **Cross-tabulation**: Create crosstab reports showing relationships between categorical variables with custom formatting

## Related

### Similar Functions

- [[FILTER]] - Filters data based on conditions, simpler syntax but less powerful than QUERY
- [[SORT]] - Sorts data by one or more columns, used within QUERY or as standalone function
- [[UNIQUE]] - Extracts unique values, can be combined with QUERY for advanced deduplication
- [[SUMIFS]] - Multiple criteria summation, less flexible than QUERY's GROUP BY and SUM combination
- [[PIVOT]] - Creates pivot tables, QUERY offers more customization and formatting control

## Data Manipulation Functions

### [[IMPORTRANGE]]
Frequently combined with QUERY for cross-spreadsheet data analysis. QUERY can process IMPORTRANGE results to create powerful multi-sheet reporting systems and consolidated dashboards.

```spreadsheets
// Cross-sheet data analysis
=QUERY(IMPORTRANGE("spreadsheet-id", "Sheet1!A:Z"), "SELECT Col1, Col3, Col5 WHERE Col2 = 'Active'")
// Queries data from external spreadsheet with filtering

// Multi-sheet consolidation
=QUERY({IMPORTRANGE("sheet1-id","Data!A:D");IMPORTRANGE("sheet2-id","Data!A:D")}, 
       "SELECT Col1, SUM(Col4) GROUP BY Col1 ORDER BY SUM(Col4) DESC")
// Combines data from multiple external sheets

// Dynamic cross-sheet reporting
=QUERY(IMPORTRANGE("master-sheet", "Data!A:M"), 
       "SELECT Col2, AVG(Col8), COUNT(Col1) WHERE Col5 >= date '"&TEXT(TODAY()-30,"yyyy-mm-dd")&"' GROUP BY Col2")
// Creates 30-day performance report from external data
```

### [[ARRAYFORMULA]]  
Essential for making QUERY results dynamic and expanding automatically. ARRAYFORMULA enables QUERY to work with variable-sized datasets and creates self-updating reports.

```spreadsheets
// Dynamic QUERY with ARRAYFORMULA
=ARRAYFORMULA(QUERY(INDIRECT("A1:Z"&COUNTA(A:A)), "SELECT A, B, C WHERE D > "&AVERAGE(D:D)))
// Auto-adjusts range based on data size, filters above average

// Conditional QUERY execution
=ARRAYFORMULA(IF(COUNTA(A:A)>10, QUERY(A:E, "SELECT A, SUM(E) GROUP BY A"), "Need more data"))
// Only runs QUERY when sufficient data exists

// Multi-condition dynamic filtering
=ARRAYFORMULA(QUERY(A:F, "SELECT * WHERE B CONTAINS '"&G1&"' AND E >= "&H1&" ORDER BY E DESC"))
// Uses cell references for dynamic filtering criteria
```

## Aggregation Functions

### [[SUM]]
QUERY includes powerful SUM capabilities within GROUP BY operations. Enables complex aggregations that would require multiple helper columns with traditional formulas.

```spreadsheets
// Advanced SUM aggregations
=QUERY(A1:E1000, "SELECT A, SUM(D), SUM(E), SUM(D)+SUM(E) GROUP BY A ORDER BY SUM(D) DESC LABEL SUM(D)+SUM(E) 'Total'")
// Creates multiple sum columns with calculated totals

// Conditional summation within QUERY
=QUERY(A:F, "SELECT B, SUM(C) WHERE D='Completed' AND E>=date '2024-01-01' GROUP BY B")
// Sums values based on multiple criteria

// Running totals with QUERY
=QUERY(A:C, "SELECT A, B, C, SUM(C) GROUP BY A, B ORDER BY A, B")
// Creates subtotals by category and subcategory
```

### [[COUNT]]
Built into QUERY for counting records and non-null values. Essential for creating statistical summaries and data quality reports with complex filtering conditions.

```spreadsheets
// Advanced counting operations
=QUERY(A:E, "SELECT B, COUNT(A), COUNT(C) WHERE D IS NOT NULL GROUP BY B ORDER BY COUNT(A) DESC")
// Counts records and non-null values by category

// Data quality analysis
=QUERY(A:Z, "SELECT 'Total Records: '&COUNT(A), 'Complete Records: '&COUNT(Z), 'Completion Rate: '&COUNT(Z)/COUNT(A)*100")
// Calculates data completeness statistics

// Time-period analysis
=QUERY(A:D, "SELECT MONTH(B)+1, COUNT(A) WHERE B >= date '2024-01-01' GROUP BY MONTH(B) ORDER BY MONTH(B)")
// Counts records by month with date filtering
```

## Text Processing Functions

### [[CONCAT]]
Used within QUERY for text concatenation and formatting. Enables creation of formatted output strings and complex text manipulations within query results.

```spreadsheets
// Text formatting in QUERY results
=QUERY(A:E, "SELECT A, B&' - '&C, D WHERE E='Active' LABEL B&' - '&C 'Full Name'")
// Concatenates columns with separator and custom label

// Dynamic text creation
=QUERY(A:F, "SELECT A, 'Total: $'&SUM(C), COUNT(B)&' items' GROUP BY A")
// Creates formatted text with aggregated values

// Multi-column text combination
=QUERY(A:H, "SELECT A&', '&B&' ('&C&')', SUM(G) GROUP BY A, B, C ORDER BY SUM(G) DESC")
// Complex text formatting with grouping
```

### [[TEXT]]
Combined with QUERY for number and date formatting within query results. Essential for creating professional-looking reports with proper formatting.

```spreadsheets
// Date formatting in QUERY
=QUERY(A:E, "SELECT A, B, TEXT(C,'mm/dd/yyyy'), D WHERE C >= date '2024-01-01' ORDER BY C")
// Formats dates within query results

// Number formatting with TEXT
=QUERY(A:F, "SELECT A, TEXT(AVG(D),'$#,##0.00'), COUNT(B) GROUP BY A LABEL TEXT(AVG(D),'$#,##0.00') 'Average Price'")
// Formats currency averages in grouped results

// Custom formatting combinations
=QUERY(A:G, "SELECT A, TEXT(B,'yyyy-mm')&': $'&TEXT(SUM(C),'#,##0') GROUP BY A, TEXT(B,'yyyy-mm') ORDER BY B")
// Creates monthly summaries with formatted output
```

## Date and Time Functions

### [[TODAY]]
Frequently used with QUERY for dynamic date-based filtering. Creates reports that automatically update based on current date without manual date updates.

```spreadsheets
// Dynamic date filtering
=QUERY(A:E, "SELECT * WHERE B >= date '"&TEXT(TODAY()-30,"yyyy-mm-dd")&"' ORDER BY B DESC")
// Shows last 30 days of data automatically

// Current month reporting
=QUERY(A:F, "SELECT C, SUM(D) WHERE B >= date '"&TEXT(EOMONTH(TODAY(),-1)+1,"yyyy-mm-dd")&"' AND B <= date '"&TEXT(EOMONTH(TODAY(),0),"yyyy-mm-dd")&"' GROUP BY C")
// Current month totals by category

// Year-to-date analysis
=QUERY(A:G, "SELECT D, AVG(E), COUNT(A) WHERE B >= date '"&YEAR(TODAY())&"-01-01' GROUP BY D ORDER BY AVG(E) DESC")
// YTD performance metrics by category
```

### [[DATE]]
Used within QUERY for date comparisons and filtering. Enables precise date range analysis and time-period reporting with exact date specifications.

```spreadsheets
// Specific date range analysis
=QUERY(A:F, "SELECT B, SUM(E) WHERE A >= date '2024-01-01' AND A <= date '2024-12-31' GROUP BY B")
// Annual summary by category with exact dates

// Quarter-based reporting
=QUERY(A:E, "SELECT C, AVG(D) WHERE B >= date '"&TEXT(DATE(YEAR(TODAY()),ROUNDUP(MONTH(TODAY())/3,0)*3-2,1),"yyyy-mm-dd")&"' GROUP BY C")
// Current quarter averages

// Date-based trend analysis
=QUERY(A:G, "SELECT YEAR(B), MONTH(B), SUM(F) WHERE B IS NOT NULL GROUP BY YEAR(B), MONTH(B) ORDER BY YEAR(B), MONTH(B)")
// Monthly trends across years
```

## Commonly Used With Functions Examples

### Advanced Business Intelligence Dashboard
```spreadsheets
// Executive summary with multiple metrics
=QUERY(Sales!A:M, "SELECT Region, 
       SUM(Revenue) as 'Total Revenue',
       AVG(Revenue) as 'Avg Deal Size',
       COUNT(DealID) as 'Deal Count',
       SUM(Revenue)/COUNT(DealID) as 'Revenue per Deal'
       WHERE CloseDate >= date '"&TEXT(TODAY()-90,"yyyy-mm-dd")&"'
       GROUP BY Region 
       ORDER BY SUM(Revenue) DESC")
// Complete regional performance dashboard for last 90 days
```

### Dynamic Cross-Sheet Consolidation
```spreadsheets
// Multi-location inventory analysis
=QUERY({Store1!A:F;Store2!A:F;Store3!A:F}, 
       "SELECT Col2 as Product, 
        SUM(Col4) as 'Total Stock',
        AVG(Col5) as 'Avg Price',
        COUNT(Col1) as 'Locations'
        WHERE Col3 = 'Active' AND Col4 > 0
        GROUP BY Col2
        HAVING SUM(Col4) < 100
        ORDER BY SUM(Col4)")
// Identifies low-stock products across all locations
```

### Time-Series Trend Analysis
```spreadsheets
// Monthly growth analysis
=QUERY(Data!A:H, "SELECT 
       YEAR(Date)*100+MONTH(Date) as Period,
       SUM(Sales) as 'Monthly Sales',
       COUNT(Transactions) as 'Transaction Count',
       SUM(Sales)/COUNT(Transactions) as 'Avg Transaction'
       WHERE Date >= date '"&TEXT(TODAY()-365,"yyyy-mm-dd")&"'
       GROUP BY YEAR(Date), MONTH(Date)
       ORDER BY YEAR(Date), MONTH(Date)")
// 12-month business performance trend analysis
```

### Customer Segmentation Report
```spreadsheets
// RFM Analysis using QUERY
=QUERY(Customers!A:J, "SELECT 
       CustomerType,
       COUNT(CustomerID) as 'Customer Count',
       AVG(TotalPurchases) as 'Avg Purchases',
       SUM(Revenue) as 'Segment Revenue',
       AVG(DaysSinceLastPurchase) as 'Avg Recency'
       WHERE Status = 'Active' 
       GROUP BY CustomerType
       ORDER BY SUM(Revenue) DESC")
// Customer value segmentation with behavioral metrics
```

### Performance Optimization Report
```spreadsheets
// Resource utilization analysis
=QUERY(Operations!A:L, "SELECT 
       Department,
       Resource,
       AVG(Utilization) as 'Avg Utilization %',
       MAX(Utilization) as 'Peak Usage',
       COUNT(Date) as 'Data Points'
       WHERE Date >= date '"&TEXT(TODAY()-30,"yyyy-mm-dd")&"'
         AND Utilization IS NOT NULL
       GROUP BY Department, Resource
       HAVING AVG(Utilization) > 80
       ORDER BY AVG(Utilization) DESC")
// Identifies high-utilization resources requiring attention
```
