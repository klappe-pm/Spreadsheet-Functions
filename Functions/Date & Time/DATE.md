---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- date-time
subTopics:
- date-construction
- date-serial-numbers
- date-manipulation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Create Date
- Build Date
- Make Date
tags:
- date
- date-construction
- serial-number
- date-arithmetic
---

# DATE

## Description

**DATE** constructs a date from three components: year, month, and day. It returns a serial number that Excel and Sheets display as a formatted date. This function is the fundamental building block for date manipulation—whenever you need to construct a specific date from numeric components, assemble a date from cell references, or manipulate individual date parts, DATE is your tool.

The real power of DATE lies in how it handles out-of-range values. If you specify month 14, DATE doesn't error—it returns February of the following year (month 12 + 2 = February). If you specify day 0, it returns the last day of the previous month. Day -1 gives you two days before the start of the month. This behavior enables elegant date arithmetic: adding months becomes DATE(YEAR(A1), MONTH(A1)+3, DAY(A1)); finding the last day of any month is DATE(year, month+1, 0). Understanding this overflow/underflow behavior unlocks advanced date manipulation without complex conditionals.

**Excel's serial number system explained:** Excel stores dates as sequential integers starting from January 1, 1900 (serial number 1). DATE(1900,1,1) returns 1, DATE(1900,1,2) returns 2, and so on. January 10, 2026 is serial number 46032, meaning 46,032 days have passed since Excel's epoch. This serial number system is why date arithmetic works: subtracting two dates gives the days between them; adding 30 to a date advances it 30 days. When you see a date displayed as "1/10/2026", the underlying value is just the number 46032.

**Year handling varies by value range:** Two-digit years (0-99) are interpreted based on a cutoff: in Excel, years 0-29 become 2000-2029, and 30-99 become 1930-1999. DATE(25,6,15) returns June 15, 2025; DATE(85,6,15) returns June 15, 1985. However, this behavior can vary by version and settings, so always use four-digit years for clarity and consistency. Google Sheets handles two-digit years similarly but the cutoff year may differ.

## Syntax

