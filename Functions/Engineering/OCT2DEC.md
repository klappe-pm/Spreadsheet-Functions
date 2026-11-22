---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Legacy Device Address Lookup
  - Octal Register Readouts
related:
  - BIN2DEC
  - CONVERT
  - DEC2OCT
  - HEX2DEC
  - OCT2BIN
  - OCT2HEX
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oct2dec-function
  - https://support.google.com/docs/answer/3093146
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Octal to Decimal
tags:
  - base-conversion
  - decimal
  - excel
  - octal
  - sheets
---

# OCT2DEC

## Description

**OCT2DEC** converts an octal (base 8) number to decimal (base 10). Octal uses the digits 0 to 7, and each position is worth a power of 8, so octal 75 means 7 times 8 plus 5, which is 61. The result is an ordinary number that can be used in later calculations.

Use OCT2DEC when values come from older systems, such as register dumps, file permission masks or device codes that are documented in octal, and the team needs to add, compare or look up the values in decimal. Use OCT2BIN when the output must be a bit pattern, and use OCT2HEX when the output must be hexadecimal. DEC2OCT performs the reverse conversion.

OCT2DEC reads signed 30-bit octal values. The most significant bit is the sign bit, and negative values use two's-complement notation. A 10-digit octal value that starts with 4 through 7 is therefore negative, so `7777777760` returns -16 rather than a large positive number.

## Syntax

```excel
=OCT2DEC(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/OCT2DEC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The octal number to convert. It may not contain more than 10 octal characters (30 bits). Digits must be 0 to 7. Google Sheets calls this argument `signed_octal_number`. |

### Return Value

A decimal number. Positive inputs return a positive number and negative inputs return a negative number. The function returns `#NUM!` when the input is not a valid octal number, such as a value that contains the digit 8 or 9.

## Examples

### Example 1: Basic Conversion

```excel
=OCT2DEC(75)
```

**Result:** `61`

Octal 75 is 7 times 8 plus 5, which equals 61 in decimal.

### Example 2: A Power of Eight

```excel
=OCT2DEC(400)
```

**Result:** `256`

Octal 400 is 4 times 8 times 8, which is 256 in decimal.

<!-- Image 2: Octal Digit Place Values. See Images/Engineering/OCT2DEC.md -->

### Example 3: Negative Value in Two's Complement

```excel
=OCT2DEC(7777777760)
```

**Result:** `-16`

The 10-digit octal value has its sign bit set, so the function returns the negative number that the 30-bit pattern represents.

### Example 4: Converting a Cell Value

```excel
=OCT2DEC(B2)
```

**Result:** `127` (with B2 holding `177`)

Octal 177 is 1 times 64 plus 7 times 8 plus 7, which equals 127. The same result comes from typing the value as text, such as `"177"`.

## Story Problems

### Problem 1: Total Bin Counts From Octal Codes

A warehouse labels its bins with octal codes. Three bins are listed in `B2:B4` with the number of items each holds, written in octal. The manager needs the total number of items in decimal.

| Bin | Octal Count |
| --- | --- |
| Bin A | 62 |
| Bin B | 145 |
| Bin C | 17 |

**Task:** Convert each octal count to decimal and add the three values. Enter the total formula in `E2`.

**Solution:**

```excel
=OCT2DEC(B2)+OCT2DEC(B3)+OCT2DEC(B4)
```

**Answer:** `166`. The counts are 50, 101 and 15 in decimal, and 50 plus 101 plus 15 equals 166.

### Problem 2: Negative Sensor Offset

A data logger stores a sensor offset as the octal value `7777777600` in `B2`. The offset is signed, so the decimal form must be negative for the correction formula to work.

| Sensor | Octal Offset |
| --- | --- |
| Humidity Probe | 7777777600 |

**Task:** Convert the stored offset to decimal.

**Solution:**

```excel
=OCT2DEC(B2)
```

**Answer:** `-128`. Octal 7777777600 is the 30-bit two's-complement form of -128.

## Use Cases

### Legacy Device Address Lookup

**Scenario:** An automation team receives device addresses in octal from an older controller and needs the decimal address to match a lookup table.

```excel
=XLOOKUP(OCT2DEC(B2), DecimalAddresses, DeviceNames)
```

**Why It Works:** The conversion produces a number that matches the decimal column of the lookup table, so the device name can be found in one formula.

### Octal Register Readouts

**Scenario:** A technician copies register values from a diagnostic printout, where each value is written in octal, and needs to check them against decimal limits.

```excel
=IF(OCT2DEC(B2)>100,"Above Limit","Within Limit")
```

**Why It Works:** Converting first lets the comparison work on a true number. Comparing the raw octal text would give wrong results.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input contains a digit other than 0 to 7, such as 8 or 9. | Check the source data for typing errors. |
| `#NUM!` | The input has more than 10 octal characters. | Confirm that the value is a 30-bit octal number. |
| Unexpected negative result | The input has its sign bit set, for example a value that starts with 7. | Read the value as a signed 30-bit number, or treat it as a positive magnitude if the source is unsigned. |
| Unexpected result | The value was typed as decimal. | Confirm the source base, or use a decimal value directly. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Argument name is number. Input may not contain more than 10 octal characters. |
| Google Sheets | Available | Argument name is signed_octal_number. Positive inputs go up to 3777777777 (octal) and negative inputs down to 4000000000 (octal). Accepts numbers or text. |

## Tips and Best Practices

- Store octal values as text when leading zeros or digits matter, so they are not changed by the spreadsheet.
- Check every input for digits 8 and 9 before converting a column.
- Combine OCT2DEC with DEC2HEX or DEC2BIN when a second base is needed for display.
- Use CONVERT for units of measure, not for number bases; OCT2DEC is the function for base conversion.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts binary to decimal. |
| [CONVERT](CONVERT.md) | Converts measurement units, which is a different job from number base conversion. |
| [DEC2OCT](DEC2OCT.md) | Converts decimal to octal, the reverse direction. |
| [HEX2DEC](HEX2DEC.md) | Converts hexadecimal to decimal. |
| [OCT2BIN](OCT2BIN.md) | Converts octal to binary. |
| [OCT2HEX](OCT2HEX.md) | Converts octal to hexadecimal. |

## Official Documentation

- [Microsoft Support: OCT2DEC function](https://support.microsoft.com/en-us/excel/functions/oct2dec-function)
- [Google Docs Editors Help: OCT2DEC](https://support.google.com/docs/answer/3093146)
