---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- diagrams
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- diagrams
- excel
- sheets
---
# Spreadsheets-Functions-Date-Time-Complete

```mermaid

graph LR
    DateTime["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Date & Time</b><br/>────────────────<br/>Date and time functions<br/><b>Total Functions:</b> 25</div>"]
    
    DateTime --> DateCalculations["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Date Calculations</b><br/>────────────────<br/>Date calculation functions<br/><b>Functions:</b> 16</div>"]
    
    DateTime --> TimeCalculations["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Time Calculations</b><br/>────────────────<br/>Time calculation functions<br/><b>Functions:</b> 5</div>"]
    
    DateTime --> Duration["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Duration</b><br/>────────────────<br/>Duration calculation functions<br/><b>Functions:</b> 4</div>"]
    
    %% Date Calculations Functions (16 functions)
    DateCalculations --> DATE["<div align='left' style='font-family: MonoLisa, monospace;'><b>DATE</b><br/>────────────────<br/>Returns the serial number of a particular date</div>"]
    DATE --> DATESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DATE(year, month, day)</div>"]
    DATE --> DATEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DATE(2025, 6, 16) → 6/16/2025</div>"]
    
    DateCalculations --> TODAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>TODAY</b><br/>────────────────<br/>Returns the serial number of today's date</div>"]
    TODAY --> TODAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TODAY()</div>"]
    TODAY --> TODAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TODAY() → 6/16/2025</div>"]
    
    DateCalculations --> YEAR["<div align='left' style='font-family: MonoLisa, monospace;'><b>YEAR</b><br/>────────────────<br/>Converts a serial number to a year</div>"]
    YEAR --> YEARSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>YEAR(serial_number)</div>"]
    YEAR --> YEAREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=YEAR(DATE(2025,6,16)) → 2025</div>"]
    
    DateCalculations --> MONTH["<div align='left' style='font-family: MonoLisa, monospace;'><b>MONTH</b><br/>────────────────<br/>Converts a serial number to a month</div>"]
    MONTH --> MONTHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MONTH(serial_number)</div>"]
    MONTH --> MONTHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MONTH(DATE(2025,6,16)) → 6</div>"]
    
    DateCalculations --> DAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>DAY</b><br/>────────────────<br/>Converts a serial number to a day of the month</div>"]
    DAY --> DAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DAY(serial_number)</div>"]
    DAY --> DAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DAY(DATE(2025,6,16)) → 16</div>"]
    
    DateCalculations --> WEEKDAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>WEEKDAY</b><br/>────────────────<br/>Converts a serial number to a day of the week</div>"]
    WEEKDAY --> WEEKDAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WEEKDAY(serial_number, [return_type])</div>"]
    WEEKDAY --> WEEKDAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WEEKDAY(DATE(2025,6,16)) → 2</div>"]
    
    %% Time Calculations Functions (5 functions)
    TimeCalculations --> TIME["<div align='left' style='font-family: MonoLisa, monospace;'><b>TIME</b><br/>────────────────<br/>Returns the serial number of a particular time</div>"]
    TIME --> TIMESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TIME(hour, minute, second)</div>"]
    TIME --> TIMEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TIME(15, 30, 0) → 3:30 PM</div>"]
    
    TimeCalculations --> NOW["<div align='left' style='font-family: MonoLisa, monospace;'><b>NOW</b><br/>────────────────<br/>Returns the serial number of the current date and time</div>"]
    NOW --> NOWSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NOW()</div>"]
    NOW --> NOWEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NOW() → 6/16/2025 3:30 PM</div>"]
    
    TimeCalculations --> HOUR["<div align='left' style='font-family: MonoLisa, monospace;'><b>HOUR</b><br/>────────────────<br/>Converts a serial number to an hour</div>"]
    HOUR --> HOURSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HOUR(serial_number)</div>"]
    HOUR --> HOUREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HOUR(TIME(15,30,0)) → 15</div>"]
    
    %% Duration Functions (4 functions)
    Duration --> DAYS["<div align='left' style='font-family: MonoLisa, monospace;'><b>DAYS</b><br/>────────────────<br/>Returns the number of days between two dates</div>"]
    DAYS --> DAYSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DAYS(end_date, start_date)</div>"]
    DAYS --> DAYSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DAYS(&quot;6/16/2025&quot;, &quot;1/1/2025&quot;) → 166</div>"]
    
    Duration --> NETWORKDAYS["<div align='left' style='font-family: MonoLisa, monospace;'><b>NETWORKDAYS</b><br/>────────────────<br/>Returns the number of whole workdays between two dates</div>"]
    NETWORKDAYS --> NETWORKDAYSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NETWORKDAYS(start_date, end_date, [holidays])</div>"]
    NETWORKDAYS --> NETWORKDAYSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NETWORKDAYS(&quot;1/1/2025&quot;, &quot;6/16/2025&quot;) → 118</div>"]
    
    %% Styling
    style DateTime fill:#F0FFFF,stroke:#333,stroke-width:2px
    style DateCalculations fill:#F0FFFF,stroke:#333,stroke-width:2px
    style TimeCalculations fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Duration fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue
    style DATE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TODAY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style YEAR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MONTH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DAY fill:#F0FFF0,stroke:#333,stroke-width:2px
    style WEEKDAY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TIME fill:#F0FFF0,stroke:#333,stroke-width:2px
    style NOW fill:#B9E9EB,stroke:#333,stroke-width:2px
    style HOUR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DAYS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style NETWORKDAYS fill:#F0FFF0,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style DATESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TODAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style YEARSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MONTHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WEEKDAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TIMESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NOWSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HOURSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DAYSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NETWORKDAYSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style DATEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TODAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style YEAREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MONTHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WEEKDAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TIMEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NOWEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HOUREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DAYSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NETWORKDAYSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---