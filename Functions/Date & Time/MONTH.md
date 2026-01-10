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
- month-component
- date-parsing
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Extract Month
- Get Month
- Month Component
- Month Number
tags:
- date
- month
- extraction
- date-component
- seasonality
---

# MONTH

## Description

**MONTH** extracts the month component from a date and returns it as an integer from 1 to 12. January is 1, February is 2, and so on through December as 12. Given any valid date—from a cell, a calculation, or a date function—MONTH isolates just the month portion. This is fundamental for monthly reporting, seasonal analysis, and any workflow that groups or filters data by month.

Like its companion functions YEAR and DAY, MONTH works with Excel's serial number date system. When Excel stores a date like "March 15, 2026" (serial number 46096), MONTH extracts the 3 (for March) by calculating which month that serial number falls within. The display format of the date doesn't matter—whether the cell shows "Mar 15, 2026", "15/03/2026", or "2026-03-15", MONTH returns 3.

**MONTH is essential for seasonality and period-based analysis.** Retail businesses track sales by month to identify seasonal patterns. Finance teams group transactions into monthly buckets for reporting. HR analyzes hiring trends by month. The function enables aggregation across years: "What's our average March performance?" requires identifying all March dates regardless of year, which MONTH enables through conditions like IF(MONTH(A1)=3, ...) or SUMIF formulas.

The MONTH function returns only a number (1-12), not the month name. To display "January" instead of 1, use TEXT(A1, "mmmm") for full month name or TEXT(A1, "mmm") for abbreviation. To convert month numbers back to dates, combine with DATE: DATE(2026, MONTH(A1), 1) creates the first of whatever month A1's date is in.

## Syntax

