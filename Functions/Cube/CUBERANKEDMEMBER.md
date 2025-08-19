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

# CUBERANKEDMEMBER

## CUBERANKEDMEMBER Description

Returns the nth ranked member from a set of cube members, ordered by a specified measure. This function is essential for creating top/bottom analyses, identifying best/worst performers, and building dynamic ranking reports from OLAP data structures.

> [!f(x)] CUBERANKEDMEMBER Syntax
>
> ```spreadsheets
> CUBERANKEDMEMBER(connection, set_expression, rank, [caption])
> ```
>
> **Parameters:**
> - `connection` (required): Text string of the name of the connection to the cube
> - `set_expression` (required): CUBESET function result or MDX set expression defining the ranked members
> - `rank` (required): Integer position in the ranking (1 = highest, 2 = second highest, etc.)
> - `caption` (optional): Text string to display in the cell instead of the member name

> [!f(x)] CUBERANKEDMEMBER Examples
>
> ```spreadsheets
> // Top performing salesperson
> CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1) → John Smith
> 
> // 3rd best selling product
> CUBERANKEDMEMBER("Products", CUBESET("Products", "TopCount([Product].Members, 5, [Measures].[Units Sold])"), 3) → Mountain Bike
> 
> // Worst performing region (last in set)
> CUBERANKEDMEMBER("Geography", CUBESET("Geography", "BottomCount([Region].Members, 10, [Measures].[Profit])"), 1) → Southwest Region
> 
> // 2nd highest customer by lifetime value with custom caption
> CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 20, [Measures].[LTV])"), 2, "Silver Customer") → Silver Customer
> 
> // Dynamic ranking using cell reference for position
> CUBERANKEDMEMBER("Performance", CUBESET("Performance", "[Employee].Members"), A1) → member at rank specified in A1
> ```

## Use Cases

### [[Top performer identification]]
- **Sales leader recognition**: Identify top performers by revenue, units sold, or profit margin for recognition programs and best practice sharing
- **Product ranking analysis**: Determine best-selling products, highest-margin items, or fastest-growing categories for inventory and marketing decisions
- **Customer tier identification**: Rank customers by lifetime value, purchase frequency, or profitability to optimize customer service and retention strategies
- **Regional performance ranking**: Compare territories, districts, or markets to identify successful strategies and areas needing improvement
- **Employee performance evaluation**: Rank staff by productivity metrics, quality scores, or achievement levels for performance reviews and promotions

### [[Competitive analysis]]
- **Market position tracking**: Determine company ranking within industry segments, product categories, or geographic markets
- **Benchmark identification**: Find top performers to use as benchmarks for goal setting and performance improvement initiatives
- **Peer comparison**: Compare performance against similar organizations, departments, or business units
- **Trend analysis**: Track changes in competitive position over time by monitoring ranking shifts across periods
- **Performance gap analysis**: Identify the gap between current performance and top-tier performance for improvement targeting

### [[Exception reporting]]
- **Outlier identification**: Find extreme performers (both high and low) that require special attention or investigation
- **Quality control**: Identify products, processes, or locations with unusual quality metrics that need investigation
- **Risk management**: Highlight highest-risk customers, products, or activities based on various risk metrics
- **Resource allocation**: Identify top opportunities or priorities for resource investment based on performance rankings
- **Alert generation**: Create automated alerts when items move into or out of top/bottom performance tiers

## Related

### Similar Functions

- [[CUBESET]] - Creates the ranked member sets that CUBERANKEDMEMBER extracts individual items from
- [[CUBEVALUE]] - Gets actual values for the ranked members identified by CUBERANKEDMEMBER
- [[CUBESETCOUNT]] - Counts members in the ranked set, useful for validation and percentage calculations
- [[CUBEMEMBER]] - Returns individual members by name, while CUBERANKEDMEMBER returns by ranking position
- [[CUBEKPIMEMBER]] - Returns KPI properties, complementing CUBERANKEDMEMBER for performance analysis

## Ranking Analysis Functions

### [[CUBEVALUE]]
Used with CUBERANKEDMEMBER to retrieve the actual performance values for ranked members, providing complete ranking context with supporting data.

