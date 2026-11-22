---
domain: Spreadsheet Functions
category: Text
subcategory: Text Generation
purpose:
  - AI Assistance
use-case:
  - Customer Feedback Summaries
  - Survey Comment Coding
  - Workbook Migration Audits
related:
  - AI
  - COUNTIF
  - IFERROR
  - ISERROR
  - SEARCH
level: 4
source:
  - https://support.microsoft.com/en-us/excel/copilot-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Copilot Function
  - Excel Copilot Formula
tags:
  - copilot
  - excel
  - preview
  - retired
---

# COPILOT

## Description

**COPILOT** sent a prompt to Microsoft Copilot and placed the generated result in the cell that held the formula. You could add a cell or range as context, so one formula could summarize, label or rewrite the text in those cells. Microsoft released it as a preview for members of the Microsoft 365 Insider and Frontier programs in August 2025.

The function is retired. Starting September 14, 2026, Microsoft no longer makes COPILOT available. Cells that already held a result keep the cached value until they recalculate. After that, they return `#NAME?`, so any workbook that still contains COPILOT formulas shows errors on its next recalculation.

Use this page to recognize retired formulas in older workbooks and to choose a replacement. For one-off text work, open the Copilot pane in Excel from the Copilot icon in the lower-right corner of the window and paste the result as plain text. For a rule you can write down, such as flagging a keyword, use a standard formula like COUNTIF, SEARCH or IFERROR so the result keeps working. Google Sheets never offered COPILOT; its closest equivalent is the AI function.

## Syntax

```excel
=COPILOT(prompt, [context])
```

<!-- Image 1: Retired Formula Warning. See Images/Text/COPILOT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `prompt` | Yes | The instruction to Copilot, in quotes or as a cell reference, such as `"Summarize these comments in one sentence"`. |
| `context` | No | A cell or range that Copilot reads together with the prompt. Omit it when the prompt needs no cell data. |

### Return Value

The generated text for the prompt. Before the retirement, a cell kept the last result it received. From September 14, 2026, recalculating a COPILOT cell returns `#NAME?`.

## Examples

Each example shows the original formula so you can recognize it in an older workbook. The stated result applies to recalculation on or after September 14, 2026.

### Example 1: Summarize a Range of Comments

```excel
=COPILOT("Summarize these comments in one sentence", B2:B50)
```

**Result:** `#NAME?`

Before the retirement, this cell showed a one-sentence summary of `B2:B50`. Excel keeps that text until the cell recalculates.

### Example 2: Ask for Text Without Cell Data

```excel
=COPILOT("Name one keyboard shortcut for copying a cell")
```

**Result:** `#NAME?`

A prompt that needs no cell data can leave out the context argument.

### Example 3: Wrap the Formula in IFERROR

```excel
=IFERROR(COPILOT("Label this comment as positive or negative", C2), "Review manually")
```

**Result:** `Review manually`

IFERROR catches the `#NAME?` error and shows a fallback message, so the sheet stays readable while you rebuild the cell.

<!-- Image 2: Find Retired Formulas. See Images/Text/COPILOT.md -->

### Example 4: Replace a Label With COUNTIF

```excel
=COUNTIF(B2:B6, "*late*")
```

**Result:** `3`

The formula counts comments that contain the word late, using the sample comments in Problem 1. COUNTIF ignores case, so "Late" and "late" both match.

## Story Problems

### Problem 1: Counting Late Deliveries

A support team pasted ticket comments into `A1:B6` and used COPILOT to tag the comments about late orders. The tagging formulas no longer work, so the team needs a formula that counts the same comments.

| Ticket | Comment |
| --- | --- |
| 101 | Delivery was late |
| 102 | Great support |
| 103 | Late refund, still waiting |
| 104 | Product works well |
| 105 | Late again |

**Task:** Count the comments that mention late orders, using a formula that still works after the retirement.

**Solution:**

```excel
=COUNTIF(B2:B6, "*late*")
```

