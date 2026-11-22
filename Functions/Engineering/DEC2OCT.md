---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - File Permission Modes
  - Octal Bin Labels
related:
  - BIN2OCT
  - DEC2BIN
  - DEC2HEX
  - HEX2OCT
  - OCT2BIN
  - OCT2DEC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dec2oct-function
  - https://support.google.com/docs/answer/3093138
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Decimal to Octal
tags:
  - conversion
  - excel
  - number-base
  - octal
  - sheets
---

# DEC2OCT

## Description

**DEC2OCT** converts a whole decimal number into octal text, which uses only the digits 0 to 7. Octal is common in Unix-style file permissions, where each digit holds three permission bits, and in older systems that group bits in threes. The result is text, so convert it back with OCT2DEC before using it in arithmetic.

Excel accepts decimal values from -536,870,912 to 536,870,911. A positive value uses only as many digits as it needs, unless the optional `places` argument pads it with leading zeros. A negative value is written as a 10-character, 30-bit two's complement number, and `places` is ignored for it.

Use DEC2OCT when the target system expects octal output. For binary or hexadecimal output, use DEC2BIN or DEC2HEX.

## Syntax

```excel
=DEC2OCT(number, [places])
```

<!-- Image 1: Octal Digits and Place Values. See Images/Engineering/DEC2OCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole decimal number from -536,870,912 to 536,870,911. Values outside the range return `#NUM!`. |
| `places` | No | The number of characters in the result. Shorter results are padded with leading zeros. Non-integer values are truncated, and negative values return `#NUM!`. |

### Return Value

A text string of octal digits. The function returns `#NUM!` when `number` is outside its range, when `places` is negative, or when the result needs more characters than `places` allows. It returns `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Pad to Three Characters

```excel
=DEC2OCT(58,3)
```

**Result:** `072`

58 is 7 times 8 plus 2, so its octal form is 72. The `places` argument pads it to three characters.

### Example 2: Two's Complement for a Negative Value

```excel
=DEC2OCT(-100)
```

**Result:** `7777777634`

A negative value is written as a 10-character, 30-bit two's complement number. The `places` argument is ignored for negative values.

### Example 3: Small Value

```excel
=DEC2OCT(8)
```

**Result:** `10`

8 is one group of eight, so its octal form is 10.

### Example 4: Value With Full Octal Digits

```excel
=DEC2OCT(199)
```

**Result:** `307`

199 is 3 times 64, plus 0 times 8, plus 7, so the octal form is 307.

## Story Problems

### Problem 1: Permission Modes in Octal

A backup script records file permissions as decimal numbers, but the restore tool expects four-digit octal modes such as 0644. Each mode must keep its leading zero so the tool can read it.

| Permission Value |
| --- |
| 420 |
| 493 |
| 384 |

**Task:** Convert each decimal permission value in column A to a four-digit octal mode, starting at A2.

**Solution:**

```excel
=DEC2OCT(A2,4)
```

Enter this in B2 and fill it down to B4.

**Answer:** `0644`, `0755`, and `0600`. Each octal digit stands for one group (owner, group or others) and packs its read, write and execute bits, so 0644 gives the owner read and write and everyone else read only, while 0600 limits access to the owner.

### Problem 2: Octal Labels for Bin Units

A storage system numbers its units in decimal, but the labels printed on each unit use octal. Unit 73 needs three octal digits, and the largest unit, 511, is the top of the three-digit range.

| Unit |
| --- |
| 73 |
| 8 |
| 511 |

**Task:** Convert each unit number in column A to its octal label, starting at A2.

**Solution:**

```excel
=DEC2OCT(A2)
```

Enter this in B2 and fill it down to B4.

**Answer:** `111`, `10`, and `777`. Unit 73 is 1 times 64, plus 1 times 8, plus 1, and unit 511 is 7 times 64, plus 7 times 8, plus 7.

<!-- Image 2: Permission Modes Table. See Images/Engineering/DEC2OCT.md -->

## Use Cases

### File Permission Modes

**Scenario:** A deployment script writes numeric permission modes into a configuration file, and the target system needs them in octal.

```excel
=DEC2OCT(Files[Mode],4)
```

**Why It Works:** Padding to four characters keeps the leading zero that Unix tools expect. Verify each mode with OCT2DEC when the file is reviewed.

### Octal Bin Labels

**Scenario:** A warehouse prints octal labels on bins that are counted in decimal, and the labels must have a fixed width.

```excel
=DEC2OCT(B2,3)
```

**Why It Works:** Three characters cover the values from 0 to 511 with no truncation, so labels stay aligned on the printed sheet.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The number is outside the Excel range, or `places` is negative. | Check the input range and use a positive `places` value. |
| `#NUM!` | The result needs more characters than `places` allows. | Increase `places` to the length of the octal value. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Clean the source cell or convert it with `VALUE`. |
| Wrong result in later math | The octal text is used in arithmetic. | Convert it back with OCT2DEC before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Range from -536,870,912 to 536,870,911. The `places` argument pads the result. |
| Google Sheets | Available | Uses `significant_digits` for padding. The help page warns that Sheets can convert the octal text silently in later calculations. Check the value range on the help page before large inputs. |

## Tips and Best Practices

- Use a fixed `places` value for permission modes and labels, so the width does not change with the data.
- Keep the result as text, and convert it back with OCT2DEC before any arithmetic.
- Check the mode in OCT2DEC when you audit permissions, since a misread digit changes the access rights.
- Wrap the formula in IFERROR when a column may hold values outside the range, and flag those rows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2OCT](BIN2OCT.md) | Converts a binary string directly to octal. |
| [DEC2BIN](DEC2BIN.md) | Converts the same decimal value to binary. |
| [DEC2HEX](DEC2HEX.md) | Converts the same decimal value to hexadecimal. |
| [HEX2OCT](HEX2OCT.md) | Converts a hexadecimal string to octal. |
| [OCT2BIN](OCT2BIN.md) | Converts an octal string to binary. |
| [OCT2DEC](OCT2DEC.md) | Converts an octal string back to decimal before arithmetic. |

## Official Documentation

- [Microsoft Support: DEC2OCT function](https://support.microsoft.com/en-us/excel/functions/dec2oct-function)
- [Google Docs Editors Help: DEC2OCT](https://support.google.com/docs/answer/3093138)
