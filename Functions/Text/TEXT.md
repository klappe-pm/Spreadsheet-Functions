---
categories:
  - spreadsheet-functions
subCategories:
  - excel
  - sheets
topics:
  - text-manipulation
  - number-formatting
subTopics:
  - format-codes
  - value-conversion
  - display-formatting
  - date-formatting
  - number-formatting
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - format-value
  - number-to-text
  - date-to-text
  - value-formatting
tags:
  - text
  - formatting
  - number-conversion
  - date-formatting
  - currency
  - excel
  - google-sheets
---

# TEXT

## Description

The TEXT function is one of the most versatile and essential functions in spreadsheet applications, serving as the primary tool for converting numeric values, dates, and times into formatted text strings according to a specified format code. Unlike simple number-to-text conversion, TEXT allows you to precisely control how the resulting text appears, including the number of decimal places, thousands separators, leading zeros, date component arrangements, currency symbols, percentage representations, and custom text elements. The function takes two arguments: the value to be converted and a format code string that defines how that value should be displayed as text. The output is always a text string, which means the result cannot be used directly in mathematical calculations without converting it back to a number, but it can be concatenated with other text, used in labels, and displayed exactly as specified.

The TEXT function is indispensable when you need to combine numbers or dates with text while maintaining specific formatting that would otherwise be lost during concatenation. When you concatenate a number directly using CONCATENATE or the ampersand operator, Excel converts the number to text using its default formatting, which means currency symbols, thousands separators, and specific decimal places are lost. For example, concatenating "Total: " with a cell containing $1,234.56 would produce "Total: 1234.56" without the TEXT function, but "Total: $1,234.56" with TEXT. The function is equally crucial for dates, which are stored internally as serial numbers; without TEXT, a date would display as a number like 45306 rather than "January 15, 2024". Common applications include creating dynamic report headers, generating formatted labels for charts, building invoice line items, preparing data for export to systems requiring specific text formats, and creating user-friendly displays of calculated values.

There are several critical gotchas and complexities to understand when working with the TEXT function. First, format codes are locale-sensitive, meaning that codes like "MM/DD/YYYY" may not work as expected in all regional settings, and decimal/thousands separators may behave differently based on system locale. Second, the result of TEXT is always a text string, so attempting to perform mathematical operations on the result will cause errors or unexpected results; use VALUE function if you need to convert back to a number. Third, format codes have specific syntax rules where placeholder characters like 0, #, and @ have special meanings, and literal text must often be enclosed in double quotes within the format string (requiring escaped quotes within the formula). Fourth, some format codes work differently or are unavailable in Google Sheets compared to Excel, particularly specialized codes for fractions, scientific notation, or conditional formatting within the format string. Fifth, when formatting dates and times, you must understand that Excel stores these as numbers (dates as integers representing days since December 30, 1899, and times as decimal fractions of a day), so the same numeric value can be formatted as either a date or a time depending on your format code.

