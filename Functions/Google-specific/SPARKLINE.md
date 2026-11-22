---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Chart Display
purpose:
  - Data Visualization
use-case:
  - Monthly Sales Trend
  - Project Progress Tracking
  - Win Loss Tracking
related:
  - ARRAYFORMULA
  - IMAGE
  - QUERY
level: 3
source:
  - https://support.google.com/docs/answer/3093289
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - In Cell Chart
  - Mini Chart
tags:
  - charts
  - data-visualization
  - sheets
  - sparkline
---

# SPARKLINE

## Description

**SPARKLINE** draws a small chart inside a single cell. The chart is built from a range of numbers, so a row of twelve monthly totals can show its overall shape in one cell next to the row. It is useful on dashboards and summary tables where a full chart would take too much space.

The default chart is a line. Set the chart type with the `"charttype"` option to draw a stacked bar, a column chart, or a win/loss chart, which plots positive values above a baseline and negative values below it. The options are written as name and value pairs, so the chart can also be given a color, a fixed axis range, or an axis line.

SPARKLINE is a visual aid, not a calculation. The chart shows the pattern of the numbers, but it does not return a number you can add up or compare. Use a formula such as COUNTIF or AVERAGE alongside it when you need the figures. Excel has no SPARKLINE function. It offers sparklines through the Insert tab instead, with different chart types and settings.

## Syntax

```excel
=SPARKLINE(data, [options])
```

<!-- Image 1: Sparkline Syntax Anatomy. See Images/Google-specific/SPARKLINE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `data` | Yes | The range or array of numbers to plot, for example `B2:M2`. |
| `options` | No | Settings that change the chart. Write them as an array literal such as `{"charttype","bar"}`, or point to a range that is two cells wide, with the option name in the first cell and its value in the second. |

Common options and their values:

| Option | Values | Applies To | Effect |
| --- | --- | --- | --- |
| `"charttype"` | `"line"` (default), `"bar"`, `"column"`, `"winloss"` | All | Sets the chart type. |
| `"color"` | A color name or hex code | Line, column | Sets the line or column color. |
| `"ymin"`, `"ymax"` | Numbers | Line, column | Fixes the vertical scale so charts in different cells match. |
| `"empty"` | `"zero"` or `"ignore"` | All | Treats empty cells as zero or skips them. |
| `"axis"` | `true` or `false` | Column, winloss | Draws a horizontal axis line. |
| `"max"` | A number | Bar | Sets the scale maximum for the bars. |

### Return Value

The function returns a chart drawn inside the cell, not a number. The official documentation does not describe the return value or the error conditions for SPARKLINE, so check the chart after you change the data range or the options.

## Examples

All examples use the monthly figures in `A1:F2` unless the example says otherwise. Each example is a separate formula, typed into a cell that has enough width to show the chart.

### Example 1: Default Line Chart

```excel
=SPARKLINE(B2:G2)
```

**Result:** A line chart of six values drawn inside the cell.

With no options, the chart is a line from left to right. Each point is one month, so the line rises and falls with the monthly totals.

### Example 2: Bar Chart With a Fixed Maximum

```excel
=SPARKLINE(B3:F3, {"charttype","bar"; "max",40})
```

**Result:** A stacked bar chart whose longest bar fills the scale set by 40.

The `"max"` option holds the scale at 40 for every bar, so bars in other rows that use the same maximum can be compared fairly.

### Example 3: Column Chart With an Axis Line

```excel
=SPARKLINE(B2:G2, {"charttype","column"; "axis",true; "axiscolor","red"})
```

**Result:** A column chart with one column per value and a red horizontal axis.

The axis line helps the reader see which columns sit above zero and which sit below it.

<!-- Image 2: Chart Types Side by Side. See Images/Google-specific/SPARKLINE.md -->

### Example 4: Win/Loss Chart

```excel
=SPARKLINE(B5:G5, {"charttype","winloss"})
```

**Result:** A chart with one fixed-height column per month, drawn above the baseline for positive values and below it for negative values.

Win/loss charts ignore the size of each value. They show only whether each month was positive or negative, which suits a quick pattern check.

### Example 5: Options Read From a Range

```excel
=SPARKLINE(B2:G2, I1:J2)
```

**Result:** The same line chart as Example 1, with the options taken from cells `I1:J2`.

