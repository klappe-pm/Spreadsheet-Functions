---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
purpose:
  - Conditional Logic
  - Data Retrieval
use-case:
  - Dynamic Table Selection
  - Pricing Tier Lookup
  - Rotating Shift Schedules
related:
  - IF
  - INDEX
  - MATCH
  - SWITCH
  - VLOOKUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/choose-function
  - https://support.google.com/docs/answer/3093371
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Index Selection
  - Value Selector
tags:
  - excel
  - index-selection
  - nested-if
  - sheets
---

# CHOOSE

## Description

**CHOOSE** returns one value from a list, using a position number that you supply. An index of 1 returns the first value, 2 returns the second, and so on. With the values "Low", "Medium" and "High" and an index of 2, CHOOSE returns "Medium". Use it when a short, fixed list of options already has a position number, such as a plan code, a weekday number or a rotation day.

CHOOSE often replaces a nested IF. The formula `=IF(A1=1,"Poor",IF(A1=2,"Fair",IF(A1=3,"Good")))` becomes `=CHOOSE(A1,"Poor","Fair","Good")`, which is shorter and easier to change. For longer lists, or lists that change often, a lookup table with INDEX and MATCH or XLOOKUP is easier to maintain than a long CHOOSE.

Values can be numbers, text, cell references, ranges, defined names or formulas. A value can be a range, so CHOOSE can select which range SUM, AVERAGE or VLOOKUP works on. Excel accepts up to 254 values. The Google Sheets page gives a limit of 29 choices in one place and 30 in another, so keep Sheets lists well below that count.

## Syntax

```excel
=CHOOSE(index_num, value1, [value2], ...)
```

<!-- Image 1: Index Argument Anatomy. See Images/Lookup & Reference/CHOOSE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `index_num` | Yes | A whole number from 1 to the count of values, or a formula or cell that gives one. Decimals are cut to the whole number below them, so 2.9 selects 2. |
| `value1` | Yes | The first value. It can be a number, text, a cell reference, a range, a defined name, a formula or a function. |
| `value2` to `value254` | No | Additional values, up to 254 values in total in Excel. |

### Return Value

The value at the position given by `index_num`, or a range when the chosen value is a range. In Excel, an index below 1 or above the number of values returns `#VALUE!`. The Google Sheets page states that an out-of-range index returns `#NUM!`.

## Examples

### Example 1: Choosing a Shipping Carrier

```excel
=CHOOSE(3, "Post", "Courier", "Freight")
```

**Result:** `Freight`

The index is 3, so CHOOSE returns the third value in the list.

### Example 2: Naming a Priority From a Code

```excel
=CHOOSE(B2, "Low", "Medium", "High")
```

**Result:** `Medium` when B2 holds 2

The index comes from B2. Changing the number in B2 changes the label without editing the formula.

<!-- Image 2: Index to Value Map. See Images/Lookup & Reference/CHOOSE.md -->

### Example 3: Weekday Name From a Date

```excel
=CHOOSE(WEEKDAY(A2), "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
```

**Result:** `Tue` when A2 holds 5 March 2024

WEEKDAY returns 3 for a Tuesday when Sunday is day 1, which is the default. CHOOSE then returns the third label.

### Example 4: Replacing a Nested IF

```excel
=IFERROR(CHOOSE(B3, "Poor", "Fair", "Good", "Very Good", "Excellent"), "Check code")
```

**Result:** `Very Good` when B3 holds 4

The five labels replace four nested IF tests. IFERROR shows "Check code" when B3 is 0, 6 or text.

### Example 5: Choosing a Range for SUM

```excel
=SUM(CHOOSE(B5, C2:C6, D2:D6))
```

**Result:** the total of D2:D6 when B5 holds 2

CHOOSE returns the range D2:D6 as a reference, and SUM adds it up. This selects a column of figures from a choice made in one cell.

## Story Problems

### Problem 1: Subscription Fee With an Annual Discount

A software seller charges by plan. The plan code is in cell B2, and the monthly fees are listed below.

| Code | Plan | Monthly Fee |
| --- | --- | --- |
| 1 | Basic | 9 |
| 2 | Plus | 19 |
| 3 | Pro | 39 |

**Task:** The customer in B2 has code 3. Find the monthly fee after a 10 percent discount.

