# Excel and Google Sheets Functions in Absurd Detail

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-purple?logo=obsidian)](https://obsidian.md/)
[![Functions](https://img.shields.io/badge/Functions-530+-brightgreen)](./Functions/)
[![Categories](https://img.shields.io/badge/Categories-15-blue)](./Functions/)
[![Documentation](https://img.shields.io/badge/Documentation-In_Progress-yellow)](./README.md)

A comprehensive, opinionated documentation system for Excel and Google Sheets functions. This isn't just another function reference—it's **absurdly detailed** explanations of what each function does, **why** you'd use it, **when** to choose alternatives, and **how** to avoid common pitfalls. Every function includes 10+ real-world examples, official Microsoft/Google documentation links, and platform difference warnings.

## What Makes This Different?

Most function references tell you `SUM(number1, [number2], ...)` and leave you to figure out the rest. This project gives you:

- **Verbose explanations** that explain the *concept*, not just the syntax
- **10-15+ examples per function** with realistic business scenarios
- **Common errors table** with causes and solutions
- **Platform differences** between Excel and Google Sheets
- **Tips and best practices** from real-world usage
- **Official documentation links** to Microsoft and Google support pages
- **Related functions** with guidance on when to use alternatives

## Function Categories

| Category | Functions | Description |
|----------|-----------|-------------|
| **Statistical** | 125 | Distributions, averages, correlation, regression |
| **Math & Trig** | 72 | Arithmetic, trigonometry, matrix, rounding |
| **Engineering** | 54 | Number systems, complex numbers, conversions |
| **Financial** | 54 | Investments, loans, depreciation, yield, NPV, IRR |
| **Text** | 40 | String manipulation, formatting, search |
| **Excel-specific** | 39 | LAMBDA, dynamic arrays, advanced features |
| **Google-specific** | 32 | IMPORT functions, QUERY, Sheets-exclusive |
| **Lookup & Reference** | 29 | VLOOKUP, INDEX/MATCH, XLOOKUP |
| **Date & Time** | 25 | Date arithmetic, formatting, business days |
| **Information** | 22 | Type checking, error validation, metadata |
| **Logical** | 14 | IF statements, Boolean logic, conditionals |
| **Database** | 12 | DAVERAGE, DCOUNT, criteria-based operations |
| **Dynamic Arrays** | 7 | UNIQUE, SORT, FILTER, modern array functions |
| **Cube** | 6 | OLAP functions for business intelligence |
| **Web** | 1 | Web services and data import |

## Documentation Format

Every function file follows this comprehensive structure:

```markdown
# FUNCTION_NAME

## Description
[4 paragraphs: What it does, Why/when to use it, Gotchas and comparisons, Platform notes]

## Syntax
> [!f(x)] FUNCTION_NAME Syntax
> =FUNCTION_NAME(param1, param2, [optional_param])

### Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| param1    | Yes      | Detailed explanation |

### Return Value
[What the function returns]

## Examples
### Example 1: Basic Usage
[10-15 examples with formulas, results, and explanations]

## Common Errors
| Error | Cause | Solution |
|-------|-------|----------|

## Use Cases
### [[Business Scenario 1]]
**Scenario:** [Real-world problem]
**Implementation:** [Formula]
**Business Application:** [How this solves the problem]
**Technical Details:** [Important considerations]

## Platform Differences
### Microsoft Excel
- Availability, specific behaviors

### Google Sheets
- Availability, specific behaviors, differences

## Tips and Best Practices
1. [6-8 actionable tips]

## Related Functions
### Similar Functions
| Function | Description | When to Use Instead |

### Commonly Used Together
[Functions frequently combined with this one]

## Official Documentation
- Microsoft Excel: [Link]
- Google Sheets: [Link]

## Version History
| Platform | Version Introduced | Notes |
```

## Recently Updated Functions (January 2026)

### Core Functions (Fully Rewritten)
- **IF, AND, OR, NOT** - Complete logical function documentation with truth tables
- **IFS, IFERROR, IFNA, SWITCH** - Modern alternatives to nested IF
- **SUM, SUMIF, SUMIFS** - Aggregation with conditional logic
- **VLOOKUP, INDEX, MATCH, HLOOKUP** - Comprehensive lookup coverage
- **AVERAGE, COUNT, COUNTA, COUNTIF, COUNTIFS** - Statistical basics

### Google Sheets Exclusive (Fully Rewritten)
- **QUERY** - SQL-like queries with 15+ examples
- **IMPORTRANGE** - Cross-spreadsheet data with permission handling
- **ARRAYFORMULA** - Array processing for bulk operations
- **GOOGLEFINANCE** - Stock data with all attributes documented
- **IMPORTHTML, IMPORTDATA, IMPORTFEED, IMPORTXML** - Web data imports with XPath

### Financial Functions (Fully Rewritten)
- **NPV, IRR, PMT, PV, FV** - Time value of money with sign conventions explained

### Text Functions (Fully Rewritten)
- **LEFT, RIGHT, MID, LEN, TRIM** - String extraction and cleaning
- **CONCATENATE, TEXT** - String building and formatting

### Date & Time Functions (Fully Rewritten)
- **TODAY, NOW, DATE, YEAR, MONTH, DAY** - Date components and calculations

### Math Functions (Fully Rewritten)
- **ROUND, ROUNDUP, ROUNDDOWN, ABS, SQRT, MOD** - Rounding and arithmetic

### Dynamic Arrays (Fully Rewritten)
- **FILTER, SORT, UNIQUE** - Modern array functions for both platforms

## Getting Started

### Using with Obsidian (Recommended)
```bash
git clone https://github.com/your-repo/Excel-and-Sheets-Functions-in-Absurd-Detail.git
# Open Obsidian > Open folder as vault > Select cloned folder
```

### Using as Reference
Browse the `/Functions/` directory by category. Each `.md` file is self-contained documentation.

## Official Documentation Links

- **Microsoft Excel:** [Excel Functions Alphabetical](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
- **Microsoft Excel by Category:** [Excel Functions by Category](https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb)
- **Google Sheets:** [Google Sheets Function List](https://support.google.com/docs/table/25273)

## Contributing

This project is a work in progress. Contributions are welcome:

1. Fork the repository
2. Follow the TEMPLATE.md format (in repository root)
3. Include realistic examples and official documentation links
4. Note platform differences between Excel and Sheets
5. Submit a pull request

## License

This project is open source under the [MIT License](LICENSE).

---

*Last Updated: January 10, 2026 | 60+ Functions Comprehensively Documented | ~470 Remaining*

## Recent Changes (January 10, 2026)

### Major Documentation Overhaul
- **New Template:** Comprehensive format with 10+ examples, error tables, platform differences
- **63 Functions Rewritten:** Complete rewrites with verbose explanations
- **Official References:** All updated functions include Microsoft and Google documentation links
- **Platform Warnings:** Clear documentation of Excel vs Sheets differences
- **Real Examples:** Business scenarios instead of placeholder text

### Quality Improvements
- Removed all generic placeholder descriptions ("performs specialized calculations")
- Added proper parameter tables with Required column
- Included common error troubleshooting
- Added tips and best practices sections
- Cross-linked related functions with usage guidance
