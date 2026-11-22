---
domain: Spreadsheet Functions
category: Google-specific
subcategory: AI Functions
purpose:
  - AI Assistance
use-case:
  - Feedback Sentiment Labels
  - Product Tagline Drafts
  - Support Ticket Triage
related:
  - ARRAYFORMULA
  - DETECTLANGUAGE
  - GOOGLETRANSLATE
  - IF
  - IFERROR
level: 3
source:
  - https://support.google.com/docs/answer/15877199
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Gemini Function
tags:
  - ai
  - automation
  - generative-ai
  - sheets
---

# AI

## Description

**AI** sends a prompt to Google's Gemini model and places the generated text in the cell. The official help page describes four main jobs: generating text, summarizing information, categorizing information (including sentiment analysis), and accessing real-time information from Google Search. The function is also available under the name **GEMINI**, which is an alternative name for the same function.

Use AI when a task needs judgment about language, such as labeling feedback as positive or negative, writing a short summary of a long comment, or drafting a slogan. Give it a clear instruction and point the optional range argument at the cells the instruction refers to. The function does not read your whole spreadsheet or other Drive files, so the data it needs must be inside the sheet and referenced in the formula.

Because the output is generated text, the same prompt can return different wording on different runs. The official page notes that you cannot undo the output, but you can regenerate it. Review results before you act on them, especially for classifications that drive decisions. The function returns text only, and it is available only in Google Sheets with an eligible plan, described below.

<!-- Image 1: AI Prompt and Range. See Images/Google-specific/AI.md -->

## Syntax

