---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- math-trig
subTopics:
- aggregation
- arithmetic
- totals
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
- Add
- Total
- Sum Function
tags:
- aggregation
- arithmetic
- totals
- basic-math
---

# SUM

## Description

**SUM** adds numbers together. That's it. It's the most fundamental spreadsheet function, the one you'll use more than any other, and the one that represents why spreadsheets exist in the first place—to do math on data automatically. You give SUM a range of cells or a list of numbers, and it returns their total.

While conceptually simple, SUM has nuances worth understanding. It ignores text values and logical values (TRUE/FALSE) within cell references—this is usually what you want, as headers and status columns won't pollute your totals. It handles errors by propagating them (one #REF! cell will make your entire SUM return #REF!), which is both a feature (you know something's wrong) and a hassle (you might want to sum despite errors).

**Why SUM instead of + signs?** You could write `=A1+A2+A3+A4+A5` instead of `=SUM(A1:A5)`, and it would work. But SUM is better for several reasons: (1) SUM ignores text and blanks while + would error, (2) SUM handles ranges that grow—add a row in the middle and SUM catches it while + doesn't, (3) SUM is readable—`SUM(Sales)` is clearer than a chain of additions, (4) SUM is faster on large datasets.

**SUM's siblings:** For conditional summing, use SUMIF (one condition) or SUMIFS (multiple conditions). For weighted sums or multiplying before summing, use SUMPRODUCT. For totals that respect filters, use SUBTOTAL or AGGREGATE. Master these and you'll handle 95% of spreadsheet aggregation needs.

## Syntax

> [!f(x)] SUM Syntax
>
> ```
> =SUM(number1, [number2], [number3], ...)
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `number1` | Yes | First number, cell reference, or range to add. Can be a single value (5), a cell (A1), a range (A1:A100), or a named range (MonthlySales). |
| `number2, number3, ...` | No | Additional numbers, cells, or ranges to include. Up to 255 arguments in Excel, practically unlimited in Google Sheets. Arguments can mix types—some ranges, some individual cells, some literal numbers. |

### Return Value

Returns a single numeric value representing the total of all numeric arguments. Text values and empty cells within ranges are ignored. If any argument is an error value, SUM returns that error.

## Examples

> [!f(x)] SUM Examples

### Example 1: Sum a Simple Range
```
=SUM(A1:A10)
```
**Result:** Total of all numbers in cells A1 through A10

**Explanation:** The most common SUM pattern—give it a range, get a total. If A1:A10 contains [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], the result is 550. Blank cells and text are ignored.

---

### Example 2: Sum Individual Cells
```
=SUM(A1, B5, C10, D15)
```
**Result:** Total of four specific cells

**Explanation:** When your numbers aren't in a contiguous range, list them individually. This is common when pulling key figures from different parts of a spreadsheet—like totaling quarterly subtotals that appear in different rows.

---

### Example 3: Sum Multiple Ranges
```
=SUM(A1:A10, C1:C10, E1:E10)
```
**Result:** Combined total of three separate ranges

**Explanation:** SUM accepts multiple range arguments. This totals column A, column C, and column E together. Useful when you have data in non-adjacent columns that need to be aggregated.

---

### Example 4: Mix Ranges with Literal Numbers
```
=SUM(A1:A10, 100, B1:B5, -50)
```
**Result:** Range totals plus 100 minus 50

**Explanation:** You can mix cell references with hardcoded numbers. The -50 subtracts (since SUM just adds all its arguments, and adding a negative subtracts). This pattern is useful for adjustments or offsets.

---

### Example 5: Sum an Entire Column
```
=SUM(A:A)
```
**Result:** Total of every number in column A

**Explanation:** Referencing an entire column (A:A) sums all values regardless of how many rows you add later. Convenient but can be slow with large datasets. Also watch out—this includes the header row if it contains a number!

---

### Example 6: Sum Across Sheets
```
=SUM(January!B2:B100, February!B2:B100, March!B2:B100)
```
**Result:** Q1 total across three monthly sheets

**Explanation:** SUM works across multiple sheets. Reference each sheet with SheetName! prefix. For many sheets, consider 3D references: `=SUM(January:March!B2:B100)` sums B2:B100 from January through March sheets.

---

### Example 7: Sum with Named Ranges
```
=SUM(MonthlySales, YearlyBonus, CommissionTotal)
```
**Result:** Total of three named ranges

**Explanation:** Named ranges make formulas readable and maintainable. `=SUM(MonthlySales)` is clearer than `=SUM(DataEntry!$F$5:$F$500)`. Define names via Formulas > Name Manager (Excel) or Data > Named Ranges (Sheets).

---

### Example 8: Handling Text in Ranges
```
=SUM(A1:A5) where A1:A5 contains [10, "N/A", 30, "", 50]
```
**Result:** 90 (ignores "N/A" and blank)

**Explanation:** SUM automatically skips text values and empty cells—no error, just ignores them. This is usually desirable: you don't want a "Total" label or a blank row breaking your formula.

---

### Example 9: Array Formula Sum (Legacy)
```
=SUM(IF(A1:A10>50, B1:B10, 0))
```
(Entered with Ctrl+Shift+Enter in older Excel)
**Result:** Sum of B values where corresponding A values exceed 50

**Explanation:** Before SUMIF existed (or when you need complex conditions), array SUM formulas provided conditional summing. Modern Excel and Sheets handle this natively, but you'll encounter this pattern in legacy spreadsheets.

---

### Example 10: Summing Filtered Data (Why SUM Doesn't Work)
```
=SUM(A1:A100)      → Sums ALL values (ignores filters)
=SUBTOTAL(9, A1:A100)  → Sums only VISIBLE values
```
**Result:** Different totals when data is filtered

**Explanation:** SUM always totals everything in the range, regardless of row visibility from filtering or hiding. To sum only visible cells, use SUBTOTAL with function number 9 (sum) or 109 (sum ignoring hidden rows).

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#REF!` | Reference to deleted cells, or circular reference | Check if any referenced cells have been deleted. Look for accidentally self-referencing formulas. |
| `#VALUE!` | Rarely occurs with SUM since it ignores text, but can happen with certain array operations | Verify array formula syntax if using advanced patterns. |
| `#NAME?` | Misspelled function name or undefined named range | Check spelling. If using named ranges, ensure they're defined. |
| `Wrong total` | Included header row or unexpected cells | Verify your range—A:A includes row 1, which might be a header. Use A2:A instead if needed. |
| `0 when expecting value` | Range is empty or contains only text | Ensure your range actually contains numeric data. Check for text-formatted numbers. |
| `Circular reference warning` | SUM range includes the cell containing the formula | Move your SUM to a cell outside the summed range. |

