---
domain: Spreadsheet Functions
category: Logical
subcategory: Error Handling
purpose:
  - Error Handling
use-case:
  - Multi-Source Lookups
  - Regional Assignments
  - Shipping Surcharges
related:
  - IFERROR
  - INDEX
  - ISNA
  - MATCH
  - NA
  - VLOOKUP
  - XLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/ifna-function
  - https://support.google.com/docs/answer/9365944
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - If NA
  - Not Available Handler
  - Lookup Error Handler
tags:
  - error-handling
  - excel
  - lookup-functions
  - na-error
  - sheets
---

# IFNA

## Description

**IFNA** returns a replacement value when a formula produces the #N/A error, and returns every other result unchanged. #N/A means that a value was not found, which is the usual outcome of a failed lookup. Because IFNA replaces only that error, it handles the expected "not found" case without hiding other problems.

This difference matters for lookups. A [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md), [MATCH](../Lookup%20%26%20Reference/MATCH.md), or [INDEX](../Lookup%20%26%20Reference/INDEX.md) with MATCH returns #N/A when the key is missing, and IFNA can show "Not Found" in its place. If the same formula fails for a different reason, such as a deleted column that produces #REF!, that error still appears, so you can fix the cause.

[IFERROR](IFERROR.md) catches every error type, which is useful for division and external data but can conceal broken formulas in lookups. Use IFNA when you want to handle only missing matches. Functions such as [SUMIF](../Math%20%26%20Trig/SUMIF.md) and COUNTIF return 0 when nothing matches, not #N/A, so IFNA does nothing for them.

## Syntax

```excel
=IFNA(value, value_if_na)
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/IFNA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The formula, cell reference, or value to check. If it returns #N/A, the replacement is returned. Any other error passes through unchanged. |
| `value_if_na` | Yes | The value returned only when `value` is #N/A. It can be text, a number, a cell reference, a formula, or an empty string (""). |

### Return Value

The result of `value` when it is not #N/A. The value_if_na argument when `value` is #N/A. Errors other than #N/A, such as #DIV/0!, #REF!, and #VALUE!, are returned as they are.

## Examples

### Example 1: Lookup With a Replacement

```excel
=IFNA(VLOOKUP(A2, B:C, 2, FALSE), "Not Found")
```

**Result:** `Not Found` when A2 is not in column B

When the key exists, the matching value from column C is returned. Only the missing-key case shows the replacement text.

### Example 2: IFNA Lets Other Errors Show

```excel
=IFNA(A2/B2, 0)
```

**Result:** `#DIV/0!` when A2 holds 50 and B2 holds 0

The formula produces a division error, which is not #N/A, so IFNA passes it through. The visible error reminds you to fix the zero divisor. IFERROR would have returned 0 and hidden the problem.

### Example 3: Position Lookup With a Default

```excel
=IFNA(MATCH(A2, B:B, 0), 0)
```

**Result:** `0` when A2 is not in column B

Returning 0 is useful when the position feeds another formula that treats 0 as no position. Choose the default that the next step can handle.

<!-- Image 2: Replacement Versus Pass-Through. See Images/Logical/IFNA.md -->

### Example 4: Fallback Across Two Tables

```excel
=IFNA(VLOOKUP(A2, Regions, 2, FALSE), IFNA(VLOOKUP(A2, Overflow, 2, FALSE), "Unassigned"))
```

**Result:** The value from Overflow when Regions has no match and Overflow does, otherwise "Unassigned"

The inner IFNA runs only when the first lookup returns #N/A. Each lookup handles its own missing-key case, so a real error in either range still shows.

### Example 5: INDEX and MATCH

```excel
=IFNA(INDEX(C:C, MATCH(A2, B:B, 0)), "No Match")
```

**Result:** `No Match` when A2 is not in column B

MATCH returns #N/A, and INDEX passes that error along. IFNA replaces it at the end of the chain.

### Example 6: Testing for Existence

```excel
=IF(ISNA(VLOOKUP(A2, B:B, 1, FALSE)), "New", "Existing")
```

**Result:** `New` when A2 is not in column B

When the decision is which path to take rather than which value to show, test with ISNA inside IF. The result is a label, not a replacement value.

## Story Problems

### Problem 1: Regional Assignment

A sales team looks up the region for each account code. The region list in F1:G4 pairs each code with its region, and AC-31 is not on the list.

| Account |
| --- |
| AC-17 |
| AC-22 |
| AC-31 |
| AC-44 |