> [!f(x)] DATE Syntax
>
> ```
> =DATE(year, month, day)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `year` | Yes | The year component. One to four digits. Two-digit years are interpreted based on system settings (typically: 0-29 = 2000-2029, 30-99 = 1930-1999). Four-digit years are used literally. |
| `month` | Yes | The month component. Valid range is 1-12, but values outside this range roll over: 13 becomes January of next year, 0 becomes December of previous year, -1 becomes November of previous year. |
| `day` | Yes | The day component. Valid range depends on month (1-28, 29, 30, or 31), but out-of-range values roll over: 32 in a 31-day month becomes the 1st of next month, 0 becomes the last day of previous month. |

### Return Value

Returns a serial number representing the specified date. In Excel's 1900 date system, January 1, 1900 = 1. The maximum date is December 31, 9999 (serial number 2958465). Negative serial numbers (dates before January 1, 1900) are not supported in standard Excel.

## Examples

> [!f(x)] DATE Examples

### Example 1: Create a Specific Date
```
=DATE(2026, 1, 10)
```
**Result:** 1/10/2026 (serial number 46032)

**Explanation:** The fundamental use case—constructing a date from year, month, and day components. The result is a true date value that can be used in calculations, comparisons, and formatting.

---

### Example 2: Combine Values from Cells
```
=DATE(A1, B1, C1)
```
**Result:** Date constructed from year in A1, month in B1, day in C1

**Explanation:** Essential for building dates from separate data fields. If your data source provides year, month, and day in separate columns, DATE combines them into a usable date value.

---

### Example 3: First Day of a Month
```
=DATE(2026, 6, 1)
```
**Result:** 6/1/2026

**Explanation:** Simply specify 1 for the day parameter. This pattern is essential for monthly reporting periods, period-start calculations, and date range boundaries.

---

### Example 4: Last Day of a Month (Day 0 Trick)
```
=DATE(2026, 7, 0)
```
**Result:** 6/30/2026 (last day of June)

**Explanation:** Day 0 returns the last day of the previous month. DATE(year, month+1, 0) gives the last day of the specified month. This handles variable month lengths (28, 29, 30, 31 days) automatically.

---

### Example 5: Last Day of February (Leap Year Aware)
```
=DATE(2024, 3, 0)
```
**Result:** 2/29/2024 (leap year)

```
=DATE(2025, 3, 0)
```
**Result:** 2/28/2025 (non-leap year)

**Explanation:** The day 0 trick automatically handles leap years. No conditional logic needed—DATE knows February 2024 has 29 days and February 2025 has 28.

---

### Example 6: Add Months to a Date
```
=DATE(YEAR(A1), MONTH(A1)+3, DAY(A1))
```
**Result:** Date 3 months after the date in A1

**Explanation:** Classic pattern for month addition. If A1 is January 15, adding 3 months gives April 15. Note: If adding months creates an invalid date (like March 31 + 1 month = April 31), the overflow creates May 1. Use EDATE for behavior that preserves end-of-month.

---

### Example 7: Subtract Months from a Date
```
=DATE(YEAR(A1), MONTH(A1)-6, DAY(A1))
```
**Result:** Date 6 months before the date in A1

**Explanation:** Negative month adjustments work correctly across year boundaries. If A1 is March 2026, subtracting 6 months correctly returns September 2025.

---

### Example 8: First Day of Current Month
```
=DATE(YEAR(TODAY()), MONTH(TODAY()), 1)
```
**Result:** First day of the current month

**Explanation:** Combines TODAY with DATE to get the start of the current month. Essential for monthly reports, period boundaries, and MTD calculations.

---

### Example 9: Same Day Next Year
```
=DATE(YEAR(A1)+1, MONTH(A1), DAY(A1))
```
**Result:** Same calendar date one year later

**Explanation:** Add 1 to the year component. Handles February 29 overflow: DATE(2024+1, 2, 29) = March 1, 2025 because Feb 29, 2025 doesn't exist.

---

### Example 10: Anniversary Date (Current Year)
```
=DATE(YEAR(TODAY()), MONTH(A1), DAY(A1))
```
**Result:** The anniversary of the date in A1 occurring this year

**Explanation:** Takes month and day from a historical date but applies the current year. Use for birthdays, contract anniversaries, and annual recurring events.

---

### Example 11: Fiscal Year Start (July 1)
```
=DATE(YEAR(A1)-IF(MONTH(A1)<7,1,0), 7, 1)
```
**Result:** The start of the fiscal year containing the date in A1

**Explanation:** For fiscal years starting July 1, dates before July belong to a fiscal year starting in the previous calendar year. The IF adjusts the year accordingly.

---

### Example 12: Handle Text Inputs
```
=DATE(VALUE(LEFT(A1,4)), VALUE(MID(A1,5,2)), VALUE(RIGHT(A1,2)))
```
**Result:** Date from text "20260110" in A1

**Explanation:** When dates are stored as text in YYYYMMDD format, extract substrings and convert to numbers for DATE. This is common when importing data from legacy systems.

---

### Example 13: Rolling Quarter Start
```
=DATE(YEAR(TODAY()), (ROUNDUP(MONTH(TODAY())/3,0)-1)*3+1, 1)
```
**Result:** First day of the current quarter

**Explanation:** Calculates which quarter we're in, then constructs the first month of that quarter. Q1 starts month 1, Q2 starts month 4, Q3 starts month 7, Q4 starts month 10.

---

### Example 14: Nth Weekday of Month (e.g., 3rd Monday)
```
=DATE(2026, 1, 1) + 7*(3-1) + MOD(2-WEEKDAY(DATE(2026, 1, 1)), 7)
```
**Result:** 1/19/2026 (3rd Monday of January 2026)

**Explanation:** Advanced formula for calculating dates like "Martin Luther King Day" (3rd Monday of January). The 2 represents Monday in WEEKDAY's default mode. Adjust the 3 for nth occurrence.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Non-numeric arguments | Ensure year, month, and day are numbers or cells containing numbers. Use VALUE() to convert text. |
| `#NUM!` | Year is negative or result exceeds date limits | Year must be 0-9999; result must be between 1/1/1900 and 12/31/9999 |
| `Unexpected year` | Two-digit year interpretation | Always use four-digit years to avoid ambiguity (2025 not 25) |
| `Wrong month` | Misunderstanding overflow behavior | Remember that month 13 = January next year; month 0 = December previous year |
| `Date displays as number` | Cell formatted as Number | Format cell as Date (right-click > Format Cells > Date) |
| `Off by one day` | Confusing 1900 date system bug | Excel incorrectly considers 1900 a leap year; avoid dates before March 1, 1900 |

## Use Cases

### [[Dynamic Reporting Period Construction]]

**Scenario:** Create a monthly report that automatically calculates the correct date range for any selected month and year, handling variable month lengths.

