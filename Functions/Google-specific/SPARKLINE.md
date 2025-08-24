---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - sheets
  - - topics
    - - google-specific
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# SPARKLINE

## SPARKLINE Description

Creates miniature charts within a single cell to visualize data trends, patterns, and distributions. Provides instant visual context for datasets without requiring separate chart objects, perfect for dashboards, reports, and inline data analysis where space is limited.

> [!f(x)] SPARKLINE Syntax
>
> ```spreadsheets
> SPARKLINE(data, [options])
> ```
>
> **Parameters:**
> - `data` (required): Range of data to chart (A1:A10 format)
> - `options` (optional): JSON object with chart customization options like {"charttype","line";"color1","blue"}

> [!f(x)] SPARKLINE Examples
>
> ```spreadsheets
> // Basic line sparkline
> SPARKLINE(A1:A12) → creates simple line chart showing trend over 12 data points
> 
> // Column chart sparkline
> SPARKLINE(B2:B20, {"charttype","column"}) → creates mini column chart for data range
> 
> // Customized line chart with color
> SPARKLINE(C1:C50, {"charttype","line";"color1","red";"linewidth",2}) → red line chart with thick line
> 
> // Win/loss chart for positive/negative data
> SPARKLINE(D2:D30, {"charttype","winloss"}) → shows gains/losses as up/down bars
> 
> // Stacked bar with custom colors
> SPARKLINE(E1:F1, {"charttype","stacked";"color1","green";"color2","red"}) → stacked bar chart with custom colors
> ```

## Use Cases

### [[Dashboard visualization]]
- **KPI trend display**: Show performance trends alongside key metrics without cluttering dashboard space
- **Inline analytics**: Embed visual context directly in data tables for immediate pattern recognition
- **Executive summaries**: Provide visual overview of multiple metrics in compact executive dashboard formats
- **Status indicators**: Use win/loss sparklines to show progress against targets and benchmarks visually

### [[Financial reporting]]  
- **Stock price trends**: Display price movements, volume patterns, and volatility indicators in financial portfolios
- **Revenue analysis**: Show monthly/quarterly revenue trends alongside actual numbers for context
- **Budget variance**: Visualize budget vs actual spending patterns over time periods
- **Portfolio performance**: Create visual summaries of investment performance across different time horizons

### [[Performance monitoring]]
- **Sales tracking**: Monitor sales team performance trends alongside actual numbers for pattern identification
- **Website analytics**: Display traffic, conversion, and engagement trends in compact dashboard format
- **Manufacturing metrics**: Show production efficiency, quality metrics, and downtime patterns visually
- **Customer satisfaction**: Track satisfaction scores, NPS trends, and customer feedback patterns over time

## Related

### Similar Functions

- [[GOOGLEFINANCE]] - Provides financial data that works excellently with SPARKLINE for market visualization
- [[IMPORTRANGE]] - Sources data for sparklines from external sheets for distributed dashboard creation
- [[QUERY]] - Filters and prepares data for sparkline visualization with specific criteria
- [[ARRAYFORMULA]] - Enables dynamic sparkline creation across multiple rows or datasets
- [[IMPORTHTML]] - Imports web data that can be visualized immediately with sparklines

## Data Visualization Functions

### [[GOOGLEFINANCE]]
Perfect combination for financial sparklines showing stock trends, currency movements, and market performance in dashboard format.

```spreadsheets
// Stock price trend sparkline
=SPARKLINE(GOOGLEFINANCE("AAPL","close",TODAY()-30,TODAY(),"DAILY"), {"charttype","line";"color1","blue";"linewidth",2})
// Shows 30-day Apple stock price trend

// Portfolio performance visualization
=SPARKLINE(TRANSPOSE(GOOGLEFINANCE(A2:A5,"changepct")), {"charttype","column";"color1","green";"negcolor","red"})
// Column chart showing daily changes for portfolio stocks

// Currency trend monitoring
=SPARKLINE(GOOGLEFINANCE("CURRENCY:USDEUR","price",TODAY()-90,TODAY(),"DAILY"), {"charttype","line";"color1","purple"})
// 90-day EUR/USD exchange rate trend
```

