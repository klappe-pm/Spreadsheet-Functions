---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- date-time
subTopics:
- date-extraction
- day-component
- date-parsing
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Extract Day
- Get Day
- Day of Month
- Day Component
tags:
- date
- day
- extraction
- date-component
---

# DAY

## Description

**DAY** extracts the day-of-month component from a date and returns it as an integer from 1 to 31. Given a date like "March 15, 2026", DAY returns 15. It isolates just the day portion, ignoring the month and year. This is the third of the three essential date component functions (YEAR, MONTH, DAY) that together decompose any date into its calendar parts.

The DAY function works with Excel's serial number date system. When a cell displays "January 10, 2026", Excel stores the serial number 46032. DAY calculates which day of the month that serial number represents and returns 10. The cell's display format is irrelevant—whether showing "10 Jan 2026", "1/10/2026", or "2026-01-10", DAY returns 10.

**Common applications for DAY include:** validating that data falls within expected day ranges, calculating days until end of month, identifying payroll cycles (like 1st and 15th), detecting month-end transactions, and reconstructing dates with modified components. Combined with YEAR and MONTH in a DATE formula, DAY enables flexible date manipulation—change any component while preserving the others.

**Day ranges vary by month:** DAY returns 1-28, 29, 30, or 31 depending on the source date's month. For February dates, maximum is 28 or 29 (leap year). For April, June, September, November: 30. For other months: 31. The function simply reports what day the date falls on; it doesn't validate whether that day "should" exist for a given month. When constructing dates with DATE function, out-of-range days roll over to subsequent months (day 32 in January becomes February 1).

## Syntax

