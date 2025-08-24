---
!!python/object/apply:collections.OrderedDict
- - - categories
    - []
  - - subCategories
    - []
  - - topics
    - []
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-16
  - - dateRevised
    - 2025-06-16
  - - aliases
    - - Spreadsheets-Functions-Date and Time
  - - tags
    - []
---
# Spreadsheets-Functions-Date and Time

```mermaid

graph LR
    DateTime["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Date & Time</b><br/>────────────────<br/>Functions for date and time calculations<br/><b>Total Functions:</b> 25</div>"]
    
    DateTime --> DateCalc["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Date Calculations</b><br/>────────────────<br/>Functions for date operations<br/><b>Functions:</b> 16</div>"]
    DateTime --> Duration["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Duration</b><br/>────────────────<br/>Functions for working days<br/><b>Functions:</b> 4</div>"]
    DateTime --> TimeCalc["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Time Calculations</b><br/>────────────────<br/>Functions for time operations<br/><b>Functions:</b> 5</div>"]
    
    %% Date Calculations (16 functions)
    %% DATE - Function 1
    DateCalc --> DATE["<div align='left' style='font-family: MonoLisa, monospace;'><b>DATE</b><br/>────────────────<br/>Creates a date from year, month, and day</div>"]
    DATE --> DATESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DATE(year, month, day)</div>"]
    DATE --> DATEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DATE(2025, 6, 16) → 6/16/2025</div>"]
    
    %% DATEDIF - Function 2
    DateCalc --> DATEDIF["<div align='left' style='font-family: MonoLisa, monospace;'><b>DATEDIF</b><br/>────────────────<br/>Calculates the difference between two dates in specified units</div>"]
    DATEDIF --> DATEDIFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DATEDIF(start_date, end_date, unit)</div>"]
    DATEDIF --> DATEDIFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DATEDIF(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;, &quot;D&quot;) → 166</div>"]
    
    %% DATEVALUE - Function 3
    DateCalc --> DATEVALUE["<div align='left' style='font-family: MonoLisa, monospace;'><b>DATEVALUE</b><br/>────────────────<br/>Converts a date string to a date value</div>"]
    DATEVALUE --> DATEVALUESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DATEVALUE(date_text)</div>"]
    DATEVALUE --> DATEVALUEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DATEVALUE(&quot;6/16/2025&quot;) → 6/16/2025</div>"]
    
    %% DAY - Function 4
    DateCalc --> DAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>DAY</b><br/>────────────────<br/>Extracts the day from a date</div>"]
    DAY --> DAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DAY(date)</div>"]
    DAY --> DAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DAY(&quot;6/16/2025&quot;) → 16</div>"]
    
    %% DAYS - Function 5
    DateCalc --> DAYS["<div align='left' style='font-family: MonoLisa, monospace;'><b>DAYS</b><br/>────────────────<br/>Returns the number of days between two dates</div>"]
    DAYS --> DAYSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DAYS(end_date, start_date)</div>"]
    DAYS --> DAYSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DAYS(&quot;6/16/2025&quot;, &quot;1/1/2025&quot;) → 166</div>"]
    
    %% DAYS360 - Function 6
    DateCalc --> DAYS360["<div align='left' style='font-family: MonoLisa, monospace;'><b>DAYS360</b><br/>────────────────<br/>Calculates days between two dates using a 360-day year</div>"]
    DAYS360 --> DAYS360SYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DAYS360(start_date, end_date, [method])</div>"]
    DAYS360 --> DAYS360EXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DAYS360(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;) → 165</div>"]
    
    %% EDATE - Function 7
    DateCalc --> EDATE["<div align='left' style='font-family: MonoLisa, monospace;'><b>EDATE</b><br/>────────────────<br/>Returns a date offset by a specified number of months</div>"]
    EDATE --> EDATESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>EDATE(start_date, months)</div>"]
    EDATE --> EDATEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=EDATE(&quot;6/16/2025&quot;, 3) → 9/16/2025</div>"]
    
    %% EOMONTH - Function 8
    DateCalc --> EOMONTH["<div align='left' style='font-family: MonoLisa, monospace;'><b>EOMONTH</b><br/>────────────────<br/>Returns the last day of the month offset by specified months</div>"]
    EOMONTH --> EOMONTHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>EOMONTH(start_date, months)</div>"]
    EOMONTH --> EOMONTHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=EOMONTH(&quot;6/16/2025&quot;, 0) → 6/30/2025</div>"]
    
    %% ISOWEEKNUM - Function 9
    DateCalc --> ISOWEEKNUM["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISOWEEKNUM</b><br/>────────────────<br/>Returns the ISO week number for a date</div>"]
    ISOWEEKNUM --> ISOWEEKNUMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISOWEEKNUM(date)</div>"]
    ISOWEEKNUM --> ISOWEEKNUMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISOWEEKNUM(&quot;6/16/2025&quot;) → 25</div>"]
    
    %% MONTH - Function 10
    DateCalc --> MONTH["<div align='left' style='font-family: MonoLisa, monospace;'><b>MONTH</b><br/>────────────────<br/>Extracts the month from a date</div>"]
    MONTH --> MONTHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MONTH(date)</div>"]
    MONTH --> MONTHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MONTH(&quot;6/16/2025&quot;) → 6</div>"]
    
    %% NOW - Function 11
    DateCalc --> NOW["<div align='left' style='font-family: MonoLisa, monospace;'><b>NOW</b><br/>────────────────<br/>Returns the current date and time</div>"]
    NOW --> NOWSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NOW()</div>"]
    NOW --> NOWEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NOW() → 6/16/2025 11:37 AM</div>"]
    
    %% TODAY - Function 12
    DateCalc --> TODAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>TODAY</b><br/>────────────────<br/>Returns the current date</div>"]
    TODAY --> TODAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TODAY()</div>"]
    TODAY --> TODAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TODAY() → 6/16/2025</div>"]
    
    %% WEEKDAY - Function 13
    DateCalc --> WEEKDAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>WEEKDAY</b><br/>────────────────<br/>Returns the day of the week for a date</div>"]
    WEEKDAY --> WEEKDAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WEEKDAY(date, [type])</div>"]
    WEEKDAY --> WEEKDAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WEEKDAY(&quot;6/16/2025&quot;, 1) → 2</div>"]
    
    %% WEEKNUM - Function 14
    DateCalc --> WEEKNUM["<div align='left' style='font-family: MonoLisa, monospace;'><b>WEEKNUM</b><br/>────────────────<br/>Returns the week number in a year for a date</div>"]
    WEEKNUM --> WEEKNUMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WEEKNUM(date, [type])</div>"]
    WEEKNUM --> WEEKNUMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WEEKNUM(&quot;6/16/2025&quot;, 1) → 25</div>"]
    
    %% YEAR - Function 15
    DateCalc --> YEAR["<div align='left' style='font-family: MonoLisa, monospace;'><b>YEAR</b><br/>────────────────<br/>Extracts the year from a date</div>"]
    YEAR --> YEARSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>YEAR(date)</div>"]
    YEAR --> YEAREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=YEAR(&quot;6/16/2025&quot;) → 2025</div>"]
    
    %% YEARFRAC - Function 16
    DateCalc --> YEARFRAC["<div align='left' style='font-family: MonoLisa, monospace;'><b>YEARFRAC</b><br/>────────────────<br/>Calculates the fraction of a year between two dates</div>"]
    YEARFRAC --> YEARFRACSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>YEARFRAC(start_date, end_date, [basis])</div>"]
    YEARFRAC --> YEARFRACEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=YEARFRAC(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;, 0) → 0.4583</div>"]
    
    %% Duration (4 functions)
    %% NETWORKDAYS.INTL - Function 17
    Duration --> NETWORKDAYSINTL["<div align='left' style='font-family: MonoLisa, monospace;'><b>NETWORKDAYS.INTL</b><br/>────────────────<br/>Calculates working days with custom weekend days</div>"]
    NETWORKDAYSINTL --> NETWORKDAYSINTLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])</div>"]
    NETWORKDAYSINTL --> NETWORKDAYSINTLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NETWORKDAYS.INTL(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;, 1) → 119</div>"]
    
    %% NETWORKDAYS - Function 18
    Duration --> NETWORKDAYS["<div align='left' style='font-family: MonoLisa, monospace;'><b>NETWORKDAYS</b><br/>────────────────<br/>Calculates working days between two dates, excluding weekends</div>"]
    NETWORKDAYS --> NETWORKDAYSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NETWORKDAYS(start_date, end_date, [holidays])</div>"]
    NETWORKDAYS --> NETWORKDAYSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NETWORKDAYS(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;) → 119</div>"]
    
    %% WORKDAY.INTL - Function 19
    Duration --> WORKDAYINTL["<div align='left' style='font-family: MonoLisa, monospace;'><b>WORKDAY.INTL</b><br/>────────────────<br/>Returns a date offset by working days with custom weekends</div>"]
    WORKDAYINTL --> WORKDAYINTLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WORKDAY.INTL(start_date, days, [weekend], [holidays])</div>"]
    WORKDAYINTL --> WORKDAYINTLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WORKDAY.INTL(&quot;6/16/2025&quot;, 10, 1) → 6/30/2025</div>"]
    
    %% WORKDAY - Function 20
    Duration --> WORKDAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>WORKDAY</b><br/>────────────────<br/>Returns a date offset by a specified number of working days</div>"]
    WORKDAY --> WORKDAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WORKDAY(start_date, days, [holidays])</div>"]
    WORKDAY --> WORKDAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WORKDAY(&quot;6/16/2025&quot;, 10) → 6/30/2025</div>"]
    
    %% Time Calculations (5 functions)
    %% HOUR - Function 21
    TimeCalc --> HOUR["<div align='left' style='font-family: MonoLisa, monospace;'><b>HOUR</b><br/>────────────────<br/>Extracts the hour from a time or datetime</div>"]
    HOUR --> HOURSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HOUR(time)</div>"]
    HOUR --> HOUREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HOUR(&quot;11:37 AM&quot;) → 11</div>"]
    
    %% MINUTE - Function 22
    TimeCalc --> MINUTE["<div align='left' style='font-family: MonoLisa, monospace;'><b>MINUTE</b><br/>────────────────<br/>Extracts the minute from a time or datetime</div>"]
    MINUTE --> MINUTESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MINUTE(time)</div>"]
    MINUTE --> MINUTEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MINUTE(&quot;11:37 AM&quot;) → 37</div>"]
    
    %% SECOND - Function 23
    TimeCalc --> SECOND["<div align='left' style='font-family: MonoLisa, monospace;'><b>SECOND</b><br/>────────────────<br/>Extracts the second from a time or datetime</div>"]
    SECOND --> SECONDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SECOND(time)</div>"]
    SECOND --> SECONDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SECOND(&quot;11:37:45 AM&quot;) → 45</div>"]
    
    %% TIME - Function 24
    TimeCalc --> TIME["<div align='left' style='font-family: MonoLisa, monospace;'><b>TIME</b><br/>────────────────<br/>Creates a time from hour, minute, and second</div>"]
    TIME --> TIMESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TIME(hour, minute, second)</div>"]
    TIME --> TIMEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TIME(11, 37, 0) → 11:37 AM</div>"]
    
    %% TIMEVALUE - Function 25
    TimeCalc --> TIMEVALUE["<div align='left' style='font-family: MonoLisa, monospace;'><b>TIMEVALUE</b><br/>────────────────<br/>Converts a time string to a time value</div>"]
    TIMEVALUE --> TIMEVALUESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TIMEVALUE(time_text)</div>"]
    TIMEVALUE --> TIMEVALUEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TIMEVALUE(&quot;11:37 AM&quot;) → 0.4840</div>"]
    
    %% Styling
    style DateTime fill:#F0FFFF,stroke:#333,stroke-width:2px
    style DateCalc fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Duration fill:#F0FFFF,stroke:#333,stroke-width:2px
    style TimeCalc fill:#F0FFFF,stroke:#333,stroke-width:2px
    %% Date Calculations functions (alternate colors)
    style DATE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DATEDIF fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DATEVALUE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DAY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DAYS fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DAYS360 fill:#B9E9EB,stroke:#333,stroke-width:2px
    style EDATE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style EOMONTH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ISOWEEKNUM fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MONTH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style NOW fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TODAY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style WEEKDAY fill:#F0FFF0,stroke:#333,stroke-width:2px
    style WEEKNUM fill:#B9E9EB,stroke:#333,stroke-width:2px
    style YEAR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style YEARFRAC fill:#B9E9EB,stroke:#333,stroke-width:2px
    %% Duration functions (continue alternating)
    style NETWORKDAYSINTL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style NETWORKDAYS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style WORKDAYINTL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style WORKDAY fill:#B9E9EB,stroke:#333,stroke-width:2px
    %% Time Calculations functions (continue alternating)
    style HOUR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MINUTE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SECOND fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TIME fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TIMEVALUE fill:#F0FFF0,stroke:#333,stroke-width:2px
    %% All syntax nodes - pink
    style DATESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DATEDIFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DATEVALUESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DAYSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DAYS360SYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style EDATESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style EOMONTHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISOWEEKNUMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MONTHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NOWSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TODAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WEEKDAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WEEKNUMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style YEARSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style YEARFRACSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NETWORKDAYSINTLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NETWORKDAYSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WORKDAYINTLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WORKDAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HOURSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MINUTESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SECONDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TIMESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TIMEVALUESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    %% All example nodes - lavender
    style DATEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DATEDIFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DATEVALUEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DAYSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DAYS360EXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style EDATEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style EOMONTHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISOWEEKNUMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MONTHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NOWEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TODAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WEEKDAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WEEKNUMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style YEAREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style YEARFRACEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NETWORKDAYSINTLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NETWORKDAYSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WORKDAYINTLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WORKDAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HOUREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MINUTEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SECONDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TIMEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TIMEVALUEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```
