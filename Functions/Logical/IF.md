---
domain: Spreadsheet Functions
category: Logical
subcategory: Conditional Tests
purpose:
  - Conditional Logic
use-case:
  - Commission Tiers
  - Inventory Status Flags
  - Status Standardization
related:
  - AND
  - IFERROR
  - IFNA
  - IFS
  - NOT
  - OR
  - SWITCH
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/if-function
  - https://support.google.com/docs/answer/3093364
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional If
  - If Then Else
  - If Statement
tags:
  - branching
  - excel
  - logical
  - nested-if
  - sheets
---

# IF

## Description

**IF** tests a condition and returns one value when the condition is TRUE and a different value when it is FALSE. It is the basic decision tool in spreadsheets, and it turns static data into results that change with the inputs. A cell can show "Over Budget" or "OK" depending on its amount, or a bonus can appear only for completed projects.

The condition can be any expression that evaluates to TRUE or FALSE, and each result can be a number, text, a cell reference, another formula, or another IF. Because the result can itself be an IF, you can build multi-step decisions. For more than two or three outcomes, [IFS](IFS.md) is easier to read than deeply nested IF calls, and [SWITCH](SWITCH.md) is a good fit when one value is compared against a list of possible matches.

When the test needs two or more requirements, place [AND](AND.md) or [OR](OR.md) inside the logical test. To catch errors produced by the value or the test, use [IFERROR](IFERROR.md) or [IFNA](IFNA.md) inside the formula.

Always enter both result arguments on purpose. When the value_if_false argument is left out in Excel, a FALSE result is returned, which often looks like a broken formula.

## Syntax

```excel
=IF(logical_test, value_if_true, [value_if_false])
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/IF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical_test` | Yes | The condition to test, such as `A2>=60`, `B2="Manager"`, or a function that returns TRUE or FALSE. |
| `value_if_true` | Yes | The value returned when the test is TRUE. It can be a number, text in quotes, a cell reference, a formula, or another IF. |
| `value_if_false` | No | The value returned when the test is FALSE. It accepts the same kinds of values as value_if_true. In Excel, leaving it out returns FALSE. In Google Sheets, it is blank by default. |

### Return Value

The value of value_if_true when the test is TRUE, or the value of value_if_false when the test is FALSE. The return type follows whatever the chosen argument produces, so one IF can return a number in some rows and text in others. Errors in the test or in the chosen argument are returned as errors.

## Examples

### Example 1: Pass or Fail

```excel
=IF(A2>=60, "Pass", "Fail")
```

**Result:** `Fail` when A2 holds 58

The test 58 is at least 60 is FALSE, so the second argument is returned. A score of 60 or higher returns "Pass". This pattern covers any yes or no classification.

### Example 2: Returning a Calculation

```excel
=IF(B2="Manager", C2*0.15, C2*0.10)
```

**Result:** `9000` when B2 holds "Manager" and C2 holds 60000

A manager's rate is 15 percent of the salary in C2, so the result is 60000 times 0.15, which is 9000. Any other title returns the 10 percent rate instead. The two results are formulas, not fixed values, so each row is calculated when it is needed.

### Example 3: Nested IF for Grade Bands

```excel
=IF(A2>=90, "A", IF(A2>=80, "B", IF(A2>=70, "C", "F")))
```

**Result:** `B` when A2 holds 84

The test runs from the highest band down. 84 fails the 90 test, passes the 80 test, and returns "B" without checking the lower bands. Keep the thresholds in order, from highest to lowest, or the first match will be wrong.

<!-- Image 2: Nested Decision Path. See Images/Logical/IF.md -->

### Example 4: Blank Check

```excel
=IF(A2="", "No Data", A2)
```

**Result:** `No Data` when A2 is empty

When A2 has a value, the formula shows that value. The test A2="" matches only a truly empty cell, so a cell that holds a space or a formula returning an empty string may not match.

### Example 5: IF Inside an IFS Alternative

```excel
=IFS(A2>=90, "A", A2>=80, "B", A2>=70, "C", TRUE, "F")
```

**Result:** `B` when A2 holds 84

IFS checks each pair of test and result in turn and returns the first match. The final TRUE acts as the fallback. This gives the same answer as Example 3 with less nesting.

### Example 6: Combining IF With AND

```excel
=IF(AND(B2>1000, C2="Active"), "Priority", "Standard")
```

**Result:** `Priority` when B2 holds 1500 and C2 holds "Active"

