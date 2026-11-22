---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Workbook Information
use-case:
  - Budget Formula Labels
  - Forecast Review Checks
  - Formula Audit Before Handoff
related:
  - CELL
  - INFO
  - ISFORMULA
  - ISREF
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/formulatext-function
  - https://support.google.com/docs/answer/9365792
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Formula As Text
  - Show Formula
tags:
  - excel
  - formula-audit
  - information
  - sheets
---

# FORMULATEXT

## Description

**FORMULATEXT** returns the formula in a cell as a text string, exactly as it appears in the formula bar. It is useful for documenting a workbook, checking which formulas a colleague wrote, or placing a readable copy of a formula next to its result. Because the output is text, you can search it with SEARCH or FIND to find cells that use a particular function or reference.

FORMULATEXT does not return a calculated value. A cell that holds a typed number or text has no formula, so Excel returns `#N/A` for it. Wrap the call in IFERROR or pair it with ISFORMULA when a sheet contains a mix of formulas and constants.

When you pass a range instead of a single cell, FORMULATEXT reads only the top-left cell of that range. Google Sheets supports the same function with the same single-cell argument, but its help page does not state the result for a cell without a formula, so test that case before relying on it.

## Syntax

```excel
=FORMULATEXT(reference)
```

<!-- Image 1: Formula Bar and Text Output. See Images/Lookup & Reference/FORMULATEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | Yes | A reference to the cell that holds the formula. If the reference covers several cells, only the top-left cell is read. |

### Return Value

A text string containing the formula, including the leading equals sign. It returns `#N/A` in Excel when the referenced cell does not contain a formula. It returns `#VALUE!` when the argument is not a valid reference.

## Examples

The examples use this small budget in `A1:A3`. Cell `A1` holds 10, `A2` holds 20, and `A3` holds the formula `=A1+A2`, which returns 30.

### Example 1: Show a Formula as Text

```excel
=FORMULATEXT(A3)
```

**Result:** `=A1+A2`

The function reads the formula in `A3` and returns it as text. The result is not recalculated, so changing `A1` does not change the text.

### Example 2: Handle a Cell That Has No Formula

```excel
=IFERROR(FORMULATEXT(A1), "Typed value")
```

**Result:** `Typed value`

`A1` holds a constant rather than a formula, so FORMULATEXT returns `#N/A`. IFERROR replaces that error with a readable label.

### Example 3: Label Each Cell as Formula or Typed Value

```excel
=IF(ISFORMULA(A3), FORMULATEXT(A3), "Typed value")
```

**Result:** `=A1+A2`

ISFORMULA checks first, so FORMULATEXT runs only on cells that contain a formula. This pattern avoids the `#N/A` error entirely.

### Example 4: Find Cells That Use a Specific Function

Cell `C2` contains `=VLOOKUP(B2, Prices!A:B, 2, FALSE)`.

```excel
=ISNUMBER(SEARCH("VLOOKUP", FORMULATEXT(C2)))
```

**Result:** `TRUE`

SEARCH finds the text `VLOOKUP` inside the formula text and is not case sensitive. Copy the formula down a column next to the cells you want to check, and each row reports whether it uses VLOOKUP.

## Story Problems

### Problem 1: Labeling the Total Formula

A small business keeps a quarterly cost sheet. Column B holds the costs, and `B4` is the total.

| Line | Cost |
| --- | --- |
| Rent | 1200 |
| Supplies | 850 |
| Total | 2050 |

`B4` contains `=SUM(B2:B3)`.

**Task:** In `C4`, show the formula used for the total so a reviewer can read it without clicking the cell.

**Solution:**

```excel
=FORMULATEXT(B4)
```

**Answer:** `=SUM(B2:B3)`. FORMULATEXT returns the formula text from the referenced cell, so the reviewer sees the range that the total adds.

### Problem 2: Sorting Formulas From Typed Prices

A price list has four rows. Some prices are typed in and others are calculated from a base price.

| Item | Price |
| --- | --- |
| Lamp | 45 |
| Lamp Shade | =B2*2 |
| Desk | 60 |
| Desk Pad | =B4+5 |

**Task:** In column C, label each price as `Formula` or `Typed`.

**Solution:**

```excel
=IF(ISFORMULA(B2), "Formula", "Typed")
```

Copy the formula down to `C5`.

**Answer:** Typed, Formula, Typed and Formula, in rows 2 to 5. Rows 3 and 5 hold calculated prices, and rows 2 and 4 hold typed prices.

<!-- Image 2: Labeled Price Column. See Images/Lookup & Reference/FORMULATEXT.md -->

## Use Cases

### Budget Formula Labels

**Scenario:** A finance manager sends a budget workbook to department heads and wants each total to show the calculation behind it.

```excel
=FORMULATEXT(B12)
```

**Why It Works:** The label recalculates when the total's formula changes, so it never goes out of date the way a typed note does.

### Formula Audit Before Handoff

**Scenario:** An analyst must confirm that no cell in a revenue column still uses an old lookup function before the workbook moves to a new owner.

```excel
=IF(ISNUMBER(SEARCH("INDEX", FORMULATEXT(D2))), "Uses INDEX", "Other")
```

**Why It Works:** SEARCH inside the formula text finds the old function, and the result column shows every cell that needs review. Use a filter on that column to list the flagged cells.

<!-- Image 3: Locating Formulas With SEARCH. See Images/Lookup & Reference/FORMULATEXT.md -->

### Forecast Review Checks

**Scenario:** A reviewer wants to confirm that every output cell in a forecast refers to the assumptions sheet.

```excel
=IF(ISNUMBER(SEARCH("Assumptions!", FORMULATEXT(E2))), "Linked", "Check")
```

**Why It Works:** The formula text includes the sheet name, so a missing `Assumptions!` reference marks the cell for review.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The referenced cell holds a typed value, not a formula. | Wrap the call in IFERROR or check with ISFORMULA first. |
| `#VALUE!` | The argument is not a valid cell or range reference. | Pass a cell reference such as `B4`, not a typed value. |
| Text shows the wrong cell | A range was passed and only the top-left cell was read. | Pass the single cell that holds the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel for the web | Returns `#N/A` for a cell without a formula. Pair with ISFORMULA to avoid the error. |
| Google Sheets | Available | Same single-cell argument. The help page does not state the output for a cell without a formula, so test before relying on it. ISFORMULA is the matching check. |

## Tips and Best Practices

- Pair FORMULATEXT with ISFORMULA so each cell reports either its formula or a clear label.
- Use SEARCH with FORMULATEXT to find every cell that uses a function, sheet name or reference you plan to retire.
- Place the formula text in a neighboring column and hide that column only when reviewers do not need it.
- Pass a single cell rather than a range, because only the top-left cell is read.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CELL](../Information/CELL.md) | Returns properties of a cell such as its format or address, not its formula text. |
| [INFO](../Information/INFO.md) | Returns information about the operating environment, not the contents of a cell. |
| [ISFORMULA](../Information/ISFORMULA.md) | Returns TRUE when a cell contains a formula, so you can check before reading its text. |
| [ISREF](../Information/ISREF.md) | Returns TRUE when a value is a valid reference, which helps when the argument might be a constant. |

## Official Documentation

- [Microsoft Support: FORMULATEXT function](https://support.microsoft.com/en-us/excel/functions/formulatext-function)
- [Google Docs Editors Help: FORMULATEXT](https://support.google.com/docs/answer/9365792)
