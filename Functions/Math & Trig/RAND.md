---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Random Numbers
purpose:
  - Randomization
use-case:
  - Monte Carlo Scenarios
  - Random Test Groups
  - Randomized Audit Samples
related:
  - INT
  - RANDARRAY
  - RANDBETWEEN
  - ROUND
  - SEQUENCE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/rand-function
  - https://support.google.com/docs/answer/3093438
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Random Decimal
  - Random Number
tags:
  - excel
  - randomization
  - sheets
  - volatile
---

# RAND

## Description

**RAND** returns a random decimal number that is at least 0 and less than 1. The value is evenly distributed across that range, so every part of the range is equally likely. The function takes no arguments, so you type `=RAND()` with empty parentheses. The lower bound is included and the upper bound is excluded, so the function never returns exactly 1.

RAND recalculates whenever the worksheet recalculates. Entering a value in another cell, or pressing F9, produces a new number in every cell that uses RAND. This behavior makes RAND useful for simulations and random sampling, but it also means that a report built from RAND values changes each time someone edits the sheet. To keep a set of numbers, copy the cells and paste them as values.

Scale and shift the result to reach a different range. `=RAND()*(b-a)+a` returns a decimal between `a` and `b`. To get whole numbers, use RANDBETWEEN, which accepts the bounds directly, or wrap RAND in INT.

## Syntax

```excel
=RAND()
```

<!-- Image 1: Random Decimal Results. See Images/Math & Trig/RAND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| None | Not applicable | RAND takes no arguments. The empty parentheses are still required. |

### Return Value

A decimal number greater than or equal to 0 and less than 1. The value changes whenever the worksheet recalculates. RAND does not return an error on its own.

<!-- Image 2: Scaling RAND to a Range. See Images/Math & Trig/RAND.md -->

## Examples

### Example 1: Random Decimal Between 0 and 1

```excel
=RAND()
```

**Result:** a decimal from 0 up to, but not including, 1, such as 0.4217. The value changes on each recalculation.

The function returns a fresh number each time the sheet recalculates. Because the upper bound is excluded, the result is always less than 1.

### Example 2: Random Decimal Below 100

```excel
=RAND()*100
```

**Result:** a decimal from 0 up to, but not including, 100

Multiplying by 100 stretches the range. The result can never equal 100.

### Example 3: Random Decimal Between 50 and 100

```excel
=RAND()*(100-50)+50
```

**Result:** a decimal from 50 up to, but not including, 100

The formula multiplies the random number by the width of the range, 50, and then adds the lower bound. This is the standard way to shift RAND to any range.

### Example 4: Simulated Die Roll

```excel
=INT(RAND()*6)+1
```

**Result:** a whole number from 1 to 6

RAND times 6 gives a decimal from 0 up to, but not including, 6. INT removes the decimal part, so the value is 0 to 5, and adding 1 gives a die face from 1 to 6.

### Example 5: Freezing a Random Value

Type `=RAND()` in the formula bar, press F9 to replace the formula with the number it currently shows, and then press Enter.

**Result:** a fixed decimal that no longer changes when the sheet recalculates

Once the formula is replaced by its value, the cell keeps that number. Use this approach for a sample that must stay the same in a report.

## Story Problems

### Problem 1: Simulated Delivery Times

A logistics planner models how long a delivery takes. Each delivery is expected to take between 2.5 and 4.5 hours, with any time in that range equally likely.

| Item | Value |
| --- | --- |
| Shortest Time (hours) | 2.5 |
| Longest Time (hours) | 4.5 |

**Task:** Write a formula that returns one simulated delivery time between the two limits, which are in `B2` and `B3`.

**Solution:**

```excel
=RAND()*(B3-B2)+B2
```

**Answer:** A decimal from 2.5 up to, but not including, 4.5 hours. It changes on each recalculation. For a fixed set of simulated times, paste the results as values.

### Problem 2: Assigning Test Groups at Random

A teacher wants each student to be assigned to group A or group B with equal chance.

| Item | Value |
| --- | --- |
| Group A Label | Group A |
| Group B Label | Group B |

**Task:** Write a formula that returns the group label for each student.

**Solution:**

```excel
=IF(RAND()<0.5,"Group A","Group B")
```

**Answer:** Group A when RAND returns a value below 0.5, and Group B otherwise. Each label occurs about half the time over many students, though any small group can be uneven.

## Use Cases

### Monte Carlo Scenarios

**Scenario:** A project manager estimates the cost of a task with an uncertain price between a low and high figure.

```excel
=RAND()*(C2-B2)+B2
```

**Why It Works:** The formula picks a value between the low estimate in `B2` and the high estimate in `C2`. Copy it down many rows, then study the spread of results to see the likely range of total cost.

### Random Test Groups

**Scenario:** A product team splits users into a control group and a test group before a feature launch.

```excel
=IF(RAND()<0.5,"Control","Variant")
```

**Why It Works:** Each user is assigned by comparing a random decimal to 0.5. Paste the assignments as values before launch so they do not change when the sheet recalculates.

### Randomized Audit Samples

**Scenario:** An internal auditor selects invoices for review from a long list without bias.

```excel
=RAND()
```

**Why It Works:** Place a RAND value beside each invoice, sort the list by that column, and review the top rows. Paste the sorted sample as values so the audit record stays fixed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Values change on every edit | RAND recalculates with the worksheet. | Paste the results as values once the sample is final. |
| Whole numbers are expected but decimals appear | RAND returns decimals. | Use RANDBETWEEN for integers, or wrap RAND in INT. |
| Upper bound never appears | The range excludes 1, and `RAND()*100` never reaches 100. | Use RANDBETWEEN for an inclusive whole-number range. |
| Report numbers do not match a later printout | A new random value was generated after the report was created. | Store the values in a separate sheet and reference that copy in the report. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | No arguments. Recalculates each time the worksheet recalculates. |
| Google Sheets | Available | No arguments. Returns a random number from 0 inclusive to 1 exclusive. The official page gives no recalculation notes, so test its behavior in your sheet. |

## Tips and Best Practices

- Use RANDBETWEEN when you need whole numbers in a fixed range.
- Paste random results as values before you share a report or record an audit sample.
- Use `RAND()*(b-a)+a` for any decimal range, and check that a is smaller than b.
- Keep a pasted copy of final results beside the live formulas so that the report keeps the numbers it was built from.
- Run a large number of rows when you need the results to show a realistic spread.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INT](INT.md) | Removes the decimal part, used with RAND to build whole numbers. |
| [RANDARRAY](RANDARRAY.md) | Returns a block of random numbers in one formula. |
| [RANDBETWEEN](RANDBETWEEN.md) | Returns a random whole number between two bounds. |
| [ROUND](ROUND.md) | Rounds the random decimal to a set number of places for display. |
| [SEQUENCE](SEQUENCE.md) | Returns an ordered list of numbers, useful as an index before random sorting. |

## Official Documentation

- [Microsoft Support: RAND function](https://support.microsoft.com/en-us/excel/functions/rand-function)
- [Google Docs Editors Help: RAND](https://support.google.com/docs/answer/3093438)
