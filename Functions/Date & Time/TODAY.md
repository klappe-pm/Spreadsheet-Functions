---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- datetime
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- datetime
- excel
- sheets
---
# TODAY

## TODAY Description

Returns the current system date as a serial date value that automatically updates when the spreadsheet recalculates. Essential for time-sensitive calculations, aging analysis, and dynamic date references.

> [!f(x)] TODAY Syntax
>
> ```spreadsheets
> TODAY()
> ```
>
> **Parameters:**
> - No parameters required - automatically retrieves current system date

> [!f(x)] TODAY Examples
>
> ```spreadsheets
> // Current date reference
> TODAY() → December 19, 2024 (updates daily)
> 
> // Days since specific date
> TODAY() - DATE(2024, 1, 1) → 353 (days since January 1, 2024)
> 
> // Age calculation from birth date
> DATEDIF(A1, TODAY(), "Y") → calculates age in years from birth date in A1
> 
> // Report date stamp
> "Report generated: " & TEXT(TODAY(), "mmmm d, yyyy") → "Report generated: December 19, 2024"
> 
> // Business day check
> IF(WEEKDAY(TODAY())>1, IF(WEEKDAY(TODAY())<7, "Business Day", "Weekend"), "Weekend") → determines if today is a business day
> ```

## Use Cases

### [[Aging analysis]]
- **Account receivables tracking**: Calculate days overdue by comparing invoice dates to TODAY() to prioritize collection efforts and identify at-risk accounts
- **Inventory age monitoring**: Determine product shelf life by comparing stock arrival dates to TODAY() for rotation scheduling and expiration management
- **Project timeline analysis**: Track project delays by comparing planned completion dates to TODAY() to identify critical path issues and resource reallocation needs
- **Employee tenure calculations**: Measure service length by comparing hire dates to TODAY() for anniversary recognition and benefit vesting schedules

### [[Dynamic reporting]]
- **Real-time dashboard creation**: Generate current date headers using TODAY() in reports that automatically update without manual intervention for daily operations
- **Performance period tracking**: Calculate month-to-date, quarter-to-date, and year-to-date metrics using TODAY() as the end point for rolling performance analysis
- **Compliance deadline monitoring**: Track regulatory filing deadlines by comparing due dates to TODAY() for proactive compliance management
- **Contract status updates**: Monitor contract expiration and renewal dates using TODAY() to trigger automatic alerts and action items

### [[Time-sensitive calculations]]
- **Interest accrual tracking**: Calculate daily interest accumulation from start dates to TODAY() for loan servicing and investment portfolio management
- **Warranty period validation**: Determine remaining warranty coverage by comparing purchase dates to TODAY() for customer service and replacement scheduling  
- **Subscription lifecycle management**: Track subscription start dates against TODAY() to calculate billing cycles, renewal dates, and churn analysis
- **Service level agreement monitoring**: Measure response times by comparing ticket creation dates to TODAY() for SLA compliance and performance metrics

## Related

### Similar Functions

- [[NOW]] - Returns current date and time, while TODAY only returns date portion without time
- [[DATE]] - Creates specific dates from components, while TODAY always returns current system date
- [[DATEVALUE]] - Converts text dates to serial values, complementing TODAY's direct system date access
- [[DAYS]] - Calculates differences between dates, often used with TODAY as reference point
- [[EDATE]] - Adds months to dates, commonly combined with TODAY for future date calculations

## Current Date Functions

### [[NOW]]
Provides current date and time while TODAY only returns date, both essential for different temporal tracking needs. NOW includes time precision for detailed timestamps and hourly calculations.

```spreadsheets
// Compare date vs datetime functions
=TODAY() → December 19, 2024 (date only)
=NOW() → December 19, 2024 3:45:30 PM (date and time)

// Time-sensitive aging with precision
=NOW() - A1 → exact hours/minutes since datetime in A1
=TODAY() - A1 → whole days since date in A1

// Business hours calculation
=IF(HOUR(NOW())>=9, IF(HOUR(NOW())<17, "Business Hours", "After Hours"), "Before Hours")
// Uses NOW() for hour-specific logic that TODAY() cannot provide
```

### [[YEAR]]
Extracts year component from TODAY results, essential for year-based filtering and fiscal period calculations using current date as reference point.

