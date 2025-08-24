---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - date & time
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
# WORKDAY

## WORKDAY Description

Calculates a date that is a specified number of working days before or after a start date, automatically excluding weekends and optionally excluding holidays. Essential for project deadline calculations, service level agreements, and business scheduling.

> [!f(x)] WORKDAY Syntax
>
> ```spreadsheets
> WORKDAY(start_date, days, [holidays])
> ```
>
> **Parameters:**
> - `start_date` (required): Starting date for the calculation
> - `days` (required): Number of working days to add (positive) or subtract (negative)
> - `holidays` (optional): Range of holiday dates to exclude from working day calculation

> [!f(x)] WORKDAY Examples
>
> ```spreadsheets
> // Project deadline calculation
> WORKDAY(TODAY(), 10) → date that is 10 working days from today
> 
> // Service response deadline with holidays
> WORKDAY(A1, 5, $H$1:$H$10) → 5 working days after A1, excluding holidays in H1:H10
> 
> // Backwards calculation for project start
> WORKDAY(B1, -15) → date that is 15 working days before B1
> 
> // Contract milestone with holiday exclusions
> WORKDAY(DATE(2024,1,15), 30, HolidayList) → 30 working days after January 15, 2024
> 
> // Dynamic payroll date calculation
> WORKDAY(EOMONTH(TODAY(),-1)+1, 14) → 14th working day of current month
> ```

## Use Cases

### [[Deadline calculations]]
- **Project milestone scheduling**: Calculate realistic delivery dates by adding working days to project start dates, ensuring deadlines account for weekends and company holidays
- **Service level agreement management**: Set accurate response and resolution deadlines by adding business days to service request dates, maintaining customer satisfaction
- **Contract completion timing**: Determine contract fulfillment dates by calculating working days from contract start, ensuring accurate legal and business commitments
- **Manufacturing lead time planning**: Schedule production completion dates by adding working days to order placement, accounting for factory shutdowns and holidays

### [[Business scheduling]]
- **Meeting and event planning**: Schedule business meetings and events on working days, avoiding weekends and holidays for maximum attendance and productivity
- **Training program coordination**: Plan employee training schedules by calculating working days for multi-day programs, ensuring minimal business disruption
- **Resource allocation timing**: Schedule equipment, facility, and personnel availability based on working days, optimizing business resource utilization
- **Vendor coordination scheduling**: Coordinate with suppliers and partners using business day calculations for delivery schedules, meetings, and collaborative projects

### [[Payroll processing]]  
- **Pay period end calculations**: Determine payroll processing deadlines by calculating working days from pay period end, ensuring timely employee compensation
- **Benefits enrollment timing**: Schedule open enrollment periods and benefit changes using working days, providing adequate processing time for HR operations
- **Performance review scheduling**: Calculate review dates by adding working days to employee anniversaries, ensuring systematic and timely performance evaluations
- **Time-off request processing**: Calculate approval deadlines and effective dates for vacation requests using working days, maintaining adequate staffing levels

## Related

### Similar Functions

- [[NETWORKDAYS]] - Counts working days between dates, complementing WORKDAY's date calculation functionality
- [[WORKDAY.INTL]] - Enhanced version with custom weekend definitions beyond Saturday/Sunday exclusions
- [[EDATE]] - Adds months to dates, while WORKDAY adds working days with weekend exclusions
- [[DATE]] - Creates specific dates from components, often combined with WORKDAY for dynamic calculations
- [[TODAY]] - Provides current date as starting point for WORKDAY future date calculations

## Working Day Functions

### [[NETWORKDAYS]]
Counts working days between existing dates while WORKDAY calculates future working dates. Both essential for complete business day planning and timeline validation.

```spreadsheets
// Validate WORKDAY calculations using NETWORKDAYS
=NETWORKDAYS(A1, WORKDAY(A1, 10)) → should equal 10 working days
// Confirms that calculated date matches expected duration

// Project timeline coordination
=WORKDAY(B1, C1) & " (end date), " & NETWORKDAYS(B1, WORKDAY(B1, C1)) & " working days"
// Shows both calculated end date and verification of working days

// Service level validation
=WORKDAY(D1, 5) & " (deadline), " & NETWORKDAYS(D1, TODAY()) & " days elapsed"
// Combines deadline calculation with progress tracking
```

### [[TODAY]]
Serves as dynamic starting point for WORKDAY calculations, essential for real-time deadline setting and current-date-based project scheduling.

```spreadsheets
// Dynamic deadline calculation
=WORKDAY(TODAY(), 7) → 7 working days from current date
// Automatically updates to maintain 7-day working deadline

// Service response timing
="Response due: " & TEXT(WORKDAY(TODAY(), 2), "mm/dd/yyyy")
// Sets 2-day working response deadline from current date

// Project milestone scheduling
=WORKDAY(TODAY(), A1) & " (estimated completion based on today)"
// Calculates completion date using current date as baseline
```

### [[WEEKDAY]]
Identifies day of week to validate WORKDAY results and ensure calculated dates fall on business days, providing quality assurance for working day calculations.

