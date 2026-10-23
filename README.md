<p align="center">
  <img src="assets/functions-terminal.svg" alt="functions terminal logo" width="900">
</p>

<p align="center">
  A searchable, category-first reference library for spreadsheet formulas in Microsoft Excel and Google Sheets.
</p>

<p align="center">
  <a href="#browse-the-library">browse the library</a> · <a href="#quick-start">quick start</a> · <a href="#contributing">contributing</a>
</p>

<p align="center">
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/blob/main/LICENSE"><img src="https://img.shields.io/github/license/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=license" alt="MIT License"></a>
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/commits/main"><img src="https://img.shields.io/github/last-commit/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=updated" alt="Last commit"></a>
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions"><img src="https://img.shields.io/github/languages/top/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6" alt="Top language"></a>
  <a href="https://github.com/klappe-pm/Spreadsheet-Functions/issues"><img src="https://img.shields.io/github/issues/klappe-pm/Spreadsheet-Functions?style=flat-square&color=4ef0b6&label=issues" alt="Open issues"></a>
</p>

## built-for-the-cell-you-are-in

This repository turns a large spreadsheet formula reference into a navigable knowledge base. Each function has its own Markdown page, grouped by the way people actually look for formulas: text cleanup, lookups, financial models, dynamic arrays, statistics, and more.

```text
$ cd Functions
$ open "Lookup & Reference/XLOOKUP.md"

XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

## quick-start

1. Pick a category in the navigation tree below.
2. Open the formula page you need.
3. Copy the syntax, adapt the examples, and keep building.

The library covers both evergreen spreadsheet workhorses and newer Excel and Google Sheets functions. Where functions are platform-specific, the category makes that distinction visible.

## browse-the-library

**532 function references** organized across **15 categories**.

<details open>
<summary><strong>navigation tree</strong></summary>

```text
Functions/
├── Cube/                     6 functions
├── Database/                12 functions
├── Date & Time/             25 functions
├── Dynamic Arrays/           7 functions
├── Engineering/             54 functions
├── Excel-specific/          39 functions
├── Financial/               54 functions
├── Google-specific/         32 functions
├── Information/             22 functions
├── Logical/                 14 functions
├── Lookup & Reference/      29 functions
├── Math & Trig/             72 functions
├── Statistical/            125 functions
├── Text/                    40 functions
└── Web/                      1 function
```

</details>

| category | useful starting points |
| --- | --- |
| [dynamic arrays](Functions/Dynamic%20Arrays) | [FILTER](Functions/Dynamic%20Arrays/FILTER.md), [LET](Functions/Dynamic%20Arrays/LET.md), [XLOOKUP](Functions/Dynamic%20Arrays/XLOOKUP.md) |
| [lookups and reference](Functions/Lookup%20%26%20Reference) | [INDEX](Functions/Lookup%20%26%20Reference/INDEX.md), [MATCH](Functions/Lookup%20%26%20Reference/MATCH.md), [VLOOKUP](Functions/Lookup%20%26%20Reference/VLOOKUP.md), [XLOOKUP](Functions/Lookup%20%26%20Reference/XLOOKUP.md) |
| [math and trigonometry](Functions/Math%20%26%20Trig) | [ROUND](Functions/Math%20%26%20Trig/ROUND.md), [SUM](Functions/Math%20%26%20Trig/SUM.md), [SUMIFS](Functions/Math%20%26%20Trig/SUMIFS.md) |
| [statistical](Functions/Statistical) | [AVERAGE](Functions/Statistical/AVERAGE.md), [COUNTIFS](Functions/Statistical/COUNTIFS.md), [MEDIAN](Functions/Statistical/MEDIAN.md) |
| [text](Functions/Text) | [CLEAN](Functions/Text/CLEAN.md), [TEXTJOIN](Functions/Text/TEXTJOIN.md), [TRIM](Functions/Text/TRIM.md) |
| [date and time](Functions/Date%20%26%20Time) | [DATE](Functions/Date%20%26%20Time/DATE.md), [NETWORKDAYS](Functions/Date%20%26%20Time/NETWORKDAYS.md), [WORKDAY](Functions/Date%20%26%20Time/WORKDAY.md) |
| [financial](Functions/Financial) | [FV](Functions/Financial/FV.md), [IRR](Functions/Financial/IRR.md), [PMT](Functions/Financial/PMT.md), [XIRR](Functions/Financial/XIRR.md) |
| [logical](Functions/Logical) | [IF](Functions/Logical/IF.md), [IFERROR](Functions/Logical/IFERROR.md), [IFS](Functions/Logical/IFS.md) |
| [Google Sheets](Functions/Google-specific) | [GOOGLEFINANCE](Functions/Google-specific/GOOGLEFINANCE.md), [QUERY](Functions/Google-specific/QUERY.md), [SPARKLINE](Functions/Google-specific/SPARKLINE.md) |
| [Excel](Functions/Excel-specific) | [LAMBDA](Functions/Excel-specific/LAMBDA.md), [MAP](Functions/Excel-specific/MAP.md), [TEXTSPLIT](Functions/Excel-specific/TEXTSPLIT.md) |

For a visual route through the library, visit the [diagram collection](Diagrams/README.md).

## what-you-will-find

- Individual pages for functions, organized by category.
- Formula syntax and reference material designed for quick lookup.
- Excel-only and Google Sheets-only collections alongside shared functions.
- Diagrams that help map related functions before choosing one.

## contributing

Spotted a missing function, a confusing explanation, or an example that could be better? [Open an issue](https://github.com/klappe-pm/Spreadsheet-Functions/issues/new) with the formula name, platform, and the improvement you have in mind. For a direct correction, [open a pull request](https://github.com/klappe-pm/Spreadsheet-Functions/compare).

## license

This project is available under the [MIT License](LICENSE).

<p align="center">
  <sub>Made for the moment when the right function is one search away.</sub>
</p>