### [[QUERY]]  
Enables filtered and processed data visualization with sparklines, creating targeted visual analysis of specific data subsets.

```spreadsheets
// Filtered data sparkline
=SPARKLINE(QUERY(A1:C100,"SELECT C WHERE B > 1000 ORDER BY A"), {"charttype","line";"color1","orange"})
// Charts only values where column B > 1000

// Aggregated trend visualization
=SPARKLINE(QUERY(Sales!A:D,"SELECT SUM(D) WHERE A >= date '2024-01-01' GROUP BY MONTH(A) ORDER BY MONTH(A)"), {"charttype","column"})
// Monthly sales totals as column chart

// Category performance comparison
=SPARKLINE(QUERY(Data!A:E,"SELECT AVG(E) GROUP BY D ORDER BY AVG(E) DESC LIMIT 5"), {"charttype","column";"color1","teal"})
// Top 5 categories by average performance
```

## Array Processing Functions

### [[ARRAYFORMULA]]
Creates multiple sparklines simultaneously and enables dynamic sparkline generation across datasets.

```spreadsheets
// Multiple trend sparklines
=ARRAYFORMULA(IF(ROW(A2:A20)<=COUNTA(Data!A:A), SPARKLINE(OFFSET(Data!B1,ROW(A2:A20),0,1,12)), ""))
// Creates sparkline for each row of 12-month data

// Conditional sparkline creation
=ARRAYFORMULA(IF(SUM(B2:M2)>0, SPARKLINE(B2:M2,{"charttype","line"}), "No data"))
// Only creates sparklines for rows with data

// Dynamic chart type selection
=ARRAYFORMULA(SPARKLINE(B2:M2, IF(MAX(B2:M2)>1000,{"charttype","column"},{"charttype","line"})))
// Uses column chart for large numbers, line for smaller
```

### [[IMPORTRANGE]]
Sources data from external sheets for sparkline visualization, creating distributed dashboard systems with visual components.

```spreadsheets
// Cross-sheet performance sparklines
=SPARKLINE(IMPORTRANGE("team-metrics","Performance!B2:M2"), {"charttype","line";"color1","green"})
// Charts performance data from external team sheet

// Multi-location trend comparison
=SPARKLINE(TRANSPOSE(IMPORTRANGE("locations","Summary!C2:C10")), {"charttype","column";"color1","blue"})
// Column chart of data from multiple locations

// Historical trend from archive
=SPARKLINE(IMPORTRANGE("data-archive","Monthly!D2:D13"), {"charttype","line";"linewidth",3})
// Historical 12-month trend from archive sheet
```

## Conditional Logic Functions

### [[IF]]
Enables conditional sparkline creation based on data availability, thresholds, and business rules for smart dashboard visualization.

```spreadsheets
// Conditional sparkline display
=IF(COUNT(B2:M2)>=6, SPARKLINE(B2:M2,{"charttype","line"}), "Need more data")
// Only shows sparkline when enough data points exist

// Performance-based chart type
=IF(AVERAGE(C2:N2)>TARGET, SPARKLINE(C2:N2,{"charttype","line";"color1","green"}), SPARKLINE(C2:N2,{"charttype","line";"color1","red"}))
// Green for above target, red for below target

// Trend-based visualization
=IF(INDEX(L2:L2,1)>INDEX(B2:B2,1), SPARKLINE(B2:L2,{"charttype","line";"color1","blue"}), SPARKLINE(B2:L2,{"charttype","line";"color1","orange"}))
// Different colors based on whether trend is up or down
```

### [[ISNUMBER]]
Validates data quality before creating sparklines, ensuring clean visualizations and preventing errors from invalid data.

```spreadsheets
// Data validation sparklines
=IF(SUMPRODUCT(--(ISNUMBER(B2:M2)))>=COLUMNS(B2:M2)*0.8, SPARKLINE(B2:M2), "Insufficient numeric data")
// Requires 80% numeric data before creating sparkline

// Clean data visualization
=SPARKLINE(IF(ISNUMBER(C2:N2),C2:N2,0), {"charttype","column";"color1","teal"})
// Replaces non-numeric values with 0 for clean charting

// Quality control sparklines
=IF(AND(ISNUMBER(MAX(D2:O2)),ISNUMBER(MIN(D2:O2))), SPARKLINE(D2:O2,{"charttype","line"}), "Data quality issue")
// Checks for valid min/max before charting
```

