---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
purpose:
  - Bitwise Operations
use-case:
  - Alarm Panel Summaries
  - Shift Coverage Masks
related:
  - BIN2DEC
  - BITAND
  - BITLSHIFT
  - BITRSHIFT
  - BITXOR
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bitor-function
  - https://support.google.com/docs/answer/9083934
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bitwise Or
tags:
  - bit-masks
  - bitwise
  - excel
  - sheets
---

# BITOR

## Description

**BITOR** returns the bitwise OR of two whole numbers. The function compares the binary patterns position by position and sets a result bit to 1 when either input has a 1 in that position. The result is returned as a decimal number.

Use BITOR to combine several flags into one number, such as building a permission mask or summarizing which alarms are active across two sensors. Where the flags do not overlap, the result equals the sum of the inputs. Where they overlap, the shared bit is counted once, so the result can be smaller than the sum.

In Microsoft Excel, each argument must be a whole number from 0 to `2^48 - 1` (281,474,976,710,655). A negative or larger value returns `#NUM!`. Google Sheets requires decimal representations and does not list range limits on its help page.

BITOR is available in both Microsoft Excel and Google Sheets.

## Syntax

```excel
=BITOR(number1, number2)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BITOR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first whole number, zero or greater. Google Sheets calls it `value1`. |
| `number2` | Yes | The second whole number, zero or greater. Google Sheets calls it `value2`. |

### Return Value

A decimal number that holds every bit set in either input. The function returns `#NUM!` in Excel when an argument is negative, not a whole number or above `2^48 - 1`, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Combining Two Bit Patterns

```excel
=BITOR(6, 11)
```

**Result:** `15`

In binary, 0110 OR 1011 gives 1111, which is 15.

### Example 2: Text Values Converted First

```excel
=BITOR(BIN2DEC("0100"), BIN2DEC("0011"))
```

**Result:** `7`

BIN2DEC turns the strings into 4 and 3. Their bits do not overlap, so the result is their sum, 7.

### Example 3: Filled Down a Column

Values in `A2:A4` are 1, 2 and 4, and `B2` holds the value 8.

```excel
=BITOR(A2, $B$2)
```

Fill the formula down to `C4`.

**Result:** `9` (A2), `10` (A3), `12` (A4)

Each result adds the flag in column A to the flag in `B2`, because the bits do not overlap.

<!-- Image 2: Bit Union Diagram. See Images/Engineering/BITOR.md -->

### Example 4: Nested Calls Build a Larger Mask

```excel
=BITOR(BITOR(1, 2), 4)
```

**Result:** `7`

The inner call returns 3, and the outer call adds the flag worth 4. Nesting is a clear way to build a mask from named flags.

## Story Problems

### Problem 1: Summarizing an Alarm Panel

An alarm panel uses four bits: Door is 1, Smoke is 2, Heat is 4 and Power is 8. Sensor A reports 5 and Sensor B reports 10. The operator needs one number that shows every alarm active across both sensors.

| Sensor | Reading |
| --- | --- |
| Sensor A | 5 |
| Sensor B | 10 |

**Task:** Put `=BITOR(B2, B3)` in `C2`, then read which alarms the number holds.

**Solution:**

```excel
=BITOR(B2, B3)
```

**Answer:** `15`. Sensor A holds Door and Heat, and Sensor B holds Smoke and Power, so all four alarms are active.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BITOR.md -->

### Problem 2: Covering Shifts With Two Rosters

Two staff masks show which of four shifts each person covers. Morning is 1, Afternoon is 2, Evening is 4 and Night is 8. The planner needs the combined coverage.

| Staff | Mask |
| --- | --- |
| Staff A | 3 |
| Staff B | 9 |

**Task:** Calculate the combined coverage and list the shifts it includes.

**Solution:**

```excel
=BITOR(3, 9)
```

**Answer:** `11`, which is 1 + 2 + 8. Morning, Afternoon and Night are covered, and Evening is not.

## Use Cases

### Alarm Panel Summaries

**Scenario:** A control room merges the alarm bits from several sensors into one status number for each panel.

```excel
=BITOR(Table1[SensorA], Table1[SensorB])
```

**Why It Works:** The function returns the combined status for each row, so a dashboard can show one number per panel.
Use the bit meanings in a legend beside the table so the number can be decoded by anyone who reads it.

### Shift Coverage Masks

**Scenario:** A scheduler builds a coverage mask for each team by combining the masks of its members.

```excel
=BITOR(BITOR(B2, B3), B4)
```

**Why It Works:** Nesting BITOR combines three masks, and each bit that appears in any member's mask stays set in the total.
Keep each member's mask in its own column so the team mask is easy to recheck.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | An argument is negative, not a whole number, or above `2^48 - 1`. | Validate each input before the call. |
| `#VALUE!` | An argument is text, blank or an error. | Convert the input to a number or reference a numeric cell. |
| Smaller total than expected | Two flags share a bit, so the overlapping bit is counted once. | Use flags with separate bits, such as powers of 2, to avoid overlap. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365 and current Excel versions | Inputs must be whole numbers from 0 to `2^48 - 1`. Check the Microsoft Support page for the exact version list. |
| Google Sheets | Available | Arguments are `value1` and `value2`. Inputs must be given in decimal form. The help page lists no range limits. |

## Tips and Best Practices

- Assign each flag a power of 2 so the combined value can be read back with BITAND.
- Label the flag values in a legend cell so the combined number is easy to decode.
- Use nested BITOR calls for a short list of masks and a helper column for a long list.
- Remember that BITOR of overlapping masks is not their sum, so do not add masks when they share bits.
- Convert binary text with BIN2DEC before combining, if the source stores masks as binary.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts binary text to decimal before the combination. |
| [BITAND](BITAND.md) | Reads the shared bits back out of a combined mask. |
| [BITLSHIFT](BITLSHIFT.md) | Creates the flag values, one bit per position. |
| [BITRSHIFT](BITRSHIFT.md) | Moves bits to the right when reading a flag from a higher position. |
| [BITXOR](BITXOR.md) | Returns the bits that differ instead of the bits either input holds. |

## Official Documentation

- [Microsoft Support: BITOR function](https://support.microsoft.com/en-us/excel/functions/bitor-function)
- [Google Docs Editors Help: BITOR](https://support.google.com/docs/answer/9083934)
