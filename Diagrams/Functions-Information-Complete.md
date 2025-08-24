---
!!python/object/apply:collections.OrderedDict
- - - categories
    - []
  - - subCategories
    - []
  - - topics
    - []
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-16
  - - dateRevised
    - 2025-06-16
  - - aliases
    - - Spreadsheets-Functions-Information-Complete
  - - tags
    - []
---
# Spreadsheets-Functions-Information-Complete

```mermaid

graph LR
    Information["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Information</b><br/>────────────────<br/>Information and data type functions<br/><b>Total Functions:</b> 41</div>"]
    
    Information --> TypeChecking["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Type Checking</b><br/>────────────────<br/>Data type validation functions<br/><b>Functions:</b> 14</div>"]
    
    Information --> ReferenceInfo["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Reference Info</b><br/>────────────────<br/>Cell and reference information<br/><b>Functions:</b> 14</div>"]
    
    Information --> ErrorChecking["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Error Checking</b><br/>────────────────<br/>Error detection functions<br/><b>Functions:</b> 8</div>"]
    
    Information --> ErrorInfo["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Error Info</b><br/>────────────────<br/>Error information functions<br/><b>Functions:</b> 2</div>"]
    
    Information --> LegacyFunctions["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Legacy Functions</b><br/>────────────────<br/>Legacy information functions<br/><b>Functions:</b> 2</div>"]
    
    Information --> DataTypes["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Data Types</b><br/>────────────────<br/>Data type identification<br/><b>Functions:</b> 1</div>"]
    
    %% Type Checking Functions (14 functions)
    TypeChecking --> ISBLANK["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISBLANK</b><br/>────────────────<br/>Checks whether a value is blank</div>"]
    ISBLANK --> ISBLANKSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISBLANK(value)</div>"]
    ISBLANK --> ISBLANKEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISBLANK(A1) → TRUE</div>"]
    
    TypeChecking --> ISERROR["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISERROR</b><br/>────────────────<br/>Checks whether a value is an error</div>"]
    ISERROR --> ISERRORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISERROR(value)</div>"]
    ISERROR --> ISERROREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISERROR(1/0) → TRUE</div>"]
    
    TypeChecking --> ISEVEN["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISEVEN</b><br/>────────────────<br/>Checks whether a number is even</div>"]
    ISEVEN --> ISEVENSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISEVEN(number)</div>"]
    ISEVEN --> ISEVENEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISEVEN(4) → TRUE</div>"]
    
    TypeChecking --> ISLOGICAL["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISLOGICAL</b><br/>────────────────<br/>Checks whether a value is a logical value</div>"]
    ISLOGICAL --> ISLOGICALSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISLOGICAL(value)</div>"]
    ISLOGICAL --> ISLOGICALEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISLOGICAL(TRUE) → TRUE</div>"]
    
    TypeChecking --> ISNUMBER["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISNUMBER</b><br/>────────────────<br/>Checks whether a value is a number</div>"]
    ISNUMBER --> ISNUMBERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISNUMBER(value)</div>"]
    ISNUMBER --> ISNUMBEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISNUMBER(123) → TRUE</div>"]
    
    TypeChecking --> ISTEXT["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISTEXT</b><br/>────────────────<br/>Checks whether a value is text</div>"]
    ISTEXT --> ISTEXTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISTEXT(value)</div>"]
    ISTEXT --> ISTEXTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISTEXT(&quot;Hello&quot;) → TRUE</div>"]
    
    %% Reference Info Functions (14 functions)
    ReferenceInfo --> CELL["<div align='left' style='font-family: MonoLisa, monospace;'><b>CELL</b><br/>────────────────<br/>Returns information about a cell</div>"]
    CELL --> CELLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CELL(info_type, [reference])</div>"]
    CELL --> CELLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CELL(&quot;address&quot;, A1) → &quot;$A$1&quot;</div>"]
    
    ReferenceInfo --> COLUMN["<div align='left' style='font-family: MonoLisa, monospace;'><b>COLUMN</b><br/>────────────────<br/>Returns the column number of a reference</div>"]
    COLUMN --> COLUMNSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>COLUMN([reference])</div>"]
    COLUMN --> COLUMNEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=COLUMN(C5) → 3</div>"]
    
    ReferenceInfo --> ROW["<div align='left' style='font-family: MonoLisa, monospace;'><b>ROW</b><br/>────────────────<br/>Returns the row number of a reference</div>"]
    ROW --> ROWSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ROW([reference])</div>"]
    ROW --> ROWEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ROW(A5) → 5</div>"]
    
    %% Error Checking Functions (8 functions)
    ErrorChecking --> ISERR["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISERR</b><br/>────────────────<br/>Checks whether a value is an error other than #N/A</div>"]
    ISERR --> ISERRSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISERR(value)</div>"]
    ISERR --> ISERREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISERR(1/0) → TRUE</div>"]
    
    ErrorChecking --> ISNA["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISNA</b><br/>────────────────<br/>Checks whether a value is the #N/A error</div>"]
    ISNA --> ISNASYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISNA(value)</div>"]
    ISNA --> ISNAEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISNA(NA()) → TRUE</div>"]
    
    %% Error Info Functions (2 functions)
    ErrorInfo --> ERROR_TYPE["<div align='left' style='font-family: MonoLisa, monospace;'><b>ERROR.TYPE</b><br/>────────────────<br/>Returns a number corresponding to an error type</div>"]
    ERROR_TYPE --> ERRORTYPESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ERROR.TYPE(error_val)</div>"]
    ERROR_TYPE --> ERRORTYPEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ERROR.TYPE(1/0) → 2</div>"]
    
    ErrorInfo --> NA_FUNC["<div align='left' style='font-family: MonoLisa, monospace;'><b>NA</b><br/>────────────────<br/>Returns the error value #N/A</div>"]
    NA_FUNC --> NAFUNCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NA()</div>"]
    NA_FUNC --> NAFUNCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NA() → #N/A</div>"]
    
    %% Legacy Functions (2 functions)
    LegacyFunctions --> INFO["<div align='left' style='font-family: MonoLisa, monospace;'><b>INFO</b><br/>────────────────<br/>Returns information about the current operating environment</div>"]
    INFO --> INFOSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>INFO(type_text)</div>"]
    INFO --> INFOEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=INFO(&quot;release&quot;) → &quot;16.0&quot;</div>"]
    
    LegacyFunctions --> TYPE["<div align='left' style='font-family: MonoLisa, monospace;'><b>TYPE</b><br/>────────────────<br/>Returns a number indicating the data type of a value</div>"]
    TYPE --> TYPESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TYPE(value)</div>"]
    TYPE --> TYPEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TYPE(&quot;Hello&quot;) → 2</div>"]
    
    %% Data Types (1 function)
    DataTypes --> TYPEOF["<div align='left' style='font-family: MonoLisa, monospace;'><b>TYPEOF</b><br/>────────────────<br/>Returns a text string indicating the data type of a value</div>"]
    TYPEOF --> TYPEOFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TYPEOF(value)</div>"]
    TYPEOF --> TYPEOFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TYPEOF(123) → &quot;Number&quot;</div>"]
    
    %% Styling
    style Information fill:#F0FFFF,stroke:#333,stroke-width:2px
    style TypeChecking fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ReferenceInfo fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ErrorChecking fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ErrorInfo fill:#F0FFFF,stroke:#333,stroke-width:2px
    style LegacyFunctions fill:#F0FFFF,stroke:#333,stroke-width:2px
    style DataTypes fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue
    style ISBLANK fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ISERROR fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ISEVEN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ISLOGICAL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ISNUMBER fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ISTEXT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CELL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style COLUMN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ROW fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ISERR fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ISNA fill:#F0FFF0,stroke:#333,stroke-width:2px
    style ERROR_TYPE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style NA_FUNC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style INFO fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TYPE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TYPEOF fill:#B9E9EB,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style ISBLANKSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISERRORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISEVENSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISLOGICALSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISNUMBERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISTEXTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CELLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style COLUMNSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ROWSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISERRSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISNASYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ERRORTYPESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NAFUNCSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style INFOSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TYPESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TYPEOFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style ISBLANKEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISERROREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISEVENEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISLOGICALEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISNUMBEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISTEXTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CELLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style COLUMNEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ROWEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISERREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISNAEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ERRORTYPEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NAFUNCEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style INFOEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TYPEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TYPEOFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---