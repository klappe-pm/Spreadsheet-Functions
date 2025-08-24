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
    - - Spreadsheets-Functions-Google-Specific-Complete
  - - tags
    - []
---
# Spreadsheets-Functions-Google-Specific-Complete

```mermaid

graph LR
    GoogleSpecific["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Google-Specific</b><br/>────────────────<br/>Google Sheets exclusive functions<br/><b>Total Functions:</b> 29</div>"]
    
    GoogleSpecific --> ArrayOperationsGoogle["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Array Operations</b><br/>────────────────<br/>Google array manipulation<br/><b>Functions:</b> 10</div>"]
    
    GoogleSpecific --> WebDataGoogle["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Web Data</b><br/>────────────────<br/>Web data import functions<br/><b>Functions:</b> 7</div>"]
    
    GoogleSpecific --> TextProcessingGoogle["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Text Processing</b><br/>────────────────<br/>Google text functions<br/><b>Functions:</b> 3</div>"]
    
    GoogleSpecific --> SingleFunctions["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Individual Functions</b><br/>────────────────<br/>Various specialized functions<br/><b>Functions:</b> 9</div>"]
    
    %% Array Operations Google Functions (10 functions)
    ArrayOperationsGoogle --> ARRAYFORMULA["<div align='left' style='font-family: MonoLisa, monospace;'><b>ARRAYFORMULA</b><br/>────────────────<br/>Enables array formulas in non-array functions</div>"]
    ARRAYFORMULA --> ARRAYFORMULASYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>ARRAYFORMULA(array_formula)</div>"]
    ARRAYFORMULA --> ARRAYFORMULAEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=ARRAYFORMULA(A1:A10*B1:B10) → Array result</div>"]
    
    ArrayOperationsGoogle --> FLATTEN["<div align='left' style='font-family: MonoLisa, monospace;'><b>FLATTEN</b><br/>────────────────<br/>Flattens all the values from one or more ranges into a single column</div>"]
    FLATTEN --> FLATTENSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FLATTEN(range1, [range2, ...])</div>"]
    FLATTEN --> FLATTENEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FLATTEN(A1:B5, D1:E5) → Single column</div>"]
    
    ArrayOperationsGoogle --> SPLIT["<div align='left' style='font-family: MonoLisa, monospace;'><b>SPLIT</b><br/>────────────────<br/>Divides text around a specified character or string</div>"]
    SPLIT --> SPLITSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SPLIT(text, delimiter, [split_by_each], [remove_empty_text])</div>"]
    SPLIT --> SPLITEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SPLIT(&quot;apple,banana,cherry&quot;, &quot;,&quot;) → Array of text</div>"]
    
    %% Web Data Google Functions (7 functions)
    WebDataGoogle --> IMPORTDATA["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMPORTDATA</b><br/>────────────────<br/>Imports data from a given URL in CSV format</div>"]
    IMPORTDATA --> IMPORTDATASYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPORTDATA(url)</div>"]
    IMPORTDATA --> IMPORTDATAEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPORTDATA(&quot;http://example.com/data.csv&quot;) → CSV data</div>"]
    
    WebDataGoogle --> IMPORTHTML["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMPORTHTML</b><br/>────────────────<br/>Imports data from a table or list within an HTML page</div>"]
    IMPORTHTML --> IMPORTHTMLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPORTHTML(url, query, index)</div>"]
    IMPORTHTML --> IMPORTHTMLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPORTHTML(&quot;http://example.com&quot;, &quot;table&quot;, 1) → HTML table</div>"]
    
    WebDataGoogle --> IMPORTXML["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>Imports data from structured data types including XML</div>"]
    IMPORTXML --> IMPORTXMLSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPORTXML(url, xpath_query)</div>"]
    IMPORTXML --> IMPORTXMLEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPORTXML(&quot;http://example.com&quot;, &quot;//title&quot;) → XML data</div>"]
    
    WebDataGoogle --> IMPORTRANGE["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMPORTRANGE</b><br/>────────────────<br/>Imports a range of cells from a specified spreadsheet</div>"]
    IMPORTRANGE --> IMPORTRANGESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMPORTRANGE(spreadsheet_url, range_string)</div>"]
    IMPORTRANGE --> IMPORTRANGEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMPORTRANGE(&quot;spreadsheet_key&quot;, &quot;Sheet1!A1:C10&quot;) → Range data</div>"]
    
    %% Text Processing Google Functions (3 functions)
    TextProcessingGoogle --> REGEXMATCH_GOOGLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXMATCH</b><br/>────────────────<br/>Tests whether a piece of text matches a regular expression</div>"]
    REGEXMATCH_GOOGLE --> REGEXMATCHGOOGLESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXMATCH(text, regular_expression)</div>"]
    REGEXMATCH_GOOGLE --> REGEXMATCHGOOGLEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXMATCH(&quot;hello@gmail.com&quot;, &quot;.+@.+&quot;) → TRUE</div>"]
    
    TextProcessingGoogle --> REGEXEXTRACT_GOOGLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXEXTRACT</b><br/>────────────────<br/>Extracts matching substrings according to a regular expression</div>"]
    REGEXEXTRACT_GOOGLE --> REGEXEXTRACTGOOGLESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXEXTRACT(text, regular_expression)</div>"]
    REGEXEXTRACT_GOOGLE --> REGEXEXTRACTGOOGLEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXEXTRACT(&quot;hello@gmail.com&quot;, &quot;@(.+)&quot;) → &quot;gmail.com&quot;</div>"]
    
    TextProcessingGoogle --> REGEXREPLACE_GOOGLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXREPLACE</b><br/>────────────────<br/>Replaces part of a text string with different text using regex</div>"]
    REGEXREPLACE_GOOGLE --> REGEXREPLACEGOOGLESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXREPLACE(text, regular_expression, replacement)</div>"]
    REGEXREPLACE_GOOGLE --> REGEXREPLACEGOOGLEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXREPLACE(&quot;hello@gmail.com&quot;, &quot;@.+&quot;, &quot;@yahoo.com&quot;) → &quot;hello@yahoo.com&quot;</div>"]
    
    %% Individual Functions (9 functions)
    SingleFunctions --> GOOGLETRANSLATE["<div align='left' style='font-family: MonoLisa, monospace;'><b>GOOGLETRANSLATE</b><br/>────────────────<br/>Translates text from one language into another</div>"]
    GOOGLETRANSLATE --> GOOGLETRANSLATESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>GOOGLETRANSLATE(text, [source_language], [target_language])</div>"]
    GOOGLETRANSLATE --> GOOGLETRANSLATEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=GOOGLETRANSLATE(&quot;Hello&quot;, &quot;en&quot;, &quot;es&quot;) → &quot;Hola&quot;</div>"]
    
    SingleFunctions --> DETECTLANGUAGE["<div align='left' style='font-family: MonoLisa, monospace;'><b>DETECTLANGUAGE</b><br/>────────────────<br/>Identifies the language used in text</div>"]
    DETECTLANGUAGE --> DETECTLANGUAGESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DETECTLANGUAGE(text_or_range)</div>"]
    DETECTLANGUAGE --> DETECTLANGUAGEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DETECTLANGUAGE(&quot;Bonjour&quot;) → &quot;fr&quot;</div>"]
    
    SingleFunctions --> IMAGE["<div align='left' style='font-family: MonoLisa, monospace;'><b>IMAGE</b><br/>────────────────<br/>Inserts an image into a cell</div>"]
    IMAGE --> IMAGESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>IMAGE(url, [mode], [height], [width])</div>"]
    IMAGE --> IMAGEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=IMAGE(&quot;http://example.com/image.jpg&quot;) → Image</div>"]
    
    %% Styling
    style GoogleSpecific fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ArrayOperationsGoogle fill:#F0FFFF,stroke:#333,stroke-width:2px
    style WebDataGoogle fill:#F0FFFF,stroke:#333,stroke-width:2px
    style TextProcessingGoogle fill:#F0FFFF,stroke:#333,stroke-width:2px
    style SingleFunctions fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue
    style ARRAYFORMULA fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FLATTEN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SPLIT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IMPORTDATA fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMPORTHTML fill:#F0FFF0,stroke:#333,stroke-width:2px
    style IMPORTXML fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMPORTRANGE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style REGEXMATCH_GOOGLE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style REGEXEXTRACT_GOOGLE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style REGEXREPLACE_GOOGLE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style GOOGLETRANSLATE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DETECTLANGUAGE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style IMAGE fill:#F0FFF0,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style ARRAYFORMULASYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FLATTENSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SPLITSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMPORTDATASYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMPORTHTMLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMPORTXMLSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMPORTRANGESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXMATCHGOOGLESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXEXTRACTGOOGLESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXREPLACEGOOGLESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style GOOGLETRANSLATESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DETECTLANGUAGESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style IMAGESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style ARRAYFORMULAEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FLATTENEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SPLITEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMPORTDATAEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMPORTHTMLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMPORTXMLEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMPORTRANGEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXMATCHGOOGLEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXEXTRACTGOOGLEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXREPLACEGOOGLEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style GOOGLETRANSLATEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DETECTLANGUAGEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style IMAGEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---