AND returns TRUE only when both tests pass, so the customer gets the priority label only when the spending and status conditions are both met.

## Story Problems

### Problem 1: Tiered Sales Commission

A sales team earns 5 percent on sales under 10000, 7 percent on sales from 10000 to 49999, and 10 percent on sales of 50000 or more.

| Rep | Sales |
| --- | --- |
| Avery | 8400 |
| Blake | 23150 |
| Casey | 61000 |
| Drew | 9990 |
| Emery | 50000 |

**Task:** Enter the formula in C2, fill it down to C6, and total the commissions.

**Solution:**

```excel
=IF(B2<10000, B2*0.05, IF(B2<50000, B2*0.07, B2*0.10))
```

**Answer:** `13640`. The commissions are 420, 1620.50, 6100, 499.50, and 5000, which add up to 13640.

<!-- Image 3: Commission Results Panel. See Images/Logical/IF.md -->

### Problem 2: Stock Status Flags

A shop wants each product labeled Out of Stock when nothing is on hand, Low Stock when the count is below the reorder point, and In Stock otherwise.

| Product | On Hand | Reorder Point |
| --- | --- | --- |
| Mugs | 0 | 10 |
| Pens | 4 | 10 |
| Notebooks | 25 | 10 |
| Staplers | 10 | 10 |

**Task:** Enter the formula in D2 and fill it down to D5. Then count the products that need reordering.

**Solution:**

```excel
=IF(B2=0, "Out of Stock", IF(B2<C2, "Low Stock", "In Stock"))
```

**Answer:** `2` products need reordering: Mugs (Out of Stock) and Pens (Low Stock). Staplers sit exactly at the reorder point, so the test "below the reorder point" is FALSE and it shows In Stock.

## Use Cases

### Dynamic Pricing Rules

**Scenario:** VIP customers always get a 20 percent discount, while regular customers get 10 percent only on orders over 500.

```excel
=IF(A2="VIP", D2*0.8, IF(D2>500, D2*0.9, D2))
```

**Why It Works:** The VIP test comes first, so VIP customers never reach the order-value test. Put rules in the order of business priority, because the first TRUE test decides the result.

### Status Standardization

**Scenario:** Inconsistent entries such as "Y", "yes", and 1 must become one standard value, "Active" or "Inactive".

```excel
=IF(OR(UPPER(A2)="Y", UPPER(A2)="YES", A2=1), "Active", "Inactive")
```

**Why It Works:** UPPER removes differences in capitalization before the comparison, and OR combines the accepted spellings. Extend the list in OR when new variants appear, or move the variants into a lookup table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A test compares text with a calculation that expects a number. | Convert the value with VALUE, or check its type first with ISNUMBER. |
| `FALSE` appears in the result | value_if_false was left out. | Enter both results, such as `""` or `"No"`, so the outcome is explicit. |
| Wrong band returned | Thresholds are not in order in a nested IF. | List the highest threshold first, or switch to IFS. |
| Formula is hard to read | Many nested IF calls. | Use IFS, SWITCH, or a lookup table. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Leaving out value_if_false returns FALSE. Nested IF calls are supported. IFS is available in newer versions for long chains. |
| Google Sheets | Available | value_if_false is blank by default. Text comparisons follow Sheets rules, so clean text with TRIM or case functions when values come from users. |

## Tips and Best Practices

- Always write value_if_false so the other outcome is visible in the formula.
- Use IFS or SWITCH when you have more than two or three outcomes.
- Put thresholds in labeled cells so the formula reads like the policy it implements.
- Order nested tests from the most specific or most important to the least.
- Test each branch with a value that goes down each path, including blanks and zero.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Requires every condition to be TRUE inside the logical test. |
| [IFERROR](IFERROR.md) | Replaces any error with a fallback value. |
| [IFNA](IFNA.md) | Replaces only #N/A errors with a fallback value. |
| [IFS](IFS.md) | Tests several conditions in order without nesting. |
| [NOT](NOT.md) | Reverses the test so the branches can be swapped. |
| [OR](OR.md) | Passes when any one condition is TRUE. |
| [SWITCH](SWITCH.md) | Compares one value against a list of possible matches. |

## Official Documentation

- [Microsoft Support: IF function](https://support.microsoft.com/en-us/excel/functions/if-function)
- [Google Docs Editors Help: IF](https://support.google.com/docs/answer/3093364)