Regarding platform differences between Excel and Google Sheets, the core TEXT function syntax and basic format codes work identically on both platforms, but there are notable variations in advanced features and code support. Excel supports a wider range of format codes, including specialized options for displaying numbers as fractions, conditional formatting within the format string (using brackets with color names or conditions), and certain locale-specific codes. Google Sheets supports most common format codes but may handle some edge cases differently, particularly with locale settings and custom format strings. Both platforms recognize the standard date and time placeholders (d, m, y, h, m, s) and number placeholders (0, #, ?,), but Excel has more extensive documentation and consistent behavior for obscure format codes. When building cross-platform spreadsheets, stick to common format codes and test thoroughly on both platforms to ensure consistent results.

## Syntax

> [!f(x)] TEXT Syntax
>
> ```excel
> =TEXT(value, format_text)
> ```
>
> **Parameters:**
>
> | Parameter | Description | Required |
> |-----------|-------------|----------|
> | `value` | The numeric value, date, time, or cell reference to be formatted as text. This can be a number, a date/time value, a cell reference containing a number or date, or a formula that returns a numeric result. Boolean values TRUE and FALSE are converted to 1 and 0 respectively before formatting. | Yes |
> | `format_text` | A text string enclosed in quotation marks that specifies how the value should be formatted. This uses format code syntax with special placeholder characters (0, #, ?, d, m, y, h, s, etc.) to define the output format. The format code determines decimal places, separators, date/time components, and other display characteristics. | Yes |

## Format Code Reference

### Number Format Codes

| Code | Description | Example Input | Example Format | Result |
|------|-------------|---------------|----------------|--------|
| `0` | Digit placeholder; displays zero if no digit | 5 | "000" | 005 |
| `#` | Digit placeholder; omits leading/trailing zeros | 5 | "###" | 5 |
| `?` | Digit placeholder; adds space for alignment | 5.2 | "???.???" | "  5.2  " |
| `.` | Decimal point | 1234.5 | "#.00" | 1234.50 |
| `,` | Thousands separator | 1234567 | "#,###" | 1,234,567 |
| `,` | Scales by 1000 (at end) | 1234567 | "#," | 1235 |
| `%` | Multiplies by 100, adds % | 0.15 | "0%" | 15% |
| `/` | Fraction display | 0.5 | "# ?/?" | 1/2 |
| `E+` `E-` | Scientific notation | 1234 | "0.00E+00" | 1.23E+03 |

### Date Format Codes

| Code | Description | Example (for Jan 5, 2024) |
|------|-------------|---------------------------|
| `d` | Day without leading zero | 5 |
| `dd` | Day with leading zero | 05 |
| `ddd` | Abbreviated day name | Fri |
| `dddd` | Full day name | Friday |
| `m` | Month without leading zero | 1 |
| `mm` | Month with leading zero | 01 |
| `mmm` | Abbreviated month name | Jan |
| `mmmm` | Full month name | January |
| `mmmmm` | First letter of month | J |
| `yy` | Two-digit year | 24 |
| `yyyy` | Four-digit year | 2024 |

### Time Format Codes

| Code | Description | Example (for 2:05:09 PM) |
|------|-------------|--------------------------|
| `h` | Hour without leading zero (12-hour) | 2 |
| `hh` | Hour with leading zero (12-hour) | 02 |
| `H` | Hour without leading zero (24-hour) | 14 |
| `HH` | Hour with leading zero (24-hour) | 14 |
| `m` | Minute without leading zero | 5 |
| `mm` | Minute with leading zero | 05 |
| `s` | Second without leading zero | 9 |
| `ss` | Second with leading zero | 09 |
| `AM/PM` | 12-hour indicator | PM |
| `A/P` | Abbreviated 12-hour indicator | P |
| `[h]` | Elapsed hours (can exceed 24) | 26 |
| `[m]` | Elapsed minutes | 1565 |
| `[s]` | Elapsed seconds | 93909 |

### Special Format Codes

| Code | Description | Example |
|------|-------------|---------|
| `"text"` | Literal text in format | "Total: "0 |
| `@` | Text placeholder | "Item: "@  |
| `\` | Escape next character | \$ displays $ |
| `_` | Skip width of next character | _( for alignment |
| `*` | Repeat character to fill | *- fills with dashes |
| `;` | Section separator | positive;negative;zero |

## Examples

### Example 1: Basic Number with Thousands Separator
```excel
=TEXT(1234567.89, "#,##0.00")
```
**Result:** `1,234,567.89`

**Explanation:** This format code adds thousands separators (commas) and displays exactly two decimal places. The # symbol represents optional digits that are only shown if present, while 0 represents required digits that show zeros if needed. This is the most common format for displaying currency amounts or large numbers in a readable format.

---

### Example 2: Currency Formatting
```excel
=TEXT(1234.5, "$#,##0.00")
```
**Result:** `$1,234.50`

**Explanation:** Adding the dollar sign before the format code includes it literally in the output. The format ensures thousands separators and exactly two decimal places, with trailing zeros added as needed (0.5 becomes 0.50). For other currencies, replace $ with the appropriate symbol or use locale-specific codes.

---

### Example 3: Percentage Formatting
```excel
=TEXT(0.156, "0.0%")
```
**Result:** `15.6%`

**Explanation:** The percent sign in the format code multiplies the value by 100 and appends the % symbol. The format "0.0%" displays one decimal place. This is essential when working with decimal ratios that need to be displayed as percentages for reports or presentations.

---

### Example 4: Leading Zeros for Fixed-Width Numbers
```excel
=TEXT(42, "00000")
```
**Result:** `00042`

**Explanation:** Each 0 in the format code represents a required digit position. If the number has fewer digits than the format specifies, leading zeros are added. This is crucial for product codes, employee IDs, invoice numbers, and any identifier that must maintain a fixed width.

---

### Example 5: Phone Number Formatting
```excel
=TEXT(5551234567, "(###) ###-####")
```
**Result:** `(555) 123-4567`

**Explanation:** Format codes can include literal characters like parentheses, spaces, and hyphens to format numbers into recognizable patterns. Each # represents a digit from the input value. This technique works for phone numbers, social security numbers, credit card numbers, and any structured numeric identifier.

---

### Example 6: Date in Long Format
```excel
=TEXT(A1, "MMMM D, YYYY")
```
Where A1 contains 1/15/2024

**Result:** `January 15, 2024`

**Explanation:** Date format codes use m for months, d for days, and y for years. Using four characters (mmmm) displays the full month name, while single d displays the day without a leading zero. This format is ideal for formal documents, letters, and reports where full date readability is important.

---

### Example 7: Date in ISO Format
```excel
=TEXT(A1, "YYYY-MM-DD")
```
Where A1 contains 1/15/2024

**Result:** `2024-01-15`

**Explanation:** ISO 8601 date format is the international standard, sorted correctly as text, and widely used in databases and programming. The format uses four-digit year, two-digit month, and two-digit day with hyphens as separators.

---

### Example 8: Date with Day Name
```excel
=TEXT(A1, "DDDD, MMMM D, YYYY")
```
Where A1 contains 1/15/2024

**Result:** `Monday, January 15, 2024`

**Explanation:** Four d characters (dddd) display the full day name. This format is perfect for meeting agendas, event schedules, and any context where knowing the day of the week is important alongside the date.

---

### Example 9: Time in 12-Hour Format with AM/PM
```excel
=TEXT(A1, "h:mm AM/PM")
```
Where A1 contains a time value of 2:30 PM

**Result:** `2:30 PM`

**Explanation:** The AM/PM code converts 24-hour time to 12-hour format with the appropriate indicator. Using single h omits the leading zero for hours less than 10, while mm ensures two-digit minutes. This format is standard for displaying times in user-facing applications.

---

### Example 10: Time in 24-Hour Format
```excel
=TEXT(A1, "HH:MM:SS")
```
Where A1 contains a time value of 2:30:45 PM

**Result:** `14:30:45`

**Explanation:** Uppercase H typically indicates 24-hour format in many contexts (though Excel actually uses context to determine this). This format includes hours, minutes, and seconds with leading zeros for each component.

---

### Example 11: Combined Date and Time
```excel
=TEXT(NOW(), "YYYY-MM-DD HH:MM:SS")
```
**Result:** `2024-01-15 14:30:45` (varies based on current time)

**Explanation:** The NOW() function returns the current date and time, which TEXT formats into a complete timestamp. This format is commonly used for logging, audit trails, and data exports where both date and time precision are required.

---

### Example 12: Custom Text with Number
```excel
=TEXT(1500, "$#,##0"" per month""")
```
**Result:** `$1,500 per month`

**Explanation:** Text within double quotes (escaped within the format string) is included literally in the output. This technique allows you to create complete phrases that include formatted numbers, useful for labels, descriptions, and user-friendly displays.

---

### Example 13: Scientific Notation
```excel
=TEXT(1234567890, "0.00E+00")
```
**Result:** `1.23E+09`

**Explanation:** Scientific notation format displays very large or very small numbers in exponential form. The format specifies two decimal places for the mantissa and two digits for the exponent. This is essential for scientific data, engineering calculations, and any context dealing with extreme values.

---

### Example 14: Fraction Display
```excel
=TEXT(0.375, "# ?/?")
```
**Result:** `3/8`

**Explanation:** The fraction format code converts decimal values to their fractional representation. The question marks allow variable-width numerators and denominators. Excel finds the closest fraction based on the number of ? placeholders used. Note: Fraction formatting may have limited support in Google Sheets.

---

### Example 15: Negative Numbers in Parentheses (Accounting Style)
```excel
=TEXT(-1234.56, "$#,##0.00_);($#,##0.00)")
```
**Result:** `($1,234.56)`

**Explanation:** Format codes can have multiple sections separated by semicolons for positive, negative, and zero values. The accounting format shows negative numbers in parentheses rather than with minus signs. The underscore followed by ) adds spacing equal to a parenthesis width for alignment.

---

### Example 16: Elapsed Time (Hours Exceeding 24)
```excel
=TEXT(A1, "[h]:mm:ss")
```
Where A1 contains 1.5 (representing 36 hours)

**Result:** `36:00:00`

**Explanation:** Square brackets around h allow hours to exceed 24, useful for calculating total time durations like project hours, timesheet totals, or elapsed time calculations that span multiple days.

---

### Example 17: Quarter and Year Display
```excel
=TEXT(A1, """Q""Q YYYY")
```
Where A1 contains 7/15/2024

**Result:** `Q3 2024`

**Explanation:** The Q format code in Excel extracts the quarter from a date. Text is wrapped in double quotes within the format string. This is useful for financial reports and quarterly analysis where dates need to be grouped by quarter.

---

### Example 18: Week Number
```excel
=TEXT(A1, "YYYY""-W""WW")
```
Where A1 contains 1/15/2024

**Result:** `2024-W03`

**Explanation:** The WW format code returns the week number of the year. Combined with the year and literal text, this creates ISO week notation useful for project planning, manufacturing schedules, and international business contexts.

---

### Example 19: Abbreviated Month-Year
```excel
=TEXT(A1, "MMM-YY")
```
Where A1 contains 7/15/2024

**Result:** `Jul-24`

**Explanation:** Three-letter month abbreviation with two-digit year creates a compact date format ideal for column headers, chart labels, and space-constrained displays where full dates are too long.

---

### Example 20: Conditional Formatting with Colors (Excel Only)
```excel
=TEXT(A1, "[Green]$#,##0.00;[Red]($#,##0.00);$0.00")
```
Where A1 contains -500

**Result:** `($500.00)` (displayed in red in Excel)

**Explanation:** Excel allows color names in brackets within format codes. The format has three sections: positive (green), negative (red), and zero. Note that the color only appears when the result is displayed in a cell with this custom format; TEXT function itself returns plain text but the color indicator is preserved in the format string structure.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | Invalid format code syntax or incompatible value type | Verify format code syntax; check that value is numeric or date/time compatible with format |
| `#NAME?` | Missing quotation marks around format code | Ensure format_text is enclosed in double quotes: `=TEXT(A1, "0.00")` not `=TEXT(A1, 0.00)` |
| `Numbers showing as serial numbers` | Using date format codes on non-date numeric values | Verify the source value is actually a date; use DATEVALUE to convert text dates first |
| `Dates showing as decimals` | Using number format codes on date values | Use date-specific format codes (d, m, y) for date values, not (#, 0) |
| `Wrong decimal/thousands separators` | Format codes display differently based on locale settings | Use locale-aware formats or explicitly set separators based on target audience region |
| `Month/minute confusion` | "m" interpreted incorrectly | Context determines meaning: m after h or before s means minutes; otherwise means month |
| `Unexpected text in output` | Unescaped characters in format code | Enclose literal text in double quotes within the format: """text""" or use backslash escape |
| `#ERROR!` in Google Sheets | Using Excel-only format codes | Use equivalent Sheets-compatible format codes; avoid Excel-specific features like color codes |
| `Empty result` | Format code sections skip zero values | Add a third section for zeros: "positive;negative;zero" format |
| `Result cannot be calculated` | TEXT output used in math operations | TEXT returns text string; use VALUE(TEXT(...)) or keep numbers unformatted for calculations |

## Use Cases

### [[Financial Reporting]]
- **Implementation**: Convert calculated financial metrics into properly formatted currency amounts for reports, statements, and presentations. Use TEXT to ensure consistent display of currency symbols, thousands separators, and decimal places across all financial figures. Format negative amounts in accounting style with parentheses or in red for visual distinction.
- **Business Application**: Financial statements require precisely formatted numbers that align properly and use appropriate currency notation. Income statements, balance sheets, and cash flow statements need consistent formatting for professional presentation. Budget variance reports benefit from conditional formatting that highlights positive and negative deviations.
- **Technical Details**: Use format codes like "$#,##0.00" for standard currency or "$#,##0.00_);[Red]($#,##0.00)" for accounting format with negative values in parentheses. Combine TEXT with CONCATENATE for inline labels like "Revenue: $1,234,567". Consider locale settings when deploying internationally; EUR or GBP symbols may be needed.

### [[Invoice and Document Generation]]
- **Implementation**: Generate professional invoices, purchase orders, and contracts by combining TEXT-formatted values with descriptive labels and line item details. Create invoice numbers with leading zeros, format line item amounts consistently, and display dates in appropriate formats for the document type.
- **Business Application**: Automated invoice generation requires consistent formatting of dates, amounts, quantities, and totals. Purchase orders need standardized document numbers and properly formatted pricing. Contracts require dates in formal formats and financial terms displayed clearly.
- **Technical Details**: Use TEXT(invoice_number, "000000") for six-digit invoice numbers. Format dates as TEXT(date, "MMMM D, YYYY") for formal documents. Create line items with TEXT(amount, "$#,##0.00") concatenated with descriptions. Consider using TEXT for quantities with appropriate decimal places based on product type.

### [[Data Export and Integration]]
- **Implementation**: Prepare data for export to external systems that require specific text formats for dates, numbers, and codes. Convert Excel dates to ISO format for databases, format account numbers with proper structure for banking systems, and ensure numeric codes maintain leading zeros when exported as text.
- **Business Application**: Integration with ERP systems often requires dates in YYYY-MM-DD format. Bank file exports need properly formatted account numbers and amounts. Government or regulatory filings have strict format requirements for numeric and date fields.
- **Technical Details**: Use TEXT(date, "YYYY-MM-DD") for ISO dates compatible with databases. Format amounts without symbols for numeric imports: TEXT(amount, "0.00"). Create fixed-width fields with TEXT(value, "0000000000") for mainframe systems. Export times as TEXT(time, "HH:MM:SS") for 24-hour format compatibility.

### [[Dashboard and Report Labels]]
- **Implementation**: Create dynamic labels and titles for dashboards that incorporate formatted values and dates. Build period descriptions like "Q3 2024 Revenue: $1.2M" where both the quarter designation and the formatted amount update automatically based on source data.
- **Business Application**: Executive dashboards need clean, formatted displays of KPIs with appropriate units and precision. Report titles must include date ranges that update automatically. Chart labels require formatted values that remain readable at various scales.
- **Technical Details**: Combine TEXT with CONCATENATE: "Q" & TEXT(date,"Q YYYY") for quarter labels. Use TEXT(amount/1000000, "$0.0""M""") for millions abbreviations. Create date ranges with TEXT(start_date, "MMM D") & " - " & TEXT(end_date, "MMM D, YYYY"). Format percentages with TEXT(pct, "0.0%") for consistent decimal places.

## Platform Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| **Basic Syntax** | =TEXT(value, format_text) | =TEXT(value, format_text) |
| **Number Format Codes** | Full support for 0, #, ?, ., , | Full support for basic codes |
| **Date Format Codes** | d, dd, ddd, dddd, m, mm, mmm, mmmm, mmmmm, y, yy, yyyy | Same codes supported |
| **Time Format Codes** | h, hh, m, mm, s, ss, AM/PM, [h], [m], [s] | Same codes supported |
| **Fraction Formatting** | Full support with ?/?, ??/??, etc. | Limited or no support |
| **Color Codes** | [Red], [Green], [Blue], etc. in format strings | Not supported in TEXT function |
| **Conditional Sections** | [>100]"High";[<50]"Low";"Medium" | Not supported |
| **Locale Format Codes** | [$-409] for US English, etc. | Different locale handling |
| **Currency Symbols** | Literal $ or locale codes | Literal symbols recommended |
| **Scientific Notation** | E+, E- fully supported | Generally supported |
| **Elapsed Time** | [h]:mm:ss works correctly | [h]:mm:ss works correctly |
| **Text in Format** | "text" within format code | "text" within format code |
| **Escape Character** | \ for single characters | \ for single characters |
| **Section Separators** | ; for positive;negative;zero;text | ; supported but limited |
| **Thousands Scaling** | , at end divides by 1000 | May work differently |

**Key Recommendations by Platform:**

For Excel:
- Take advantage of conditional format sections for positive/negative/zero handling
- Use color codes in custom number formats for cell formatting (not TEXT function output)
- Leverage locale codes for international date/number formats
- Fraction formats work reliably for specialized applications

For Google Sheets:
- Stick to standard format codes for maximum compatibility
- Avoid color codes and conditional format sections in TEXT
- Test fraction and specialized formats before relying on them
- Use simple format codes and handle complex cases with additional formulas

## Tips and Best Practices

1. **Always Enclose Format Codes in Quotes**: The format_text argument must be a text string. Always use double quotes: `=TEXT(A1, "0.00")`. Forgetting quotes is one of the most common errors.

2. **Remember TEXT Output is Text**: The result cannot be used in calculations. If you need to calculate with formatted numbers, keep the original number for calculations and use TEXT only for display. Use VALUE() to convert back if absolutely necessary.

3. **Use 0 for Required Digits, # for Optional**: Understanding the difference prevents unexpected formatting. `"00.00"` ensures at least two digits before and after the decimal; `"#.##"` displays only significant digits.

4. **Handle the Month/Minute Ambiguity**: The letter "m" means months when used with dates (after d or y) but minutes when used with times (after h or before s). Be aware of this context-sensitivity when building format codes.

5. **Test Edge Cases**: Always test your TEXT formulas with zero values, negative numbers, very large numbers, and boundary dates. Format codes often behave differently for edge cases.

6. **Use Consistent Formats Across Documents**: Establish standard format codes for your organization (date formats, currency formats, etc.) and use them consistently. Consider storing common formats in named cells for easy reference.

7. **Combine TEXT with CONCATENATE for Labels**: The most powerful use of TEXT is in combination with text concatenation: `="Total: " & TEXT(SUM(A:A), "$#,##0.00")`. This creates dynamic labels with properly formatted values.

8. **Document Your Format Codes**: Complex format codes can be difficult to understand later. Add comments or use a reference sheet that explains each format code used in critical formulas, especially for codes with multiple sections or special characters.

## Related Functions

### Similar Functions

| Function | Description | Key Difference from TEXT |
|----------|-------------|--------------------------|
| [[VALUE]] | Converts text to number | Opposite of TEXT; converts formatted text back to numeric value |
| [[FIXED]] | Formats number with fixed decimals | Simpler than TEXT but limited to decimal places and thousands separator |
| [[DOLLAR]] | Formats as currency | Specifically for currency; less flexible than TEXT for general formatting |
| [[NUMBERVALUE]] | Converts text to number with locale | Handles locale-specific number formats when converting text to numbers |
| [[T]] | Returns text if value is text | Simple type checking; returns empty for non-text values |

### Commonly Used Together

**[[CONCATENATE]]** - Combine formatted values with text labels

*Use TEXT with CONCATENATE to create formatted labels and descriptions:*
```excel
=CONCATENATE("Total Revenue: ", TEXT(B1, "$#,##0.00"), " (", TEXT(B1/B2, "0.0%"), " of target)")
```
This formula creates a complete sentence like "Total Revenue: $125,000.00 (94.5% of target)" by formatting both the currency amount and the percentage.

**[[IF]]** - Conditional formatting based on value

*Use IF with TEXT to apply different formats based on conditions:*
```excel
=IF(A1>=1000000, TEXT(A1/1000000, "0.0""M"""), IF(A1>=1000, TEXT(A1/1000, "0.0""K"""), TEXT(A1, "0")))
```
This formula displays numbers in abbreviated format: millions as "1.5M", thousands as "250K", and smaller numbers as-is.

**[[NOW]] and [[TODAY]]** - Current date/time formatting

*Use TEXT with NOW or TODAY to create formatted timestamps:*
```excel
=TEXT(NOW(), "YYYY-MM-DD HH:MM:SS")
```
This formula creates a precisely formatted timestamp of the current date and time, useful for logging and version tracking.

**[[SUM, AVERAGE, MAX, MIN]]** - Format calculation results

*Use TEXT with aggregate functions to display formatted results:*
```excel
="Average Sale: " & TEXT(AVERAGE(B2:B100), "$#,##0.00")
```
This formula calculates the average of a range and displays it with currency formatting as part of a label.

**[[LEFT, RIGHT, MID]]** - Extract portions of formatted text

*Use text extraction functions on TEXT output for specific components:*
```excel
=LEFT(TEXT(A1, "MMMM"), 3)
```
This formula gets the full month name and extracts just the first three characters for a custom abbreviated format.

**[[SUBSTITUTE]]** - Modify formatted output

*Use SUBSTITUTE to adjust TEXT output:*
```excel
=SUBSTITUTE(TEXT(A1, "#,##0.00"), ".", ",")
```
This formula formats a number with comma thousands separator, then swaps the decimal point for a comma (European format workaround).

## Official Documentation

- **Microsoft Excel**: [TEXT function](https://support.microsoft.com/en-us/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c)
- **Microsoft Excel**: [Number format codes](https://support.microsoft.com/en-us/office/number-format-codes-5026bbd6-04bc-48cd-bf33-80f18b4eae68)
- **Microsoft Excel**: [Format dates](https://support.microsoft.com/en-us/office/format-a-date-the-way-you-want-8e10019e-d5d8-47a1-ba95-db95123d273e)
- **Google Sheets**: [TEXT function](https://support.google.com/docs/answer/3094139)
- **Google Sheets**: [Date and number formats](https://support.google.com/docs/answer/56470)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| Excel 97 | 1997 | Original TEXT function with basic format codes |
| Excel 2003 | 2003 | Enhanced format code support, improved locale handling |
| Excel 2007 | 2007 | Additional format codes for new date/time features |
| Excel 2010 | 2010 | Improved compatibility with international formats |
| Excel 2013 | 2013 | Better support for custom format codes |
| Excel 2016 | 2016 | Enhanced number format engine, better locale support |
| Excel 365 | 2018+ | Continuous improvements, dynamic array compatibility |
| Google Sheets | 2006 | Original TEXT function release |
| Google Sheets | 2015 | Improved format code compatibility with Excel |
| Google Sheets | 2018 | Enhanced locale and regional format support |
| Google Sheets | 2021 | Performance improvements for large datasets |
| Excel for Web | 2020 | Full parity with desktop TEXT function |

## Comprehensive Format Code Reference

### Number Formatting Examples

| Value | Format Code | Result | Description |
|-------|------------|--------|-------------|
| 1234.5 | "0" | 1235 | Round to integer |
| 1234.5 | "0.0" | 1234.5 | One decimal place |
| 1234.5 | "0.000" | 1234.500 | Three decimals with trailing zeros |
| 1234.5 | "#,##0" | 1,235 | Thousands separator, integer |
| 1234.5 | "#,##0.00" | 1,234.50 | Thousands separator, two decimals |
| 0.5 | "0.00" | 0.50 | Show leading zero |
| 0.5 | "#.00" | .50 | Hide leading zero |
| 1234.5 | "$#,##0.00" | $1,234.50 | US currency format |
| 1234.5 | "#,##0.00 EUR" | 1,234.50 EUR | Euro with symbol after |
| 0.15 | "0%" | 15% | Percentage, integer |
| 0.156 | "0.0%" | 15.6% | Percentage, one decimal |
| 5 | "00000" | 00005 | Five-digit with leading zeros |
| 1234567 | "0.00E+00" | 1.23E+06 | Scientific notation |
| 1234567 | "#," | 1235 | Divide by 1000 |
| 1234567 | "#,," | 1 | Divide by 1000000 |
| -1234.5 | "#,##0.00;(#,##0.00)" | (1,234.50) | Negative in parentheses |

### Date Formatting Examples

| Date Value | Format Code | Result |
|------------|------------|--------|
| 1/5/2024 | "M/D/YYYY" | 1/5/2024 |
| 1/5/2024 | "MM/DD/YYYY" | 01/05/2024 |
| 1/5/2024 | "DD-MM-YYYY" | 05-01-2024 |
| 1/5/2024 | "YYYY-MM-DD" | 2024-01-05 |
| 1/5/2024 | "D MMMM YYYY" | 5 January 2024 |
| 1/5/2024 | "MMMM D, YYYY" | January 5, 2024 |
| 1/5/2024 | "DDDD, MMMM D, YYYY" | Friday, January 5, 2024 |
| 1/5/2024 | "DDD, MMM D" | Fri, Jan 5 |
| 1/5/2024 | "MMM-YY" | Jan-24 |
| 1/5/2024 | "MMMMM" | J |
| 1/5/2024 | "YY" | 24 |

### Time Formatting Examples

| Time Value | Format Code | Result |
|------------|------------|--------|
| 2:30:45 PM | "H:MM" | 14:30 |
| 2:30:45 PM | "h:mm AM/PM" | 2:30 PM |
| 2:30:45 PM | "HH:MM:SS" | 14:30:45 |
| 2:30:45 PM | "h:mm:ss a/p" | 2:30:45 p |
| 1.5 (36 hours) | "[H]:MM:SS" | 36:00:00 |
| 0.5 (12 hours) | "[M]" | 720 |
