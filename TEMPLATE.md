---
categories:
- spreadsheet-functions
subCategories:
- excel     # Include if available in Excel
- sheets    # Include if available in Google Sheets
topics:
- category-name    # One of: statistical, math-trig, engineering, financial, text, lookup-reference, date-time, information, logical, database, dynamic-arrays, cube, web, excel-specific, google-specific
subTopics: []
dateCreated: 'YYYY-MM-DD'
dateRevised: 'YYYY-MM-DD'
aliases: []
tags: []
---

# FUNCTION_NAME

## Description

<!--
REQUIREMENTS FOR DESCRIPTION:
- Minimum 3-4 paragraphs explaining the function in detail
- Paragraph 1: What the function does in plain English
- Paragraph 2: Why/when you would use this function (real-world context)
- Paragraph 3: How it differs from similar functions or common gotchas
- Paragraph 4 (optional): Historical context, version availability, platform differences
-->

**FUNCTION_NAME** [detailed explanation of what this function does, written for someone who has never seen it before. Explain the concept, not just the mechanics. What problem does this function solve?]

[Second paragraph explaining when and why you would use this function in real-world scenarios. Give context about the business problems or data analysis tasks this function helps solve. Be specific about use cases.]

[Third paragraph discussing important considerations, limitations, common mistakes, or how this function compares to similar alternatives. If there are platform differences between Excel and Google Sheets, explain them here.]

[Fourth paragraph (optional) covering version availability, when this function was introduced, or any historical context that helps users understand compatibility.]

## Syntax

> [!f(x)] FUNCTION_NAME Syntax
>
> ```
> =FUNCTION_NAME(required_param1, required_param2, [optional_param1], [optional_param2])
> ```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `required_param1` | Yes | [Detailed description of this parameter - what values are accepted, what data types work, what happens with edge cases] |
| `required_param2` | Yes | [Detailed description] |
| `optional_param1` | No | [Detailed description including what the default value is if omitted] |
| `optional_param2` | No | [Detailed description] |

### Return Value

[Describe what the function returns - data type, possible values, error conditions]

## Examples

> [!f(x)] FUNCTION_NAME Examples

### Example 1: Basic Usage
```
=FUNCTION_NAME(value1, value2)
```
**Result:** `expected_result`

**Explanation:** [Detailed explanation of what this example demonstrates and why you would use it this way]

---

### Example 2: With Optional Parameters
```
=FUNCTION_NAME(value1, value2, optional_value)
```
**Result:** `expected_result`

**Explanation:** [Explanation of how the optional parameter changes the behavior]

---

### Example 3: Real-World Scenario - [Scenario Name]
```
=FUNCTION_NAME(A1:A100, B1, "criteria")
```
**Result:** `expected_result`

**Explanation:** [A realistic business scenario showing how this would be used with actual data. Include sample data context.]

---

### Example 4: Combined with Other Functions
```
=OTHER_FUNCTION(FUNCTION_NAME(A1, B1), C1)
```
**Result:** `expected_result`

**Explanation:** [Show how this function works in combination with other common functions]

---

### Example 5: Handling Edge Cases
```
=FUNCTION_NAME(edge_case_value)
```
**Result:** `expected_result or #ERROR!`

**Explanation:** [Demonstrate what happens with empty cells, zeros, errors, or other edge cases]

---

### Example 6: Array/Range Application
```
=FUNCTION_NAME(A1:A10, B1:B10)
```
**Result:** `expected_result`

**Explanation:** [If applicable, show how the function works with ranges or as an array formula]

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#VALUE!` | [Description of what causes this error] | [How to fix it] |
| `#REF!` | [Description] | [Solution] |
| `#NAME?` | [Description] | [Solution] |
| `#N/A` | [Description] | [Solution] |

## Use Cases

### [[Use Case 1: Descriptive Name]]

**Scenario:** [Describe a specific, realistic business scenario]

**Implementation:**
```
=FUNCTION_NAME(specific_formula_for_this_use_case)
```

**Business Application:** [How this solves a real business problem]

**Technical Details:** [Any important technical considerations for this use case]

---

### [[Use Case 2: Descriptive Name]]

**Scenario:** [Different realistic scenario]

**Implementation:**
```
=FUNCTION_NAME(specific_formula)
```

**Business Application:** [Real-world application]

**Technical Details:** [Technical considerations]

---

### [[Use Case 3: Descriptive Name]]

**Scenario:** [Third scenario]

**Implementation:**
```
=FUNCTION_NAME(specific_formula)
```

**Business Application:** [Application]

**Technical Details:** [Details]

## Platform Differences

### Microsoft Excel
- **Availability:** Excel 2007+ / Excel 365 / Excel Online
- **Specific Behavior:** [Any Excel-specific behavior or syntax]

### Google Sheets
- **Availability:** All versions
- **Specific Behavior:** [Any Sheets-specific behavior or syntax differences]

## Tips and Best Practices

1. **[Tip Title]:** [Practical advice for using this function effectively]
2. **[Tip Title]:** [Another useful tip]
3. **[Tip Title]:** [Performance considerations, if any]
4. **[Tip Title]:** [Common mistakes to avoid]

## Related Functions

### Similar Functions
| Function | Description | When to Use Instead |
|----------|-------------|---------------------|
| [[SIMILAR_FUNCTION_1]] | [Brief description] | [When you'd choose this over the current function] |
| [[SIMILAR_FUNCTION_2]] | [Brief description] | [When to use this one] |
| [[SIMILAR_FUNCTION_3]] | [Brief description] | [When to use this one] |

### Commonly Used Together

**[[FUNCTION_A]]** - [Brief description of FUNCTION_A]

*Combined with FUNCTION_NAME for [specific purpose]:*
```
=FUNCTION_A(FUNCTION_NAME(A1:A10), additional_params)
```
[Explanation of what this combination accomplishes]

---

**[[FUNCTION_B]]** - [Brief description]

*Combined with FUNCTION_NAME for [specific purpose]:*
```
=FUNCTION_B(FUNCTION_NAME(value), other_value)
```
[Explanation]

---

**[[FUNCTION_C]]** - [Brief description]

*Combined with FUNCTION_NAME for [specific purpose]:*
```
=IF(FUNCTION_NAME(A1)>threshold, "Yes", "No")
```
[Explanation]

## Official Documentation

- **Microsoft Excel:** [FUNCTION_NAME function](https://support.microsoft.com/en-us/office/function_name-function-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
- **Google Sheets:** [FUNCTION_NAME](https://support.google.com/docs/answer/xxxxxxx)

## Version History

| Platform | Version Introduced | Notes |
|----------|-------------------|-------|
| Excel | Excel 2007 | [Any notes about initial release] |
| Excel 365 | [Date] | [Any enhancements in 365] |
| Google Sheets | [Date] | [Notes] |

---

*Last updated: YYYY-MM-DD*
