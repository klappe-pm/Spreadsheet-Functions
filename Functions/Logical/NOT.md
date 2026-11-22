---
domain: Spreadsheet Functions
category: Logical
subcategory: Boolean Values
purpose:
  - Conditional Logic
use-case:
  - Checkbox Status Labels
  - Exclusion Lists
  - Required Field Checks
related:
  - AND
  - IF
  - ISBLANK
  - ISERROR
  - OR
  - XOR
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/not-function
  - https://support.google.com/docs/answer/3093305
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Boolean Negation
  - Logical Not
tags:
  - boolean
  - conditional-logic
  - excel
  - logical
  - sheets
---

# NOT

## Description

**NOT** reverses a logical value. It returns FALSE for TRUE and TRUE for FALSE. Use it when a rule is easier to state as "anything except" than as a list of matches, such as "every status except Discontinued."

NOT works on one value at a time. Most formulas use it inside IF, AND or OR. For example, `=IF(NOT(ISBLANK(A2)),"Has Entry","Empty")` puts the case you care about in the TRUE branch. For a single test, a comparison with the opposite operator is often clearer: `NOT(A2>100)` and `A2<=100` return the same result.

NOT does not treat text as a logical value. Google Sheets returns `#VALUE!` for text input, and the Excel help page does not describe how text is handled. Compare text explicitly, such as `NOT(A2="Yes")`, so the test does not depend on the input type.

## Syntax

```excel
=NOT(logical)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/NOT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `logical` | Yes | A value or expression that evaluates to TRUE or FALSE. It can be a comparison such as `A2>100`, a logical function such as `ISBLANK(A2)`, a cell that holds TRUE or FALSE, or a number, where 0 counts as FALSE and any other number counts as TRUE in Google Sheets. |

### Return Value

The opposite of the logical value supplied: FALSE when the argument is TRUE and TRUE when it is FALSE. Text input returns `#VALUE!` in Google Sheets.

## Examples

### Example 1: Inverting a Comparison

```excel
=NOT(A2>=100)
```

**Result:** `TRUE` when A2 holds 85.

A2>=100 is FALSE for 85, so NOT returns TRUE. The formula is equivalent to `A2<100`, and it reads well when the rule is about the values that fall short of a target.

### Example 2: Checking for a Non-Empty Cell

```excel
=IF(NOT(ISBLANK(B2)),"Has Entry","Empty")
```

**Result:** `Empty` when B2 has no content.

ISBLANK returns TRUE for an empty cell, and NOT flips it to FALSE, so the formula reaches the "Empty" branch. A cell that contains a formula returning an empty string is not blank for ISBLANK, so test for `""` when that matters.

### Example 3: Excluding Several Statuses

```excel
=IF(NOT(OR(C2="Cancelled",C2="Refunded")),"Active","Closed")
```

**Result:** `Closed` when C2 holds `Refunded`.

OR returns TRUE when C2 matches either excluded status. NOT inverts that result, so only orders outside the excluded list are "Active." Adding a third excluded status means adding one more test to OR.

<!-- Image 2: Truth Table for NOT. See Images/Logical/NOT.md -->

### Example 4: Testing Numbers for Zero

```excel
=NOT(D2)
```

**Result:** `FALSE` when D2 holds 7, and `TRUE` when D2 holds 0.

Google Sheets treats 0 as FALSE and any other number as TRUE. For a clearer test of zero, write `NOT(D2=0)`, which returns TRUE for every value except zero.

### Example 5: De Morgan Equivalence

```excel
=NOT(AND(E2>0,F2>0))
```

```excel
=OR(E2<=0,F2<=0)
```

**Result:** `TRUE` for both when E2 holds 5 and F2 holds 0.

AND is FALSE here because F2 is not above 0. NOT flips it to TRUE. The second formula applies De Morgan's law: the negation of an AND equals the OR of the negated tests. Use whichever form matches how the rule was written.

## Story Problems

### Problem 1: Keeping Only Active Products

A catalog export lists the status of five products in column B. Products that are not discontinued stay in the catalog.

| Product | Status |
| --- | --- |
| Desk Lamp | Active |
| Old Router | Discontinued |
| Phone Case | Active |
| Paper Tray | Discontinued |
| Pen Set | Pending |

**Task:** Put `Keep` or `Remove` in column C for each product, then count the rows marked `Remove`.

**Solution:**

```excel
=IF(NOT(B2="Discontinued"),"Keep","Remove")
```

