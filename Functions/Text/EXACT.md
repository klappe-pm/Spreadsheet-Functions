---
domain: Spreadsheet Functions
category: Text
subcategory: Text Comparison
purpose:
  - Data Validation
  - Text Manipulation
use-case:
  - Import Cleanup
  - Password Change Checks
  - Product Code Matching
related:
  - CLEAN
  - FIND
  - LOWER
  - SEARCH
  - TRIM
  - UPPER
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/exact-function
  - https://support.google.com/docs/answer/3094073
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Case Sensitive Compare
  - Identical Text Check
tags:
  - case-sensitive
  - comparison
  - excel
  - sheets
  - text-matching
---

# EXACT

## Description

**EXACT** tests whether two text strings are identical and returns `TRUE` or `FALSE`. The comparison is case-sensitive, so `Word` and `word` do not match. Spaces and hidden characters also count, so `word` and `word ` (with a trailing space) do not match either.

Use EXACT when the difference between uppercase and lowercase letters or between visible and invisible characters matters. Passwords, case-sensitive codes and imported identifiers are typical examples. For an ordinary comparison that ignores case, use the equals operator (`=`) instead, because `=` treats `Word` and `word` as equal.

EXACT ignores formatting such as bold, italic or font color. It compares only the characters in each string. Both arguments are required.

## Syntax

```excel
=EXACT(text1, text2)
```

<!-- Image 1: EXACT Arguments and Result. See Images/Text/EXACT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text1` | Yes | The first string to compare. It can be a literal in quotes, a cell reference or a formula that returns text. In Google Sheets this argument is named `string1`. |
| `text2` | Yes | The second string to compare. It follows the same rules as `text1`. In Google Sheets this argument is named `string2`. |

### Return Value

`TRUE` when the two strings contain exactly the same characters in the same case, and `FALSE` otherwise. The function does not return an error for mismatched text.

## Examples

### Example 1: Identical Strings

```excel
=EXACT("word", "word")
```

**Result:** `TRUE`

Both strings have the same characters in the same case.

### Example 2: Different Case

```excel
=EXACT("Word", "word")
```

**Result:** `FALSE`

The first letter is uppercase in one string and lowercase in the other. The `=` operator would return `TRUE` for this pair.

### Example 3: Password Comparison

```excel
=EXACT(A2, B2)
```

Where A2 contains `Summer2026` and B2 contains `summer2026`

**Result:** `FALSE`

The two passwords differ only in the first letter, so they do not match.

### Example 4: Ignoring Stray Spaces Before Comparing

```excel
=EXACT(TRIM(A3), B3)
```

Where A3 contains `AB-100 ` (with a trailing space) and B3 contains `AB-100`

**Result:** `TRUE`

TRIM removes the trailing space from A3 before the comparison. Use TRIM only when extra spaces are not meaningful in your data.

### Example 5: Labeling the Result

```excel
=IF(EXACT(A4, B4), "Match", "Mismatch")
```

Where A4 contains `w ord` and B4 contains `word`

**Result:** `"Mismatch"`

Wrapping EXACT in IF turns the logical result into a readable label. The space inside `w ord` makes the strings different.

## Story Problems

### Problem 1: Changing a Password

A help desk compares the old password saved in A2 with a new entry in B2 to confirm that the user did not reuse the same text with only a change in case.

| Field | Value |
| --- | --- |
| Old password (A2) | Summer2026 |
| New entry (B2) | summer2026 |

**Task:** Write a formula in C2 that returns `TRUE` only when the two entries are identical.

**Solution:**

```excel
=EXACT(A2, B2)
```

**Answer:** `FALSE`. The letter S differs in case, so EXACT reports a mismatch even though `=` would call them equal.

### Problem 2: Counting Exact SKU Matches

A warehouse compares two SKU lists in A2:A6 and B2:B6, which should be identical row for row. Some values differ in case or contain a trailing space.

| Row | List A | List B |
| --- | --- | --- |
| 1 | Blue Fox | Blue Fox |
| 2 | Red Hen | red hen |
| 3 | Green Owl | Green Owl |
| 4 | Gray Cat | Gray Cat (trailing space) |
| 5 | Gold Ram | Gold Ram |

**Task:** Count how many rows match exactly.

**Solution:**

```excel
=SUMPRODUCT(--EXACT(A2:A6, B2:B6))
```

**Answer:** `3`. Rows 1, 3 and 5 match. Row 2 differs in case, and row 4 differs by a trailing space.

<!-- Image 2: Case and Space Differences in Matching Rows. See Images/Text/EXACT.md -->

## Use Cases

### Product Code Matching

**Scenario:** A supplier uses codes such as `AB-100` and `ab-100` for different variants. The purchasing team needs to flag rows where the case of a code differs from the master list.

```excel
=IF(EXACT(B2, INDEX(Master[Code], MATCH(B2, Master[Code], 0))), "Same", "Case Differs")
```

**Why It Works:** EXACT separates the two variants that the equals operator would treat as the same code. Use the result to decide which record needs review.

### Import Cleanup Check

**Scenario:** After a data import, a team needs to find customer names that contain leading or trailing spaces.

```excel
=IF(EXACT(A2, TRIM(A2)), "Clean", "Extra Spaces")
```

**Why It Works:** TRIM returns the name without extra spaces. When the cleaned copy is not identical to the original, EXACT flags the cell so the spaces can be removed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for values that look the same | Different case, extra spaces or invisible characters. | Compare LEN values, then clean the source with TRIM and CLEAN. |
| Case-sensitive check on a range fails | EXACT compares two values at a time and does not search a range. | Compare row by row, or use SUMPRODUCT with EXACT across two ranges. |
| Case-insensitive match needed | EXACT is case-sensitive by design. | Use `=` or compare with LOWER on both sides. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions. | Case-sensitive, and spaces and hidden characters count. |
| Google Sheets | Available. | Same results. Case and whitespace must be identical for a `TRUE` result. |

## Tips and Best Practices

- Use the equals operator for everyday comparisons and EXACT only when case or spacing matters.
- Compare with `LEN` first when a mismatch is unexpected, because a different length points to hidden characters.
- Combine EXACT with TRIM or CLEAN only after confirming that the extra characters are unwanted.
- Use `SUMPRODUCT(--EXACT(range1, range2))` to count exact matches across two columns.
- Apply EXACT in a helper column so that the results are easy to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LOWER](LOWER.md) | Converts text to lowercase so that a case-insensitive comparison can be made with EXACT. |
| [UPPER](UPPER.md) | Converts text to uppercase, which can normalize codes before comparison. |
| [TRIM](TRIM.md) | Removes extra spaces before a comparison. |
| [CLEAN](CLEAN.md) | Removes nonprinting characters before a comparison. |
| [FIND](FIND.md) | Locates text inside a string, case-sensitively, but does not test for an identical match. |
| [SEARCH](SEARCH.md) | Locates text inside a string without regard to case. |

## Official Documentation

- [Microsoft Support: EXACT function](https://support.microsoft.com/en-us/excel/functions/exact-function)
- [Google Docs Editors Help: EXACT](https://support.google.com/docs/answer/3094073)
