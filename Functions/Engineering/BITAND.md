---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
purpose:
  - Bitwise Operations
use-case:
  - Feature Flag Checks
  - Permission Mask Audits
related:
  - BIN2DEC
  - BITLSHIFT
  - BITOR
  - BITRSHIFT
  - BITXOR
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bitand-function
  - https://support.google.com/docs/answer/9061440
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bitwise And
tags:
  - bit-masks
  - bitwise
  - excel
  - sheets
---

# BITAND

## Description

**BITAND** returns the bitwise AND of two whole numbers. The function writes each number in binary, compares the two bit patterns position by position, and sets a result bit to 1 only when both inputs have a 1 in that position. The result is returned as a decimal number.

Use BITAND to test whether one or more flags are set in a number that packs several yes or no settings. A permission value such as 13 can hold four flags, and `BITAND(13, 4)` shows whether the flag worth 4 is on. This is the everyday use of the function in permission checks and feature toggles.

In Microsoft Excel, both arguments must be non-negative integers no greater than `2^48 - 1` (281,474,976,710,655). A negative, fractional or larger value returns `#NUM!`. Google Sheets accepts decimal representations of the numbers and does not list range limits on its help page.

BITAND is available in both Microsoft Excel and Google Sheets.

## Syntax

```excel
=BITAND(number1, number2)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BITAND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first whole number, zero or greater. Google Sheets calls it `value1`. |
| `number2` | Yes | The second whole number, zero or greater. Google Sheets calls it `value2`. |

### Return Value

A decimal number that holds the bits both inputs share. The function returns `#NUM!` in Excel when an argument is negative, not an integer or above `2^48 - 1`, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Bits Shared by Two Numbers

```excel
=BITAND(14, 7)
```

**Result:** `6`

In binary, 1110 AND 0111 gives 0110, which is 6.

### Example 2: Text Values Converted First

```excel
=BITAND(BIN2DEC("1011"), BIN2DEC("0110"))
```

**Result:** `2`

BIN2DEC turns the two binary strings into 11 and 6. Their bits overlap only in the position worth 2.

### Example 3: Filled Down a Column

Values in `A2:A4` are 3, 5 and 7, and `B2` holds the mask 6.

```excel
=BITAND(A2, $B$2)
```

Fill the formula down to `C4`.

**Result:** `2` (A2), `4` (A3), `6` (A4)

The dollar signs hold the mask in `B2` fixed while the formula moves down the column.

<!-- Image 2: Bit Overlap Diagram. See Images/Engineering/BITAND.md -->

### Example 4: Negative Input Returns an Error

```excel
=BITAND(-1, 5)
```

**Result:** `#NUM!`

A negative argument is outside the range Excel accepts, so the function returns an error instead of a number.

## Story Problems

### Problem 1: Approval Rights in a Permission Mask

A records team stores each user's rights as one number. Read is 1, Write is 2, Approve is 4 and Export is 8. The manager needs a count of users who can approve.

| User | Mask |
| --- | --- |
| Avery | 7 |
| Blake | 13 |
| Casey | 4 |
| Drew | 9 |
| Emery | 12 |

**Task:** Put `=BITAND(B2, 4)` in `C2`, fill it down to `C6`, then count the rows that return 4.

**Solution:**

```excel
=COUNTIF(C2:C6, 4)
```

**Answer:** `4`. Avery, Blake, Casey and Emery have the Approve bit set. Drew's mask is 9, which is Read and Export only.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BITAND.md -->

### Problem 2: Rights Two Users Share

Two accounts have the masks 12 and 10. The administrator needs the rights that both accounts hold.

| Account | Mask |
| --- | --- |
| Account A | 12 |
| Account B | 10 |

**Task:** Calculate the shared rights as one number.

**Solution:**

```excel
=BITAND(12, 10)
```

**Answer:** `8`, which is the Export right alone. Account A has Approve and Export, and Account B has Write and Export, so Export is the only right in common.

## Use Cases

### Feature Flag Checks

**Scenario:** A product team stores enabled features as one number, and a support script needs to know whether the beta feature worth 16 is on for each account.

```excel
=BITAND(Table1[FeatureMask], 16) = 16
```

**Why It Works:** The formula returns TRUE for each row where the flag bit is set, so a filter on the column finds every account with the feature.
Use flag values that are powers of 2 so each flag occupies one bit.

### Permission Mask Audits

**Scenario:** A compliance reviewer needs a list of every mask that grants the Export right in a permission table.

```excel
=FILTER(Table1[User], BITAND(Table1[Mask], 8) = 8)
```

**Why It Works:** BITAND runs on the whole mask column, and FILTER keeps the users whose result equals 8.
FILTER requires a dynamic array version of Excel or a current version of Google Sheets.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | An argument is negative, not a whole number, or above `2^48 - 1`. | Check each input and convert or validate it before the call. |
| `#VALUE!` | An argument is text, blank or an error. | Convert the input to a number or reference a numeric cell. |
| Unexpected result | Two flags combined in one input, so the test needs a different bit. | Test the exact flag value, and remember that BITAND returns the shared bits, not a yes or no answer. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365 and current Excel versions | Inputs must be whole numbers from 0 to `2^48 - 1`. Check the Microsoft Support page for the exact version list. |
| Google Sheets | Available | Arguments are `value1` and `value2`. Inputs must be given in decimal form. The help page lists no range limits. |

## Tips and Best Practices

- Keep flag values as powers of 2 (1, 2, 4, 8, 16) so each one maps to a single bit.
- Compare the result with the flag value, such as `=BITAND(B2, 4) = 4`, to get a clear yes or no.
- Store masks in decimal and use BIN2DEC only when the source system writes binary text.
- Put the flag values in labeled cells so a reader can see which right each bit stands for.
- Use BITOR to build a mask from several flags and BITAND to read it back.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts binary text to a decimal number before the bit test. |
| [BITLSHIFT](BITLSHIFT.md) | Moves bits left, which creates the flag values for each position. |
| [BITOR](BITOR.md) | Combines flags, the counterpart to the shared-bit test. |
| [BITRSHIFT](BITRSHIFT.md) | Moves bits right, which reads a flag from a higher position. |
| [BITXOR](BITXOR.md) | Returns the bits that differ between two numbers. |

## Official Documentation

- [Microsoft Support: BITAND function](https://support.microsoft.com/en-us/excel/functions/bitand-function)
- [Google Docs Editors Help: BITAND](https://support.google.com/docs/answer/9061440)
