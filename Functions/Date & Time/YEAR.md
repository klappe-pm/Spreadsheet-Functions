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
- year-component
- date-parsing
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Extract Year
- Get Year
- Year Component
tags:
- date
- year
- extraction
- date-component
---

# YEAR

## Description

**YEAR** extracts the year component from a date and returns it as a four-digit integer. Given any date value—whether from a cell, a calculation, or a date function like TODAY()—YEAR returns just the year portion as a number between 1900 and 9999. It's the fundamental function for year-based analysis, grouping, filtering, and calculations. When you need to know "what year is this date in?", YEAR is your answer.

Understanding YEAR requires understanding how Excel stores dates. Remember that dates are serial numbers (days since January 1, 1900). When you see "1/10/2026" in a cell, Excel stores 46032. YEAR extracts the year from this serial number, returning 2026. This extraction works the same whether the cell shows "January 10, 2026", "10-Jan-26", or "2026-01-10"—the underlying serial number is what matters, not the display format.

YEAR is one of three companion functions (along with MONTH and DAY) that decompose a date into its calendar components. These functions are essential for date manipulation: to add a year to a date, use DATE(YEAR(A1)+1, MONTH(A1), DAY(A1)). To compare just years regardless of month/day: IF(YEAR(A1)=YEAR(B1), "Same Year", "Different Year"). They're the building blocks for fiscal year calculations, age determination, anniversary detection, and year-over-year analysis.

**Handling edge cases:** YEAR of an invalid date returns #VALUE! error. YEAR of 0 returns 1900 (since serial number 0 maps to January 0, 1900, which Excel treats as December 31, 1899, but displays as January 0, 1900—a quirk of the 1900 date system bug). YEAR correctly handles leap years and works consistently across the valid date range. When given a datetime value (like NOW()), YEAR ignores the time component and returns just the year.

## Syntax

