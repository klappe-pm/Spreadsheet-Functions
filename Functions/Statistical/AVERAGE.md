---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- statistical
subTopics:
- arithmetic-mean
- central-tendency
- descriptive-statistics
- data-summarization
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Arithmetic Mean
- Mean
- Average Value
- AVG
tags:
- statistical
- average
- mean
- central-tendency
- aggregation
---

# AVERAGE

## Description

**AVERAGE** calculates the arithmetic mean of a set of numbers by summing all values and dividing by the count of those values. It is the most commonly used measure of central tendency in spreadsheets, answering the fundamental question: "What is the typical value in this dataset?" From calculating grade point averages to analyzing sales performance, AVERAGE is the go-to function for understanding what is "normal" in your data.

The function accepts multiple arguments including individual numbers, cell references, and ranges. It intelligently ignores text values, empty cells, and logical values (TRUE/FALSE) within referenced ranges, counting only numeric values for both the sum and the divisor. However, when you directly include a logical value or text representation of a number as an argument (not in a range), the behavior differs: TRUE counts as 1, FALSE as 0, and numeric text is converted. This distinction between direct arguments and range references trips up many users.

**Key gotcha:** AVERAGE ignores empty cells but includes zeros. This distinction matters enormously. If you have test scores of 85, 90, 0, and 95, the average is 67.5 (270/4), not 90 (270/3). That zero might represent a missed test (should be excluded) or an actual score of zero (should be included). For scenarios where you need to exclude zeros, use AVERAGEIF with a criteria of "<>0" instead.

**Platform behavior:** Excel and Google Sheets implement AVERAGE identically for standard use cases. Both handle up to 255 arguments, both ignore text and blanks in ranges, and both return #DIV/0! when no numeric values exist. The only notable difference arises with array formulas in older Excel versions, where AVERAGE may require Ctrl+Shift+Enter for array evaluation, while Google Sheets handles arrays natively.

## Syntax

> [!f(x)] AVERAGE Syntax
>
> ```
> =AVERAGE(number1, [number2], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number1` | Yes | The first number, cell reference, or range for which you want the average. Can be a single value, a range like A1:A100, or a named range. |
| `number2, ...` | No | Additional numbers, cell references, or ranges to include in the average. Up to 255 total arguments supported. |

### Return Value

Returns a numeric value representing the arithmetic mean (sum divided by count) of all numeric values in the arguments. Returns #DIV/0! if no numeric values are found. Returns #VALUE! if any direct argument cannot be interpreted as a number.

## Examples

> [!f(x)] AVERAGE Examples

### Example 1: Basic Numeric Average
```
=AVERAGE(10, 20, 30)
```
**Result:** 20

**Explanation:** The simplest case: (10 + 20 + 30) / 3 = 60 / 3 = 20. Direct numeric arguments are summed and divided by their count.

---

### Example 2: Average of a Range
```
=AVERAGE(A1:A5)
```
Where A1:A5 contains: 85, 90, 78, 92, 88

**Result:** 86.6

**Explanation:** Sums all five values (433) and divides by 5. This is the typical use case for calculating class averages, sales averages, or any dataset in a column or row.

---

### Example 3: Handling Empty Cells
```
=AVERAGE(A1:A5)
```
Where A1:A5 contains: 100, 200, [empty], [empty], 300

**Result:** 200

**Explanation:** Only the three numeric values count. The sum is 600, divided by 3 (not 5). Empty cells are completely ignored in both the sum and the count.

---

### Example 4: Handling Zeros vs. Empty Cells
```
=AVERAGE(A1:A5)
```
Where A1:A5 contains: 100, 200, 0, 0, 300

**Result:** 120

**Explanation:** Zeros ARE counted: (100 + 200 + 0 + 0 + 300) / 5 = 600 / 5 = 120. This differs significantly from the empty cell example. If those zeros should be excluded, use AVERAGEIF.

---