**Implementation:**
```
=DATE(B2, C2, 1)                     (Period start - B2=year, C2=month)
=DATE(B2, C2+1, 0)                   (Period end - last day of month)
=DATE(B2-1, C2, 1)                   (Same period, prior year start)
=DATE(B2-1, C2+1, 0)                 (Same period, prior year end)
```

**Business Application:** Finance teams can select any year/month combination and immediately get correct date ranges for data filtering, year-over-year comparisons, and report headers. No need to manually look up month lengths or remember leap years.

**Technical Details:** The day 0 trick (DATE(year, month+1, 0)) is essential here—it automatically returns 28, 29, 30, or 31 depending on the month. February 2024 gets 29 days, February 2025 gets 28, without any conditional logic.

---

### [[Contract and Subscription Date Calculations]]

**Scenario:** Calculate renewal dates, expiration warnings, and proration periods for contracts with various term lengths.

**Implementation:**
```
=DATE(YEAR(B2)+D2, MONTH(B2), DAY(B2))           (End date: B2=start, D2=years)
=DATE(YEAR(B2), MONTH(B2)+E2, DAY(B2))           (End date: E2=months)
=DATE(YEAR(B2), MONTH(B2)+E2, DAY(B2))-1         (Last day of contract)
```

**Business Application:** Account management systems automatically calculate renewal dates for contracts of any length. Subscription platforms determine billing cycles. Legal teams track contract expirations without manual date calculations.

**Technical Details:** When adding months to the 31st of a month, DATE's overflow behavior may produce unexpected results (Jan 31 + 1 month = March 3 in non-leap years). For end-of-month handling, consider using EOMONTH or adding logic to cap the day at the last day of the result month.

---

### [[Data Transformation and Cleansing]]

**Scenario:** Convert dates stored as separate columns or in non-standard text formats into proper date values for analysis.

**Implementation:**
```
=DATE(A2, B2, C2)                                                (Year/Month/Day columns)
=DATE(VALUE(RIGHT(A2,4)), VALUE(LEFT(A2,2)), VALUE(MID(A2,4,2))) (MM/DD/YYYY text)
=DATE(VALUE(LEFT(A2,4)), VALUE(MID(A2,6,2)), VALUE(RIGHT(A2,2))) (YYYYMMDD text)
```

**Business Application:** Data analysts can normalize date data from various source systems into a consistent format. ETL processes convert legacy system exports into analysis-ready date values. Database imports from systems with different date conventions become standardized.

**Technical Details:** Always validate transformed dates. Use error checking like IFERROR(DATE(...), "Invalid") to catch malformed data. Consider DATEVALUE as an alternative for standard text date formats.

---

### [[Payroll and HR Date Calculations]]

**Scenario:** Calculate pay period boundaries, tenure milestones, and benefit eligibility dates based on hire dates.

**Implementation:**
```
=DATE(YEAR(B2)+5, MONTH(B2), DAY(B2))            (5-year anniversary)
=DATE(YEAR(B2), MONTH(B2)+3, 1)                  (Benefits eligibility: 1st of month after 90 days)
=DATE(YEAR(NOW()), MONTH(B2), DAY(B2))           (This year's service anniversary)
```

**Business Application:** HR systems automatically flag upcoming service anniversaries for recognition programs. Payroll calculates correct benefit eligibility dates. Management reports show tenure distributions and milestone projections.

**Technical Details:** For benefits that start "first of month after 90 days", combine DATE with date arithmetic: DATE(YEAR(hire+90), MONTH(hire+90)+1, 1) starts benefits on the first of the month following the 90-day wait.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Date system:** Default 1900 system (January 1, 1900 = 1). Mac Excel historically used 1904 system by default
- **Year handling:** Years 0-29 interpreted as 2000-2029; 30-99 as 1930-1999 (default behavior, may vary)
- **Maximum date:** December 31, 9999 (serial 2958465)
- **Minimum date:** January 1, 1900 (serial 1); dates before this return errors
- **1900 leap year bug:** Excel incorrectly treats 1900 as a leap year, so DATE(1900,2,29) returns a "date" that never existed

### Google Sheets
- **Availability:** All versions
- **Date system:** Uses epoch of December 30, 1899 (serial 0), compatible with Excel for dates after March 1, 1900
- **Year handling:** Similar to Excel, but cutoff year may differ
- **Maximum date:** Similar limits to Excel
- **Minimum date:** Can handle dates before 1900 using negative serial numbers

