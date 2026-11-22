---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
purpose:
  - Bitwise Operations
use-case:
  - Badge Code Decoding
  - Device Status Packing
related:
  - BIN2DEC
  - BITAND
  - BITLSHIFT
  - BITOR
  - BITXOR
  - DEC2BIN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/bitrshift-function
  - https://support.google.com/docs/answer/9084100
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bitwise Right Shift
  - Binary Right Shift
tags:
  - binary
  - bitwise
  - excel
  - sheets
---

# BITRSHIFT

## Description

**BITRSHIFT** moves the binary bits of a whole number to the right by a set number of places. Each place drops the rightmost bit and fills the left side with zeros, so shifting right by one place halves the value and drops any remainder. Use it to pull a packed field out of a larger number, such as the site code stored in the upper bits of a badge ID.

Excel accepts a `number` from 0 up to `(2^48)-1` and a `shift_amount` from -53 to 53. A negative shift amount moves the bits left instead, so `BITRSHIFT(3,-2)` returns the same result as `BITLSHIFT(3,2)`. Google Sheets documents a narrower shift range of -52 to 53 and a non-negative `value`, so check the limits before you copy a formula between the two platforms.

BITRSHIFT works best with BITAND. BITAND keeps only the bits you select, and BITRSHIFT then moves them down to the lowest position so the field reads as a plain number.

## Syntax

```excel
=BITRSHIFT(number, shift_amount)
```

<!-- Image 1: Bit Pattern Before and After a Right Shift. See Images/Engineering/BITRSHIFT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole number of 0 or more, up to `(2^48)-1`. Values above that limit return `#NUM!`. |
| `shift_amount` | Yes | A whole number from -53 to 53. Positive values shift right and negative values shift left. Values outside the range return `#NUM!`. |

### Return Value

A decimal number with the bits moved. Zeros fill the positions opened on the left, and bits pushed past the right edge are discarded. The function returns `#NUM!` when `number` or `shift_amount` is outside its limits and `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Shift a Small Number Right

```excel
=BITRSHIFT(13,2)
```

**Result:** `3`

13 is 1101 in binary. Removing the two rightmost bits leaves 11, which is 3 in decimal.

### Example 2: Divide by a Power of Two

```excel
=BITRSHIFT(8,2)
```

**Result:** `2`

8 is 1000 in binary. Shifting it right two places gives 10, which is 2. Each shifted place halves the value, so two places divide by 4 and drop the remainder.

### Example 3: Shift Left With a Negative Amount

```excel
=BITRSHIFT(3,-2)
```

**Result:** `12`

A negative shift amount moves the bits left. 3 is 11 in binary, and shifting it left two places gives 1100, which is 12. The same result comes from `BITLSHIFT(3,2)`.

### Example 4: Extract the Site Code From a Badge ID

```excel
=BITRSHIFT(A2,8)
```

**Result:** `101` when cell A2 holds the badge ID 25857

The site code sits in the upper eight bits of a 16-bit badge ID. Shifting right by eight places removes the lower eight bits, which hold the door code, and leaves the site code. Problem 1 below uses this formula on a full list.

## Story Problems

### Problem 1: Site Codes in Badge IDs

A building access system stores each badge as one 16-bit number. The upper eight bits hold the site code, and the lower eight bits hold the door code. The security office needs the site code for each badge so it can group access logs by site.

| Badge ID |
| --- |
| 25857 |
| 12290 |
| 4611 |
| 65281 |

**Task:** Calculate the site code for each badge ID in column A, starting at A2.

**Solution:**

```excel
=BITRSHIFT(A2,8)
```

Enter the formula in B2 and fill it down to B5.

**Answer:** `101`, `48`, `18`, and `255`, in row order. The last badge is 65281, which is 255 times 256 plus 1, so its site code is 255.

<!-- Image 2: Badge IDs Split Into Site and Door Fields. See Images/Engineering/BITRSHIFT.md -->

### Problem 2: Counting Full Carton Groups

A packing line stacks cartons in groups of four. Each row of the log shows the carton count for one shipment, and the clerk needs the number of complete groups of four in each shipment. Shifting right two places divides by four and drops any partial group.

| Shipment | Cartons |
| --- | --- |
| North | 37 |
| South | 52 |
| West | 19 |

**Task:** Count the complete groups of four cartons for each shipment in column B, starting at B2.

**Solution:**

```excel
=BITRSHIFT(B2,2)
```

Enter the formula in C2 and fill it down to C4.

**Answer:** `9`, `13`, and `4`. North has nine full groups with one carton left over, South has exactly 13 groups, and West has four groups with three cartons left over.

## Use Cases

### Badge Code Decoding

**Scenario:** A facility report needs the site code for every scan, but the access export contains only the packed 16-bit badge value.

```excel
=BITRSHIFT(Scans[Badge ID],8)
```

**Why It Works:** Shifting right by eight places discards the door code in the lower byte. In Excel 365 the formula spills one site code per row. Keep the shift amount in a labeled cell so the field width is visible to anyone reviewing the report.

### Device Status Packing

**Scenario:** A controller packs an alarm group into the upper bits of a status word, and a dashboard needs the group number alone.

```excel
=BITRSHIFT(B2,4)
```

**Why It Works:** Shifting right four places drops the lowest four bits, which hold the detail code. Combine it with `BITAND(B2,15)` to read the detail code, since 15 is the binary mask 1111.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number` is above `(2^48)-1`, or `shift_amount` is outside -53 to 53. | Check the input range and split very large values into smaller fields. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Clean the source column or convert it with `VALUE` before the shift. |
| Unexpected result | The shift amount is negative, so the bits moved left instead of right. | Use a positive shift amount for a right shift. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | `number` up to `(2^48)-1` and `shift_amount` from -53 to 53. |
| Google Sheets | Available | Documents a `shift_amount` range of -52 to 53 and a non-negative `value`. |

## Tips and Best Practices

- Use a right shift only as a division by a power of two, since `BITRSHIFT(x,n)` equals the whole part of `x` divided by `2^n` for non-negative values.
- Pair BITRSHIFT with BITAND to read one field: BITAND keeps the bits, and BITRSHIFT moves them down.
- Put the shift amount in a labeled input cell so the field width is visible.
- Check a sample value with DEC2BIN before you build the formula, so the bit positions match the layout in the specification.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BIN2DEC](BIN2DEC.md) | Converts a binary text value to decimal before shifting. |
| [BITAND](BITAND.md) | Keeps selected bits, usually combined with a right shift. |
| [BITLSHIFT](BITLSHIFT.md) | Moves bits left, the opposite direction. |
| [BITOR](BITOR.md) | Sets bits in a value, the bitwise OR counterpart. |
| [BITXOR](BITXOR.md) | Flags the bits that differ between two values. |
| [DEC2BIN](DEC2BIN.md) | Displays a shifted result as a binary string. |

## Official Documentation

- [Microsoft Support: BITRSHIFT function](https://support.microsoft.com/en-us/excel/functions/bitrshift-function)
- [Google Docs Editors Help: BITRSHIFT](https://support.google.com/docs/answer/9084100)
