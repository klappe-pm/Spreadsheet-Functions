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
# DATE

## DATE Description

Creates a date value by combining separate year, month, and day values into a serial date that spreadsheet applications can recognize and format. Essential for constructing dates dynamically from component parts.

> [!f(x)] DATE Syntax
>
> ```spreadsheets
> DATE(year, month, day)
> ```
>
> **Parameters:**
> - `year` (required): Year value (1900-9999 in Excel, 1-3000 in Sheets)
> - `month` (required): Month value (1-12, values outside range adjust the year)
> - `day` (required): Day value (1-31, values outside range adjust the month)

> [!f(x)] DATE Examples
>
> ```spreadsheets
> // Basic date construction
> DATE(2024, 3, 15) → March 15, 2024
> 
> // Using cell references for dynamic dates
> DATE(A1, B1, C1) → constructs date from values in cells A1, B1, C1
> 
> // Date arithmetic with automatic adjustment
> DATE(2024, 13, 1) → January 1, 2025 (month overflow adjusts year)
> 
> // Project deadline calculation
> DATE(2024, 6, 30) → June 30, 2024 for quarterly reporting
> 
> // Payroll date construction
> DATE(YEAR(TODAY()), MONTH(TODAY()), 15) → 15th of current month
> ```

## Use Cases

### [[Project management]]
- **Dynamic milestone tracking**: Construct project deadlines by combining user-selected years, quarters, and day requirements for flexible scheduling across multiple time horizons
- **Contract date generation**: Build contract start dates from separate legal approval dates, processing delays, and standard business terms to ensure compliance timing
- **Resource allocation scheduling**: Create equipment reservation dates by combining project phase schedules, resource availability windows, and buffer time calculations
- **Budget cycle planning**: Generate fiscal year reporting dates from organizational calendar settings, departmental requirements, and regulatory deadline specifications

### [[Payroll systems]]
- **Pay period calculations**: Construct pay dates from employee start dates, company pay cycle rules, and holiday adjustments to ensure consistent payroll processing
- **Benefits enrollment timing**: Generate open enrollment dates from policy effective dates, regulatory requirements, and employee anniversary schedules
- **Performance review scheduling**: Build review dates from hire dates, promotion dates, and organizational review cycle policies to maintain fair evaluation timelines
- **Time-off accrual tracking**: Create accrual milestone dates from employment start dates, policy changes, and anniversary calculations for accurate leave management

### [[Financial modeling]]
- **Investment maturity calculations**: Construct bond maturity dates from purchase dates, term lengths, and market calendar adjustments for portfolio planning
- **Loan payment scheduling**: Generate payment due dates from origination dates, payment frequency settings, and business day adjustments for accurate billing cycles
- **Depreciation schedule creation**: Build asset depreciation milestone dates from purchase dates, useful life parameters, and accounting period requirements
- **Tax deadline tracking**: Create tax filing dates from fiscal year definitions, entity types, and regulatory calendar changes for compliance management

## Related

### Similar Functions

- [[TODAY]] - Returns current date without parameters, while DATE requires year/month/day inputs
- [[DATEVALUE]] - Converts date text to serial dates, complementing DATE's numeric input approach
- [[TIME]] - Creates time values from hour/minute/second components, parallel to DATE's date construction
- [[NOW]] - Returns current date and time, combining DATE and TIME functionality automatically
- [[EDATE]] - Adds months to existing dates, extending DATE's basic construction capabilities

## Date Construction Functions

### [[YEAR]]
Extracts year components from DATE results, commonly used together for date validation and reconstruction. YEAR helps verify DATE outputs and enables dynamic date building with current year references.

```spreadsheets
// Validate constructed date matches intended year
=IF(YEAR(DATE(A1,B1,C1))=A1, DATE(A1,B1,C1), "Date error")
// Ensures constructed date hasn't rolled over to different year

// Build date with current year reference
=DATE(YEAR(TODAY()), 12, 25) 
// Creates Christmas date for current year

// Financial year-end calculation
=DATE(YEAR(TODAY())+IF(MONTH(TODAY())>6,1,0), 6, 30)
// Creates June 30 year-end date based on current fiscal position
```

### [[MONTH]]
Works with DATE to extract and validate month components, essential for reconstructing dates and building month-specific calculations with proper month validation logic.

```spreadsheets
// Quarter-end date construction
=DATE(YEAR(A1), MONTH(A1)+3-MOD(MONTH(A1)-1,3), DAY(EOMONTH(A1,2-MOD(MONTH(A1)-1,3))))
// Creates quarter-end date from any date input

// Monthly reporting date series
=DATE(YEAR(B1), MONTH(B1)+ROW(A1:A12)-1, 1)
// Generates 12 monthly first-day dates starting from date in B1

// Seasonal date adjustments
=DATE(YEAR(TODAY()), IF(MONTH(TODAY())<=6,1,7), 1)
// Creates either January 1 or July 1 based on current month
```