**Answer:** `3`, because tickets 101, 103 and 105 contain the word late. COUNTIF ignores case, so "Late refund" matches.

### Problem 2: Finding Cells That Show #NAME?

A monthly summary sheet has one summary cell for each report line. After a recalculation, the two cells that used COPILOT show errors.

| Report Line | Summary |
| --- | --- |
| North | #NAME? |
| South | Stock levels stable |
| East | #NAME? |
| West | Returns fell 4 percent |

**Task:** Count how many summary cells now return an error, so the team knows how many to rebuild.

**Solution:**

```excel
=SUMPRODUCT(--ISERROR(B2:B5))
```

**Answer:** `2`, because the North and East cells return errors and the other two cells hold text.

<!-- Image 3: Rebuilding Retired Summary Cells. See Images/Text/COPILOT.md -->

## Use Cases

### Customer Feedback Summaries

**Scenario:** A feedback workbook has a summary column in `C` that was built with COPILOT. Readers need a clear message instead of an error code.

```excel
=IF(ISERROR(C2), "Rebuild summary", C2)
```

**Why It Works:** ISERROR detects the `#NAME?` result after the retirement, so the sheet shows a plain message in its place. Replace each message with a manual summary or a standard formula.

### Survey Comment Coding

**Scenario:** Survey comments in column `B` need a label of Refund, Delivery or Other.

```excel
=IF(ISNUMBER(SEARCH("refund", B2)), "Refund", IF(ISNUMBER(SEARCH("late", B2)), "Delivery", "Other"))
```

**Why It Works:** SEARCH finds a keyword at any position and ignores case, and ISNUMBER returns TRUE when a keyword is found. The nested IF tests Refund first, so a comment that mentions both words gets the Refund label.

### Workbook Migration Audits

**Scenario:** An analyst must find every retired formula in a large workbook before a deadline.

```excel
=SUMPRODUCT(--ISERROR(B2:B500))
```

**Why It Works:** The count shows how many cells in the range return an error. To list the cells that contain the retired formula, use Find and Replace with the Look in option set to Formulas and search for COPILOT.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The function was retired on September 14, 2026, so recalculation cannot find it. | Replace the formula with a standard formula, or copy the cell and paste values to keep the last result. |
| Old text stays | Cached results remain until a cell recalculates. | Copy the text as values if you need a record of it before the workbook recalculates. |
| `#NAME?` in Google Sheets | Google Sheets has no COPILOT function. | Use the AI function in Google Sheets, or a standard formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Retired from September 14, 2026 | Was a preview for Microsoft 365 Insider and Frontier members from August 2025. Existing cells keep cached values and return `#NAME?` on recalculation. |
| Google Sheets | Not available | The closest alternative is the AI function, which generates text from a prompt and cell data. |

## Tips and Best Practices

- Use Find and Replace with Look in set to Formulas to list every COPILOT cell before you rebuild a workbook.
- Replace each COPILOT formula with a rule you can write down, such as COUNTIF or SEARCH, because those formulas keep recalculating after the retirement.
- Wrap any remaining COPILOT formula in IFERROR so the sheet shows a clear message while you rebuild it.
- Paste the text of a one-off Copilot pane answer as values so it does not depend on a retired function.
- Keep a copy of each workbook from before the retirement date so you can compare the old results with the new formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AI](../Google-specific/AI.md) | The Google Sheets function closest to COPILOT, for prompt-based text results. |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts cells that match a keyword rule, the usual replacement for a label. |
| [IFERROR](../Logical/IFERROR.md) | Shows a fallback message instead of `#NAME?`. |
| [ISERROR](../Information/ISERROR.md) | Tests whether a cell returns an error, which helps audit retired formulas. |
| [SEARCH](../Text/SEARCH.md) | Finds a keyword inside text, ignoring case. |

## Official Documentation

- [Microsoft Support: COPILOT function](https://support.microsoft.com/en-us/excel/copilot-function)
