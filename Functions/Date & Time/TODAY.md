---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- date-time
subTopics:
- current-date
- volatile-functions
- date-serial-numbers
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Current Date
- System Date
- Todays Date
tags:
- date
- current-date
- volatile
- dynamic
---

# TODAY

## Description

**TODAY** returns the current date as a serial number, which Excel and Sheets display as a formatted date. It takes no arguments and updates automatically whenever your spreadsheet recalculates. This seemingly simple function is one of the most frequently used in date-based calculations because it provides a dynamic anchor point that stays current without manual updates. Every time you open your spreadsheet, TODAY reflects the actual current date.

Understanding how Excel stores dates is crucial for working with TODAY effectively. Excel (and Google Sheets) represent dates as sequential serial numbers, where each integer represents one day. In Excel's default date system, January 1, 1900 is serial number 1, January 2, 1900 is serial number 2, and so on. TODAY returns the serial number for the current date (for example, January 10, 2026 would be serial number 46032). This serial number approach enables date arithmetic: add 30 to TODAY() and you get the date 30 days from now. Subtract one date from another and you get the number of days between them.

**Volatility warning:** TODAY is a volatile function, meaning it recalculates every time Excel recalculates—not just when its inputs change (it has no inputs!). In large workbooks with thousands of TODAY references, this can slow performance. Unlike regular formulas that only recalculate when their precedent cells change, TODAY recalculates on every edit, every F9 press, and every workbook open. Consider converting TODAY results to static values (paste special as values) when you need a snapshot date rather than a continuously updating one.

The date returned by TODAY is based on your computer's system date (in desktop Excel) or your account's timezone settings (in Google Sheets and Excel Online). There's no time component—TODAY always returns midnight of the current day. If you need both date and time, use NOW instead. Note that different users in different time zones may see different results from the same TODAY formula if they're accessing a cloud-based spreadsheet near midnight.

## Syntax

