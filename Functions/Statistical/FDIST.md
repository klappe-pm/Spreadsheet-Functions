---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Legacy Model Maintenance
  - Significance Testing
  - Workbook Compatibility Review
related:
  - CHIDIST
  - F.DIST
  - F.DIST.RT
  - FINV
  - TDIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/fdist-function
  - https://support.google.com/docs/answer/6055799
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Right Tail F
tags:
  - compatibility
  - distribution
  - excel
  - hypothesis-testing
  - sheets
---

# FDIST

## Description

**FDIST** returns the right-tailed F probability, which is the chance of an F value greater than `x` when the two samples come from populations with equal variances. It is the same calculation as F.DIST.RT, under the name used in earlier versions of Excel.

Microsoft lists FDIST as a compatibility function. It remains available so that older workbooks keep working, but Microsoft warns that it may not be available in future versions. For new work, use F.DIST.RT, which has the same arguments and the same result.

Use FDIST when you maintain a workbook that already contains it, or when you need the older name for a report that expects it. When you have the choice, F.DIST.RT is the better formula, because it matches the rest of the F function family.

The degrees of freedom are each sample size minus 1. Non-integer values are truncated to whole numbers.

## Syntax

```excel
=FDIST(x, deg_freedom1, deg_freedom2)
```

<!-- Image 1: Legacy Function Mapped to Its Replacement. See Images/Statistical/FDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The F value to test. It must not be negative. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |

### Return Value

A probability from 0 to 1 for the right tail. A larger `x` gives a smaller result. Excel returns `#VALUE!` when an argument is not numeric and `#NUM!` when `x` is negative, a degrees-of-freedom value is less than 1, or a degrees-of-freedom value is 10^10 or more.

## Examples

### Example 1: Right-Tail Probability

```excel
=FDIST(4.5, 5, 10)
```

**Result:** `0.0208` (rounded to four decimal places)

The result equals 1 minus F.DIST(4.5, 5, 10, TRUE), which is 1 minus 0.9792. The right tail holds about 2.1 percent of the curve.

### Example 2: Matching the Modern Function

```excel
=FDIST(2.2, 8, 12)
```

**Result:** `0.1055` (rounded to four decimal places)

With the same inputs, F.DIST.RT(2.2, 8, 12) returns the same value. Use this check when you move a workbook from FDIST to F.DIST.RT.

<!-- Image 2: Legacy and Replacement Results Side by Side. See Images/Statistical/FDIST.md -->

### Example 3: Wider Degrees of Freedom

```excel
=FDIST(1.5, 10, 10)
```

**Result:** `0.2666` (rounded to four decimal places)

With 10 degrees of freedom in each sample, a ratio of 1.5 is not unusual, so the right-tail probability is well above 0.05.

## Story Problems

### Problem 1: Legacy Model Output

A finance team built a variance model in 2012. The model cell holds the F ratio, and two cells hold the sample sizes of the two groups it compares. The ratio is 3.1, the first group has 5 observations and the second has 21.

| Input | Value |
| --- | --- |
| F ratio | 3.1 |
| First sample size | 5 |
| Second sample size | 21 |

**Task:** Return the right-tail probability for the ratio, using the values in `B2:B4`.

**Solution:**

```excel
=FDIST(B2, B3-1, B4-1)
```

**Answer:** `0.0388`. The degrees of freedom are 4 and 20. Because the result is below 0.05, the model flags the difference as significant.

### Problem 2: Workbook Review Before Migration

A reviewer audits the same model before moving it to newer functions. The ratio is 2.6, the first sample has 4 observations and the second has 31. The reviewer must confirm the legacy result and decide whether it crosses the 0.05 threshold.

| Input | Value |
| --- | --- |
| F ratio | 2.6 |
| First sample size | 4 |
| Second sample size | 31 |

**Task:** Return the legacy right-tail probability using the values in `B2:B4`, and compare it with 0.05.

**Solution:**

```excel
=FDIST(B2, B3-1, B4-1)
```

**Answer:** `0.0705`. The degrees of freedom are 3 and 30. The result is above 0.05, so the difference is not significant, and the reviewer records the same conclusion as the modern function.

## Use Cases

### Legacy Model Maintenance

**Scenario:** A team keeps a variance model built on an older template and must update one value each month without rebuilding the sheet.

```excel
=FDIST(B2, B3-1, B4-1)
```

**Why It Works:** The formula keeps working in older workbooks without change. Plan to replace it with F.DIST.RT during the next template update, because Microsoft may drop the legacy name.

### Workbook Compatibility Review

**Scenario:** An analyst confirms that a migrated workbook returns the same p-values as the original.

```excel
=F.DIST.RT(B2, B3-1, B4-1) - FDIST(B2, B3-1, B4-1)
```

**Why It Works:** The difference should be 0 for every row. A nonzero result points to a changed input, a different sample size, or a formula that was not copied correctly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or a degrees-of-freedom value is less than 1 or at least 10^10. | Check the ratio and the sample sizes. |
| `#VALUE!` | An argument is text. | Convert the value or fix the reference. |
| Wrong probability | The sample size was entered in place of sample size minus 1. | Subtract 1 from each sample size. |
| Different results after migration | The formula was changed to a left-tail function. | Use F.DIST.RT, which returns the right tail, to match FDIST. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function, still available | Microsoft says the function may not be available in future versions. Replace it with F.DIST.RT. |
| Google Sheets | Available | Google's help page for this name points to F.DIST.RT, which has the same calculation. |

## Tips and Best Practices

- Replace FDIST with F.DIST.RT in new work, and keep the legacy name only where an existing workbook requires it.
- Record the replacement in a comment next to each legacy formula, so the next reviewer knows what to change.
- Use the comparison formula in the Use Cases section to prove a migration returned the same values.
- Keep the right-tail convention in mind: FDIST answers "how unusual is this ratio," not "how much of the curve lies below it."

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIDIST](CHIDIST.md) | Legacy right-tail chi square function, the same family of compatibility names. |
| [F.DIST](F.DIST.md) | Left-tail probability, the complement of this function. |
| [F.DIST.RT](F.DIST.RT.md) | The current name for the same right-tail calculation. Use it in new work. |
| [FINV](FINV.md) | Legacy inverse of this function, which returns the F value for a right-tail probability. |
| [TDIST](TDIST.md) | Legacy t distribution function, used for the same kind of significance test on means. |

## Official Documentation

- [Microsoft Support: FDIST function](https://support.microsoft.com/en-us/excel/functions/fdist-function)
- [Google Docs Editors Help: F.DIST.RT](https://support.google.com/docs/answer/6055799)
