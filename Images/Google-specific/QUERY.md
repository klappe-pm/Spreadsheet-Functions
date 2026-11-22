---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Query and Filtering
related:
  - QUERY
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - query-language
---

# QUERY Image Guide

Images planned for [QUERY](../../Functions/Google-specific/QUERY.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Query Clause Order

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Horizontal flow diagram with labeled boxes. |
| Content | The formula `=QUERY(data, query, [headers])` on the left with each argument boxed. On the right, the clause sequence SELECT, WHERE, GROUP BY, PIVOT, ORDER BY, LIMIT, OFFSET, LABEL, FORMAT, OPTIONS as connected boxes, each marked optional, with a note that the order is fixed. |
| Alt Text | Diagram of the QUERY formula arguments and the fixed order of the query language clauses. |
| File Name | QUERY Clause Order.png |

## Image 2: Grouped Output Example

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Two-panel screenshot of a worksheet. |
| Content | Left panel: the sales list in `A1:D7` with the desk rows shaded. Right panel: the QUERY output in F1 with a header row and three regional totals, North 450, South 280 and West 600. An arrow links the shaded rows to the output. |
| Alt Text | A sales list with desk rows shaded and a grouped output showing one total per region. |
| File Name | QUERY Grouped Output.png |

## Image 3: Attendance Story Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The event table in `A1:C6` with the Workshop and Training rows greyed out, and the QUERY output beside it listing Summit 510, Launch 240 and Expo 180 under a header row. |
| Alt Text | An event attendance table with three events above 100 attendees listed in descending order by a QUERY formula. |
| File Name | QUERY Attendance Result.png |
