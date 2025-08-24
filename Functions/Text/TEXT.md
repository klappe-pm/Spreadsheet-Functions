---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- text
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- text
- excel
- sheets
---
# TEXT

## TEXT Description

Converts numbers, dates, and times into formatted text strings using custom format codes. Essential for controlling the display of numeric data, creating readable reports, and preparing data for export and concatenation operations.

> [!f(x)] TEXT Syntax
>
> ```spreadsheets
> TEXT(value, format_text)
> ```
>
> **Parameters:**
> - `value` (required): The numeric value, date, or time to format
> - `format_text` (required): The format code string that specifies how to display the value

> [!f(x)] TEXT Examples
>
> ```spreadsheets
> // Format currency with commas and decimals
> TEXT(1234.56, "$#,##0.00") → "$1,234.56"
> 
> // Format percentage with one decimal place
> TEXT(0.1234, "0.0%") → "12.3%"
> 
> // Format date as month/day/year
> TEXT(DATE(2024,3,15), "mm/dd/yyyy") → "03/15/2024"
> 
> // Format large numbers with abbreviation
> TEXT(1500000, "#,##0,,") → "2" (millions)
> 
> // Format time as 12-hour with AM/PM
> TEXT(TIME(14,30,0), "h:mm AM/PM") → "2:30 PM"
> 
> // Format number with leading zeros
> TEXT(123, "00000") → "00123"
> ```

## Use Cases

### [[Financial reporting and analysis]]
- **Currency formatting**: Display monetary values with proper currency symbols, thousand separators, and decimal precision for financial statements
- **Percentage displays**: Format ratio calculations as readable percentages with appropriate decimal places for performance metrics
- **Accounting formats**: Create negative number displays with parentheses and red formatting for accounting standards compliance
- **Financial ratios**: Format complex calculations into readable text for investor reports and financial analysis dashboards

### [[Date and time presentation]]
- **Report date stamps**: Format current dates in various styles for report headers, file names, and documentation timestamps
- **Timeline formatting**: Display project dates in consistent formats for Gantt charts, schedules, and milestone tracking
- **Time logging**: Format elapsed time calculations in hours:minutes format for timesheet reporting and project billing
- **Regional date formats**: Convert dates to locale-specific formats for international reporting and data exchange

### [[Data export preparation]]
- **CSV formatting**: Convert numeric data to text format to prevent scientific notation in exported spreadsheet files
- **System integration**: Format numbers as text with specific patterns required by external systems and APIs
- **Report generation**: Create formatted text strings for automated report generation and document template population
- **Barcode preparation**: Format numeric codes with specific digit patterns required for barcode generation and inventory systems

## Related

### Similar Functions

- [[VALUE]] - Converts text that represents numbers back to numeric values, opposite of TEXT function
- [[FORMAT]] - Alternative function for number formatting in some spreadsheet applications
- [[FIXED]] - Rounds numbers to specified decimal places and formats as text, simpler alternative to TEXT
- [[DOLLAR]] - Specifically formats numbers as currency text, specialized version of TEXT for monetary values
- [[CONCATENATE]] - Combines TEXT results with other strings for complex formatted output

## Number Formatting Functions

### [[CONCATENATE]]
Essential partnership for building complex formatted strings. TEXT handles the number formatting while CONCATENATE assembles the complete text output with labels, separators, and additional context.

```spreadsheets
// Build formatted financial summary
=CONCATENATE("Revenue: ", TEXT(A1, "$#,##0"), " | Expenses: ", TEXT(B1, "$#,##0"), " | Profit: ", TEXT(A1-B1, "$#,##0"))
// Example: "Revenue: $50,000 | Expenses: $35,000 | Profit: $15,000"

// Create progress report with percentages
=CONCATENATE("Project completion: ", TEXT(C1/C2, "0%"), " (", TEXT(C1, "#,##0"), " of ", TEXT(C2, "#,##0"), " tasks)")
// Example: "Project completion: 75% (150 of 200 tasks)"

// Format date range for reports
=CONCATENATE("Report Period: ", TEXT(D1, "mmmm d, yyyy"), " - ", TEXT(E1, "mmmm d, yyyy"))
// Example: "Report Period: March 1, 2024 - March 31, 2024"
```

### [[IF]]
Critical for conditional formatting and handling edge cases. IF enables TEXT to apply different formatting based on value conditions and handle null or error values gracefully.