```excel
=COUNTIF(C2:C6,"Remove")
```

**Answer:** `2`. Old Router and Paper Tray are discontinued. Desk Lamp, Phone Case and Pen Set stay in the catalog.

<!-- Image 3: Catalog Status Worksheet. See Images/Logical/NOT.md -->

### Problem 2: Finding Complete Contact Rows

A contact list needs a name, an email address and a phone number on every row before it is shared.

| Name | Email | Phone |
| --- | --- | --- |
| Ana Ruiz | ana@example.com | 555-0101 |
| Ben Ito |  | 555-0102 |
|  | cam@example.com | 555-0103 |
| Dee Park | dee@example.com | 555-0104 |

**Task:** Label each row `Complete` or `Incomplete` in column D, then count the complete rows.

**Solution:**

```excel
=IF(NOT(AND(A2<>"",B2<>"",C2<>"")),"Incomplete","Complete")
```

```excel
=COUNTIF(D2:D5,"Complete")
```

**Answer:** `2`. Ana Ruiz and Dee Park have all three fields. Ben Ito has no email, and the third row has no name.

## Use Cases

### Checkbox Status Labels

**Scenario:** A task sheet has a checkbox in column A that is ticked when a task is done. A reporting column should show the open tasks in words.

```excel
=IF(NOT(A2),"Still Open","Finished")
```

**Why It Works:** The checkbox returns TRUE when ticked. NOT sends an unticked box to the "Still Open" branch without a second test.

### Exclusion Lists

**Scenario:** A mailing list must skip every address on a hold list in column H.

```excel
=IF(NOT(COUNTIF(H2:H50,B2)>0),"Send","Hold")
```

**Why It Works:** COUNTIF returns the number of matches for the address in B2. NOT turns "no matches" into "Send," so the hold list can grow without changing the formula.

### Required Field Checks

**Scenario:** An order import needs a customer code in column A and a delivery date in column C before a row can be processed.

```excel
=IF(NOT(AND(A2<>"",C2<>"")),"Fix Row","Ready")
```

**Why It Works:** AND is TRUE only when both fields are filled, so NOT flags every row where either field is missing.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Text is passed where a logical value is expected, which Google Sheets returns as an error. | Compare the text explicitly, such as `NOT(A2="Yes")`. |
| Unexpected TRUE | An empty cell or a 0 is treated as FALSE. | Test the value directly, such as `NOT(A2=0)` or `NOT(A2="")`. |
| Unexpected FALSE | A non-zero number in Google Sheets is treated as TRUE. | Compare with the value you mean, such as `NOT(A2=5)`. |
| Hard to read | Double or triple negation hides the rule. | Replace the test with the opposite comparison, such as `A2<=5` for `NOT(A2>5)`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365 (Windows, Mac and web) | The help page describes TRUE and FALSE input only. It does not describe numeric or text input, so test those cases before relying on them. |
| Google Sheets | Available | Treats 0 as FALSE and other numbers as TRUE. Text input returns `#VALUE!`. Also accepts a cell reference that holds a logical expression. |

## Tips and Best Practices

- Prefer the opposite comparison when it is simpler: `A2<=5` is clearer than `NOT(A2>5)`.
- Use NOT with OR for exclusion lists so the excluded values are the only ones you have to maintain.
- Test blank cells, zero and text separately, because each one behaves differently from TRUE and FALSE.
- Use NOT(NOT(A2)) only when you need to force a value to TRUE or FALSE, and say so in a note nearby.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AND](AND.md) | Returns TRUE only when every test is TRUE. NOT is often wrapped around it. |
| [OR](OR.md) | Returns TRUE when any test is TRUE. Negate it to build an exclusion list. |
| [IF](IF.md) | Chooses a result from a TRUE or FALSE test. NOT is commonly used in its test. |
| [ISBLANK](../Information/ISBLANK.md) | Returns TRUE for an empty cell. NOT(ISBLANK()) tests for content. |
| [ISERROR](../Information/ISERROR.md) | Returns TRUE for any error. NOT(ISERROR()) tests for success. |
| [XOR](XOR.md) | Returns TRUE when an odd number of tests are TRUE. Use it when exactly one of two conditions should hold. |

## Official Documentation

- [Microsoft Support: NOT function](https://support.microsoft.com/en-us/excel/functions/not-function)
- [Google Docs Editors Help: NOT](https://support.google.com/docs/answer/3093305)
