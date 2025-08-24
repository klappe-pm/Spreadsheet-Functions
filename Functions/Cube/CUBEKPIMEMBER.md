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
# CUBEKPIMEMBER

## CUBEKPIMEMBER Description

Returns a key performance indicator (KPI) property from a cube, including KPI values, goals, status indicators, trends, and weights. This function is essential for building executive dashboards and performance scorecards that display business-critical metrics with their associated targets and status indicators.

> [!f(x)] CUBEKPIMEMBER Syntax
>
> ```spreadsheets
> CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])
> ```
>
> **Parameters:**
> - `connection` (required): Text string of the name of the connection to the cube
> - `kpi_name` (required): Text string name of the KPI in the cube
> - `kpi_property` (required): Integer or text string specifying which KPI property to return (1=Value, 2=Goal, 3=Status, 4=Trend, 5=Weight, 6=StatusGraphic, 7=TrendGraphic)
> - `caption` (optional): Text string to display in the cell instead of the property name

> [!f(x)] CUBEKPIMEMBER Examples
>
> ```spreadsheets
> // Current revenue KPI value
> CUBEKPIMEMBER("Financial", "Revenue Growth", 1) → 0.125 (12.5% growth)
> 
> // Revenue growth target/goal
> CUBEKPIMEMBER("Financial", "Revenue Growth", 2) → 0.15 (15% target)
> 
> // KPI status indicator (-1=bad, 0=ok, 1=good)
> CUBEKPIMEMBER("Financial", "Revenue Growth", 3) → 0 (meeting expectations)
> 
> // Customer satisfaction trend indicator
> CUBEKPIMEMBER("Customer", "Customer Satisfaction", 4, "Satisfaction Trend") → 1 (trending up)
> 
> // KPI weight in overall scorecard
> CUBEKPIMEMBER("Scorecard", "Market Share", 5) → 0.25 (25% weight)
> ```

## Use Cases

### [[Executive dashboards]]
- **C-level scorecards**: Display key business metrics with actual values, targets, and status indicators for quick executive decision making
- **Performance monitoring**: Track critical KPIs like revenue growth, customer satisfaction, operational efficiency with real-time status updates
- **Strategic goal tracking**: Monitor progress against annual objectives, quarterly targets, and strategic initiatives with visual status indicators
- **Board reporting**: Create comprehensive dashboards showing organizational performance across all key metrics with trend analysis
- **Risk management dashboards**: Display risk indicators, compliance metrics, and warning signals with automated status evaluation

### [[KPI reporting]]
- **Balanced scorecard implementation**: Build comprehensive scorecards with financial, customer, internal process, and learning & growth perspectives
- **Department performance tracking**: Monitor departmental KPIs with individual targets, weights, and performance status across the organization
- **Project portfolio management**: Track project KPIs including budget variance, timeline adherence, quality metrics, and resource utilization
- **Sales performance management**: Monitor sales KPIs like quota attainment, pipeline health, conversion rates, and territory performance
- **Operational excellence tracking**: Display operational KPIs including efficiency ratios, quality metrics, safety indicators, and productivity measures

### [[Performance analysis]]
- **Variance analysis**: Compare actual KPI values against targets to identify performance gaps and improvement opportunities
- **Trend identification**: Track KPI trends over time to identify patterns, seasonal variations, and long-term directional changes
- **Benchmarking**: Compare KPI performance against industry standards, historical performance, and peer organizations
- **Root cause analysis**: Use KPI status and trend information to identify underlying performance drivers and improvement levers
- **Predictive analysis**: Combine KPI trends with forecasting models to predict future performance and proactive intervention needs

## Related

### Similar Functions

- [[CUBEVALUE]] - Returns raw measure values from cubes, while CUBEKPIMEMBER returns structured KPI properties
- [[CUBEMEMBER]] - Returns basic cube members, while CUBEKPIMEMBER specifically handles KPI objects
- [[CUBESET]] - Creates member sets that can include KPI members for grouped analysis
- [[CUBERANKEDMEMBER]] - Ranks regular members, while CUBEKPIMEMBER focuses on KPI status and properties
- [[CUBESETCOUNT]] - Counts set members, complementary to CUBEKPIMEMBER for KPI portfolio analysis

## KPI Analysis Functions

### [[CUBEVALUE]]
Used alongside CUBEKPIMEMBER to provide additional context and supporting metrics for KPI analysis. CUBEKPIMEMBER shows KPI status while CUBEVALUE provides detailed breakdowns.