```spreadsheets
// Current fiscal year calculation
=IF(MONTH(TODAY())>=7, YEAR(TODAY())+1, YEAR(TODAY()))
// Determines fiscal year assuming July-June cycle

// Age group categorization
=IF(YEAR(TODAY())-YEAR(A1)>=65, "Senior", IF(YEAR(TODAY())-YEAR(A1)>=18, "Adult", "Minor"))
// Categorizes ages using current year from TODAY()

// Annual report period
="Annual Report for " & YEAR(TODAY()-1) & "-" & YEAR(TODAY())
// Creates report title spanning two calendar years
```

### [[MONTH]]
Works with TODAY to extract current month for monthly reporting, seasonal analysis, and month-specific calculations in dynamic systems.

```spreadsheets
// Quarter calculation from current date
="Q" & ROUNDUP(MONTH(TODAY())/3,0)
// Returns current quarter (Q1, Q2, Q3, Q4)

// Seasonal pricing logic
=IF(MONTH(TODAY())<=2, "Winter", IF(MONTH(TODAY())<=5, "Spring", IF(MONTH(TODAY())<=8, "Summer", "Fall")))
// Applies seasonal categories based on current month

// Monthly performance comparison
=SUMIFS(B:B, A:A, ">="&DATE(YEAR(TODAY()), MONTH(TODAY()), 1), A:A, "<="&TODAY())
// Sums current month-to-date values using TODAY() as endpoint
```

## Date Difference Functions

### [[DATEDIF]]
Calculates precise differences from past dates to TODAY, essential for age calculations, tenure tracking, and elapsed time measurements with flexible unit options.

```spreadsheets
// Employee tenure with TODAY as end point
=DATEDIF(B2, TODAY(), "Y") & " years, " & DATEDIF(B2, TODAY(), "YM") & " months"
// Calculates complete tenure from hire date to current date

// Contract remaining time
=DATEDIF(TODAY(), C2, "D") & " days remaining"
// Shows days from today until contract expiration

// Project timeline status
=IF(DATEDIF(D2, TODAY(), "D")>0, DATEDIF(D2, TODAY(), "D") & " days overdue", "On schedule")
// Determines if project deadlines have passed using TODAY
```

### [[NETWORKDAYS]]
Counts business days between past dates and TODAY, critical for service level tracking, project management, and business day calculations.

```spreadsheets
// Business days since ticket creation
=NETWORKDAYS(A2, TODAY())
// Calculates working days elapsed for SLA tracking

// Project days remaining (excluding weekends)
=NETWORKDAYS(TODAY(), B2)
// Shows business days from today until project deadline

// Response time analysis
=IF(NETWORKDAYS(C2, TODAY())<=5, "Within SLA", "SLA Breach")
// Compares business days elapsed against 5-day service standard
```

## Commonly Used With Functions Examples

### TODAY with Conditional Logic
```spreadsheets
// Dynamic status based on current date
=IF(A2>TODAY(), "Future", IF(A2=TODAY(), "Today", "Past"))
// Categorizes dates relative to current date

// Payment status with grace periods
=IF(B2<TODAY()-30, "Overdue", IF(B2<TODAY(), "Due Soon", "Current"))
// Creates payment status categories using TODAY as reference

// Project milestone alerts
=IF(C2<=TODAY()+7, "Due This Week", IF(C2<=TODAY()+30, "Due This Month", "Future Task"))
// Generates alerts based on proximity to TODAY
```

### TODAY with Text Formatting
```spreadsheets
// Dynamic report headers with current date
="Sales Report as of " & TEXT(TODAY(), "mmmm dd, yyyy")
// Creates professional report headers that update automatically

// Age display from birth dates
=DATEDIF(A2, TODAY(), "Y") & " years old (as of " & TEXT(TODAY(), "mm/dd/yyyy") & ")"
// Shows age calculation with current date reference

// Business day countdown
=NETWORKDAYS(TODAY(), B2) & " business days until " & TEXT(B2, "mmmm dd")
// Combines business day calculation with formatted target date
```

### TODAY with Mathematical Operations
```spreadsheets
// Rolling 30-day period calculations
=SUMIFS(B:B, A:A, ">="&TODAY()-30, A:A, "<="&TODAY())
// Sums values from 30 days ago through today

// Compound interest with current date
=C2*(1+D2)^((TODAY()-E2)/365)
// Calculates compound interest from start date to today

// Depreciation calculations
=F2*(1-G2)^(DATEDIF(H2, TODAY(), "Y"))
// Applies annual depreciation from purchase date to current date
```
