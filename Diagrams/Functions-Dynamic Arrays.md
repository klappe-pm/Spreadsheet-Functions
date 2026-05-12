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
# Spreadsheets-Functions-Dynamic Arrays

```mermaid


graph LR
    A["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Dynamic Arrays</b><br/>────────────────<br/>Modern Excel array manipulation functions<br/><b>Total Functions:</b> 5</div>"] --> B["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Array Functions</b><br/>────────────────<br/>Functions for dynamic array operations<br/><b>Total Functions:</b> 5</div>"]
    
    B --> UNIQUE["<div align='left' style='font-family: MonoLisa, monospace;'><b>UNIQUE</b><br/>────────────────<br/>Returns unique values from a range or array</div>"]
    
    UNIQUE --> UNIQUESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>UNIQUE(array, [by_col], [exactly_once])</div>"]
    
    UNIQUE --> UNIQUEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=UNIQUE(A1:A10)</div>"]
    
    B --> FILTER["<div align='left' style='font-family: MonoLisa, monospace;'><b>FILTER</b><br/>────────────────<br/>Filters a range of data based on criteria</div>"]
    
    FILTER --> FILTERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FILTER(array, include, [if_empty])</div>"]
    
    FILTER --> FILTEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FILTER(A1:B10, B1:B10&gt;100)</div>"]
    
    B --> SORTBY["<div align='left' style='font-family: MonoLisa, monospace;'><b>SORTBY</b><br/>────────────────<br/>Sorts an array based on another array</div>"]
    
    SORTBY --> SORTBYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SORTBY(array, by_array, [sort_order], [by_array2, sort_order2, …])</div>"]
    
    SORTBY --> SORTBYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SORTBY(A1:A10, B1:B10, -1)</div>"]
    
    B --> SEQUENCE["<div align='left' style='font-family: MonoLisa, monospace;'><b>SEQUENCE</b><br/>────────────────<br/>Generates a sequence of numbers in an array</div>"]
    
    SEQUENCE --> SEQUENCESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SEQUENCE(rows, [columns], [start], [step])</div>"]
    
    SEQUENCE --> SEQUENCEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SEQUENCE(5, 1, 1, 2)</div>"]
    
    B --> RANDARRAY["<div align='left' style='font-family: MonoLisa, monospace;'><b>RANDARRAY</b><br/>────────────────<br/>Generates an array of random numbers</div>"]
    
    RANDARRAY --> RANDARRAYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RANDARRAY([rows], [columns], [min], [max], [integer])</div>"]
    
    RANDARRAY --> RANDARRAYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RANDARRAY(3, 2, 1, 10, TRUE)</div>"]
    
    style A fill:#F0FFFF,stroke:#333,stroke-width:2px
    style B fill:#F0FFFF,stroke:#333,stroke-width:2px
    style UNIQUE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style UNIQUESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style UNIQUEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FILTER fill:#B9E9EB,stroke:#333,stroke-width:2px
    style FILTERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FILTEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SORTBY fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SORTBYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SORTBYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SEQUENCE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SEQUENCESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SEQUENCEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RANDARRAY fill:#F0FFF0,stroke:#333,stroke-width:2px
    style RANDARRAYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RANDARRAYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```