```spreadsheets
// KPI with supporting detail
=CUBEKPIMEMBER("Sales", "Revenue Growth", 1) & " actual vs " & 
 CUBEKPIMEMBER("Sales", "Revenue Growth", 2) & " target (" & 
 TEXT(CUBEVALUE("Sales", "[Measures].[Current Revenue]"), "$#,##0") & " current revenue)"
// Shows KPI value, target, and supporting revenue detail

// Performance context with KPI status
=IF(CUBEKPIMEMBER("Operations", "Efficiency KPI", 3) = 1, 
    "Excellent: " & CUBEVALUE("Operations", "[Measures].[Efficiency %]"),
    "Needs Improvement: " & CUBEVALUE("Operations", "[Measures].[Efficiency %]"))
// Uses KPI status to contextualize detailed efficiency metrics

// Comprehensive KPI dashboard cell
="KPI: " & CUBEKPIMEMBER("Scorecard", "Customer Sat", 1) & 
 " | Target: " & CUBEKPIMEMBER("Scorecard", "Customer Sat", 2) & 
 " | Detail: " & CUBEVALUE("Customer", "[Measures].[Satisfaction Score]")
// Combines KPI properties with detailed cube values
```

### [[CHOOSE]]
Combined with CUBEKPIMEMBER to translate numeric KPI properties into meaningful business descriptions and visual indicators.

```spreadsheets
// Convert KPI status to descriptive text
=CHOOSE(CUBEKPIMEMBER("Performance", "Sales KPI", 3) + 2, "Poor", "Below Target", "Meeting Target", "Exceeding Target")
// Translates -1,0,1 status to business-friendly descriptions

// KPI trend interpretation
=CHOOSE(CUBEKPIMEMBER("Trends", "Market Share", 4) + 2, "Declining", "Stable", "Growing")
// Converts trend indicators to meaningful descriptions

// Weighted KPI importance display
=CHOOSE(ROUND(CUBEKPIMEMBER("Scorecard", "Profit Margin", 5) * 4) + 1, 
        "Low Priority", "Medium Priority", "High Priority", "Critical Priority")
// Converts KPI weights to priority levels
```

### [[LOOKUP]]
Used with CUBEKPIMEMBER to create sophisticated KPI interpretation tables and status mapping systems.

```spreadsheets
// KPI status lookup table
=LOOKUP(CUBEKPIMEMBER("Quality", "Defect Rate", 3), {-1;0;1}, 
        {"Action Required";"Monitor Closely";"Performing Well"})
// Maps KPI status values to action recommendations

// Performance rating based on KPI value and target
=LOOKUP(CUBEKPIMEMBER("Revenue", "Growth Rate", 1) / CUBEKPIMEMBER("Revenue", "Growth Rate", 2),
        {0;0.8;0.95;1.05;1.2}, 
        {"Critical";"Below";"Approaching";"Meeting";"Exceeding"})
// Creates performance rating based on actual vs target ratio

// KPI weight-based reporting priority
=LOOKUP(CUBEKPIMEMBER("Executive", A1, 5), {0;0.1;0.2;0.3}, 
        {"Optional";"Standard";"Important";"Critical"})
// Determines reporting priority based on KPI weight
```

## Status Indicator Functions

### [[IF]]
Essential for KPI status evaluation, conditional formatting, and automated alerting based on KPI performance and trends.

```spreadsheets
// KPI status-based conditional formatting
=IF(CUBEKPIMEMBER("Safety", "Incident Rate", 3) = -1, "🔴 ALERT", 
    IF(CUBEKPIMEMBER("Safety", "Incident Rate", 3) = 0, "🟡 WATCH", "🟢 GOOD"))
// Visual status indicators based on KPI status

// Multi-criteria KPI evaluation
=IF(AND(CUBEKPIMEMBER("Financial", "ROI", 3) >= 0, 
        CUBEKPIMEMBER("Financial", "Revenue Growth", 4) >= 0),
    "Strong Financial Performance", "Financial Concerns")
// Evaluates multiple KPI dimensions simultaneously

// Trend-based alerts
=IF(CUBEKPIMEMBER("Customer", "Satisfaction", 4) = -1, 
    "Customer satisfaction declining - immediate action needed",
    IF(CUBEKPIMEMBER("Customer", "Satisfaction", 4) = 1, "Customer satisfaction improving", "Stable performance"))
// Generates alerts based on KPI trend indicators
```

