---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Array Shaping
  - Statistical Analysis
use-case:
  - Most Common Shirt Sizes
  - Tied Delivery Times
related:
  - AVERAGE
  - FREQUENCY
  - MEDIAN
  - MODE
  - MODE.SNGL
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/mode-mult-function
  - https://support.google.com/docs/answer/9368267
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - All Most Common Values
  - Multiple Modes
tags:
  - arrays
  - averages
  - excel
  - mode
  - sheets
---

# MODE.MULT

## Description

**MODE.MULT** returns every value that appears most often in a set of numbers. When one value is the most common, the result is that single value. When two or more values tie for the highest count, the result lists all of them as a vertical array. This makes it the right choice when a tie matters, such as two shirt sizes that sell equally well.

Because the function returns several results, it works differently from MODE.SNGL. In Microsoft 365, the results spill automatically into the cells below the formula, so those cells must be empty. In older versions of Excel, select the cells first and enter the formula as an array formula. Google Sheets returns the results as an array as well.

When no number repeats, MODE.MULT returns `#N/A`. Wrap the formula in IFERROR if a message is clearer, or count the results with ROWS to see how many modes exist. The function ignores text, logical values, and blank cells in ranges and references, and it includes zeros. The Microsoft documentation does not state an order for the results, so sort them yourself when order matters.

## Syntax

```excel
=MODE.MULT(number1, [number2], ...)
```

<!-- Image 1: Several Values Tied for Most Common. See Images/Statistical/MODE.MULT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or array to evaluate, for example `F2:F10`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. A single array or range can be passed in place of the list. |

### Return Value

A vertical array of the values that occur most often. It returns one value when only one mode exists, and several values when they tie. It returns `#N/A` when no value repeats. It returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

All examples use the values in `F2:F10` below, unless the example says otherwise.

| Reading |
| --- |
| 1 |
| 2 |
| 2 |
| 3 |
| 3 |
| 4 |
| 5 |
| 5 |
| 6 |

The values 2, 3, and 5 each appear twice, and no other value repeats.

### Example 1: All Modes in a Column

```excel
=MODE.MULT(F2:F10)
```

**Result:** `2`, `3`, `5` in three cells, one below the other

Each tied value is returned. In Microsoft 365 the results spill down the column automatically.

### Example 2: Modes Across a Row

```excel
=TRANSPOSE(MODE.MULT(F2:F10))
```

**Result:** `2`, `3`, `5` in three cells, side by side

TRANSPOSE turns the vertical result into a horizontal one. Use it when a report needs the modes in one row.

### Example 3: Counting the Modes

```excel
=ROWS(MODE.MULT(F2:F10))
```

**Result:** `3`

ROWS counts the values returned, so the result shows how many values tie for the most frequent count.

### Example 4: No Repeated Value

Assume `G2:G5` holds `1`, `2`, `3`, and `4`.

```excel
=MODE.MULT(G2:G5)
```

**Result:** `#N/A`

Each value appears once, so no mode exists.

### Example 5: Two Tied Modes

Assume `H2:H7` holds `10`, `10`, `20`, `30`, `30`, and `40`.

```excel
=MODE.MULT(H2:H7)
```

**Result:** `10`, `30` in two cells

The values 10 and 30 tie with two appearances each, so both are returned.

## Story Problems

### Problem 1: Most Common Shirt Sizes

A clothing shop records the size of each shirt sold in one week in `A1:B9`.

| Sale | Size |
| --- | --- |
| 1 | 38 |
| 2 | 40 |
| 3 | 42 |
| 4 | 40 |
| 5 | 38 |
| 6 | 44 |
| 7 | 42 |
| 8 | 46 |

**Task:** Find every shirt size that sold most often, because the buyer wants to stock all of the best sellers.

**Solution:**

```excel
=MODE.MULT(B2:B9)
```

**Answer:** `38`, `40`, and `42` in three cells. Each of these sizes sold twice, and no other size sold more than once.

### Problem 2: Tied Delivery Times

A courier records the delivery time in days for six parcels in `A1:B7`.

| Parcel | Days |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 3 | 3 |
| 4 | 5 |
| 5 | 5 |
| 6 | 8 |

**Task:** Find how many delivery times tie for the most common value.

**Solution:**

```excel
=ROWS(MODE.MULT(B2:B7))
```

**Answer:** `2`. The times 3 days and 5 days each occur twice, so two values tie.

<!-- Image 2: Story Problem Result. See Images/Statistical/MODE.MULT.md -->

## Use Cases

### Stocking Popular Sizes

**Scenario:** A buyer wants a list of every size that sold most often, so the next order covers all the strong sellers.

```excel
=MODE.MULT(Sales[Size])
```

**Why It Works:** All tied sizes are returned in one formula. In Microsoft 365 the list spills into the cells below, so leave those cells empty.

### Tied Delivery Times

**Scenario:** A logistics analyst wants to know how many different delivery times share the top frequency, to judge how consistent the service is.

```excel
=ROWS(MODE.MULT(Shipments[DaysToArrive]))
```

**Why It Works:** ROWS counts the returned values. A count of 1 means the service has one clear typical time, and a higher count means several times are equally common.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No value repeats in the data. | Wrap the formula in IFERROR, or confirm the data has repeats with COUNTIF. |
| `#SPILL!` | In Microsoft 365, a cell below the formula is not empty, so the results cannot spill. | Clear the cells below the formula, or move the formula to a cell with enough empty space. |
| Only one value appears | The formula is in a single cell in an older version of Excel that needs an array formula. | Select the cells for the results and enter the formula as an array formula. |
| Unexpected order | The results are not sorted by the documentation. | Wrap the result in SORT when a specific order is required. |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Returns a vertical array. Microsoft 365 spills the results. Older versions need the formula entered as an array formula. |
| Google Sheets | Available | Returns an array of the most frequent values. The help page says an error appears when every value occurs once, without naming the error code. |

## Tips and Best Practices

- Use MODE.MULT when a tie matters, and MODE.SNGL when one answer is enough.
- Leave the cells below a spilling formula empty so the results can display.
- Count the results with ROWS before you use them in a calculation.
- Wrap the result in SORT when the modes must appear in a fixed order.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MODE.SNGL](MODE.SNGL.md) | Returns only one most-common value, even when several tie. |
| [MODE](MODE.md) | The legacy function, kept for compatibility. |
| [FREQUENCY](FREQUENCY.md) | Counts how many values fall into each bin, which shows the tie in more detail. |
| [MEDIAN](MEDIAN.md) | Returns the middle value rather than the most frequent values. |
| [AVERAGE](AVERAGE.md) | Returns the arithmetic mean. |

## Official Documentation

- [Microsoft Support: MODE.MULT function](https://support.microsoft.com/en-us/excel/functions/mode-mult-function)
- [Google Docs Editors Help: MODE.MULT](https://support.google.com/docs/answer/9368267)
