---
domain: Spreadsheet Functions
category: Logical
subcategory: Error Handling
purpose:
  - Error Handling
use-case:
  - Lookup Fallbacks
  - Price Lookups
  - Safe Division
related:
  - IF
  - IFNA
  - INDEX
  - ISERROR
  - ISNA
  - LET
  - MATCH
  - VLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/iferror-function
  - https://support.google.com/docs/answer/3093304
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Error Handler
  - Trap Error
  - Replace Error Value
tags:
  - defensive-formulas
  - error-handling
  - excel
  - logical
  - sheets
---

# IFERROR

## Description

**IFERROR** evaluates a formula or value and returns a replacement when that result is an error. When the result is not an error, IFERROR returns it unchanged. Use it to keep a report readable when a lookup finds nothing, a divisor is zero, or an input is incomplete.

The most common use is a lookup. A VLOOKUP that cannot find its value returns #N/A, and IFERROR can replace that with "Not Found" so the error does not spread into other formulas. Division is the other frequent case, where a zero denominator returns #DIV/0! and a fallback such as 0 keeps totals working.

IFERROR catches every error type, including errors that point to real problems such as #REF! from a deleted column or #NAME? from a misspelled function. Those errors then stay hidden. For lookups, [IFNA](IFNA.md) is often the safer choice because it replaces only #N/A and lets other errors show. To run different logic depending on the error, use [IF](IF.md) with [ISERROR](../Information/ISERROR.md).

## Syntax

