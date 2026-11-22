---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Counting
  - Database Queries
use-case:
  - Lead Follow-Up Lists
  - Missing Contact Details
  - Student Note Tracking
related:
  - COUNTA
  - COUNTIFS
  - DCOUNT
  - DGET
  - DSUM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dcounta-function
  - https://support.google.com/docs/answer/3094147
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Count All
  - Count Nonblank Records
tags:
  - counting
  - criteria
  - database
  - excel
  - sheets
---

# DCOUNTA

## Description

**DCOUNTA** counts the nonblank cells in one field (column) of a list, considering only the records that match the conditions in a separate criteria range. Unlike DCOUNT, it counts text as well as numbers, so it answers the question "how many records have something entered here?" The list is a range where the first row holds column labels and every row below it is a record.

Use DCOUNTA to check completeness, such as how many leads in one region have a phone number, or how many students in a class have a note. A blank cell is not counted. A cell that holds a space or a formula returning an empty result may still be counted, so test a sample before relying on the total.

The criteria range is built from column labels with conditions beneath them. Conditions on the same row combine with AND, and conditions on separate rows combine with OR. For fixed conditions written inside a formula, COUNTIFS is simpler. DCOUNTA is the better choice when conditions are edited on the sheet or when several condition rows are needed.

## Syntax

```excel
=DCOUNTA(database, [field], criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DCOUNTA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | No | The column to count: a header label in quotes (`"Phone"`), a cell that holds the label, or the column position as a number. When omitted, the function counts the matching records. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A whole number: how many nonblank cells in the field belong to records that match the criteria. A count of zero means no matching record has a value in that field.

## Examples

All examples use this shop list in `A1:E8`. The Units value for the Hillside desk is the text `Pending`.

| Store | Product | Category | Units | Price |
| --- | --- | --- | --- | --- |
| Riverside | Desk | Furniture | 4 | 220 |
| Riverside | Lamp | Lighting | 12 | 35 |
| Hillside | Desk | Furniture | Pending | 240 |
| Hillside | Chair | Furniture | 9 | 85 |
| Lakeview | Lamp | Lighting | 6 | 40 |
| Lakeview | Shelf | Storage | 5 | 60 |
| Riverside | Shelf | Storage | 3 | 55 |

### Example 1: Text Counts as an Entry

Criteria in `G1:G2`: `Store` above `Hillside`.

```excel
=DCOUNTA(A1:E8, "Units", G1:G2)
```

**Result:** `2`

Both Hillside records have something in the Units column. The text `Pending` is counted, so the result is 2. DCOUNT returns 1 for the same criteria.

### Example 2: Count Records in One Category

Criteria in `G1:G2`: `Category` above `Storage`.

```excel
=DCOUNTA(A1:E8, "Product", G1:G2)
```

**Result:** `2`

The two storage records each have a product name, so both are counted.

<!-- Image 2: Nonblank Counting Versus Numeric Counting. See Images/Database/DCOUNTA.md -->

### Example 3: Omit the Field Argument

Criteria in `G1:G2`: `Store` above `Riverside`.

```excel
=DCOUNTA(A1:E8,, G1:G2)
```

**Result:** `3`

With the field left empty, the function counts the matching records. Three records belong to Riverside.

### Example 4: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Store` above `Riverside`, then `Lakeview` on the next row.

```excel
=DCOUNTA(A1:E8, "Product", G1:G3)
```

**Result:** `5`

Riverside has three products (desk, lamp and shelf) and Lakeview has two (lamp and shelf). The five records are counted once each.

## Story Problems

### Problem 1: Leads Missing a Phone Number

A sales team keeps a lead list in `A1:C6`. Some leads have not yet shared a phone number, so their cell is empty.

| Lead | Region | Phone |
| --- | --- | --- |
| Ana | North | 555-0101 |
| Ben | South | |
| Cy | North | |
| Dev | North | 555-0144 |
| Eli | South | 555-0177 |

**Task:** Put `Region` in `E1` and `North` in `E2`, then count the North leads who have a phone number on file.

**Solution:**

```excel
=DCOUNTA(A1:C6, "Phone", E1:E2)
```

**Answer:** `2`, because Ana and Dev have numbers recorded. Cy's cell is empty and is not counted.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DCOUNTA.md -->

### Problem 2: Students With a Note

A teacher records notes for students in `A1:C5`. Some students have no note yet.

| Student | Class | Note |
| --- | --- | --- |
| Ivy | Art | Late |
| Jon | Art | |
| Kai | Math | Absent |
| Lou | Art | Excused |

**Task:** Put `Class` in `E1` and `Art` in `E2`, then count the Art students with a note.

**Solution:**

```excel
=DCOUNTA(A1:C5, "Note", E1:E2)
```

**Answer:** `2`, because Ivy and Lou have notes. Jon has no note, and Kai is in Math, so neither is counted.

## Use Cases

### Lead Follow-Up Lists

**Scenario:** A sales manager sees how many leads in each territory still lack a phone number, with the territory typed into a cell.

```excel
=DCOUNTA(Leads, "Phone", TerritoryFilter)
```

**Why It Works:** The named criteria range keeps the formula unchanged while the manager switches territories. A count below the lead total shows how many records need follow-up.

### Missing Contact Details

**Scenario:** An events team checks how many attendees in one ticket group have an email address before sending confirmations.

```excel
=DCOUNTA(Attendees, "Email", GroupCriteria)
```

**Why It Works:** DCOUNTA counts text, which is what an email address is. Compare the result with the group size to find the missing entries.

### Student Note Tracking

**Scenario:** A school counts how many students in one class have a teacher note this term.

```excel
=DCOUNTA(Records, "Note", ClassCriteria)
```

**Why It Works:** Blank notes are skipped, so the count reflects only the records where a teacher actually wrote something.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count higher than expected | A cell contains a space or a formula that returns an empty string, which is not truly blank. | Clear the cells or test them with a helper column before counting. |
| Count of 0 | Criteria labels do not match the database headers. | Copy the header cells into the criteria range. |
| Unexpected count | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| Unexpected count | Text criteria match more values than intended, such as `North` matching `Northeast`. | Use `="=North"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Counts nonblank cells, including text. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same arguments and the same nonblank counting purpose. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use DCOUNTA for completeness checks and DCOUNT for numeric totals.
- Compare DCOUNTA with the count of records that match the criteria alone to find how many cells are empty.
- Keep the criteria range above or beside the list, never below it.
- Remove stray spaces from imported data, because a space makes a cell look filled.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTA](../Statistical/COUNTA.md) | Counts nonblank cells in a plain range with no criteria. |
| [COUNTIFS](../Statistical/COUNTIFS.md) | Counts rows that meet conditions written inside the formula. |
| [DCOUNT](DCOUNT.md) | Counts only numeric values for the same matching records. |
| [DGET](DGET.md) | Returns the single value that matches the criteria. |
| [DSUM](DSUM.md) | Adds the numeric values for the same matching records. |

## Official Documentation

- [Microsoft Support: DCOUNTA function](https://support.microsoft.com/en-us/excel/functions/dcounta-function)
- [Google Docs Editors Help: DCOUNTA](https://support.google.com/docs/answer/3094147)
