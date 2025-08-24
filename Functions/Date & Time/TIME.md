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
# TIME

## TIME Description

Creates a time value by combining separate hour, minute, and second values into a serial time that spreadsheet applications can recognize and format. Essential for constructing precise time values from component parts.

> [!f(x)] TIME Syntax
>
> ```spreadsheets
> TIME(hour, minute, second)
> ```
>
> **Parameters:**
> - `hour` (required): Hour value (0-23, values outside range adjust the day)
> - `minute` (required): Minute value (0-59, values outside range adjust the hour)
> - `second` (required): Second value (0-59, values outside range adjust the minute)

> [!f(x)] TIME Examples
>
> ```spreadsheets
> // Basic time construction
> TIME(14, 30, 0) → 2:30:00 PM
> 
> // Using cell references for dynamic times
> TIME(A1, B1, C1) → constructs time from values in cells A1, B1, C1
> 
> // Time arithmetic with automatic adjustment
> TIME(25, 0, 0) → 1:00:00 AM next day (hour overflow adjusts day)
> 
> // Business hours boundary
> TIME(17, 0, 0) → 5:00:00 PM for closing time calculations
> 
> // Precise scheduling with seconds
> TIME(9, 15, 30) → 9:15:30 AM for detailed time tracking
> ```

## Use Cases

### [[Business scheduling]]
- **Meeting time coordination**: Create precise meeting times by combining hour, minute, and second components for calendar integration and time zone calculations
- **Shift scheduling optimization**: Construct start and end times for employee shifts, break periods, and overtime calculations with minute-level precision
- **Appointment booking systems**: Generate time slots by constructing times from scheduling parameters, availability windows, and service duration requirements
- **Conference call coordination**: Build precise timing for international calls by combining local time components with time zone offset calculations

### [[Time calculations]]
- **Duration analysis tracking**: Calculate time differences by constructing start and end times from logged data, performance metrics, and operational measurements
- **Payroll time tracking**: Build clock-in and clock-out times from employee time entry data for accurate wage calculations and overtime determination
- **Manufacturing process timing**: Create cycle times and production schedules by combining process hours, setup minutes, and quality check durations
- **Service level monitoring**: Construct response times and resolution periods from support ticket data for SLA compliance and performance analysis

### [[Deadline management]]
- **Task scheduling precision**: Set exact deadline times by combining date functions with TIME for hour-specific project milestones and deliverable timing
- **Alert system configuration**: Create notification times by constructing specific hours and minutes for automated reminders and escalation procedures
- **Maintenance window planning**: Build maintenance schedules by combining optimal hours with system availability windows for minimal business impact
- **Compliance reporting timing**: Construct regulatory filing deadlines with precise time requirements for legal and financial reporting obligations

## Related

### Similar Functions

- [[NOW]] - Returns current date and time automatically, while TIME constructs specific times from components
- [[DATE]] - Creates dates from year/month/day components, parallel to TIME's hour/minute/second construction
- [[TIMEVALUE]] - Converts text time to serial time, complementing TIME's numeric input approach  
- [[TODAY]] - Returns current date only, often combined with TIME for complete datetime construction
- [[HOUR]] - Extracts hour component from TIME results for validation and time-based calculations

## Time Construction Functions

### [[NOW]]
Provides current system time automatically while TIME constructs specific times from components. Both essential for different temporal reference needs requiring either current or constructed time values.

```spreadsheets
// Compare current vs constructed time
=NOW() → December 19, 2024 3:45:30 PM (current datetime)
=TIME(15,45,30) → 3:45:30 PM (constructed time only)

// Business hours validation using both
=IF(TIME(NOW())>TIME(17,0,0), "After hours", "Business hours")
// Uses TIME to create 5 PM boundary for comparison with NOW

// Scheduled vs current time comparison
=IF(NOW()>DATE(YEAR(NOW()),MONTH(NOW()),DAY(NOW()))+TIME(A1,B1,C1), "Past deadline", "On schedule")
// Combines NOW with constructed deadline time
```

### [[HOUR]]
Extracts hour components from TIME results, commonly used together for time validation and hour-specific calculations with precise time construction.

```spreadsheets
// Validate constructed time components
=HOUR(TIME(A1,B1,C1)) & ":" & MINUTE(TIME(A1,B1,C1)) & ":" & SECOND(TIME(A1,B1,C1))
// Reconstructs time display from TIME function result

// Business hours boundary checking
=IF(HOUR(TIME(A1,B1,C1))>=9, IF(HOUR(TIME(A1,B1,C1))<17, "Business hours", "After hours"), "Before hours")
// Uses HOUR with TIME for business hours validation

// Hourly time slot generation
=TIME(HOUR(A1)+ROW()-1, MINUTE(A1), SECOND(A1))
// Creates hourly time series starting from time in A1
```

