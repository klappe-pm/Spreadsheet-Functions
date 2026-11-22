---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
purpose:
  - Bitwise Operations
use-case:
  - Feature Flag Comparison
  - Sensor Change Detection
related:
  - BITAND
  - BITLSHIFT
  - BITOR
  - BITRSHIFT
  - DEC2BIN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/bitxor-function
  - https://support.google.com/docs/answer/9083935
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bitwise Exclusive Or
  - Bitwise XOR
tags:
  - binary
  - bitwise
  - excel
  - sheets
---

# BITXOR

## Description

**BITXOR** compares two whole numbers bit by bit and returns a new number whose bits are 1 wherever the two inputs differ and 0 wherever they match. It is the bitwise "exclusive or" operation. Use it to find which flags, switches or sensors changed between two snapshots, because the bits that come back as 1 mark exactly the positions that differ.

The arguments are whole numbers from 0 up to `(2^48)-1` in Excel. Google Sheets coerces the inputs to numbers, so the text "3" and the logical value TRUE are read as 3 and 1. The order of the two arguments does not change the result, since XOR is symmetric.

BITXOR is the right tool for comparing bit patterns. For a plain numeric difference, use subtraction, because BITXOR does not tell you how far apart two numbers are.

## Syntax

```excel
=BITXOR(number1, number2)
```

<!-- Image 1: Bit-by-Bit Comparison of Two Values. See Images/Engineering/BITXOR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first whole number, from 0 up to `(2^48)-1`. Negative values return `#NUM!`. |
| `number2` | Yes | The second whole number, from 0 up to `(2^48)-1`. Negative values return `#NUM!`. |

### Return Value

A decimal number that holds the bits where the two inputs differ. The function returns `#NUM!` when an argument is negative or above `(2^48)-1`, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Compare Two Small Values

```excel
=BITXOR(5,3)
```

**Result:** `6`

5 is 101 in binary and 3 is 011. Bits in positions 2 and 1 differ, and position 0 matches, so the result is 110, which is 6.

### Example 2: Values Given in Different Order

```excel
=BITXOR(2,4)
```

**Result:** `6`

2 is 010 and 4 is 100. Every bit that is set in only one value appears in the result, giving 110. Swapping the arguments to `BITXOR(4,2)` returns the same 6.

### Example 3: Bits That Match Cancel Out

```excel
=BITXOR(9,5)
```

**Result:** `12`

9 is 1001 and 5 is 0101. The two leftmost bits differ, and the two rightmost bits match. The result is 1100, which is 12, because matching bits drop out.

### Example 4: Compare Two Cells

```excel
=BITXOR(B2,C2)
```

**Result:** `5` when B2 holds 22 and C2 holds 19

The formula returns the bits that changed between the previous and current status masks. The story problem below applies the same formula to a full list.

## Story Problems

### Problem 1: Sensor Status Changes

A conveyor has five sensors, and each one is stored as a bit in a status mask: 1 means the sensor is on and 0 means it is off. The maintenance team compares the mask at the start and end of each shift to see which sensors switched state.

| Line | Previous Mask | Current Mask |
| --- | --- | --- |
| Line 1 | 22 | 19 |
| Line 2 | 31 | 31 |
| Line 3 | 8 | 24 |

**Task:** Find the bits that changed for each line, starting from the Line 1 row at B2 and C2, and write the result in column D.

**Solution:**

```excel
=BITXOR(B2,C2)
```

Enter the formula in D2 and fill it down to D4.

**Answer:** `5`, `0`, and `16`. Line 1 changed bits 0 and 2 (5 is 00101). Line 2 changed nothing. Line 3 changed bit 4 only (16 is 10000).

### Problem 2: Comparing Two Batch Codes

A scanner records an 8-bit code for each batch on two production lines. A batch code that matches on both lines should return 0. Any other pairing returns the bits that differ, which the quality team uses to locate the fault.

| Batch | Line A Code | Line B Code |
| --- | --- | --- |
| Batch 101 | 170 | 85 |
| Batch 102 | 60 | 60 |
| Batch 103 | 96 | 33 |

**Task:** Calculate the differing bits for each batch, starting from the Batch 101 row at B2 and C2, and write the results in column D.

**Solution:**

```excel
=BITXOR(B2,C2)
```

Enter the formula in D2 and fill it down to D4.

**Answer:** `255`, `0`, and `65`. Batch 101 differs in all eight bits, batch 102 matches exactly, and batch 103 differs in bits 0 and 6 (65 is 01000001).

<!-- Image 2: Sensor Masks and Changed Bits Table. See Images/Engineering/BITXOR.md -->

## Use Cases

### Sensor Change Detection

**Scenario:** A monitoring report must list only the sensors whose state changed since the last reading.

```excel
=BITXOR(B2,C2)
```

**Why It Works:** Each 1 in the result marks a sensor whose bit flipped between the two masks. Pair the result with BITAND against the current mask to show whether each changed sensor turned on or off.

### Feature Flag Comparison

**Scenario:** A release team compares two feature-flag settings stored as bit masks to see which features differ between staging and production.

```excel
=BITXOR(staging_flags,production_flags)
```

**Why It Works:** A result of 0 means the environments match exactly. Any other result identifies the flags that differ, and BITAND with each flag value shows which environment enabled them.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | An argument is negative or above `(2^48)-1`. | Check the inputs or convert signed values to their unsigned form before comparing. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Clean the source cells or convert them with `VALUE`. |
| Unexpected result | The inputs are decimal numbers that were meant to be binary strings. | Convert binary text with BIN2DEC before calling BITXOR. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Arguments from 0 up to `(2^48)-1`. Non-numeric input returns `#VALUE!`. |
| Google Sheets | Available | Arguments are coerced to numbers, so text such as "3" and TRUE work. The help page does not state a numeric limit. |

## Tips and Best Practices

- Store each flag or sensor in its own bit position and document the positions beside the sheet.
- Compare a result to 0 to test for an exact match of two masks.
- Use BITAND with the XOR result to see which side of the comparison holds each changed bit.
- Build the mask with BITLSHIFT when you need to set a specific bit, such as `BITLSHIFT(1,4)` for bit 4.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BITAND](BITAND.md) | Keeps only the bits that both values share. |
| [BITLSHIFT](BITLSHIFT.md) | Builds a mask by moving a bit to a chosen position. |
| [BITOR](BITOR.md) | Combines bits from both values, the opposite of a change check. |
| [BITRSHIFT](BITRSHIFT.md) | Moves a changed field down to a readable number. |
| [DEC2BIN](DEC2BIN.md) | Shows the XOR result as a binary string for review. |

## Official Documentation

- [Microsoft Support: BITXOR function](https://support.microsoft.com/en-us/excel/functions/bitxor-function)
- [Google Docs Editors Help: BITXOR](https://support.google.com/docs/answer/9083935)
