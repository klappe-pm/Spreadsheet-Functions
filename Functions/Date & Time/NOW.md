---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- date-time
subTopics:
- current-datetime
- volatile-functions
- timestamps
- timezone
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Current Date Time
- Current Timestamp
- System Time
tags:
- datetime
- timestamp
- current-time
- volatile
- dynamic
---

# NOW

## Description

**NOW** returns the current date and time as a serial number that Excel and Sheets display as a formatted datetime. Like TODAY, it takes no arguments and updates automatically with each spreadsheet recalculation. The critical difference is that NOW includes the time component—not just "January 10, 2026" but "January 10, 2026 3:45:23 PM". This makes NOW essential for timestamping, time-sensitive calculations, and any scenario where hours, minutes, and seconds matter.

Excel's datetime serial numbers work by using the integer portion for the date and the decimal portion for the time. For example, 46032.75 represents noon on January 10, 2026: 46032 is the date (January 10, 2026) and 0.75 represents 18 hours (75% of a 24-hour day, or 6:00 PM). This elegant system means time arithmetic is straightforward: adding 0.5 to NOW adds 12 hours; adding 1/24 adds one hour; adding 1/1440 adds one minute. Understanding this decimal system is key to mastering time calculations in spreadsheets.

**Timezone considerations are critical with NOW.** In desktop Excel, NOW returns the time according to your computer's system clock and timezone setting. If your computer is set to Eastern Time, NOW reflects Eastern Time. In Google Sheets and Excel Online, the timezone is determined by the spreadsheet's settings, not your local computer. This means two users in different timezones accessing the same Google Sheet will see the SAME NOW value (based on the sheet's timezone setting), which may not match either user's local time. For international teams, this can cause significant confusion—a timestamp that says "3:00 PM" might be 3:00 PM in New York even though the user creating it is in London at 8:00 PM.

**Volatility caution:** NOW is volatile, recalculating on every spreadsheet change, not just when relevant inputs change. A workbook with many NOW formulas will recalculate constantly, potentially impacting performance. More importantly, if you enter NOW to "timestamp" when you made an entry, that timestamp will keep updating! For a permanent timestamp, you must immediately copy and paste as values, or use alternative methods like Ctrl+Shift+; (which enters a static time in Excel) or Google Sheets' automatic timestamp scripts.

## Syntax

> [!f(x)] NOW Syntax
>
> ```
> =NOW()
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| *(none)* | N/A | NOW takes no parameters. The empty parentheses are required syntax. |

### Return Value

Returns a serial number representing the current date and time. The integer portion represents the date (days since January 1, 1900), and the decimal portion represents the time (fraction of a 24-hour day). For example, 46032.5 represents noon on January 10, 2026.

## Examples

> [!f(x)] NOW Examples

### Example 1: Display Current Date and Time
```
=NOW()
```
**Result:** 1/10/2026 3:45:23 PM (format depends on cell settings)

**Explanation:** Returns both date and time components. The display format varies based on regional settings and cell formatting—could show 24-hour time, seconds, or various date formats. The underlying serial number (like 46032.65654) is always the same.

---

### Example 2: Extract Just the Date from NOW
```
=INT(NOW())
```
**Result:** 1/10/2026 (date only, no time)

**Explanation:** INT truncates the decimal portion, leaving only the date. This is functionally equivalent to TODAY(), but using INT(NOW()) in formulas that also need time elsewhere maintains consistency.

---

### Example 3: Extract Just the Time from NOW
```
=NOW()-INT(NOW())
```
**Result:** 3:45:23 PM (time only)

**Explanation:** Subtracting the integer date portion leaves only the decimal time fraction. Format the cell as Time to display properly. Alternatively, use MOD(NOW(), 1) for the same result.

---

### Example 4: Calculate Hours Until an Event
```
=(A1-NOW())*24
```
**Result:** 36.5 (hours until datetime in A1)

**Explanation:** Datetime subtraction yields days, so multiply by 24 for hours. If A1 contains a datetime 1.5 days away, the result is 36 hours. Negative results indicate the event has passed.

---

### Example 5: Calculate Minutes Elapsed Since Start Time
```
=(NOW()-B1)*24*60
```
**Result:** 127 (minutes since the datetime in B1)

**Explanation:** Multiply by 24 for hours, then by 60 for minutes. Essential for tracking elapsed time in workflows, timing processes, or calculating duration.

---

### Example 6: Add Hours to Current Time
```
=NOW()+5/24
```
**Result:** Current datetime plus 5 hours

**Explanation:** Since 1 = one day, 1/24 = one hour. Adding 5/24 adds 5 hours. This pattern is essential for deadline calculations: NOW()+3/24 is 3 hours from now.

---

### Example 7: Add Minutes to Current Time
```
=NOW()+30/1440
```
**Result:** Current datetime plus 30 minutes

**Explanation:** There are 1440 minutes in a day (24*60), so 1/1440 equals one minute. For a 30-minute deadline, add 30/1440. Alternatively, use TIME(0,30,0) which equals 30/1440.

---

### Example 8: Round to Nearest Hour
```
=ROUND(NOW()*24, 0)/24
```
**Result:** Current time rounded to nearest hour

**Explanation:** Multiply by 24 to convert to hours, round to whole number, divide by 24 to convert back. Use ROUNDDOWN or FLOOR for truncating to current hour.

---

### Example 9: Is It Currently Business Hours?
```
=IF(AND(HOUR(NOW())>=9, HOUR(NOW())<17, WEEKDAY(NOW(),2)<=5), "Open", "Closed")
```
**Result:** "Open" or "Closed" based on current time

**Explanation:** Checks if current hour is between 9 AM and 5 PM AND it's a weekday (Monday-Friday in mode 2). Adjust hours and weekday logic for different business schedules.

---

### Example 10: Time Since Last Update in Hours and Minutes
```
=TEXT(NOW()-A1, "h:mm")
```
**Result:** "4:35" (4 hours, 35 minutes since datetime in A1)

**Explanation:** TEXT with time format converts the decimal difference to readable hours:minutes. For durations over 24 hours, use "[h]:mm" format to show total hours beyond 24.

---

### Example 11: Create Timestamp Text
```
=TEXT(NOW(), "yyyy-mm-dd hh:mm:ss")
```
**Result:** "2026-01-10 15:45:23"

**Explanation:** Converts NOW to a formatted text string. Useful for generating filenames, log entries, or export headers. The TEXT function gives precise control over the output format.

---

### Example 12: Seconds Until Midnight
```
=(INT(NOW())+1-NOW())*86400
```
**Result:** 29737 (seconds remaining until midnight)

**Explanation:** INT(NOW())+1 is midnight tonight. Subtract NOW to get remaining days as decimal, multiply by 86400 (seconds per day) for seconds remaining. Useful for countdown timers.

---

### Example 13: Dynamic Greeting Based on Time of Day
```
=IF(HOUR(NOW())<12, "Good Morning", IF(HOUR(NOW())<17, "Good Afternoon", "Good Evening"))
```
**Result:** "Good Morning", "Good Afternoon", or "Good Evening"

**Explanation:** HOUR extracts the hour (0-23) from current time. Nested IFs create greeting tiers. Use in dashboard headers, automated emails, or user-facing reports.

---

### Example 14: Calculate Working Hours Today
```
=IF(HOUR(NOW())<9, 0, IF(HOUR(NOW())>17, 8, (NOW()-INT(NOW())-TIME(9,0,0))*24))
```
**Result:** Hours worked so far today (assuming 9 AM start)

**Explanation:** Returns 0 before 9 AM, 8 after 5 PM, and elapsed hours during work hours. Demonstrates combining NOW with TIME function for business hour calculations.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Attempting to use NOW with arguments | Remove any arguments—NOW() takes no parameters |
| `Time shows as decimal` | Cell formatted as Number | Format cell as Time or Date/Time (Ctrl+1) |
| `Timestamp keeps changing` | NOW is volatile and recalculates | Copy and Paste Special > Values to freeze the timestamp |
| `Wrong timezone` | Cloud spreadsheet using different timezone | Check spreadsheet timezone settings (File > Settings in Sheets) |
| `Times don't match across users` | Local vs. spreadsheet timezone mismatch | In Google Sheets, NOW uses sheet timezone, not user's local time |
| `Calculations off by hours` | Timezone conversion errors in imported data | Ensure imported timestamps are in expected timezone; use timezone conversion if needed |

## Use Cases

### [[Automated Timestamp Logging]]

**Scenario:** Record when each data entry was made, creating an audit trail without manual timestamp entry.

**Implementation:**
```
=IF(A2<>"", IF(B2="", NOW(), B2), "")
```
Note: This pattern requires copying and pasting values, or using Apps Script/VBA for true automatic timestamps.

**Alternative with Apps Script (Google Sheets):**
```javascript
function onEdit(e) {
  if (e.range.getColumn() == 1) {
    e.range.offset(0, 1).setValue(new Date());
  }
}
```

**Business Application:** Compliance tracking, audit trails, and process monitoring all require accurate timestamps. Knowing exactly when data was entered supports quality control, dispute resolution, and regulatory requirements.

**Technical Details:** Pure formula-based timestamps have limitations because NOW updates continuously. For true static timestamps, use VBA/Apps Script, keyboard shortcuts (Ctrl+Shift+; for time), or immediately paste values after entry.

---

### [[SLA Response Time Monitoring]]

**Scenario:** Track support ticket response times against SLA requirements, flagging tickets approaching or exceeding SLA thresholds.

**Implementation:**
```
=IF(C2="", (NOW()-B2)*24, (C2-B2)*24)                   (Hours elapsed or to response)
=IF(D2>4, "SLA BREACH", IF(D2>3, "WARNING", "OK"))      (Status based on 4-hour SLA)
```
Where B2 is ticket creation time, C2 is response time (empty if unresponded).

**Business Application:** Support managers get real-time visibility into SLA performance. Escalation workflows can trigger automatically based on elapsed time. Customer success teams can prioritize tickets approaching SLA breach.

**Technical Details:** NOW continuously updates, so elapsed time for open tickets refreshes automatically. Closed tickets use the fixed response timestamp. Consider timezone alignment between ticket system and spreadsheet.

---

### [[Shift and Scheduling Calculations]]

**Scenario:** Determine current shift, calculate remaining shift time, and identify which schedule rules apply based on current datetime.

**Implementation:**
```
=IF(AND(HOUR(NOW())>=6, HOUR(NOW())<14), "Day Shift", IF(AND(HOUR(NOW())>=14, HOUR(NOW())<22), "Swing Shift", "Night Shift"))
=IF(HOUR(NOW())<14, TIME(14,0,0)-MOD(NOW(),1), TIME(22,0,0)-MOD(NOW(),1))*24  (Hours remaining in shift)
```

**Business Application:** Workforce management dashboards automatically show current shift status. Payroll calculations can apply correct shift differentials. Resource planning knows current staffing levels without manual lookups.

**Technical Details:** MOD(NOW(),1) extracts just the time portion for comparison against shift boundaries. Handle midnight crossover carefully for night shifts that span two calendar days.

---

### [[Real-Time Dashboard Updates]]

**Scenario:** Display "Last Refreshed" timestamp and data freshness indicators on executive dashboards.

**Implementation:**
```
="Dashboard updated: " & TEXT(NOW(), "mmm d, yyyy h:mm AM/PM")
=IF((NOW()-$Z$1)*24 > 1, "Data may be stale", "Data current")
```
Where Z1 contains the last data refresh timestamp.

**Business Application:** Dashboard users can trust data currency without guessing. Stale data warnings prevent decisions based on outdated information. Automated refresh systems can use these calculations to trigger updates.

**Technical Details:** The difference between NOW and last refresh, multiplied by 24, gives hours since refresh. Adjust the staleness threshold (1 hour in this example) based on data update frequency and business needs.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Timezone:** Uses local computer's system clock and timezone setting
- **Precision:** Displays to seconds; internal precision is approximately 1/100th of a second
- **Volatility:** Recalculates on every worksheet change, F9 press, or workbook open
- **1900 vs 1904 date system:** Affects the serial number but not the displayed date/time

### Google Sheets
- **Availability:** All versions
- **Timezone:** Uses the spreadsheet's timezone setting (File > Settings > Time zone), NOT your local timezone
- **Precision:** Similar to Excel, milliseconds available via API
- **Volatility:** Similar recalculation behavior to Excel
- **Timezone display:** The same NOW() shows the same time to all users regardless of their location

### Key Difference Alert
**Timezone handling is the critical difference.** In desktop Excel, NOW reflects your computer's local time—a user in London sees London time, a user in Tokyo sees Tokyo time. In Google Sheets, NOW reflects the spreadsheet's timezone setting. If the sheet is set to Pacific Time, a user in London accessing that sheet sees Pacific Time, not London time. This is intentional (ensures all users see consistent times) but can confuse users expecting local time. Always document which timezone your spreadsheet uses, and consider adding a timezone indicator in your headers.

For Excel Online, the behavior is similar to Google Sheets—the NOW function uses the spreadsheet's timezone settings rather than the user's local computer time.

## Tips and Best Practices

1. **Use keyboard shortcuts for static timestamps:** In Excel, Ctrl+; enters today's date and Ctrl+Shift+; enters current time as static values. In Sheets, Ctrl+; works for date but Ctrl+Shift+; enters the formula =NOW() rather than a static value.

2. **Immediately paste as values for audit timestamps:** If using NOW() for logging when something happened, immediately copy the cell and paste as values (Ctrl+Shift+V or Paste Special > Values). Otherwise, it will update every time the sheet recalculates.

3. **Centralize NOW references for performance:** Instead of 1000 cells with NOW(), put NOW() in one cell (like $Z$1) and reference that cell. This reduces recalculation overhead.

4. **Document your timezone:** Add a cell or note indicating which timezone the spreadsheet uses. This prevents confusion for remote teams and when sharing across time zones.

5. **Use TIME for time arithmetic:** Instead of NOW()+2/24 for adding 2 hours, consider NOW()+TIME(2,0,0) which is more readable and self-documenting.

6. **Handle day boundaries carefully:** Calculations spanning midnight need extra logic. A shift starting at 10 PM and ending at 6 AM crosses a date boundary, complicating duration calculations.

7. **Consider NOW vs. timestamp columns:** For data entry tracking, a separate timestamp column with static values (via script or manual paste) is more reliable than formulas containing NOW.

8. **Test timezone behavior before deployment:** If your spreadsheet will be used across time zones, test NOW behavior from different locations or by changing spreadsheet timezone settings.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[TODAY]] | Returns current date only (no time) | When you only need the date, not time—cleaner for date-only calculations |
| [[TIME]] | Creates time value from hour, minute, second | When constructing specific times rather than getting current time |
| [[TIMEVALUE]] | Converts text to time serial number | When parsing text strings that represent times |

