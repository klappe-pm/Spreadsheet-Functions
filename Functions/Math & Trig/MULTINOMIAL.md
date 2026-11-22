---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Probability
  - Special Functions
use-case:
  - Anagram Counts
  - Committee Partitions
  - Task Allocation Counts
related:
  - COMBIN
  - FACT
  - FACTDOUBLE
  - SUM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/multinomial-function
  - https://support.google.com/docs/answer/3093429
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Multinomial Coefficient
tags:
  - combinatorics
  - excel
  - factorial
  - sheets
---

# MULTINOMIAL

## Description

**MULTINOMIAL** returns the number of ways to split a total into groups of fixed sizes, when the order of items inside each group does not matter and the order of the groups does matter. The result is the factorial of the sum of the group sizes, divided by the product of each group size's factorial.

For example, MULTINOMIAL(3, 2, 1) returns 60. The six items can be split into a group of 3, a group of 2, and a group of 1 in 60 different ways. The same calculation also counts the distinct arrangements of letters in a word: the word BANANA has 3 A's, 2 N's, and 1 B, so it has 60 distinct arrangements.

When there are only two groups, the result equals COMBIN for the same total. Use MULTINOMIAL when there are three or more groups. All values must be whole numbers zero or greater, because the factorial of a negative number is undefined.

## Syntax

```excel
=MULTINOMIAL(number1, [number2], ...)
```

<!-- Image 1: Group Sizes and Total. See Images/Math & Trig/MULTINOMIAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The size of the first group. It must be a number zero or greater. |
| `number2`, ... | No | The sizes of the remaining groups. Microsoft Excel accepts 1 to 255 values in total. |

### Return Value

A whole number: the factorial of the sum of the values divided by the product of each value's factorial. MULTINOMIAL returns `#NUM!` when any argument is negative, and `#VALUE!` when any argument is not numeric.

<!-- Image 2: Splitting a Total Into Groups. See Images/Math & Trig/MULTINOMIAL.md -->

## Examples

### Example 1: Four Groups of Varying Size

```excel
=MULTINOMIAL(2, 3, 4)
```

**Result:** `1260`

The total is 9, and 9! = 362880. Dividing by 2! x 3! x 4! = 2 x 6 x 24 = 288 gives 1260.

### Example 2: Three Groups

```excel
=MULTINOMIAL(3, 2, 1)
```

**Result:** `60`

The total is 6, and 6! = 720. Dividing by 3! x 2! x 1! = 12 gives 60.

### Example 3: Two Groups Match COMBIN

```excel
=MULTINOMIAL(2, 2)
```

**Result:** `6`

The result equals COMBIN(4, 2), which is also 6. With two groups the two functions agree.

### Example 4: Negative Group Size

```excel
=MULTINOMIAL(2, -1, 3)
```

**Result:** `#NUM!`

Any argument below zero is rejected.

### Example 5: Text Input

```excel
=MULTINOMIAL(2, "three")
```

**Result:** `#VALUE!`

A non-numeric argument is rejected.

## Story Problems

### Problem 1: Splitting Volunteers Across Tasks

A community fair has six volunteers. The coordinator needs three for setup, two for registration, and one for cleanup. The group sizes are in `B2:B4`.

| Task | Volunteers |
| --- | --- |
| Setup | 3 |
| Registration | 2 |
| Cleanup | 1 |

**Task:** Count the different ways to assign the six volunteers to the three tasks.

**Solution:**

```excel
=MULTINOMIAL(B2, B3, B4)
```

**Answer:** `60`. The calculation is 6! / (3! x 2! x 1!) = 720 / (6 x 2 x 1) = 720 / 12 = 60, because the order of volunteers within each task does not matter.

### Problem 2: Kitchen Ticket Lanes

A kitchen has nine tickets to route to three stations. Station one takes five tickets, station two takes three, and station three takes one. The counts are in `B2:B4`.

| Station | Tickets |
| --- | --- |
| Grill | 5 |
| Fry | 3 |
| Garnish | 1 |

**Task:** Calculate how many distinct ways the nine tickets can be split across the three stations.

**Solution:**

```excel
=MULTINOMIAL(B2, B3, B4)
```

**Answer:** `504`. The calculation is 9! / (5! x 3! x 1!) = 362880 / 720 = 504.

## Use Cases

### Anagram Counts

**Scenario:** A puzzle designer wants to know how many distinct arrangements the letters in a word can have.

```excel
=MULTINOMIAL(LetterCountA, LetterCountN, LetterCountB)
```

**Why It Works:** Repeated letters do not create new arrangements, so dividing by the factorial of each letter count removes the duplicates. For BANANA, the call is MULTINOMIAL(3, 2, 1), which gives 60.

### Committee Partitions

**Scenario:** A board must split its members into three committees of set sizes, and the planner wants to know how many splits are possible.

```excel
=MULTINOMIAL(SizeA, SizeB, SizeC)
```

**Why It Works:** The formula counts the distinct ways the members can fill each committee, which helps size scenario analysis before a vote.

### Sample Allocation Counts

**Scenario:** A quality team assigns a fixed number of inspections across three product lines and wants to compare the possible allocations.

```excel
=MULTINOMIAL(LinesA, LinesB, LinesC)
```

**Why It Works:** The result gives the number of distinct allocations for the stated counts, which can be compared with the total when assessing a sampling plan.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | One argument is negative. | Check the source cells for negative values and correct them. |
| `#VALUE!` | An argument is text or an empty cell that should contain a number. | Convert text to numbers or fill the blank. |
| Very large result shown in exponent form | The total is large, so the answer has many digits. | Format the cell as a number with no decimals. |
| Unexpected result | A group cell holds a running total instead of the group size. | Check that each argument is the size of one group. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Accepts 1 to 255 values. Returns `#NUM!` for negative arguments. |
| Google Sheets | Available | Accepts ranges as arguments. The help page states a limit of 30 arguments but notes that Sheets accepts any number. It does not describe negative input. |

## Tips and Best Practices

- Use MULTINOMIAL when there are three or more groups, and use COMBIN for two.
- Enter each group size in its own cell so the calculation can be audited.
- Check that the group sizes add up to the total you intend to split.
- Expect very large results quickly as the total grows, and format the cell accordingly.
- Use FACT to check intermediate factorials when you verify a result by hand.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBIN](COMBIN.md) | Counts the ways to choose items for two groups, a special case of MULTINOMIAL. |
| [FACT](FACT.md) | Returns the factorial that the formula uses in its numerator and denominator. |
| [FACTDOUBLE](FACTDOUBLE.md) | Returns the double factorial, a related counting function. |
| [SUM](SUM.md) | Adds the group sizes to find the total used in the numerator. |

## Official Documentation

- [Microsoft Support: MULTINOMIAL function](https://support.microsoft.com/en-us/excel/functions/multinomial-function)
- [Google Docs Editors Help: MULTINOMIAL](https://support.google.com/docs/answer/3093429)
