---
domain: Spreadsheet Functions
category: Add-in & Automation
subcategory: Add-in Functions
purpose:
  - Add-in Automation
use-case:
  - Legacy Library Integration
  - Machine Uptime Reports
related:
  - IFERROR
  - ISERROR
  - ISNUMBER
  - REGISTER.ID
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/call-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Call Code Resource
  - Call DLL Procedure
tags:
  - add-in
  - automation
  - dll
  - excel
---

# CALL

## Description

**CALL** runs a procedure from a dynamic link library (DLL) or a code resource, such as an XLL add-in, and returns the value that the procedure returns. It reaches Windows and third-party routines that Excel has no built-in function for, such as the system timer used in the examples below.

The function has two forms. The first form takes a register ID from REGISTER.ID (or the older REGISTER function) and calls a code resource that is already registered. The second form names the DLL and procedure directly and registers and calls them in one step. When a workbook calls the same procedure many times, register it once with REGISTER.ID and store the ID in a cell.

CALL is an advanced function. Microsoft warns that incorrect use can cause errors that require you to restart the computer, and the function is not available in Excel for the web. Test every new CALL formula in a copy of the workbook before you share it.

## Syntax

```excel
=CALL(register_id, [argument1], ...)
```

```excel
=CALL(module_text, procedure, type_text, [argument1], ...)
```

<!-- Image 1: Two Forms of CALL. See Images/Add-in & Automation/CALL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `register_id` | Yes (first form) | The number that REGISTER.ID or REGISTER returned for a procedure that is already registered. |
| `module_text` | Yes (second form) | Text with the name of the DLL that contains the procedure. Microsoft describes this form for Excel for Windows. |
| `procedure` | Yes (second form) | Text with the procedure name in the DLL, or the procedure's ordinal number from the EXPORTS statement of its .DEF file. The ordinal must be a number, not text. |
| `type_text` | Yes (second form, see note) | Text whose first letter gives the data type of the return value and whose remaining letters give the data type of each argument. For a stand-alone DLL or XLL, Microsoft says this argument can be omitted. |
| `argument1, ...` | No | The values passed to the procedure, in the order the procedure expects. |

### Return Value

The value the procedure returns, typed by the first letter of `type_text`. Microsoft's page does not list error values for CALL. A wrong module, procedure or type text can cause errors that require restarting the computer.

## Examples

All examples use Excel for Windows and a registration stored in `A5`.

### Example 1: Register a Windows Procedure

In `A5`:

```excel
=REGISTER.ID("Kernel32", "GetTickCount", "J!")
```

Then in any other cell:

```excel
=CALL(A5)
```

**Result:** A whole number of milliseconds since Windows started. The value differs on every computer and changes over time.

The first form reuses the registration in `A5`, so the REGISTER.ID formula must be entered first.

<!-- Image 2: Register and Call Steps. See Images/Add-in & Automation/CALL.md -->

### Example 2: Convert the Result to Minutes

```excel
=CALL(A5)/60000
```

**Result:** The minutes since Windows started, shown with the cell's number format.

One minute is 60,000 milliseconds, so dividing by 60000 converts the result to minutes.

### Example 3: Show a Fallback When the Call Fails

```excel
=IFERROR(CALL(A5)/60000, "Not registered")
```

**Result:** The minutes value, or `Not registered` when the formula returns an error.

IFERROR catches error values only. It cannot stop Excel from crashing on a bad procedure, so the registration step still needs careful testing.

## Story Problems

### Problem 1: Kiosk Uptime Comparison

A maintenance log stores each kiosk's uptime in milliseconds, as returned by CALL. The values sit in `A1:B4`.

| Kiosk | Uptime (ms) |
| --- | --- |
| Kiosk A | 5400000 |
| Kiosk B | 16200000 |
| Kiosk C | 2700000 |

**Task:** Find the uptime of the kiosk that has been running longest, in minutes.

**Solution:**

```excel
=MAX(B2:B4)/60000
```

**Answer:** `270`, because the largest value is 16200000 and 16200000 divided by 60000 is 270 minutes (Kiosk B).

<!-- Image 3: Results Panel for the Story Problems. See Images/Add-in & Automation/CALL.md -->

### Problem 2: Flagging Missing Registrations

A workbook keeps register IDs in column B. Some rows are blank because the registration step was skipped. Column C should show each uptime in minutes, or `Not registered` for a blank row.

**Task:** Write one formula for `C2` that handles both cases, then fill it down.

**Solution:**

```excel
=IF(B2="", "Not registered", CALL(B2)/60000)
```

**Answer:** Blank rows show `Not registered`. Every other row shows the minutes since Windows started on that computer. Those minutes depend on the machine, so this answer describes the behavior rather than a fixed number.

## Use Cases

### Machine Uptime Reports

**Scenario:** A support team keeps a weekly sheet that shows how long each kiosk has run since its last restart.

```excel
=CALL(B2)/60000
```

**Why It Works:** Each row holds its own register ID, so one formula fills down the sheet. Dividing by 60000 reports minutes instead of milliseconds.

### Legacy Library Integration

**Scenario:** A plant floor workbook calls a procedure in an in-house DLL that reads a value from older equipment. The DLL name and procedure name are placeholders in this example.

```excel
=CALL("PlantTools.dll", "ReadSensor", "J", A2)
```

**Why It Works:** The second form registers and calls the procedure in one step and passes `A2` as the argument. The type text `"J"` is the code that Microsoft's examples use for the return value. Confirm the codes against the DLL's own documentation.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Function unavailable | The workbook is open in Excel for the web, which does not support CALL. | Open the workbook in the Excel desktop app. |
| Computer needs a restart | A wrong module, procedure or type text was used. | Check the names and type text against the DLL's documentation, and test in a copy. |
| Unexpected return value | The first letter of `type_text` does not match the procedure's return type. | Set the first letter to the procedure's return type. |
| Procedure rejected | The ordinal was entered as text. | Enter the ordinal as a number, not in quotation marks. |
| Blank or unexpected result | The register ID cell is empty or does not hold an ID from REGISTER.ID. | Run REGISTER.ID first and reference the cell it fills. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel on Windows. | Microsoft describes the function as for advanced users and says it works only from an Excel macro sheet. It is not available in Excel for the web. |
| Google Sheets | Not available | The closest alternative is Google Apps Script for custom code. Apps Script cannot load Windows DLLs. |

## Tips and Best Practices

- Register each procedure once with REGISTER.ID, store the ID in a labeled cell, and point CALL formulas at that cell.
- Test every new procedure in a copy of the workbook before you share it.
- Back up your data before any registry work, as Microsoft advises.
- Wrap CALL in IFERROR for a readable fallback, but do not rely on it to catch crashes.
- Confirm module names, procedure names and type codes against the DLL's own documentation.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REGISTER.ID](REGISTER.ID.md) | Registers the procedure and returns the register ID that the first form of CALL uses. |
| [IFERROR](../Logical/IFERROR.md) | Shows a fallback value when the call returns an error. |
| [ISERROR](../Information/ISERROR.md) | Tests a call result for an error before you use it. |
| [ISNUMBER](../Information/ISNUMBER.md) | Confirms that a returned value is a number before you do arithmetic on it. |

## Official Documentation

- [Microsoft Support: CALL function](https://support.microsoft.com/en-us/excel/functions/call-function)