> [!f(x)] YEAR Syntax
>
> ```
> =YEAR(serial_number)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `serial_number` | Yes | A date value from which to extract the year. Can be a cell reference containing a date, a date function like TODAY() or DATE(), a serial number, or a text string that Excel can interpret as a date. |

### Return Value

Returns an integer representing the year, in the range 1900 to 9999. Note that YEAR returns a number, not a date—the result is just the integer 2026, not a date value.

## Examples

> [!f(x)] YEAR Examples

### Example 1: Extract Year from a Date Cell
```
=YEAR(A1)
```
**Result:** 2026 (if A1 contains January 10, 2026)

**Explanation:** The most basic use—extract the year component from a date. Works regardless of how the date is formatted in the cell. The result is the number 2026, which you can use in calculations.

---

### Example 2: Current Year
```
=YEAR(TODAY())
```
**Result:** 2026 (current year)

**Explanation:** Combines with TODAY() to get the current year. Useful for headers, footers, and calculations that need to reference the current year dynamically.

---

### Example 3: Year from a Constructed Date
```
=YEAR(DATE(2026, 1, 10))
```
**Result:** 2026

**Explanation:** Extracts year from a DATE function result. This pattern is useful for validating date construction or extracting components from calculated dates.

---

### Example 4: Calculate Age in Years
```
=YEAR(TODAY())-YEAR(A1)
```
**Result:** 35 (approximate age if A1 contains a birth year in 1991)

**Explanation:** Simple age calculation by subtracting birth year from current year. Note: This gives calendar year difference, not actual age. Someone born December 31, 1991 would show 35 in January 2026 but actually just turned 34.

---

### Example 5: Accurate Age Calculation
```
=YEAR(TODAY())-YEAR(A1)-IF(DATE(YEAR(TODAY()),MONTH(A1),DAY(A1))>TODAY(),1,0)
```
**Result:** 34 or 35 depending on whether birthday has occurred this year

**Explanation:** Adjusts for whether the birthday has passed this year. If today is before the birthday, subtract 1 from the year difference. DATEDIF(A1, TODAY(), "Y") is a cleaner alternative.

---

### Example 6: Check if Date is Current Year
```
=IF(YEAR(A1)=YEAR(TODAY()), "This Year", "Other Year")
```
**Result:** "This Year" or "Other Year"

**Explanation:** Compares years to classify dates. Essential for filtering current-year transactions, identifying new records, or separating current from historical data.

---

### Example 7: Year-Over-Year Comparison
```
=IF(YEAR(A1)=YEAR(B1)-1, "Prior Year", "Not Prior Year")
```
**Result:** Identifies if A1 is exactly one year before B1's year

**Explanation:** Compare years between two dates. Use for YoY analysis, matching records across years, or validating date relationships.

---

### Example 8: Extract Year from Text Date
```
=YEAR(DATEVALUE("January 10, 2026"))
```
**Result:** 2026

**Explanation:** DATEVALUE converts text to a date serial number, then YEAR extracts the year. Useful when importing data that contains dates as text.

---

### Example 9: Fiscal Year Calculation (July Start)
```
=YEAR(A1)+IF(MONTH(A1)>=7, 1, 0)
```
**Result:** Fiscal year for organizations using July-June fiscal year

**Explanation:** If the month is July or later, it belongs to the next calendar year's fiscal year. July 2025 through June 2026 is "FY 2026" for many organizations.

---

### Example 10: Years Between Two Dates
```
=YEAR(B1)-YEAR(A1)
```
**Result:** Calendar years between two dates (not complete years)

**Explanation:** Simple year difference. Note this counts calendar years crossed, not complete years elapsed. Use DATEDIF for complete years.

---

### Example 11: Generate Year List for Dropdown
```
=YEAR(TODAY())+ROW()-1
```
**Result:** Creates sequence of years when dragged down (2026, 2027, 2028...)

**Explanation:** ROW() returns the row number; subtracting 1 and adding to current year creates a dynamic year sequence. Use in data validation dropdowns.

---

### Example 12: Group by Decade
```
=FLOOR(YEAR(A1), 10)
```
**Result:** 2020 (for any date in 2020-2029)

**Explanation:** FLOOR rounds down to nearest 10, grouping years into decades. Useful for historical analysis, demographic grouping, or long-term trend visualization.

---

### Example 13: Century Calculation
```
=ROUNDUP(YEAR(A1)/100, 0)
```
**Result:** 21 (for years 2001-2100)

**Explanation:** Dividing by 100 and rounding up gives century number. Note that year 2000 is actually the last year of the 20th century by strict definition, but this formula gives practical "21st century" grouping.

---

### Example 14: Leap Year Check
```
=IF(OR(MOD(YEAR(A1),400)=0, AND(MOD(YEAR(A1),4)=0, MOD(YEAR(A1),100)<>0)), "Leap Year", "Not Leap Year")
```
**Result:** "Leap Year" or "Not Leap Year"

**Explanation:** A year is a leap year if divisible by 400, OR divisible by 4 but not by 100. 2024 is leap (divisible by 4, not by 100). 2100 is not (divisible by 100, not by 400).

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Argument is text that can't be parsed as a date | Ensure the input is a valid date or use DATEVALUE to convert recognizable text dates |
| `#VALUE!` | Cell contains an error value | Check source cell for errors; use IFERROR to handle gracefully |
| `1900 returned unexpectedly` | Input is 0 or very small number | Verify the cell actually contains a date, not a small number |
| `Wrong year from text` | Regional date format mismatch | Text "1/2/2026" may be Jan 2 or Feb 1 depending on locale; use unambiguous formats |
| `Decimal returned` | Cell formatted as date but contains text | YEAR doesn't error on numbers; ensure source is truly a date |

## Use Cases

### [[Year-Over-Year Financial Analysis]]

**Scenario:** Compare revenue, expenses, and other metrics between the current year and previous years for trend analysis and performance evaluation.

**Implementation:**
```
=SUMIF(A:A, YEAR(TODAY()), B:B)                          (This year total)
=SUMIF(A:A, YEAR(TODAY())-1, B:B)                        (Last year total)
=(SUMIF(A:A,YEAR(TODAY()),B:B)-SUMIF(A:A,YEAR(TODAY())-1,B:B))/SUMIF(A:A,YEAR(TODAY())-1,B:B)   (YoY growth %)
```
Where column A contains dates and column B contains values.