```spreadsheets
// Conditional currency formatting for positive/negative
=IF(A1>=0, TEXT(A1, "$#,##0.00"), "(" & TEXT(ABS(A1), "$#,##0.00") & ")")
// Shows positive as $1,234.56 and negative as ($1,234.56)

// Format based on magnitude
=IF(B1>=1000000, TEXT(B1, "$#,##0.0,,") & "M", TEXT(B1, "$#,##0"))
// Shows millions as $1.2M, smaller amounts as $50,000

// Date formatting with validation
=IF(ISNUMBER(C1), TEXT(C1, "mm/dd/yyyy"), "Invalid date")
// Only formats valid dates, shows error message otherwise
```

## String Processing Functions

### [[VALUE]]
Works opposite to TEXT, converting formatted text back to numbers. Together they enable round-trip formatting and data type conversions for import/export operations.

```spreadsheets
// Convert formatted currency back to number
=VALUE(SUBSTITUTE(TEXT(A1, "$#,##0.00"), "$", ""))
// Formats as currency, then converts back to numeric value

// Round-trip percentage formatting
=VALUE(SUBSTITUTE(TEXT(B1, "0.0%"), "%", ""))/100
// Formats as percentage text, then converts back to decimal

// Clean and reformat numbers
=TEXT(VALUE(SUBSTITUTE(SUBSTITUTE(C1, ",", ""), "$", "")), "#,##0.00")
// Strips formatting, converts to number, reformats consistently
```

### [[FIND]]
Combines with TEXT for position-based formatting and parsing formatted text strings. FIND locates specific characters in TEXT-formatted strings for extraction and validation.

```spreadsheets
// Extract currency amount from formatted text
=VALUE(MID(TEXT(A1, "$#,##0.00"), 2, LEN(TEXT(A1, "$#,##0.00"))-1))
// Formats number, then extracts numeric portion

// Parse formatted date components
=VALUE(LEFT(TEXT(B1, "mm/dd/yyyy"), 2))
// Formats date, extracts month as number

// Find decimal position in formatted number
=FIND(".", TEXT(C1, "#,##0.00"))
// Locates decimal point in formatted number string
```

## Commonly Used With Functions Examples

### Financial Dashboard Creation
```spreadsheets
// Create comprehensive financial display from raw numbers
// A1=Revenue, B1=Expenses, C1=Profit, D1=ProfitMargin

// Executive summary with multiple formats
=CONCATENATE("Q1 Results: Revenue ", TEXT(A1, "$#,##0.0,"), "K, Expenses ", TEXT(B1, "$#,##0.0,"), "K, Profit ", TEXT(C1, "$#,##0.0,"), "K (", TEXT(D1, "0.0%"), " margin)")
// Result: "Q1 Results: Revenue $125.5K, Expenses $89.2K, Profit $36.3K (29.0% margin)"

// Variance analysis with conditional formatting
=CONCATENATE("Profit vs Target: ", IF(C1>=E1, "✓ ", "⚠ "), TEXT(C1, "$#,##0"), " vs ", TEXT(E1, "$#,##0"), " (", IF(C1>=E1, "+", ""), TEXT((C1-E1)/E1, "0.0%"), ")")
// Result: "Profit vs Target: ✓ $36,300 vs $30,000 (+21.0%)"

// Multi-period comparison
=CONCATENATE(TEXT(F1, "mmm"), ": ", TEXT(G1, "$#,##0"), " | ", TEXT(H1, "mmm"), ": ", TEXT(I1, "$#,##0"), " | Change: ", TEXT((I1-G1)/G1, "+0.0%;-0.0%"))
// Result: "Mar: $36,300 | Feb: $31,200 | Change: +16.3%"
```

### Project Management Reporting
```spreadsheets
// Generate project status reports with dates and percentages
// J1=StartDate, K1=EndDate, L1=TasksCompleted, M1=TotalTasks, N1=Budget, O1=Spent

// Project timeline summary
=CONCATENATE("Project Duration: ", TEXT(J1, "mmm d"), " - ", TEXT(K1, "mmm d"), " (", TEXT(K1-J1, "0"), " days)")
// Result: "Project Duration: Mar 1 - Apr 15 (45 days)"

// Progress indicator with visual elements
=CONCATENATE("Progress: ", TEXT(L1/M1, "0%"), " complete (", TEXT(L1, "#,##0"), "/", TEXT(M1, "#,##0"), " tasks) ", IF(L1/M1>=0.5, "🟢", IF(L1/M1>=0.25, "🟡", "🔴")))
// Result: "Progress: 75% complete (150/200 tasks) 🟢"

// Budget status with remaining calculations
=CONCATENATE("Budget: ", TEXT(O1, "$#,##0"), " spent of ", TEXT(N1, "$#,##0"), " (", TEXT(O1/N1, "0.0%"), " used, ", TEXT(N1-O1, "$#,##0"), " remaining)")
// Result: "Budget: $45,000 spent of $60,000 (75.0% used, $15,000 remaining)"
```