## Date and Time Functions

### [[TODAY]]
Creates dynamic time-based sparklines that automatically update with current data and time periods.

```spreadsheets
// Rolling 30-day sparkline
=SPARKLINE(FILTER(B:B,A:A>=TODAY()-30), {"charttype","line";"color1","blue"})
// Shows last 30 days of data automatically

// Current month performance
=SPARKLINE(FILTER(Sales!C:C,MONTH(Sales!A:A)=MONTH(TODAY())), {"charttype","column"})
// Current month sales trend

// Year-to-date visualization
=SPARKLINE(FILTER(Revenue!D:D,YEAR(Revenue!A:A)=YEAR(TODAY())), {"charttype","line";"linewidth",2})
// YTD revenue trend with thick line
```

### [[WEEKNUM]]
Creates weekly and periodic sparklines for time-series analysis and seasonal pattern identification.

```spreadsheets
// Weekly performance sparklines
=SPARKLINE(QUERY(Data!A:C,"SELECT SUM(C) WHERE WEEKNUM(A) >= "&(WEEKNUM(TODAY())-12)&" GROUP BY WEEKNUM(A) ORDER BY WEEKNUM(A)"), {"charttype","column"})
// Last 12 weeks of data as columns

// Seasonal pattern visualization
=SPARKLINE(QUERY(Sales!A:B,"SELECT AVG(B) GROUP BY WEEKNUM(A) ORDER BY WEEKNUM(A)"), {"charttype","line";"color1","purple"})
// Average weekly sales pattern across year

// Quarterly trend comparison
=SPARKLINE(QUERY(Metrics!A:D,"SELECT SUM(D) GROUP BY QUARTER(A), YEAR(A) ORDER BY YEAR(A), QUARTER(A)"), {"charttype","column";"color1","green"})
// Quarterly totals across multiple years
```

## Text Processing Functions

### [[CONCATENATE]]
Creates dynamic sparkline titles and labels, combining visual charts with descriptive text for comprehensive dashboard elements.

```spreadsheets
// Sparkline with dynamic title
=CONCATENATE("Trend: ", TEXT(INDEX(B2:M2,COLUMNS(B2:M2)),"0.0"), " | ", SPARKLINE(B2:M2,{"charttype","line"}))
// Combines current value with trend visualization

// Multi-metric sparkline display
=CONCATENATE(A2, " Performance: ", SPARKLINE(B2:M2,{"charttype","line"}), " | Avg: ", TEXT(AVERAGE(B2:M2),"0.00"))
// Shows name, sparkline, and average in one cell

// Status indicator with visualization
=CONCATENATE(IF(INDEX(L2:L2,1)>K2,"↑","↓"), " ", SPARKLINE(B2:L2,{"charttype","line"}), " ", TEXT(INDEX(L2:L2,1),"0.0%"))
// Trend arrow, sparkline, and current percentage
```

## Commonly Used With Functions Examples

### Executive Dashboard with Multiple KPIs
```spreadsheets
// Multi-metric performance dashboard
=ARRAYFORMULA(IF(A2:A10="","",{
  A2:A10,
  SPARKLINE(OFFSET(MonthlyData!B1,MATCH(A2:A10,MonthlyData!A:A,0)-1,0,1,12),{"charttype","line";"color1","blue"}),
  TEXT(INDEX(OFFSET(MonthlyData!B1,MATCH(A2:A10,MonthlyData!A:A,0)-1,0,1,12),0,12),"0.0"),
  IF(INDEX(OFFSET(MonthlyData!B1,MATCH(A2:A10,MonthlyData!A:A,0)-1,0,1,12),0,12)>INDEX(OFFSET(MonthlyData!B1,MATCH(A2:A10,MonthlyData!A:A,0)-1,0,1,12),0,11),"↑","↓")
}))
// Shows KPI name, 12-month sparkline, current value, and trend direction
```