### Example 5: Text in Range is Ignored
```
=AVERAGE(A1:A5)
```
Where A1:A5 contains: 50, "N/A", 60, "Pending", 70

**Result:** 60

**Explanation:** Only the numeric values (50, 60, 70) are averaged. Text entries are silently skipped. This is helpful for data with mixed content but can mask data quality issues.

---

### Example 6: Multiple Ranges
```
=AVERAGE(A1:A10, C1:C10, E1:E10)
```
**Result:** Combined average of all three ranges

**Explanation:** All numeric values from all three ranges are pooled together. The function calculates one average across all 30 potential cells (minus any blanks or text).

---

### Example 7: Mixing Values and Ranges
```
=AVERAGE(A1:A5, 100, B1:B3)
```
**Result:** Average including the explicit 100 plus all values from both ranges

**Explanation:** You can combine individual values with ranges. The number 100 is included as one of the values to average. Useful for adding a benchmark or target to a calculation.

---

### Example 8: Direct Logical Values
```
=AVERAGE(1, 2, TRUE, FALSE, 3)
```
**Result:** 1.4

**Explanation:** When TRUE and FALSE are direct arguments (not in a range), they are converted: TRUE=1, FALSE=0. The calculation is (1 + 2 + 1 + 0 + 3) / 5 = 7 / 5 = 1.4. This differs from how logicals in ranges are handled (they would be ignored).

---

### Example 9: #DIV/0! Error - No Numeric Values
```
=AVERAGE(A1:A5)
```
Where A1:A5 contains: "No", "Data", "Available", [empty], [empty]

**Result:** #DIV/0!

**Explanation:** When no numeric values exist to average, Excel and Sheets cannot divide by zero, hence the error. Wrap in IFERROR to handle gracefully: `=IFERROR(AVERAGE(A1:A5), "No data")`.

---

### Example 10: Entire Column Average
```
=AVERAGE(A:A)
```
**Result:** Average of all numeric values in column A

**Explanation:** You can average an entire column without specifying exact row numbers. Only cells with numeric values are included. Useful for dynamic datasets that grow over time.

---

### Example 11: Average with Condition Comparison
```
=IF(AVERAGE(A1:A10) >= 70, "Passing", "Failing")
```
**Result:** "Passing" or "Failing" based on average

**Explanation:** Combine AVERAGE with IF for threshold-based classifications. Calculate the class average and immediately evaluate whether it meets a standard.

---

### Example 12: Weighted Average Workaround
```
=SUMPRODUCT(A1:A5, B1:B5) / SUM(B1:B5)
```
Where A1:A5 are values and B1:B5 are weights

**Result:** Weighted average of values

**Explanation:** AVERAGE treats all values equally. For weighted averages (like GPA calculation), use SUMPRODUCT divided by the sum of weights. This is a common pattern when values have different importance.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#DIV/0!` | No numeric values in the specified range(s) | Check for data entry errors. Use IFERROR to provide a default value. Verify range references are correct. |
| `#VALUE!` | Direct argument contains non-convertible text (e.g., "hello" as an argument, not in a range) | Ensure direct arguments are numbers, cell references, or ranges. Move text-containing cells into a range reference where they'll be ignored. |
| `Unexpected result` | Zeros are being included when they should be excluded | Use AVERAGEIF(range, "<>0") to exclude zero values from the calculation. |
| `Unexpected result` | Hidden rows are included in the average | AVERAGE includes hidden rows. Use AGGREGATE(1, 5, range) for average that ignores hidden rows. |
| `Result differs from expected` | Text-formatted numbers (numbers stored as text) are being skipped | Convert text-numbers to actual numbers using VALUE() or multiply by 1. Check for leading apostrophes. |

## Use Cases

### [[Student Grade Calculation]]

**Scenario:** A teacher needs to calculate final grades by averaging test scores, with different sections having different numbers of tests.

**Implementation:**
```
=AVERAGE(B2:F2)
```
Where B2:F2 contains test scores (some cells may be empty if fewer tests were given).

