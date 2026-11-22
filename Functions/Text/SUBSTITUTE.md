---
domain: Spreadsheet Functions
category: Text
subcategory: Text Cleaning
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Account Code Cleanup
  - Quarter Label Updates
  - Report Title Corrections
related:
  - CLEAN
  - REGEXREPLACE
  - REPLACE
  - TRIM
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/substitute-function
  - https://support.google.com/docs/answer/3094215
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Replace Text
  - Substitute Text
tags:
  - excel
  - sheets
  - text-cleaning
  - text-replacement
---

# SUBSTITUTE

## Description

**SUBSTITUTE** replaces existing text with new text wherever the old text appears in a string. Use it to correct a word everywhere it occurs, remove a symbol such as a hyphen or a comma, or change a label that appears several times in one cell. Unlike [REPLACE](REPLACE.md), which replaces characters at a fixed position, SUBSTITUTE finds the text you name.

By default, every occurrence of the old text is replaced. The optional last argument limits the change to one occurrence, counted from the left. The match also applies to partial words, so a search for `vent` changes the middle of the word `eventual`. Use a word boundary or a delimiter in the search text when a partial match is not wanted.

The result is always text. Wrap the formula in VALUE when a number is needed, and use TRIM when extra spaces are left behind after a substitution.

SUBSTITUTE works the same way in Microsoft Excel and Google Sheets, with the same argument order.

## Syntax

```excel
=SUBSTITUTE(text, old_text, new_text, [instance_num])
```

<!-- Image 1: Old Text and New Text Anatomy. See Images/Text/SUBSTITUTE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that holds the text, in which to substitute characters. |
| `old_text` | Yes | The text to find and replace. It must match the source text exactly. |
| `new_text` | Yes | The text that replaces each match of `old_text`. It can be empty. |
| `instance_num` | No | The occurrence of `old_text` to replace, counted from the left. When it is omitted, every occurrence is replaced. |

### Return Value

Text. The original text with the selected occurrences of `old_text` replaced by `new_text`.

## Examples

### Example 1: Replace Every Occurrence

```excel
=SUBSTITUTE("Q1 sales, Q1 returns", "Q1", "Q2")
```

**Result:** `Q2 sales, Q2 returns`

Both occurrences of `Q1` are replaced because `instance_num` is omitted.

### Example 2: Replace Only the Second Occurrence

```excel
=SUBSTITUTE("Q1 sales, Q1 returns", "Q1", "Q2", 2)
```

**Result:** `Q1 sales, Q2 returns`

The second occurrence is the only one that changes. The first `Q1` stays as it was.

### Example 3: Remove a Hyphen From a Date Code

```excel
=SUBSTITUTE("2025-0419", "-", "")
```

**Result:** `20250419`

Replacing the hyphen with an empty string removes it. The result is still text, so VALUE converts it to a number when the code must be used in a calculation.

### Example 4: Partial Words Also Match

```excel
=SUBSTITUTE("eventual plan", "vent", "")
```

**Result:** `eual plan`

The search matches the letters `vent` inside the word `eventual`, which shows why the search text should be chosen carefully.

### Example 5: Collapse Double Spaces

```excel
=SUBSTITUTE("Acme  Corp", "  ", " ")
```

**Result:** `Acme Corp`

The two spaces in the source are replaced by one space. Repeat the formula, or wrap it with TRIM, when more than two spaces appear.

<!-- Image 2: Occurrence Selection Example. See Images/Text/SUBSTITUTE.md -->

## Story Problems

### Problem 1: Clean Invoice Date Codes

A finance team receives invoice date codes with hyphens, and the payment system needs them without any separators. The first code is `2025-0419`.

| Date Code |
| --- |
| 2025-0419 |
| 2025-1102 |

**Task:** Remove the hyphen from the first code and state the result.

**Solution:**

```excel
=SUBSTITUTE(A2, "-", "")
```

**Answer:** `20250419`. Every hyphen is removed, and the result is text that can be converted with VALUE if needed.

### Problem 2: Relabel the Second Quarter Reference

A quarterly report mentions the quarter twice in one cell, and only the second mention refers to the period being reported. The team wants to change only that mention from `Q1` to `Q2`.

| Report Note |
| --- |
| Q1 sales, Q1 returns |

**Task:** Replace only the second `Q1` with `Q2`, and state the result.

**Solution:**

```excel
=SUBSTITUTE(A2, "Q1", "Q2", 2)
```

**Answer:** `Q1 sales, Q2 returns`. The first mention is left as it was, and the second is replaced.

<!-- Image 3: Single Occurrence Replacement Result. See Images/Text/SUBSTITUTE.md -->

## Use Cases

### Account Code Cleanup

**Scenario:** Account codes exported from an old system contain spaces and hyphens, and the new system accepts only letters and digits.

```excel
=SUBSTITUTE(SUBSTITUTE(A2, " ", ""), "-", "")
```

**Why It Works:** The inner formula removes spaces and the outer formula removes hyphens. Nesting SUBSTITUTE is clear when only a few symbols must go.

### Quarter Label Updates

**Scenario:** A template contains the label `FY26 Q1` in many cells, and the team must roll it forward to `FY26 Q2` for the next report.

```excel
=SUBSTITUTE(A2, "Q1", "Q2")
```

**Why It Works:** Every occurrence in the cell changes at once, so titles that mention the quarter more than once stay consistent.

### Report Title Corrections

**Scenario:** A list of client report titles uses the old company name, and the new name must be applied without changing the rest of the title.

```excel
=SUBSTITUTE(A2, "Old Name Ltd", "New Name Ltd")
```

**Why It Works:** The search text names the old company, so only that name changes. Check that the old name does not appear as part of a longer name before you fill the formula down.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| No change | The old text does not match the source text exactly. | Check the spelling and spacing of the search text, or convert the source with LOWER or UPPER first. |
| Unexpected change inside a word | The old text is also part of a longer word. | Use a longer search string that includes spaces or punctuation. |
| Number result is text | SUBSTITUTE always returns text. | Wrap the formula in VALUE when the result feeds a calculation. |
| Extra spaces remain | The replacement left double spaces behind. | Wrap the formula in TRIM. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Same four arguments. The optional argument is `instance_num`. |
| Google Sheets | Available | Same argument order. The optional argument is `occurrence_number`. Omitting it replaces every occurrence. |

## Tips and Best Practices

- Use SUBSTITUTE for text you can name, and REPLACE for characters at a known position.
- Nest SUBSTITUTE only for a few symbols, and use REGEXREPLACE when many patterns must change.
- Test the search text on a few rows that contain partial matches.
- Use the occurrence argument when a label appears more than once and only one change is wanted.
- Apply TRIM after a substitution that removes words, so no extra spaces remain.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REPLACE](REPLACE.md) | Replaces characters at a fixed position rather than matching text. |
| [REGEXREPLACE](REGEXREPLACE.md) | Replaces text that matches a pattern, for more complex cleanup. |
| [TRIM](TRIM.md) | Removes extra spaces left behind after a substitution. |
| [CLEAN](CLEAN.md) | Removes non-printing characters that SUBSTITUTE cannot match by name. |
| [VALUE](VALUE.md) | Converts the text result to a number when it is used in a calculation. |

## Official Documentation

- [Microsoft Support: SUBSTITUTE function](https://support.microsoft.com/en-us/excel/functions/substitute-function)
- [Google Docs Editors Help: SUBSTITUTE](https://support.google.com/docs/answer/3094215)
