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
# NETWORKDAYS

## NETWORKDAYS Description

Calculates the number of working days between two dates, automatically excluding weekends (Saturday and Sunday) and optionally excluding custom holidays. Essential for business day calculations, project scheduling, and service level agreements.

> [!f(x)] NETWORKDAYS Syntax
>
> ```spreadsheets
> NETWORKDAYS(start_date, end_date, [holidays])
> ```
>
> **Parameters:**
> - `start_date` (required): Starting date of the period
> - `end_date` (required): Ending date of the period
> - `holidays` (optional): Range of dates representing holidays to exclude from working day count

> [!f(x)] NETWORKDAYS Examples
>
> ```spreadsheets
> // Basic business days calculation
> NETWORKDAYS(DATE(2024,3,1), DATE(2024,3,31)) → 21 working days in March 2024
> 
> // Project timeline with holidays excluded
> NETWORKDAYS(A1, B1, $H$1:$H$10) → working days between A1 and B1, excluding holidays in H1:H10
> 
> // Service level agreement tracking
> NETWORKDAYS(C1, TODAY()) → business days since service request date
> 
> // Payroll period calculation
> NETWORKDAYS(DATE(2024,1,1), DATE(2024,1,15), HolidayList) → first half January working days
> 
> // Contract duration in business days
> NETWORKDAYS(TODAY(), D1) → working days remaining until contract expiration
> ```

## Use Cases

### [[Project scheduling]]
- **Timeline estimation accuracy**: Calculate realistic project durations by excluding weekends and holidays from delivery estimates, ensuring accurate milestone planning and resource allocation
- **Critical path analysis**: Determine working days between project dependencies to identify bottlenecks and optimize task sequencing for efficient project completion
- **Resource planning optimization**: Schedule team assignments and equipment usage based on actual working days, avoiding weekend and holiday conflicts in project timelines
- **Client delivery commitments**: Provide accurate delivery dates by calculating business days for service commitments, contract obligations, and customer expectations

### [[Service level agreements]]
- **Response time compliance**: Track service desk response times using business days to ensure SLA compliance while excluding weekends and holidays from performance metrics
- **Resolution tracking accuracy**: Measure problem resolution periods in working days to provide fair assessment of service quality and team performance
- **Escalation threshold management**: Set appropriate escalation timers based on business days to ensure critical issues receive attention during working hours
- **Performance benchmarking**: Compare service delivery performance across teams using standardized business day measurements for consistent evaluation

### [[Payroll calculations]]
- **Working day verification**: Calculate exact working days for hourly employees, contractors, and temporary staff to ensure accurate payroll processing and time tracking
- **Leave balance calculations**: Determine business days taken for vacation, sick leave, and personal time off to maintain accurate employee leave balances
- **Overtime threshold tracking**: Monitor working days to identify overtime patterns and ensure compliance with labor regulations and company policies
- **Benefits accrual timing**: Calculate working-day-based benefit accruals for vacation time, sick leave, and other time-based employee benefits

## Related

### Similar Functions

- [[WORKDAY]] - Adds working days to a date, complementing NETWORKDAYS' counting functionality
- [[NETWORKDAYS.INTL]] - Enhanced version with custom weekend definitions beyond Saturday/Sunday
- [[DAYS]] - Counts all calendar days including weekends, parallel to NETWORKDAYS' business-only approach
- [[DATEDIF]] - Calculates date differences in various units, while NETWORKDAYS focuses on working days
- [[WEEKDAY]] - Identifies day of week, often used with NETWORKDAYS for weekend validation

## Business Day Functions

### [[WORKDAY]]
Calculates future working dates while NETWORKDAYS counts working days between existing dates. Both essential for comprehensive business day planning and timeline management.

```spreadsheets
// Compare counting vs calculating working dates
=NETWORKDAYS(A1, B1) → 15 working days between A1 and B1
=WORKDAY(A1, 15) → date that is 15 working days after A1

// Project timeline coordination
=NETWORKDAYS(C1, WORKDAY(C1, D1)) → should equal D1 (working days in duration)
// Validates that calculated end date matches expected duration

// Service level calculations
=WORKDAY(E1, 5) & " (deadline), " & NETWORKDAYS(E1, TODAY()) & " days elapsed"
// Shows both deadline and progress in business days
```

### [[TODAY]]
Provides dynamic reference point for NETWORKDAYS calculations, essential for real-time business day tracking and current-state project monitoring.

```spreadsheets
// Dynamic business day tracking
=NETWORKDAYS(A1, TODAY()) & " business days elapsed"
// Automatically updates daily showing working days since start date

// Service level monitoring
=IF(NETWORKDAYS(B1, TODAY())<=5, "Within SLA", "SLA Breach")
// Real-time SLA compliance checking using TODAY as endpoint

// Project status with current date
="Project: " & NETWORKDAYS(TODAY(), C1) & " working days remaining"
// Dynamic countdown showing working days until project completion
```

