---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Inventory Count Checks
  - Order Matching
  - Stock Count Reconciliation
related:
  - GT
  - GTE
  - IF
  - LT
  - LTE
  - NE
level: 2
source:
  - https://support.google.com/docs/answer/3093593
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Equal Test
tags:
  - comparison
  - logic
  - operators
  - sheets
---

# EQ

## Description

**EQ** tests whether two values are equal. It returns `TRUE` when the values match and `FALSE` otherwise. It is equivalent to the equals operator (`=`), so `=EQ(B2, C2)` and `=B2=C2` give the same answer.

Use EQ when a comparison needs to be written as a function, for example inside a larger formula that already uses function syntax, or when a script builds the test by name. In everyday sheets most people write the `=` operator directly. Both forms are read the same way by Google Sheets.

The official help page documents only the basic rule: the result is `TRUE` for equal values and `FALSE` for unequal ones. It does not explain how text compares with numbers, so test a sample before relying on a comparison between a number stored as text and a number. EQ is available only in Google Sheets. Its companions NE (not equal), LT, LTE, GT and GTE test the other comparison directions.

<!-- Image 1: EQ Result Column. See Images/Google-specific/EQ.md -->

## Syntax

```excel
=EQ(value1, value2)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value to compare. It can be a number, text, a cell reference, or a formula result. |
| `value2` | Yes | The second value. The function tests whether it equals `value1`. |

### Return Value

`TRUE` when the two values are equal, and `FALSE` when they are not. The result is a logical value, so it can feed IF, COUNTIF or any other function that accepts a true or false test.

## Examples

### Example 1: Comparing Two Numbers That Match

```excel
=EQ(B2, C2)
```

**Result:** `TRUE` when B2 and C2 both hold `10`.

The formula returns `TRUE` because the two numbers are identical.

### Example 2: Comparing Two Numbers That Differ

```excel
=EQ(B3, C3)
```

**Result:** `FALSE` when B3 holds `8` and C3 holds `7`.

Any difference, however small, returns `FALSE`.

### Example 3: Returning a Message From the Test

```excel
=IF(EQ(B2, C2), "Counts match", "Recount needed")
```

**Result:** `Counts match` when the two values are equal, and `Recount needed` otherwise.

Wrapping EQ in IF turns the true or false test into a message that a reader can act on.

### Example 4: Checking a Text Value

```excel
=EQ(A2, "Shipped")
```

**Result:** `TRUE` when A2 contains the word Shipped, and `FALSE` for any other status.

Text comparisons are useful for status columns. Keep the spelling and capitalization consistent across the sheet, or use a clean-up step with TRIM first.

## Story Problems

### Problem 1: Stock Count Reconciliation

A warehouse planned a stock count for five bins. The planned quantity is in column B and the counted quantity is in column C. The team wants to know which bins match.

| Bin | Planned | Counted |
| --- | --- | --- |
| A1 | 10 | 10 |
| A2 | 8 | 7 |
| A3 | 5 | 5 |
| A4 | 12 | 12 |
| A5 | 3 | 4 |

**Task:** Fill `D2:D6` with a test for each bin, then count how many bins match.

**Solution:**

```excel
=EQ(B2, C2)
```

Fill this formula down `D2:D6`, then count the matches with `=COUNTIF(D2:D6, TRUE)` in a separate cell.

**Answer:** `3`, because bins A1, A3 and A4 match. Bins A2 and A5 need a recount.

<!-- Image 2: EQ Match Column. See Images/Google-specific/EQ.md -->

### Problem 2: Confirming a Shipment Against an Order

A buyer ordered 24 units and the supplier confirmed 24. A second order of 40 units was confirmed as 38.

| Order | Ordered | Confirmed |
| --- | --- | --- |
| PO 101 | 24 | 24 |
| PO 102 | 40 | 38 |

**Task:** Put a match test for each order in column D and count the orders that match.

**Solution:**

```excel
=EQ(B2, C2)
```

**Answer:** `1`, because only PO 101 matches. PO 102 is 2 units short and needs follow up.

## Use Cases

### Inventory Count Checks

**Scenario:** A stock controller compares the system count with the physical count after each shift.

```excel
=IF(EQ(B2, C2), "OK", "Recount")
```

**Why It Works:** The formula reports OK only when the counts are identical. Any difference, including a one unit gap, flags the row for a recount.

### Order Matching

**Scenario:** An accounts team matches supplier confirmations to purchase orders before paying invoices.

```excel
=COUNTIF(D2:D50, TRUE)
```

**Why It Works:** After EQ fills column D with TRUE or FALSE, COUNTIF counts the matches. A total below the number of orders points to the rows to review.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected `FALSE` | A number is stored as text on one side of the comparison. | Convert the text with VALUE, or re-enter the number. |
| Unexpected `FALSE` | Text differs by extra spaces or capitalization. | Clean the values with TRIM first, then compare. |
| Blank or `FALSE` for blank cells | An empty cell is compared with a value. | Check for blanks with IF before running the test. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is the equals operator, `=B2=C2`. | Excel has no EQ function; the operator returns the same TRUE or FALSE result. |
| Google Sheets | Available | Equivalent to the `=` operator. Returns TRUE when values are equal and FALSE otherwise. |

## Tips and Best Practices

- Use `=B2=C2` in workbooks that Excel users open, because the operator works in both programs.
- Test a sample of mixed types, such as a number stored as text, before trusting a count built from EQ.
- Combine EQ with COUNTIF to count matches, or with FILTER to list the mismatched rows.
- Name the columns being compared so the test is easy to read in a review.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NE](NE.md) | Returns the opposite result: TRUE when the values differ. |
| [GT](GT.md) | Tests whether the first value is greater than the second. |
| [GTE](GTE.md) | Tests whether the first value is greater than or equal to the second. |
| [LT](LT.md) | Tests whether the first value is less than the second. |
| [LTE](LTE.md) | Tests whether the first value is less than or equal to the second. |
| [IF](../Logical/IF.md) | Turns the TRUE or FALSE result into a message or another value. |

## Official Documentation

- [Google Docs Editors Help: EQ](https://support.google.com/docs/answer/3093593)
