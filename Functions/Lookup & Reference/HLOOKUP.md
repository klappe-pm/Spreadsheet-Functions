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

# HLOOKUP

## HLOOKUP Description

Searches horizontally across the first row of a table for a lookup value and returns a corresponding value from a specified row below. The horizontal counterpart to VLOOKUP, designed for tables where data is organized in rows rather than columns.

> [!f(x)] HLOOKUP Syntax
>
> ```spreadsheets
> HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
> ```
>
> **Parameters:**
> - `lookup_value` (required): The value to search for in the first row
> - `table_array` (required): The range containing both lookup and return rows
> - `row_index_num` (required): Row number in table_array to return value from (1-based)
> - `range_lookup` (optional): TRUE/FALSE or 1/0 for approximate/exact match (default: TRUE)

> [!f(x)] HLOOKUP Examples
>
> ```spreadsheets
> // Monthly sales lookup by product
> HLOOKUP("January", SalesTable, 2, FALSE) → returns January sales from row 2
> 
> // Product price lookup across quarters
> HLOOKUP(B1, PricingTable, 3, 0) → finds price for product in B1
> 
> // Performance metric by time period
> HLOOKUP("Q2", MetricsTable, 4, TRUE) → approximate match for Q2 metrics
> 
> // Dynamic row reference
> HLOOKUP(E1, DataTable, MATCH("Target", RowHeaders, 0), FALSE)
> 
> // Time-based data retrieval
> HLOOKUP(TODAY(), DateTable, 2, TRUE) → finds closest date match
> ```

## Use Cases

### [[Time series analysis]]
- **Monthly financial reports**: Look up revenue, expenses, or profit figures by month when data is arranged horizontally by time periods
- **Quarterly performance tracking**: Retrieve KPIs and metrics organized by quarters across horizontal layouts
- **Historical trend analysis**: Access past performance data where years or periods are column headers
- **Seasonal data extraction**: Find seasonal patterns in sales, inventory, or customer behavior organized by time periods

### [[Cross-tab reporting]]  
- **Product comparison matrices**: Extract specifications or features from tables where products are columns and attributes are rows
- **Regional performance analysis**: Look up sales figures, market share, or growth rates organized by geographic regions
- **Demographic analysis**: Retrieve survey results or census data organized by age groups, income brackets, or other categories
- **Competitive analysis**: Compare competitor performance across different metrics arranged in horizontal format

### [[Dashboard data retrieval]]
- **Dynamic chart data**: Feed charts and graphs with data retrieved based on user-selected time periods or categories
- **KPI monitoring**: Extract current period performance metrics from horizontally organized scorecards
- **Budget vs actual reporting**: Compare planned versus actual results organized by departments or cost centers
- **Executive summary generation**: Pull key figures for leadership reports from horizontally structured summary tables

## Related

### Similar Functions

- [[VLOOKUP]] - Searches vertically down columns instead of horizontally across rows
- [[XLOOKUP]] - Modern replacement that searches in any direction with enhanced features
- [[INDEX]] - Combined with MATCH provides more flexible horizontal lookups
- [[MATCH]] - Finds position in horizontal ranges, often used with INDEX
- [[CHOOSE]] - Selects from horizontal list by position number

## Error Handling Functions

### [[IFERROR]]
Essential for handling HLOOKUP errors gracefully when lookup values don't exist in the first row. Provides user-friendly alternatives to #N/A errors.

```spreadsheets
// Handle missing time periods
=IFERROR(HLOOKUP("Q5", QuarterlyData, 2, 0), "Quarter not found")
// Returns friendly message instead of #N/A error

// Default to zero for missing values
=IFERROR(HLOOKUP(MonthName, MonthlyBudget, 3, FALSE), 0)
// Returns 0 when month budget not available

// Chain multiple table lookups
=IFERROR(HLOOKUP(Period, CurrentYear, 2, 0), HLOOKUP(Period, PreviousYear, 2, 0))
// Tries previous year if current year data unavailable
```

### [[ISERROR]]  
Tests if HLOOKUP will generate an error before executing expensive operations, enabling conditional logic based on lookup success.

```spreadsheets
// Conditional processing based on data availability
=IF(ISERROR(HLOOKUP(Quarter, PerformanceTable, 2, 0)), "Data pending", "Report ready")
// Different status based on data availability

// Validation before calculation
=IF(ISERROR(HLOOKUP(Month, RevenueTable, 2, 0)), 0, HLOOKUP(Month, RevenueTable, 2, 0) * 1.1)
// Only applies markup if revenue data exists

// Multi-condition validation
=IF(AND(NOT(ISERROR(HLOOKUP(Period, Table1, 1, 0))), Period<>""), "Valid period", "Invalid")
// Validates both lookup success and non-empty input
```

## Date Functions

### [[TEXT]]
Formats dates and periods for consistent HLOOKUP matching, especially important when dealing with time-based horizontal tables.

```spreadsheets
// Month name lookup with consistent formatting
=HLOOKUP(TEXT(TODAY(), "mmmm"), MonthlyData, 2, FALSE)
// Converts current date to month name for lookup

// Quarter formatting for lookup
=HLOOKUP("Q" & ROUNDUP(MONTH(A1)/3, 0), QuarterlyTable, 3, 0)
// Creates quarter format like "Q1" for lookup

// Year-month combination
=HLOOKUP(TEXT(B1, "yyyy-mm"), TimeSeriesData, 4, FALSE)
// Creates consistent year-month format for horizontal time series
```

### [[TODAY]]
Enables dynamic time-based lookups that automatically update with current date, essential for rolling reports and dashboards.