**Business Application:** Finance teams automatically separate current-year from prior-year transactions for comparative reporting. Executive dashboards show YoY growth rates that update as new data enters. Budget variance analysis compares actual performance to prior year baselines.

**Technical Details:** When using SUMIF with years, convert YEAR(TODAY()) to match date column format if needed. For complex analysis with multiple criteria, use SUMIFS with custom year-extraction helper columns.

---

### [[Employee Service Year Tracking]]

**Scenario:** Categorize employees by service years for benefits administration, recognition programs, and workforce planning.

**Implementation:**
```
=YEAR(TODAY())-YEAR(B2)                                  (Service years - approximate)
=DATEDIF(B2, TODAY(), "Y")                               (Complete service years)
=IF(YEAR(TODAY())-YEAR(B2)>=5, "Vested", "Not Vested")   (Vesting status)
```

**Business Application:** HR systems automatically calculate tenure for benefit eligibility, vacation accrual tiers, and service milestone awards. Workforce planning reports show experience distribution across the organization. Retirement eligibility calculations use years of service thresholds.

**Technical Details:** Simple year subtraction may overcount by 1 if the hire date anniversary hasn't occurred this year. DATEDIF with "Y" parameter gives accurate complete years. For specific anniversary date identification, compare MONTH and DAY.

---

### [[Product Lifecycle and Vintage Analysis]]

**Scenario:** Track product age, warranty status, and inventory vintage for quality control and depreciation calculations.

**Implementation:**
```
=YEAR(TODAY())-YEAR(C2)                                  (Product age in years)
=IF(YEAR(TODAY())-YEAR(C2)>3, "Out of Warranty", "Under Warranty")
=YEAR(C2)                                                (Manufacturing year for vintage grouping)
```

**Business Application:** Quality teams identify aging inventory requiring inspection or write-down. Customer service quickly determines warranty status from manufacture date. Supply chain analysis shows inventory age distribution to optimize ordering.

**Technical Details:** For precise warranty calculations (e.g., 3-year warranty expiring on exact anniversary), use DATE(YEAR(C2)+3, MONTH(C2), DAY(C2))>TODAY() rather than simple year arithmetic.

---

### [[Academic Year and Cohort Assignment]]

**Scenario:** Assign students or records to academic years, graduation cohorts, or fiscal year groupings based on dates.

**Implementation:**
```
=YEAR(A2)+IF(MONTH(A2)>=9, 1, 0)                         (Academic year starting September)
="Class of "&(YEAR(B2)+IF(MONTH(B2)>=9, 4, 3))           (Expected graduation year from enrollment)
=IF(YEAR(A2)=YEAR(B2), "Same Cohort", "Different Cohort")
```

**Business Application:** Educational institutions assign students to academic years automatically. Alumni systems group graduates by class year. Research studies identify participant cohorts for longitudinal analysis.

**Technical Details:** Academic and fiscal year definitions vary by institution. Always document which month marks the year boundary. Consider edge cases like students who enroll mid-year or graduate early/late.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions since Excel 1.0
- **Date system compatibility:** Works with both 1900 and 1904 date systems
- **Range:** Returns years from 1900 to 9999
- **Edge case:** YEAR(0) returns 1900 (maps to the fictional January 0, 1900)
- **Text handling:** Automatically parses recognizable date text in regional format

### Google Sheets
- **Availability:** All versions
- **Date system:** Uses 1899 epoch but returns years compatible with Excel
- **Range:** Similar to Excel, 1900-9999 for standard use
- **Edge case:** YEAR(0) returns 1899 (December 30, 1899 = serial 0 in Sheets)
- **Text handling:** Similar text-to-date parsing, may differ on ambiguous formats

### Key Difference Alert
The most significant difference is YEAR(0): Excel returns 1900 while Google Sheets returns 1899. This only matters when dealing with very old dates or serial number 0 specifically, which is rare in practice. For dates in the 20th and 21st centuries, behavior is identical across platforms.

