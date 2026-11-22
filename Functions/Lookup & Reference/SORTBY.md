---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Sorting and Filtering
use-case:
  - Engineer Job Queues
  - Exam Score Rankings
  - Multi-Level Sales Reports
related:
  - FILTER
  - RANDARRAY
  - SEQUENCE
  - SORT
  - TAKE
  - UNIQUE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/sortby-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sort By Array
  - Sort By Columns
tags:
  - dynamic-array
  - excel
  - sorting
---

# SORTBY

## Description

**SORTBY** returns an array sorted by the values in one or more separate arrays. The sort keys do not have to be part of the output, so you can sort a list of names by a column of dates that is not shown in the result.

Use SORTBY when the order depends on more than one key, or when the key lives in a different column from the data. Each key has its own direction: 1 sorts ascending, and -1 sorts descending. Ascending is the default when the direction is left out. Any other direction value returns `#VALUE!`.

Microsoft recommends SORTBY over SORT for sorting grid data because it follows the source columns when columns are inserted or deleted. SORTBY works in Excel only. Google Sheets has no SORTBY, but SORT with a separate range as its sort column gives the same result for a single key.

## Syntax

```excel
=SORTBY(array, by_array1, [sort_order1], [by_array2, sort_order2], ...)
```

<!-- Image 1: SORTBY Key Pairs. See Images/Lookup & Reference/SORTBY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to return in the new order. It can be a row, a column or a block. |
| `by_array1` | Yes | The first sort key. It must be a single row or a single column, and it must be the same size as `array` in the sort direction. |
| `sort_order1` | No | `1` for ascending (the default) or `-1` for descending. |
| `by_array2` | No | A second sort key, used to break ties in the first key. Add more pairs of key and direction in the same way. |
| `sort_order2` | No | The direction for `by_array2`: `1` or `-1`. |

### Return Value

An array with the same shape as `array`, rearranged by the keys. It spills into the cells below and to the right of the formula when it is the final result of the formula. All arguments must be the same size, or the formula returns an error.

## Examples

All examples use this sales list in `A2:C6`.

| Rep | Region | Sales |
| --- | --- | --- |
| Avery | East | 1200 |
| Blake | West | 850 |
| Casey | East | 640 |
| Drew | North | 975 |
| Emery | West | 1530 |

### Example 1: Sort by Sales, Largest First

```excel
=SORTBY(A2:C6, C2:C6, -1)
```

**Result:** Emery (1530), Avery (1200), Drew (975), Blake (850), Casey (640)

The sort key is column C, but column C is also part of the output. The key does not need to be shown to be used.

### Example 2: Sort by Region, Then by Sales

```excel
=SORTBY(A2:C6, B2:B6, 1, C2:C6, -1)
```

**Result:** Avery (East, 1200), Casey (East, 640), Drew (North, 975), Emery (West, 1530), Blake (West, 850)

Region sorts from A to Z first. Within each region, the sales figures sort from highest to lowest.

### Example 3: Sort by Rep Name, Z to A

```excel
=SORTBY(A2:C6, A2:A6, -1)
```

**Result:** Emery, Drew, Casey, Blake, Avery

The key is a text column, and -1 reverses the alphabetical order.

### Example 4: Sort by Sales, Smallest First

```excel
=SORTBY(A2:C6, C2:C6)
```

**Result:** Casey (640), Blake (850), Drew (975), Avery (1200), Emery (1530)

The direction is left out, so the sort is ascending.

<!-- Image 2: Two-Key Sort Layout. See Images/Lookup & Reference/SORTBY.md -->

## Story Problems

### Problem 1: Engineer Job Queue

A dispatcher tracks each engineer's job count and miles driven in `A2:C6`.

| Engineer | Jobs | Miles |
| --- | --- | --- |
| Ana | 5 | 120 |
| Ben | 7 | 210 |
| Cy | 7 | 150 |
| Dee | 4 | 90 |
| Eli | 6 | 95 |

