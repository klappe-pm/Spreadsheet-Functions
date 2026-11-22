---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Legacy Device Codes
  - Valve Control Codes
related:
  - BIN2DEC
  - BIN2HEX
  - DEC2OCT
  - OCT2BIN
  - OCT2DEC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bin2oct-function
  - https://support.google.com/docs/answer/3092993
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Binary To Octal
tags:
  - binary
  - excel
  - number-base
  - octal
  - sheets
---

# BIN2OCT

## Description

**BIN2OCT** converts a binary number to octal text. The input follows the same 10-bit rules as the other binary conversion functions: up to 10 characters, a leftmost sign bit, and two's complement for negative values.
Each octal digit stands for three bits, so an octal result is a compact way to show a binary code, which is why older equipment and control systems often list codes in octal.

Use BIN2OCT when a legacy device, a manual or a control table expresses codes in octal and the source data is binary. A negative input always returns a 10-character octal result, and the places argument is ignored for it.

The optional places argument pads the result with leading zeros to a fixed width. Only the digits 0 and 1 are valid input. A result that needs more digits than places allows returns `#NUM!`.

BIN2OCT is available in Microsoft Excel and Google Sheets. Google calls the second argument `significant_digits`.

## Syntax

```excel
=BIN2OCT(number, [places])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BIN2OCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The binary value to convert, up to 10 characters. A 10-character value with a leading 1 is negative. |
| `places` | No | The number of characters in the result, padded with leading zeros. Ignored for negative values. A non-integer is truncated, and a negative value returns `#NUM!`. |

### Return Value

An octal value as text, using the digits 0 to 7. The function returns `#NUM!` for invalid binary input or when the result is wider than `places` allows, and `#VALUE!` when `places` is not numeric.

## Examples

### Example 1: Padding to Three Characters

```excel
=BIN2OCT(1011, 3)
```

**Result:** `013`

The binary value is 11, which is 13 in octal. The places argument pads the result to three characters.

### Example 2: Without Padding

```excel
=BIN2OCT(101101)
```

**Result:** `55`

The binary value 101101 is 45 in decimal, which is 55 in octal.

### Example 3: Filled Down a Column

Codes in `A2:A4` are `1000`, `111` and `1100`.

```excel
=BIN2OCT(A2)
```

Fill the formula down to `B4`.

**Result:** `10` (A2), `7` (A3), `14` (A4)

Each code converts on its own row, so a list of mixed lengths converts in one step.

<!-- Image 2: Three-Bit Groups to Octal Digits. See Images/Engineering/BIN2OCT.md -->

### Example 4: Negative Input

```excel
=BIN2OCT(1000000000)
```

**Result:** `7777777000`

The input is -512 in 10-bit two's complement. Negative results always show 10 octal characters.

## Story Problems

### Problem 1: Valve Control Codes

A plant maintenance log stores valve position codes in binary. The older controller expects three-digit octal codes, so the team converts each one.

| Valve | Code |
| --- | --- |
| V1 | 1111 |
| V2 | 1010 |
| V3 | 110 |

**Task:** Put `=BIN2OCT(B2, 3)` in `C2`, fill it down to `C4`, and record the three results.

**Solution:**

```excel
=BIN2OCT(B2, 3)
```

**Answer:** V1 `017`, V2 `012` and V3 `006`.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BIN2OCT.md -->

### Problem 2: Checking a Mode Code

A test rig reports a mode code of `1111111110`, which the technician must convert to octal for the manual.

| Item | Value |
| --- | --- |
| Mode code | 1111111110 |

**Task:** Convert the mode code to octal.

**Solution:**

```excel
=BIN2OCT("1111111110")
```

**Answer:** `7777777776`. The input is -2 in 10-bit two's complement, shown as 10 octal characters.

## Use Cases

### Legacy Device Codes

**Scenario:** A technician maintains a list of device codes that a legacy controller reads only in octal, while the source system stores them in binary.

```excel
=BIN2OCT(Table1[DeviceBits], 3)
```

**Why It Works:** A fixed three-character width keeps every code aligned for the controller.
Dynamic array versions of Excel fill the whole column from one formula.

### Valve Control Codes

**Scenario:** A maintenance supervisor checks that each valve code in a logbook matches the octal value printed on the controller panel.

```excel
=IF(BIN2OCT(B2, 3)=C2, "Match", "Check")
```

**Why It Works:** Comparing the converted value with the panel value flags any mismatch quickly.
Both values must be text of the same width, so keep the places argument consistent.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a digit other than 0 or 1, or has more than 10 characters. | Clean the source text and remove any spaces or letters. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` or remove it. |
| `#VALUE!` | `places` is text. | Enter a number for the places argument. |
| Wrong arithmetic in Sheets | Octal results are read as decimal in later math. | Convert with OCT2DEC before doing arithmetic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365 and current Excel versions | Arguments are `number` and `places`. Check the Microsoft Support page for the exact version list. |
| Google Sheets | Available | Arguments are `signed_binary_number` and `significant_digits`. Results can be read as decimal numbers in later arithmetic, so convert them first. |

## Tips and Best Practices

- Set `places` to the width the target system expects so the codes stay aligned.
- Keep the binary source as text so leading zeros are preserved.
- Convert with OCT2DEC before doing arithmetic on an octal result.
- Use OCT2BIN to reverse the conversion when the target system needs binary again.
- Check negative results against their 10-character form before using them in a fixed-width field.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts the same binary value to decimal. |
| [BIN2HEX](BIN2HEX.md) | Converts the same binary value to hexadecimal. |
| [DEC2OCT](DEC2OCT.md) | Converts a decimal number to octal. |
| [OCT2BIN](OCT2BIN.md) | Converts octal text back to binary. |
| [OCT2DEC](OCT2DEC.md) | Converts octal text to decimal for arithmetic. |

## Official Documentation

- [Microsoft Support: BIN2OCT function](https://support.microsoft.com/en-us/excel/functions/bin2oct-function)
- [Google Docs Editors Help: BIN2OCT](https://support.google.com/docs/answer/3092993)
