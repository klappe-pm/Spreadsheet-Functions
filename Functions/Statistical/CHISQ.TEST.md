---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
use-case:
  - Shift Pattern Comparison
  - Survey Question Independence
  - Website Layout Comparison
related:
  - CHISQ.DIST.RT
  - CHISQ.INV.RT
  - CHITEST
  - SUM
  - T.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chisq-test-function
  - https://support.google.com/docs/answer/7004263
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Chi Squared Independence Test
  - Test For Independence
tags:
  - chi-squared
  - excel
  - hypothesis-testing
  - independence
  - sheets
---

# CHISQ.TEST

## Description

**CHISQ.TEST** tests whether two categorical variables are independent. You give it a table of observed counts and a table of expected counts with the same shape, and it returns the probability of seeing a chi-squared statistic at least as large as the one calculated, if the variables were in fact independent. A small result, such as 0.05 or lower, suggests the variables are related.

The expected table is built from the data. Each expected count equals its row total multiplied by its column total, divided by the grand total. Many analysts write this as a formula beside the observed table so the expected values update when the observed counts change. Example 1 shows the formula.

CHISQ.TEST replaces the older CHITEST function, which returns the same result. Use CHISQ.TEST in new Excel workbooks. Google Sheets documents this test under the name CHITEST, so use CHITEST there.

The test is most reliable when every expected count is at least 5. Many small expected counts make the chi-squared approximation weak, so combine categories or collect more data when that happens.

## Syntax

```excel
=CHISQ.TEST(actual_range, expected_range)
```

<!-- Image 1: Observed and Expected Tables. See Images/Statistical/CHISQ.TEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `actual_range` | Yes | The observed counts, one count per cell, arranged in rows and columns. |
| `expected_range` | Yes | The expected counts for the same cells. It must contain the same number of data points as `actual_range`. |

### Return Value

A probability between 0 and 1. Small values, such as 0.05 or lower, indicate that the observed pattern is unlikely under independence. The function returns `#N/A` when the two ranges have different numbers of data points or when both ranges are a single cell.

Degrees of freedom follow these rules. When the table has more than one row and more than one column, the degrees of freedom equal (rows minus 1) times (columns minus 1). When the table is a single row or a single column, the degrees of freedom equal the number of cells minus 1.

## Examples

### Example 1: Build the Expected Table With a Formula

Observed counts sit in `A2:B3`: row 2 holds 30 and 10, and row 3 holds 20 and 40. The expected table in `A6:B7` uses this formula in `A6`, filled across and down.

```excel
=SUM($A2:$B2)*SUM(A$2:A$3)/SUM($A$2:$B$3)
```

**Result:** `20` in `A6`, `20` in `B6`, `30` in `A7`, `30` in `B7`

Each cell multiplies its row total by its column total and divides by the grand total of 100.

### Example 2: Test a 2 by 2 Table

```excel
=CHISQ.TEST(A2:B3, A6:B7)
```

**Result:** `0.0000446` (rounded)

The chi-squared statistic for this table is 16.666667 with 1 degree of freedom. The very small result says these two counts are far from independent.

<!-- Image 2: Expected Counts From Row and Column Totals. See Images/Statistical/CHISQ.TEST.md -->

### Example 3: Test a Single Row

Observed counts in `A2:C2` are 50, 30 and 20. Expected counts in `A5:C5` are 40, 40 and 20.

```excel
=CHISQ.TEST(A2:C2, A5:C5)
```

**Result:** `0.0821` (rounded)

With one row and three columns the degrees of freedom are 2. The statistic is 5, and the probability is about 0.082, which is above the usual 0.05 threshold.

### Example 4: Turn the Probability Into a Decision

```excel
=IF(CHISQ.TEST(A2:B3, A6:B7) < 0.05, "Association Found", "No Clear Association")
```

**Result:** `Association Found`

The probability from Example 2 is far below 0.05, so the formula reports an association. Pick the significance level before you look at the data and store it in a cell if several tests share it.

## Story Problems

### Problem 1: Website Layout Test

A web team shows two page layouts to 1,000 visitors and records who clicks the main button. Layout A had 500 visitors and Layout B had 500. The observed counts are in `A2:C3`.

| Layout | Clicked | Did Not Click |
| --- | --- | --- |
| Layout A | 120 | 380 |
| Layout B | 150 | 350 |

The expected counts go in `B6:C7`. Use the Example 1 formula with its column references shifted one column to the right.

**Task:** Use the observed and expected tables to find the probability that the click pattern is independent of layout.

**Solution:**

```excel
=CHISQ.TEST(B2:C3, B6:C7)
```

**Answer:** `0.0326`. Because the value is below 0.05, the click rate differs by layout at the usual significance level. The expected counts are 135 and 365 in each row.

### Problem 2: Overtime Requests by Shift

A plant planned overtime requests across three shifts: 40, 40 and 20. Actual requests were 50, 30 and 20. The actual counts are in `A2:C2` and the plan is in `A5:C5`.

**Task:** Find the probability that the actual pattern matches the plan.

**Solution:**

```excel
=CHISQ.TEST(A2:C2, A5:C5)
```

**Answer:** `0.0821`. The table has one row and three columns, so the degrees of freedom are 2. The probability is above 0.05, so the plan is not rejected.

## Use Cases

### Survey Question Independence

**Scenario:** A researcher wants to know whether the answer to a yes or no question depends on the respondent's region. The counts for each region and answer are in a table.

```excel
=CHISQ.TEST(B3:C6, B10:C13)
```

**Why It Works:** The observed table holds the counts. The expected table holds the formula-based values, so the test compares what the data shows with what independence would produce.

### Defect Rate by Plant

**Scenario:** A manufacturer compares pass and fail counts for two plants to decide whether plant and result are related before it looks at specific defects.

```excel
=IF(CHISQ.TEST(Observed, Expected) < Alpha, "Review Plants", "No Action")
```

**Why It Works:** Named ranges keep the test readable. Changing the `Alpha` cell updates the decision for every plant without editing the formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two ranges have a different number of cells. | Make the expected table the same shape as the observed table. |
| `#N/A` | Both ranges are a single cell. | A test needs at least two cells. |
| Misleading result | Expected counts are too small, often below 5. | Combine categories or collect more data. |
| Misleading result | The expected range holds observed counts or percentages. | Build the expected table from row totals, column totals and the grand total. |
| `#VALUE!` | A range contains text. | Remove text from both tables before testing. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | The support page lists CHISQ.TEST as the modern replacement for CHITEST. |
| Google Sheets | Documented as CHITEST | The Sheets help page for this test is filed under CHITEST. Use CHITEST for the same calculation. |

## Tips and Best Practices

- Build the expected table with formulas so it updates when the observed counts change.
- Check the expected counts before you trust the probability; a value below 5 in many cells weakens the result.
- Use CHISQ.TEST for categorical counts. Use T.TEST when comparing averages.
- Keep both tables the same size and orientation. Mismatched shapes are the most common cause of `#N/A`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | Converts a chi-squared statistic into a right-tail probability. |
| [CHISQ.INV.RT](CHISQ.INV.RT.md) | Returns the critical value for a chosen significance level. |
| [CHITEST](CHITEST.md) | The same test under its Sheets name and the earlier Excel name. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Totals rows, columns and the grand total for the expected table. |
| [T.TEST](T.TEST.md) | Compares averages rather than counts. |

## Official Documentation

- [Microsoft Support: CHISQ.TEST function](https://support.microsoft.com/en-us/excel/functions/chisq-test-function)
- [Google Docs Editors Help: CHITEST](https://support.google.com/docs/answer/7004263)
