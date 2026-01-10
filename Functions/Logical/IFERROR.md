---
categories:
  - spreadsheet-functions
subCategories:
  - excel
  - sheets
topics:
  - logical
subTopics:
  - error-handling
  - error-trapping
  - formula-protection
  - defensive-programming
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - error-handler
  - trap-error
  - catch-error
  - error-replacement
tags:
  - logical
  - error-handling
  - errors
  - defensive-formulas
  - vlookup-errors
  - division-errors
  - excel
  - google-sheets
---

# IFERROR

## Description

The **IFERROR function** is a powerful error-handling function that evaluates a formula or expression and returns a specified value if an error occurs, or returns the result of the formula if no error occurs. It acts as a safety net for formulas that might produce errors under certain conditions, allowing spreadsheets to display meaningful alternative values instead of cryptic error codes like #N/A, #DIV/0!, #VALUE!, #REF!, #NAME?, #NUM!, or #NULL!. The function takes two arguments: the value or formula to evaluate, and the value to return if that evaluation results in any error. This simple two-argument structure makes IFERROR one of the most frequently used functions for building robust, production-ready spreadsheets that can handle imperfect data gracefully.

The primary use case for IFERROR is wrapping lookup functions (VLOOKUP, HLOOKUP, INDEX+MATCH, XLOOKUP) to handle situations where the lookup value is not found in the data. Without IFERROR, a VLOOKUP that cannot find a match returns #N/A, which can cascade through dependent formulas and make reports look unprofessional. With IFERROR, you can display "Not Found", 0, a blank cell (""), or any other appropriate value. Beyond lookups, IFERROR is essential for division operations (handling divide-by-zero), array formulas that might reference empty ranges, data connections that might fail, and any formula working with external or user-entered data that could be incomplete or malformed. The function has become so fundamental that it's almost reflexive for experienced spreadsheet users to wrap potentially error-prone formulas in IFERROR.