### Sales Performance Dashboard
```spreadsheets
// Build comprehensive sales metrics display
// P1=CurrentSales, Q1=Target, R1=LastYear, S1=Quota, T1=Commission

// Sales achievement summary
=CONCATENATE("Sales: ", TEXT(P1, "$#,##0.0,"), "K vs ", TEXT(Q1, "$#,##0.0,"), "K target (", TEXT(P1/Q1, "0%"), " achieved)")
// Result: "Sales: $127.5K vs $120.0K target (106% achieved)"

// Year-over-year comparison
=CONCATENATE("YoY Growth: ", TEXT(P1, "$#,##0"), " vs ", TEXT(R1, "$#,##0"), " last year (", IF(P1>R1, "+", ""), TEXT((P1-R1)/R1, "0.0%"), " change)")
// Result: "YoY Growth: $127,500 vs $115,200 last year (+10.7% change)"

// Commission calculation with tiers
=CONCATENATE("Commission: ", IF(P1>=S1, TEXT(T1*1.2, "$#,##0"), TEXT(T1, "$#,##0")), " (", IF(P1>=S1, "Bonus tier", "Standard rate"), " - ", TEXT(T1/P1, "0.0%"), " of sales)")
// Result: "Commission: $7,650 (Bonus tier - 6.0% of sales)"
```

### Data Export Formatting System
```spreadsheets
// Prepare data for export with consistent formatting
// U1=ID, V1=Name, W1=Amount, X1=Date, Y1=Status

// Create CSV-ready formatted record
=CONCATENATE(TEXT(U1, "00000"), ",", SUBSTITUTE(V1, ",", " "), ",", TEXT(W1, "0.00"), ",", TEXT(X1, "yyyy-mm-dd"), ",", Y1)
// Result: "00123,John Smith,$1234.56,2024-03-15,Active"

// Generate fixed-width export format
=CONCATENATE(TEXT(U1, "00000"), " ", LEFT(V1&REPT(" ", 20), 20), " ", TEXT(W1, "000000.00"), " ", TEXT(X1, "mm/dd/yyyy"), " ", Y1)
// Result: "00123 John Smith          001234.56 03/15/2024 Active"

// Create JSON-formatted data string
=CONCATENATE("{""id"":", TEXT(U1, "0"), ",""name"":""", V1, """,""amount"":", TEXT(W1, "0.00"), ",""date"":""", TEXT(X1, "yyyy-mm-dd"), """,""status"":""", Y1, """}")
// Result: {"id":123,"name":"John Smith","amount":1234.56,"date":"2024-03-15","status":"Active"}
```

### International Reporting System
```spreadsheets
// Handle multiple currencies and date formats
// Z1=Amount, AA1=ExchangeRate, BB1=Date, CC1=Region

// Multi-currency display with exchange rates
=CONCATENATE("USD: ", TEXT(Z1, "$#,##0.00"), " | EUR: ", TEXT(Z1*AA1, "€#,##0.00"), " (Rate: ", TEXT(AA1, "0.0000"), ")")
// Result: "USD: $1,234.56 | EUR: €1,111.10 (Rate: 0.9000)"

// Regional date formatting
=IF(CC1="US", TEXT(BB1, "mm/dd/yyyy"), IF(CC1="EU", TEXT(BB1, "dd/mm/yyyy"), TEXT(BB1, "yyyy-mm-dd")))
// Result: "03/15/2024" for US, "15/03/2024" for EU, "2024-03-15" for others

// Time zone adjusted display
=CONCATENATE("Local: ", TEXT(BB1, "mm/dd/yyyy h:mm"), " | UTC: ", TEXT(BB1-TIME(CC1,0,0), "mm/dd/yyyy h:mm"), " | Timezone: UTC", IF(CC1>=0, "+", ""), TEXT(CC1, "0"))
// Result: "Local: 03/15/2024 14:30 | UTC: 03/15/2024 19:30 | Timezone: UTC+5"
```
