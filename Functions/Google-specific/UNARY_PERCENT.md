---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Financial Modeling
  - Number Formatting
use-case:
  - Discount Calculations
  - Markup Calculations
related:
  - TO_PERCENT
  - UMINUS
  - UPLUS
level: 2
source:
  - https://support.google.com/docs/answer/3093982
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Percent Operator
tags:
  - operators
  - percentages
  - sheets
---

# UNARY_PERCENT

## Description

**UNARY_PERCENT** returns a value interpreted as a percentage. It divides the number by 100, so `UNARY_PERCENT(100)` returns `1`, which is the same as 100 percent. It is the function form of the percent operator, the `%` sign placed after a number in a formula. Writing `=B2%` and writing `=UNARY_PERCENT(B2)` give the same result.

Use UNARY_PERCENT when a source gives rates as whole numbers, such as 15 for fifteen percent, and a calculation needs the decimal. A discount of 15 becomes 0.15, so a price of 200 becomes 200 times (1 minus 0.15), which is 170. The function is also useful when a formula would otherwise contain a `%` sign that is hard to read inside a longer expression.

UNARY_PERCENT is roughly the inverse of TO_PERCENT. TO_PERCENT only changes the display of a decimal, while UNARY_PERCENT changes the value itself. Applying UNARY_PERCENT to a number that is already a decimal divides it by 100 again, which is a common source of unexpected results.

## Syntax

```excel
=UNARY_PERCENT(percentage)
```

<!-- Image 1: Whole Number Rate Converted to a Decimal. See Images/Google-specific/UNARY_PERCENT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `percentage` | Yes | The number, or a reference to a cell that holds a number, to interpret as a percentage. The value is divided by 100. |

### Return Value

A decimal number equal to the input divided by 100. For example, 100 returns 1, and 93 returns 0.93. The official documentation does not describe error conditions or limits for UNARY_PERCENT.

## Examples

Each example is a separate formula, and the cell references assume the values shown in each example.

### Example 1: The Documented Case

```excel
=UNARY_PERCENT(100)
```

**Result:** `1`

A value of 100 is the whole, so it returns 1.

### Example 2: Whole Number Rate

```excel
=UNARY_PERCENT(15)
```

**Result:** `0.15`

Fifteen percent is returned as the decimal 0.15.

### Example 3: Cell Reference in a Price Calculation

```excel
=200*(1-UNARY_PERCENT(B2))
```

**Result:** `170` when `B2` holds `15`

The rate in `B2` becomes 0.15, the discount is taken from 200, and the discounted price is 170.

<!-- Image 2: Discount Calculation Steps. See Images/Google-specific/UNARY_PERCENT.md -->

### Example 4: Fractional Rate

```excel
=UNARY_PERCENT(B2)
```

**Result:** `0.075` when `B2` holds `7.5`

A rate with a decimal part is divided the same way, so 7.5 becomes 0.075.

### Example 5: Same Result as the Percent Operator

```excel
=B2%
```

**Result:** `0.15` when `B2` holds `15`

The percent operator in a formula returns the same value as UNARY_PERCENT for the same input.

## Story Problems

### Problem 1: Discounted Prices

A store sells an item for 200 and offers three discounts, written as whole numbers in `B2:B4`. The price sheet must show the price after each discount.

| Discount | Rate |
| --- | --- |
| Spring | 15 |
| Member | 20 |
| Clearance | 7.5 |

**Task:** Calculate the discounted price for each rate in `C2:C4`, using the item price of 200 in `E1`.

**Solution:**

```excel
=$E$1*(1-UNARY_PERCENT(B2))
```

**Answer:** `170` for Spring, `160` for Member and `185` for Clearance. Each result is 200 reduced by the decimal rate: 0.15, 0.2 and 0.075.

<!-- Image 3: Discounted Price Table. See Images/Google-specific/UNARY_PERCENT.md -->

### Problem 2: Marked Up Cost

A bakery buys flour for a cost of 80 and wants to price it with a markup of 25 percent. The markup is entered as the whole number 25.

**Task:** Calculate the selling price in `B3`, using the cost in `B1` and the markup in `B2`.

**Solution:**

```excel
=B1*(1+UNARY_PERCENT(B2))
```

**Answer:** `100`, because 80 multiplied by 1.25 is 100. The markup of 25 becomes 0.25 before it is added to 1.

## Use Cases

### Discount Calculations

**Scenario:** A promotions sheet lists discounts as whole numbers, and the final price formula needs them as decimals.

```excel
=ListPrice*(1-UNARY_PERCENT(Discount))
```

**Why It Works:** The discount becomes a decimal before it reduces the price, so the formula returns the correct final price for each row.

### Markup Calculations

**Scenario:** A pricing sheet adds a markup percentage to each product cost, and the percentages are typed as whole numbers.

```excel
=Cost*(1+UNARY_PERCENT(Markup))
```

**Why It Works:** The formula adds the decimal markup to 1, so the selling price rises by the stated percentage of the cost.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result is 100 times too small | The input is already a decimal, such as 0.15, and the function divides it by 100 again. | Pass whole numbers to UNARY_PERCENT, or skip the function when the input is already a decimal. |
| Result looks like a plain decimal | UNARY_PERCENT returns a number, and the cell has no percent format. | Apply TO_PERCENT or the Percent format to the result cell. |
| Discount produces a larger price | The formula adds the rate where it should subtract it, or the wrong sign is used. | Check whether the formula uses 1 minus the rate for discounts and 1 plus the rate for markups. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as a function | Use the percent operator, such as `=B2%`, which returns the decimal. |
| Google Sheets | Available | Works as a function, and matches the percent operator for the same input. |

## Tips and Best Practices

- Check whether a source file stores rates as whole numbers or decimals before choosing UNARY_PERCENT or TO_PERCENT.
- Keep a single rate convention across a workbook, so one formula does not divide a decimal by 100 by mistake.
- Use 1 minus the rate for discounts and 1 plus the rate for markups, so the sign of the change is clear in the formula.
- Use TO_PERCENT to display a decimal as a percentage, and UNARY_PERCENT to convert a whole number into a decimal.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TO_PERCENT](TO_PERCENT.md) | Displays a decimal as a percentage without changing its value. |
| [UMINUS](UMINUS.md) | Reverses the sign of a number. |
| [UPLUS](UPLUS.md) | Returns a number unchanged. |

## Official Documentation

- [Google Docs Editors Help: UNARY_PERCENT](https://support.google.com/docs/answer/3093982)