## Tips and Best Practices

1. **Use YEAR for grouping, not sorting:** To sort by year, sort by the original date (oldest to newest). To group by year for reporting, extract YEAR into a helper column or use PivotTables.

2. **Combine YEAR with MONTH for fiscal years:** Fiscal year calculations typically need both: =YEAR(A1)+IF(MONTH(A1)>=fiscal_start_month, 1, 0). Document your fiscal year definition.

3. **Remember YEAR returns a number, not a date:** =YEAR(A1)+1 gives next year as a number (e.g., 2027), not a date. To get the same date next year, use DATE(YEAR(A1)+1, MONTH(A1), DAY(A1)).

4. **Handle text dates carefully:** YEAR("2026-01-10") may work, but YEAR(DATEVALUE("2026-01-10")) is more explicit and reliable, especially with regional format variations.

5. **Use for validation:** Check that years are reasonable: =IF(AND(YEAR(A1)>=2000, YEAR(A1)<=YEAR(TODAY())+1), "Valid", "Check Date"). Catches typos and data entry errors.

6. **Create year-based named ranges:** Define names like CurrentYear =YEAR(TODAY()) and use throughout your workbook. Easier to maintain and audit than repeated YEAR(TODAY()) calls.

7. **Consider performance in large datasets:** In worksheets with millions of rows, extracting YEAR into a helper column (calculated once) is more efficient than repeated YEAR() calls in other formulas.

8. **Watch for two-digit year confusion:** If importing data, ensure "1/1/26" is interpreted as 2026 not 1926. YEAR will return whatever Excel interpreted, so validate early.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[MONTH]] | Extracts month component (1-12) | When you need the month portion of a date |
| [[DAY]] | Extracts day component (1-31) | When you need the day-of-month portion |
| [[WEEKDAY]] | Returns day of week (1-7) | When you need to know what weekday a date falls on |
| [[WEEKNUM]] | Returns week number (1-54) | When grouping by week rather than year |

### Commonly Used Together

**[[DATE]]** - Reconstruct modified dates

*Change the year of a date:*
```
=DATE(YEAR(A1)+1, MONTH(A1), DAY(A1))    // Same date next year
=DATE(2026, MONTH(A1), DAY(A1))          // Change to specific year
```
The core pattern for date manipulation—extract, modify, reconstruct.

---

**[[MONTH]] / [[DAY]]** - Complete date decomposition

*Extract all components:*
```
=YEAR(A1)    // Year portion
=MONTH(A1)   // Month portion (1-12)
=DAY(A1)     // Day portion (1-31)
```
Together, these three functions completely decompose any date into its components.

---

**[[TODAY]]** - Current year reference

*Dynamic current-year calculations:*
```
=YEAR(TODAY())                           // Current year as number
=IF(YEAR(A1)=YEAR(TODAY()), "Current Year", "Other")
=YEAR(TODAY())-YEAR(A1)                  // Years since date in A1
```
Essential for age calculations, period identification, and dynamic reporting.

---

**[[DATEDIF]]** - Precise year differences

*Calculate complete years between dates:*
```
=DATEDIF(A1, TODAY(), "Y")               // Complete years elapsed
=DATEDIF(A1, B1, "Y")                    // Complete years between two dates
```
More accurate than YEAR(B1)-YEAR(A1) because it counts complete years, not calendar years crossed.

---

**[[IF]] / [[SUMIF]] / [[COUNTIF]]** - Conditional year-based logic

*Year-based conditions and aggregation:*
```
=IF(YEAR(A1)=2026, "This Year", "Other Year")
=SUMIF(years_column, 2026, values_column)
=COUNTIF(dates_column, ">=1/1/2026")
```
Apply conditions based on year for filtering, counting, and summing.

## Official Documentation

- **Microsoft Excel:** [YEAR function](https://support.microsoft.com/en-us/office/year-function-23adf6b4-f9e3-4fe2-8156-3a0e7baf5ff3)
- **Google Sheets:** [YEAR function](https://support.google.com/docs/answer/3093061)

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
