---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Arithmetic Operations
use-case:
  - Cost Per Unit
  - Per Person Share
  - Unit Price Comparison
related:
  - ADD
  - IFERROR
  - MINUS
  - MULTIPLY
  - QUOTIENT
level: 1
source:
  - https://support.google.com/docs/answer/3093973
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - arithmetic
  - operators
  - sheets
---

# DIVIDE

## Description

**DIVIDE** returns one number divided by another. The first argument is the dividend (the number being divided) and the second is the divisor (the number you divide by). It is equivalent to the forward slash operator (`/`), so `=DIVIDE(B2, C2)` and `=B2/C2` return the same value.

Use DIVIDE when you want an operator call in a named form, for example when a formula builder or a script produces the function name rather than the symbol. For everyday work, many spreadsheet users write the operator directly because it is shorter and familiar.

The official help page states one rule clearly: the divisor cannot be 0. When the divisor is 0, the formula does not produce a number, so guard the formula with IFERROR or check the divisor before dividing. DIVIDE works only with two values at a time, so it cannot divide a range of numbers in one step. The function is available only in Google Sheets.

<!-- Image 1: DIVIDE Arguments. See Images/Google-specific/DIVIDE.md -->

## Syntax

```excel
=DIVIDE(dividend, divisor)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `dividend` | Yes | The number to be divided. It can be a number, a cell reference, or a formula that returns a number. |
| `divisor` | Yes | The number to divide by. It cannot be 0. |

### Return Value

A number: the dividend divided by the divisor. If the divisor is 0, the formula does not return a valid number, so the official page's rule that the divisor cannot equal 0 applies.

## Examples

### Example 1: Dividing Two Cells

```excel
=DIVIDE(B2, C2)
```

**Result:** `15` when B2 holds `120` and C2 holds `8`.

The formula returns the same value as `=B2/C2`. The result keeps its decimal places, so a division such as 10 divided by 4 returns `2.5`.

### Example 2: Dividing Typed Numbers

```excel
=DIVIDE(4, 2)
```

**Result:** `2`

Typed numbers work the same way as cell references and are useful for testing a formula before you point it at a data range.

### Example 3: Guarding Against a Zero Divisor

```excel
=IFERROR(DIVIDE(B2, C2), 0)
```

**Result:** `0` when C2 holds `0`, and the quotient otherwise.

Because the divisor cannot be 0, this pattern replaces a failed division with a value you choose. Choose the fallback carefully; a zero can hide a missing input.

<!-- Image 2: DIVIDE Zero Divisor Guard. See Images/Google-specific/DIVIDE.md -->

### Example 4: Dividing a Total by a Count

```excel
=DIVIDE(D2, COUNTA(A2:A9))
```

**Result:** The average value per filled row. With the Story Problem 1 data this returns `45`.

COUNTA counts the filled cells in the name column, so the divisor follows the data as rows are added.

## Story Problems

### Problem 1: Equal Share of a Group Bill

Eight friends share a dinner bill. Their names are in `A2:A9`, and the bill total is typed into `D2`.

| Name |
| --- |
| Amal |
| Bea |
| Cruz |
| Dana |
| Eli |
| Fay |
| Gus |
| Hana |

**Task:** With the bill total of 360 in `D2`, find each person's equal share and put it in `D3`.

**Solution:**

```excel
=DIVIDE(D2, COUNTA(A2:A9))
```

**Answer:** `45`, because 360 divided by 8 people is 45.

### Problem 2: Cost Per Unit for a Bulk Order

A warehouse buys 36 units of one product for a total of 1260.

| Item | Total Cost | Units |
| --- | --- | --- |
| Storage bin | 1260 | 36 |

**Task:** Put the cost of one unit in `D2`.

**Solution:**

```excel
=DIVIDE(B2, C2)
```

**Answer:** `35`, because 1260 divided by 36 is 35.

## Use Cases

### Cost Per Unit

**Scenario:** A purchasing team wants to know what each item costs once a bulk order arrives.

```excel
=DIVIDE(B2, C2)
```

**Why It Works:** The total cost in B2 is divided by the unit count in C2. Protect the formula with IFERROR when a unit count can be blank.

### Per Person Share

**Scenario:** A team splits a shared expense into equal parts based on the number of people who attended.

```excel
=IFERROR(DIVIDE(B2, COUNTA(A2:A20)), "No attendees")
```

**Why It Works:** COUNTA gives the number of names, and DIVIDE returns each person's share. The fallback text appears when no names are entered, which avoids dividing by 0.

### Unit Price Comparison

**Scenario:** A buyer compares two pack sizes of the same product to see which one costs less per item.

```excel
=DIVIDE(B2, C2)
```

**Why It Works:** Put the pack price in column B and the number of items in column C. Sort or compare the resulting unit prices to find the better value.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Division error | The divisor is 0 or an empty cell. The official page says the divisor cannot equal 0. | Check the divisor first or wrap the formula in IFERROR. |
| Unexpected value | A range was passed as an argument and DIVIDE works on two single values. | Divide one cell at a time, or use an array formula with the `/` operator. |
| Text value | A number was stored as text in the dividend or divisor. | Convert the cell with VALUE or re-enter the number as a number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is the slash operator, `=B2/C2`. | For a whole-number quotient without the remainder, Excel and Sheets both offer QUOTIENT. |
| Google Sheets | Available | Equivalent to the `/` operator. The divisor cannot be 0. |

## Tips and Best Practices

- Use the `/` operator in workbooks shared with Excel users so the formula works in both programs.
- Wrap DIVIDE in IFERROR where a blank input is possible, and pick a fallback that is clearly not a real value.
- Use COUNTA rather than a typed number for the divisor so averages update as rows are added.
- Keep totals and counts in separate cells so each division is easy to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ADD](ADD.md) | The matching operator function for addition. |
| [MINUS](MINUS.md) | The matching operator function for subtraction. |
| [MULTIPLY](MULTIPLY.md) | The matching operator function for multiplication. |
| [QUOTIENT](../Math%20%26%20Trig/QUOTIENT.md) | Returns only the integer part of a division, which DIVIDE does not do. |
| [IFERROR](../Logical/IFERROR.md) | Catches a failed division and returns a fallback value. |

## Official Documentation

- [Google Docs Editors Help: DIVIDE](https://support.google.com/docs/answer/3093973)