```spreadsheets
// Current month performance
=HLOOKUP(TEXT(TODAY(), "mmm"), PerformanceTable, 2, 0)
// Automatically looks up current month's data

// Current quarter lookup
=HLOOKUP("Q" & ROUNDUP(MONTH(TODAY())/3, 0), QuarterlyBudget, 3, FALSE)
// Finds current quarter budget automatically

// Rolling 12-month comparison
=HLOOKUP(TEXT(TODAY()-365, "mmm yyyy"), HistoricalData, 2, 0)
// Compares to same month previous year
```

## Logical Functions

### [[IF]]
Controls HLOOKUP execution based on conditions and provides conditional logic for different lookup scenarios.

```spreadsheets
// Conditional table selection
=IF(FiscalYear=2024, HLOOKUP(Month, Data2024, 2, 0), HLOOKUP(Month, DataArchive, 2, 0))
// Different tables based on fiscal year

// Seasonal lookup logic
=IF(MONTH(TODAY())<=6, HLOOKUP("H1", HalfYearData, 2, 0), HLOOKUP("H2", HalfYearData, 2, 0))
// First or second half year data based on current month

// Performance tier lookup
=IF(Region="Premium", HLOOKUP(Product, PremiumPricing, 2, 0), HLOOKUP(Product, StandardPricing, 2, 0))
// Different pricing tables based on region tier
```

### [[AND]]
Enables complex conditional logic for HLOOKUP operations, particularly useful for multi-criteria validation.

```spreadsheets
// Multi-condition lookup validation
=IF(AND(Month<>"", NOT(ISERROR(HLOOKUP(Month, DataTable, 1, 0)))), 
   HLOOKUP(Month, DataTable, 2, 0), 
   "Invalid month")
// Validates both non-empty and valid month

// Date range validation
=IF(AND(InputDate>=StartDate, InputDate<=EndDate), 
   HLOOKUP(TEXT(InputDate, "mmm"), RangeData, 2, 0), 
   "Date out of range")
// Only performs lookup within valid date range
```

## Mathematical Functions

### [[SUM]]
Combines with HLOOKUP to create running totals and aggregate calculations across horizontal data layouts.

```spreadsheets
// Year-to-date calculation
=SUM(HLOOKUP("Jan", MonthlyData, 2, 0):HLOOKUP(TEXT(TODAY(), "mmm"), MonthlyData, 2, 0))
// Sums from January to current month

// Multi-product totals
=SUM(HLOOKUP(Product1, SalesTable, 2, 0), HLOOKUP(Product2, SalesTable, 2, 0))
// Adds sales for multiple products

// Quarterly aggregation
=SUM(HLOOKUP("Jan", Data, 2, 0):HLOOKUP("Mar", Data, 2, 0))
// Sums Q1 months for quarterly total
```

## Commonly Used With Functions Examples

### Dynamic Monthly Dashboard
```spreadsheets
// Current month performance with error handling
=IFERROR(
   HLOOKUP(TEXT(TODAY(), "mmm yyyy"), 
          PerformanceData, 
          MATCH("Revenue", RowLabels, 0), 
          FALSE), 
   "Current month data not available")
// Looks up current month revenue with graceful error handling
```

### Quarterly Comparison Analysis
```spreadsheets
// Compare current vs previous quarter
=CONCATENATE(
   "Current Q: $", HLOOKUP("Q" & ROUNDUP(MONTH(TODAY())/3, 0), QuarterlyData, 2, 0),
   " | Previous Q: $", HLOOKUP("Q" & ROUNDUP(MONTH(TODAY())/3, 0)-1, QuarterlyData, 2, 0),
   " | Change: ", 
   IF(HLOOKUP("Q" & ROUNDUP(MONTH(TODAY())/3, 0), QuarterlyData, 2, 0) > 
      HLOOKUP("Q" & ROUNDUP(MONTH(TODAY())/3, 0)-1, QuarterlyData, 2, 0), "↑", "↓"))
// Comprehensive quarterly comparison with trend indicators
```

### Multi-Criteria Budget Lookup
```spreadsheets
// Department budget by month with validation
=IF(AND(Department<>"", Month<>""), 
   IFERROR(
     HLOOKUP(Month, 
            INDIRECT(Department & "Budget"), 
            2, FALSE), 
     "No budget data for " & Department & " in " & Month), 
   "Please select department and month")
// Dynamic sheet reference with comprehensive validation
```

### Seasonal Performance Tracker
```spreadsheets
// Seasonal comparison with historical data
=IF(MONTH(TODAY()) IN {12,1,2}, 
   HLOOKUP("Winter", SeasonalData, 2, 0), 
   IF(MONTH(TODAY()) IN {3,4,5}, 
      HLOOKUP("Spring", SeasonalData, 2, 0), 
      IF(MONTH(TODAY()) IN {6,7,8}, 
         HLOOKUP("Summer", SeasonalData, 2, 0), 
         HLOOKUP("Fall", SeasonalData, 2, 0))))
// Automatic seasonal data lookup based on current date
```

### Executive Summary Generator
```spreadsheets
// Multi-metric executive summary
=CONCATENATE(
   "Revenue: $", HLOOKUP(ReportMonth, ExecutiveData, 2, 0), 
   " | Profit: $", HLOOKUP(ReportMonth, ExecutiveData, 3, 0), 
   " | Margin: ", ROUND(HLOOKUP(ReportMonth, ExecutiveData, 3, 0) / 
                       HLOOKUP(ReportMonth, ExecutiveData, 2, 0) * 100, 1), "%")
// Creates comprehensive one-line executive summary
```