> [!f(x)] TODAY Syntax
>
> ```
> =TODAY()
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| *(none)* | N/A | TODAY takes no parameters. The empty parentheses are required syntax. |

### Return Value

Returns a serial number representing the current date. Excel displays this as a formatted date based on cell formatting. The serial number is an integer (no decimal portion) representing days since the epoch date (January 1, 1900 in Excel's standard system).

## Examples

> [!f(x)] TODAY Examples

### Example 1: Display Today's Date
```
=TODAY()
```
**Result:** 1/10/2026 (displayed based on cell format, stored as 46032)

**Explanation:** The most basic use—simply shows today's date. The actual display depends on your regional settings and cell format (could show as 10-Jan-2026, 2026-01-10, or other formats). The underlying value is always the serial number.

---

### Example 2: Calculate Days Until a Deadline
```
=A1-TODAY()
```
**Result:** 45 (if A1 contains a date 45 days in the future)

**Explanation:** Date subtraction yields days between dates. If A1 contains February 24, 2026, and today is January 10, 2026, the result is 45. Negative results mean the deadline has passed.

---

### Example 3: Calculate Days Since an Event
```
=TODAY()-B1
```
**Result:** 365 (if B1 contains a date exactly one year ago)

**Explanation:** Reverse the subtraction to count days elapsed. Use this for aging analysis, tenure calculations, or tracking time since last activity.

---

### Example 4: Add Days to Today
```
=TODAY()+30
```
**Result:** 2/9/2026 (30 days from January 10, 2026)

**Explanation:** Adding an integer to TODAY adds that many days. This is perfect for calculating due dates, expiration dates, or future milestones. For example, "Invoice due in 30 days" would use this pattern.

---

### Example 5: First Day of Current Month
```
=DATE(YEAR(TODAY()), MONTH(TODAY()), 1)
```
**Result:** 1/1/2026 (first day of current month)

**Explanation:** Combines TODAY with DATE, YEAR, and MONTH to construct a specific date. By hardcoding day as 1, you get the month's start. Essential for monthly reporting periods.

---

### Example 6: Last Day of Current Month
```
=EOMONTH(TODAY(), 0)
```
**Result:** 1/31/2026 (last day of January 2026)

**Explanation:** EOMONTH with 0 as the second argument returns the end of the current month. The alternative formula using DATE(YEAR(TODAY()), MONTH(TODAY())+1, 0) also works by finding day 0 of next month.

---

### Example 7: Age Calculation in Years
```
=DATEDIF(A1, TODAY(), "Y")
```
**Result:** 35 (if A1 contains birthdate 35 years ago)

**Explanation:** DATEDIF calculates complete years between two dates. Critical for HR applications calculating employee age, tenure, or time-in-grade. Note: DATEDIF is undocumented in Excel but works reliably.

---

### Example 8: Is the Date Today?
```
=IF(A1=TODAY(), "Today!", "Not Today")
```
**Result:** "Today!" if A1 contains today's date

**Explanation:** Direct comparison checks if a date matches today. Use this to highlight current items, flag same-day actions, or identify records requiring immediate attention.

---

### Example 9: Days Remaining in Year
```
=DATE(YEAR(TODAY()), 12, 31)-TODAY()
```
**Result:** 355 (days remaining from January 10 to December 31)

**Explanation:** Calculates distance to year-end. Useful for annual planning, budget pacing, or quota tracking. Combine with project timelines to assess year-end feasibility.

---

### Example 10: Current Week Number
```
=WEEKNUM(TODAY())
```
**Result:** 2 (second week of the year for January 10, 2026)

**Explanation:** Extracts the week number from today's date. Combine with YEAR(TODAY()) for fiscal period tracking. Note that week numbering varies by regional settings.

---

### Example 11: Days Until Next Birthday
```
=DATE(YEAR(TODAY())+IF(DATE(YEAR(TODAY()),MONTH(A1),DAY(A1))<TODAY(),1,0), MONTH(A1), DAY(A1))-TODAY()
```
**Result:** 156 (days until next occurrence of birthday in A1)

**Explanation:** Advanced formula that calculates days until next birthday. The IF checks whether this year's birthday has passed; if so, it uses next year. Demonstrates TODAY in complex date logic.

---

### Example 12: Is It the Weekend?
```
=IF(OR(WEEKDAY(TODAY())=1, WEEKDAY(TODAY())=7), "Weekend", "Weekday")
```
**Result:** "Weekday" or "Weekend" based on current day

**Explanation:** WEEKDAY returns 1 for Sunday and 7 for Saturday (default mode). Combine with TODAY for scheduling logic, determining business day status, or adjusting processes.

---

### Example 13: Current Quarter
```
=ROUNDUP(MONTH(TODAY())/3, 0)
```
**Result:** 1 (Q1 for January), 2 (Q2 for April-June), etc.

**Explanation:** Dividing month by 3 and rounding up yields quarter number. Essential for quarterly reporting, fiscal analysis, and period-based aggregation.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Attempting to use TODAY with arguments | Remove any arguments—TODAY() takes no parameters |
| `Number displayed instead of date` | Cell formatted as Number or General | Format cell as Date (Ctrl+1 or right-click > Format Cells) |
| `Wrong date showing` | Computer system date is incorrect | Check and correct system date settings |
| `Different dates across users` | Timezone differences in cloud spreadsheets | Be aware that cloud-based sheets may show different TODAY values near midnight across time zones |
| `Date not updating` | Manual calculation mode enabled | Press F9 to recalculate, or set calculation to Automatic (Formulas > Calculation Options) |

## Use Cases

### [[Invoice Due Date Calculation]]

**Scenario:** Automatically calculate payment due dates as 30 days from invoice date, with status indicators for overdue invoices.

**Implementation:**
```
=A2+30                              (Due date in column B)
=IF(B2<TODAY(), "OVERDUE", "")      (Status in column C)
=TODAY()-B2                          (Days overdue in column D)
```

**Business Application:** Accounts receivable teams can instantly identify overdue invoices without manual date comparison. Finance dashboards can automatically flag aging receivables, trigger collection workflows, and calculate late fees based on days past due.

**Technical Details:** The formula updates daily without intervention. For rolling reports, TODAY ensures the aging buckets (0-30, 31-60, 61-90 days) always reflect current status. Combine with conditional formatting to color-code overdue items.

---

### [[Employee Tenure Tracking]]

**Scenario:** Calculate years of service for each employee based on their hire date, triggering milestone notifications and benefits eligibility.

**Implementation:**
```
=DATEDIF(B2, TODAY(), "Y")                           (Complete years)
=DATEDIF(B2, TODAY(), "YM")                          (Additional months)
=IF(DATEDIF(B2, TODAY(), "Y")>=5, "Eligible", "")    (5-year benefit eligibility)
```

**Business Application:** HR systems automatically track tenure for benefits vesting, vacation accrual rates, and service awards. No manual updates needed as employees cross tenure thresholds—the spreadsheet always shows current tenure.

**Technical Details:** DATEDIF with "Y" returns complete years, "YM" returns months beyond complete years. For precise tenure (including days), use "Y", "YM", and "MD" together. Consider leap years and hire date edge cases.

---

### [[Contract Expiration Alerts]]

**Scenario:** Monitor contract end dates and create an early warning system for renewals 90, 60, and 30 days before expiration.

**Implementation:**
```
=B2-TODAY()                                                             (Days remaining)
=IF(B2-TODAY()<=0, "EXPIRED", IF(B2-TODAY()<=30, "URGENT", IF(B2-TODAY()<=60, "WARNING", IF(B2-TODAY()<=90, "UPCOMING", "OK"))))
```

**Business Application:** Procurement and vendor management teams avoid contract lapses by receiving tiered alerts. Legal teams can prioritize renewal negotiations. The spreadsheet serves as an always-current contract tracking system.

**Technical Details:** The nested IF creates priority tiers. For cleaner formulas, use IFS or create a separate lookup table with threshold values. Combine with conditional formatting for visual alerts.

---

### [[Project Timeline Tracking]]

**Scenario:** Compare planned milestone dates against current date to show project status—on track, at risk, or behind schedule.

**Implementation:**
```
=IF(C2<TODAY(), IF(D2="Complete", "Done", "LATE"), IF(C2-TODAY()<=7, "Due Soon", "On Track"))
```
Where C2 is planned date and D2 is status.

**Business Application:** Project managers get real-time visibility into milestone status. Daily standups can reference the sheet knowing status is current. Executive dashboards can aggregate red/yellow/green status across all projects.

**Technical Details:** The formula checks if the date has passed, then evaluates completion status. Uncompleted past-due items are "LATE", while upcoming items within 7 days are "Due Soon". Adjust the 7-day threshold as needed for your project cadence.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Date system:** Default is 1900 date system (January 1, 1900 = 1). Mac Excel historically used 1904 date system by default (January 1, 1904 = 0), but modern Mac Excel uses 1900 by default
- **Time zone:** Uses local computer's system date
- **Volatility:** Recalculates on every worksheet change, F9, or workbook open
- **Minimum date:** January 1, 1900 (serial number 1)
- **Maximum date:** December 31, 9999 (serial number 2958465)

### Google Sheets
- **Availability:** All versions
- **Date system:** Uses 1899 system (December 30, 1899 = 0) which is effectively compatible with Excel's 1900 system
- **Time zone:** Uses spreadsheet timezone setting (File > Settings > Time zone), not local computer time
- **Volatility:** Recalculates similarly to Excel
- **Minimum date:** December 30, 1899 (serial number 0)

### Key Difference Alert
The most significant difference is timezone handling in cloud environments. Excel desktop uses your computer's clock, so TODAY is always your local date. Google Sheets uses the spreadsheet's timezone setting, which can be different from your browser's timezone. A user in Tokyo accessing a Sheets file set to New York timezone will see New York's current date, not Tokyo's. This can cause confusion for international teams working near date boundaries.

## Tips and Best Practices

1. **Watch for volatility impact:** In workbooks with thousands of TODAY formulas, consider using a single TODAY reference in a dedicated cell and referencing that cell elsewhere. This reduces recalculation overhead.

2. **Convert to static when needed:** If you need to preserve a specific date (like "date report was generated"), copy the cell and Paste Special > Values. Otherwise, TODAY will update and you'll lose the original date.

3. **Handle text dates carefully:** When comparing TODAY against imported data, ensure the imported dates are true dates, not text strings that look like dates. Use DATEVALUE to convert text to dates if needed.

4. **Consider EOMONTH for month-end:** For end-of-month calculations, EOMONTH(TODAY(), 0) is more reliable than DATE(YEAR(TODAY()), MONTH(TODAY())+1, 0) because it handles year boundaries correctly.

5. **Use TODAY for conditional formatting:** Highlight rows where dates have passed using conditional formatting with formulas like =$B2<TODAY(). This creates dynamic visual indicators.

6. **Combine with WORKDAY for business days:** When calculating deadlines that exclude weekends, use WORKDAY(TODAY(), 10) instead of TODAY()+10 for a deadline 10 business days away.

7. **Be timezone-aware in shared workbooks:** For collaborative cloud spreadsheets, document which timezone the date calculations are based on, especially for teams spanning multiple time zones.

8. **Test near midnight and date boundaries:** Formulas using TODAY near midnight may behave unexpectedly during testing. The date changes at midnight according to the relevant timezone setting.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[NOW]] | Returns current date AND time | When you need timestamps with time component, not just date |
| [[DATE]] | Creates date from year, month, day | When constructing specific dates from components rather than getting current date |
| [[DATEVALUE]] | Converts text to date serial number | When parsing text strings that represent dates |

### Commonly Used Together

**[[YEAR]] / [[MONTH]] / [[DAY]]** - Extract date components

*Extract parts of the current date:*
```
=YEAR(TODAY())   // Returns current year (2026)
=MONTH(TODAY())  // Returns current month (1-12)
=DAY(TODAY())    // Returns current day of month (1-31)
```
Essential for building date-based logic, grouping by period, or constructing new dates from today's components.

---

**[[DATEDIF]]** - Calculate date differences

*Calculate time elapsed since a date:*
```
=DATEDIF(A1, TODAY(), "Y")    // Complete years between A1 and today
=DATEDIF(A1, TODAY(), "M")    // Complete months between A1 and today
=DATEDIF(A1, TODAY(), "D")    // Days between A1 and today
```
Perfect for age calculations, tenure tracking, or any elapsed-time measurement.

---

**[[EDATE]] / [[EOMONTH]]** - Date offset calculations

*Calculate dates relative to today:*
```
=EDATE(TODAY(), 3)     // Date 3 months from today
=EOMONTH(TODAY(), 0)   // Last day of current month
=EOMONTH(TODAY(), -1)  // Last day of previous month
```
Essential for billing cycles, subscription renewals, and monthly reporting periods.

---

**[[WEEKDAY]]** - Day of week

*Determine if today is a weekday or weekend:*
```
=WEEKDAY(TODAY())                                    // Returns 1-7 (Sunday=1)
=IF(WEEKDAY(TODAY(), 2)>5, "Weekend", "Weekday")    // Using Monday=1 mode
```
Critical for scheduling logic, business day calculations, and conditional processing.

---

**[[IF]]** - Conditional logic

*Apply conditions based on current date:*
```
=IF(A1<TODAY(), "Past Due", "Current")
=IF(TODAY()>=B1, "Active", "Pending")
```
The most common pairing—comparing dates against today for status indicators.

## Official Documentation

- **Microsoft Excel:** [TODAY function](https://support.microsoft.com/en-us/office/today-function-5eb3078b-a82c-4751-8930-8b8e6ba0df53)
- **Google Sheets:** [TODAY function](https://support.google.com/docs/answer/3092984)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | One of the original functions |
| Excel 2007+ | All subsequent | No changes to function behavior |
| Excel for Mac | All versions | Historically used 1904 date system by default; now uses 1900 |
| Google Sheets | Original launch (2006) | Identical behavior to Excel |
| Excel Online | Original launch | Uses spreadsheet timezone, not browser timezone |

---

*Last updated: 2026-01-10*