**Solution:**

```excel
=CHOOSE(B2, 9, 19, 39) * 0.9
```

**Answer:** `35.1`. CHOOSE returns 39 for code 3, and the 10 percent discount reduces it to 35.1.

### Problem 2: Shift Rotation

A plant runs three shifts in a repeating order: Day, Swing and Night. Day 1 of the cycle is Day, day 2 is Swing, day 3 is Night, and the cycle then repeats. The rotation day for a worker is in cell A2.

| Rotation Day | Shift |
| --- | --- |
| 6 | Night |
| 7 | Day |
| 8 | ? |

**Task:** Return the shift for rotation day 8 in cell A2, using a formula that works for any day number.

**Solution:**

```excel
=CHOOSE(MOD(A2 - 1, 3) + 1, "Day", "Swing", "Night")
```

**Answer:** `Swing`. MOD(7, 3) is 1, adding 1 gives position 2, and position 2 in the list is Swing.

<!-- Image 3: Shift Rotation Result. See Images/Lookup & Reference/CHOOSE.md -->

## Use Cases

### Pricing Tier Lookup

**Scenario:** A subscription business has four customer tiers stored as the numbers 1 to 4. Each tier needs a discount rate and a display name.

```excel
=CHOOSE($B$2, 0%, 4%, 8%, 12%)
```

**Why It Works:** One tier cell drives every CHOOSE in the sheet, so the discount and the display name always match. Store the tier as a number for calculations and use CHOOSE only for labels and rates.

### Dynamic Table Selection

**Scenario:** A product sheet has three separate price tables, one per region, and the user picks the region from a drop-down that holds the number 1, 2 or 3.

```excel
=VLOOKUP(B2, CHOOSE(A1, North!A:D, South!A:D, West!A:D), 3, FALSE)
```

**Why It Works:** CHOOSE returns the chosen table as a reference, and VLOOKUP searches it. The formula avoids INDIRECT, which builds a reference from text.

### Rotating Shift Schedules

**Scenario:** A call center runs a three-day rotation for each team and needs the shift for any date in a column of dates.

```excel
=CHOOSE(MOD(A2 - $A$1, 3) + 1, "Day", "Swing", "Night")
```

**Why It Works:** MOD counts the days since the start date in `$A$1` and repeats every three days. CHOOSE turns the repeating position into the shift name. Copy the formula down to cover the schedule.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Excel) | The index is below 1 or above the number of values. | Check the index range, or wrap the formula in IFERROR. |
| `#NUM!` (Google Sheets) | The index is outside the number of choices. | Check the count of values, or wrap the formula in IFERROR. |
| `#VALUE!` | The index cell holds text that is not a number. | Convert it with VALUE, or fix the source cell. |
| Unexpected result | The source list is numbered from 0. | Add 1 to the index so 0 becomes 1. |
| Empty result | The selected value is an empty cell. | This is not an error. Check the source cell that holds the value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 and current Excel versions | Accepts up to 254 values. An out-of-range index returns `#VALUE!`. An array index evaluates every value. |
| Google Sheets | Available | The page states that an out-of-range index returns `#NUM!`. It gives a limit of 29 choices in one place and 30 in another. |

## Tips and Best Practices

- Use CHOOSE for short fixed lists, and use INDEX with MATCH or XLOOKUP for lists that change often.
- Wrap CHOOSE in IFERROR on sheets that other people fill in, so a bad index shows a clear message.
- Store the index as a whole number, and document what each position means beside the formula.
- Keep the number of values low; a long CHOOSE is hard to audit when a value changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IF](../Logical/IF.md) | Chooses between two outcomes based on a condition rather than a position. |
| [INDEX](INDEX.md) | Returns a value from a range by position, which suits longer or changing lists. |
| [MATCH](MATCH.md) | Converts a value into the position that CHOOSE needs as its index. |
| [SWITCH](../Logical/SWITCH.md) | Chooses a result by matching a value instead of a position number. |
| [VLOOKUP](VLOOKUP.md) | Looks up a value in a table by key, which suits larger tables. |

## Official Documentation

- [Microsoft Support: CHOOSE function](https://support.microsoft.com/en-us/excel/functions/choose-function)
- [Google Docs Editors Help: CHOOSE](https://support.google.com/docs/answer/3093371)
