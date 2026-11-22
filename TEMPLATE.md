---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Data Retrieval
use-case:
  - Price Lookup
related:
  - INDEX
  - MATCH
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/function-name-function
  - https://support.google.com/docs/answer/0000000
date-created: YYYY-MM-DD
date-revised: YYYY-MM-DD
aliases: []
tags:
  - excel
  - sheets
---

# FUNCTION_NAME

<!--
Template rules
Frontmatter keys appear in exactly this order. List values are deduplicated and sorted A to Z (case-insensitive); an empty list is written as [].
domain: always Spreadsheet Functions.
category: the folder the page lives in (the official Microsoft category, or the Google category for a Sheets-only function).
subcategory: one Title Case group inside the category.
purpose: one or more Title Case values from the purpose vocabulary in the Frontmatter Schema section of README.md.
use-case: one or more Title Case business scenarios.
related: function names (uppercase) that exist in this library.
level: 1 Foundational, 2 Core, 3 Intermediate, 4 Advanced, 5 Specialist.
source: official Microsoft and Google documentation URLs only.
date-created never changes; date-revised changes on every content edit.
tags: lowercase; include excel and/or sheets for each platform that supports the function.
Headings use Title Case. Formula code fences use the excel tag; other fences use text.
Never use an em dash, en dash, spaced hyphen or double hyphen as punctuation. Never hard-wrap prose.
Image placement markers are HTML comments that point to the image guide in Images/<Category>/<NAME>.md.
-->

## Description

One to four paragraphs: what the function does in plain language, when to use it, how it differs from similar functions, and any platform or version caveats.

## Syntax

```excel
=FUNCTION_NAME(required_arg, [optional_arg])
```

<!-- Image 1: Syntax Anatomy. See Images/<Category>/FUNCTION_NAME.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `required_arg` | Yes | What it accepts and how edge cases behave. |
| `optional_arg` | No | What it does and the default when omitted. |

### Return Value

The data type returned and the conditions that produce errors.

## Examples

### Example 1: Basic Usage

```excel
=FUNCTION_NAME(A2, B2)
```

**Result:** `value`

What the example shows and why it works.

### Example 2: Combined With Other Functions

```excel
=IFERROR(FUNCTION_NAME(A2, B2), "Not found")
```

**Result:** `value`

What the combination adds.

## Story Problems

### Problem 1: Short Scenario Title

A short, original business story with the data the reader needs.

| Column A | Column B |
| --- | --- |
| value | value |

**Task:** What the reader must calculate.

**Solution:**

```excel
=FUNCTION_NAME(A2:A6, B2)
```

**Answer:** `value`, with one or two sentences on why.

## Use Cases

### Use Case Title

**Scenario:** A realistic business situation.

```excel
=FUNCTION_NAME(Table1[Column], criteria)
```

**Why It Works:** How the formula solves the problem and what to watch for.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | What triggers it. | How to fix it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Version or release | Excel-only behavior. |
| Google Sheets | Availability | Sheets-only behavior. |

## Tips and Best Practices

- Practical advice in one line per tip.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | When to use it instead or together. |

## Official Documentation

- [Microsoft Support: FUNCTION_NAME function](https://support.microsoft.com/en-us/excel/functions/function-name-function)
- [Google Docs Editors Help: FUNCTION_NAME](https://support.google.com/docs/answer/0000000)