The region list in F1:G4 holds AC-17 with East, AC-22 with West, AC-44 with North, and AC-50 with South.

**Task:** Enter the formula in B2 of the account table, fill it down to B5, and show "Unassigned" for accounts not in the list.

**Solution:**

```excel
=IFNA(VLOOKUP(A2, $F$1:$G$4, 2, FALSE), "Unassigned")
```

**Answer:** `1` account is unassigned, AC-31. Its code is not in the list, so VLOOKUP returns #N/A and IFNA shows "Unassigned". The other three accounts show East, West, and North, in that order.

<!-- Image 3: Region Lookup Results. See Images/Logical/IFNA.md -->

### Problem 2: Delivery Surcharge

A courier charges a surcharge by delivery zone. The zone table in E1:F3 lists zone 2 at 4.50, zone 4 at 7.25, and zone 5 at 9.00. A zone that is not in the table should show a message instead of an error.

| Order | Zone |
| --- | --- |
| Order 1 | 2 |
| Order 2 | 9 |
| Order 3 | 4 |

**Task:** Enter the formula in C2 of the order table, fill it down to C4, and show the surcharge, or the text "No Zone Rate" when the zone is not listed.

**Solution:**

```excel
=IFNA(VLOOKUP(B2, $E$1:$F$3, 2, FALSE), "No Zone Rate")
```

**Answer:** Order 1 shows 4.50, Order 3 shows 7.25, and Order 2 shows "No Zone Rate" because zone 9 is missing from the table.

## Use Cases

### Multi-Source Lookups

**Scenario:** A finance analyst searches three regional tables in order and needs the first match, or a clear note that no region has the account.

```excel
=IFNA(VLOOKUP(AccountCode, Americas, 2, FALSE), IFNA(VLOOKUP(AccountCode, EMEA, 2, FALSE), "Not In Any Region"))
```

**Why It Works:** Each table is tried in turn, and an error in one table does not hide the next table's result. A broken range in any table still shows as an error.

### Shipping Surcharges

**Scenario:** A shipping rate sheet adds a surcharge only for zones on the list. Other zones should show a clear note for the sales team.

```excel
=IFNA(VLOOKUP(Zone, RateTable, 2, FALSE), "No Zone Rate")
```

**Why It Works:** The replacement appears only when the zone is missing. If RateTable is deleted, the #REF! error still appears, which prevents a silent wrong charge.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` shows instead of a replacement | A range reference is broken. | Repair the reference. IFNA correctly passes this error through. |
| `#N/A` still shows | The formula returns a different error, or the #N/A comes from a cell the formula does not wrap. | Wrap the innermost lookup, and check the error type with ERROR.TYPE. |
| Replacement never appears | The function returns 0, not #N/A, when nothing matches, such as SUMIF or COUNTIF. | Use IFNA only with lookups and MATCH. |
| Replacement appears for a deliberate NA() | NA() was used on purpose and IFNA caught it. | Test for the condition before the lookup instead of relying on IFNA. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2013 and later | Catches only #N/A. In Microsoft 365, it works element by element on arrays. |
| Google Sheets | Available | Replaces only #N/A. Other errors, such as #DIV/0!, are returned as they are. Empty arguments are treated as empty text. |

## Tips and Best Practices

- Use IFNA rather than IFERROR when a lookup is the only expected error.
- Return 0 when the result feeds a calculation, "" when it is display only, and a message when someone must act.
- Chain IFNA calls to try several sources in order, and keep the final fallback visible.
- Test three cases: a found key, a missing key, and a broken reference, so you confirm that real errors still show.
- Confirm that a function returns #N/A before wrapping it, because SUMIF and COUNTIF do not.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IFERROR](IFERROR.md) | Replaces every error type, so use it when any failure is acceptable. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns a value by position and passes along a MATCH #N/A. |
| [ISNA](../Information/ISNA.md) | Tests for #N/A so that IF can choose a different path. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Returns #N/A when the value is not found. |
| [NA](../Information/NA.md) | Creates an intentional #N/A, which IFNA also catches. |
| [VLOOKUP](../Lookup%20%26%20Reference/VLOOKUP.md) | The lookup most often protected by IFNA. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Has its own not-found argument, but IFNA can still wrap it. |

## Official Documentation

- [Microsoft Support: IFNA function](https://support.microsoft.com/en-us/excel/functions/ifna-function)
- [Google Docs Editors Help: IFNA](https://support.google.com/docs/answer/9365944)