> [!f(x)] MONTH Syntax
>
> ```
> =MONTH(serial_number)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `serial_number` | Yes | A date value from which to extract the month. Can be a cell reference containing a date, a date function like TODAY() or DATE(), a serial number, or a text string that Excel can interpret as a date. |

### Return Value

Returns an integer from 1 to 12 representing the month: 1=January, 2=February, 3=March, 4=April, 5=May, 6=June, 7=July, 8=August, 9=September, 10=October, 11=November, 12=December.

## Examples

> [!f(x)] MONTH Examples

### Example 1: Extract Month from a Date Cell
```
=MONTH(A1)
```
**Result:** 3 (if A1 contains March 15, 2026)

**Explanation:** The most basic use—extract the month number from a date. Returns 1-12 regardless of how the date is formatted. Works with any date format displayed in the cell.

---

### Example 2: Current Month
```
=MONTH(TODAY())
```
**Result:** 1 (in January 2026)

**Explanation:** Combines with TODAY() to get the current month number. Essential for dynamic reports that should adjust monthly: "show data for current month" formulas.

---

### Example 3: Month Name from Date
```
=TEXT(A1, "mmmm")
```
**Result:** "March" (if A1 contains March 15, 2026)

**Explanation:** While not MONTH function itself, this is how to get month names. "mmmm" = full name, "mmm" = abbreviation (Mar). Combine: =TEXT(DATE(2026, MONTH(A1), 1), "mmmm")

---

### Example 4: Convert Month Number to Name
```
=TEXT(DATE(2026, A1, 1), "mmmm")
```
**Result:** "July" (if A1 contains 7)

**Explanation:** When you have a month number (1-12) and need the name, create a dummy date with that month and format it. Any year and day work; only the month matters.

---

### Example 5: First Day of Date's Month
```
=DATE(YEAR(A1), MONTH(A1), 1)
```
**Result:** 3/1/2026 (if A1 contains March 15, 2026)

**Explanation:** Classic pattern: extract year and month, combine with day 1 to get month start. Essential for period boundaries in SUMIFS, COUNTIFS, and date range filtering.

---

### Example 6: Last Day of Date's Month
```
=DATE(YEAR(A1), MONTH(A1)+1, 0)
```
**Result:** 3/31/2026 (if A1 contains March 15, 2026)

**Explanation:** Adding 1 to month and using day 0 returns last day of original month. Handles 28/29/30/31-day months automatically. Critical for month-end calculations.

---

### Example 7: Check if Same Month
```
=IF(MONTH(A1)=MONTH(B1), "Same Month", "Different Month")
```
**Result:** "Same Month" or "Different Month"

**Explanation:** Compare month portions of two dates. Note: This compares months regardless of year. March 2025 and March 2026 show "Same Month". Add YEAR comparison for complete matching.

---

### Example 8: Filter by Specific Month
```
=IF(MONTH(A1)=12, "December", "Other Month")
```
**Result:** "December" for any December date

**Explanation:** Identify specific months for filtering or classification. Use in conditional formatting to highlight December dates, or in formulas to apply month-specific logic.

---

### Example 9: Quarter from Month
```
=ROUNDUP(MONTH(A1)/3, 0)
```
**Result:** 1, 2, 3, or 4

**Explanation:** Dividing month by 3 and rounding up gives quarter. Jan-Mar=Q1, Apr-Jun=Q2, Jul-Sep=Q3, Oct-Dec=Q4. Essential for quarterly reporting aggregation.

---

### Example 10: Months Between Two Dates
```
=(YEAR(B1)-YEAR(A1))*12 + (MONTH(B1)-MONTH(A1))
```
**Result:** Number of months between dates

**Explanation:** Calculates total months difference. Year difference * 12 + month difference. Note: This counts calendar months crossed, not complete months. DATEDIF(A1,B1,"M") is an alternative.

---

### Example 11: Same Month and Year Check
```
=IF(AND(MONTH(A1)=MONTH(B1), YEAR(A1)=YEAR(B1)), "Same Period", "Different Period")
```
**Result:** "Same Period" only if both month AND year match

**Explanation:** Complete month-period matching requires checking both components. March 2025 and March 2026 are now "Different Period".

---

### Example 12: Add Months to a Date
```
=DATE(YEAR(A1), MONTH(A1)+3, DAY(A1))
```
**Result:** Date 3 months after A1

**Explanation:** Add to the month component, DATE handles overflow automatically. If A1 is November 15, MONTH+3=14, which DATE converts to February of next year.

---

### Example 13: Fiscal Month (July Start)
```
=MOD(MONTH(A1)+5, 12)+1
```
**Result:** 1 for July, 2 for August, ... 12 for June

**Explanation:** For fiscal years starting July, convert calendar month to fiscal month. July becomes month 1, August becomes 2, through June as month 12.

---

### Example 14: Season from Month
```
=IF(OR(MONTH(A1)=12, MONTH(A1)<=2), "Winter", IF(MONTH(A1)<=5, "Spring", IF(MONTH(A1)<=8, "Summer", "Fall")))
```
**Result:** "Winter", "Spring", "Summer", or "Fall"

**Explanation:** Northern hemisphere seasons by month. Dec-Feb=Winter, Mar-May=Spring, Jun-Aug=Summer, Sep-Nov=Fall. Adjust boundaries for southern hemisphere or meteorological definitions.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Argument is text that can't be parsed as a date | Ensure input is a valid date; use DATEVALUE for text dates |
| `#VALUE!` | Empty cell or non-date value | Validate input cells; use IFERROR for graceful handling |
| `0 returned` | Passed a time-only value (serial < 1) | Times without dates have no month; ensure full date is provided |
| `Wrong month` | Regional date format misinterpretation | "1/2/2026" could be Jan 2 or Feb 1; use unambiguous formats |
| `Unexpected result` | Cell contains text that looks like a date | Verify with ISNUMBER: =ISNUMBER(A1) should be TRUE for real dates |

## Use Cases

### [[Monthly Sales Reporting]]

**Scenario:** Aggregate transaction data into monthly summaries for trend analysis, budget comparison, and performance tracking.

**Implementation:**
```
=SUMIFS(C:C, A:A, ">="&DATE(2026,MONTH(TODAY()),1), A:A, "<="&DATE(2026,MONTH(TODAY())+1,0))
=SUMPRODUCT((MONTH(A:A)=MONTH(TODAY()))*(C:C))     (All years' current month)
=MONTH(A2)                                         (Helper column for pivot tables)
```