```excel
=IFERROR(value, value_if_error)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/IFERROR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The formula, cell reference, or value to check. If it returns an error, the replacement is returned. |
| `value_if_error` | Yes | The value returned when `value` is an error. It can be text, a number, a cell reference, a formula, or an empty string (""). |

### Return Value

The result of `value` when it is not an error. The value_if_error argument when `value` is any error. Microsoft Excel catches #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, and #NULL!. Google Sheets treats an omitted value_if_error as a blank.

## Examples

### Example 1: Lookup With a Fallback

```excel
=IFERROR(VLOOKUP(A2, B:C, 2, FALSE), "Not Found")
```

**Result:** `Not Found` when A2 does not appear in column B

When the lookup succeeds, the matching value from column C appears instead. The text "Not Found" is shown only when VLOOKUP returns an error.

### Example 2: Division Protection

```excel
=IFERROR(A2/B2, 0)
```

**Result:** `0` when A2 holds 50 and B2 holds 0

The division would return #DIV/0!. The formula returns 0 so that totals that add this cell keep working. Use "" or "N/A" instead when a zero would be misleading.

### Example 3: Text to Number With Fallback

```excel
=IFERROR(VALUE(A2), A2)
```

**Result:** `12.5` when A2 holds the text "12.5"

VALUE converts the text to a number. If A2 holds text that is not a number, such as "n/a", VALUE returns an error and the original text is returned instead.

### Example 4: Index and Match With a Fallback

```excel
=IFERROR(INDEX(C:C, MATCH(A2, B:B, 0)), "No Match")
```

**Result:** `No Match` when A2 is not in column B

MATCH returns #N/A when it cannot find the value, and INDEX passes that error through. IFERROR catches it at the end of the chain.

### Example 5: Fallback Chain

```excel
=IFERROR(VLOOKUP(A2, Current, 2, FALSE), IFERROR(VLOOKUP(A2, Archive, 2, FALSE), "Not in Either Table"))
```

**Result:** The value from Archive when Current has no match and Archive does, otherwise "Not in Either Table"

The second IFERROR runs only when the first lookup fails. Each named range is a separate table, so the formula checks the current list first and then the older one.

<!-- Image 2: Replacement Versus Original Result. See Images/Logical/IFERROR.md -->

### Example 6: Target Percentage With a Message

```excel
=IFERROR(ROUND(B2/C2*100, 1), "No Target")
```

**Result:** `No Target` when C2 holds 0

When a target exists, the formula returns the percentage rounded to one decimal place. A missing target gives a clear message instead of an error.

## Story Problems

### Problem 1: Sales per Visit

A store group records sales and visits for each shop. Hilltop has no visits recorded yet, which would make the ratio impossible to calculate.

| Shop | Sales | Visits | Sales per Visit |
| --- | --- | --- | --- |
| Riverside | 1800 | 60 | |
| Hilltop | 2400 | 0 | |
| Lakeside | 960 | 32 | |
| Northgate | 1500 | 25 | |

**Task:** Enter the formula in D2, fill it down to D5, and calculate the average of the values in column D.

**Solution:**

```excel
=IFERROR(B2/C2, "No Visits")
```

**Answer:** `40`. Riverside shows 30, Lakeside shows 30, and Northgate shows 60. Hilltop shows "No Visits", which AVERAGE skips because it ignores text. The average of 30, 30, and 60 is 40.

### Problem 2: Pricing an Order List

An order sheet looks up unit prices in a price list in H1:I3. Order O3 uses SKU Z-999, which is not in the list.

| Order | SKU | Quantity |
| --- | --- | --- |
| O1 | A-100 | 4 |
| O2 | C-300 | 2 |
| O3 | Z-999 | 3 |
| O4 | B-200 | 5 |

| SKU | Unit Price |
| --- | --- |
| A-100 | 12.50 |
| B-200 | 8.00 |
| C-300 | 25.00 |

**Task:** Enter the formula in D2 of the order sheet, fill it down to D5, and total column D.

**Solution:**

```excel
=IFERROR(VLOOKUP(B2, $H$1:$I$3, 2, FALSE) * C2, 0)
```

**Answer:** `140`. O1 is 50, O2 is 50, O3 is 0 because its SKU is missing, and O4 is 40. The total is 140. A 0 also shows that O3 needs attention, so pair this column with a check that counts zeros.

<!-- Image 3: Order Totals Panel. See Images/Logical/IFERROR.md -->

## Use Cases

### Lookup Fallbacks

**Scenario:** A customer record sheet shows a credit limit for each customer ID. New customers do not have a limit yet.

```excel
=IFERROR(VLOOKUP(CustomerID, CustomerMaster, 5, FALSE), 0)
```

**Why It Works:** The formula shows 0 for an unknown customer, so later calculations still run. Pair it with a separate check for new customers, because 0 can look like a real limit.

### Safe Division

**Scenario:** A dashboard shows profit margin for each product. Products with no revenue must not stop the summary from loading.

```excel
=IFERROR((Revenue-COGS)/Revenue, "N/A")
```

**Why It Works:** Only the rows with zero revenue show "N/A". The rest of the dashboard keeps its values, and the label makes the gap visible to the reader.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Real problem hidden | A broken reference or misspelled name returns an error that IFNA would have shown. | Use IFNA for lookups, and check formulas for #REF! or #NAME? periodically. |
| Fallback is an error | value_if_error itself refers to a failing formula. | Make the fallback a constant or wrap it in its own IFERROR. |
| Totals are wrong | "" was used as the fallback in a sum or product. | Use 0 when the result feeds a calculation. |
| Formula runs slowly | The protected formula is very large and evaluated for every row. | Move heavy calculations into helper columns, or store the result with LET. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2007 and later | Catches #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, and #NULL!. In Microsoft 365, it works element by element on arrays. |
| Google Sheets | Available | When value_if_error is omitted, the result is a blank. |

## Tips and Best Practices

- Use IFNA instead of IFERROR for lookups when you want other errors to stay visible.
- Choose the fallback for its use: 0 for calculations, "" for display, and a message for people who must act.
- Wrap only formulas with a real error case, so genuine mistakes are not hidden.
- Store a repeated expression in LET when the fallback needs the same result again.
- Test each protected formula with an input that produces the error, such as a zero divisor or a missing key.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](IF.md) | Runs different logic for errors and successes. |
| [IFNA](IFNA.md) | Replaces only #N/A, so other errors stay visible. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Often wrapped with MATCH inside IFERROR. |
| [ISERROR](../Information/ISERROR.md) | Tests whether a value is any error, for use inside IF. |
| [ISNA](../Information/ISNA.md) | Tests whether a value is #N/A. |
| [LET](LET.md) | Stores a result once so the fallback can reuse it. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Returns a position and an error when the value is missing. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | The lookup most often protected with IFERROR. |

## Official Documentation

- [Microsoft Support: IFERROR function](https://support.microsoft.com/en-us/excel/functions/iferror-function)
- [Google Docs Editors Help: IFERROR](https://support.google.com/docs/answer/3093304)
