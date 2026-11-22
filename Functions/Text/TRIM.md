---
domain: Spreadsheet Functions
category: Text
subcategory: Text Cleaning
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Customer Name Cleanup
  - Form Input Cleanup
  - Lookup Key Cleanup
related:
  - CLEAN
  - LEN
  - PROPER
  - SUBSTITUTE
  - VALUE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/trim-function
  - https://support.google.com/docs/answer/3094140
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Clean Whitespace
  - Remove Spaces
  - Strip Spaces
  - Trim Spaces
tags:
  - data-cleaning
  - excel
  - normalization
  - sheets
  - whitespace
---

# TRIM

## Description

**TRIM** removes the spaces at the start and end of a text string, and reduces each run of repeated spaces between words to a single space. Text pasted from another system often looks correct but fails a comparison, a lookup or a count because of stray spaces. TRIM is the usual first step in repairing that kind of data.

TRIM removes only the ordinary space character. It does not remove non-breaking spaces (often found in web content), tabs, or line breaks. For those, first replace the non-breaking space with SUBSTITUTE, and remove non-printing characters with CLEAN, then apply TRIM. Text that is already clean passes through unchanged, so TRIM is safe to apply to any input.

The result is always text. A number that has been trimmed becomes text, so convert it with VALUE before using it in calculations.

## Syntax

```excel
=TRIM(text)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TRIM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to clean. It can be a text string in double quotes, a cell reference or a formula that returns text. |

### Return Value

Text: the string with leading and trailing spaces removed and internal runs of spaces reduced to one. An input that contains only spaces returns an empty string.

## Examples

### Example 1: Remove Leading, Trailing and Repeated Spaces

```excel
=TRIM("  Quarterly   sales  ")
```

**Result:** `Quarterly sales`

The two leading spaces, the two trailing spaces and the three spaces between the words are all reduced.

### Example 2: Clean a Cell Reference

```excel
=TRIM(A2)
```

**Result:** `Pine Street`

With `A2` holding `  Pine  Street `, TRIM returns the cleaned text and leaves `A2` unchanged.

### Example 3: Count the Extra Spaces

```excel
=LEN(A2)-LEN(TRIM(A2))
```

**Result:** `4`

`A2` has 15 characters. After TRIM it has 11, so four characters were removed. A result of 0 means the cell has no extra spaces.

### Example 4: Replace Non-Breaking Spaces First

```excel
=TRIM(SUBSTITUTE(A3,CHAR(160)," "))
```

**Result:** `Lee Park`

When `A3` holds Lee, a non-breaking space and Park, SUBSTITUTE turns the non-breaking space into an ordinary space before TRIM runs. TRIM alone would leave the text unchanged.

### Example 5: Compare Two Values After Cleaning

```excel
=TRIM(A4)=TRIM(B4)
```

**Result:** `TRUE`

With `A4` holding `Ms. Lee ` and `B4` holding ` Ms. Lee`, the spacing is different but the cleaned values match.

### Example 6: Look Up a Value With Stray Spaces

```excel
=VLOOKUP(TRIM(D2),A2:B4,2,FALSE)
```

**Result:** `19.5`

With `D2` holding ` MS-11 ` and a price table in `A2:B4`, the lookup key matches the table entry `MS-11` once the spaces are removed. Without TRIM, the same lookup returns `#N/A`.

<!-- Image 2: Before and After Cleaning. See Images/Text/TRIM.md -->

## Story Problems

### Problem 1: Count the Names That Need Cleaning

A mailing list export has five names in `A2:A6`. Some have leading, trailing or doubled spaces, and one is already clean.

| Name |
| --- |
| `  Ana Ruiz` |
| `Ben  Clark ` |
| ` Cy Lo` |
| `Dee Park` |
| `Eli  Stone ` |

**Task:** Count how many names change when they are trimmed.

**Solution:**

```excel
=SUMPRODUCT(--(LEN(A2:A6)<>LEN(TRIM(A2:A6))))
```

