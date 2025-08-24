---
categories:
- spreadsheet-functions
subCategories:
- excel
- sheets
topics:
- diagrams
subTopics: []
dateCreated: '2025-08-17'
dateRevised: '2025-08-17'
aliases: []
tags:
- diagrams
- excel
- sheets
---
# Spreadsheets-Functions-Lookup and References

```mermaid

graph LR
    LookupRef["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Lookup & Reference</b><br/>────────────────<br/>Functions for looking up and referencing data<br/><b>Total Functions:</b> 29</div>"]
    
    LookupRef --> Lookup["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Lookup</b><br/>────────────────<br/>Functions for searching and retrieving data<br/><b>Functions:</b> 8</div>"]
    
    %% Lookup functions (8 total)
    %% FILTER - Function 1
    Lookup --> FILTER["<div align='left' style='font-family: MonoLisa, monospace;'><b>FILTER</b><br/>────────────────<br/>Filters a range based on criteria</div>"]
    FILTER --> FILTERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FILTER(range, condition1, [condition2, …])</div>"]
    FILTER --> FILTEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FILTER(A1:B10, A1:A10&gt;100) → Filtered rows</div>"]
    
    %% HLOOKUP - Function 2
    Lookup --> HLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>HLOOKUP</b><br/>────────────────<br/>Searches horizontally for a value in the first row and returns a value from a specified row</div>"]
    HLOOKUP --> HLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HLOOKUP(search_key, range, index, [sorted])</div>"]
    HLOOKUP --> HLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HLOOKUP(&quot;Q2&quot;, A1:D3, 2, FALSE) → 500</div>"]
    
    %% INDEX - Function 3
    Lookup --> INDEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>INDEX</b><br/>────────────────<br/>Returns a value at a specified position in a range or array</div>"]
    INDEX --> INDEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>INDEX(reference, [row], [column], [area_number])</div>"]
    INDEX --> INDEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=INDEX(A1:C3, 2, 2) → &quot;Value&quot;</div>"]
    
    %% LOOKUP - Function 4
    Lookup --> LOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>LOOKUP</b><br/>────────────────<br/>Searches for a value in a range and returns a corresponding value</div>"]
    LOOKUP --> LOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LOOKUP(search_key, search_range, [result_range])</div>"]
    LOOKUP --> LOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LOOKUP(10, A1:A5, B1:B5) → &quot;Result&quot;</div>"]
    
    %% MATCH - Function 5
    Lookup --> MATCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>MATCH</b><br/>────────────────<br/>Returns the relative position of a value in a range</div>"]
    MATCH --> MATCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MATCH(search_key, range, [search_type])</div>"]
    MATCH --> MATCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MATCH(&quot;Apple&quot;, A1:A5, 0) → 2</div>"]
    
    %% VLOOKUP - Function 6
    Lookup --> VLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>VLOOKUP</b><br/>────────────────<br/>Searches vertically for a value in the first column and returns a value from a specified column</div>"]
    VLOOKUP --> VLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>VLOOKUP(search_key, range, index, [sorted])</div>"]
    VLOOKUP --> VLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=VLOOKUP(&quot;Apple&quot;, A1:C5, 2, FALSE) → &quot;Fruit&quot;</div>"]
    
    %% XLOOKUP - Function 7
    Lookup --> XLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>XLOOKUP</b><br/>────────────────<br/>Advanced lookup with flexible search options and error handling</div>"]
    XLOOKUP --> XLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>XLOOKUP(search_key, lookup_range, return_range, [if_not_found], [match_mode], [search_mode])</div>"]
    XLOOKUP --> XLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=XLOOKUP(&quot;Apple&quot;, A1:A5, B1:B5, &quot;Not Found&quot;) → &quot;Fruit&quot;</div>"]
    
    %% XMATCH - Function 8
    Lookup --> XMATCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>XMATCH</b><br/>────────────────<br/>Advanced match with flexible search modes</div>"]
    XMATCH --> XMATCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>XMATCH(search_key, lookup_range, [match_mode], [search_mode])</div>"]
    XMATCH --> XMATCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=XMATCH(&quot;Apple&quot;, A1:A5, 0) → 2</div>"]
    
    %% Styling
    style LookupRef fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Lookup fill:#F0FFFF,stroke:#333,stroke-width:2px
    %% Functions alternate colors
    style FILTER fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HLOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style INDEX fill:#F0FFF0,stroke:#333,stroke-width:2px
    style LOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style MATCH fill:#F0FFF0,stroke:#333,stroke-width:2px
    style VLOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style XLOOKUP fill:#F0FFF0,stroke:#333,stroke-width:2px
    style XMATCH fill:#B9E9EB,stroke:#333,stroke-width:2px
    %% All syntax nodes - pink
    style FILTERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style INDEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MATCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style VLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style XLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style XMATCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    %% All example nodes - lavender
    style FILTEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style INDEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MATCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style VLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style XLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style XMATCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
```