```spreadsheets
// Validate WORKDAY results fall on weekdays
=WEEKDAY(WORKDAY(A1, B1), 2) & " (should be 1-5 for weekday)"
// Confirms WORKDAY result is a business day (1=Mon, 5=Fri)

// Business day confirmation
=IF(WEEKDAY(WORKDAY(C1, D1), 2)<=5, "Valid business day", "Error: Weekend result")
// Validates WORKDAY calculation produces working day

// Deadline day identification
="Deadline falls on " & TEXT(WORKDAY(E1, F1), "dddd")
// Shows which day of week the calculated deadline falls on
```

## Date Calculation Functions

### [[EDATE]]
Adds months to dates while WORKDAY adds working days, both essential for different types of timeline calculations and scheduling needs.

```spreadsheets
// Compare monthly vs working day scheduling
=EDATE(A1, 3) & " (3 months later)"
=WORKDAY(A1, 66) & " (approximately 3 months in working days)"
// Shows different approaches to similar time periods

// Contract scheduling comparison
=EDATE(B1, 6) & " (6-month contract end)"
=WORKDAY(B1, 130) & " (6 months in business days)"
// Different perspectives on contract duration

// Mixed timeline calculations
=WORKDAY(EDATE(C1, 1), 5) → 5 working days after 1 month from C1
// Combines monthly and working day calculations
```

### [[DATE]]
Creates constructed dates for WORKDAY inputs, enabling dynamic working day calculations with computed start dates and flexible scheduling logic.

```spreadsheets
// Quarter-end deadline calculation
=WORKDAY(DATE(YEAR(TODAY()), 3*ROUNDUP(MONTH(TODAY())/3,0), 1), -5)
// 5 working days before quarter end

// Monthly reporting deadlines
=WORKDAY(DATE(YEAR(A1), MONTH(A1), 1), 10)
// 10th working day of the month containing date A1

// Annual deadline scheduling
=WORKDAY(DATE(YEAR(TODAY())+1, 1, 1), B1)
// Working days into next year for annual planning
```

## Business Logic Functions

### [[IF]]
Enables conditional WORKDAY calculations based on business rules, allowing flexible deadline setting and schedule management with different scenarios.

```spreadsheets
// Priority-based deadline setting
=IF(A1="High", WORKDAY(TODAY(),2), IF(A1="Medium", WORKDAY(TODAY(),5), WORKDAY(TODAY(),10)))
// Different working day deadlines based on priority level

// Holiday-aware scheduling
=IF(COUNTIF($H$1:$H$10, WORKDAY(B1,C1))>0, WORKDAY(B1,C1+1), WORKDAY(B1,C1))
// Adjusts deadline if it falls on company holiday

// Business rule application
=IF(WEEKDAY(D1,2)<=3, WORKDAY(D1,5), WORKDAY(D1,7))
// Different timelines based on start day of week
```

## Commonly Used With Functions Examples

### WORKDAY with Conditional Logic
```spreadsheets
// Dynamic deadline based on request type
=IF(A1="Urgent", WORKDAY(TODAY(),1), IF(A1="Standard", WORKDAY(TODAY(),5), WORKDAY(TODAY(),10)))
// Sets 1, 5, or 10 working day deadlines based on urgency

// Holiday-adjusted project scheduling
=IF(COUNTIF($Holidays$1:$Holidays$20, WORKDAY(B1,C1))>0, WORKDAY(B1,C1+1,$Holidays$1:$Holidays$20), WORKDAY(B1,C1,$Holidays$1:$Holidays$20))
// Extends deadline if initial calculation falls on holiday

// Weekend start date adjustment
=IF(WEEKDAY(D1,2)>5, WORKDAY(D1,E1), WORKDAY(D1,E1))
// Handles weekend start dates in working day calculations
```

### WORKDAY with Text Formatting
```spreadsheets
// Professional deadline communication
="Project deadline: " & TEXT(WORKDAY(A1,B1), "dddd, mmmm dd, yyyy") & " (" & B1 & " working days)"
// Example: "Project deadline: Friday, March 15, 2024 (10 working days)"

// Service level display
="Response due by " & TEXT(WORKDAY(C1,2), "mm/dd/yyyy") & " (2 business days)"
// Shows formatted deadline with business day context

// Progress tracking with deadlines
=NETWORKDAYS(D1,TODAY()) & " of " & NETWORKDAYS(D1,WORKDAY(D1,E1)) & " working days elapsed (deadline: " & TEXT(WORKDAY(D1,E1), "mm/dd") & ")"
// Complete progress display with formatted deadline
```

### WORKDAY with Mathematical Operations
```spreadsheets
// Staggered deadline calculations
=WORKDAY(A1, B1*(ROW()-1))
// Creates series of deadlines with B1 working day intervals

// Proportional timeline adjustments
=WORKDAY(C1, ROUND(D1*E1,0))
// Adjusts working days based on proportion or percentage

// Milestone spacing calculations
=WORKDAY(F1, G1/3) & " (1st milestone), " & WORKDAY(F1, G1*2/3) & " (2nd milestone), " & WORKDAY(F1, G1) & " (completion)"
// Creates evenly spaced project milestones using working days
```