### Key Difference Alert
The most notable difference is handling of dates before March 1, 1900. Excel has a deliberate bug (for Lotus 1-2-3 compatibility) treating 1900 as a leap year, so Excel's serial number for March 1, 1900 is 61 while the "correct" value would be 60. For practical purposes, this only matters when working with very old dates or calculating day counts spanning across February 1900. For dates after March 1, 1900, Excel and Sheets are fully compatible.

## Tips and Best Practices

1. **Always use four-digit years:** DATE(25,1,1) might mean 2025 or 1925 depending on settings. DATE(2025,1,1) is unambiguous. Future-proof your spreadsheets.

2. **Leverage overflow behavior intentionally:** DATE(2026, 13, 1) = January 1, 2027. DATE(2026, 1, 0) = December 31, 2025. This isn't a bug—it's a powerful feature for date arithmetic.

3. **Use DATE for last-day-of-month:** DATE(year, month+1, 0) is more reliable than trying to remember month lengths. Works for any month, including February in leap years.

4. **Combine with YEAR/MONTH/DAY for manipulation:** To change just the year of a date: DATE(new_year, MONTH(date), DAY(date)). This pattern is fundamental for date manipulation.

5. **Validate imported dates:** When constructing dates from text or separate fields, add validation: =IF(AND(A1>=1, A1<=12), DATE(...), "Invalid month"). Catch data quality issues early.

6. **Watch for day overflow at month ends:** Adding months to January 31 gives different results than you might expect—DATE(2026, 1+1, 31) = March 3, not February 28. Use EDATE for end-of-month-aware month addition.

7. **Use DATE for dynamic ranges:** Build start/end dates programmatically for SUMIFS, COUNTIFS, and other functions with date criteria. DATE(year, quarter*3-2, 1) to DATE(year, quarter*3+1, 0) gives quarter boundaries.

8. **Document date system assumptions:** If your workbook might be opened in Mac Excel or moved between platforms, add a note about which date system is expected.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[DATEVALUE]] | Converts text to date | When you have dates as text strings in standard formats |
| [[TIME]] | Creates time from hour, minute, second | When constructing time values, not dates |
| [[EDATE]] | Adds months to a date | When adding months and you want end-of-month awareness |

### Commonly Used Together

**[[YEAR]] / [[MONTH]] / [[DAY]]** - Extract and reconstruct

*Modify individual components of a date:*
```
=DATE(YEAR(A1)+1, MONTH(A1), DAY(A1))     // Same date next year
=DATE(YEAR(A1), MONTH(A1)+6, DAY(A1))     // Six months later
=DATE(2026, MONTH(A1), DAY(A1))           // Same month/day in 2026
```
The fundamental pattern for date manipulation—extract, modify, reconstruct.

---

**[[TODAY]]** - Current date reference

*Build dates relative to today:*
```
=DATE(YEAR(TODAY()), 1, 1)          // January 1 of current year
=DATE(YEAR(TODAY()), MONTH(TODAY()), 1)    // First of current month
=DATE(YEAR(TODAY())+1, 1, 1)        // January 1 of next year
```
Essential for dynamic date ranges that adjust as time passes.

---

**[[EOMONTH]]** - End of month

*Compare with DATE's day 0 approach:*
```
=EOMONTH(DATE(2026, 6, 1), 0)       // June 30, 2026
=DATE(2026, 7, 0)                   // June 30, 2026 (equivalent)
=EOMONTH(A1, 3)                     // End of month, 3 months from A1
```
EOMONTH is often cleaner for end-of-month calculations, especially when adding months.

---

**[[IF]]** - Conditional date construction

*Build dates conditionally:*
```
=DATE(IF(MONTH(A1)<7, YEAR(A1), YEAR(A1)+1), 7, 1)   // Next July 1
=DATE(B1, C1, IF(C1=2, 28, 30))                      // Last day approximation
```
Combine IF with DATE for complex date logic.

---

**[[TEXT]]** - Format date output

*Create formatted date strings:*
```
=TEXT(DATE(2026, 1, 10), "mmmm d, yyyy")     // "January 10, 2026"
=TEXT(DATE(A1, B1, C1), "yyyy-mm-dd")        // "2026-01-10"
```
Convert DATE results to specific text formats for display or export.

## Official Documentation

- **Microsoft Excel:** [DATE function](https://support.microsoft.com/en-us/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349)
- **Google Sheets:** [DATE function](https://support.google.com/docs/answer/3092969)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | One of the original functions |
| Excel 2007+ | All subsequent | No changes to function behavior |
| Excel for Mac | All versions | Historically used 1904 date system by default |
| Google Sheets | Original launch (2006) | Functionally identical to Excel |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