## Use Cases

### [[Monthly Budget Tracking]]

**Scenario:** Total all expense categories to show monthly spending.

**Implementation:**
```
=SUM(C5:C15)
```
Where C5:C15 contains individual expense amounts (Rent, Utilities, Groceries, etc.)

**Business Application:** Personal finance tracking, departmental expense reports, project cost monitoring. The simplest and most common aggregation task.

**Technical Details:** Consider using named ranges for categories (`=SUM(Expenses)`) and SUMIF when you need category-level subtotals within a larger dataset.

---

### [[Sales Territory Rollup]]

**Scenario:** Calculate total sales for a region by summing individual rep totals across multiple sheets.

**Implementation:**
```
=SUM(JanSales!D15, FebSales!D15, MarSales!D15)
```
Or using 3D reference: `=SUM(JanSales:MarSales!D15)`

**Business Application:** Quarterly and annual sales reporting, regional performance comparison, commission pool calculation.

**Technical Details:** 3D references (SheetStart:SheetEnd!Range) only work when sheets are contiguous. Adding a sheet in the middle automatically includes it in the sum—be careful with sheet ordering.

---

### [[Running Total Calculation]]

**Scenario:** Create a cumulative sum column showing running balance.

**Implementation:**
```
Cell C2: =SUM($B$2:B2)
Cell C3: =SUM($B$2:B3)
...drag down...
```
Or in C2 with OFFSET: `=SUM($B$2:B2)` and drag down

**Business Application:** Cash flow tracking, inventory counts, cumulative revenue reporting. Shows how totals build over time.

**Technical Details:** The mixed reference $B$2:B2 keeps the start fixed while the end grows as you drag down. This creates an expanding range—classic running total pattern.

---

### [[Cross-Departmental Budget Aggregation]]

**Scenario:** Combine budget figures from multiple departments' columns into a company-wide total.