### [[DAY]]
Pairs with DATE for day-level date manipulation and validation, particularly useful for end-of-month calculations and day-specific recurring date generation.

```spreadsheets
// Preserve day when changing month/year
=DATE(2025, 3, DAY(A1))
// Moves date in A1 to March 2025 keeping same day

// Payroll date calculation (15th and last day)
=IF(B1="mid", DATE(YEAR(A1),MONTH(A1),15), DATE(YEAR(A1),MONTH(A1)+1,0))
// Creates either 15th of month or last day of month based on B1 value

// Anniversary date calculation
=DATE(YEAR(TODAY()), MONTH(C1), DAY(C1))
// Creates this year's anniversary from hire date in C1
```

## Date Arithmetic Functions

### [[DATEDIF]]
Calculates differences between DATE-constructed dates, essential for age calculations, tenure tracking, and duration analysis using DATE as input for precise date range measurements.

```spreadsheets
// Project duration from constructed dates
=DATEDIF(DATE(2024,1,15), DATE(2024,6,30), "D") & " days"
// Calculates exact days between constructed project start and end dates

// Employee tenure calculation
=DATEDIF(DATE(YEAR(B1),MONTH(B1),DAY(B1)), TODAY(), "Y") & " years, " & 
 DATEDIF(DATE(YEAR(B1),MONTH(B1),DAY(B1)), TODAY(), "YM") & " months"
// Shows complete tenure from hire date to current date

// Contract remaining time
=DATEDIF(TODAY(), DATE(2025,12,31), "M") & " months remaining"
// Shows months remaining until constructed contract end date
```

### [[NETWORKDAYS]]
Counts business days between DATE-constructed dates, critical for project timelines, delivery schedules, and business day calculations excluding weekends and holidays.

```spreadsheets
// Business days for project phases
=NETWORKDAYS(DATE(2024,3,1), DATE(2024,6,15))
// Calculates working days between constructed project dates

// Service level agreement tracking
=NETWORKDAYS(DATE(YEAR(A1),MONTH(A1),DAY(A1)), TODAY())
// Shows business days elapsed since service request date

// Delivery schedule calculation
=NETWORKDAYS(TODAY(), DATE(YEAR(B1),MONTH(B1),DAY(B1)), $H$1:$H$10)
// Business days until delivery date excluding holidays in range H1:H10
```

## Commonly Used With Functions Examples

### DATE with Conditional Logic
```spreadsheets
// Dynamic quarter-end date calculation
=DATE(YEAR(TODAY()), 3*ROUNDUP(MONTH(TODAY())/3,0), DAY(EOMONTH(DATE(YEAR(TODAY()), 3*ROUNDUP(MONTH(TODAY())/3,0), 1), 0)))
// Creates current quarter-end date automatically

// Project milestone with buffer days
=IF(WEEKDAY(DATE(A1,B1,C1))=1, DATE(A1,B1,C1)+1, IF(WEEKDAY(DATE(A1,B1,C1))=7, DATE(A1,B1,C1)+2, DATE(A1,B1,C1)))
// Adjusts constructed date to avoid weekends

// Age-based date validation
=IF(DATEDIF(DATE(A1,B1,C1), TODAY(), "Y")>=18, DATE(A1,B1,C1), "Invalid: Must be 18+")
// Validates constructed birth date meets age requirements
```

### DATE with Text Formatting
```spreadsheets
// Professional date display with formatting
=TEXT(DATE(YEAR(A1), MONTH(A1), DAY(A1)), "mmmm dd, yyyy") & " (" & TEXT(DATE(YEAR(A1), MONTH(A1), DAY(A1)), "dddd") & ")"
// Example: "March 15, 2024 (Friday)"

// Fiscal period identification
="Q" & ROUNDUP(MONTH(DATE(A1,B1,C1))/3,0) & " FY" & IF(MONTH(DATE(A1,B1,C1))<=6, YEAR(DATE(A1,B1,C1)), YEAR(DATE(A1,B1,C1))+1)
// Example: "Q2 FY2025" for dates between Jan-Jun

// International date formatting
=TEXT(DATE(A1,B1,C1), "[$-409]mm/dd/yyyy") & " (US) | " & TEXT(DATE(A1,B1,C1), "[$-809]dd/mm/yyyy") & " (UK)"
// Shows same date in different international formats
```

### DATE with Mathematical Operations
```spreadsheets
// Payment schedule generation
=DATE(YEAR(A1), MONTH(A1)+((ROW()-1)*3), DAY(A1))
// Creates quarterly payment dates from start date in A1

// Age calculation with decimal precision
=ROUNDUP((TODAY()-DATE(A1,B1,C1))/365.25, 2) & " years old"
// Calculates precise age from constructed birth date

// Business day adjustment calculation
=DATE(A1,B1,C1) + IF(WEEKDAY(DATE(A1,B1,C1))=7, 2, IF(WEEKDAY(DATE(A1,B1,C1))=1, 1, 0))
// Automatically moves weekend dates to next Monday
```