**Business Application:** Automates grade calculation across varying numbers of assessments. Teachers can add new test columns without modifying the formula. Empty cells for excused absences are automatically excluded.

**Technical Details:** For weighted categories (tests worth 60%, homework 40%), use: `=0.6*AVERAGE(Tests) + 0.4*AVERAGE(Homework)`. Consider AVERAGEIF to exclude zeros for missed assignments vs. actual zero scores.

---

### [[Sales Performance Benchmarking]]

**Scenario:** A sales manager compares individual rep performance against team and company averages to identify top performers and those needing coaching.

**Implementation:**
```
Individual Score: =B2/AVERAGE(B:B)*100
Comparison: =IF(B2>AVERAGE(B$2:B$50), "Above Average", "Below Average")
```

**Business Application:** Creates relative performance metrics that automatically adjust as the team changes. Enables fair comparison regardless of absolute numbers, which may vary by territory or season.

**Technical Details:** Lock the range with $ for consistent comparison when copying down. Consider using MEDIAN instead of AVERAGE if you have extreme outliers (one rep with extraordinarily high or low numbers skewing the average).

---

### [[Inventory Turnover Analysis]]

**Scenario:** Calculate average inventory levels over a period to determine turnover ratios and identify slow-moving stock.

**Implementation:**
```
Average Inventory: =AVERAGE(MonthlyInventory)
Turnover Ratio: =AnnualCOGS/AVERAGE(MonthlyInventory)
```

**Business Application:** Tracks how efficiently inventory converts to sales. High turnover indicates efficient operations; low turnover suggests overstocking or obsolescence. Critical for cash flow management and warehouse planning.

**Technical Details:** Use trailing averages (last 3, 6, or 12 months) to smooth seasonal variations. For beginning/ending inventory method: `=AVERAGE(BeginningInventory, EndingInventory)`.

---

### [[Response Time Monitoring]]

**Scenario:** IT support team tracks average ticket resolution times to meet SLA requirements and identify process bottlenecks.

**Implementation:**
```
Avg Resolution: =AVERAGE(ResolutionTimes)
SLA Status: =IF(AVERAGE(ResolutionTimes)<=TargetTime, "Meeting SLA", "SLA Breach")
```

**Business Application:** Provides real-time visibility into service level performance. Enables proactive management before SLA breaches occur. Supports capacity planning and staffing decisions.

**Technical Details:** Consider using AVERAGEIF to exclude outliers or segment by ticket priority. For time-based SLAs, ensure times are in consistent units (hours, minutes). MEDIAN may better represent "typical" resolution when extreme cases skew averages.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (Excel 97 onward)
- **Maximum arguments:** 255 arguments or cell references
- **Array behavior:** Pre-365 Excel may need Ctrl+Shift+Enter for array formulas containing AVERAGE
- **Ignores:** Text, empty cells, and logical values in ranges (but converts direct logical arguments)

### Google Sheets
- **Availability:** All versions since launch
- **Maximum arguments:** 255 arguments
- **Array behavior:** Native array formula support without special entry
- **Ignores:** Same behavior as Excel - text, empty cells, and logical values in ranges

### Key Difference Alert
There is no significant functional difference between Excel and Google Sheets for AVERAGE. Both platforms handle the function identically for standard use cases. The only practical difference is in array formula handling in older Excel versions, where Ctrl+Shift+Enter may be required.

## Tips and Best Practices

1. **Understand the zero vs. empty distinction:** Zeros are counted in the average; empty cells are not. Know your data: is a zero a valid value or a placeholder for missing data? Use AVERAGEIF with "<>0" criteria when zeros should be excluded.

2. **Use AVERAGEIF for conditional averages:** To average only values meeting specific criteria (like positive numbers, specific categories, or dates in a range), AVERAGEIF and AVERAGEIFS are more elegant than filtering data manually.

