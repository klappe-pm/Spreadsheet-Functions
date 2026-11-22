---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Legacy Critical Values
  - Significance Testing
  - Workbook Migration
related:
  - F.INV
  - F.INV.RT
  - FDIST
  - TINV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/finv-function
  - https://support.google.com/docs/answer/7003960
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Right Tail F Inverse
tags:
  - compatibility
  - critical-value
  - distribution
  - excel
  - sheets
---

# FINV

## Description

**FINV** returns the F value whose right-tailed probability equals the `probability` you supply. It is the inverse of FDIST: if p equals FDIST(x, df1, df2), then FINV(p, df1, df2) returns `x`. Analysts use it to find the critical value for an F test at a chosen significance level, such as 0.05 or 0.01.

Microsoft lists FINV as a compatibility function, replaced by F.INV and F.INV.RT. It still works in older workbooks, but Microsoft warns that it may not be available in future versions. For new work, use F.INV.RT, which returns the same value for the right tail.

Google's help page for this name points to F.INV.RT, so the calculation is the same in both programs.

The probability must be between 0 and 1. The degrees of freedom are each sample size minus 1, and non-integer values are truncated.

## Syntax

```excel
=FINV(probability, deg_freedom1, deg_freedom2)
```

<!-- Image 1: Legacy Inverse Mapped to Its Replacement. See Images/Statistical/FINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The right-tail probability, such as 0.05 or 0.01. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |

### Return Value

The F value whose right-tail probability equals `probability`. Excel returns `#VALUE!` when an argument is not numeric, `#NUM!` when the probability is outside 0 to 1 or a degrees-of-freedom value is less than 1 or at least 10^10, and `#N/A` when its iterative search does not converge.

## Examples

### Example 1: Critical Value at 2.5 Percent

```excel
=FINV(0.025, 10, 12)
```

**Result:** `3.3736` (rounded to four decimal places)

A variance ratio above 3.3736 falls in the top 2.5 percent of ratios with 10 and 12 degrees of freedom.

### Example 2: Critical Value at 10 Percent

```excel
=FINV(0.1, 3, 12)
```

**Result:** `2.6055` (rounded to four decimal places)

A looser 10 percent test needs a smaller ratio to reach significance than the 5 percent test does.

<!-- Image 2: Right-Tail Cutoff on the F Curve. See Images/Statistical/FINV.md -->

### Example 3: Critical Value at 5 Percent for a Larger Sample

```excel
=FINV(0.05, 4, 20)
```

**Result:** `2.8661` (rounded to four decimal places)

With 4 numerator and 20 denominator degrees of freedom, the 5 percent cutoff is 2.8661.

## Story Problems

### Problem 1: Critical Value From a Legacy Template

A lab's quality template uses FINV to set its cutoff. Lab A has 4 samples and Lab B has 13 samples. The template tests at the 5 percent level and must return the cutoff for those sample sizes.

| Lab | Sample Size |
| --- | --- |
| Lab A | 4 |
| Lab B | 13 |

**Task:** Find the critical value at the 5 percent level, using the sample sizes in `B2:B3`.

**Solution:**

```excel
=FINV(0.05, B2-1, B3-1)
```

**Answer:** `3.4903`. The degrees of freedom are 3 and 12. A ratio above this value is significant at the 5 percent level.

### Problem 2: Lenient Cutoff for Two Teams

Two support teams have 11 weekly ratings each. The manager wants a 10 percent cutoff for an early warning, which is less strict than the usual 5 percent test.

| Team | Sample Size |
| --- | --- |
| North | 11 |
| South | 11 |

**Task:** Find the critical value at the 10 percent level, using the sample sizes in `B2:B3`.

**Solution:**

```excel
=FINV(0.1, B2-1, B3-1)
```

**Answer:** `2.3226`. The degrees of freedom are 10 and 10. A ratio above 2.3226 triggers the early warning.

## Use Cases

### Legacy Critical Values

**Scenario:** A department keeps a cutoff table in a workbook that predates the F.INV.RT function, and the table must keep working.

```excel
=FINV(0.05, B2-1, B3-1)
```

**Why It Works:** The formula returns the same cutoff as F.INV.RT with the same inputs. Keep it in the legacy table, and add a note that points to F.INV.RT for future edits.

### Workbook Migration

**Scenario:** An analyst moves a set of critical values to a new template and checks that each row matches the original.

```excel
=F.INV.RT(0.05, B2-1, B3-1) - FINV(0.05, B2-1, B3-1)
```

**Why It Works:** The difference should be 0 for each row. A different value means a probability, a sample size or a reference was entered differently in the new template.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is outside 0 to 1. | Enter a probability such as 0.05, not a percentage such as 5. |
| `#NUM!` | A degrees-of-freedom value is less than 1 or at least 10^10. | Check that each sample has at least two values. |
| `#N/A` | The iterative search did not converge. | Check the probability and degrees of freedom for unusual values. |
| Wrong cutoff | The sample size was entered in place of sample size minus 1. | Subtract 1 from each sample size. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function, still available | Microsoft says the function may not be available in future versions. Replace it with F.INV.RT. |
| Google Sheets | Available | Google's help page for this name points to F.INV.RT, which returns the same right-tail value. |

## Tips and Best Practices

- Use F.INV.RT in new work, and keep FINV only where an existing workbook depends on it.
- Put the significance level in its own labeled cell so the critical values in a table stay consistent.
- Compare the result with F.DIST.RT to confirm the cutoff: the right-tail probability at the cutoff should equal the level you chose.
- Note the replacement next to each legacy formula, so the next reviewer does not need to research it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.INV](F.INV.md) | Left-tail inverse, the counterpart to this right-tail function. |
| [F.INV.RT](F.INV.RT.md) | The current name for the same right-tail calculation. Use it in new work. |
| [FDIST](FDIST.md) | The forward calculation: it returns the probability for a given F value. |
| [TINV](TINV.md) | Legacy t distribution inverse, used for critical values on means. |

## Official Documentation

- [Microsoft Support: FINV function](https://support.microsoft.com/en-us/excel/functions/finv-function)
- [Google Docs Editors Help: F.INV.RT](https://support.google.com/docs/answer/7003960)