### Commonly Used Together

**[[INT]]** - Extract date from datetime

*Remove time component from NOW:*
```
=INT(NOW())    // Returns just the date portion
=NOW()-INT(NOW())  // Returns just the time portion
```
Fundamental for separating date and time components for different calculations.

---

**[[HOUR]] / [[MINUTE]] / [[SECOND]]** - Extract time components

*Break down current time into components:*
```
=HOUR(NOW())     // Current hour (0-23)
=MINUTE(NOW())   // Current minute (0-59)
=SECOND(NOW())   // Current second (0-59)
```
Essential for time-based logic, scheduling rules, and time display formatting.

---

**[[TEXT]]** - Format datetime as text

*Create formatted timestamp strings:*
```
=TEXT(NOW(), "yyyy-mm-dd hh:mm:ss")    // "2026-01-10 15:45:23"
=TEXT(NOW(), "dddd, mmmm d, yyyy")     // "Friday, January 10, 2026"
=TEXT(NOW(), "h:mm AM/PM")             // "3:45 PM"
```
Critical for creating human-readable timestamps, log entries, and export formats.

---

**[[WEEKDAY]]** - Day of week from datetime

*Combine with NOW for day-based logic:*
```
=WEEKDAY(NOW())                    // Returns 1-7
=WEEKDAY(NOW(), 2)                 // Returns 1-7 with Monday=1
```
Use for business hour logic, weekend detection, and scheduling rules.

---

**[[IF]]** - Conditional logic

*Apply time-based conditions:*
```
=IF(NOW()-A1 > 1, "Over 24 hours old", "Recent")
=IF(HOUR(NOW())<12, "AM", "PM")
```
Essential for status indicators, alerts, and time-sensitive business rules.

---

**[[NETWORKDAYS]] / [[WORKDAY]]** - Business day calculations

*Calculate business days from now:*
```
=WORKDAY(NOW(), 5)              // 5 business days from now
=NETWORKDAYS(A1, NOW())         // Business days between A1 and now
```
Critical for SLA calculations, delivery estimates, and project timelines that exclude weekends.

## Official Documentation

- **Microsoft Excel:** [NOW function](https://support.microsoft.com/en-us/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46)
- **Google Sheets:** [NOW function](https://support.google.com/docs/answer/3092981)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | One of the original functions |
| Excel 2007+ | All subsequent | No changes to function behavior |
| Excel for Mac | All versions | Same behavior as Windows version |
| Google Sheets | Original launch (2006) | Uses spreadsheet timezone setting |
| Excel Online | Original launch | Uses spreadsheet timezone, not browser timezone |

---

*Last updated: 2026-01-10*
