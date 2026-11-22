---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Date Range Validation
  - Form Completeness Checks
  - Loan Pre-Approval
related:
  - IF
  - IFS
  - NOT
  - OR
  - XOR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/and-function
  - https://support.google.com/docs/answer/3093301
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - All Conditions True
  - Boolean And
  - Logical And
tags:
  - boolean
  - excel
  - logical
  - multi-condition
  - sheets
---

# AND

## Description

**AND** returns TRUE only when every condition you give it is TRUE. If any single argument is FALSE, the result is FALSE. Use it when a record must meet several requirements at once, such as a score above a threshold, a status of Active, and a date inside a reporting window.

AND rarely works alone. Most formulas place it inside [IF](IF.md) so the result can be a message or a value instead of TRUE or FALSE. A formula such as `=IF(AND(A2>0, B2>0), "Valid", "Invalid")` stays readable as conditions are added, while nesting one IF inside another becomes hard to follow.

When any one of several conditions is enough, use [OR](OR.md). When exactly one of two conditions must hold, use [XOR](XOR.md). To reverse a result, wrap it in [NOT](NOT.md).

Inside a range argument, AND ignores text and empty cells. If a range holds no logical values at all, Excel returns the #VALUE! error.

## Syntax

```excel
=AND(logical1, [logical2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/AND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical1` | Yes | The first condition to test. It can be a comparison such as `A2>=70`, a function that returns TRUE or FALSE such as `ISBLANK(A2)`, or a cell that contains TRUE or FALSE. |
| `logical2, ...` | No | Additional conditions. Excel accepts up to 255 arguments. Google Sheets accepts additional expressions, and its help page does not state a maximum. |

### Return Value

TRUE when every argument evaluates to TRUE. FALSE when one or more arguments evaluate to FALSE. In Excel, if a reference or array contains no logical values, the result is the #VALUE! error.

## Examples

### Example 1: Two Conditions

```excel
=AND(A2>=70, B2>=70)
```

**Result:** `FALSE` when A2 holds 85 and B2 holds 64

The first test passes because 85 is at least 70. The second fails because 64 is below 70, so the whole result is FALSE. Change B2 to 78 and the result becomes TRUE.

### Example 2: AND Inside IF for a Decision

```excel
=IF(AND(B2>=650, C2>=25000), "Approved", "Review")
```

**Result:** `Approved` when B2 holds 700 and C2 holds 30000

The IF wrapper converts the TRUE or FALSE result into a message. If either number falls below its threshold, the cell shows "Review" instead.

### Example 3: Date Inside a Window

```excel
=AND(A2>=DATE(2026,1,1), A2<=DATE(2026,3,31))
```

**Result:** `TRUE` when A2 holds 14 February 2026

Both bounds are inclusive, so 1 January 2026 and 31 March 2026 also return TRUE. Dates are stored as serial numbers, so the comparisons work the same way as comparisons between numbers.

<!-- Image 2: Two Conditions Truth Table. See Images/Logical/AND.md -->

### Example 4: Required Fields Are Filled

```excel
=AND(A2<>"", B2<>"")
```

**Result:** `FALSE` when A2 holds "Ana" and B2 is empty

The second test compares B2 with an empty string. Because B2 is blank, that test is FALSE and so is the whole result. This check works well as a gate before a row is processed.

### Example 5: AND Nested Inside OR

```excel
=OR(AND(A2="Manager", B2>=5), AND(A2="Director", B2>=3))
```

**Result:** `TRUE` when A2 holds "Director" and B2 holds 4

Each AND defines one path to eligibility. The Manager path fails because the title is not Manager, but the Director path passes, so OR returns TRUE.

## Story Problems

### Problem 1: Scholarship Eligibility

A college scholarship committee screens applicants. An applicant qualifies only with a GPA of at least 3.2, at least 30 completed credits, and a submitted essay.