3. **Consider MEDIAN for skewed data:** AVERAGE is sensitive to outliers. If one extremely high or low value distorts your result, MEDIAN (the middle value) may better represent "typical." Compare both to understand your data distribution.

4. **Handle errors gracefully:** Wrap AVERAGE in IFERROR for ranges that might contain no numeric data: `=IFERROR(AVERAGE(A1:A10), 0)` prevents #DIV/0! errors from breaking your spreadsheet.

5. **Use TRIMMEAN for outlier resistance:** TRIMMEAN calculates the average after excluding a percentage of outliers from both ends. Useful for survey data or measurements where extreme values may be errors.

6. **Lock references appropriately:** When comparing values to an average, use absolute references (`$A$1:$A$10`) so the average range does not shift when copying the formula.

7. **Be aware of text-formatted numbers:** Numbers stored as text (often from imports) are ignored by AVERAGE. Look for the green triangle error indicator in Excel, or check if values are left-aligned (text) vs. right-aligned (numbers).

8. **Document your exclusions:** If you are using AVERAGEIF to exclude certain values, add a comment explaining why. Future users (including yourself) will appreciate understanding the business logic behind filtered calculations.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[AVERAGEA]] | Averages values, counting text as 0 and TRUE/FALSE as 1/0 | When you need text and logical values to contribute to the average |
| [[AVERAGEIF]] | Averages values meeting a single criterion | When you need to average only values that match a condition |
| [[AVERAGEIFS]] | Averages values meeting multiple criteria | When filtering by multiple conditions simultaneously |
| [[MEDIAN]] | Returns the middle value | When data has outliers that would skew the mean |
| [[TRIMMEAN]] | Averages excluding percentage of outliers | When you want automatic outlier exclusion |
| [[GEOMEAN]] | Geometric mean (nth root of product) | For growth rates, returns, or multiplicative processes |
| [[HARMEAN]] | Harmonic mean (reciprocal of arithmetic mean of reciprocals) | For rates, ratios, or averaging speeds |

### Commonly Used Together

**[[COUNT]]** - Counts numeric values

*Use with AVERAGE to show sample size:*
```
=TEXT(AVERAGE(A1:A100),"0.00") & " (n=" & COUNT(A1:A100) & ")"
```
Displays the average with the count of values, providing context for statistical significance.

---

**[[STDEV.S]] / [[STDEV.P]]** - Standard deviation

*Combine with AVERAGE for complete descriptive statistics:*
```
Mean: =AVERAGE(A1:A100)
StdDev: =STDEV.S(A1:A100)
```
Together, mean and standard deviation describe the center and spread of your data.

---

**[[MIN]] / [[MAX]]** - Minimum and maximum values

*Use with AVERAGE to show data range:*
```
="Range: " & MIN(A1:A100) & " to " & MAX(A1:A100) & ", Average: " & AVERAGE(A1:A100)
```
Provides context by showing the full range alongside the central tendency.

---

**[[IF]]** - Conditional logic

*Combine for threshold-based decisions:*
```
=IF(AVERAGE(Scores)>=PassingGrade, "Class Passed", "Remediation Needed")
```
Make automatic pass/fail or threshold decisions based on averages.

---

**[[ROUND]]** - Round to specified decimal places

*Clean up average display:*
```
=ROUND(AVERAGE(A1:A100), 2)
```
Averages often produce long decimal values. ROUND provides cleaner presentation.

## Official Documentation

- **Microsoft Excel:** [AVERAGE function](https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)
- **Google Sheets:** [AVERAGE function](https://support.google.com/docs/answer/3093615)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2.0 (1987) | Original function, one of the earliest statistical functions |
| Excel 2007 | AVERAGEIF, AVERAGEIFS introduced | Conditional averaging added |
| Excel 2010+ | All subsequent versions | No changes to core functionality |
| Excel 365 | Continuous updates | Native dynamic array support |
| Google Sheets | Original launch (2006) | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