```excel
=AI("prompt", [range])
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `prompt` | Yes | A specific instruction that describes the action you want, such as a classification, a summary or a short slogan. Put it in quotation marks or refer to a cell that holds it. |
| `range` | No | The cells the prompt refers to when generating the output, such as `A2` or `A2:D2`. Include it whenever the prompt talks about data in the sheet. |

### Return Value

Text: the generated response for the prompt. The official page states that responses are limited to text, so numbers, charts and images are not returned.

## Examples

### Example 1: Writing a Short Label

```excel
=AI("Write a three word label for this product", B2)
```

**Result:** A short text label based on the product name in B2. The exact words vary between runs.

Because the output is generated, check that the label fits the product before publishing it.

### Example 2: Summarizing a Comment

```excel
=AI("Summarize this customer comment in one sentence", C2)
```

**Result:** A single sentence that restates the comment in C2. Length and wording depend on the comment and the model.

Summaries work best for comments of a few sentences; very long text may need a clearer instruction.

### Example 3: Classifying Sentiment

```excel
=AI("Label this message as Positive, Negative or Neutral", D2)
```

**Result:** One of the three labels for the message in D2. The model chooses the label, so review borderline messages by hand.

Naming the allowed labels in the prompt keeps the output consistent enough to count with COUNTIF.

<!-- Image 2: AI Sentiment Label Column. See Images/Google-specific/AI.md -->

### Example 4: Working With a Multi-Cell Range

```excel
=AI("Give a one sentence summary of this feedback for the store manager", A2:D2)
```

**Result:** One sentence that combines the four cells in row 2. The output appears in the cell that holds the formula.

Use a range when the prompt needs several related cells together, such as a name, a date and a comment in one row.

## Story Problems

### Problem 1: Labeling Customer Feedback

A café collected four feedback notes in `A2:A5`. The manager wants a sentiment label next to each note in column B.

| Feedback |
| --- |
| The coffee was excellent and staff were quick. |
| The seat was cold and the wait was long. |
| The bakery items were fine, nothing special. |
| Loved the new oat milk option. |

**Task:** Put a sentiment label for each note in `B2:B5`, then count how many labels were produced.

**Solution:**

```excel
=AI("Label this feedback as Positive, Negative or Neutral", A2)
```

Fill this formula down `B2:B5`.

**Answer:** Four labels, one per note. The wording of each label depends on the model, so a reviewer should confirm each one. A reasonable result is Positive for the first and last notes, Negative for the second, and Neutral for the third.

### Problem 2: Drafting Tagline Options

A small shop wants a tagline of ten words or fewer for each of its three products listed in `A2:A4`.

| Product |
| --- |
| Ceramic mug |
| Linen tote |
| Cedar candle |

**Task:** Write a tagline in column B for each product, keeping each one to ten words or fewer.

**Solution:**

```excel
=AI("Write one tagline of ten words or fewer for this product", A2)
```

**Answer:** Three taglines, one per product. Count the words in each result with a separate formula, because the official examples show prompts that limit length but do not guarantee the exact count.

## Use Cases

### Feedback Sentiment Labels

**Scenario:** A support team receives hundreds of survey comments each week and wants a quick positive, negative or neutral label on each one before a manager reviews them.

```excel
=AI("Label this comment as Positive, Negative or Neutral", A2)
```

**Why It Works:** The prompt names the allowed labels, and the range points at one comment. Review a sample each week, because the model can misread sarcasm or mixed comments.

### Support Ticket Triage

**Scenario:** A help desk wants a first guess at the category of each new ticket so that the right team sees it sooner.

```excel
=IFERROR(AI("Classify this ticket as Billing, Technical or Account", B2), "Check manually")
```

**Why It Works:** IFERROR returns a fallback message if the function cannot produce a result, so the sheet stays readable. Route tickets by the label only after a person has checked the early results.

### Product Tagline Drafts

**Scenario:** A marketing assistant needs first drafts of short taglines for a catalog of products.

```excel
=AI("Write one tagline of ten words or fewer for this product", A2)
```

**Why It Works:** The product name sits in one cell, so the same formula works down a column. Treat each output as a draft for editing, not final copy.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Function not available | Your account has no eligible Google Workspace or Google AI plan, and you are not in the Experiments program. | Ask an administrator to confirm the plan, or use a manual or other formula alternative. |
| Function blocked | An administrator setting or the sheet language restricts AI. | Check the admin settings and the language setting. |
| Nested use fails | AI was placed inside another function such as IF. The official page says embedded AI functions are not supported. | Put AI in its own cell and reference that cell from the other formula. |
| Partial output | A multi-cell selection has more than 350 cells with AI functions; only the first 350 generate. | Split the work into batches of 350 cells or fewer. |
| Output stops | A short-term or long-term generation limit was reached. | Wait for the limit to reset. If a long-term limit applies, wait 24 hours. |
| Stale result | The data changed, but concatenated non-contiguous ranges do not refresh automatically. | Refresh the output manually by regenerating it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The Excel COPILOT function was retired on September 14, 2026, so no formula-based equivalent is available from that date. | See [COPILOT](../Text/COPILOT.md) for the retirement details. |
| Google Sheets | Requires an eligible Google Workspace or Google AI plan, or the Google Workspace Experiments trusted tester program. | Restricted when admin settings or the sheet language block access. Returns text only. |

## Tips and Best Practices

- Write prompts that name the exact output format, such as a label list or a word limit, so results are easier to check.
- Put only the data the prompt needs in the range, and keep sensitive records out of the sheet unless your administrator has approved AI use for them.
- Wrap AI in IFERROR for formulas that feed reports, so one failed cell does not break the layout.
- Spot check a sample of results before a team acts on them, and regenerate outputs that look wrong.
- Keep AI in its own column, not nested inside IF or other functions, because nested use is not supported.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYFORMULA](ARRAYFORMULA.md) | Applies a single formula across a range; AI runs per cell, so combine with care. |
| [DETECTLANGUAGE](../Text/DETECTLANGUAGE.md) | Identifies the language of text, which can be checked before generating output. |
| [GOOGLETRANSLATE](GOOGLETRANSLATE.md) | Translates text between languages using two-letter language codes, a task with a fixed target language. |
| [IF](../Logical/IF.md) | Uses a label or flag from AI to choose another value. |
| [IFERROR](../Logical/IFERROR.md) | Returns a fallback message when AI cannot produce an output. |

## Official Documentation

- [Google Docs Editors Help: AI function in Google Sheets](https://support.google.com/docs/answer/15877199)
