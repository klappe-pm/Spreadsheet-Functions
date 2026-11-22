---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Furigana Reading Lists
  - Japanese Name Sorting
related:
  - ASC
  - JIS
  - LENB
  - MIDB
  - UNICODE
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/phonetic-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Furigana Extraction
  - Phonetic Guide Text
tags:
  - excel
  - furigana
  - japanese
  - text
---

# PHONETIC

## Description

**PHONETIC** returns the furigana (the phonetic guide) stored with text in a cell. Furigana is the small kana reading that Japanese text can carry above or beside its kanji. Excel stores it when a user types the text with the Phonetic Guide, and PHONETIC returns that stored reading as text instead of the kanji itself.

Use PHONETIC when a Japanese name list or product list holds readings that must be sorted, filtered or exported. Sorting by the reading gives the order that a Japanese reader expects, which is often different from the order of the kanji.

PHONETIC needs a Far East language setting, such as Japanese, Chinese or Korean, to work as documented. It reads only furigana that already exists in the cell, so it cannot create a reading for text that has none. Google Sheets does not include an equivalent function, so readings that must be kept in a Sheets file belong in a separate column.

## Syntax

```excel
=PHONETIC(reference)
```

<!-- Image 1: PHONETIC Reference Argument. See Images/Text/PHONETIC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | Yes | A text string, or a reference to a single cell or a range of cells that contains furigana. For a range of adjacent cells, the furigana from the upper-left cell is returned. A range of nonadjacent cells returns `#N/A`. |

### Return Value

The furigana stored in the referenced cell, as text. The function returns the reading, not the characters of the text itself. When a range is referenced, it returns the reading from the upper-left cell. A reference to nonadjacent cells returns `#N/A`.

## Examples

### Example 1: Reading a Single Name

Cell `A2` contains the kanji for a Tokyo ward name, and the cell has a furigana reading typed with the Phonetic Guide.

```excel
=PHONETIC(A2)
```

**Result:** The kana reading stored in cell `A2`, shown in the form typed in the Phonetic Guide. The formula does not return the kanji.

<!-- Image 2: Phonetic Guide Stored in a Cell. See Images/Text/PHONETIC.md -->

### Example 2: Reading From the Upper-Left Cell of a Range

Cells `A2:A4` each contain a name with a stored reading.

```excel
=PHONETIC(A2:A4)
```

**Result:** The reading stored in `A2` only. The readings in `A3` and `A4` are not returned by this formula.

### Example 3: Nonadjacent Cells Return an Error

Cells `A2` and `A4` each contain a name with a stored reading, and `A3` is between them.

```excel
=PHONETIC((A2,A4))
```

**Result:** `#N/A`

The reference covers two cells that are not next to each other, which PHONETIC does not accept.

### Example 4: Copying Readings Down a List

Cells `A2:A10` each hold a name with a stored reading. The formula fills column B.

```excel
=PHONETIC(A2)
```

Copy the formula from `B2` down to `B10`.

**Result:** Each row in column B shows the reading of the name in the same row of column A.

## Story Problems

### Problem 1: Sorting a Name List by Reading

A school office keeps a list of student names with readings typed in the Phonetic Guide. The attendance report must list the students in reading order.

| Student Name |
| --- |
| 田中 花子 |
| 佐藤 健 |
| 鈴木 一郎 |

**Task:** Put each student's reading in column B, then sort the list by that column.

**Solution:**

```excel
=PHONETIC(A2)
```

Copy the formula down column B, then sort the rows by column B.

**Answer:** Each row in column B shows the stored reading for its name, and sorting by column B puts the students in reading order. The exact readings depend on the text typed in the Phonetic Guide, and the readings must be checked by a person who reads Japanese before the list is published.

### Problem 2: Fixing a #N/A Result

An analyst selects cells `A2` and `A4` with the mouse and enters a formula that refers to both cells at once. The formula returns `#N/A`.

**Task:** Explain the error and give a corrected approach.

**Solution:**

```excel
=PHONETIC(A2)
```

Enter the formula once for each cell, in separate cells.

**Answer:** The error occurs because the two cells are not adjacent. One formula per cell avoids the error, and each formula returns the reading of its own cell.

## Use Cases

### Furigana Reading Lists

**Scenario:** A publisher prepares a glossary in which each term needs its reading shown beside it.

```excel
=PHONETIC(A2)
```

**Why It Works:** The reading is taken straight from the cell, so the glossary stays in sync when a reading is corrected in the source column.

### Japanese Name Sorting

**Scenario:** A membership list must be sorted in the reading order used by Japanese records.

```excel
=PHONETIC(B2)
```

**Why It Works:** Sorting by the reading column follows the order of the kana rather than the order of the kanji, which is what the office expects.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The reference covers nonadjacent cells. | Use one formula per cell, or a single contiguous range. |
| Empty or unexpected result | The cell has no stored furigana. | Add the reading with the Phonetic Guide, or type it in a separate column. |
| Result is the kanji, not the reading | The text was not typed with the Phonetic Guide. | Set the reading in the Phonetic Guide and check the result again. |
| Function does not respond as documented | The Far East language setting is not enabled. | Enable a Japanese, Chinese or Korean language in the operating system settings. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available with a Far East language setting | The function returns furigana stored with the text. The Microsoft page does not describe how blank cells or non-text values are handled. |
| Google Sheets | Not available | No furigana function exists. Keep readings in a separate column, typed or imported. |

## Tips and Best Practices

- Keep the readings in a separate column when a file must work in both Excel and Sheets.
- Check the stored readings with a person who reads Japanese before you sort or publish a list.
- Use one formula per cell when the readings come from scattered cells.
- Use ASC or JIS to convert half-width and full-width characters when you prepare a list for matching.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASC](ASC.md) | Converts full-width letters to half-width, a text preparation step. |
| [JIS](JIS.md) | Converts half-width letters to full-width, the reverse of ASC. |
| [LENB](LENB.md) | Measures text in bytes for double-byte fields. |
| [MIDB](MIDB.md) | Extracts a byte count from double-byte text. |
| [UNICODE](UNICODE.md) | Returns the code point of the first character, useful for checking characters. |

## Official Documentation

- [Microsoft Support: PHONETIC function](https://support.microsoft.com/en-us/excel/functions/phonetic-function)
