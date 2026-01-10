---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- lookup-reference
subTopics:
- index-selection
- value-list
- conditional-selection
- switch-case
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Index Selection
- Value Selector
- Switch Case
- List Selection
tags:
- lookup
- reference
- selection
- index
- choose
---

# CHOOSE

## Description

**CHOOSE** returns a value from a list based on an index number you provide. Think of it as a numbered menu: give it a 1, get the first item; give it a 2, get the second item; and so on. If you have options like "Low", "Medium", "High" and the index is 2, CHOOSE returns "Medium". This simple concept enables powerful techniques for converting codes to descriptions, selecting ranges dynamically, and replacing nested IF statements with cleaner, more maintainable formulas.

The function takes an index number followed by up to 254 values (or references). The index must be between 1 and the number of values provided—there is no zero-based option. Values can be text strings, numbers, cell references, ranges, named ranges, or even other formulas. This flexibility makes CHOOSE remarkably versatile: you can select not just single values, but entire ranges for functions like SUM, AVERAGE, or VLOOKUP to operate on.

**CHOOSE excels at replacing nested IFs for small, fixed value sets.** Instead of `=IF(A1=1,"Jan",IF(A1=2,"Feb",IF(A1=3,"Mar",...)))`, write `=CHOOSE(A1,"Jan","Feb","Mar",...)`. The formula is shorter, faster to write, easier to read, and simpler to modify. For lookups in larger or dynamic datasets, VLOOKUP or INDEX+MATCH are more appropriate; CHOOSE is ideal when you have a small, fixed set of options (typically 2-15 items) that rarely changes.

**Platform considerations:** CHOOSE works identically in Excel and Google Sheets. Both platforms support up to 254 value arguments, though practical formulas rarely exceed 10-20 options. In modern Excel (365) and Google Sheets, CHOOSE can return arrays when given array arguments, enabling sophisticated array-based selections. One important note: CHOOSE only evaluates the selected value, not all values in the list—this makes it efficient and safe to use with formulas that might be slow or produce errors in the non-selected positions.

## Syntax