There are important gotchas and trade-offs when using IFERROR that every user should understand. First, IFERROR catches ALL error types indiscriminately, which can mask genuine problems in your formulas. If you have a typo in a cell reference (#REF!) or a formula syntax error (#NAME?), IFERROR will hide it and return your alternative value, making debugging much harder. This is why IFNA (which only catches #N/A errors) was later introduced and is often preferred for lookup functions. Second, the formula in the first argument is only evaluated once, but if you need to use its result in the error-alternative calculation, you must repeat the formula or use a helper cell—there's no built-in way to reference "the value that would have been returned." Third, IFERROR always evaluates the first argument completely before checking for errors, which can have performance implications for very complex formulas. Fourth, returning blank ("") might cause issues with subsequent calculations expecting numbers, so consider returning 0 instead when the result will be used in mathematical operations.

Platform behavior for IFERROR is nearly identical between Excel and Google Sheets, with both supporting the function since early versions. Excel introduced IFERROR in Excel 2007, making it available in virtually all modern Excel installations. Google Sheets has supported IFERROR since its inception. Both platforms treat all Excel/Sheets error types the same way. The only notable difference is in array handling: in Excel 365 with dynamic arrays, IFERROR can process entire arrays and return arrays where errors are replaced element-by-element. Google Sheets handles arrays natively with ARRAYFORMULA. For cross-platform compatibility, IFERROR is one of the safest functions to use since its behavior is consistent and it has been available for many years on both platforms.

## Syntax

> [!f(x)] IFERROR Syntax
>
> ```
> =IFERROR(value, value_if_error)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `value` | Yes | The value, cell reference, or formula to evaluate. If this argument results in an error, the function returns value_if_error. Can be any valid Excel/Sheets expression including formulas, cell references, arrays, or literal values. |
| `value_if_error` | Yes | The value to return if the first argument evaluates to an error. Can be a number, text string, cell reference, formula, empty string (""), or any valid Excel/Sheets value. This is returned for ANY error type: #N/A, #DIV/0!, #VALUE!, #REF!, #NAME?, #NUM!, #NULL!, #CALC!, #SPILL!. |

### Return Value

Returns the result of evaluating the first argument (value) if no error occurs. If any error occurs during evaluation of the first argument, returns the second argument (value_if_error). The function cannot distinguish between different error types—all errors are treated identically. If the first argument is itself an error value passed directly (not the result of a calculation), that error is also caught.

### Error Types Caught by IFERROR

| Error | Common Cause | Example |
|-------|--------------|---------|
| `#N/A` | Lookup function cannot find a match | VLOOKUP looking for value not in list |
| `#DIV/0!` | Division by zero | =A1/B1 when B1 is 0 or empty |
| `#VALUE!` | Wrong type of argument | =A1+B1 when B1 contains text |
| `#REF!` | Invalid cell reference | Reference to deleted cell or sheet |
| `#NAME?` | Unrecognized formula name | Typo in function name or undefined name |
| `#NUM!` | Invalid numeric value | =SQRT(-1) or number too large |
| `#NULL!` | Incorrect range operator | Space instead of colon in range |
| `#CALC!` | Calculation not supported (Excel 365) | Array formula engine error |
| `#SPILL!` | Spill range blocked (Excel 365) | Dynamic array has no room to spill |

## Examples

> [!f(x)] IFERROR Examples

### Example 1: VLOOKUP with Error Handling
```
=IFERROR(VLOOKUP(A1, B:C, 2, FALSE), "Not Found")
```
**Result:** Returns lookup value if found, or "Not Found" if A1's value doesn't exist in column B

**Explanation:** This is the most common IFERROR pattern. VLOOKUP returns #N/A when the lookup value isn't found. IFERROR catches this and returns "Not Found" instead. This makes reports more readable and prevents #N/A from cascading into other formulas that reference this cell.

---

### Example 2: Division with Zero Handling
```
=IFERROR(A1/B1, 0)
```
**Result:** Returns the division result, or 0 if B1 is zero or empty

**Explanation:** Division by zero produces #DIV/0! error. IFERROR returns 0 instead, which is often appropriate for calculations like profit margins or percentages when the denominator is zero. Consider whether 0, blank (""), or "N/A" is most meaningful for your use case.

---

### Example 3: Return Blank Instead of Error
```
=IFERROR(VLOOKUP(A1, Data, 2, FALSE), "")
```
**Result:** Returns lookup value if found, or an empty cell if not found

**Explanation:** Returning an empty string ("") makes cells appear blank when errors occur, useful for cleaner reports where "Not Found" text would clutter the display. Be cautious: blank cells can cause issues with subsequent calculations or charts expecting numeric values.

---

### Example 4: INDEX+MATCH with Error Handling
```
=IFERROR(INDEX(C:C, MATCH(A1, B:B, 0)), "No Match")
```
**Result:** Returns matching value from column C, or "No Match" if A1 isn't found in column B

**Explanation:** INDEX+MATCH is a powerful lookup combination, but MATCH returns #N/A when it can't find the value. Wrapping in IFERROR provides a clean alternative. This pattern is more flexible than VLOOKUP as it can look left and doesn't depend on column positions.

---

### Example 5: Nested Lookup with Fallback
```
=IFERROR(VLOOKUP(A1, PrimaryTable, 2, FALSE), IFERROR(VLOOKUP(A1, BackupTable, 2, FALSE), "Not in any table"))
```
**Result:** Searches PrimaryTable first, then BackupTable, returns "Not in any table" if both fail

**Explanation:** IFERROR can be nested to create fallback chains. This formula tries the primary lookup, and if that fails (returns error), tries a backup lookup. Only if both fail does it return the final message. Useful for data reconciliation where values might exist in different sources.

---

### Example 6: Percentage Calculation Protection
```
=IFERROR(ActualSales/TargetSales-1, "No Target Set")
```
**Result:** Returns percentage variance, or "No Target Set" if TargetSales is zero/empty

**Explanation:** Sales variance calculations commonly divide actual by target. When targets aren't set (zero), this errors. IFERROR provides a meaningful message explaining WHY the calculation couldn't be performed, which is more helpful than just showing 0 or blank.

---

### Example 7: Date Calculation Error Handling
```
=IFERROR(DATEDIF(StartDate, EndDate, "D"), "Invalid Dates")
```
**Result:** Returns number of days between dates, or "Invalid Dates" if dates are invalid or reversed

**Explanation:** DATEDIF errors when the start date is after the end date or when dates are invalid. IFERROR catches these data quality issues and returns a clear message. This is essential for user-entered dates where validation might not have caught all issues.

---

### Example 8: Array Formula Error Handling (Excel 365)
```
=IFERROR(FILTER(A:B, B:B>100), "No items over 100")
```
**Result:** Returns filtered rows where B>100, or message if no rows match

**Explanation:** In Excel 365, FILTER returns #CALC! error when no rows match the criteria. IFERROR catches this and returns a user-friendly message. Without IFERROR, dashboards would display cryptic errors when filters return no results.

---

### Example 9: Web Query Error Handling
```
=IFERROR(WEBSERVICE(A1), "URL Failed")
```
**Result:** Returns web data if successful, or "URL Failed" if the request fails

**Explanation:** Web data connections can fail for many reasons: invalid URL, server down, network issues. IFERROR ensures your spreadsheet remains functional even when external data sources are unavailable, displaying a clear message instead of cryptic errors.

---

### Example 10: Converting Text to Numbers Safely
```
=IFERROR(VALUE(A1), A1)
```
**Result:** Returns A1 as a number if convertible, or the original text if conversion fails

**Explanation:** VALUE converts text to numbers but errors on non-numeric text. This formula attempts conversion and falls back to the original value if it fails. Useful for data cleaning where some values might already be numbers and others are text representations.

---

### Example 11: XLOOKUP with IFERROR Override
```
=IFERROR(XLOOKUP(A1, B:B, C:C, "Default"), "Lookup Error")
```
**Result:** Uses XLOOKUP's built-in not-found value, but catches other errors

**Explanation:** XLOOKUP has a built-in not_found argument, but other errors (like #REF! from deleted columns) aren't caught by it. Wrapping in IFERROR provides comprehensive error protection. The "Lookup Error" only appears for errors OTHER than not-found.

---

### Example 12: Handling Multiple Operations
```
=IFERROR(SUM(A1:A10)/COUNT(A1:A10)*100, 0)
```
**Result:** Returns percentage if calculation succeeds, or 0 if any error occurs

**Explanation:** This formula calculates an average as a percentage. If the range is empty, COUNT returns 0 causing #DIV/0!. If the range contains only text, SUM or COUNT might behave unexpectedly. IFERROR catches any issue and returns 0, ensuring dependent calculations continue.

---

### Example 13: Protecting Against #REF! in Dynamic Ranges
```
=IFERROR(OFFSET(A1, 0, 0, COUNTA(A:A), 1), A1:A100)
```
**Result:** Returns dynamic range based on data, or fixed range A1:A100 if OFFSET fails

**Explanation:** Dynamic range formulas using OFFSET can fail if the calculation produces invalid dimensions. IFERROR falls back to a fixed range, ensuring charts, data validation lists, and other features depending on this named range continue working.

---

### Example 14: Logarithm Calculation Protection
```
=IFERROR(LOG(A1), "Invalid Input")
```
**Result:** Returns logarithm of A1, or "Invalid Input" for zero, negative, or non-numeric values

**Explanation:** LOG function errors for zero or negative inputs (#NUM!) and for text (#VALUE!). Scientific and financial calculations often encounter edge cases. IFERROR ensures these don't break downstream calculations or reports.

---

### Example 15: Multi-Cell Reference Validation
```
=IFERROR(A1&B1&C1&D1, "Missing Data")
```
**Result:** Concatenates all cells if valid, or "Missing Data" if any cell has an error

**Explanation:** If any referenced cell contains an error value, concatenation propagates that error. IFERROR catches cases where source data has issues, particularly useful when data is imported from external sources that might have partial failures.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Still shows error` | IFERROR syntax is wrong or not wrapping the error-generating formula | Verify the entire formula that generates errors is inside the first argument of IFERROR |
| `Masks real problems` | IFERROR hiding formula errors (#REF!, #NAME?) that indicate real issues | Use IFNA instead for lookup functions; review source formulas periodically for hidden errors |
| `Returns error value from value_if_error` | The second argument itself produces an error | Ensure value_if_error is error-free; wrap it in IFERROR if needed |
| `Performance issues` | Complex formula evaluated even though result isn't used | Consider IF+ISERROR for conditional evaluation when performance is critical |
| `Unexpected blanks affecting calculations` | Using "" as value_if_error in formulas that expect numbers | Use 0 instead of "" when the result feeds into mathematical calculations |
| `#VALUE! not caught` | IFERROR placed incorrectly in nested formula | Ensure IFERROR wraps the innermost error-generating function, or wraps the entire formula |
| `Double evaluation concerns` | Need to use the successful result in the alternative | Use LET function to store result once, or use helper cell: `=LET(x, VLOOKUP(...), IFERROR(x, ...))` |
| `Array mismatch in older Excel` | Using with array functions in Excel pre-365 | Use ARRAYFORMULA in Sheets or ensure array dimensions match in older Excel |

## Use Cases

### [[Financial Dashboard Error Protection]]

**Scenario:** A CFO dashboard pulls data from multiple sources including databases, other workbooks, and web services to display key financial metrics. Any single data source failure could cause errors to cascade across the dashboard, making it unusable for executive review.

**Implementation:**
```
Revenue Display:
=IFERROR(RevenueQuery, "Data Unavailable")

Profit Margin:
=IFERROR(
  (Revenue-COGS)/Revenue,
  IFERROR(
    (LastMonthRevenue-LastMonthCOGS)/LastMonthRevenue,
    "N/A"
  )
)

Year-over-Year Growth:
=IFERROR(
  (CurrentYear-PriorYear)/ABS(PriorYear),
  IFS(PriorYear=0, "New Metric", ISBLANK(PriorYear), "No Prior Data", TRUE, "Calc Error")
)
```

**Business Application:** Executive dashboards are frequently viewed in meetings where data source issues cannot be resolved immediately. IFERROR ensures the dashboard remains presentable, showing which metrics are unavailable rather than displaying confusing error codes. The nested IFERROR pattern provides fallback values (like last month's data) when current data is unavailable, maximizing the dashboard's usefulness even during data outages.

**Technical Details:** Layer your IFERROR protection strategically: wrap data source connections first, then wrap calculations that depend on those sources. Consider using helper columns for raw data with IFERROR, then building calculations on those protected values. This makes debugging easier since you can identify exactly where data issues occur. Log errors to a separate sheet using IF(ISERROR(...), timestamp & error location, "") for monitoring and troubleshooting.

---

### [[Customer Lookup and Validation System]]

**Scenario:** A sales order system uses VLOOKUP to retrieve customer information (name, address, credit limit, discount tier) from a customer master database. When salespeople enter unknown customer IDs, the system must handle the error gracefully and guide them to create a new customer record.

**Implementation:**
```
Customer Name:
=IFERROR(VLOOKUP(CustomerID, CustomerMaster, 2, FALSE), "** NEW CUSTOMER - Enter Details Below **")

Credit Limit:
=IFERROR(VLOOKUP(CustomerID, CustomerMaster, 5, FALSE), 0)

Discount Rate:
=IFERROR(VLOOKUP(CustomerID, CustomerMaster, 6, FALSE)/100, 0)

Validation Status:
=IF(
  ISERROR(VLOOKUP(CustomerID, CustomerMaster, 1, FALSE)),
  "NEW",
  IF(VLOOKUP(CustomerID, CustomerMaster, 7, FALSE)="Active", "VALID", "INACTIVE")
)
```

**Business Application:** Order entry systems must handle both existing and new customers. Rather than blocking order entry when a customer isn't found, IFERROR allows the order to proceed with default values while clearly flagging that customer setup is needed. This maintains productivity while ensuring data quality issues are visible and actionable.

**Technical Details:** Distinguish between IFERROR (for display values like names) and ISERROR with IF (for validation logic). The validation status example uses IF+ISERROR because it needs different logic for "not found" versus "found but inactive." For credit limits and discounts, returning 0 via IFERROR prevents calculations from breaking while effectively applying no discount/zero credit to unvalidated customers. Consider adding conditional formatting to highlight cells using IFERROR fallback values.

---

### [[Data Import and Transformation Pipeline]]

**Scenario:** A data analyst receives weekly CSV exports from multiple vendor systems. The data quality varies significantly, with some files containing blank cells, text in numeric fields, invalid dates, and missing required fields. The analyst needs to transform this data into a standardized format for reporting.

**Implementation:**
```
Safe Number Conversion:
=IFERROR(VALUE(SUBSTITUTE(SUBSTITUTE(A1, "$", ""), ",", "")), 0)

Safe Date Conversion:
=IFERROR(DATEVALUE(A1), IFERROR(A1*1, "Invalid Date"))

Calculated Field with Multiple Error Sources:
=IFERROR(
  ROUND(SafeRevenue / SafeUnits, 2),
  IFERROR(
    IF(SafeUnits=0, 0, "Data Error"),
    0
  )
)

Status Code Translation:
=IFERROR(
  INDEX(StatusLookup, MATCH(RawStatus, StatusCodes, 0), 2),
  "Unknown Status: " & RawStatus
)
```

**Business Application:** Data transformation is inherently error-prone when working with external data sources. Each vendor may format data differently, and data quality issues are common. A robust transformation pipeline uses IFERROR at each conversion step to prevent single bad records from breaking the entire import. The formulas continue processing good records while flagging problematic ones for manual review.

**Technical Details:** Build your transformation pipeline in stages, with IFERROR protection at each stage. Use helper columns: Column A = Raw Data, Column B = Cleaned Data (with IFERROR), Column C = Calculations on Cleaned Data. This makes it easy to identify where transformations fail. For the status translation, returning "Unknown Status: " concatenated with the raw value helps analysts identify new status codes that need to be added to the lookup table. Consider adding a final validation column that checks ISERROR across all transformed fields to flag records needing attention.

---

### [[Automated Report Generation System]]

**Scenario:** A business intelligence team builds automated reports that are generated and emailed to stakeholders each morning. The reports pull from live databases and calculate dozens of metrics. Any error in the report would require manual intervention, delaying distribution and reducing trust in the automated system.

**Implementation:**
```
Metric with Confidence Level:
=IFERROR(
  MetricCalculation,
  "[Data Issue]"
) & IFERROR(
  " (" & TEXT(ConfidenceCalculation, "0%") & " confidence)",
  ""
)

Summary Section:
="Revenue: " & IFERROR(TEXT(RevenueCalc, "$#,##0"), "Unavailable")
& " | Growth: " & IFERROR(TEXT(GrowthCalc, "+0.0%;-0.0%"), "N/A")
& " | Target: " & IFERROR(TEXT(TargetCalc, "$#,##0"), "Not Set")

Error Count for Monitoring:
=SUMPRODUCT(ISERROR(AllMetrics)*1)

Report Health Check:
=IF(ErrorCount>0, "REVIEW REQUIRED: " & ErrorCount & " metrics unavailable", "All metrics calculated successfully")
```

**Business Application:** Automated reports must be reliable. Stakeholders lose trust when they receive reports with error codes or when reports fail to send due to formula errors. IFERROR ensures reports always generate with the available data, while clearly marking unavailable metrics. The error count and health check provide quick visibility into report quality without requiring recipients to scan for issues.

**Technical Details:** For automated reports, consider a three-tier approach: (1) Individual metric formulas with IFERROR returning specific fallback values, (2) A hidden "error tracking" section that counts and lists errors for the IT team, (3) A visible "data quality" indicator for report recipients. Use TEXT within IFERROR to ensure consistent formatting. For emailed reports, the health check can be used to modify the email subject line (e.g., "Daily Report - REVIEW REQUIRED" vs. "Daily Report - Complete").

## Platform Differences

### Microsoft Excel

- **Availability:** Excel 2007 and later versions
- **Legacy alternative:** Prior to 2007, use `=IF(ISERROR(formula), error_value, formula)` (evaluates formula twice)
- **Array support:** In Excel 365, IFERROR works element-wise on arrays
- **Dynamic arrays:** Handles #SPILL! and #CALC! errors in Excel 365
- **Performance:** Single evaluation of the formula; more efficient than IF+ISERROR pattern
- **Named range support:** Can be used within named range definitions

### Google Sheets

- **Availability:** All versions since Google Sheets launch
- **Array support:** Works with ARRAYFORMULA for array processing
- **ERROR.TYPE integration:** Can combine with ERROR.TYPE for error categorization
- **Apps Script:** IFERROR behavior can be replicated in custom functions
- **Performance:** Efficient single evaluation; preferred over IF+ISERROR

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Version requirement | 2007+ | All versions |
| Array handling | Native in 365 | Via ARRAYFORMULA |
| #CALC! error support | Yes (365) | N/A (no #CALC! in Sheets) |
| #SPILL! error support | Yes (365) | N/A (no #SPILL! in Sheets) |
| Performance vs IF+ISERROR | Significantly better | Better |
| Maximum nesting depth | 64 levels | 50 levels |
| Works in named ranges | Yes | Yes |
| Works in conditional formatting | Yes | Yes |
| Works in data validation | Yes | Yes |

## Tips and Best Practices

1. **Prefer IFNA for lookup functions:** When using VLOOKUP, INDEX+MATCH, or XLOOKUP, use IFNA instead of IFERROR when you only want to catch "not found" errors. IFERROR catches ALL errors including #REF! and #NAME?, which can mask formula problems. IFNA only catches #N/A errors, making debugging easier.

2. **Choose appropriate fallback values:** Think carefully about what your fallback value should be: "" (empty) for display purposes, 0 for calculations that should continue, "Not Found" for user-facing lookups, or even a formula that provides alternative data. The right choice depends on how the result will be used.

3. **Don't over-protect formulas:** Not every formula needs IFERROR. Only wrap formulas that have legitimate error scenarios (lookups, division, external data). Wrapping everything masks real formula errors and makes spreadsheets harder to debug and maintain.

4. **Consider using LET to avoid formula repetition:** If you need to reference the successful value in complex ways, use LET: `=LET(result, VLOOKUP(...), IFERROR(result * 1.1, 0))`. This evaluates the lookup once and makes the formula more readable.

5. **Add error logging for production systems:** For important spreadsheets, create an error log that captures when IFERROR catches errors. Use something like: `=IF(ISERROR(formula), NOW()&": Error in Cell X", "")` in a logging area. This helps identify data quality issues over time.

6. **Test with actual error conditions:** Don't just assume IFERROR will work—test your formulas with conditions that actually produce errors. Delete a lookup value, enter zero for a divisor, break a reference. Verify the fallback value displays correctly.

7. **Document where IFERROR is used:** When auditing or maintaining spreadsheets, it's helpful to know which cells have error protection. Consider using a consistent comment pattern or creating a documentation sheet that lists all IFERROR-protected formulas.

8. **Be cautious with cascading IFERROR:** While nesting IFERROR can create useful fallback chains, too many levels become hard to maintain and debug. If you find yourself with more than 3 levels, consider a lookup table approach or helper columns instead.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[IFNA]] | Catches only #N/A errors | Preferred for lookup functions (VLOOKUP, MATCH) where you want to catch "not found" but not mask other errors |
| [[ISERROR]] | Returns TRUE if value is any error | Use with IF when you need conditional logic beyond simple replacement: `=IF(ISERROR(x), logic1, logic2)` |
| [[ISNA]] | Returns TRUE if value is #N/A specifically | Use with IF for #N/A-specific logic when IFNA doesn't provide enough control |
| [[ERROR.TYPE]] | Returns number indicating error type | Use when you need to handle different errors differently in complex error handling logic |
| [[AGGREGATE]] | Performs calculations ignoring errors | Use for SUM, AVERAGE, COUNT operations where you want to skip error values rather than replace them |

### Commonly Used Together

**[[VLOOKUP]]** - Most common function wrapped by IFERROR

*Protect VLOOKUP from "not found" errors:*
```
=IFERROR(VLOOKUP(A1, Table, 2, FALSE), "Not Found")
```
This is the quintessential IFERROR use case. Every VLOOKUP in a production spreadsheet should have error protection unless you specifically want #N/A to propagate.

---

**[[INDEX]] + [[MATCH]]** - Flexible lookup combination requiring error protection

*Protect INDEX+MATCH lookups:*
```
=IFERROR(INDEX(B:B, MATCH(A1, C:C, 0)), "No Match")
```
MATCH returns #N/A when it can't find a value. INDEX propagates this error. IFERROR catches it and returns a useful alternative.

---

**[[XLOOKUP]]** - Modern lookup with built-in error handling

*Add IFERROR as additional protection beyond XLOOKUP's not_found argument:*
```
=IFERROR(XLOOKUP(A1, B:B, C:C, "Not Found"), "Lookup Error")
```
XLOOKUP has a built-in not_found argument, but IFERROR catches other errors like #REF! that XLOOKUP doesn't handle.

---

**[[LET]]** - Avoid repeating formulas within IFERROR

*Use LET to evaluate once and reference multiple times:*
```
=LET(lookup_result, VLOOKUP(A1, Table, 2, FALSE),
     IFERROR(lookup_result & " (" & lookup_result*1.1 & ")", "Not Found"))
```
LET stores the lookup result in a variable, so you don't need to write the VLOOKUP twice if you need to use the result in the fallback calculation.

---

**[[IF]] + [[ISERROR]]** - More control than IFERROR

*Use IF+ISERROR when you need conditional logic based on error state:*
```
=IF(ISERROR(VLOOKUP(A1, Table, 2, FALSE)), ProcessNewCustomer(), ProcessExisting())
```
When you need to run different logic (not just return different values) based on whether an error occurred, IF+ISERROR provides more flexibility.

---

**[[TEXT]]** - Format numbers within IFERROR

*Format successful results while providing text fallback:*
```
=IFERROR(TEXT(Calculation, "$#,##0.00"), "N/A")
```
When the successful result needs formatting, put TEXT inside IFERROR. The error alternative can be any text since IFERROR already handles the error case.

---

**[[SUMPRODUCT]] + [[ISERROR]]** - Count errors in a range

*Count how many errors exist in a range:*
```
=SUMPRODUCT(ISERROR(A1:A100)*1)
```
Useful for data quality monitoring—count errors in a dataset to identify data issues. ISERROR returns TRUE/FALSE, multiplying by 1 converts to 1/0 for summing.

## Official Documentation

- **Microsoft Excel:** [IFERROR function](https://support.microsoft.com/en-us/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611)
- **Google Sheets:** [IFERROR function](https://support.google.com/docs/answer/3093304)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel 2007 | 2007 | Initial release; replaced IF+ISERROR pattern |
| Excel 2010 | 2010 | No changes |
| Excel 2013 | 2013 | No changes |
| Excel 2016 | 2016 | No changes; IFNA introduced as complement |
| Excel 2019 | 2019 | No changes |
| Excel 365 | 2018+ | Enhanced array support; handles #CALC! and #SPILL! errors |
| Excel for Mac | 2008+ | Full support matching Windows version |
| Excel Online | 2010+ | Full support |
| Google Sheets | 2006 | Available since Sheets launch |
| Google Sheets | 2014 | Improved array formula support |
| LibreOffice Calc | 3.4 (2011) | Added for Excel compatibility |
| Apple Numbers | 2013 | Full support |

---

*Last updated: 2026-01-10*