| Applicant | GPA | Credits | Essay Submitted |
| --- | --- | --- | --- |
| Rowan | 3.4 | 45 | Yes |
| Imani | 3.1 | 52 | Yes |
| Teo | 3.8 | 28 | Yes |
| Lucia | 3.5 | 36 | No |
| Omar | 3.9 | 60 | Yes |

**Task:** Enter the formula in E2, fill it down to E6, and identify which applicants show TRUE.

**Solution:**

```excel
=AND(B2>=3.2, C2>=30, D2="Yes")
```

**Answer:** `2` applicants qualify, Rowan and Omar. Imani misses the GPA test, Teo misses the credit test, and Lucia has no essay.

<!-- Image 3: Scholarship Results Panel. See Images/Logical/AND.md -->

### Problem 2: Invoice Release

A billing team releases an invoice for payment only when it is approved, its amount is 5000 or less, and it has been open 30 days or fewer.

| Invoice | Approved | Amount | Days Open |
| --- | --- | --- | --- |
| INV-101 | Yes | 4200 | 12 |
| INV-102 | Yes | 7800 | 5 |
| INV-103 | No | 900 | 3 |
| INV-104 | Yes | 1500 | 45 |
| INV-105 | Yes | 2750 | 20 |

**Task:** Enter the formula in E2, fill it down to E6, and total the amounts of the invoices that show TRUE.

**Solution:**

```excel
=AND(B2="Yes", C2<=5000, D2<=30)
```

**Answer:** `6950`. INV-101 (4200) and INV-105 (2750) pass all three tests. INV-102 is over the amount limit, INV-103 is not approved, and INV-104 has been open too long.

## Use Cases

### Loan Pre-Approval

**Scenario:** A lender pre-approves an applicant only when the credit score, annual income, and debt-to-income ratio all meet policy.

```excel
=IF(AND(B2>=680, C2>=35000, D2<=0.35), "Pre-Approved", "Manual Review")
```

**Why It Works:** Every requirement is a separate test, so one weak factor sends the file to a person for review. Store the three thresholds in cells and point the formula at them so policy changes do not require editing the formula.

### Form Completeness Checks

**Scenario:** Before a registration row is saved, the sheet confirms that name, email, and phone are all filled in.

```excel
=IF(AND(A2<>"", B2<>"", C2<>""), "Complete", "Incomplete")
```

**Why It Works:** Each test checks one required field, so a single blank field marks the whole row as incomplete.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A range argument contains no logical values. | Compare the range inside each argument, or test individual cells. |
| `FALSE` when a match looks correct | A value has an extra space or different capitalization. | Clean the text with TRIM, and compare with UPPER or LOWER on both sides. |
| Too many arguments | More than 255 conditions in Excel. | Split the conditions into groups, such as `AND(AND(...), AND(...))`. |
| Unexpected `TRUE` | A blank cell passed a test you expected to fail. | Add an explicit test such as `B2<>""` for each required field. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Accepts up to 255 logical arguments. Ignores text and empty cells in range arguments. Returns #VALUE! when a range has no logical values. |
| Google Sheets | Available | Accepts additional expressions. The help page does not state a maximum number of arguments. |

## Tips and Best Practices

- Wrap AND in IF, or in another function, when people need to read a message instead of TRUE or FALSE.
- Place each condition in its own argument so a failing test is easy to spot when you check the formula.
- Keep thresholds in labeled cells, such as `B2>=$H$1`, so policy changes need one edit.
- Use OR instead of AND when one passing condition is enough.
- Move long condition lists into helper columns, with one column per test, when a formula becomes hard to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](IF.md) | Returns a value or message based on the AND result. |
| [IFS](IFS.md) | Tests several conditions in order and returns the first matching value. |
| [NOT](NOT.md) | Reverses a logical value, useful for excluding a case. |
| [OR](OR.md) | Returns TRUE when any argument is TRUE. |
| [XOR](XOR.md) | Returns TRUE when exactly one of two conditions holds. |

## Official Documentation

- [Microsoft Support: AND function](https://support.microsoft.com/en-us/excel/functions/and-function)
- [Google Docs Editors Help: AND](https://support.google.com/docs/answer/3093301)