> [!f(x)] DAY Syntax
>
> ```
> =DAY(serial_number)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `serial_number` | Yes | A date value from which to extract the day-of-month. Can be a cell reference containing a date, a date function like TODAY() or DATE(), a serial number, or a text string that Excel can interpret as a date. |

### Return Value

Returns an integer from 1 to 31 representing the day of the month. The maximum value depends on the month in the source date (28-31).

## Examples

> [!f(x)] DAY Examples

### Example 1: Extract Day from a Date Cell
```
=DAY(A1)
```
**Result:** 15 (if A1 contains March 15, 2026)

**Explanation:** Extracts just the day number from any date. Works regardless of date format displayed in the cell—the underlying serial number determines the result.

---

### Example 2: Current Day of Month
```
=DAY(TODAY())
```
**Result:** 10 (on January 10, 2026)

**Explanation:** Combines with TODAY() to get the current day-of-month. Useful for identifying where we are in the current month for pacing calculations.

---

### Example 3: Days Remaining in Month
```
=DAY(EOMONTH(A1,0))-DAY(A1)
```
**Result:** 16 (if A1 contains March 15, 2026; March has 31 days)

**Explanation:** EOMONTH returns the last day of the month; subtracting today's day gives remaining days. March 31 - 15 = 16 days remaining.

---

### Example 4: Is It Month End?
```
=IF(DAY(A1)=DAY(EOMONTH(A1,0)), "Month End", "Not Month End")
```
**Result:** "Month End" for dates like Jan 31, Feb 28/29, etc.

**Explanation:** Compares the day to the month's last day. Identifies month-end dates regardless of whether the month has 28, 29, 30, or 31 days.

---

### Example 5: First Day of Month Check
```
=IF(DAY(A1)=1, "Month Start", "Mid-Month")
```
**Result:** "Month Start" if date is 1st of any month

**Explanation:** Simple check for the first day. Use for identifying period starts, processing month-opening transactions, or applying first-of-month business rules.

---

### Example 6: Payroll Date Check (1st and 15th)
```
=IF(OR(DAY(A1)=1, DAY(A1)=15), "Payday", "Not Payday")
```
**Result:** "Payday" for 1st or 15th of any month

**Explanation:** Many organizations pay on the 1st and 15th. This identifies payroll dates. Extend with WEEKDAY checks for business day adjustments.

---

### Example 7: Weekly Pattern (Days 1-7, 8-14, etc.)
```
=CEILING(DAY(A1)/7, 1)
```
**Result:** 1 for days 1-7, 2 for days 8-14, 3 for days 15-21, 4 for days 22-28, 5 for days 29-31

**Explanation:** Groups days into weekly segments. Useful for intra-month analysis where you want to see patterns by week-of-month.

---

### Example 8: Same Day Check Across Dates
```
=IF(DAY(A1)=DAY(B1), "Same Day of Month", "Different Day")
```
**Result:** Compares day-of-month regardless of month/year

**Explanation:** Checks if two dates share the same day number. June 15 and December 15 return "Same Day of Month". Use for anniversary calculations.

---

### Example 9: Days Since Start of Month
```
=DAY(A1)-1
```
**Result:** 14 (if A1 is March 15, representing 14 complete days since March 1)

**Explanation:** Simple subtraction gives elapsed days within the month. March 15 means 14 days have passed since the month started.

---

### Example 10: Adjust Day to End of Month
```
=IF(DAY(A1)>DAY(EOMONTH(DATE(B1,C1,1),0)), DAY(EOMONTH(DATE(B1,C1,1),0)), DAY(A1))
```
**Result:** Caps day at maximum for target month

**Explanation:** If trying to apply day 31 to April (which has 30 days), this caps it at 30. Prevents invalid date creation when moving dates between months.

---

### Example 11: Create Same Day Next Month
```
=DATE(YEAR(A1), MONTH(A1)+1, DAY(A1))
```
**Result:** Same day next month (with potential overflow)

**Explanation:** Uses DAY to preserve the day-of-month. Warning: January 31 + 1 month = March 3 (because Feb 31 overflows). Use EDATE for smarter month addition.

---

### Example 12: Extract Day from Text Date
```
=DAY(DATEVALUE("March 15, 2026"))
```
**Result:** 15

**Explanation:** DATEVALUE converts text to a date serial number, then DAY extracts the day component. Useful for parsing imported text data.

---

### Example 13: Business Day of Month
```
=NETWORKDAYS(DATE(YEAR(A1),MONTH(A1),1), A1)
```
**Result:** Which business day of the month (excluding weekends)

**Explanation:** Counts working days from month start to the date. March 15 might be the 10th business day. Add holidays parameter for more accuracy.

---

### Example 14: Day of Year (Ordinal Date)
```
=A1-DATE(YEAR(A1),1,0)
```
**Result:** Day number in the year (1-366)

**Explanation:** Subtracting December 31 of prior year (day 0 of current year) gives ordinal date. March 15, 2026 = day 74. Not DAY function directly, but related concept.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Argument is text that can't be parsed as a date | Ensure input is a valid date; use DATEVALUE for text strings |
| `#VALUE!` | Empty cell or error value in source | Validate inputs; use IFERROR for error handling |
| `0 returned` | Time-only value (serial number < 1) | Ensure source contains a full date, not just time |
| `Unexpected day` | Regional date format misinterpretation | "1/2/2026" could be Jan 2 (day 2) or Feb 1 (day 1); use unambiguous formats |
| `Day higher than expected` | Date overflow from DATE construction | DATE(2026,2,30) = March 2; the 30th "overflowed" February |

## Use Cases

### [[Invoice and Payment Due Date Calculation]]

**Scenario:** Calculate payment terms and identify invoices due on specific days of the month for cash flow planning.

**Implementation:**
```
=DATE(YEAR(A2), MONTH(A2)+1, DAY(A2))        (Same day next month)
=IF(DAY(B2)<=15, "Early", "Late")            (Early vs. late month billing)
=IF(DAY(TODAY())>=DAY(C2), "Due", "Not Yet") (Is invoice due yet this month?)
```

**Business Application:** Accounts payable teams identify which invoices fall on their payment processing days. Cash flow forecasting groups payables by day-of-month to predict daily cash needs. Vendors paid "Net 30, same day" calculations use DAY to preserve due date patterns.

**Technical Details:** When due dates fall on non-existent days (e.g., 31st in a 30-day month), decide on business rules: cap at month end, or move to next valid day. Handle explicitly with formulas like MIN(DAY(A2), DAY(EOMONTH(target_month, 0))).

---

### [[Payroll and Recurring Payment Processing]]

**Scenario:** Identify payroll processing dates and calculate work days for employees paid on specific days of the month.