**Answer:** `4`. Ana Ruiz, Ben Clark, Cy Lo and Eli Stone each lose at least one space. Dee Park has a single space between the words and is unchanged.

### Problem 2: Find a Price Despite Stray Spaces

A price table holds codes in `A2:A4`, with prices in `B2:B4`: KB-20 at 45, MS-11 at 19.5 and HD-07 at 129. A sales rep types ` MS-11 ` into `D2`, with a space on each side.

**Task:** Return the price for the code in `D2`.

**Solution:**

```excel
=VLOOKUP(TRIM(D2),A2:B4,2,FALSE)
```

**Answer:** `19.5`. TRIM removes the stray spaces, so the exact match finds the MS-11 row.

## Use Cases

### Customer Name Cleanup

**Scenario:** Customer names imported from a legacy system have stray spaces and inconsistent capitalization, and the mailing labels need a clean, consistent form.

```excel
=PROPER(TRIM(A2))
```

**Why It Works:** TRIM removes the extra spaces first, so PROPER capitalizes each word of the cleaned name. Apply the formula in a helper column, then copy the results as values back into the source.

### Form Input Cleanup

**Scenario:** A sign-up form accepts email addresses, and users sometimes type a space or a capital letter at the start.

```excel
=TRIM(LOWER(A2))
```

**Why It Works:** Email addresses are not case-sensitive in practice, so lowercasing and trimming produce one standard form for comparison and matching.

### Lookup Key Cleanup

**Scenario:** A duplicate check compares customer records by name and city, and spacing differences create false mismatches.

```excel
=TRIM(LOWER(A2))&"|"&TRIM(LOWER(B2))
```

**Why It Works:** Each field is cleaned before it is joined with a separator, so the key is the same for rows that differ only in spacing or capitalization.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Spaces remain | Non-breaking spaces (character 160) are not removed by TRIM. | Replace them with SUBSTITUTE, such as `=TRIM(SUBSTITUTE(A2,CHAR(160)," "))`. |
| Line breaks or tabs remain | TRIM removes only the space character. | Use `=TRIM(CLEAN(A2))` to remove non-printing characters too. |
| Number is treated as text | TRIM returns text, even for a number. | Convert the result with VALUE, such as `=VALUE(TRIM(A2))`. |
| Lookup still fails | The table column itself has stray characters. | Clean the table column with the same formula, and paste the results as values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Removes ordinary spaces only. Non-breaking spaces, tabs and line breaks remain. |
| Google Sheets | Available | Same behavior: removes leading, trailing and repeated spaces, and leaves non-breaking spaces in place. Works with ARRAYFORMULA on ranges. |

## Tips and Best Practices

- Apply TRIM to both sides of a comparison, such as `TRIM(A1)=TRIM(B1)`, so spacing cannot cause a false mismatch.
- Trim lookup keys before a VLOOKUP or INDEX and MATCH, because a single stray space causes a miss.
- Count the spaces with `LEN(A1)-LEN(TRIM(A1))` to audit a column before cleaning it.
- Use the full cleaning chain, `TRIM(CLEAN(SUBSTITUTE(A1,CHAR(160)," ")))`, for text copied from web pages.
- Convert trimmed numbers with VALUE before adding them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CLEAN](../Text/CLEAN.md) | Removes non-printing characters that TRIM leaves in place. |
| [LEN](../Text/LEN.md) | Counts characters, so the difference before and after TRIM shows how many spaces were removed. |
| [PROPER](../Text/PROPER.md) | Capitalizes each word, often applied after TRIM. |
| [SUBSTITUTE](../Text/SUBSTITUTE.md) | Replaces a character such as the non-breaking space before TRIM runs. |
| [VALUE](../Text/VALUE.md) | Converts a trimmed number stored as text back into a number. |

## Official Documentation

- [Microsoft Support: TRIM function](https://support.microsoft.com/en-us/excel/functions/trim-function)
- [Google Docs Editors Help: TRIM](https://support.google.com/docs/answer/3094140)