### [[COUNTIF]]
Used with multiple CUBEKPIMEMBER calls to analyze KPI portfolio health, identify patterns, and create summary statistics.

```spreadsheets
// Count KPIs by status across scorecard
=COUNTIF(A1:A10, CUBEKPIMEMBER("Scorecard", "Revenue", 3)) & " KPIs with same status as Revenue"
// Counts KPIs sharing similar performance status

// Portfolio health analysis
=COUNTIF(B1:B20, 1) & " KPIs exceeding targets, " & 
 COUNTIF(B1:B20, -1) & " KPIs below targets (" & 
 COUNT(B1:B20) & " total KPIs tracked)"
// Where B1:B20 contains CUBEKPIMEMBER status calls

// Trend analysis across KPI portfolio
=COUNTIF(C1:C15, 1) / COUNT(C1:C15) * 100 & "% of KPIs showing positive trends"
// Where C1:C15 contains CUBEKPIMEMBER trend calls
```

## Text Processing Functions

### [[TEXT]]
Combined with CUBEKPIMEMBER to format KPI values, percentages, and status information for professional dashboard presentation.

```spreadsheets
// Formatted KPI value with target comparison
=TEXT(CUBEKPIMEMBER("Sales", "Conversion Rate", 1), "0.0%") & " vs " & 
 TEXT(CUBEKPIMEMBER("Sales", "Conversion Rate", 2), "0.0%") & " target"
// Example: "12.5% vs 15.0% target"

// Executive summary with KPI formatting
="Performance: " & TEXT(CUBEKPIMEMBER("Executive", "Overall Score", 1), "0.0") & 
 "/5.0 (" & CHOOSE(CUBEKPIMEMBER("Executive", "Overall Score", 3) + 2, "Poor", "Fair", "Good") & ")"
// Example: "Performance: 3.8/5.0 (Good)"

// Weighted KPI importance display
=TEXT(CUBEKPIMEMBER("Portfolio", A1, 5), "0%") & " weight - " & 
 TEXT(CUBEKPIMEMBER("Portfolio", A1, 1), "#,##0") & " current value"
// Example: "25% weight - 1,247 current value"
```

### [[CONCATENATE]]
Used with CUBEKPIMEMBER to build comprehensive KPI reports, status summaries, and dashboard narratives.

```spreadsheets
// Comprehensive KPI status report
=CONCATENATE(
  "KPI: ", A1, " | ",
  "Status: ", CHOOSE(CUBEKPIMEMBER("Dashboard", A1, 3) + 2, "🔴", "🟡", "🟢"), " | ",
  "Trend: ", CHOOSE(CUBEKPIMEMBER("Dashboard", A1, 4) + 2, "↓", "→", "↑"), " | ",
  "Weight: ", TEXT(CUBEKPIMEMBER("Dashboard", A1, 5), "0%"))
// Example: "KPI: Revenue Growth | Status: 🟢 | Trend: ↑ | Weight: 30%"

// Executive dashboard summary
=CONCATENATE(
  "Q", QUARTER(TODAY()), " Performance: ",
  COUNTIF(B1:B10, 1), " exceeding, ",
  COUNTIF(B1:B10, 0), " meeting, ",
  COUNTIF(B1:B10, -1), " below targets")
// Where B1:B10 contains KPI status values

// Dynamic KPI narrative
=CONCATENATE(
  "Top Priority: ", INDEX(A1:A20, MATCH(MAX(E1:E20), E1:E20, 0)), 
  " (Weight: ", TEXT(MAX(E1:E20), "0%"), ", ",
  "Status: ", CHOOSE(INDEX(F1:F20, MATCH(MAX(E1:E20), E1:E20, 0)) + 2, "Needs Attention", "On Track", "Exceeding"), ")")
// Where E1:E20 contains KPI weights and F1:F20 contains KPI status
```

## Commonly Used With Functions Examples

### Executive KPI Dashboard
```spreadsheets
// Comprehensive executive KPI summary
=CONCATENATE(
  "🎯 ", A1, ": ", TEXT(CUBEKPIMEMBER("Executive", A1, 1), "#,##0.0"), 
  " vs ", TEXT(CUBEKPIMEMBER("Executive", A1, 2), "#,##0.0"), " target ",
  CHOOSE(CUBEKPIMEMBER("Executive", A1, 3) + 2, "🔴", "🟡", "🟢"), 
  " (", CHOOSE(CUBEKPIMEMBER("Executive", A1, 4) + 2, "↓", "→", "↑"), " trend, ",
  TEXT(CUBEKPIMEMBER("Executive", A1, 5), "0%"), " weight)")
// Example: "🎯 Revenue Growth: 12.5 vs 15.0 target 🟡 (↑ trend, 30% weight)"
```

