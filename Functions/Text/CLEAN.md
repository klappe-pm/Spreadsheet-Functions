---
domain: Spreadsheet Functions
category: Text
subcategory: Text Cleaning
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Imported Export Cleanup
  - Line Break Removal
  - Pasted Text Repair
related:
  - CHAR
  - CODE
  - REGEXREPLACE
  - SUBSTITUTE
  - TRIM
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/clean-function
  - https://support.google.com/docs/answer/3267340
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Remove Nonprintable Characters
tags:
  - data-cleaning
  - excel
  - sheets
  - text-cleaning
---

# CLEAN

## Description

**CLEAN** removes nonprintable characters from text. These are control characters that often arrive with data copied from web pages, exported from other systems or read from older files. They do not display, but they break lookups, sorting and exact matches, so a value that looks correct can fail to match.

In Excel, CLEAN removes the first 32 nonprinting 7-bit ASCII characters, which have codes 0 to 31. That range includes the tab (code 9) and the line feed (code 10). Excel does not remove the additional Unicode nonprinting characters with codes 127, 129, 141, 143, 144 and 157. Google Sheets also removes only the nonprintable ASCII characters and leaves other Unicode characters in place.

CLEAN removes characters without adding spaces. When a tab or line feed separated two words, the words join together after cleaning. Replace those characters with a space first, then clean, then trim the result.

<!-- Image 1: Hidden Characters in Imported Text. See Images/Text/CLEAN.md -->

## Syntax

```excel
=CLEAN(text)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that contains text, to clean. |

### Return Value

The same text with the nonprintable characters of codes 0 to 31 removed. Text without those characters is returned unchanged.

## Examples

### Example 1: Removing a Tab Between Words

```excel
=CLEAN("Sales" & CHAR(9) & "Total")
```

**Result:** `SalesTotal`

The tab disappears, so the two words join with no space. Use the fix in the Story Problems section when that matters.

### Example 2: Cleaning Then Trimming a Line Feed

```excel
=TRIM(CLEAN(A2))
```

Where `A2` contains `Row one` followed by a line feed and ` Row two`.

**Result:** `Row one Row two`

CLEAN removes the line feed, so the words meet at the space that was already in the text. TRIM then removes any extra spacing that remains at the ends.

### Example 3: Text Without Hidden Characters

```excel
=CLEAN(A3)
```

Where `A3` contains `Plain text`.

**Result:** `Plain text`

Clean text passes through unchanged, so CLEAN is safe to apply to a whole column.

<!-- Image 2: Text Before and After Cleaning. See Images/Text/CLEAN.md -->

## Story Problems

### Problem 1: Notes Pasted From a Web Page

A team pastes notes into `B2:B3`. Each note may contain a hidden tab.

| Part | Note |
| --- | --- |
| Gear | Checked, then a hidden tab and a space, then today |
| Belt | Pending |

**Task:** Return the note for `Gear` in column C with the hidden tab removed and no extra spacing.

**Solution:**

```excel
=TRIM(CLEAN(B2))
```

**Answer:** `Checked today`, because CLEAN removes the tab and TRIM reduces the spacing to one space.

### Problem 2: Product Code With a Trailing Line Feed

A supplier export stores the code `AX40` followed by a line feed in `A2`.

**Task:** Return a code that matches the master list, which holds `AX40`.

**Solution:**

```excel
=CLEAN(A2)
```

**Answer:** `AX40`, because the line feed is removed and the lookup can now match.

## Use Cases

### Cleaning Imported Vendor Files

**Scenario:** A monthly vendor file contains line feeds inside part descriptions, so lookups against the item master fail for those rows.

```excel
=TRIM(CLEAN(Imports!C2))
```

**Why It Works:** CLEAN removes the nonprintable characters first, and TRIM then removes extra spaces. Copy the result as values into a new column once it has been checked.

### Preparing Codes for Exact Lookups

**Scenario:** Identifiers copied from a PDF carry hidden characters, and the match against the master table must be exact.

```excel
=VLOOKUP(CLEAN(A2), Master!A:B, 2, FALSE)
```

**Why It Works:** Cleaning the lookup key removes the hidden characters, so the exact match succeeds. If some rows still fail, look for characters outside the 0 to 31 range.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Lookup still fails | Non-breaking spaces (CHAR(160)) or other Unicode characters remain. | Replace CHAR(160) with a space using SUBSTITUTE, then apply TRIM. |
| Words run together | A tab or line feed separated the words, and CLEAN removed it without adding a space. | Replace the tab or line feed with a space first, then apply CLEAN. |
| Characters still hidden | The character has a code outside 0 to 31, such as 127. | Remove the specific character with SUBSTITUTE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Removes codes 0 to 31. Codes 127, 129, 141, 143, 144 and 157 remain. |
| Google Sheets | Available | Removes nonprintable ASCII characters. Other Unicode characters stay in place. |

## Tips and Best Practices

- Replace tabs and line feeds with a space before cleaning when they separate words.
- Apply TRIM after CLEAN to remove the spaces that remain.
- Test on a sample before replacing a whole column.
- Keep the original column so you can compare the cleaned values.
- Use REGEXREPLACE when you need to remove a pattern that CLEAN does not cover.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHAR](CHAR.md) | Builds the characters that CLEAN removes, and creates replacements for them. |
| [CODE](CODE.md) | Returns the code of a suspicious first character so you can spot hidden characters. |
| [REGEXREPLACE](REGEXREPLACE.md) | Removes or replaces any pattern, including characters CLEAN leaves behind. |
| [SUBSTITUTE](SUBSTITUTE.md) | Replaces a specific character, such as a non-breaking space, with another one. |
| [TRIM](TRIM.md) | Removes the extra spaces that remain after cleaning. |

## Official Documentation

- [Microsoft Support: CLEAN function](https://support.microsoft.com/en-us/excel/functions/clean-function)
- [Google Docs Editors Help: CLEAN](https://support.google.com/docs/answer/3267340)
