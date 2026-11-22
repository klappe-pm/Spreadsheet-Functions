---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Reference Building
  - Type Checking
use-case:
  - Named Range Input Check
  - Text Address Check
related:
  - INDIRECT
  - ISFORMULA
  - ISNUMBER
  - OFFSET
  - ROW
level: 3
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093354
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - references
  - sheets
  - type-checking
---

# ISREF

## Description

**ISREF** returns TRUE when a value is a reference to a cell or range, and FALSE when it is a plain value or text. A cell address typed as text, such as `"A2"`, is a string, not a reference, so it returns FALSE. Writing `=ISREF(A2)` returns TRUE because A2 itself is a reference, whatever its content.

Use ISREF in formulas that accept a range or cell as an input, such as a template that must receive a reference, or a helper that checks whether a named range was passed in. It tests the kind of value, not what the cell contains. To test whether a cell holds a formula, use ISFORMULA.

To turn a text address into a usable reference, use INDIRECT. After that conversion, ISREF of the INDIRECT result is a reference test, not a text test.

## Syntax

```excel
=ISREF(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISREF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. A cell reference, a range or a name that refers to a cell or range is the typical input. Text and numbers return FALSE. |

### Return Value

TRUE when `value` is a reference to a cell or range. FALSE when `value` is a text string, a number, a logical value or the result of a calculation.

## Examples

### Example 1: A Cell Reference

```excel
=ISREF(A2)
```

**Result:** `TRUE`

A2 is a reference to a cell, so the function returns TRUE regardless of what A2 contains.

### Example 2: A Text Address

```excel
=ISREF("A2")
```

**Result:** `FALSE`

The quotation marks make the address a text string, which is not a reference.

### Example 3: The Result of a Calculation

```excel
=ISREF(MIN(A2:A6))
```

**Result:** `FALSE`

MIN returns a number, not a reference, so the function returns FALSE.

### Example 4: Labeling a Calculated Input

Cells B2 and B3 hold the numbers 4 and 9.

```excel
=IF(ISREF(MAX(B2:B3)),"Reference","Value")
```

**Result:** `Value`

MAX returns a number, not a reference, so the formula labels the input as a value.

## Story Problems

### Problem 1: Named Range Passed to a Template

A budget template expects a named range as its input. The name `Sales` refers to the range `B2:B8` on the data sheet. The template author wants a check that confirms the name refers to a range before the template runs.

| Name | Refers To |
| --- | --- |
| Sales | Data!B2:B8 |

**Task:** Test whether the name `Sales` is a reference.

**Solution:**

```excel
=ISREF(Sales)
```

**Answer:** `TRUE`. The name refers to a range, so it is a reference.

### Problem 2: Two Kinds of Address Input

A form takes two inputs. The first input is a cell reference, entered in a way that passes the reference itself. The second input is the address typed as text. The builder wants to see how ISREF treats each one.

| Argument | How It Is Entered |
| --- | --- |
| Argument 1 | Cell reference A3 |
| Argument 2 | Text "A3" |

**Task:** Test both arguments.

**Solution:**

```excel
=ISREF(A3)
=ISREF("A3")
```

**Answer:** `TRUE` for argument 1 and `FALSE` for argument 2. Only the reference passes the test, and the typed address needs INDIRECT before it can be used as a reference.

<!-- Image 2: Two Kinds of Address Input. See Images/Information/ISREF.md -->

## Use Cases

### Named Range Input Check

**Scenario:** A reporting formula accepts a named range from a drop-down. The formula should stop with a clear message if the name does not point to a range.

```excel
=IF(ISREF(Sales),SUM(Sales),"Select a named range")
```

**Why It Works:** When the name refers to a range, ISREF returns TRUE and the sum runs. If the name is missing or points to a value, the message appears instead of an error.

### Text Address Check

**Scenario:** A helper formula sums a range that the caller passes in. Callers sometimes type the address as text instead of passing a real range.

```excel
=LAMBDA(src,IF(ISREF(src),SUM(src),"Pass a range, not typed text"))("B2:B8")
```

**Why It Works:** The typed text "B2:B8" is a string, so ISREF returns FALSE and the guard returns a message instead of a wrong total. Convert typed text with INDIRECT only after the address has been checked.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for an address that looks valid | The address is stored as text, such as "A2". | Convert the text with INDIRECT before using it as a reference. |
| `FALSE` for a cell that holds a formula | ISREF tests the kind of value, not whether the cell holds a formula. | Use ISFORMULA to test for a formula. |
| `#NAME?` | The name in the formula is not defined. | Create the name in Name Manager or correct the spelling. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Accepts cell references, ranges and named references. Text addresses return FALSE. |
| Google Sheets | Available | The Sheets help page describes it as checking whether a value is a valid cell reference. Test named ranges and INDIRECT results before relying on them. |

## Tips and Best Practices

- Use ISREF in templates and helper formulas that must receive a reference, not a value.
- Convert typed addresses with INDIRECT only after confirming they are valid.
- Use ISFORMULA or ISNUMBER when the question is about the cell content instead of the reference type.
- Keep named ranges simple so ISREF checks read clearly.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDIRECT](../Lookup%20%26%20Reference/INDIRECT.md) | Converts a text address into a reference that ISREF accepts. |
| [ISFORMULA](ISFORMULA.md) | Tests whether a cell holds a formula, a different question from ISREF. |
| [ISNUMBER](ISNUMBER.md) | Tests whether a value is numeric, which is useful after a reference is read. |
| [OFFSET](../Lookup%20%26%20Reference/OFFSET.md) | Returns a reference that ISREF can test. |
| [ROW](../Lookup%20%26%20Reference/ROW.md) | Returns row numbers, which can help build references by position. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISREF](https://support.google.com/docs/answer/3093354)