**Implementation:**
```
=SUM(Marketing!C:C, Sales!C:C, Engineering!C:C, Operations!C:C)
```

**Business Application:** Executive reporting, board presentations, annual planning. Aggregates across organizational units.

**Technical Details:** Full-column references (C:C) ensure new entries are automatically included. For performance on large files, consider specific ranges (C2:C1000) instead.

## Platform Differences

### Microsoft Excel
- **Availability:** All versions (original function from Excel 1.0)
- **Argument limit:** 255 arguments maximum
- **Performance:** Optimized for large ranges; full-column references (A:A) perform well
- **3D references:** Fully supported for summing across sheet ranges

### Google Sheets
- **Availability:** All versions
- **Argument limit:** Practically unlimited (30,000+ cells per argument)
- **Performance:** Can slow on very large full-column references
- **3D references:** Not supported; must list sheets individually

### Both Platforms
- Text and empty cells are ignored within ranges
- Errors propagate (one error cell causes SUM to error)
- Logical values (TRUE/FALSE) in cell references are ignored
- Literal TRUE in arguments is treated as 1, FALSE as 0

## Tips and Best Practices

1. **Use ranges, not individual cells:** `=SUM(A1:A100)` beats `=A1+A2+A3+...` for readability, flexibility, and maintenance.

2. **Be careful with full-column references:** `=SUM(A:A)` includes row 1. If that's your header, you might accidentally sum a number-like header. Use `=SUM(A2:A)` (Sheets) or `=SUM(A2:A1048576)` (Excel) to skip headers.

3. **Use SUBTOTAL for filtered data:** If your data will be filtered, SUM still totals hidden rows. Use `=SUBTOTAL(9, range)` to sum only visible cells.

4. **Combine with IFERROR to handle errors gracefully:** If your range might contain errors: `=SUM(IFERROR(A1:A10, 0))` converts errors to 0 before summing (array formula in older Excel).

5. **Consider SUMPRODUCT for complex conditions:** When you need to multiply ranges before summing (like quantity × price), SUMPRODUCT is more elegant than nested SUMs.

6. **Name your ranges:** `=SUM(Q1_Revenue)` is infinitely more readable than `=SUM($D$15:$G$15,Sheet2!$D$15:$G$15)`.

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[SUMIF]] | Sum based on one condition | When summing only values matching a criterion |
| [[SUMIFS]] | Sum based on multiple conditions | When summing with multiple criteria across different columns |
| [[SUMPRODUCT]] | Sum of products of ranges | When multiplying arrays together before summing |
| [[SUBTOTAL]] | Sum with filter awareness | When summing data that may be filtered |
| [[AGGREGATE]] | Sum with error/hidden row handling | When you need to ignore errors or hidden rows flexibly |

### Commonly Used Together

**[[COUNT]]** - Count numeric values

*Combined with SUM for averages or validation:*
```
=SUM(A1:A10)/COUNT(A1:A10)   (Same as AVERAGE)
```
Verify your data has values before dividing.

---

**[[IF]]** - Conditional logic

*Combined with SUM for conditional totals (legacy approach):*
```
=SUM(IF(B1:B10="Sales", A1:A10, 0))
```
Array formula approach before SUMIF was widespread. SUMIF is cleaner now.

---

**[[IFERROR]]** - Error handling

*Combined with SUM to handle errors in range:*
```
=IFERROR(SUM(A1:A10), "Error in data")
```
Provides a custom message if SUM fails. For ignoring individual errors, use AGGREGATE.

---

**[[ROUND]]** - Rounding results

*Combined with SUM for clean totals:*
```
=ROUND(SUM(A1:A10), 2)
```
Currency totals often need rounding to avoid floating-point display issues like $99.99999999997.

---

**[[AVERAGE]]** - Calculate mean

*Related aggregation function:*
```
=AVERAGE(A1:A10)  is equivalent to  =SUM(A1:A10)/COUNT(A1:A10)
```
When you need the mean instead of the total.

## Official Documentation

- **Microsoft Excel:** [SUM function](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- **Google Sheets:** [SUM function](https://support.google.com/docs/answer/3093669)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 1.0 (1985) | Original function |
| Excel 2007+ | All subsequent | No changes to function behavior |
| Google Sheets | Original launch | Identical to Excel implementation |

---

*Last updated: 2026-01-10*
