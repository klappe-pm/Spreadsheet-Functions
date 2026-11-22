---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Order Value Caps
  - Shipping Weight Limits
related:
  - GT
  - GTE
  - IF
  - LT
  - NE
level: 1
source:
  - https://support.google.com/docs/answer/3093976
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Less Than or Equal
tags:
  - comparison
  - operator
  - sheets
---

# LTE

## Description

**LTE** compares two values and returns `TRUE` when the first is less than or equal to the second. It returns `FALSE` otherwise. The function is the named form of the `<=` operator, so `=LTE(B2, C2)` and `=B2<=C2` produce the same result.

Use LTE when the comparison should be written as a function name, for example in a formula that a script or template generates. The logical result works directly inside IF, AND, OR and FILTER.

LTE includes the boundary. A value equal to the second argument returns `TRUE`. For a strict test that excludes the boundary, use LT. Microsoft Excel has no LTE function, so Excel users write the `<=` operator instead.

## Syntax

```excel
=LTE(value1, value2)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/LTE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The value to test. Usually a cell reference or a number. |
| `value2` | Yes | The value that `value1` is compared against. |

### Return Value

A logical value: `TRUE` when `value1` is less than or equal to `value2`, and `FALSE` when it is greater. LTE takes exactly two arguments.

## Examples

All examples use this parcel weight check, where the limit is 5 kg.

| Parcel | Weight (kg) | Limit (kg) |
| --- | --- | --- |
| Carton | 4.5 | 5 |
| Crate | 5 | 5 |
| Drum | 5.2 | 5 |

### Example 1: Under the Limit

```excel
=LTE(B2, C2)
```

**Result:** `TRUE`

The carton weighs 4.5 kg, which is less than the 5 kg limit.

### Example 2: Equal Values Pass

```excel
=LTE(B3, C3)
```

**Result:** `TRUE`

The crate weighs exactly 5 kg. The boundary value counts as a match.

### Example 3: Over the Limit

```excel
=LTE(B4, C4)
```

**Result:** `FALSE`

The drum weighs 5.2 kg, which is more than the limit.

<!-- Image 2: Weight Check Results. See Images/Google-specific/LTE.md -->

### Example 4: Compare With a Literal Number

```excel
=LTE(B4, 6)
```

**Result:** `TRUE`

The drum's 5.2 kg is less than 6, so the test passes against this higher limit.

### Example 5: Label the Result With IF

```excel
=IF(LTE(B2, C2), "Within limit", "Overweight")
```

**Result:** `Within limit`

IF converts the logical result into a label for the shipping team.

## Story Problems

### Problem 1: Courier Weight Limit

A courier accepts parcels up to and including 5 kg. Weights are in column B of `A1:B4`, and the limit of 5 is typed into cell `E1`.

| Parcel | Weight (kg) |
| --- | --- |
| Box | 5.0 |
| Crate | 6.0 |
| Bag | 3.8 |

**Task:** In column C, show `TRUE` for each parcel the courier can accept.

**Solution:**

```excel
=LTE(B2, $E$1)
```

Fill the formula down to C4.

**Answer:** `TRUE`, `FALSE` and `TRUE` for Box, Crate and Bag. The box weighs exactly 5 kg, so it is accepted, and the crate at 6 kg is refused.

### Problem 2: Order Value Cap for Free Shipping

A shop offers free shipping on orders of 100 or less when a customer buys during a promotion. Order totals are in column B of `A1:B4`, and the cap of 100 is in cell `E1`.

| Order | Total |
| --- | --- |
| 1042 | 120 |
| 1043 | 100 |
| 1044 | 80 |

**Task:** In column C, show `TRUE` for each order that qualifies for free shipping.

**Solution:**

```excel
=LTE(B2, $E$1)
```

Fill the formula down to C4.

**Answer:** `FALSE`, `TRUE` and `TRUE` for orders 1042, 1043 and 1044. Order 1043 equals the cap and qualifies.

## Use Cases

### Shipping Weight Limits

**Scenario:** A logistics coordinator checks whether each parcel stays within the carrier's weight limit before booking a pickup.

```excel
=IF(LTE(B2, $F$1), "Book", "Re-pack")
```

**Why It Works:** The limit sits in `F1`, so a new carrier limit updates every decision. Parcels at exactly the limit are booked.

### Order Value Caps

**Scenario:** A sales team approves discounts only on orders whose subtotal is at or below a set cap.

```excel
=IF(LTE(C2, $H$1), "Discount approved", "Above cap")
```

**Why It Works:** The formula compares each subtotal with the cap in `H1` and labels the result, so reviewers see the decision on each line.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a value that looks equal | One side is text, such as a number typed as text. | Convert the text with VALUE or retype the source cell as a number. |
| Boundary value unexpectedly passes | LTE includes equal values. | Use LT when the boundary should fail. |
| Formula does not calculate | The function has fewer or more than two arguments. | Provide exactly two values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `<=` operator, for example `=B2<=C2`. |
| Google Sheets | Available | Returns the same result as the `<=` operator. |

## Tips and Best Practices

- Use LTE for limits that allow the exact value, such as a weight cap or a discount cap.
- Store limits in their own cells and reference them with absolute references so one change updates every row.
- Check that compared values are numbers before relying on the result.
- Combine LTE with AND to test two limits at once, such as a minimum and a maximum.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LT](LT.md) | Strictly less than. Excludes the boundary value. |
| [GTE](GTE.md) | Greater than or equal. The opposite test. |
| [GT](GT.md) | Strictly greater than. |
| [NE](NE.md) | Tests whether two values differ. |
| [IF](../Logical/IF.md) | Uses the logical result to return a chosen value. |

## Official Documentation

- [Google Docs Editors Help: LTE](https://support.google.com/docs/answer/3093976)
