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
# Spreadsheets-Functions-Lookup-Reference-Complete

```mermaid

graph LR
    LookupRef["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Lookup & Reference</b><br/>────────────────<br/>Lookup and reference functions<br/><b>Total Functions:</b> 29</div>"]
    
    LookupRef --> Lookup["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Lookup</b><br/>────────────────<br/>Data lookup functions<br/><b>Functions:</b> 8</div>"]
    
    LookupRef --> Reference["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Reference</b><br/>────────────────<br/>Cell reference functions<br/><b>Functions:</b> 21</div>"]
    
    %% Lookup Functions (8 functions)
    Lookup --> VLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>VLOOKUP</b><br/>────────────────<br/>Searches for a value in the first column of a table and returns a value in the same row from another column</div>"]
    VLOOKUP --> VLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])</div>"]
    VLOOKUP --> VLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=VLOOKUP(&quot;Apple&quot;, A1:C10, 2, FALSE) → &quot;Fruit&quot;</div>"]
    
    Lookup --> HLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>HLOOKUP</b><br/>────────────────<br/>Searches for a value in the top row of a table and returns a value in the same column from another row</div>"]
    HLOOKUP --> HLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])</div>"]
    HLOOKUP --> HLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HLOOKUP(&quot;Q1&quot;, A1:E3, 2, FALSE) → 1000</div>"]
    
    Lookup --> INDEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>INDEX</b><br/>────────────────<br/>Returns a value or reference of the cell at the intersection of a particular row and column</div>"]
    INDEX --> INDEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>INDEX(array, row_num, [column_num])</div>"]
    INDEX --> INDEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=INDEX(A1:C10, 5, 2) → B5</div>"]
    
    Lookup --> MATCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>MATCH</b><br/>────────────────<br/>Searches for a specified item in a range of cells and returns the relative position</div>"]
    MATCH --> MATCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MATCH(lookup_value, lookup_array, [match_type])</div>"]
    MATCH --> MATCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MATCH(&quot;Apple&quot;, A1:A10, 0) → 3</div>"]
    
    Lookup --> LOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>LOOKUP</b><br/>────────────────<br/>Searches for a value in a vector or array</div>"]
    LOOKUP --> LOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LOOKUP(lookup_value, lookup_vector, [result_vector])</div>"]
    LOOKUP --> LOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LOOKUP(&quot;Apple&quot;, A1:A10, B1:B10) → &quot;Fruit&quot;</div>"]
    
    Lookup --> XLOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>XLOOKUP</b><br/>────────────────<br/>Searches a range or array and returns corresponding item from second array</div>"]
    XLOOKUP --> XLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])</div>"]
    XLOOKUP --> XLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=XLOOKUP(&quot;Apple&quot;, A1:A10, B1:B10) → &quot;Fruit&quot;</div>"]
    
    Lookup --> XMATCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>XMATCH</b><br/>────────────────<br/>Returns the relative position of an item in an array</div>"]
    XMATCH --> XMATCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])</div>"]
    XMATCH --> XMATCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=XMATCH(&quot;Apple&quot;, A1:A10) → 3</div>"]
    
    Lookup --> FILTER_LOOKUP["<div align='left' style='font-family: MonoLisa, monospace;'><b>FILTER</b><br/>────────────────<br/>Filters a range of data based on criteria you define</div>"]
    FILTER_LOOKUP --> FILTERLOOKUPSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FILTER(array, include, [if_empty])</div>"]
    FILTER_LOOKUP --> FILTERLOOKUPEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FILTER(A1:B10, A1:A10=&quot;Apple&quot;) → Filtered array</div>"]
    
    %% Reference Functions (21 functions) - showing key functions
    Reference --> ADDRESS["<div align='left' style='font-family: MonoLisa, monospace;'><b>ADDRESS</b><br/>────────────────<br/>Returns a reference as text to a single cell in a worksheet</div>"]
    ADDRESS --> ADDRESSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])</div>"]
    ADDRESS --> ADDRESSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ADDRESS(2, 3) → &quot;$C$2&quot;</div>"]
    
    Reference --> AREAS["<div align='left' style='font-family: MonoLisa, monospace;'><b>AREAS</b><br/>────────────────<br/>Returns the number of areas in a reference</div>"]
    AREAS --> AREASSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>AREAS(reference)</div>"]
    AREAS --> AREASEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=AREAS((A1:B4,C1:D4)) → 2</div>"]
    
    Reference --> CHOOSE["<div align='left' style='font-family: MonoLisa, monospace;'><b>CHOOSE</b><br/>────────────────<br/>Chooses a value from a list of values</div>"]
    CHOOSE --> CHOOSESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CHOOSE(index_num, value1, [value2], ...)</div>"]
    CHOOSE --> CHOOSEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CHOOSE(2, &quot;Red&quot;, &quot;Blue&quot;, &quot;Green&quot;) → &quot;Blue&quot;</div>"]
    
    Reference --> INDIRECT["<div align='left' style='font-family: MonoLisa, monospace;'><b>INDIRECT</b><br/>────────────────<br/>Returns a reference indicated by a text string</div>"]
    INDIRECT --> INDIRECTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>INDIRECT(ref_text, [a1])</div>"]
    INDIRECT --> INDIRECTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=INDIRECT(&quot;A1&quot;) → Value in A1</div>"]
    
    Reference --> OFFSET["<div align='left' style='font-family: MonoLisa, monospace;'><b>OFFSET</b><br/>────────────────<br/>Returns a reference to a range that is a specified number of rows and columns from a cell or range</div>"]
    OFFSET --> OFFSETSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OFFSET(reference, rows, cols, [height], [width])</div>"]
    OFFSET --> OFFSETEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OFFSET(A1, 2, 3) → D3</div>"]
    
    Reference --> HYPERLINK["<div align='left' style='font-family: MonoLisa, monospace;'><b>HYPERLINK</b><br/>────────────────<br/>Creates a shortcut or jump that opens a document stored on a network server</div>"]
    HYPERLINK --> HYPERLINKSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HYPERLINK(link_location, [friendly_name])</div>"]
    HYPERLINK --> HYPERLINKEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HYPERLINK(&quot;http://www.example.com&quot;, &quot;Visit Site&quot;)</div>"]
    
    Reference --> TRANSPOSE_REF["<div align='left' style='font-family: MonoLisa, monospace;'><b>TRANSPOSE</b><br/>────────────────<br/>Returns the transpose of an array</div>"]
    TRANSPOSE_REF --> TRANSPOSEREFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TRANSPOSE(array)</div>"]
    TRANSPOSE_REF --> TRANSPOSEREFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TRANSPOSE(A1:C3)</div>"]
    
    Reference --> GETPIVOTDATA["<div align='left' style='font-family: MonoLisa, monospace;'><b>GETPIVOTDATA</b><br/>────────────────<br/>Returns data stored in a PivotTable report</div>"]
    GETPIVOTDATA --> GETPIVOTDATASYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>GETPIVOTDATA(data_field, pivot_table, [field1, item1], ...)</div>"]
    GETPIVOTDATA --> GETPIVOTDATAEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=GETPIVOTDATA(&quot;Sum of Sales&quot;, A3)</div>"]
    
    Reference --> RTD["<div align='left' style='font-family: MonoLisa, monospace;'><b>RTD</b><br/>────────────────<br/>Retrieves real-time data from a program that supports COM automation</div>"]
    RTD --> RTDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RTD(progid, server, topic1, [topic2], ...)</div>"]
    RTD --> RTDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RTD(&quot;mycomserver&quot;, &quot;&quot;, &quot;NYSE&quot;, &quot;MSFT&quot;)</div>"]
    
    %% Styling
    style LookupRef fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Lookup fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Reference fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue (global numbering 1-29)
    style VLOOKUP fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HLOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style INDEX fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MATCH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style LOOKUP fill:#F0FFF0,stroke:#333,stroke-width:2px
    style XLOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style XMATCH fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FILTER_LOOKUP fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ADDRESS fill:#F0FFF0,stroke:#333,stroke-width:2px
    style AREAS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CHOOSE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style INDIRECT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style OFFSET fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HYPERLINK fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TRANSPOSE_REF fill:#F0FFF0,stroke:#333,stroke-width:2px
    style GETPIVOTDATA fill:#B9E9EB,stroke:#333,stroke-width:2px
    style RTD fill:#F0FFF0,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style VLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style INDEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MATCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style XLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style XMATCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FILTERLOOKUPSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ADDRESSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style AREASSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CHOOSESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style INDIRECTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OFFSETSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HYPERLINKSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TRANSPOSEREFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style GETPIVOTDATASYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RTDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style VLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style INDEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MATCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style XLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style XMATCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FILTERLOOKUPEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ADDRESSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style AREASEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CHOOSEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style INDIRECTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OFFSETEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HYPERLINKEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TRANSPOSEREFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style GETPIVOTDATAEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RTDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---