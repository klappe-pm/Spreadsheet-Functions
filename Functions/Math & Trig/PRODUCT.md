---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Aggregation
  - Arithmetic Operations
use-case:
  - Discount Chain Totals
  - Joint Probability Estimates
  - Scoring Multipliers
related:
  - FACT
  - MMULT
  - SUM
  - SUMPRODUCT
  - SUMSQ
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/product-function
  - https://support.google.com/docs/answer/3093502
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Multiply Numbers
  - Multiply Range
tags:
  - arithmetic
  - excel
  - multiplication
  - sheets
---

# PRODUCT

## Description

**PRODUCT** multiplies all the numbers you give it and returns the result. Each argument can be a single number, a cell reference or a range. `=PRODUCT(2,3,4)` returns 24, and `=PRODUCT(B2:B4)` multiplies every number in the range B2 to B4. Excel accepts up to 255 arguments, and Google Sheets documents a limit of 30 factors.

Use PRODUCT when you need the multiplication of a whole column or a list of factors, such as a chain of discounts, the combined probability of independent events, or a set of score multipliers. For two or three cells, the multiplication operator (`A2*B2*C2`) is just as clear. PRODUCT is the better choice when the range grows or changes size.

PRODUCT skips empty cells and any text or logical values inside a range or reference. Those values do not count as zero, so a blank cell does not change the result, but a typed zero does. Because the function ignores text inside ranges, check the input column for a missing factor when the result looks too large or too small.

## Syntax

```excel
=PRODUCT(number1, [number2], ...)
```

<!-- Image 1: Factor Range Layout. See Images/Math & Trig/PRODUCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, or range to multiply. |
| `number2`, ... | No | Additional numbers or ranges. Excel accepts up to 255 arguments in total. |

### Return Value

A number: the product of all the numeric values supplied. Empty cells, logical values and text inside a range or reference are ignored. A single argument returns that number. A zero in the list makes the whole result zero.

## Examples

### Example 1: Multiply a Range of Factors

The discount factors are in `B2:B4` and hold 0.9, 0.8 and 0.95.

```excel
=PRODUCT(B2:B4)
```

**Result:** `0.684`

Each factor is the share of the price that remains after a discount. Multiplying the three factors gives the share left after all three discounts.

### Example 2: Multiply Typed Numbers

```excel
=PRODUCT(1,2,3,4,5)
```

**Result:** `120`

Each typed number is a factor. The product of the integers from 1 to 5 is 120, which equals 5 factorial.

### Example 3: Skip Text and Blank Cells

The values in `A2:A6` are 2, the word `Pending`, a blank cell, 5 and 3.

```excel
=PRODUCT(A2:A6)
```

**Result:** `30`

PRODUCT multiplies 2, 5 and 3. The text and the blank cell are ignored, so they do not change the result or cause an error.

### Example 4: Apply a Chain of Discounts to a Price

```excel
=ROUND(250*PRODUCT(B2:B4), 2)
```

**Result:** `171`

The price is multiplied by the product of the three discount factors. The 250 base price is not part of the range, so it is typed directly in the formula.

### Example 5: Multiply a Product Total by a Count

```excel
=PRODUCT(B2:B4, 2)
```

**Result:** `1.368`

PRODUCT multiplies each argument in turn. Here the range product, 0.684, is multiplied by the additional argument 2.

## Story Problems

### Problem 1: Final Price After Three Discounts

A store takes three discounts off a $250 jacket one after another. Each discount is applied to the price left after the previous one.

| Discount Stage | Factor (share paid) |
| --- | --- |
| Seasonal Promotion (10 percent off) | 0.9 |
| Loyalty Card (20 percent off) | 0.8 |
| Clearance (5 percent off) | 0.95 |

**Task:** Calculate the final price of the jacket, rounded to cents.

**Solution:**

```excel
=ROUND(250*PRODUCT(B2:B4), 2)
```

**Answer:** `171.00`. The three factors multiply to 0.684, and 250 times 0.684 is 171.00.

<!-- Image 2: Discount Chain Worksheet. See Images/Math & Trig/PRODUCT.md -->

### Problem 2: Chance That All Three Checks Pass

A quality team runs three independent checks on each unit. The pass rates are 98 percent, 95 percent and 99 percent. The team wants the probability that a unit passes all three.

| Check | Pass Rate |
| --- | --- |
| Dimensional | 0.98 |
| Electrical | 0.95 |
| Visual | 0.99 |

**Task:** Calculate the probability that a unit passes all three checks, rounded to four decimal places.

**Solution:**

```excel
=ROUND(PRODUCT(B2:B4), 4)
```

**Answer:** `0.9217`, or about 92.17 percent. For independent checks, the probabilities multiply, and 0.98 times 0.95 times 0.99 is 0.92169.

## Use Cases

### Discount Chain Totals

**Scenario:** A retailer applies a sequence of promotions to a shopping cart, and each promotion is a row in a table.

```excel
=ROUND(B2*PRODUCT(C2:C6), 2)
```

**Why It Works:** Each row in `C2:C6` holds the share of the price that remains after one promotion. Multiplying the cart total in `B2` by the product gives the final amount. Store the factors as decimals, not percentages typed as whole numbers.

### Joint Probability Estimates

**Scenario:** A risk analyst estimates the chance that several independent events all happen.

```excel
=PRODUCT(D2:D4)
```

**Why It Works:** For independent events, the probability that all occur is the product of the individual probabilities. Each value in `D2:D4` must be between 0 and 1.

### Scoring Multipliers

**Scenario:** A procurement team scores a supplier by multiplying weights that reward or penalize each criterion.

```excel
=PRODUCT(E2:E6)
```

**Why It Works:** Multipliers above 1 raise the score and multipliers below 1 lower it. A single multiplier of 0 removes the supplier entirely, so review the inputs before ranking.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result is zero | A factor in the range is 0. | Find the zero with a filter, and correct the input if it should not be zero. |
| Result is far too small | A percentage was entered as a whole number, such as 10 instead of 0.1. | Enter rates as decimals, or divide the percentage by 100. |
| Result is too large | A factor is missing, so a multiplier that should reduce the total is skipped. | Check that every expected factor is present in the range. |
| Missing factor is ignored | A cell in the range is empty or contains text. | Fill the empty cell or convert the text to a number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Accepts up to 255 arguments. Ignores empty cells, text and logical values in ranges and references. |
| Google Sheets | Available | Documents up to 30 factors. Empty cells in a range are ignored. |

## Tips and Best Practices

- Enter discounts as factors (1 minus the rate), such as 0.9 for a 10 percent discount.
- Use PRODUCT for a range and `*` for two or three named cells, which is easier to read.
- Round only the final result, not each factor, to avoid compounding rounding error.
- Check the range for missing values with COUNT before you trust a product.
- Confirm that every probability in a range lies between 0 and 1 before you multiply them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FACT](FACT.md) | Product of the whole numbers from 1 to n, a special case of PRODUCT. |
| [MMULT](MMULT.md) | Matrix multiplication, which combines rows and columns rather than one list. |
| [SUM](SUM.md) | Adds the numbers instead of multiplying them. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies matching items across arrays and adds the results. |
| [SUMSQ](SUMSQ.md) | Adds the squares of the numbers, the additive counterpart to squaring each factor. |

## Official Documentation

- [Microsoft Support: PRODUCT function](https://support.microsoft.com/en-us/excel/functions/product-function)
- [Google Docs Editors Help: PRODUCT](https://support.google.com/docs/answer/3093502)
