---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Exclusive Approval Checks
  - Mutually Exclusive Flags
related:
  - AND
  - FALSE
  - IF
  - NOT
  - OR
  - TRUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/xor-function
  - https://support.google.com/docs/answer/9116491
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exclusive Or
tags:
  - boolean
  - excel
  - logical
  - parity
  - sheets
---

# XOR

## Description

**XOR** returns TRUE when an odd number of its logical arguments are TRUE, and FALSE when an even number are TRUE. With two conditions, that means XOR returns TRUE only when exactly one of them is TRUE. Use it for rules that allow one choice or the other but not both, such as a discount that applies through a coupon or a loyalty card, but not both.

OR is the right choice when either condition is enough. XOR is stricter: when both conditions are TRUE, it returns FALSE, which is often the answer a rule needs when both options together are a problem.

With three or more arguments, XOR does not mean "exactly one". It returns TRUE for an odd count, so three TRUE values also return TRUE. To require exactly one TRUE among three or more conditions, count the TRUE values and compare the count with 1.

Microsoft lists XOR for Excel 2016 and later, including Microsoft 365 and Excel for the web. Google Sheets supports XOR and treats 0 as FALSE and every other number as TRUE.

## Syntax

```excel
=XOR(logical1, [logical2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/XOR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical1` | Yes | The first condition. It can be a TRUE or FALSE value, a comparison such as `B2>10`, or a range of logical values. |
| `logical2, ...` | No | More conditions. Microsoft allows up to 254 arguments in total. Google calls the arguments `logical_expression1` and `logical_expression2`. |

### Return Value

TRUE when the count of TRUE values is odd, and FALSE when the count is even. In a range or array, Microsoft ignores text and empty cells. If a range holds no logical values, Microsoft returns `#VALUE!`.

## Examples

### Example 1: Exactly One Condition Is True

Cell `B2` holds `15` and cell `C2` holds `5`.

```excel
=XOR(B2>10, C2>10)
```

**Result:** `TRUE`

Only the first comparison is TRUE, so the count of TRUE values is 1, which is odd.

### Example 2: Both Conditions Are True

Cell `B2` holds `15` and cell `C2` holds `20`.

```excel
=XOR(B2>10, C2>10)
```

**Result:** `FALSE`

Both comparisons are TRUE, so the count is 2, which is even. OR would return TRUE for the same inputs.

### Example 3: Three Conditions

Cells `B2`, `C2` and `D2` hold `15`, `20` and `30`.

```excel
=XOR(B2>10, C2>10, D2>10)
```

**Result:** `TRUE`

All three comparisons are TRUE. The count of 3 is odd, so XOR returns TRUE, even though more than one condition is true. This is why XOR is not a test for exactly one.

### Example 4: Choosing a Label From Two Flags

Cell `B2` holds `Yes` and cell `C2` holds `No`.

```excel
=IF(XOR(B2="Yes", C2="Yes"), "One Flag Set", "Check Flags")
```

**Result:** `One Flag Set`

Only one flag is set, so XOR returns TRUE and IF returns the first label. If both flags were `Yes` or both were `No`, the second label would appear.

## Story Problems

### Problem 1: Coupon or Loyalty Discount

A shop allows a coupon or a loyalty discount on each order, but not both. The order list is in `A1:C6`.

| Order | Coupon Used | Loyalty Used |
| --- | --- | --- |
| 1001 | Yes | No |
| 1002 | Yes | Yes |
| 1003 | No | Yes |
| 1004 | No | No |
| 1005 | Yes | No |

**Task:** In column D, mark each order TRUE when it used exactly one discount. Then count the TRUE results.

**Solution:**

```excel
=XOR(B2="Yes", C2="Yes")
```

```excel
=COUNTIF(D2:D6, TRUE)
```

**Answer:** `3`. Orders 1001, 1003 and 1005 each used exactly one discount. Order 1002 used both, and order 1004 used neither.

### Problem 2: Three Inspection Flags

Each product has three inspection flags in `B1:D4`. A flag is TRUE when the check failed.

| Product | Flag A | Flag B | Flag C |
| --- | --- | --- | --- |
| P-10 | TRUE | FALSE | FALSE |
| P-11 | TRUE | TRUE | TRUE |
| P-12 | FALSE | FALSE | FALSE |
| P-13 | TRUE | TRUE | FALSE |

**Task:** In column E, return TRUE for each product with an odd number of failed flags. Then list how many products return TRUE.

**Solution:**

```excel
=XOR(B2, C2, D2)
```

**Answer:** `2`. P-10 has one failed flag and P-11 has three, so both return TRUE. P-12 has none and P-13 has two, so both return FALSE.

<!-- Image 2: Odd Count Truth Table. See Images/Logical/XOR.md -->

## Use Cases

### Exclusive Approval Checks

**Scenario:** A purchase needs a manager sign-off or a finance sign-off, and a record with both or neither goes to review.

```excel
=IF(XOR(D2="Yes", E2="Yes"), "Route Normally", "Review")
```

**Why It Works:** XOR is TRUE only when exactly one sign-off is recorded, so both-signed and unsigned records are both sent to review.

### Mutually Exclusive Flags

**Scenario:** Each customer row should have an email address or a phone number, but not both, to keep one primary contact method.

```excel
=XOR(G2<>"", H2<>"")
```

**Why It Works:** The formula returns TRUE when exactly one of the two contact cells is filled in. Filter the column for FALSE to find rows with both or neither.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A range or array holds no TRUE or FALSE values. | Test each input with a comparison, such as `B2>10`, or convert the range to logical results. |
| Unexpected TRUE with three inputs | XOR tests for an odd count, not for exactly one. | Use `=COUNTIF(B2:D2, TRUE)=1` when exactly one condition must be TRUE. |
| FALSE when one was expected | Both conditions are TRUE, so the count is even. | Use OR when either condition is enough. |
| Unexpected result from a range | Text and blank cells in a range are ignored. | Check that the range holds the logical results you expect. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365, and Excel for the web | Accepts 1 to 254 conditions. Ignores text and blank cells in ranges. Returns `#VALUE!` when a range has no logical values. |
| Google Sheets | Available | Accepts logical expressions and ranges. Numbers are converted to logical values: 0 is FALSE and every other number is TRUE. |

## Tips and Best Practices

- Use XOR for "one or the other, not both" rules, and use OR when both options are acceptable.
- Test two conditions first; with more than two, count the TRUE values instead of relying on the odd-count result.
- Put comparisons directly inside XOR when each test is used only once, and use helper columns when several formulas reuse the same test.
- Pair XOR with IF to return a label, as in Example 4, so the result is readable to non-technical users.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Returns TRUE only when every condition is TRUE. |
| [FALSE](FALSE.md) | Returns the logical value FALSE. |
| [IF](IF.md) | Chooses an output based on the XOR result. |
| [NOT](NOT.md) | Reverses a single logical value. |
| [OR](OR.md) | Returns TRUE when at least one condition is TRUE. |
| [TRUE](TRUE.md) | Returns the logical value TRUE. |

## Official Documentation

- [Microsoft Support: XOR function](https://support.microsoft.com/en-us/excel/functions/xor-function)
- [Google Docs Editors Help: XOR](https://support.google.com/docs/answer/9116491)
