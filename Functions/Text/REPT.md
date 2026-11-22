---
domain: Spreadsheet Functions
category: Text
subcategory: Text Construction
purpose:
  - Text Manipulation
use-case:
  - Bar Charts in Cells
  - Report Divider Lines
  - Visual Score Markers
related:
  - CONCAT
  - JOIN
  - LEN
  - REPLACE
  - TEXT
  - TRIM
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/rept-function
  - https://support.google.com/docs/answer/3094134
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Repeat Text
tags:
  - excel
  - repetition
  - sheets
  - text-generation
---

# REPT

## Description

**REPT** repeats a piece of text a number of times and returns the combined result. It is most often used to build simple visual indicators inside a cell, such as a bar of symbols that grows with a value, a divider line for a printed report, or a row of markers that shows a score.

REPT adds nothing between the repeats. If you want a space between each copy, include the space in the text you repeat, then remove the trailing space with TRIM. The function accepts a single character or a longer string, and the result can be used in any text formula, for example with CONCAT or the `&` operator.

The number of repeats is taken as a whole number. Decimal values are cut down to their integer part, and a value of zero returns empty text. The result cannot exceed 32,767 characters in Excel, and the Google Sheets page gives a limit of 32,000 characters. A longer result returns `#VALUE!`.

REPT is available in Microsoft Excel and Google Sheets with the same two arguments.

## Syntax

```excel
=REPT(text, number_times)
```

<!-- Image 1: Repeat Count Anatomy. See Images/Text/REPT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The character or string to repeat. A cell reference or a formula that returns text is also allowed. |
| `number_times` | Yes | The number of times to repeat `text`. Decimal values are truncated, so 2.9 repeats twice. |

### Return Value

Text containing `text` repeated `number_times` times, or empty text when `number_times` is zero. A result longer than the limit returns `#VALUE!`.

## Examples

### Example 1: Build a Simple Divider

```excel
=REPT("*", 5)
```

**Result:** `*****`

The character `*` is repeated five times with nothing between the copies. Use this for a quick visual separator in a header cell.

### Example 2: Fixed-Length Divider

```excel
=REPT("=", 20)
```

**Result:** `====================`

The result is 20 equal signs. LEN confirms the length if you need to check it: `=LEN(REPT("=", 20))` returns `20`.

### Example 3: Bar Length Driven by a Value

```excel
=REPT("|", B2)
```

**Result:** `|||||||` when B2 contains `7`

The number in B2 sets the length of the bar. Filling the formula down gives each row a bar that matches its count.

### Example 4: Repeat a Word With Spaces

```excel
=TRIM(REPT("ha ", 3))
```

**Result:** `ha ha ha`

The space is part of the repeated text, so the result has three copies separated by spaces. TRIM removes the trailing space that the last copy leaves behind.

### Example 5: Decimal Count Is Truncated

```excel
=REPT("ab", 2.9)
```

**Result:** `abab`

The count 2.9 is cut down to 2, so the text is repeated twice rather than rounded to three times.

<!-- Image 2: Text Bar Chart Result. See Images/Text/REPT.md -->

## Story Problems

### Problem 1: Draw Sales Bars for a Regional Report

A regional manager wants a quick text bar chart in a report. Each `#` stands for one unit sold. The units are listed in column B, and column C should show the bars.

| Region | Units Sold |
| --- | --- |
| North | 7 |
| South | 4 |
| East | 0 |
| West | 12 |

**Task:** Build the bar for each region, then give the number of `#` characters in the West bar.

**Solution:**

```excel
=REPT("#", B2)
```

**Answer:** The North bar has 7 characters, South has 4, East is empty because the count is zero, and West has 12. The West bar holds `12` characters.

### Problem 2: Create a Separator Line for Each Section

A report template needs a line of 30 dashes under each section title. The title sits in A2, and the dash line goes in A3.

| Section Title |
| --- |
| Quarterly Summary |

**Task:** Write the formula for the dash line and state its length.

**Solution:**

```excel
=REPT("-", 30)
```

**Answer:** The formula returns 30 dash characters. `=LEN(A3)` on that cell returns `30`.

<!-- Image 3: Score Marker Layout. See Images/Text/REPT.md -->

## Use Cases

### Bar Charts in Cells

**Scenario:** A dashboard shows survey scores from 1 to 10 next to each team name, and a bar makes the spread easy to read at a glance.

```excel
=REPT("█", B2)
```

**Why It Works:** The bar grows with the score, so a glance shows which teams lead. Add a number in the next column so readers can see the exact value.

### Report Divider Lines

**Scenario:** A monthly report is printed from a sheet, and each section needs a line that matches its title width.

```excel
=REPT("_", LEN(A2))
```

**Why It Works:** LEN sets the repeat count from the title length, so the line always matches the title.

### Visual Score Markers

**Scenario:** A quality review uses a row of markers to show how many checks a supplier passed out of five.

```excel
=REPT("*", B2) & REPT("-", 5 - B2)
```

**Why It Works:** The first REPT draws the passed checks and the second draws the rest, so the full marker always has five positions.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The result would be longer than the platform limit. | Reduce the count, or split the output across cells. |
| Empty cell | `number_times` is zero or the source cell is blank. | Check the source value, or use IF to show a placeholder. |
| Bar shorter than expected | `number_times` holds a decimal, which is truncated. | Round the value with ROUND or INT before passing it to REPT. |
| Uneven spacing | The repeated text has no space between copies. | Include the space inside the text and remove the trailing space with TRIM. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The Microsoft page lists a 32,767 character result limit. Other arguments behave as described above. |
| Google Sheets | Available | The Google page lists a 32,000 character result limit. The page does not say how negative counts are handled. |

## Tips and Best Practices

- Keep the repeat count in its own column so the bars can be recalculated when the data changes.
- Use CONCAT or the `&` operator to add a label next to the bar.
- Check the length of very long results before you fill them down a column.
- Round decimal counts first when the bar must match a whole number.
- Use a symbol font that renders well in both print and screen views.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](CONCAT.md) | Joins the repeated text with a label or another value. |
| [JOIN](JOIN.md) | Joins a list of values with a separator, useful when the repeated pieces differ. |
| [LEN](LEN.md) | Measures text length, often used to set the repeat count. |
| [REPLACE](REPLACE.md) | Changes part of a text value after it is built. |
| [TEXT](TEXT.md) | Formats a number before it is used as text in a label. |
| [TRIM](TRIM.md) | Removes the trailing space left after a repeated word or symbol. |

## Official Documentation

- [Microsoft Support: REPT function](https://support.microsoft.com/en-us/excel/functions/rept-function)
- [Google Docs Editors Help: REPT](https://support.google.com/docs/answer/3094134)
