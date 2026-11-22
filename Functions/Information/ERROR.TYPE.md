---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
purpose:
  - Error Handling
  - Type Checking
use-case:
  - Error Code Logging
  - Labeled Error Dashboards
related:
  - CHOOSE
  - IFERROR
  - ISERR
  - ISERROR
  - ISNA
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/error-type-function
  - https://support.google.com/docs/answer/3238305
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - error-codes
  - error-handling
  - excel
  - sheets
---

# ERROR.TYPE

## Description

**ERROR.TYPE** returns a number that identifies which error a cell contains. A `#DIV/0!` error returns 2, a `#N/A` error returns 7, and so on. The number is easier to store in a log, compare in a formula or map to a plain-language label than the error text itself.

Use ERROR.TYPE when a report needs to say what kind of error occurred, not only that one occurred. ISERROR and ISERR answer a yes or no question. ERROR.TYPE answers the follow-up question of which error it was. Pair it with CHOOSE to turn the number into a label, or with IF to route different errors to different owners.

Pass a cell reference rather than typing the error into the formula. The function returns the error number for the value in the referenced cell. Microsoft documents a `#N/A` result when the input is not an error, which lets you tell a clean cell apart from a failing one. Google Sheets maps all errors that are not in its list to the number 8, while Excel returns `#N/A` for anything outside its list. See Platform Differences before you rely on the number for unusual errors.

## Syntax

```excel
=ERROR.TYPE(error_val)
```

<!-- Image 1: Error Number Table. See Images/Information/ERROR.TYPE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `error_val` | Yes | The error value to identify. Usually a reference to a cell that contains an error or a formula that can return one. In Excel you can also type an error value directly, such as `#N/A`. |

### Return Value

A number from 1 to 8 that matches the error type, as listed in the table below. Excel returns `#N/A` when the input is not an error or is an error outside its list. Google Sheets returns 8 for any other error.

| Error | Number |
| --- | --- |
| `#NULL!` | 1 |
| `#DIV/0!` | 2 |
| `#VALUE!` | 3 |
| `#REF!` | 4 |
| `#NAME?` | 5 |
| `#NUM!` | 6 |
| `#N/A` | 7 |
| `#GETTING_DATA` | 8 |

## Examples

### Example 1: Identifying a Division Error

Cell A1 contains the formula `=1/0`, which returns `#DIV/0!`.

```excel
=ERROR.TYPE(A1)
```

**Result:** `2`

The number 2 matches `#DIV/0!` in the table.

### Example 2: Identifying a Missing Lookup

```excel
=ERROR.TYPE(NA())
```

**Result:** `7`

`NA()` produces the `#N/A` error, which is the value that lookup functions return when no match exists.

### Example 3: Turning the Number Into a Label

```excel
=CHOOSE(ERROR.TYPE(A1), "Null", "Division by zero", "Value", "Reference", "Name", "Number", "Not available")
```

**Result:** `Division by zero`

ERROR.TYPE returns 2 for cell A1, and CHOOSE returns the second label in the list.

### Example 4: Checking a Cell With No Error

Cell A2 contains the text `Paid`, which is not an error.

```excel
=ERROR.TYPE(A2)
```

**Result:** `#N/A`

Microsoft documents that the function returns `#N/A` when no error exists in the reference. Wrap it in IF(ISERROR(A2), ERROR.TYPE(A2), "No error") to show a clear message instead.

## Story Problems

### Problem 1: Finding the Cause of a Failed Lookup

A price sheet shows the result of a lookup in column B.

| Item | Result |
| --- | --- |
| Bolt | 0.25 |
| Nut | `#N/A` |
| Washer | `#DIV/0!` |

**Task:** Put a formula in C2 that returns the error number for the Nut result in B2.

**Solution:**

```excel
=ERROR.TYPE(B2)
```

**Answer:** `7`. The `#N/A` error means the lookup did not find the item. The number 7 is the code for `#N/A` in the table.

### Problem 2: Labeling Errors in a Daily Report

A report cell B5 shows a broken link to another sheet, which produces `#REF!`.

**Task:** Put a formula in C5 that returns the plain-language label for the error in B5.

**Solution:**

```excel
=CHOOSE(ERROR.TYPE(B5), "Null", "Division by zero", "Value", "Reference", "Name", "Number", "Not available")
```

**Answer:** `Reference`. The `#REF!` error returns 4, and the fourth label in the list is Reference.

## Use Cases

### Error Code Logging

**Scenario:** A finance team records errors from a monthly close workbook in a log so the owner of each error type can review it.

```excel
=ERROR.TYPE(Close!C14)
```

**Why It Works:** A number is easy to filter and count in a log table. Keep a legend sheet that maps each number to its meaning so reviewers do not have to memorize the list.

### Labeled Error Dashboards

**Scenario:** A sales dashboard shows a status column that should read clearly for managers who do not read formulas.

```excel
=IFERROR(CHOOSE(ERROR.TYPE(B2), "Null", "Division by zero", "Value", "Reference", "Name", "Number", "Not available"), "OK")
```

**Why It Works:** IFERROR returns `OK` for cells without an error. For cells with an error, CHOOSE turns the code into a label, so the dashboard shows readable text instead of raw error codes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` from ERROR.TYPE | The referenced cell does not contain an error. | Test with ISERROR first, or wrap the call in IF to show a message for clean cells. |
| Unexpected `8` in Google Sheets | The error is not in the documented list, so Sheets returns the catch-all code. | Read the error text directly with a separate check, or treat 8 as other. |
| `#VALUE!` in a CHOOSE label | CHOOSE received a code outside its label list, such as 8 when only seven labels are given. | Supply a label for every code from 1 to 8, or wrap the call in IFERROR. |
| Confusion about `#N/A` | Microsoft uses 7 for `#N/A`, and a clean cell also returns `#N/A`. | Check for an error first with ISERROR, then read the code. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel for the web | Returns 1 to 8 for the listed errors, `#GETTING_DATA` included. Returns `#N/A` for any other input. |
| Google Sheets | Available | Returns 1 to 7 for the listed errors and 8 for all other errors. The documentation does not describe a result for non-error input. |

## Tips and Best Practices

- Pass a cell reference instead of a typed error value so the formula follows the cell.
- Keep the number-to-label mapping in one place, such as a legend range, so every report uses the same wording.
- Test with ISERROR before calling ERROR.TYPE when the cell may be clean.
- Use ISNA when only the `#N/A` case matters, and ERROR.TYPE when the team needs the full error type.
- Check results in both Excel and Google Sheets if the workbook is shared across platforms.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSE](../Lookup%20%26%20Reference/CHOOSE.md) | Turns the error number into a readable label. |
| [IFERROR](../Logical/IFERROR.md) | Replaces an error with a fallback value, without identifying it. |
| [ISERR](ISERR.md) | Tests for any error except `#N/A`, and returns TRUE or FALSE. |
| [ISERROR](ISERROR.md) | Tests for any error, including `#N/A`, and returns TRUE or FALSE. |
| [ISNA](ISNA.md) | Tests only for the `#N/A` error. |

## Official Documentation

- [Microsoft Support: ERROR.TYPE function](https://support.microsoft.com/en-us/excel/functions/error-type-function)
- [Google Docs Editors Help: ERROR.TYPE](https://support.google.com/docs/answer/3238305)