### Financial Portfolio Visualization
```spreadsheets
// Stock portfolio with price trends and performance
=ARRAYFORMULA(IF(A2:A20="","",{
  A2:A20,
  GOOGLEFINANCE(A2:A20,"price"),
  SPARKLINE(GOOGLEFINANCE(A2:A20,"close",TODAY()-30,TODAY(),"DAILY"),{"charttype","line";"color1",IF(GOOGLEFINANCE(A2:A20,"changepct")>0,"green","red")}),
  TEXT(GOOGLEFINANCE(A2:A20,"changepct"),"+0.00%;-0.00%"),
  GOOGLEFINANCE(A2:A20,"volume")
}))
// Symbol, price, 30-day trend (green/red based on performance), change %, volume
```

### Sales Performance Dashboard
```spreadsheets
// Regional sales performance with trends
=QUERY(ARRAYFORMULA({
  SalesData!B:B,
  SPARKLINE(QUERY(SalesData!A:C,"SELECT SUM(C) WHERE B = '"&SalesData!B2:B50&"' GROUP BY MONTH(A) ORDER BY MONTH(A)"),{"charttype","column"}),
  QUERY(SalesData!A:C,"SELECT SUM(C) WHERE B = '"&SalesData!B2:B50&"'"),
  QUERY(SalesData!A:C,"SELECT AVG(C) WHERE B = '"&SalesData!B2:B50&"'")
}), "SELECT Col1, Col2, Col3, Col4 WHERE Col1 IS NOT NULL GROUP BY Col1")
// Region, monthly trend sparkline, total sales, average monthly sales
```

### Website Analytics Visualization
```spreadsheets
// Multi-metric web analytics dashboard
=ARRAYFORMULA({
  {"Metric","7-Day Trend","Current","Change"},
  {"Page Views",SPARKLINE(IMPORTRANGE("analytics","Daily!B2:B8"),{"charttype","line";"color1","blue"}),IMPORTRANGE("analytics","Daily!B8"),TEXT((IMPORTRANGE("analytics","Daily!B8")-IMPORTRANGE("analytics","Daily!B7"))/IMPORTRANGE("analytics","Daily!B7"),"+0.0%;-0.0%")},
  {"Sessions",SPARKLINE(IMPORTRANGE("analytics","Daily!C2:C8"),{"charttype","line";"color1","green"}),IMPORTRANGE("analytics","Daily!C8"),TEXT((IMPORTRANGE("analytics","Daily!C8")-IMPORTRANGE("analytics","Daily!C7"))/IMPORTRANGE("analytics","Daily!C7"),"+0.0%;-0.0%")},
  {"Conversion Rate",SPARKLINE(IMPORTRANGE("analytics","Daily!D2:D8"),{"charttype","line";"color1","purple"}),TEXT(IMPORTRANGE("analytics","Daily!D8"),"0.00%"),TEXT((IMPORTRANGE("analytics","Daily!D8")-IMPORTRANGE("analytics","Daily!D7"))/IMPORTRANGE("analytics","Daily!D7"),"+0.0%;-0.0%")}
})
// Comprehensive web analytics with sparklines for key metrics
```

### Manufacturing Quality Control
```spreadsheets
// Quality metrics with trend visualization and alerts
=ARRAYFORMULA(IF(A2:A15="","",{
  A2:A15,
  SPARKLINE(OFFSET(QualityData!B1,MATCH(A2:A15,QualityData!A:A,0)-1,0,1,24),IF(AVERAGE(OFFSET(QualityData!B1,MATCH(A2:A15,QualityData!A:A,0)-1,0,1,24))<0.95,{"charttype","line";"color1","red"},{"charttype","line";"color1","green"})),
  TEXT(AVERAGE(OFFSET(QualityData!B1,MATCH(A2:A15,QualityData!A:A,0)-1,0,1,24)),"0.0%"),
  IF(AVERAGE(OFFSET(QualityData!B1,MATCH(A2:A15,QualityData!A:A,0)-1,0,1,24))<0.95,"⚠️ ALERT","✓ OK")
}))
// Process name, 24-hour trend (red if <95% quality), current average, status alert
```
