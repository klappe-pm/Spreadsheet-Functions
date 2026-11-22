---
domain: Spreadsheet Functions
category: Add-in & Automation
subcategory: Add-in Functions
purpose:
  - Add-in Automation
use-case:
  - Add-in Diagnostics
  - Legacy Library Registration
  - Registration Audits
related:
  - CALL
  - IFERROR
  - ISERROR
  - ISNUMBER
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/register-id-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Register DLL Procedure
  - Register Procedure ID
tags:
  - add-in
  - dll
  - excel
  - registration
---

# REGISTER.ID

## Description

**REGISTER.ID** registers a procedure from a dynamic link library (DLL) or code resource and returns its register ID. The ID is the number that the first form of CALL uses to run the procedure. If the procedure was not registered before, REGISTER.ID registers it first and then returns the ID.

Unlike REGISTER, REGISTER.ID works in worksheet cells. Store the returned ID in a labeled cell, and CALL formulas can reuse it without registering the procedure again.

Microsoft's page documents the Windows syntax only. Excel for Windows and Excel for the Macintosh use different code resource types, so the syntax differs slightly between them. The page also warns that incorrect registry edits can severely damage the operating system, so back up your data before any registry work.

## Syntax

```excel
=REGISTER.ID(module_text, procedure, [type_text])
```

<!-- Image 1: Register ID in a Cell. See Images/Add-in & Automation/REGISTER.ID.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `module_text` | Yes | Text with the name of the DLL that contains the procedure. Microsoft describes this form for Excel for Windows. |
| `procedure` | Yes | Text with the procedure name, or the procedure's ordinal number from the EXPORTS statement of its .DEF file. The ordinal must be a number, not text. |
| `type_text` | No | Text whose first letter gives the return data type and whose remaining letters give the data type of each argument. You can omit it when the procedure is already registered. |

### Return Value

The register ID of the procedure, a number that CALL uses. If the procedure was not registered before, the function registers it first and then returns the ID. Microsoft's page lists no error values for this function.

## Examples

### Example 1: Register a Windows Procedure

In `A5`:

```excel
=REGISTER.ID("Kernel32", "GetTickCount", "J!")
```

**Result:** A register ID number. Microsoft's page does not state the value.

<!-- Image 2: Register and Reuse Layout. See Images/Add-in & Automation/REGISTER.ID.md -->

### Example 2: Reuse the Registered Procedure

In `B5`:

```excel
=REGISTER.ID("Kernel32", "GetTickCount")
```

**Result:** The same ID as `A5`.

Because the procedure is already registered, this formula can omit `type_text`.

### Example 3: Check the Registration

```excel
=IF(ISNUMBER(A5), "Registered", "Register the procedure first")
```

**Result:** `Registered` when `A5` holds a number.

## Story Problems

### Problem 1: Counting Registered Procedures

A help desk keeps a log of the procedures a workbook registers. Column C holds each register ID, and a blank cell marks a registration that did not complete. The log sits in `A1:C5`.

| Module | Procedure | Register ID |
| --- | --- | --- |
| Tools.dll | ExportRows | 14 |
| Tools.dll | ImportRows | 15 |
| Reports.dll | BuildTotals | |
| Reports.dll | SortLines | 22 |

**Task:** Count how many procedures have a register ID.

**Solution:**

```excel
=COUNT(C2:C5)
```

**Answer:** `3`, because three of the four cells hold numbers (14, 15 and 22).

<!-- Image 3: Results Panel for the Story Problems. See Images/Add-in & Automation/REGISTER.ID.md -->

### Problem 2: Showing a Label When Registration Fails

A macro team wants a register ID for the procedure named in `A2` and `B2`, or a clear label when registration fails. Microsoft's page does not list error values, so the formula catches any error.

**Task:** Write a formula in `D2` that returns the register ID, or `Not registered` when the formula returns an error.

**Solution:**

```excel
=IFERROR(REGISTER.ID(A2, B2), "Not registered")
```

**Answer:** A registration that succeeds returns its ID. A registration that returns an error shows `Not registered`. The page does not list which errors occur, so the result for a specific failing DLL cannot be stated here.

## Use Cases

### Add-in Diagnostics

**Scenario:** An IT team checks that each procedure in a configuration sheet has registered before a workbook is released.

```excel
=IF(ISNUMBER(C2), "OK", "Check registration")
```

**Why It Works:** A registered procedure returns a number, so ISNUMBER separates successful rows from blank or error rows.

### Legacy Library Registration

**Scenario:** A sales workbook stores the register ID of a hypothetical in-house DLL that formats quotes, so that many CALL formulas can reuse one registration.

```excel
=REGISTER.ID("QuoteTools.dll", "FormatQuote", "J")
```

**Why It Works:** Storing the result in one cell lets every CALL formula point to the same registration. The type text `"J"` follows the pattern in Microsoft's examples, so confirm the codes for your procedure.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Misspelled names | The module or procedure text does not match the DLL. | Check the spelling against the DLL's export list. |
| Ordinal rejected | The ordinal number was entered in quotation marks. | Enter the ordinal as a number. |
| Wrong return type | The first letter of `type_text` does not match the procedure's return type. | Set the first letter to the procedure's return type. |
| Macintosh syntax fails | The Windows form was used on a Mac. | Check Microsoft's Macintosh notes, because the page covers only the Windows syntax. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016, Excel for the web and Excel on mobile devices. | Windows and Macintosh use different code resource types, so the syntax differs. The page gives only the Windows form. |
| Google Sheets | Not available | The closest alternative is Google Apps Script, which can run custom code but cannot load Windows DLLs. |

## Tips and Best Practices

- Store the register ID in a labeled cell and point CALL formulas at that cell.
- Omit `type_text` only when the procedure is already registered, as Example 2 shows.
- Test each registration in a copy of the workbook before you share it.
- Back up before any registry work, because incorrect edits can severely damage the operating system.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CALL](CALL.md) | Runs the procedure that the register ID identifies. |
| [IFERROR](../Logical/IFERROR.md) | Shows a fallback label when registration returns an error. |
| [ISERROR](../Information/ISERROR.md) | Tests a result for any error value. |
| [ISNUMBER](../Information/ISNUMBER.md) | Confirms that a register ID is a number. |

## Official Documentation

- [Microsoft Support: REGISTER.ID function](https://support.microsoft.com/en-us/excel/functions/register-id-function)