```spreadsheets
// Top performer with performance value
=CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1) & 
 ": " & TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
                     CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 10, [Measures].[Revenue])"), 1)), "$#,##0")
// Example: "John Smith: $245,000"

// Performance gap analysis
="Gap between #1 and #2: " & 
 TEXT(CUBEVALUE("Performance", "[Measures].[Score]", 
              CUBERANKEDMEMBER("Performance", CUBESET("Performance", "[Team].Members"), 1)) - 
     CUBEVALUE("Performance", "[Measures].[Score]", 
              CUBERANKEDMEMBER("Performance", CUBESET("Performance", "[Team].Members"), 2)), "0.0")
// Shows performance difference between top two performers

// Bottom performer improvement opportunity
="Improvement potential: " & 
 TEXT(CUBEVALUE("Quality", "[Measures].[Rating]", 
              CUBERANKEDMEMBER("Quality", CUBESET("Quality", "TopCount([Process].Members, 1, [Measures].[Rating])"), 1)) - 
     CUBEVALUE("Quality", "[Measures].[Rating]", 
              CUBERANKEDMEMBER("Quality", CUBESET("Quality", "BottomCount([Process].Members, 1, [Measures].[Rating])"), 1)), "+0.0")
// Calculates gap between best and worst performers
```

### [[CUBESET]]
Provides the foundation for CUBERANKEDMEMBER by defining the ranked member groups. Different CUBESET expressions create different ranking contexts.

```spreadsheets
// Dynamic top N analysis
=CUBERANKEDMEMBER("Revenue", 
                 CUBESET("Revenue", "TopCount([Product].Members, "&A1&", [Measures].[Sales])"), 
                 B1)
// Where A1 contains the number of top products and B1 contains the rank position

// Filtered ranking within segments
=CUBERANKEDMEMBER("Customer", 
                 CUBESET("Customer", "TopCount(Filter([Customer].Members, [Measures].[Segment] = 'Premium'), 10, [Measures].[Value])"), 
                 1)
// Gets top customer within premium segment only

// Time-based ranking
=CUBERANKEDMEMBER("Trends", 
                 CUBESET("Trends", "TopCount([Product].Members, 5, ([Measures].[Growth %], [Time].[Current Year]))"), 
                 C1)
// Ranks by current year growth rate
```

### [[CUBESETCOUNT]]
Validates ranking operations and provides context about the size of ranked sets. Essential for percentage calculations and ranking validation.

```spreadsheets
// Ranking with context
=CUBERANKEDMEMBER("Team", CUBESET("Team", "[Employee].Members"), 1) & 
 " is #1 of " & CUBESETCOUNT(CUBESET("Team", "[Employee].Members")) & " employees"
// Example: "Sarah Johnson is #1 of 47 employees"

// Percentile ranking
="Rank " & D1 & " of " & CUBESETCOUNT(CUBESET("Market", "[Company].Members")) & 
 " (" & TEXT(D1/CUBESETCOUNT(CUBESET("Market", "[Company].Members")), "0.0%") & " percentile)"
// Shows both absolute and percentile ranking

// Top percentage identification
=IF(E1 <= CUBESETCOUNT(CUBESET("Performance", "[Performer].Members")) * 0.1, 
    "Top 10%: " & CUBERANKEDMEMBER("Performance", CUBESET("Performance", "[Performer].Members"), E1),
    "Below Top 10%")
// Identifies if ranking position is in top decile
```

## Comparison Functions

### [[RANK]]
Compares traditional spreadsheet ranking with cube-based ranking for validation and cross-verification of ranking logic.

```spreadsheets
// Cross-validation of ranking methods
="Cube Rank: " & F1 & " | Spreadsheet Rank: " & 
 RANK(CUBEVALUE("Validation", "[Measures].[Value]", G1), H1:H20, 0)
// Where F1 is cube rank position, G1 is the member, H1:H20 is value array

// Ranking consistency check
=IF(ABS(RANK(CUBEVALUE("Check", "[Measures].[Score]", I1), J1:J50, 0) - K1) <= 1, 
    "Ranking Consistent", "Ranking Discrepancy")
// Where K1 contains cube-based rank for validation

// Performance tier identification using both methods
=IF(RANK(L1, M1:M100, 0) <= 10 AND 
    CUBERANKEDMEMBER("Tier", CUBESET("Tier", "TopCount([Item].Members, 10, [Measures].[Performance])"), RANK(L1, M1:M100, 0)) = N1,
    "Confirmed Top 10", "Ranking needs verification")
// Cross-validates top tier membership
```

