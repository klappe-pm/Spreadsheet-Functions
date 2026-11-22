---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Conditional Logic
use-case:
  - Price Change Detection
  - Reconciliation Mismatch Flags
related:
  - EQ
  - GTE
  - IF
  - LTE
  - NOT
level: 1
source:
  - https://support.google.com/docs/answer/3093981
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Not Equal
tags:
  - comparison
  - operator
  - sheets
---

# NE

## Description

**NE** compares two values and returns `TRUE` when they are not equal, and `FALSE` when they are equal. It is the named form of the `<>` operator, so `=NE(B2, C2)` and `=B2<>C2` produce the same result.

Use NE to flag differences: a ledger that disagrees with a bank statement, a price that changed since the last list, or a status that no longer matches the plan. The logical result works directly inside IF, AND, OR and FILTER.

NE is the opposite of EQ. To test for equality, use EQ or the `=` operator. Microsoft Excel has no NE function, so Excel users write the `<>` operator instead.

## Syntax

```excel
=NE(value1, value2)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/NE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value to compare. Usually a cell reference. |
| `value2` | Yes | The value that `value1` is tested against for inequality. |

### Return Value

A logical value: `TRUE` when the two values are not equal, and `FALSE` when they are equal. NE takes exactly two arguments.

## Examples

All examples use this invoice status check.

| Invoice | Ledger Status | Bank Status |
| --- | --- | --- |
| INV-201 | Paid | Paid |
| INV-202 | Open | Paid |
| INV-203 | Paid | Paid |

### Example 1: Matching Statuses

```excel
=NE(B2, C2)
```

**Result:** `FALSE`

Both systems show INV-201 as Paid, so the values are equal.

### Example 2: Mismatched Statuses

```excel
=NE(B3, C3)
```

**Result:** `TRUE`

The ledger shows INV-202 as Open while the bank shows it as Paid.

<!-- Image 2: Invoice Mismatch Results. See Images/Google-specific/NE.md -->

### Example 3: Compare Numbers

```excel
=NE(1200, 1250)
```

**Result:** `TRUE`

The two amounts differ, so the test returns `TRUE`.

### Example 4: Label the Result With IF

```excel
=IF(NE(B3, C3), "Check invoice", "Matches")
```

**Result:** `Check invoice`

IF converts the logical result into a label that a reviewer can filter on.

### Example 5: Compare a Cell With a Literal

```excel
=NE(B4, "Paid")
```

**Result:** `FALSE`

INV-203 shows Paid in the ledger, so the test against the literal text fails to find a difference.

## Story Problems

### Problem 1: Bank Reconciliation

A bookkeeper compares each invoice status in the ledger with the status reported by the bank. The data is in `A1:C5`.

| Invoice | Ledger | Bank |
| --- | --- | --- |
| INV-310 | Paid | Paid |
| INV-311 | Open | Paid |
| INV-312 | Paid | Paid |
| INV-313 | Open | Open |

**Task:** In column D, show `TRUE` for each invoice whose statuses disagree.

**Solution:**

```excel
=NE(B2, C2)
```

Fill the formula down to D5.

**Answer:** `FALSE`, `TRUE`, `FALSE` and `FALSE` for INV-310 to INV-313. Only INV-311 differs, because the ledger shows it as Open and the bank shows it as Paid.

### Problem 2: Price List Changes

A distributor sends a new price list each month. The old price is in column B and the new price is in column C of `A1:C4`.

| Product | Old Price | New Price |
| --- | --- | --- |
| Filter | 18.50 | 18.50 |
| Hose | 12.00 | 12.75 |
| Gasket | 4.20 | 4.20 |

**Task:** In column D, show `TRUE` for each product whose price changed.

**Solution:**

```excel
=NE(B2, C2)
```

Fill the formula down to D4.

**Answer:** `FALSE`, `TRUE` and `FALSE` for Filter, Hose and Gasket. Only the hose price moved, from 12.00 to 12.75.

## Use Cases

### Reconciliation Mismatch Flags

**Scenario:** An accounts team needs to see every invoice where the ledger and bank disagree before the month closes.

```excel
=FILTER(A2:A50, ARRAYFORMULA(NE(B2:B50, C2:C50)))
```

**Why It Works:** ARRAYFORMULA applies NE to each row, and FILTER returns only the invoice numbers where the statuses differ.

### Price Change Detection

**Scenario:** A purchasing manager reviews a new supplier list and wants to see only the products whose prices changed.

```excel
=IF(NE(B2, C2), "Changed", "")
```

**Why It Works:** The label appears only on rows where the two prices differ, so unchanged items stay blank.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `TRUE` for values that look the same | One value has a trailing space or is text, not a number. | Clean the text with TRIM or convert it with VALUE. |
| Formula does not calculate | The function has fewer or more than two arguments. | Provide exactly two values. |
| Result is inverted | The formula used NE when EQ was intended. | Use EQ for equality and NE for difference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `<>` operator, for example `=B2<>C2`. |
| Google Sheets | Available | Returns the same result as the `<>` operator. |

## Tips and Best Practices

- Use NE to find differences between two lists before you try to explain them.
- Run TRIM on imported text before comparing, because a stray space makes equal-looking values differ.
- Combine NE with FILTER to produce an exception list automatically.
- Pair NE with IF to add a readable label to each row.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EQ](EQ.md) | Tests whether two values are equal. The opposite test. |
| [GTE](GTE.md) | Tests whether one value is at least another. |
| [LTE](LTE.md) | Tests whether one value is at most another. |
| [IF](../Logical/IF.md) | Uses the logical result to return a chosen label. |
| [NOT](../Logical/NOT.md) | Reverses a logical value, as an alternative to EQ. |

## Official Documentation

- [Google Docs Editors Help: NE](https://support.google.com/docs/answer/3093981)