**Implementation:**
```
=IF(OR(DAY(A2)=1, DAY(A2)=15), "Standard Payday", "")
=IF(AND(DAY(A2)=15, WEEKDAY(A2,2)>5), "Move to Friday", "Process Normal")
=NETWORKDAYS(DATE(YEAR(A2),MONTH(A2),1), A2)  (Work days elapsed this period)
```

**Business Application:** Payroll systems flag processing dates automatically. HR reports show pay period progress for time-tracking. Finance forecasts biweekly cash requirements based on day-of-month patterns.

**Technical Details:** Real payroll systems must handle weekends and holidays. If the 15th is Sunday, pay Friday the 13th or Monday the 16th? Document your policy and encode it: =IF(WEEKDAY(DATE(y,m,15),2)=6, DATE(y,m,14), IF(WEEKDAY(DATE(y,m,15),2)=7, DATE(y,m,16), DATE(y,m,15)))

---

### [[Subscription Billing Cycle Management]]

**Scenario:** Manage subscription billing where customers are charged on their anniversary day each month.

**Implementation:**
```
=DAY(B2)                                                          (Customer's billing day)
=IF(DAY(TODAY())=DAY(B2), "Bill Today", "Not Billing Day")
=DATE(YEAR(TODAY()), MONTH(TODAY()), MIN(DAY(B2), DAY(EOMONTH(TODAY(),0))))  (This month's billing date, capped at month end)
```

**Business Application:** Subscription platforms identify which customers are due for billing each day. Revenue recognition systems allocate monthly charges based on billing day. Customer service knows each subscriber's next billing date instantly.

**Technical Details:** The MIN formula handles customers who signed up on the 31st—in February, they're billed on the 28th (or 29th). This is the standard "bill on anniversary or last day of month, whichever is earlier" pattern.

---

### [[Monthly Report Cutoff and Period Identification]]

**Scenario:** Determine whether transactions fall before or after monthly cutoff dates for financial reporting periods.

**Implementation:**
```
=IF(DAY(A2)<=5, "Prior Month Accrual", "Current Month")   (5-day cutoff for late entries)
=IF(DAY(A2)>DAY(EOMONTH(A2,0))-3, "Month-End Close", "Normal Processing")
=DAY(EOMONTH(TODAY(),0))-DAY(TODAY())                     (Days until month-end close)
```

**Business Application:** Accounting teams identify transactions needing period adjustment. Close processes flag last-day-of-month entries for review. Management reports show how close we are to month-end cutoff.

**Technical Details:** Cutoff rules vary by organization. Some close on the 25th for reporting; others use actual month end. Parameterize cutoff day in a named cell for easy adjustment rather than hardcoding.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Date system:** Works with both 1900 and 1904 date systems
- **Range:** Returns 1-31 depending on the date
- **Text parsing:** Parses text dates according to regional settings
- **Edge case:** DAY(0) returns 0 (the fictional January 0, 1900)

### Google Sheets
- **Availability:** All versions
- **Date system:** Uses 1899 epoch
- **Range:** Same as Excel, 1-31
- **Text parsing:** Similar to Excel, may differ on ambiguous formats
- **Edge case:** DAY(0) returns 30 (December 30, 1899)

### Key Difference Alert
The DAY(0) edge case differs: Excel returns 0 (from the fictional January 0, 1900) while Sheets returns 30 (from December 30, 1899). Since serial number 0 isn't used for real dates, this is only relevant for edge case testing. For all practical dates, behavior is identical.

## Tips and Best Practices

1. **Use DAY with EOMONTH for month-end logic:** DAY(EOMONTH(A1,0)) gives the last day of the month (28, 29, 30, or 31). Compare with DAY(A1) to identify month-end dates.

2. **Handle end-of-month transfers carefully:** When moving a date from a 31-day month to a 30-day month, DAY preserves the 31, causing DATE to overflow to the next month. Use MIN(DAY(A1), DAY(EOMONTH(target,0))) to cap appropriately.

3. **Create helper columns for day numbers:** In large datasets, a =DAY(A1) helper column simplifies SUMIF, COUNTIF, and PivotTable analysis by day-of-month.

4. **Remember DAY returns 1-31, not 0-30:** Unlike some programming languages, spreadsheet days are 1-indexed. The first day is 1, not 0.

