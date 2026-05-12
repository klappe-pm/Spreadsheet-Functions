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
# Spreadsheets-Functions-Logical-Complete

```mermaid

graph LR
    Logical["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Logical</b><br/>────────────────<br/>Logical and conditional functions<br/><b>Total Functions:</b> 14</div>"]
    
    Logical --> ConditionalLogic["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Conditional Logic</b><br/>────────────────<br/>Basic conditional functions<br/><b>Functions:</b> 4</div>"]
    
    Logical --> AdvancedLogic["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Advanced Logic</b><br/>────────────────<br/>Advanced logical operations<br/><b>Functions:</b> 6</div>"]
    
    Logical --> ErrorHandling["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Error Handling</b><br/>────────────────<br/>Error handling functions<br/><b>Functions:</b> 3</div>"]
    
    Logical --> DynamicArrays["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Dynamic Arrays</b><br/>────────────────<br/>Array-based logical functions<br/><b>Functions:</b> 1</div>"]
    
    %% Conditional Logic Functions (4 functions)
    ConditionalLogic --> IF["<div align='left' style='font-family: MonoLisa, monospace;'><b>IF</b><br/>────────────────<br/>Specifies a logical test to perform</div>"]
    IF --> IFSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IF(logical_test, [value_if_true], [value_if_false])</div>"]
    IF --> IFEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IF(A1&gt;10, &quot;High&quot;, &quot;Low&quot;) → &quot;High&quot;</div>"]
    
    ConditionalLogic --> IFS["<div align='left' style='font-family: MonoLisa, monospace;'><b>IFS</b><br/>────────────────<br/>Checks whether one or more conditions are met</div>"]
    IFS --> IFSSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2]...)</div>"]
    IFS --> IFSEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IFS(A1&gt;90, &quot;A&quot;, A1&gt;80, &quot;B&quot;, A1&gt;70, &quot;C&quot;) → &quot;A&quot;</div>"]
    
    ConditionalLogic --> SWITCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>SWITCH</b><br/>────────────────<br/>Evaluates an expression against a list of values</div>"]
    SWITCH --> SWITCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SWITCH(expression, value1, result1, [value2, result2]..., [default])</div>"]
    SWITCH --> SWITCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SWITCH(A1, 1, &quot;One&quot;, 2, &quot;Two&quot;, 3, &quot;Three&quot;) → &quot;Two&quot;</div>"]
    
    ConditionalLogic --> CHOOSE_LOGICAL["<div align='left' style='font-family: MonoLisa, monospace;'><b>CHOOSE</b><br/>────────────────<br/>Chooses a value from a list of values based on index</div>"]
    CHOOSE_LOGICAL --> CHOOSELOGICALSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CHOOSE(index_num, value1, [value2], ...)</div>"]
    CHOOSE_LOGICAL --> CHOOSELOGICALEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CHOOSE(2, &quot;Red&quot;, &quot;Blue&quot;, &quot;Green&quot;) → &quot;Blue&quot;</div>"]
    
    %% Advanced Logic Functions (6 functions)
    AdvancedLogic --> AND["<div align='left' style='font-family: MonoLisa, monospace;'><b>AND</b><br/>────────────────<br/>Returns TRUE if all arguments are TRUE</div>"]
    AND --> ANDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>AND(logical1, [logical2], ...)</div>"]
    AND --> ANDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=AND(A1&gt;5, B1&lt;10) → TRUE</div>"]
    
    AdvancedLogic --> OR["<div align='left' style='font-family: MonoLisa, monospace;'><b>OR</b><br/>────────────────<br/>Returns TRUE if any argument is TRUE</div>"]
    OR --> ORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OR(logical1, [logical2], ...)</div>"]
    OR --> OREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OR(A1&gt;10, B1&lt;5) → FALSE</div>"]
    
    AdvancedLogic --> NOT["<div align='left' style='font-family: MonoLisa, monospace;'><b>NOT</b><br/>────────────────<br/>Reverses the logic of its argument</div>"]
    NOT --> NOTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>NOT(logical)</div>"]
    NOT --> NOTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=NOT(A1&gt;10) → TRUE</div>"]
    
    AdvancedLogic --> XOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>XOR</b><br/>────────────────<br/>Returns TRUE if an odd number of arguments are TRUE</div>"]
    XOR --> XORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>XOR(logical1, [logical2], ...)</div>"]
    XOR --> XOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=XOR(TRUE, FALSE, TRUE) → FALSE</div>"]
    
    AdvancedLogic --> TRUE_FUNC["<div align='left' style='font-family: MonoLisa, monospace;'><b>TRUE</b><br/>────────────────<br/>Returns the logical value TRUE</div>"]
    TRUE_FUNC --> TRUEFUNCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TRUE()</div>"]
    TRUE_FUNC --> TRUEFUNCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TRUE() → TRUE</div>"]
    
    AdvancedLogic --> FALSE_FUNC["<div align='left' style='font-family: MonoLisa, monospace;'><b>FALSE</b><br/>────────────────<br/>Returns the logical value FALSE</div>"]
    FALSE_FUNC --> FALSEFUNCSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FALSE()</div>"]
    FALSE_FUNC --> FALSEFUNCEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FALSE() → FALSE</div>"]
    
    %% Error Handling Functions (3 functions)
    ErrorHandling --> IFERROR["<div align='left' style='font-family: MonoLisa, monospace;'><b>IFERROR</b><br/>────────────────<br/>Returns a value you specify if a formula evaluates to an error</div>"]
    IFERROR --> IFERRORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IFERROR(value, value_if_error)</div>"]
    IFERROR --> IFERROREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IFERROR(A1/B1, &quot;Error&quot;) → &quot;Error&quot;</div>"]
    
    ErrorHandling --> IFNA["<div align='left' style='font-family: MonoLisa, monospace;'><b>IFNA</b><br/>────────────────<br/>Returns the value you specify if the expression resolves to #N/A</div>"]
    IFNA --> IFNASYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IFNA(value, value_if_na)</div>"]
    IFNA --> IFNAEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IFNA(VLOOKUP(A1, B:C, 2, 0), &quot;Not Found&quot;) → &quot;Not Found&quot;</div>"]
    
    ErrorHandling --> ISERROR_LOGICAL["<div align='left' style='font-family: MonoLisa, monospace;'><b>ISERROR</b><br/>────────────────<br/>Checks whether a value is an error</div>"]
    ISERROR_LOGICAL --> ISERRORLOGICALSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ISERROR(value)</div>"]
    ISERROR_LOGICAL --> ISERRORLOGICALEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ISERROR(1/0) → TRUE</div>"]
    
    %% Dynamic Arrays Functions (1 function)
    DynamicArrays --> BYCOL["<div align='left' style='font-family: MonoLisa, monospace;'><b>BYCOL</b><br/>────────────────<br/>Applies a LAMBDA to each column and returns an array</div>"]
    BYCOL --> BYCOLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BYCOL(array, lambda)</div>"]
    BYCOL --> BYCOLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BYCOL(A1:C3, LAMBDA(col, SUM(col)))</div>"]
    
    %% Styling
    style Logical fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ConditionalLogic fill:#F0FFFF,stroke:#333,stroke-width:2px
    style AdvancedLogic fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ErrorHandling fill:#F0FFFF,stroke:#333,stroke-width:2px
    style DynamicArrays fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue (global numbering 1-14)
    style IF fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IFS fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SWITCH fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CHOOSE_LOGICAL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style AND fill:#F0FFF0,stroke:#333,stroke-width:2px
    style OR fill:#B9E9EB,stroke:#333,stroke-width:2px
    style NOT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style XOR fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TRUE_FUNC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FALSE_FUNC fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IFERROR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IFNA fill:#B9E9EB,stroke:#333,stroke-width:2px
    style ISERROR_LOGICAL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BYCOL fill:#B9E9EB,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style IFSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IFSSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SWITCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CHOOSELOGICALSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ANDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style NOTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style XORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TRUEFUNCSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FALSEFUNCSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IFERRORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IFNASYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style ISERRORLOGICALSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BYCOLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style IFEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IFSEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SWITCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CHOOSELOGICALEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ANDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style NOTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style XOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TRUEFUNCEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FALSEFUNCEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IFERROREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IFNAEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style ISERRORLOGICALEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BYCOLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---