---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - math & trig
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
# AGGREGATE

## AGGREGATE Description

Performs aggregate calculations while automatically ignoring hidden rows, filtered data, and error values. Provides 19 different statistical and mathematical functions with built-in error handling and data filtering capabilities, making it ideal for dynamic reports and filtered datasets.

> [!f(x)] AGGREGATE Syntax
>
> ```spreadsheets
> AGGREGATE(function_num, options, array)
> AGGREGATE(function_num, options, array, [k])
> ```
>
> **Parameters:**
> - `function_num` (required): Number 1-19 specifying which function to perform (AVERAGE, COUNT, MAX, MIN, etc.)
> - `options` (required): Number 0-7 specifying what to ignore (errors, hidden rows, nested subtotals)
> - `array` (required): Range or array to perform the function on
> - `k` (optional): Required for functions 14-19, specifies the k-th value to return

> [!f(x)] AGGREGATE Examples
>
> ```spreadsheets
> // Basic average ignoring errors
> AGGREGATE(1, 6, A1:A10) → average of visible cells, ignoring errors
> 
> // Count visible non-empty cells
> AGGREGATE(2, 5, B1:B20) → counts visible cells only
> 
> // Maximum value ignoring hidden rows and errors
> AGGREGATE(4, 7, C1:C15) → max value from visible, error-free cells
> 
> // Find 2nd largest value
> AGGREGATE(14, 6, D1:D25, 2) → second largest value ignoring errors
> 
> // Sum ignoring nested SUBTOTAL functions
> AGGREGATE(9, 2, E1:E30) → sum excluding nested subtotals
> ```

## Use Cases

### [[Dynamic reporting]]
- **Dashboard calculations**: Create reports that automatically adjust when data is filtered or hidden
- **Executive summaries**: Generate accurate totals and averages that ignore filtered-out divisions or time periods
- **Performance metrics**: Calculate KPIs that remain accurate regardless of applied filters or data visibility
- **Automated analytics**: Build self-updating reports that handle missing data and errors gracefully

### [[Data analysis with filters]]  
- **Filtered dataset analysis**: Perform statistical analysis on filtered data without creating helper columns
- **Outlier exclusion**: Calculate statistics while automatically excluding error values and outliers
- **Conditional reporting**: Generate reports that adapt to user-applied filters and data visibility settings
- **Multi-level analysis**: Analyze data at different aggregation levels while maintaining calculation accuracy

### [[Error-resistant calculations]]
- **Robust statistical analysis**: Calculate statistics that automatically handle missing data and calculation errors
- **Quality assurance**: Perform calculations that ignore data quality issues while maintaining analytical integrity
- **Production reporting**: Generate reliable reports that function correctly even with incomplete or problematic data
- **Automated data validation**: Create validation rules that work regardless of data filtering or error conditions

## Related

### Similar Functions

- [[SUBTOTAL]] - Performs calculations on visible cells only, but limited to 11 functions
- [[AVERAGE]] - Basic average calculation without advanced filtering options
- [[SUM]] - Basic summation without error handling or filtering capabilities  
- [[MAX]] - Finds maximum value but doesn't handle errors or hidden data automatically
- [[MIN]] - Finds minimum value without built-in filtering and error handling

## Statistical Functions

### [[SUBTOTAL]]
AGGREGATE extends SUBTOTAL functionality with more functions and better error handling, making it the preferred choice for advanced filtering scenarios.

```spreadsheets
// SUBTOTAL equivalent using AGGREGATE
=SUBTOTAL(1, A1:A10)  // Old way: average of visible cells
=AGGREGATE(1, 5, A1:A10)  // New way: same result with more options

// Enhanced error handling
=AGGREGATE(1, 6, B1:B20)  // Average ignoring both hidden rows and errors
=SUBTOTAL(1, B1:B20)  // Would fail if errors present

// Advanced statistical functions not available in SUBTOTAL
=AGGREGATE(12, 6, C1:C30)  // Median of visible, error-free cells
=AGGREGATE(15, 5, D1:D40, 3)  // Third smallest value, ignoring hidden rows
```

### [[AVERAGE]]
AGGREGATE provides error-resistant averaging with automatic filtering, superior to basic AVERAGE for real-world data analysis.

```spreadsheets
// Basic vs. robust averaging
=AVERAGE(E1:E25)  // Fails if any errors present
=AGGREGATE(1, 6, E1:E25)  // Automatically handles errors and hidden rows

// Filtered data analysis
=AVERAGE(F1:F50)  // Includes hidden/filtered data
=AGGREGATE(1, 5, F1:F50)  // Only visible data

// Combined with data validation
=IF(AGGREGATE(2, 5, G1:G20)>=10, AGGREGATE(1, 5, G1:G20), "Insufficient data")
// Only calculates average if enough visible data points exist
```