**Task:** Rank the engineers by the most jobs first. When two engineers have the same number of jobs, the one with fewer miles comes first. Name the top engineer.

**Solution:**

```excel
=SORTBY(A2:C6, B2:B6, -1, C2:C6, 1)
```

**Answer:** `Cy`, with 7 jobs and 150 miles. Ben also has 7 jobs but drove 210 miles, so he ranks second.

### Problem 2: Exam Ranking

A teacher lists five students with their scores in `A2:B6`.

| Student | Score |
| --- | --- |
| Ivy | 88 |
| Jules | 92 |
| Kofi | 75 |
| Lena | 92 |
| Milo | 81 |

**Task:** Rank the students from the highest score to the lowest. Break ties by name, A to Z. Name the student in second place.

**Solution:**

```excel
=INDEX(SORTBY(A2:B6, B2:B6, -1, A2:A6, 1), 2, 1)
```

**Answer:** `Lena`. Jules and Lena both scored 92, and Jules comes first alphabetically.

## Use Cases

### Engineer Job Queue

**Scenario:** A dispatcher wants the next job assigned to the engineer with the most open jobs, and ties resolved by travel distance.

```excel
=SORTBY(Engineers!A2:A20, Engineers!B2:B20, -1, Engineers!C2:C20, 1)
```

**Why It Works:** The first key ranks by job count, and the second key uses the shorter mileage to break ties. The sorted list updates whenever the job counts change.

### Top Five Customers

**Scenario:** A regional report shows the five largest customers by revenue, with the name and region shown beside the revenue.

```excel
=TAKE(SORTBY(Customers!A2:C200, Customers!C2:C200, -1), 5)
```

**Why It Works:** SORTBY orders the list by revenue without showing that column first, and TAKE returns the top five rows.

### Shuffled Draw List

**Scenario:** A teacher needs a random order of student names for a presentation schedule.

```excel
=SORTBY(Students!A2:A31, RANDARRAY(ROWS(Students!A2:A31)))
```

**Why It Works:** RANDARRAY produces one random number per student, and SORTBY uses those numbers as the key. The order changes each time the sheet recalculates.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A sort direction is something other than 1 or -1. | Use 1 for ascending or -1 for descending. |
| Formula error or wrong result | A key array is not the same size as `array`. | Make every key cover the same rows or columns as `array`. |
| Key is not a single row or column | A `by_array` is a block rather than a row or column. | Pass one row or one column as the key. |
| `#SPILL!` | The cells below or beside the formula are not empty. | Clear the spill range, or move the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2021, Excel 2024, Microsoft 365, Excel for the web | Not listed for Excel 2019 or earlier. Accepts any number of key and direction pairs. |
| Google Sheets | Not available | Use SORT with a separate range as the sort column for a single key, for example `=SORT(A2:C6, C2:C6, FALSE)`. |

## Tips and Best Practices

- Put the most important key first, because it decides the order before any later key is considered.
- Use a key that is not part of the output when you want to sort by a hidden helper column.
- Use RANDARRAY as a key for a shuffled list, and paste its values if the order must stay fixed.
- Check that every key covers the same rows as the array, or the result will not be reliable.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SORT](SORT.md) | Sorts by one column of the output, with a simpler syntax. |
| [FILTER](FILTER.md) | Selects the rows to sort before SORTBY orders them. |
| [TAKE](TAKE.md) | Returns the first or last rows of a sorted result. |
| [RANDARRAY](../Math%20%26%20Trig/RANDARRAY.md) | Produces random keys for a shuffled order. |
| [SEQUENCE](../Math%20%26%20Trig/SEQUENCE.md) | Builds rank numbers to pair with a sorted list. |
| [UNIQUE](UNIQUE.md) | Removes duplicates before a sort. |

## Official Documentation

- [Microsoft Support: SORTBY function](https://support.microsoft.com/en-us/excel/functions/sortby-function)
