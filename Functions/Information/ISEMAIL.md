---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Contact List Cleanup
  - Signup Form Validation
related:
  - COUNTIF
  - ISBLANK
  - ISDATE
  - ISTEXT
  - SEARCH
level: 2
source:
  - https://support.google.com/docs/answer/3256503
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - data-validation
  - email-validation
  - sheets
  - type-checks
---

# ISEMAIL

## Description

**ISEMAIL** checks whether a value follows a commonly accepted email address format. It returns TRUE when the text has the shape of an address, such as a name, an at sign and a domain, and FALSE when it does not.

Use ISEMAIL to catch typing mistakes in a contact list or a signup form before the addresses are used. It is a format check only. It does not confirm that the mailbox exists, that the domain accepts mail or that the person who typed the address owns it. A TRUE result means the text looks right, not that the message will arrive.

Google does not publish the full rules that ISEMAIL applies, so do not rely on it for edge cases such as unusual characters or very long addresses. Trim stray spaces from imported text with TRIM before you test the values. ISEMAIL is available in Google Sheets only.

## Syntax

```excel
=ISEMAIL(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISEMAIL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The text to test. Put the address in quotation marks, or pass a cell reference such as `B2`. |

### Return Value

TRUE when the value follows the accepted email format. FALSE when it does not, for example when the at sign is missing. The function does not check whether the address exists.

## Examples

### Example 1: Standard Address

```excel
=ISEMAIL("sam.lee@example.com")
```

**Result:** `TRUE`

The text has a name, an at sign and a domain, so it follows the accepted shape.

### Example 2: Missing At Sign

```excel
=ISEMAIL("sam.lee.example.com")
```

**Result:** `FALSE`

Without the at sign, the text cannot be an email address, so the test returns FALSE.

### Example 3: Checking a Cell

Cell B2 holds the address `lee@club.org`.

```excel
=ISEMAIL(B2)
```

**Result:** `TRUE`

Pass a cell reference to test whatever the user typed there.

<!-- Image 2: Email Check Results. See Images/Information/ISEMAIL.md -->

### Example 4: Labeling Each Row

Cell B3 holds the text `kim.club.org`.

```excel
=IF(ISEMAIL(B3), "OK", "Check address")
```

**Result:** `Check address`

The IF formula turns the test into a label that a reviewer can filter.

### Example 5: Trimming Before the Test

Cell B4 holds `  dee@mail.net ` with stray spaces.

```excel
=ISEMAIL(TRIM(B4))
```

**Result:** `TRUE`

TRIM removes the leading and trailing spaces, so the test sees the address itself.

## Story Problems

### Problem 1: Cleaning a Contact List

A contact list has four rows with an email address in column B.

| Name | Email |
| --- | --- |
| Ana | ana@studio.org |
| Ben | ben.studio.org |
| Cy | cy@mail.net |
| Dee | dee at mail.net |

**Task:** Put `=ISEMAIL(B2)` in C2, fill it down to row 5, and count the TRUE results in C2:C5.

**Solution:**

```excel
=COUNTIF(C2:C5, TRUE)
```

**Answer:** `2`. Ana and Cy have an at sign and a domain. Ben has no at sign and Dee wrote the at sign as words.

### Problem 2: Flagging a Signup Entry

A signup sheet collects one address per row in column A. Two entries are `lee@club.org` and `kim.club.org`.

**Task:** Put a formula in B2 that returns `OK` when A2 passes the check and `Missing @` otherwise, then fill it down to row 3.

**Solution:**

```excel
=IF(ISEMAIL(A2), "OK", "Missing @")
```

**Answer:** Row 2 shows `OK`. Row 3 shows `Missing @`, because the address has no at sign.

## Use Cases

### Signup Form Validation

**Scenario:** A community group collects signups in a shared sheet, and the welcome emails fail when someone types an address without an at sign.

```excel
=IF(ISEMAIL(C2), "", "Ask for correct address")
```

**Why It Works:** The reminder appears next to the entry, so the organizer can ask for the address before the welcome email is sent.

### Contact List Cleanup

**Scenario:** A sales team imports three lists with email addresses from different sources, and it wants to count how many rows need repair before the import.

```excel
=COUNTIF(D2:D500, FALSE)
```

**Why It Works:** When column D holds `ISEMAIL` results for each row, COUNTIF gives the number of rows that failed the format check.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| FALSE for a real address | The text has stray spaces or characters the check does not accept. | Trim the text and review unusual characters. |
| TRUE for a mailbox that does not exist | ISEMAIL checks format only. | Confirm addresses with a separate process before sending. |
| Single result for a column | ISEMAIL returns one result per value. | Fill the formula down, or use ARRAYFORMULA with a range. |
| Wrong count | The result column holds text, not logical values. | Make sure the formula returns TRUE or FALSE, or count the label instead. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Closest alternative: `=ISNUMBER(SEARCH("@", B2))`, which checks only that an at sign exists. |
| Google Sheets | Available | Checks a commonly accepted format. It does not check that the address exists. |

## Tips and Best Practices

- Use TRIM on imported text before you run the check.
- Treat TRUE as "the format looks right" and keep a separate confirmation step for important mailings.
- Label rows with IF so the results are easy to filter and fix.
- Combine ISEMAIL with ISBLANK so empty cells are not reported as bad addresses.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts the TRUE or FALSE results of ISEMAIL across a column. |
| [ISBLANK](ISBLANK.md) | Tests for an empty cell, which should be handled before the format check. |
| [ISDATE](ISDATE.md) | Tests whether a value is a date. |
| [ISTEXT](ISTEXT.md) | Tests whether a value is text. |
| [SEARCH](../Text/SEARCH.md) | Finds the position of a character, such as the at sign, in text. |

## Official Documentation

- [Google Docs Editors Help: ISEMAIL](https://support.google.com/docs/answer/3256503)
