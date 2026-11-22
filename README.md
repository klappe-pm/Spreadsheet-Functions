<p align="center">
  <img src="assets/functions-terminal.svg" alt="functions terminal logo" width="900">
</p>

<p align="center">
  A searchable, category-first reference library for spreadsheet functions in Microsoft Excel and Google Sheets.
</p>

<p align="center">
  <a href="#browse-the-library">Browse the Library</a> · <a href="#quick-start">Quick Start</a> · <a href="#frontmatter-schema">Frontmatter Schema</a> · <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/blob/main/LICENSE"><img src="https://img.shields.io/github/license/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=license" alt="MIT License"></a>
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/commits/main"><img src="https://img.shields.io/github/last-commit/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=updated" alt="Last commit"></a>
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/issues"><img src="https://img.shields.io/github/issues/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=issues" alt="Open issues"></a>
</p>

## Built for the Cell You Are In

Each function has one page, filed under its official category: the Microsoft Excel category for functions Excel supports, or the Google Sheets category for functions only Sheets supports. Every page follows the same layout: description, syntax and parameters, worked examples, story problems, use cases, common errors, platform differences, tips, related functions and links to the official Microsoft and Google documentation.

```text
Functions/Lookup & Reference/XLOOKUP.md

=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

## Quick Start

1. Pick a category in the navigation tree below.
2. Open the function page you need.
3. Copy the syntax, work through an example, then try the story problems.

Each page states whether the function runs in Excel, Google Sheets or both. Where the two platforms behave differently, the Platform Differences table says how.

## Browse the Library

**576 function pages** in **14 categories**.

<details open>
<summary><strong>Navigation Tree</strong></summary>

```text
Functions/
├── Add-in & Automation/      3 functions
├── Cube/                     7 functions
├── Database/                13 functions
├── Date & Time/             26 functions
├── Engineering/             57 functions
├── Financial/               55 functions
├── Google-specific/         29 functions
├── Information/             26 functions
├── Logical/                 19 functions
├── Lookup & Reference/      41 functions
├── Math & Trig/             83 functions
├── Statistical/            151 functions
├── Text/                    54 functions
└── Web/                     12 functions
```

</details>

| Category | Useful Starting Points |
| --- | --- |
| [Lookup and Reference](Functions/Lookup%20%26%20Reference) | [XLOOKUP](Functions/Lookup%20%26%20Reference/XLOOKUP.md), [FILTER](Functions/Lookup%20%26%20Reference/FILTER.md), [INDEX](Functions/Lookup%20%26%20Reference/INDEX.md), [MATCH](Functions/Lookup%20%26%20Reference/MATCH.md), [GROUPBY](Functions/Lookup%20%26%20Reference/GROUPBY.md) |
| [Logical](Functions/Logical) | [IF](Functions/Logical/IF.md), [IFS](Functions/Logical/IFS.md), [LET](Functions/Logical/LET.md), [LAMBDA](Functions/Logical/LAMBDA.md), [MAP](Functions/Logical/MAP.md) |
| [Math and Trigonometry](Functions/Math%20%26%20Trig) | [SUM](Functions/Math%20%26%20Trig/SUM.md), [SUMIFS](Functions/Math%20%26%20Trig/SUMIFS.md), [SUMPRODUCT](Functions/Math%20%26%20Trig/SUMPRODUCT.md), [ROUND](Functions/Math%20%26%20Trig/ROUND.md), [SEQUENCE](Functions/Math%20%26%20Trig/SEQUENCE.md) |
| [Statistical](Functions/Statistical) | [AVERAGE](Functions/Statistical/AVERAGE.md), [COUNTIFS](Functions/Statistical/COUNTIFS.md), [MEDIAN](Functions/Statistical/MEDIAN.md), [STDEV.S](Functions/Statistical/STDEV.S.md), [FORECAST.LINEAR](Functions/Statistical/FORECAST.LINEAR.md) |
| [Text](Functions/Text) | [TEXTSPLIT](Functions/Text/TEXTSPLIT.md), [TEXTJOIN](Functions/Text/TEXTJOIN.md), [TRIM](Functions/Text/TRIM.md), [REGEXEXTRACT](Functions/Text/REGEXEXTRACT.md), [TEXT](Functions/Text/TEXT.md) |
| [Date and Time](Functions/Date%20%26%20Time) | [DATE](Functions/Date%20%26%20Time/DATE.md), [EOMONTH](Functions/Date%20%26%20Time/EOMONTH.md), [NETWORKDAYS](Functions/Date%20%26%20Time/NETWORKDAYS.md), [WORKDAY](Functions/Date%20%26%20Time/WORKDAY.md) |
| [Financial](Functions/Financial) | [PMT](Functions/Financial/PMT.md), [NPV](Functions/Financial/NPV.md), [IRR](Functions/Financial/IRR.md), [XIRR](Functions/Financial/XIRR.md) |
| [Google Sheets](Functions/Google-specific) | [QUERY](Functions/Google-specific/QUERY.md), [ARRAYFORMULA](Functions/Google-specific/ARRAYFORMULA.md), [GOOGLEFINANCE](Functions/Google-specific/GOOGLEFINANCE.md), [AI](Functions/Google-specific/AI.md) |
| [Web](Functions/Web) | [IMPORTRANGE](Functions/Web/IMPORTRANGE.md), [IMPORTXML](Functions/Web/IMPORTXML.md), [WEBSERVICE](Functions/Web/WEBSERVICE.md) |

## What You Will Find

- One page per function, verified against the official Microsoft and Google documentation.
- Story problems: short original business scenarios with data, a task, a solution formula and the answer.
- Legacy compatibility functions (such as NORMDIST and STDEV) marked with their modern replacements.
- An image guide for every page in [Images](Images), describing where each planned illustration goes and what it shows.
- Mermaid relationship diagrams in [Diagrams](Diagrams/README.md).
- A [change log](CHANGELOG.md) of the library's revisions.

## Frontmatter Schema

Every function page opens with the same YAML keys, in this order. The [template](TEMPLATE.md) shows the full page layout.

| Key | Meaning |
| --- | --- |
| `domain` | Always Spreadsheet Functions. |
| `category` | The folder the page lives in. |
| `subcategory` | A group inside the category, such as Modern Lookup or Legacy Compatibility. |
| `purpose` | One or more values from the purpose vocabulary below. |
| `use-case` | Business scenarios the function serves. |
| `related` | Other functions in this library, for linking and graph views. |
| `level` | Technical depth from 1 to 5 (see below). |
| `source` | Official Microsoft and Google documentation URLs. |
| `date-created` | When the page was first written. |
| `date-revised` | When the content last changed. |
| `aliases` | Alternate search phrases. |
| `tags` | Lowercase tags, including `excel` and `sheets` for platform support. |

### Levels

| Level | Name | Typical Functions |
| --- | --- | --- |
| 1 | Foundational | SUM, TODAY, UPPER, ABS |
| 2 | Core | IF, COUNTIFS, VLOOKUP, ROUND, TEXT |
| 3 | Intermediate | INDEX, MATCH, XLOOKUP, FILTER, SUMPRODUCT, PMT |
| 4 | Advanced | LET, LAMBDA, MAP, REDUCE, QUERY, GROUPBY, XIRR |
| 5 | Specialist | Bessel functions, complex numbers, CUBE functions, add-in functions |

### Purpose Vocabulary

Add-in Automation, Aggregation, AI Assistance, Arithmetic Operations, Array Shaping, Bitwise Operations, Bond Analysis, Complex Numbers, Conditional Logic, Counting, Data Cleaning, Data Import, Data Retrieval, Data Validation, Database Queries, Date Calculation, Depreciation, Error Handling, Financial Modeling, Forecasting, Hypothesis Testing, Investment Analysis, Loan Analysis, Matrix Math, Number Base Conversion, Number Formatting, OLAP Analysis, Probability, Randomization, Ranking, Reference Building, Regression, Rounding, Sorting and Filtering, Special Functions, Statistical Analysis, Text Manipulation, Time Calculation, Trigonometry, Type Checking, Unit Conversion, Workbook Information.

## Contributing

Spotted a missing function, a confusing explanation or an example that could be better? [Open an issue](https://github.com/klappe-pm/Spreadsheet-Functions/issues/new) with the function name, the platform and the improvement you have in mind. For a direct correction, [open a pull request](https://github.com/klappe-pm/Spreadsheet-Functions/compare) that follows the [template](TEMPLATE.md).

## License

This project is available under the [MIT License](LICENSE).

<p align="center">
  <sub>Made for the moment when the right function is one search away.</sub>
</p>