### Scorecard Performance Matrix
```spreadsheets
// Multi-dimensional scorecard analysis
=IF(CUBEKPIMEMBER("Scorecard", B1, 5) >= 0.2,  // High-weight KPI
    TEXT(CUBEKPIMEMBER("Scorecard", B1, 1), "0.0") & 
    IF(CUBEKPIMEMBER("Scorecard", B1, 3) = 1, " ✓ EXCEEDING", 
       IF(CUBEKPIMEMBER("Scorecard", B1, 3) = 0, " → MEETING", " ✗ BELOW")) & 
    " (" & TEXT(CUBEKPIMEMBER("Scorecard", B1, 5), "0%") & " weight)",
    TEXT(CUBEKPIMEMBER("Scorecard", B1, 1), "0.0") & " (" & 
    TEXT(CUBEKPIMEMBER("Scorecard", B1, 5), "0%") & " weight)")
// Example: "85.7 ✓ EXCEEDING (25% weight)" for high-weight KPIs
```

### KPI Alert System
```spreadsheets
// Automated KPI alerting with trend analysis
=IF(AND(CUBEKPIMEMBER("Operations", C1, 3) <= 0, CUBEKPIMEMBER("Operations", C1, 4) = -1),
    "🚨 CRITICAL: " & C1 & " is " & 
    CHOOSE(CUBEKPIMEMBER("Operations", C1, 3) + 2, "POOR", "BELOW TARGET") & 
    " and DECLINING (" & TEXT(CUBEKPIMEMBER("Operations", C1, 1), "0.0%") & " current)",
    IF(CUBEKPIMEMBER("Operations", C1, 3) = -1,
       "⚠️ WARNING: " & C1 & " below target (" & TEXT(CUBEKPIMEMBER("Operations", C1, 1), "0.0%") & ")",
       "✅ " & C1 & " performing well (" & TEXT(CUBEKPIMEMBER("Operations", C1, 1), "0.0%") & ")"))
// Example: "🚨 CRITICAL: Safety Score is POOR and DECLINING (2.1% current)"
```

### Weighted Portfolio Analysis
```spreadsheets
// Portfolio-wide performance calculation with KPI weights
=SUMPRODUCT((CUBEKPIMEMBER("Portfolio", D1:D10, 1) / CUBEKPIMEMBER("Portfolio", D1:D10, 2)) * 
            CUBEKPIMEMBER("Portfolio", D1:D10, 5)) * 100 & 
 "% weighted portfolio performance (" & 
 COUNTIF(INDIRECT("E1:E"&ROWS(D1:D10)), ">="&0.95) & "/" & ROWS(D1:D10) & " KPIs meeting 95%+ of target, " &
 TEXT(SUMPRODUCT(CUBEKPIMEMBER("Portfolio", D1:D10, 5)), "0%") & " total weight verified)"
// Where E1:E10 contains actual-to-target ratios
// Example: "87.3% weighted portfolio performance (7/10 KPIs meeting 95%+ of target, 100% total weight verified)"
```

### Trend-Based Forecasting
```spreadsheets
// KPI trend analysis with predictive insights
=CONCATENATE(
  "Current: ", TEXT(CUBEKPIMEMBER("Forecast", E1, 1), "#,##0.0"), 
  " | Target: ", TEXT(CUBEKPIMEMBER("Forecast", E1, 2), "#,##0.0"),
  " | Trend: ", CHOOSE(CUBEKPIMEMBER("Forecast", E1, 4) + 2, "Declining ↓", "Stable →", "Improving ↑"),
  " | Projection: ", 
  IF(CUBEKPIMEMBER("Forecast", E1, 4) = 1, "Target achievable", 
     IF(CUBEKPIMEMBER("Forecast", E1, 4) = 0, "Monitor closely", "Intervention needed")),
  " (Confidence: ", TEXT(ABS(CUBEKPIMEMBER("Forecast", E1, 4)) * CUBEKPIMEMBER("Forecast", E1, 5), "0%"), ")")
// Example: "Current: 87.5 | Target: 90.0 | Trend: Improving ↑ | Projection: Target achievable (Confidence: 78%)"
```