> [!f(x)] CHOOSE Syntax
>
> ```
> =CHOOSE(index_num, value1, [value2], [value3], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `index_num` | Yes | A number between 1 and 254 specifying which value to return. 1 returns value1, 2 returns value2, etc. Can be a cell reference, calculation result, or literal number. |
| `value1` | Yes | The first value in the list. Can be a number, text string, cell reference, range, named range, or formula. |
| `value2...254` | No | Additional values in the list. Up to 253 additional values (254 total). Each can be any data type supported by value1. |

### Return Value

Returns the value from the list at the position specified by index_num. Returns #VALUE! error if index_num is less than 1 or greater than the number of values provided. Returns the result of a formula if the selected value is a formula. Returns a range reference if the selected value is a range (useful for passing to SUM, VLOOKUP, etc.).

## Examples

> [!f(x)] CHOOSE Examples

### Example 1: Basic Value Selection
```
=CHOOSE(2, "Apple", "Banana", "Cherry")
```
**Result:** "Banana"

**Explanation:** Index 2 selects the second value from the list. This is the simplest form of CHOOSE—selecting from a hardcoded list of text values.

---

### Example 2: Cell Reference as Index
```
=CHOOSE(A1, "Small", "Medium", "Large", "X-Large")
```
Where A1 contains 3

**Result:** "Large"

**Explanation:** The index comes from cell A1. If A1 is 1, result is "Small"; if 2, "Medium"; if 3, "Large"; if 4, "X-Large". This is how CHOOSE typically appears in real spreadsheets—with the index controlled by user input or another formula.

---

### Example 3: Converting Day Number to Name
```
=CHOOSE(WEEKDAY(A1), "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
```
**Result:** Returns the day name for the date in A1

**Explanation:** WEEKDAY returns 1-7 (Sunday-Saturday by default). CHOOSE converts this number to the actual day name. More readable than a VLOOKUP against a day table for this common conversion.

---

### Example 4: Converting Month Number to Name
```
=CHOOSE(MONTH(A1), "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
```
**Result:** Returns the abbreviated month name for the date in A1

**Explanation:** MONTH returns 1-12. CHOOSE maps each number to its corresponding month abbreviation. Alternative: TEXT(A1,"MMM"), but CHOOSE allows custom abbreviations or full names.

---

### Example 5: Replacing Nested IF Statements
```
Nested IF approach:
=IF(A1=1,"Poor",IF(A1=2,"Fair",IF(A1=3,"Good",IF(A1=4,"Very Good",IF(A1=5,"Excellent","Invalid")))))

CHOOSE approach:
=IFERROR(CHOOSE(A1,"Poor","Fair","Good","Very Good","Excellent"),"Invalid")
```
**Result:** Both return rating text for 1-5 scale

**Explanation:** The CHOOSE version is much cleaner and easier to modify. Adding a 6th rating requires adding one value to CHOOSE vs. adding another nested IF layer. IFERROR handles out-of-range indices.

---

### Example 6: Selecting Numeric Values
```
=CHOOSE(A1, 0.05, 0.10, 0.15, 0.20, 0.25)
```
Where A1 contains a tier number 1-5

**Result:** Returns the discount rate for the selected tier

**Explanation:** CHOOSE works with numbers, not just text. This returns discount percentages based on customer tier. Tier 1 gets 5%, Tier 5 gets 25%.

---

### Example 7: Selecting Cell References
```
=CHOOSE(A1, B1, B2, B3, B4, B5)
```
Where A1 contains 3

**Result:** Returns the value in cell B3

**Explanation:** Values can be cell references. If A1 is 3, the formula returns whatever is in B3. This creates a simple indexed lookup without needing VLOOKUP or INDEX.

---

### Example 8: Selecting Ranges for SUM
```
=SUM(CHOOSE(A1, B2:B10, C2:C10, D2:D10))
```
Where A1 contains 2

**Result:** Sums the range C2:C10

**Explanation:** CHOOSE can return entire ranges. Here, if A1 is 1, sums column B; if 2, sums column C; if 3, sums column D. The selected range passes to SUM for aggregation.

---

### Example 9: Selecting Named Ranges
```
=AVERAGE(CHOOSE(A1, NorthSales, SouthSales, EastSales, WestSales))
```
**Result:** Averages the sales for the region corresponding to A1

**Explanation:** Named ranges work just like regular ranges in CHOOSE. This enables user-selectable regions in dashboards where A1 is a dropdown with values 1-4 (or converted from region names).

---

### Example 10: Dynamic VLOOKUP Table Selection
```
=VLOOKUP(B2, CHOOSE(A1, Products!A:D, Services!A:D, Subscriptions!A:D), 3, FALSE)
```
**Result:** Performs VLOOKUP in the table corresponding to category in A1

**Explanation:** The entire table_array for VLOOKUP can be selected dynamically with CHOOSE. If A1 is 1, searches Products; if 2, Services; if 3, Subscriptions. Cleaner than INDIRECT for this use case.

---

### Example 11: Conditional Calculation Selection
```
=CHOOSE(A1, B1*0.1, B1*0.15+100, B1*0.2+250)
```
Where A1 is the plan type (1, 2, or 3) and B1 is the base amount

**Result:** Calculates cost based on selected pricing plan

**Explanation:** CHOOSE can contain formulas, not just static values. Each plan has a different calculation: Plan 1 is 10% of base, Plan 2 is 15% + $100, Plan 3 is 20% + $250. Only the selected formula is evaluated.

---

### Example 12: Creating a Rotation Schedule
```
=CHOOSE(MOD(ROW()-2, 4)+1, "Team A", "Team B", "Team C", "Team D")
```
**Result:** Cycles through teams as you copy the formula down rows

**Explanation:** MOD creates a repeating pattern (0,1,2,3,0,1,2,3...). Adding 1 shifts to 1-4 range for CHOOSE. This creates automatic rotation schedules, shift assignments, or cyclical patterns.

---

### Example 13: Quarter Selection from Month
```
=CHOOSE(ROUNDUP(MONTH(A1)/3, 0), "Q1", "Q2", "Q3", "Q4")
```
**Result:** Returns the quarter for any date

**Explanation:** MONTH gives 1-12. Dividing by 3 and rounding up converts to 1-4 (Q1-Q4). This is more elegant than nested IFs checking month ranges.

---

### Example 14: CHOOSE with Boolean Index
```
=CHOOSE((A1>100)+1, "Standard", "Premium")
```
**Result:** "Standard" if A1 <= 100, "Premium" if A1 > 100

**Explanation:** Boolean comparison returns TRUE (1) or FALSE (0). Adding 1 converts to 1 or 2 for CHOOSE. This is a compact way to select between two options based on a condition—essentially a two-option IF alternative.

---

### Example 15: Error-Safe CHOOSE with IFERROR
```
=IFERROR(CHOOSE(A1, "Low", "Medium", "High"), "Unknown")
```
**Result:** Returns category name or "Unknown" for invalid index

**Explanation:** If A1 is 0, negative, or greater than 3, CHOOSE returns #VALUE!. IFERROR catches this and returns "Unknown". Always consider wrapping CHOOSE when the index might be out of range.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | index_num is less than 1 | Ensure index is at least 1. Use MAX(1, index) if needed, or wrap in IFERROR. |
| `#VALUE!` | index_num is greater than number of values | Add more values to the list, or validate index before CHOOSE. Check that index matches expected range. |
| `#VALUE!` | index_num is text or non-numeric | Convert text numbers with VALUE(). Ensure the index cell contains a number, not text that looks like a number. |
| `#VALUE!` | index_num is decimal | CHOOSE truncates decimals (2.9 becomes 2), but very large decimals may cause issues. Use INT() or ROUND() explicitly. |
| `#NAME?` | Misspelled function or undefined named range | Check CHOOSE spelling. Verify named ranges in value arguments exist. |
| `#REF!` | One of the value arguments references deleted cells | Update the value arguments to reference valid cells/ranges. |
| `Unexpected result` | Index off by one | Remember CHOOSE is 1-indexed, not 0-indexed. If your source is 0-indexed, add 1 to the index. |
| `Empty result` | Selected value is an empty cell or blank string | This is not an error—CHOOSE returns what's there. Check the source cell for the selected value. |

## Use Cases

### [[Customer Tier Pricing Calculator]]

**Scenario:** An e-commerce platform has four customer tiers (Bronze, Silver, Gold, Platinum) with different discount percentages, free shipping thresholds, and reward multipliers. The checkout system needs to apply the correct pricing rules based on the customer's tier level stored as a number (1-4).

**Implementation:**
```
Customer Tier (B2): 1=Bronze, 2=Silver, 3=Gold, 4=Platinum

Discount Percentage:
=CHOOSE($B$2, 0%, 5%, 10%, 15%)

Free Shipping Threshold:
=CHOOSE($B$2, 100, 75, 50, 0)

Rewards Multiplier:
=CHOOSE($B$2, 1, 1.5, 2, 3)

Final Price Calculation:
=Subtotal * (1 - CHOOSE($B$2, 0, 0.05, 0.1, 0.15))
+IF(Subtotal < CHOOSE($B$2, 100, 75, 50, 0), ShippingCost, 0)

Display Tier Name:
=CHOOSE($B$2, "Bronze Member", "Silver Member", "Gold Member", "Platinum VIP")
```

**Business Application:** Tiered pricing, loyalty programs, subscription levels, service packages. Any scenario where customer classification determines multiple pricing parameters.

**Technical Details:** Each CHOOSE references the same tier cell ($B$2), ensuring consistency. Store tier as a number for calculations; use CHOOSE to display human-readable names. Adding a 5th tier requires adding one value to each CHOOSE formula. Consider creating a tier lookup table if you have more than 10-15 parameters per tier.

---

### [[Dynamic Report Period Selector]]

**Scenario:** A financial reporting dashboard allows users to select a time period (Monthly, Quarterly, Yearly) from a dropdown. Based on this selection, all aggregations should use the appropriate date grouping columns and summary ranges. The data has pre-calculated summaries in different column sets for each period type.

**Implementation:**
```
Data Layout:
Column A: Date
Column B-M: Monthly data (12 columns)
Column N-Q: Quarterly data (4 columns)
Column R: Yearly data

Period Selector (A1): Dropdown with 1=Monthly, 2=Quarterly, 3=Yearly

Revenue Summary:
=SUM(CHOOSE($A$1, B2:M2, N2:Q2, R2))

Period Count:
=CHOOSE($A$1, 12, 4, 1)

Average Per Period:
=SUM(CHOOSE($A$1, B2:M2, N2:Q2, R2)) / CHOOSE($A$1, 12, 4, 1)

Chart Data Range (Named Range):
ChartData = CHOOSE(Dashboard!$A$1, Data!$B:$M, Data!$N:$Q, Data!$R:$R)

Period Labels:
=CHOOSE($A$1, "Monthly View", "Quarterly View", "Annual View")
```

**Business Application:** Management reporting, dashboard period selection, multi-granularity analysis. Users can switch views without recreating reports.

**Technical Details:** CHOOSE selects different column ranges based on the period type. The chart named range (using CHOOSE) automatically adjusts the data source when period changes. This is more maintainable than INDIRECT-based solutions because the ranges are explicitly listed and don't rely on constructed text strings.

---

### [[Survey Rating to Text Converter]]

**Scenario:** A customer satisfaction survey collects numeric ratings (1-5 stars or 1-10 scale). Reports need to display these as human-readable labels, calculate sentiment distributions, and color-code responses. The system should handle different rating scales consistently.

**Implementation:**
```
5-Star Scale Conversion:
Rating Label: =CHOOSE(A2, "Very Poor", "Poor", "Average", "Good", "Excellent")
Sentiment: =CHOOSE(A2, "Negative", "Negative", "Neutral", "Positive", "Positive")
Color Code: =CHOOSE(A2, "Red", "Orange", "Yellow", "Light Green", "Green")

10-Point NPS Scale:
Category: =CHOOSE(MIN(A2, 3), "Detractor", "Detractor", "Passive", "Promoter")
(Where: 1-6=Detractor, 7-8=Passive, 9-10=Promoter)

Simplified 10-point to 3-category:
=CHOOSE(ROUNDUP(A2/3.34, 0), "Detractor", "Passive", "Promoter")

Conditional Formatting Approach:
=CHOOSE(A2, 1, 1, 2, 3, 3) -- Returns 1=Red, 2=Yellow, 3=Green format index
```

**Business Application:** Customer satisfaction reporting, NPS analysis, employee engagement surveys, product reviews aggregation.

**Technical Details:** Multiple CHOOSE formulas can convert the same numeric rating to different representations (text label, sentiment category, display color). This is more maintainable than complex IF logic. For conditional formatting, return a format index that cell formatting rules can interpret.

---

### [[Shift Schedule Generator]]

**Scenario:** A manufacturing plant operates three shifts (Day, Swing, Night) with four teams rotating through a defined pattern. The scheduler needs to automatically display which team works which shift for any given day, cycling through the rotation pattern indefinitely.

**Implementation:**
```
Base Date (A1): Start date of rotation cycle
Current Date Column (A2:A367): Dates for the year

Rotation Pattern (4-day cycle):
Day 1: Team A=Day, Team B=Swing, Team C=Night, Team D=Off
Day 2: Team A=Off, Team B=Day, Team C=Swing, Team D=Night
Day 3: Team A=Night, Team B=Off, Team C=Day, Team D=Swing
Day 4: Team A=Swing, Team B=Night, Team C=Off, Team D=Day

Team A Shift: =CHOOSE(MOD(A2-$A$1, 4)+1, "Day", "Off", "Night", "Swing")
Team B Shift: =CHOOSE(MOD(A2-$A$1, 4)+1, "Swing", "Day", "Off", "Night")
Team C Shift: =CHOOSE(MOD(A2-$A$1, 4)+1, "Night", "Swing", "Day", "Off")
Team D Shift: =CHOOSE(MOD(A2-$A$1, 4)+1, "Off", "Night", "Swing", "Day")

Formatting Shift Display:
=CHOOSE(MATCH(B2, {"Day","Swing","Night","Off"}, 0), "6AM-2PM", "2PM-10PM", "10PM-6AM", "")
```

**Business Application:** Manufacturing shift scheduling, hospital staff rotation, retail store coverage, call center scheduling. Any scenario with cyclical team rotations.

**Technical Details:** MOD creates the rotation pattern by calculating days since cycle start modulo cycle length. Each team's CHOOSE contains the same shifts but rotated by their position in the sequence. Copy formulas down for any date range. Changing rotation patterns requires updating the values in each team's CHOOSE formula.

## Platform Differences

### Microsoft Excel

- **Availability:** All versions from Excel 97 onward
- **Maximum values:** 254 value arguments (value1 through value254)
- **Array support:** Excel 365 supports array formulas with CHOOSE
- **Evaluation:** Only evaluates the selected value, not all values
- **Range returns:** Can return range references for use in other functions
- **Performance:** Non-volatile function; only recalculates when dependencies change

### Google Sheets

- **Availability:** All versions from Sheets' inception
- **Maximum values:** 254 value arguments (matching Excel)
- **Array support:** Supports ARRAYFORMULA with CHOOSE
- **Evaluation:** Only evaluates the selected value
- **Range returns:** Can return range references for use in other functions
- **Performance:** Non-volatile function; efficient calculation

### Key Differences

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Maximum values | 254 | 254 |
| Array formula support | Dynamic arrays (365) | ARRAYFORMULA |
| Volatility | Non-volatile | Non-volatile |
| Range as value | Full support | Full support |
| Formula as value | Full support | Full support |
| Named range as value | Full support | Full support |
| Index from formula | Supported | Supported |

## Tips and Best Practices

1. **Use CHOOSE to replace nested IFs for small option sets:** For 2-10 fixed options, CHOOSE is cleaner and more maintainable than nested IF statements. Each option is visible in the formula, and adding options means adding values, not restructuring logic.

2. **Remember that CHOOSE is 1-indexed:** Unlike many programming languages, CHOOSE starts at 1, not 0. If your source data is 0-indexed, add 1: `=CHOOSE(A1+1, "Option0", "Option1", "Option2")`.

3. **Wrap CHOOSE in IFERROR for user-facing formulas:** `=IFERROR(CHOOSE(A1, "A", "B", "C"), "Invalid selection")` handles out-of-range indices gracefully instead of displaying #VALUE!.

4. **Use CHOOSE to select ranges for aggregation functions:** `=SUM(CHOOSE(A1, Range1, Range2, Range3))` is cleaner than INDIRECT-based solutions and doesn't have volatility overhead.

5. **Leverage CHOOSE for code-to-description conversions:** Converting numeric codes (1, 2, 3) to meaningful text ("Low", "Medium", "High") is CHOOSE's sweet spot. It's faster to write and easier to read than VLOOKUP for small, fixed lists.

6. **Combine CHOOSE with MOD for cyclical patterns:** `=CHOOSE(MOD(ROW(), 4)+1, "A", "B", "C", "D")` creates repeating sequences. Useful for rotation schedules, alternating formatting, and pattern generation.

7. **Document your index-to-value mapping:** Since CHOOSE doesn't show what index 1 or 2 means, add a comment or reference cell documenting the mapping. Future maintainers will thank you.

8. **Consider VLOOKUP/INDEX for larger or dynamic option sets:** If you have more than 15-20 options, or if options might change frequently, a lookup table with VLOOKUP or INDEX+MATCH is more maintainable than a very long CHOOSE formula.

## Related Functions

### Similar Functions

| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[IF]] | Conditional logic returning one of two values | When you have exactly 2 options or need complex condition logic beyond simple index matching |
| [[IFS]] | Multiple conditions without nesting | When selection is based on conditions (A1>100, A1>50) rather than index numbers |
| [[SWITCH]] | Value-based selection | Excel 2019+/Sheets: when matching specific values rather than index positions |
| [[INDEX]] | Return value from array position | When selecting from a range rather than listed values, or for larger option sets |
| [[VLOOKUP]] | Lookup in table | When options are in a table column rather than listed in formula |

### Commonly Used Together

**[[MATCH]]** - Find position for index

*Combined to convert value to index for CHOOSE:*
```
=CHOOSE(MATCH(A1, {"S","M","L","XL"}, 0), "Small", "Medium", "Large", "X-Large")
```
MATCH finds the position of A1's value in the array, providing the index for CHOOSE. This enables value-based selection with descriptive outputs.

---

**[[WEEKDAY]]/[[MONTH]]** - Date component extraction

*Combined with CHOOSE for date-to-name conversion:*
```
=CHOOSE(WEEKDAY(A1), "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
=CHOOSE(MONTH(A1), "January", "February", ..., "December")
```
Date functions return 1-based numbers perfect for CHOOSE indexing.

---

**[[MOD]]** - Modulo for cycling patterns

*Combined with CHOOSE for rotation schedules:*
```
=CHOOSE(MOD(A1-1, 3)+1, "Team A", "Team B", "Team C")
```
MOD creates repeating patterns (0,1,2,0,1,2...) that map to CHOOSE indexes for cyclical selections.

---

**[[IFERROR]]** - Error handling

*Wrap CHOOSE for graceful error handling:*
```
=IFERROR(CHOOSE(A1, "Low", "Med", "High"), "Invalid")
```
Returns "Invalid" instead of #VALUE! when index is out of range.

---

**[[SUM]]/[[AVERAGE]]** - Aggregation functions

*Using CHOOSE-selected ranges:*
```
=SUM(CHOOSE(A1, NorthData, SouthData, EastData, WestData))
```
CHOOSE returns a range reference that SUM then aggregates. Enables user-selected data aggregation.

---

**[[VLOOKUP]]** - Lookup function

*Using CHOOSE for dynamic table selection:*
```
=VLOOKUP(B1, CHOOSE(A1, Table1, Table2, Table3), 2, FALSE)
```
CHOOSE selects which table VLOOKUP searches in, enabling category-based lookups.

## Official Documentation

- **Microsoft Excel:** [CHOOSE function](https://support.microsoft.com/en-us/office/choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc)
- **Google Sheets:** [CHOOSE function](https://support.google.com/docs/answer/3256172)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 97 (1997) | Original implementation with up to 29 values |
| Excel 2007 | Enhanced | Increased to 254 value arguments |
| Excel 2010 | Enhanced | Better array handling |
| Excel 2019/365 | Dynamic arrays | CHOOSE works with spilling array results |
| Google Sheets | Original launch (2006) | Full compatibility with 254 values |
| Google Sheets | 2018+ | Improved ARRAYFORMULA integration |

---

*Last updated: 2026-01-10*