Put the option name in `I1` (for example `charttype`) and its value in `J1`, then add a second option on row 2. Changing the cells changes the chart without editing the formula.

## Story Problems

### Problem 1: Monthly Profit Pattern

A small shop records profit for six months in `B1:G2`. Positive months are profitable, and negative months are losses.

| Month | Jan | Feb | Mar | Apr | May | Jun |
| --- | --- | --- | --- | --- | --- | --- |
| Profit | 1200 | -350 | 900 | -80 | 430 | 610 |

**Task:** Show the profit pattern as a win/loss chart in `B4`, and count the profitable months in `B5`.

**Solution:**

```excel
=SPARKLINE(B2:G2, {"charttype","winloss"})
=COUNTIF(B2:G2, ">0")
```

**Answer:** The chart shows four columns above the baseline and two below it. The count is `4`, because January, March, May and June are positive.

<!-- Image 3: Win/Loss Results for the Shop Profit Problem. See Images/Google-specific/SPARKLINE.md -->

### Problem 2: Project Task Progress

A team tracks the number of tasks it closed each week in `B2:F2`, and wants a column chart that uses the same scale as the other project rows.

| Week | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Tasks closed | 4 | 7 | 5 | 9 | 6 |

**Task:** Draw the chart with a fixed scale from 0 to 10 so it can be compared with other rows.

**Solution:**

```excel
=SPARKLINE(B2:F2, {"charttype","column"; "ymin",0; "ymax",10})
```

**Answer:** The chart shows five columns. The tallest column is week 4 (9 tasks), and the shortest is week 1 (4 tasks). The chart draws the values, so the total of 31 tasks comes from `=SUM(B2:F2)`.

## Use Cases

### Monthly Sales Trend

**Scenario:** A sales report lists twelve months of revenue for each region on one row, and the manager wants a visual trend beside each total.

```excel
=SPARKLINE(B2:M2)
```

**Why It Works:** One formula per row adds a trend chart without a separate chart object. Set the same `"ymin"` and `"ymax"` on every row so the charts can be compared.

### Project Progress Tracking

**Scenario:** A project tracker shows weekly progress for each workstream, and the lead wants to see the pattern at a glance.

```excel
=SPARKLINE(B5:F5, {"charttype","bar"; "max",10})
```

**Why It Works:** The bar chart fills in proportion to the value, and the fixed maximum keeps each bar measured against the same goal.

### Win Loss Tracking

**Scenario:** A trading team records daily results and wants to see which days were gains and which were losses.

```excel
=SPARKLINE(B8:K8, {"charttype","winloss"})
```

**Why It Works:** The win/loss chart shows only the sign of each value, so a long run of gains or losses is easy to spot.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Gaps or unexpected drops in the chart | The data range contains blank cells or text. | Convert text to numbers, or set `"empty"` to `"zero"` to treat blanks as zero. |
| Charts look different from each other | Each cell scales to its own minimum and maximum by default. | Set the same `"ymin"` and `"ymax"` on every chart in the group. |
| Option has no effect | The option name is misspelled, or the option does not apply to the chart type. | Check the option name and the chart types listed in the Parameters table. |
| Chart is not visible | The formula sits in a cell that is too narrow to show the chart. | Widen the column or the row that holds the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as a function | Insert sparklines from the Insert tab, choosing Line, Column or Win/Loss. Adjust the chart on the Sparkline Tools tab. |
| Google Sheets | Available | Set the chart type and other options inside the formula. |

## Tips and Best Practices

- Give related sparklines the same `"ymin"` and `"ymax"` so the shapes can be compared fairly.
- Keep a number next to each sparkline, such as a total or an average, because the chart shows the shape but not the exact figures.
- Use a win/loss chart when only the direction matters, and a line or column chart when the size of each change matters.
- Put the options in cells when several people need to change the chart style without editing formulas.
- Remember that a sparkline is a picture of the cells, so it updates when the data changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYFORMULA](ARRAYFORMULA.md) | Applies a formula to a whole range, useful for building the data a sparkline plots. |
| [IMAGE](../Lookup%20%26%20Reference/IMAGE.md) | Places a picture in a cell, for when a fixed image is needed instead of a chart. |
| [QUERY](QUERY.md) | Filters or summarizes a table before the results are charted. |

## Official Documentation

- [Google Docs Editors Help: SPARKLINE](https://support.google.com/docs/answer/3093289)
