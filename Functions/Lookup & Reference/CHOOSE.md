---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- lookup reference
- excel
- sheets
---
# CHOOSE

## CHOOSE Description

Returns a value from a list of values based on a position number. Simpler alternative to complex nested IF statements when selecting from a known set of options. The position number determines which value from the list to return.

> [!f(x)] CHOOSE Syntax
>
> ```spreadsheets
> CHOOSE(index_num, value1, [value2], [value3], ...)
> ```
>
> **Parameters:**
> - `index_num` (required): Position number (1-254) indicating which value to return
> - `value1, value2, ...` (required): List of values to choose from (up to 254 values)

> [!f(x)] CHOOSE Examples
>
> ```spreadsheets
> // Select month name by number
> CHOOSE(3, "Jan", "Feb", "Mar", "Apr") → "Mar"
> 
> // Dynamic pricing by customer tier
> CHOOSE(CustomerTier, 100, 85, 70, 60) → returns price based on tier
> 
> // Select formula result by condition
> CHOOSE(WEEKDAY(TODAY()), "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
> 
> // Choose calculation method
> CHOOSE(CalcType, SUM(A:A), AVERAGE(A:A), MAX(A:A)) → different calculations
> 
> // Select range by user input
> SUM(CHOOSE(RangeNum, A1:A10, B1:B10, C1:C10)) → sum different columns
> ```

## Use Cases

### [[Conditional selections]]
- **Menu-driven calculations**: Allow users to select calculation types through dropdown menus or input values
- **Tiered pricing systems**: Apply different prices, discounts, or rates based on customer categories or volume tiers
- **Status-based formatting**: Display different text, colors, or formats based on status codes or condition numbers
- **Multi-option reporting**: Generate different report sections or data views based on user selections

### [[Data transformation]]  
- **Code translation**: Convert numeric codes to meaningful text descriptions or categories
- **Lookup alternatives**: Replace complex VLOOKUP operations when working with short, known lists
- **Dynamic range selection**: Choose different data ranges for analysis based on calculated or user-specified criteria
- **Formula routing**: Direct calculations through different formula paths based on business rules

### [[User interface enhancement]]
- **Dynamic dropdown results**: Show different results based on primary dropdown selections in cascading menus
- **Interactive dashboards**: Change dashboard content based on user selections or filter criteria
- **Form logic**: Display different form sections or validation rules based on user choices
- **Report customization**: Allow users to select different report formats, time periods, or data groupings

## Related

### Similar Functions

- [[INDEX]] - Returns values from ranges by position, more flexible for large datasets
- [[VLOOKUP]] - Searches for values in tables, better for unknown or large lists
- [[IF]] - Handles conditional logic but becomes complex with multiple conditions
- [[SWITCH]] - Modern alternative with more flexible syntax (Excel 365)
- [[IFS]] - Multiple IF conditions in single function (Excel 365)

## Commonly Used With Functions Examples

### Dynamic Report Generation
```spreadsheets
// Comprehensive reporting based on period selection
=CONCATENATE(
   "Report for ", CHOOSE(Period, "Daily", "Weekly", "Monthly", "Quarterly"), 
   ": $", 
   CHOOSE(Period, 
          SUM(DailyData), 
          SUM(WeeklyData), 
          SUM(MonthlyData), 
          SUM(QuarterlyData)))
// Generates period-specific reports with appropriate data
```

### Customer Tier Pricing System
```spreadsheets
// Multi-factor pricing calculation
=CHOOSE(CustomerLevel, BasePrice, BasePrice*0.9, BasePrice*0.8, BasePrice*0.7) * 
 CHOOSE(VolumeDiscount, 1, 0.95, 0.9, 0.85)
// Applies both customer level and volume discounts
```

### Performance Status Dashboard
```spreadsheets
// Status-based performance display
=CONCATENATE(
   "Performance: ", 
   CHOOSE(PerformanceLevel, 
          "⭕ Critical", 
          "🔶 Warning", 
          "✅ Good", 
          "🌟 Excellent"), 
   " (Score: ", Score, ")")
// Shows status with appropriate emoji and score
```

### Dynamic Chart Data Selection
```spreadsheets
// Interactive chart data source
=CHOOSE(ChartType, 
        Revenue, 
        Profit, 
        Units, 
        CONCATENATE("Revenue: $", Revenue, " | Profit: $", Profit))
// Different data series based on chart type selection
```

### Multi-Language Interface
```spreadsheets
// Language-specific text display
=CHOOSE(LanguageCode, 
        "Welcome", 
        "Bienvenido", 
        "Bienvenue", 
        "Willkommen", 
        "Benvenuto")
// Shows welcome message in selected language
```