### [[PERCENTRANK]]
Provides percentile context for cube rankings, enabling statistical analysis of ranking positions.

```spreadsheets
// Percentile rank of cube-ranked member
=TEXT(PERCENTRANK(P1:P100, 
                 CUBEVALUE("Percentile", "[Measures].[Score]", 
                          CUBERANKEDMEMBER("Percentile", CUBESET("Percentile", "[Competitor].Members"), Q1))), "0.0%") & 
 " percentile rank"
// Shows percentile position of ranked member

// Performance distribution analysis
="Position " & Q1 & " represents " & 
 TEXT(PERCENTRANK(R1:R200, 
                 CUBEVALUE("Distribution", "[Measures].[Value]", 
                          CUBERANKEDMEMBER("Distribution", CUBESET("Distribution", "[Entity].Members"), Q1))), "0.0%") & 
 " of all performers"
// Contextualizes ranking within overall distribution

// Quartile identification
=CHOOSE(MIN(ROUNDUP(PERCENTRANK(S1:S150, 
                               CUBEVALUE("Quartile", "[Measures].[Rating]", 
                                        CUBERANKEDMEMBER("Quartile", CUBESET("Quartile", "[Unit].Members"), T1))) * 4, 0), 4),
        "Bottom Quartile", "Second Quartile", "Third Quartile", "Top Quartile")
// Assigns quartile labels based on percentile rank
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional ranking analysis, tier identification, and dynamic ranking interpretation based on business rules.

```spreadsheets
// Dynamic ranking tier assignment
=IF(U1 <= 3, "Gold Tier: " & CUBERANKEDMEMBER("Tier", CUBESET("Tier", "[Member].Members"), U1),
    IF(U1 <= 10, "Silver Tier: " & CUBERANKEDMEMBER("Tier", CUBESET("Tier", "[Member].Members"), U1),
       "Bronze Tier: " & CUBERANKEDMEMBER("Tier", CUBESET("Tier", "[Member].Members"), U1)))
// Assigns performance tiers based on ranking position

// Ranking trend analysis
=IF(CUBERANKEDMEMBER("Trend", CUBESET("Trend", "[Performer].Members"), V1) = W1, 
    "Maintained Position",
    IF(CUBERANKEDMEMBER("Trend", CUBESET("Trend", "[Performer].Members"), V1) < W1, 
       "Improved " & (W1 - CUBERANKEDMEMBER("Trend", CUBESET("Trend", "[Performer].Members"), V1)) & " positions",
       "Dropped " & (CUBERANKEDMEMBER("Trend", CUBESET("Trend", "[Performer].Members"), V1) - W1) & " positions"))
// Where W1 is previous period rank

// Performance alert based on ranking
=IF(CUBERANKEDMEMBER("Alert", CUBESET("Alert", "BottomCount([Department].Members, 5, [Measures].[Performance])"), 1) = X1,
    "ALERT: " & X1 & " is lowest performing department",
    IF(CUBERANKEDMEMBER("Alert", CUBESET("Alert", "TopCount([Department].Members, 3, [Measures].[Performance])"), 1) = X1,
       "RECOGNITION: " & X1 & " is top performing department",
       "Standard Performance"))
// Generates alerts for extreme performers
```

## Commonly Used With Functions Examples

### Sales Leaderboard
```spreadsheets
// Complete sales ranking with performance details
=CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 20, [Measures].[Revenue])"), A1) & 
 " - #" & A1 & " with " & 
 TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
               CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 20, [Measures].[Revenue])"), A1)), "$#,##0") & 
 " (" & TEXT(CUBEVALUE("Sales", "[Measures].[Revenue]", 
                     CUBERANKEDMEMBER("Sales", CUBESET("Sales", "TopCount([Salesperson].Members, 20, [Measures].[Revenue])"), A1)) / 
             CUBEVALUE("Sales", "[Measures].[Total Revenue]"), "0.0%") & " of total)"
