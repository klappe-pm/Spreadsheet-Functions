---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
use-case:
  - Legacy Workbook Migration
  - Shift Pattern Comparison
  - Ticket Channel Comparison
related:
  - CHIDIST
  - CHIINV
  - CHISQ.DIST.RT
  - CHISQ.INV.RT
  - CHISQ.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chitest-function
  - https://support.google.com/docs/answer/7004263
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Chi Squared Independence Legacy
  - Pearson Chi Squared Test
tags:
  - chi-squared
  - compatibility
  - excel
  - hypothesis-testing
  - sheets
---

# CHITEST

## Description

**CHITEST** returns the probability from a chi-squared test of independence. You give it a table of observed counts and a table of expected counts of the same shape, and it returns the chance of a statistic at least as large as the one calculated if the two variables were independent. It is the same test as CHISQ.TEST.

Microsoft Excel lists CHITEST as a compatibility function. The support page says it is still available for backward compatibility but may not be available in future versions, and it recommends CHISQ.TEST for new work. Use CHITEST when you open or maintain a workbook that already depends on it. Build new formulas with CHISQ.TEST in Excel.

Google Sheets documents this test as CHITEST and has no separate CHISQ.TEST page, so CHITEST is the name to use in Sheets. Its argument names differ slightly from Excel, but the calculation is the same.

The expected table is built from the data as row total times column total, divided by the grand total. A result below 0.05 suggests that the variables are related. The test is most reliable when every expected count is at least 5.

## Syntax

```excel
=CHITEST(actual_range, expected_range)
```

<!-- Image 1: Legacy Test Arguments. See Images/Statistical/CHITEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `actual_range` | Yes | The observed counts. Google Sheets names this argument `observed_range`. |
| `expected_range` | Yes | The expected counts for the same cells. Google Sheets names this argument `expected_range` as well. |

Both ranges must have the same shape. In Excel, ranges with a different number of data points return `#N/A`. In Google Sheets, both ranges must have the same number of rows and columns, and any non-numeric cell is excluded along with its matching cell in the other range.

### Return Value

A probability between 0 and 1. The function returns `#N/A` when the ranges have different numbers of data points, when both ranges are a single cell, or when the ranges contain a dimension problem described above.

Degrees of freedom are (rows minus 1) times (columns minus 1) for a table with more than one row and column. For a single row or a single column, the degrees of freedom equal the number of cells minus 1.

## Examples

### Example 1: Test a 2 by 2 Table

Observed counts sit in `A2:B3` and expected counts in `A6:B7`. The expected values are 55 and 45 in each row.

```excel
=CHITEST(A2:B3, A6:B7)
```

**Result:** `0.0000201` (rounded)

The chi-squared statistic is 18.181818 with 1 degree of freedom. The probability is very small, so the two variables are unlikely to be independent.

### Example 2: Test a Single Row

Observed counts in `A2:C2` are 25, 35 and 40. Expected counts in `A5:C5` are 30, 30 and 40.

```excel
=CHITEST(A2:C2, A5:C5)
```

**Result:** `0.4346` (rounded)

With three columns and one row, the degrees of freedom are 2. The probability is well above 0.05, so the observed pattern is consistent with the expected one.

### Example 3: Confirm a Migration to CHISQ.TEST

```excel
=CHISQ.TEST(A2:B3, A6:B7) - CHITEST(A2:B3, A6:B7)
```

**Result:** `0`

Both functions return the same probability for the same ranges, so a workbook can move from CHITEST to CHISQ.TEST without changing its results.

<!-- Image 2: Migration Check. See Images/Statistical/CHITEST.md -->

### Example 4: Show a Message When the Shapes Do Not Match

```excel
=IFERROR(CHITEST(A2:B3, A6:C7), "Check Table Shapes")
```

**Result:** `Check Table Shapes`

The expected range has a different shape from the observed range, so the function returns an error and the wrapper shows a readable message instead.

## Story Problems

### Problem 1: Ticket Channel Comparison

A box office compares how buyers pay across two channels. The legacy workbook still uses CHITEST. Channel labels sit in column A, observed counts in `B2:C3`, and expected counts in `B6:C7`.

| Channel | Card Purchase | Cash Purchase |
| --- | --- | --- |
| Online | 80 | 20 |
| Box Office | 50 | 50 |

**Task:** Find the probability that payment method is independent of channel, using the legacy function.

**Solution:**

```excel
=CHITEST(B2:C3, B6:C7)
```

**Answer:** `0.0000087` (rounded). The expected counts are 65 and 35 in each row. The result is far below 0.05, so payment method depends on channel.

### Problem 2: Shift Pattern Comparison

A plant expects 20 overtime requests on each of the first two shifts and 30 on the third. The actual counts are 18, 22 and 30.

**Task:** Find the probability that the actual pattern matches the plan.

**Solution:**

```excel
=CHITEST(A2:C2, A5:C5)
```

**Answer:** `0.8187`. The observed counts sit in `A2:C2` and the plan in `A5:C5`. The result is high, so the difference from the plan is small.

## Use Cases

### Legacy Workbook Migration

**Scenario:** An inherited financial model uses CHITEST in dozens of cells, and the team wants to confirm the results before moving to a new standard.

```excel
=CHISQ.TEST(Observed, Expected) - CHITEST(Observed, Expected)
```

**Why It Works:** A zero difference confirms that the two functions agree on the current data. Copy the check into a hidden column, and remove it once the migration is complete.

### Survey Independence Check

**Scenario:** A team runs the same independence test each quarter on a survey and keeps the older formula because a shared template already uses it.

```excel
=IF(CHITEST(Q1Observed, Q1Expected) < 0.05, "Related", "Independent")
```

**Why It Works:** The formula keeps the template working. The decision threshold sits in the formula so each quarter's review uses the same rule.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The two ranges have a different number of data points. | Make the expected table the same size as the observed table. |
| `#N/A` | Both ranges are a single cell. | Use at least two cells. |
| Misleading result | Expected counts are small, often below 5. | Combine categories or collect more data. |
| Unexpected result in Sheets | A non-numeric cell removed a pair from the test. | Check the tables for text entries before testing. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function | The support page recommends CHISQ.TEST and warns that CHITEST may not be available in future versions. |
| Google Sheets | Available | The help page documents the function as CHITEST with the arguments `observed_range` and `expected_range`. Non-numeric cells are excluded in pairs. |

## Tips and Best Practices

- Use CHISQ.TEST for new Excel work and keep CHITEST only where an existing workbook depends on it.
- Test the two functions side by side during a migration, as in Example 3.
- Keep the observed and expected tables in matching shapes to avoid `#N/A`.
- Document the significance level next to the result so readers know what the probability is compared against.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIDIST](CHIDIST.md) | Legacy right-tail probability for a chi-squared statistic. |
| [CHIINV](CHIINV.md) | Legacy right-tail inverse, the cutoff for a given probability. |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | Modern right-tail probability for a chi-squared statistic. |
| [CHISQ.INV.RT](CHISQ.INV.RT.md) | Modern cutoff for a right-tail probability. |
| [CHISQ.TEST](CHISQ.TEST.md) | The modern name for the same test and the recommended replacement in Excel. |

## Official Documentation

- [Microsoft Support: CHITEST function](https://support.microsoft.com/en-us/excel/functions/chitest-function)
- [Google Docs Editors Help: CHITEST](https://support.google.com/docs/answer/7004263)