5. **Combine with WEEKDAY for business day analysis:** DAY tells you it's the 15th; WEEKDAY tells you it's a Tuesday. Together they answer "Is the 15th a business day this month?"

6. **Use for data validation:** Catch impossible dates in imported data: =IF(DAY(A1)>31, "Invalid", "OK") won't catch everything (DATE auto-corrects), but validates after the fact.

7. **Consider billing day edge cases:** If customers signed up on the 29th, 30th, or 31st, they need special handling in February. Document and test these scenarios explicitly.

8. **Use TEXT for ordinal display:** =DAY(A1)&IF(OR(DAY(A1)=11,DAY(A1)=12,DAY(A1)=13),"th",IF(MOD(DAY(A1),10)=1,"st",IF(MOD(DAY(A1),10)=2,"nd",IF(MOD(DAY(A1),10)=3,"rd","th")))) gives "1st", "2nd", "3rd", "4th", etc.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[YEAR]] | Extracts year component (1900-9999) | When you need the year portion of a date |
| [[MONTH]] | Extracts month component (1-12) | When you need the month portion of a date |
| [[WEEKDAY]] | Returns day of week (1-7) | When you need weekday (Mon/Tue/etc), not day-of-month |
| [[DAYS]] | Returns days between two dates | When calculating day differences, not extracting component |

### Commonly Used Together

**[[DATE]]** - Reconstruct dates with modified day

*Change day or find period boundaries:*
```
=DATE(YEAR(A1), MONTH(A1), 1)        // First of the month
=DATE(YEAR(A1), MONTH(A1), 15)       // 15th of the month
=DATE(YEAR(A1), MONTH(A1)+1, 0)      // Last of the month (day 0 trick)
```
Essential for creating fixed day-of-month dates or adjusting days while preserving month/year.

---

**[[YEAR]] / [[MONTH]]** - Complete date decomposition

*Extract all components:*
```
=YEAR(A1)    // Year portion
=MONTH(A1)   // Month portion
=DAY(A1)     // Day portion
```
Together these three functions fully decompose any date for manipulation or analysis.

---

**[[EOMONTH]]** - Month-end calculations

*Work with last day of month:*
```
=EOMONTH(A1, 0)                      // Last day of A1's month
=DAY(EOMONTH(A1, 0))                 // Number of days in A1's month (28-31)
=EOMONTH(A1, 0)-A1                   // Days remaining in month
```
Essential companion for month-end detection, days-remaining calculations, and period boundaries.

---

**[[TODAY]]** - Current day reference

*Dynamic day-of-month calculations:*
```
=DAY(TODAY())                        // Current day of month
=DAY(EOMONTH(TODAY(),0))-DAY(TODAY()) // Days remaining this month
=IF(DAY(TODAY())>=DAY(A1), "Due", "Not Due")
```
Enables dynamic month progress tracking and due date comparisons.

---

**[[IF]]** - Conditional day logic

*Day-based conditions:*
```
=IF(DAY(A1)=1, "Month Start", "")
=IF(DAY(A1)>15, "Second Half", "First Half")
=IF(AND(DAY(A1)>=1, DAY(A1)<=7), "Week 1", "Later")
```
Foundation for all day-based decision logic and classification.

---

**[[WEEKDAY]]** - Day of week companion

*Combine calendar day with weekday:*
```
=IF(AND(DAY(A1)=15, WEEKDAY(A1,2)<=5), "Payday", "Weekend - Adjust")
```
DAY tells you the calendar date; WEEKDAY tells you if it's a working day.

## Official Documentation

- **Microsoft Excel:** [DAY function](https://support.microsoft.com/en-us/office/day-function-8a7d1cbb-6c7d-4ba1-8ced-f8f2e75e8445)
- **Google Sheets:** [DAY function](https://support.google.com/docs/answer/3093040)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | One of the original functions |
| Excel 2007+ | All subsequent | No changes to function behavior |
| Excel for Mac | All versions | Same behavior as Windows version |
| Google Sheets | Original launch (2006) | Functionally identical to Excel |
| LibreOffice Calc | All versions | Compatible implementation |

---

*Last updated: 2026-01-10*