### [[WEEKDAY]]
Identifies weekend days that NETWORKDAYS automatically excludes, useful for validation and weekend-aware business logic in conjunction with working day calculations.

```spreadsheets
// Validate NETWORKDAYS assumptions
=IF(WEEKDAY(A1,2)<=5, "Weekday start", "Weekend start") & ", " & NETWORKDAYS(A1, B1) & " working days"
// Shows start day type and working day count

// Weekend adjustment validation
=IF(AND(WEEKDAY(C1,2)<=5, WEEKDAY(D1,2)<=5), NETWORKDAYS(C1,D1), "Weekend dates detected")
// Validates both dates are weekdays before counting

// Business day boundary checking
=NETWORKDAYS(E1, E1) & " days (should be 1 if weekday, 0 if weekend)"
// Tests single-day NETWORKDAYS behavior
```

## Date Range Functions

### [[DAYS]]
Counts all calendar days while NETWORKDAYS counts only business days, both essential for complete timeline analysis and scheduling perspective comparison.

```spreadsheets
// Compare calendar vs business day perspectives
=DAYS(A1, B1) & " total days, " & NETWORKDAYS(A1, B1) & " working days"
// Shows both calendar and business day durations

// Weekend calculation from difference
=DAYS(C1, D1) - NETWORKDAYS(C1, D1) & " weekend days excluded"
// Calculates weekend days by subtracting working from total days

// Efficiency ratio analysis
=ROUND(NETWORKDAYS(E1, F1)/DAYS(E1, F1)*100, 1) & "% working days"
// Shows percentage of period that consists of working days
```

### [[DATEDIF]]
Calculates date differences in multiple units while NETWORKDAYS specializes in business day counting, both used for different temporal analysis needs.

```spreadsheets
// Multiple time unit analysis
=DATEDIF(A1, B1, "D") & " calendar days, " & NETWORKDAYS(A1, B1) & " working days"
// Shows same period in calendar and business day units

// Long-term vs business day analysis
=DATEDIF(C1, TODAY(), "M") & " months, " & NETWORKDAYS(C1, TODAY()) & " working days"
// Combines monthly duration with business day precision

// Project duration comparison
="Duration: " & DATEDIF(D1, E1, "M") & "m " & DATEDIF(D1, E1, "D") & "d total, " & NETWORKDAYS(D1, E1) & " working days"
// Complete duration analysis with multiple perspectives
```

## Commonly Used With Functions Examples

### NETWORKDAYS with Conditional Logic
```spreadsheets
// Service level tier determination
=IF(NETWORKDAYS(A1,TODAY())<=1, "Priority", IF(NETWORKDAYS(A1,TODAY())<=5, "Standard", "Overdue"))
// Categorizes tickets based on business days elapsed

// Project status with working day thresholds
=IF(NETWORKDAYS(TODAY(),B1)<0, "Overdue by " & ABS(NETWORKDAYS(TODAY(),B1)) & " days", NETWORKDAYS(TODAY(),B1) & " working days remaining")
// Shows either overdue status or remaining time

// Holiday-adjusted deadline checking
=IF(NETWORKDAYS(C1,D1,$H$1:$H$10)>=10, "Sufficient time", "Tight deadline")
// Evaluates timeline adequacy considering holidays
```

### NETWORKDAYS with Text Formatting
```spreadsheets
// Professional timeline display
="Timeline: " & NETWORKDAYS(A1,B1) & " working days (" & TEXT(A1,"mm/dd") & " to " & TEXT(B1,"mm/dd") & ")"
// Shows working days with formatted date range

// Service level reporting
=NETWORKDAYS(C1,TODAY()) & " business days elapsed" & IF(NETWORKDAYS(C1,TODAY())>5, " (SLA BREACH)", "")
// Highlights SLA violations in timeline display

// Progress reporting with percentages
=NETWORKDAYS(D1,TODAY()) & " of " & NETWORKDAYS(D1,E1) & " working days (" & ROUND(NETWORKDAYS(D1,TODAY())/NETWORKDAYS(D1,E1)*100,0) & "% complete)"
// Shows progress as both absolute and percentage values
```

### NETWORKDAYS with Mathematical Operations
```spreadsheets
// Hourly cost calculation for business days
=NETWORKDAYS(A1,B1) * 8 * C1
// Calculates total project cost assuming 8 hours per working day

// Average working days per month
=NETWORKDAYS(D1,E1) / DATEDIF(D1,E1,"M")
// Shows average working days per month in date range

// Working day productivity metrics
=F1 / NETWORKDAYS(G1,H1)
// Calculates output per working day for productivity analysis
```