**Business Application:** Finance teams generate monthly revenue summaries automatically. Sales managers track month-to-date progress versus targets. Executive dashboards show monthly trends across product lines.

**Technical Details:** For large datasets, a helper column with =MONTH(A1) is more efficient than embedding MONTH in every SUMIF. PivotTables can group dates by month automatically, but explicit MONTH columns give more control.

---

### [[Seasonal Inventory Planning]]

**Scenario:** Identify seasonal patterns in demand to optimize inventory levels and purchasing schedules.

**Implementation:**
```
=AVERAGEIFS(D:D, MONTH(A:A), MONTH(TODAY()))       (Average for current month across years)
=SUMPRODUCT((MONTH(A:A)=B1)*(D:D))/SUMPRODUCT((MONTH(A:A)=B1)*1)  (Average for month in B1)
=IF(MONTH(A1)>=11, "Holiday Season", IF(MONTH(A1)<=2, "Winter Clearance", "Regular"))
```

**Business Application:** Retailers identify which months historically see peak demand for specific products. Purchasing teams time orders based on seasonal lead time requirements. Marketing plans campaigns aligned with seasonal patterns.

**Technical Details:** Seasonal analysis requires multiple years of data. Use MONTH to group, then calculate averages or totals per month across all available years. Visualize with charts showing 12-month patterns.

---

### [[Subscription and Billing Cycle Management]]

**Scenario:** Manage monthly billing cycles, identify which customers are due for renewal, and track monthly recurring revenue.

**Implementation:**
```
=IF(MONTH(B2)=MONTH(TODAY()), "Due This Month", "Not Due")
=DATE(YEAR(TODAY()), MONTH(TODAY()), DAY(B2))     (This month's billing date for customer)
=IF(DAY(TODAY())>=DAY(B2), "Billed", "Pending")   (Status based on billing day)
```

**Business Application:** Subscription businesses identify customers with bills due this month. Accounting generates monthly invoice lists automatically. Finance forecasts monthly recurring revenue by counting active subscriptions.

**Technical Details:** Handle edge cases where billing day (e.g., 31st) doesn't exist in all months. Use MIN(DAY(B2), DAY(EOMONTH(TODAY(),0))) to cap billing day at month's last day.

---

### [[Academic Calendar and School Year Tracking]]

**Scenario:** Classify activities, absences, and grades by academic term based on month.

**Implementation:**
```
=IF(OR(MONTH(A1)>=9, MONTH(A1)<=1), "Fall Semester", IF(MONTH(A1)<=5, "Spring Semester", "Summer"))
=IF(AND(MONTH(A1)>=9, MONTH(A1)<=12), "Q1", IF(MONTH(A1)<=2, "Q2", IF(MONTH(A1)<=5, "Q3", "Summer")))
```

**Business Application:** Schools track attendance by semester automatically. Grading systems aggregate scores by academic term. Resource planning identifies high-activity versus low-activity months.

**Technical Details:** Academic calendars vary by institution. Parameterize semester boundaries (semester_start, semester_end) in named ranges for easy adjustment rather than hardcoding months.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Date system:** Works with both 1900 and 1904 date systems
- **Range:** Returns 1-12 for all valid dates
- **Text parsing:** Automatically parses recognizable date text per regional settings
- **Edge case:** MONTH(0) returns 1 (January 0, 1900 maps to January)

### Google Sheets
- **Availability:** All versions
- **Date system:** Uses 1899 epoch but returns same 1-12 values
- **Range:** Same as Excel
- **Text parsing:** Similar behavior, may differ on ambiguous formats
- **Edge case:** MONTH(0) returns 12 (December 30, 1899)

### Key Difference Alert
The only notable difference is MONTH(0): Excel returns 1 while Sheets returns 12. This stems from the different epoch dates (Excel: Jan 0, 1900; Sheets: Dec 30, 1899). In practice, serial number 0 is never used for actual dates, so this difference is academic. For any real-world date, MONTH behaves identically.

## Tips and Best Practices

