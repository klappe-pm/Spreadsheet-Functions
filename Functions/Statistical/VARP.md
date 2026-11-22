---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Cashier Staffing Variance
  - Population Spread Reporting
related:
  - DVARP
  - STDEVP
  - VAR
  - VAR.P
  - VARPA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/varp-function
  - https://support.google.com/docs/answer/3094113
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Legacy Population Variance
tags:
  - compatibility
  - dispersion
  - excel
  - population
  - sheets
  - variance
---

# VARP

## Description

**VARP** calculates the variance of a complete population. It measures how far the values spread around their mean, and it divides the sum of squared deviations by the number of values, because every value you supply is treated as the entire group of interest.

VARP is a legacy compatibility function. Microsoft states that it has been replaced by VAR.P, which returns the same result with a clearer name. VARP remains available so older workbooks keep working, but it may not exist in future versions of Excel. Use VAR.P in new formulas.

When the values are a sample from a larger group rather than the whole group, use VAR, or VAR.S in new work. Those functions divide by one fewer than the count and give a slightly larger result. When you supply a range, VARP ignores logical values and text; use VARPA to count them.

## Syntax

```excel
=VARP(number1,[number2],...)
```

<!-- Image 1: Population Values and the Population Variance. See Images/Statistical/VARP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, reference or array that holds population values. |
| `number2, ...` | No | Up to 254 more numbers, references or arrays from the same population. Numbers typed directly into the list are counted, including logical values and numeric text. |

### Return Value

A number: the population variance. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Logical values and text inside a range are ignored.

## Examples

All examples use six values in `A2:A7`: 4, 8, 6, 5, 3 and 7. Their mean is 5.5 and the sum of squared deviations is 17.5.

### Example 1: Population Variance of a Range

```excel
=VARP(A2:A7)
```

**Result:** `2.9167`

Dividing 17.5 by six, the number of values, gives 2.9167.

### Example 2: Add a Seventh Value

```excel
=VARP(A2:A7,10)
```

**Result:** `4.9796`

Adding 10 raises the population variance to 4.9796 because the spread of the seven values is wider.

### Example 3: The Replacement Function

```excel
=VAR.P(A2:A7)
```

**Result:** `2.9167`

VAR.P returns the same population variance as VARP. Use it in new formulas.

### Example 4: Convert to the Sample Variance

```excel
=VARP(A2:A7)*6/5
```

**Result:** `3.5`

Multiplying the population variance by six divided by five converts it to the sample variance, the same value that VAR returns for these six values.

### Example 5: Values Typed Directly

```excel
=VARP(4,8,6,5,3,7)
```

**Result:** `2.9167`

Typing the population values gives the same result as referencing the range.

## Story Problems

### Problem 1: Cashier Customer Counts

A store has six registers open for a full shift, and the manager records how many customers each cashier served in `A2:A7`. The six cashiers are the entire staff on duty, so the manager uses the population variance to measure how evenly the work was shared.

| Cashier | Customers Served |
| --- | --- |
| C1 | 18 |
| C2 | 22 |
| C3 | 15 |
| C4 | 20 |
| C5 | 25 |
| C6 | 17 |

**Task:** Compute the population variance of the customers served.

**Solution:**

```excel
=VARP(B2:B7)
```

**Answer:** `10.9167`. The mean is 19.5 customers. The squared deviations add up to 65.5, and dividing by six gives 10.9167. The sample variance of the same numbers would be 13.1.

<!-- Image 2: Cashier Variance Result. See Images/Statistical/VARP.md -->

### Problem 2: Packing Line Totals

A packing team has four lines, and the supervisor records the boxes packed by each line in `B2:B5` during one hour. The four lines are the whole team, so the population variance describes the team's output.

| Line | Boxes Packed |
| --- | --- |
| L1 | 40 |
| L2 | 46 |
| L3 | 37 |
| L4 | 43 |

**Task:** Compute the population variance of the four line totals.

**Solution:**

```excel
=VARP(B2:B5)
```

**Answer:** `11.25`. The mean is 41.5 boxes. The squared deviations add up to 45, and dividing by four gives 11.25.

## Use Cases

### Cashier Staffing Variance

**Scenario:** A store manager compares the workload of every cashier in one shift to decide whether the rota needs rebalancing.

```excel
=SQRT(VARP(Shift[CustomersServed]))
```

**Why It Works:** The table holds every cashier on the shift, so the population variance applies. The square root gives the standard deviation in customers, which the manager can compare with the target.

### Population Spread Reporting

**Scenario:** A finance team reports the variance of department spending across every department in the company.

```excel
=VARP(Departments[Spend])
```

**Why It Works:** The report covers all departments, not a sample, so the population divisor is correct. Add new departments to the table so the result stays complete.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is an error value, or text typed directly into the list cannot be converted to a number. | Correct the source cell or the typed value. |
| Unexpected result | Logical values and text inside a range are ignored. | Use VARPA to count them as 1, 0 or text values. |
| Unexpected result | The values are a sample, so the population divisor understates the spread. | Use VAR.S or VAR. |
| Unexpected result | Empty cells are assumed to be zeros. | Empty cells are skipped. Enter a 0 in the cell when the value really is zero. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions | Legacy compatibility function. Microsoft recommends VAR.P, and VARP may be removed from future versions. |
| Google Sheets | Available | Takes `value1, [value2, ...]`. Ignores text in the arguments, and VARPA treats text as 0. Returns `#DIV/0!` when fewer than two values are supplied in total. |

## Tips and Best Practices

- Use VAR.P for new work, and keep VARP only in workbooks that already use it.
- Confirm that the data covers the entire group before choosing the population divisor.
- Take the square root to report the spread in the units of the data.
- Check the range for blank cells and text that VARP will skip without warning.
- Use VARPA when a range holds logical flags that should count.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DVARP](../Database/DVARP.md) | Population variance of the records that match database criteria. |
| [STDEVP](STDEVP.md) | Legacy population standard deviation, the square root of this result. |
| [VAR](VAR.md) | Legacy sample variance, which divides by one fewer than the count. |
| [VAR.P](VAR.P.md) | Modern replacement that returns the same population variance. |
| [VARPA](VARPA.md) | Population variance that counts logical values and text inside a range. |

## Official Documentation

- [Microsoft Support: VARP function](https://support.microsoft.com/en-us/excel/functions/varp-function)
- [Google Docs Editors Help: VARP](https://support.google.com/docs/answer/3094113)