// Example: "John Smith - #1 with $245,000 (18.7% of total)"
```

### Product Performance Matrix
```spreadsheets
// Product ranking with category context
=CUBERANKEDMEMBER("Products", CUBESET("Products", "TopCount([Product].Members, 10, [Measures].[Profit])"), B1) & 
 " (Category: " & CUBEVALUE("Products", "[Measures].[Category]", 
                           CUBERANKEDMEMBER("Products", CUBESET("Products", "TopCount([Product].Members, 10, [Measures].[Profit])"), B1)) & 
 ", Rank #" & B1 & " overall, #" & 
 CUBERANKEDMEMBER("Category", CUBESET("Category", "TopCount(Filter([Product].Members, [Measures].[Category] = '" & 
                                     CUBEVALUE("Products", "[Measures].[Category]", 
                                              CUBERANKEDMEMBER("Products", CUBESET("Products", "TopCount([Product].Members, 10, [Measures].[Profit])"), B1)) & 
                                     "'), 5, [Measures].[Profit])"), 1) & " in category)"
// Example: "Mountain Bike Pro (Category: Bikes, Rank #3 overall, #1 in category)"
```

### Customer Tier Analysis
```spreadsheets
// Customer ranking with tier assignment and value analysis
=IF(C1 <= 5, 
    "🥇 VIP: " & CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 100, [Measures].[LTV])"), C1) & 
    " (LTV: " & TEXT(CUBEVALUE("Customer", "[Measures].[LTV]", 
                             CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 100, [Measures].[LTV])"), C1)), "$#,##0") & 
    ", " & TEXT(C1/CUBESETCOUNT(CUBESET("Customer", "TopCount([Customer].Members, 100, [Measures].[LTV])")), "0.0%") & " percentile)",
    IF(C1 <= 20, "🥈 Premium: " & CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 100, [Measures].[LTV])"), C1),
       "🥉 Standard: " & CUBERANKEDMEMBER("Customer", CUBESET("Customer", "TopCount([Customer].Members, 100, [Measures].[LTV])"), C1)))
// Example: "🥇 VIP: ABC Corporation (LTV: $45,200, 5.0% percentile)"
```

### Regional Performance Dashboard
```spreadsheets
// Regional ranking with growth trend analysis
=CUBERANKEDMEMBER("Regional", CUBESET("Regional", "[Geography].[Region].Members"), D1) & 
 " ranks #" & D1 & " (" & 
 TEXT(CUBEVALUE("Regional", "[Measures].[Revenue]", 
               CUBERANKEDMEMBER("Regional", CUBESET("Regional", "[Geography].[Region].Members"), D1)), "$#,##0K") & " revenue, " &
 TEXT(CUBEVALUE("Regional", "[Measures].[Growth %]", 
               CUBERANKEDMEMBER("Regional", CUBESET("Regional", "[Geography].[Region].Members"), D1)), "+0.0%;-0.0%") & " growth) - " &
 IF(CUBEVALUE("Regional", "[Measures].[Growth %]", 
             CUBERANKEDMEMBER("Regional", CUBESET("Regional", "[Geography].[Region].Members"), D1)) > 
   CUBEVALUE("Regional", "[Measures].[Avg Growth %]"), 
   "Above Average", "Below Average") & " vs company avg"
// Example: "West Region ranks #2 ($1,250K revenue, +12.5% growth) - Above Average vs company avg"
```

### Competitive Benchmarking
```spreadsheets
// Market position analysis with benchmarking
=CONCATENATE(
  "Market Position: #", E1, " of ", CUBESETCOUNT(CUBESET("Market", "[Competitor].Members")), " competitors | ",
  "Leader: ", CUBERANKEDMEMBER("Market", CUBESET("Market", "TopCount([Competitor].Members, 1, [Measures].[Market Share])"), 1), 
  " (", TEXT(CUBEVALUE("Market", "[Measures].[Market Share]", 
                     CUBERANKEDMEMBER("Market", CUBESET("Market", "TopCount([Competitor].Members, 1, [Measures].[Market Share])"), 1)), "0.0%"), ") | ",
  "Gap to Leader: ", 
  TEXT(CUBEVALUE("Market", "[Measures].[Market Share]", 
                CUBERANKEDMEMBER("Market", CUBESET("Market", "TopCount([Competitor].Members, 1, [Measures].[Market Share])"), 1)) - 
      CUBEVALUE("Market", "[Measures].[Market Share]", "[Competitor].[Us]"), "+0.0%;-0.0%"))
// Example: "Market Position: #3 of 12 competitors | Leader: CompanyX (35.2%) | Gap to Leader: -8.7%"
```