1. **Create helper columns for month numbers:** In large datasets, adding a =MONTH(A1) helper column makes SUMIF, COUNTIF, and PivotTable operations faster and simpler than embedding MONTH in criteria.

2. **Pair with YEAR for complete period identification:** MONTH alone groups March 2025 and March 2026 together. For distinct month-periods, use both: =YEAR(A1)&"-"&MONTH(A1) or a combined check with AND.

3. **Use TEXT for display, MONTH for calculation:** When you need "March" for display, use TEXT(A1,"mmmm"). When you need 3 for math or comparisons, use MONTH(A1). Don't mix them up.

4. **Remember months are 1-indexed:** January is 1, not 0. Arrays/lists of month data should account for this if using MONTH as an index.

5. **Handle fiscal month conversions explicitly:** Document your fiscal year start month and create a named formula for fiscal month: =MOD(MONTH(date)-fiscal_start_month+12, 12)+1.

6. **Validate imported dates:** Use ISNUMBER to confirm cells contain true dates before applying MONTH. Text that looks like dates won't error but may give wrong results.

7. **Consider performance in massive datasets:** In multi-million row scenarios, repeated MONTH function calls add up. Pre-calculate month numbers in a dedicated column during data import.

8. **Use for conditional formatting:** Highlight all cells from a specific month: =MONTH($A1)=6 highlights June dates. Combine with YEAR for specific month-year highlighting.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[YEAR]] | Extracts year component (1900-9999) | When you need the year portion of a date |
| [[DAY]] | Extracts day component (1-31) | When you need the day-of-month portion |
| [[WEEKDAY]] | Returns day of week (1-7) | When you need the weekday, not calendar month |
| [[WEEKNUM]] | Returns week number (1-54) | When grouping by week rather than month |

### Commonly Used Together

**[[DATE]]** - Reconstruct dates with modified month

*Change month or find month boundaries:*
```
=DATE(YEAR(A1), MONTH(A1), 1)        // First of the month
=DATE(YEAR(A1), MONTH(A1)+1, 0)      // Last of the month
=DATE(YEAR(A1), MONTH(A1)+6, DAY(A1)) // 6 months later
```
Essential for creating period boundaries and date arithmetic.

---

**[[YEAR]] / [[DAY]]** - Complete date decomposition

*Extract all components:*
```
=YEAR(A1)   // Year portion
=MONTH(A1)  // Month portion
=DAY(A1)    // Day portion
```
Together these fully decompose any date for manipulation or analysis.

---

**[[TEXT]]** - Month names

*Display month names from numbers:*
```
=TEXT(A1, "mmmm")                    // "March"
=TEXT(A1, "mmm")                     // "Mar"
=TEXT(DATE(2026, MONTH(A1), 1), "mmmm") // Month name from number
```
Convert numeric months to readable names for reports and displays.

---

**[[EOMONTH]]** - End of month

*Month-end calculations:*
```
=EOMONTH(A1, 0)                      // Last day of A1's month
=EOMONTH(A1, -1)                     // Last day of previous month
=EOMONTH(TODAY(), 3)                 // End of month, 3 months from now
```
Often simpler than DATE(YEAR, MONTH+1, 0) approach for month-end dates.

---

**[[SUMIFS]] / [[COUNTIFS]]** - Conditional aggregation

*Aggregate by month:*
```
=SUMIFS(B:B, MONTH(A:A), 3)          // Sum where month=March (may need array formula)
=COUNTIFS(A:A, ">="&DATE(2026,3,1), A:A, "<="&DATE(2026,3,31))  // Count March 2026
```
Use with MONTH helper column or date range boundaries for best performance.

---

**[[IF]]** - Conditional month logic

*Month-based conditions:*
```
=IF(MONTH(A1)<=6, "H1", "H2")        // Half-year classification
=IF(MONTH(A1)=MONTH(TODAY()), "This Month", "Other")
```
Foundation for all month-based decision logic.

## Official Documentation

- **Microsoft Excel:** [MONTH function](https://support.microsoft.com/en-us/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8)
- **Google Sheets:** [MONTH function](https://support.google.com/docs/answer/3093052)

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