## Lookup and Analysis Functions

### [[LARGE]]
AGGREGATE includes LARGE functionality (function 14) with added filtering and error handling capabilities.

```spreadsheets
// Find largest values with error protection
=LARGE(H1:H30, 1)  // Fails if errors present
=AGGREGATE(14, 6, H1:H30, 1)  // Largest value ignoring errors

// Dynamic top-N analysis
=AGGREGATE(14, 5, I1:I100, ROW(A1))  // Create dynamic ranking list
// Drag down to get 1st, 2nd, 3rd largest from visible data

// Percentile analysis
=AGGREGATE(14, 6, J1:J200, INT(COUNT(J1:J200)*0.9))  // 90th percentile
// Robust percentile calculation with error handling
```

### [[SMALL]]
AGGREGATE includes SMALL functionality (function 15) with enhanced data filtering and error resistance.

```spreadsheets
// Find smallest values with filtering
=SMALL(K1:K40, 1)  // Basic smallest value
=AGGREGATE(15, 7, K1:K40, 1)  // Smallest value ignoring errors and hidden rows

// Bottom quartile analysis
=AGGREGATE(15, 6, L1:L80, INT(AGGREGATE(2,6,L1:L80)*0.25))  
// 25th percentile with error handling

// Quality control analysis
=AGGREGATE(15, 5, M1:M60, 3)  // Third lowest value from visible data
// Useful for identifying consistent low performers
```

## Conditional Logic Functions

### [[IF]]
Essential for controlling AGGREGATE execution and handling edge cases in dynamic reporting scenarios.

```spreadsheets
// Conditional aggregation with data validation
=IF(AGGREGATE(2,5,N1:N50)>=5, AGGREGATE(1,5,N1:N50), "Need more data")
// Only calculates average if sufficient visible data

// Multi-level conditional analysis
=IF(AGGREGATE(14,6,O1:O30,1)>1000, "High performance", "Review needed")
// Performance categorization based on maximum values

// Error-resistant conditional reporting
=IF(ISERROR(AGGREGATE(1,6,P1:P25)), "Data issues", AGGREGATE(1,6,P1:P25))
// Provides user-friendly error messages
```

## Commonly Used With Functions Examples

### Dynamic Dashboard Creation
```spreadsheets
// Complete dashboard metric with error handling
="Average: " & ROUND(AGGREGATE(1,6,A:A),2) & " | Max: " & AGGREGATE(4,6,A:A) & " | Count: " & AGGREGATE(2,5,A:A)

// Performance ranking with filtering
="Top performer: " & INDEX(B:B, MATCH(AGGREGATE(14,5,C:C,1), C:C, 0)) & " (" & AGGREGATE(14,5,C:C,1) & ")"

// Trend analysis with statistical validation
=IF(AGGREGATE(2,5,D:D)>=12, "Trend: " & IF(AGGREGATE(14,5,D:D,1)>AGGREGATE(15,5,D:D,1)*2, "Volatile", "Stable"), "Insufficient data")
```

### Quality Control and Analysis
```spreadsheets
// Multi-criteria quality assessment
="Quality Score: " & AGGREGATE(1,6,E:E) & "/10 (Range: " & AGGREGATE(15,6,E:E,1) & "-" & AGGREGATE(14,6,E:E,1) & ")"

// Outlier detection with statistical thresholds
=IF(AGGREGATE(14,6,F:F,1)>AGGREGATE(1,6,F:F)+2*AGGREGATE(7,6,F:F), "Outliers detected", "Normal distribution")

// Process control with automated limits
="Control: " & IF(AND(AGGREGATE(4,6,G:G)<H1, AGGREGATE(3,6,G:G)>H2), "In control", "Out of spec")
```

### Filtered Data Reporting
```spreadsheets
// Comprehensive filtered summary
="Visible data summary: " & AGGREGATE(2,5,I:I) & " records, Avg: " & ROUND(AGGREGATE(1,5,I:I),2) & ", Total: " & AGGREGATE(9,5,J:J)

// Dynamic percentile analysis
="P90: " & AGGREGATE(14,5,K:K,MAX(1,INT(AGGREGATE(2,5,K:K)*0.1))) & " | P10: " & AGGREGATE(15,5,K:K,MAX(1,INT(AGGREGATE(2,5,K:K)*0.9)))

// Error-resistant team performance
="Team stats (errors ignored): Members: " & AGGREGATE(2,6,L:L) & ", Avg score: " & ROUND(AGGREGATE(1,6,M:M),1) & ", Top: " & AGGREGATE(14,6,M:M,1)
```