### [[MINUTE]]
Works with TIME to extract and validate minute precision, essential for detailed scheduling and minute-level time calculations.

```spreadsheets
// Meeting duration calculations
=TIME(HOUR(B1)+INT((MINUTE(B1)+C1)/60), MOD(MINUTE(B1)+C1,60), SECOND(B1))
// Adds C1 minutes to time in B1 using TIME construction

// Time interval creation
=TIME(HOUR(A1), MINUTE(A1)+(ROW()-1)*15, SECOND(A1))
// Creates 15-minute interval times starting from A1

// Precision time validation
=IF(MINUTE(TIME(D1,E1,F1))=E1, "Valid construction", "Minute overflow occurred")
// Validates that constructed time preserves intended minute value
```

## Date-Time Combination Functions

### [[DATE]]
Creates date components that combine with TIME for complete datetime construction, essential for scheduling and timestamp creation with full date-time precision.

```spreadsheets
// Complete datetime construction
=DATE(YEAR(A1), MONTH(A1), DAY(A1)) + TIME(B1, C1, D1)
// Combines date from A1 with time from B1:D1 components

// Appointment scheduling
=DATE(2024,6,15) + TIME(14,30,0)
// Creates specific appointment datetime: June 15, 2024 2:30:00 PM

// Business day time stamping
=WORKDAY(TODAY(),5) + TIME(9,0,0)
// Creates 9 AM timestamp on 5th working day from today
```

### [[WORKDAY]]
Calculates working dates that combine with TIME for business day scheduling with specific time requirements and precise business hour planning.

```spreadsheets
// Business deadline with specific time
=WORKDAY(TODAY(), 3) + TIME(17,0,0)
// Creates 5 PM deadline 3 working days from today

// Meeting scheduling on working days
=WORKDAY(A1, B1) + TIME(C1, D1, 0)
// Schedules meeting at time C1:D1 on working day calculated from A1+B1

// Service level deadlines
=WORKDAY(E1, 2) + TIME(12,0,0)
// Sets noon deadline 2 business days after service request date
```

## Commonly Used With Functions Examples

### TIME with Conditional Logic
```spreadsheets
// Business hours conditional logic
=IF(TIME(A1,B1,C1)>=TIME(9,0,0), IF(TIME(A1,B1,C1)<=TIME(17,0,0), "Business hours", "After hours"), "Before hours")
// Categorizes constructed time relative to business hours

// Shift scheduling validation
=IF(TIME(D1,E1,F1)>TIME(G1,H1,I1), "End after start", "Invalid: End before start")
// Validates that end time is after start time using TIME construction

// Meeting duration checking
=IF((TIME(J1,K1,L1)-TIME(M1,N1,O1))*24*60<=90, "Within limit", "Exceeds 90 minutes")
// Checks if meeting duration using TIME construction stays within limits
```

### TIME with Text Formatting
```spreadsheets
// Professional time display formatting
=TEXT(TIME(A1,B1,C1), "h:mm AM/PM") & " (" & TEXT(TIME(A1,B1,C1), "HH:mm") & " 24-hour)"
// Shows both 12-hour and 24-hour format: "2:30 PM (14:30 24-hour)"

// Schedule display with duration
="Meeting: " & TEXT(DATE(D1,E1,F1)+TIME(G1,H1,I1), "mm/dd/yyyy h:mm AM/PM")
// Creates formatted appointment display combining DATE and TIME

// Time zone conversion display
=TEXT(TIME(J1,K1,L1), "h:mm AM/PM") & " EST = " & TEXT(TIME(J1+3,K1,L1), "h:mm AM/PM") & " PST"
// Shows time in multiple zones using TIME for calculation
```

### TIME with Mathematical Operations
```spreadsheets
// Time duration calculations
=(TIME(M1,N1,O1)-TIME(P1,Q1,R1))*24*60 & " minutes difference"
// Calculates minutes between two constructed times

// Overtime calculations
=MAX(0, (TIME(S1,T1,U1)-TIME(17,0,0))*24) & " overtime hours"
// Calculates overtime hours past 5 PM using TIME boundary

// Average time calculation
=TIME(HOUR(AVERAGE(V1:V10*24)), MINUTE(AVERAGE(V1:V10*24*60)), SECOND(AVERAGE(V1:V10*24*3600)))
// Creates average time from range of time values using TIME reconstruction
```
