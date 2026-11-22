---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Counting
  - Statistical Analysis
use-case:
  - Delivery Time Bands
  - Test Score Bands
related:
  - COUNTIF
  - COUNTIFS
  - PERCENTILE.INC
  - QUARTILE.INC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/frequency-function
  - https://support.google.com/docs/answer/3094286
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Frequency Distribution
tags:
  - distribution
  - excel
  - histogram
  - sheets
---

# FREQUENCY

## Description

**FREQUENCY** counts how many values in a data set fall into each band, or class, defined by a list of upper limits. It returns a vertical array of counts, one count for each limit plus one extra count for the values above the highest limit. The result is the data behind a histogram, so you can see the shape of a distribution without sorting the list.

Each count covers the values above the previous limit up to and including the current one. Blank cells and text in the data are ignored. Use FREQUENCY when you need counts for a whole set of bands at once. For a single band with a simple condition, COUNTIFS is shorter and easier to read.

FREQUENCY returns an array, so the formula must fill several cells. In Excel for Microsoft 365, enter it in the top-left cell of the output range and the results spill down. In older Excel versions, select the output range, enter the formula in the top-left cell, and press Ctrl+Shift+Enter. Google Sheets fills the results automatically in the same order as the bins.

## Syntax

```excel
=FREQUENCY(data_array, bins_array)
```

<!-- Image 1: Data and Bins Layout. See Images/Statistical/FREQUENCY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `data_array` | Yes | The values to count, as a range or an array. Blank cells and text are ignored. If the argument contains no values, the result is an array of zeros. |
| `bins_array` | Yes | The upper limits of the bands, as a range or an array. Each limit is included in its own band. If the argument contains no values, the result is the number of values in `data_array`. |

### Return Value

A vertical array of counts with one more element than `bins_array`. The first element counts values up to and including the first limit, each later element counts values above the previous limit up to and including its own limit, and the last element counts values above the highest limit.

## Examples

The examples use 13 test scores in `A2:A14` and four upper limits in `C2:C5`: 60, 70, 80 and 90.

### Example 1: Counting Each Band

```excel
=FREQUENCY(A2:A14, C2:C5)
```

**Result:** A vertical array of five counts: `3`, `3`, `3`, `2` and `2`.

The counts cover up to 60, above 60 to 70, above 70 to 80, above 80 to 90, and above 90. The five counts add up to 13, the number of scores.

### Example 2: Checking the Total

```excel
=SUM(FREQUENCY(A2:A14, C2:C5))
```

**Result:** `13`

The sum of all bands equals the number of values counted. A total smaller than the number of scores means some values were blank or text.

<!-- Image 2: Histogram of Band Counts. See Images/Statistical/FREQUENCY.md -->

### Example 3: Counting One Band With COUNTIFS

```excel
=COUNTIFS(A2:A14, ">60", A2:A14, "<=70")
```

**Result:** `3`

This formula checks the second band on its own. The scores 61, 67 and 70 fall above 60 and up to 70.

### Example 4: Pulling One Count From the Array

```excel
=INDEX(FREQUENCY(A2:A14, C2:C5), 5)
```

**Result:** `2`

The fifth element counts the scores above the highest limit of 90, which are 92 and 95. Use INDEX when a dashboard needs one band rather than the whole array.

## Story Problems

### Problem 1: Delivery Time Bands

A courier company records the minutes each delivery took. Limits of 10, 20 and 30 minutes divide the results into bands.

| Delivery | Minutes |
| --- | --- |
| 1 | 8 |
| 2 | 12 |
| 3 | 25 |
| 4 | 31 |
| 5 | 14 |
| 6 | 40 |
| 7 | 19 |
| 8 | 22 |
| 9 | 9 |
| 10 | 27 |

The limits 10, 20 and 30 are in `D2:D4`.

**Task:** Count the deliveries in each band with one formula.

**Solution:**

```excel
=FREQUENCY(B2:B11, D2:D4)
```

**Answer:** `2`, `3`, `3` and `2`, which means two deliveries took up to 10 minutes, three took above 10 to 20 minutes, three took above 20 to 30 minutes, and two took more than 30 minutes.

<!-- Image 3: Delivery Time Results Table. See Images/Statistical/FREQUENCY.md -->

### Problem 2: Scores Above the Top Limit

A teacher uses the 13 scores from Example 1 and wants the number of scores above 90.

**Task:** Return only the count above the highest limit.

**Solution:**

```excel
=INDEX(FREQUENCY(A2:A14, C2:C5), 5)
```

**Answer:** `2`, because 92 and 95 are the only scores above 90.

## Use Cases

### Delivery Time Bands

**Scenario:** An operations manager reports how many deliveries fall into each time band each week.

```excel
=FREQUENCY(Minutes, Band_Limits)
```

**Why It Works:** Named ranges let the same formula update when the list grows. The extra final count shows deliveries that exceeded the highest limit, which is often the number to watch.

### Test Score Bands

**Scenario:** A teacher builds a histogram of quiz scores to see where most students fall.

```excel
=FREQUENCY(Scores, Grade_Bands)
```

**Why It Works:** The grade bands are typed in a visible column, so the teacher can change the limits without editing the formula. Chart the result as columns to show the histogram.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Only one number shows | The formula was entered in one cell in an older Excel version. | Select the full output range, then press Ctrl+Shift+Enter in the top-left cell. |
| `0` in every band | The data argument is empty or contains only text. | Check that the data range holds numbers. |
| Total is lower than the number of scores | Some values are blank or text and were ignored. | Clean the data column, then compare the sum with the count of numbers. |
| Counts do not match a COUNTIFS check | A value equal to a limit falls into the lower band. | Compare the bands with the same inclusive limits. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Excel for Microsoft 365 spills the result. Older versions need the array entry described in the Description. |
| Google Sheets | Available | Results follow the order of the classes in the formula. The Google page describes the argument as `classes` rather than `bins_array`. |

## Tips and Best Practices

- Sort the bins in increasing order, and keep them in one labeled column so the band boundaries are visible.
- Add a label next to each count, and pair the counts with the bin labels in a summary table.
- Leave the output range one cell longer than the bin list, because the final cell holds the values above the top limit.
- Use FREQUENCY for histograms and COUNTIFS for a single band with a simple condition.
- Chart the counts as columns, and keep the bands equal width so the bars can be compared.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTIF](COUNTIF.md) | Counts values that meet one condition. |
| [COUNTIFS](COUNTIFS.md) | Counts values that meet several conditions, useful for a single band. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns the value at a chosen percentile, which helps choose the bands. |
| [QUARTILE.INC](QUARTILE.INC.md) | Returns quartile boundaries that can serve as bins. |

## Official Documentation

- [Microsoft Support: FREQUENCY function](https://support.microsoft.com/en-us/excel/functions/frequency-function)
- [Google Docs Editors Help: FREQUENCY](https://support.google.com/docs/answer/3094286)
