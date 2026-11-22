---
domain: Spreadsheet Functions
category: Project
subcategory: Change Log
purpose:
  - Workbook Information
use-case:
  - Tracking Library Revisions
related: []
level: 1
source:
  - https://support.google.com/docs/table/25273
  - https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188
date-created: 2026-11-22
date-revised: 2026-11-22
aliases: []
tags:
  - changelog
---

# Change Log

## 2026-11-22: Full Library Audit and Rewrite

### Structure

- Every function now has exactly one page. 44 functions had two or three copies in different folders; the copies were merged into one page and the extras removed.
- Each page lives in its official category: the Microsoft Excel category when Excel supports the function, otherwise the Google Sheets category. Sheets-only functions in Google's Google, Array, Filter, Operator and Parser groups live in Google-specific.
- The Dynamic Arrays and Excel-specific folders were retired. Most of their functions also run in Google Sheets, so the folder names no longer described them. Their pages moved to Lookup & Reference, Logical, Math & Trig, Text, Information, Financial and Web.
- New folder Add-in & Automation holds CALL, REGISTER.ID and EUROCONVERT.
- The misnamed files `SEARCH-.md` and `BYCOL _.md` were replaced by `SEARCH.md` and `BYCOL.md`.

### Frontmatter

- Replaced the old keys (categories, subCategories, topics, subTopics, dateCreated, dateRevised) with domain, category, subcategory, purpose, use-case, related, level, source, date-created, date-revised, aliases and tags. The original creation dates were kept.
- Added a 1 to 5 technical level, a controlled purpose vocabulary and official source links for every page. The schema and vocabulary are documented in the README.

### Content

- Rewrote 457 placeholder pages that had invented syntax (for example `FUNCTION(input_value, [options])`) and generic text, using the official Microsoft and Google documentation.
- Reviewed the 75 pages that already had real content against the official documentation and corrected wrong results, wrong version claims and wrong platform statements. Examples: IRR, NPV and MID examples gave wrong results; DATE claimed two-digit years map to 2000 to 2029; QUERY claimed HAVING support; FILTER gave Sheets an if_empty argument; XLOOKUP was dated to Excel 2019; ROUND described negative halves rounding toward negative infinity; several pages said Sheets lacks functions it has (XLOOKUP, LEFTB, MIDB, RIGHTB).
- Removed unsourced version history tables and "Last updated" footers.
- Added a Story Problems section to every page: original business scenarios with data, a task, a solution formula and a verified answer.
- Added an image guide for every page under `Images/<Category>/<NAME>.md`, with matching placement markers in the page.
- Formatting: Title Case headings, language tags on every code fence, pipe tables, relative links instead of wikilinks, no Obsidian callouts, no dash punctuation.
- Removed GETJSON, which is not a Google Sheets function. IMPORTJSON is kept and labeled as a community Apps Script custom function.

### Added Functions

91 functions were added: 59 that Microsoft documents (including the legacy compatibility functions such as BETADIST, NORMDIST and TTEST, the double-byte text functions, and GROUPBY, PIVOTBY, PERCENTOF, TRIMRANGE, REGEXTEST, TRANSLATE, ISOMITTED, FORMULATEXT and ISREF), 29 that only Google Sheets documents (operator and parser functions such as ADD, EQ and TO_DATE, plus AI, ISDATE, ISEMAIL, ISURL, MARGINOFERROR and AVERAGE.WEIGHTED), and the Excel import functions IMPORTCSV and IMPORTTEXT plus the retired COPILOT function.

### Diagrams

- Reviewed every diagram file: corrected function descriptions and syntax in nodes, updated category names and counts, replaced wikilinks with relative links, fixed Mermaid class names, and moved frontmatter to the new schema.
- The diagram set itself was not restructured. Several diagrams overlap; consolidation is proposed separately and not yet applied.
- The old diagram project overview was rewritten as `Diagrams/Diagram-Collection-Guide.md`.

### Known Gaps

- Some behavior is undocumented on the official pages (for example the error code for certain edge cases in Google Sheets). Pages say so instead of guessing.
- Results for live-data functions (STOCKHISTORY, GOOGLEFINANCE, FIELDVALUE, CUBE functions, DETECTLANGUAGE) are described in words.
- Excel previews announced in September 2026 (FLATTEN, HAS, HASANY, HASALL) have no Microsoft support page yet and are not in the library.
