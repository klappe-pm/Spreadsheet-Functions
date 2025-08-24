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
    - - Spreadsheets-Functions-Excel-Specific-Complete
  - - tags
    - []
---
# Spreadsheets-Functions-Excel-Specific-Complete

```mermaid

graph LR
    ExcelSpecific["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Excel-Specific</b><br/>────────────────<br/>Excel-only functions and features<br/><b>Total Functions:</b> 40</div>"]
    
    ExcelSpecific --> ArrayOperations["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Array Operations</b><br/>────────────────<br/>Advanced array manipulation<br/><b>Functions:</b> 16</div>"]
    
    ExcelSpecific --> DynamicArraysExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Dynamic Arrays</b><br/>────────────────<br/>Dynamic array functions<br/><b>Functions:</b> 4</div>"]
    
    ExcelSpecific --> FinancialExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Financial</b><br/>────────────────<br/>Excel financial functions<br/><b>Functions:</b> 6</div>"]
    
    ExcelSpecific --> PowerQuery["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Power Query</b><br/>────────────────<br/>Power Query integration<br/><b>Functions:</b> 3</div>"]
    
    ExcelSpecific --> TextProcessingExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Text Processing</b><br/>────────────────<br/>Excel text functions<br/><b>Functions:</b> 4</div>"]
    
    ExcelSpecific --> WebDataExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Web Data</b><br/>────────────────<br/>Web data retrieval<br/><b>Functions:</b> 2</div>"]
    
    ExcelSpecific --> InformationExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Information</b><br/>────────────────<br/>Excel information functions<br/><b>Functions:</b> 2</div>"]
    
    ExcelSpecific --> NewFunctionsExcel["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>New Functions</b><br/>────────────────<br/>Latest Excel functions<br/><b>Functions:</b> 3</div>"]
    
    %% Array Operations Functions (16 functions) - showing key functions
    ArrayOperations --> SORT["<div align='left' style='font-family: MonoLisa, monospace;'><b>SORT</b><br/>────────────────<br/>Sorts the contents of a range or array</div>"]
    SORT --> SORTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SORT(array, [sort_index], [sort_order], [by_col])</div>"]
    SORT --> SORTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SORT(A1:B10, 1, 1) → Sorted array</div>"]
    
    ArrayOperations --> SORTBY["<div align='left' style='font-family: MonoLisa, monospace;'><b>SORTBY</b><br/>────────────────<br/>Sorts the contents of a range or array based on values in a corresponding range</div>"]
    SORTBY --> SORTBYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SORTBY(array, by_array1, [sort_order1], [by_array2, sort_order2]...)</div>"]
    SORTBY --> SORTBYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SORTBY(A1:A10, B1:B10, -1) → Sorted array</div>"]
    
    ArrayOperations --> UNIQUE_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>UNIQUE</b><br/>────────────────<br/>Returns a list of unique values in a list or range</div>"]
    UNIQUE_EXCEL --> UNIQUEEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>UNIQUE(array, [by_col], [exactly_once])</div>"]
    UNIQUE_EXCEL --> UNIQUEEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=UNIQUE(A1:A10) → Unique values</div>"]
    
    ArrayOperations --> FILTER_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>FILTER</b><br/>────────────────<br/>Filters a range of data based on criteria you define</div>"]
    FILTER_EXCEL --> FILTEREXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FILTER(array, include, [if_empty])</div>"]
    FILTER_EXCEL --> FILTEREXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FILTER(A1:B10, A1:A10&gt;5) → Filtered array</div>"]
    
    %% Dynamic Arrays Excel Functions (4 functions)
    DynamicArraysExcel --> SEQUENCE_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>SEQUENCE</b><br/>────────────────<br/>Generates a list of sequential numbers in an array</div>"]
    SEQUENCE_EXCEL --> SEQUENCEEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SEQUENCE(rows, [columns], [start], [step])</div>"]
    SEQUENCE_EXCEL --> SEQUENCEEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SEQUENCE(5, 1, 1, 2) → {1;3;5;7;9}</div>"]
    
    DynamicArraysExcel --> RANDARRAY_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>RANDARRAY</b><br/>────────────────<br/>Returns an array of random numbers</div>"]
    RANDARRAY_EXCEL --> RANDARRAYEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RANDARRAY([rows], [columns], [min], [max], [integer])</div>"]
    RANDARRAY_EXCEL --> RANDARRAYEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RANDARRAY(3, 2, 1, 10, TRUE) → Random array</div>"]
    
    %% Financial Excel Functions (6 functions)
    FinancialExcel --> STOCKHISTORY_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>STOCKHISTORY</b><br/>────────────────<br/>Retrieves historical stock data from the internet</div>"]
    STOCKHISTORY_EXCEL --> STOCKHISTORYEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>STOCKHISTORY(stock, start_date, [end_date], [interval], [headers], [properties])</div>"]
    STOCKHISTORY_EXCEL --> STOCKHISTORYEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=STOCKHISTORY(&quot;MSFT&quot;, TODAY()-365) → Stock data</div>"]
    
    %% Power Query Functions (3 functions)
    PowerQuery --> POWERQUERY["<div align='left' style='font-family: MonoLisa, monospace;'><b>POWERQUERY</b><br/>────────────────<br/>Executes a Power Query and returns the results</div>"]
    POWERQUERY --> POWERQUERYSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>POWERQUERY(query_name, [parameters])</div>"]
    POWERQUERY --> POWERQUERYEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=POWERQUERY(&quot;DataQuery&quot;) → Query results</div>"]
    
    %% Text Processing Excel Functions (4 functions)
    TextProcessingExcel --> TEXTJOIN_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>TEXTJOIN</b><br/>────────────────<br/>Combines the text from multiple ranges using a delimiter</div>"]
    TEXTJOIN_EXCEL --> TEXTJOINEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)</div>"]
    TEXTJOIN_EXCEL --> TEXTJOINEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TEXTJOIN(&quot;, &quot;, TRUE, A1:A5) → &quot;Apple, Banana, Cherry&quot;</div>"]
    
    TextProcessingExcel --> CONCAT_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>CONCAT</b><br/>────────────────<br/>Combines the text from multiple ranges</div>"]
    CONCAT_EXCEL --> CONCATEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CONCAT(text1, [text2], ...)</div>"]
    CONCAT_EXCEL --> CONCATEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CONCAT(A1:A3) → &quot;HelloWorld&quot;</div>"]
    
    %% Web Data Excel Functions (2 functions)
    WebDataExcel --> WEBSERVICE_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>WEBSERVICE</b><br/>────────────────<br/>Returns data from a web service on the Internet</div>"]
    WEBSERVICE_EXCEL --> WEBSERVICEEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>WEBSERVICE(url)</div>"]
    WEBSERVICE_EXCEL --> WEBSERVICEEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=WEBSERVICE(&quot;http://api.example.com/data&quot;) → Web data</div>"]
    
    WebDataExcel --> FILTERXML_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>FILTERXML</b><br/>────────────────<br/>Returns specific data from XML content using an XPath</div>"]
    FILTERXML_EXCEL --> FILTERXMLEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FILTERXML(xml, xpath)</div>"]
    FILTERXML_EXCEL --> FILTERXMLEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FILTERXML(A1, &quot;//price&quot;) → XML data</div>"]
    
    %% New Functions Excel (3 functions)
    NewFunctionsExcel --> LAMBDA_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>LAMBDA</b><br/>────────────────<br/>Creates custom, reusable functions without using VBA</div>"]
    LAMBDA_EXCEL --> LAMBDAEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LAMBDA([parameter1, parameter2, ...], calculation)</div>"]
    LAMBDA_EXCEL --> LAMBDAEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LAMBDA(x, y, x*y)(2, 3) → 6</div>"]
    
    NewFunctionsExcel --> LET_EXCEL["<div align='left' style='font-family: MonoLisa, monospace;'><b>LET</b><br/>────────────────<br/>Assigns names to calculation results to improve performance</div>"]
    LET_EXCEL --> LETEXCELSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LET(name1, value1, [name2, value2, ...], calculation)</div>"]
    LET_EXCEL --> LETEXCELEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LET(x, 5, y, 10, x+y) → 15</div>"]
    
    %% Styling
    style ExcelSpecific fill:#F0FFFF,stroke:#333,stroke-width:2px
    style ArrayOperations fill:#F0FFFF,stroke:#333,stroke-width:2px
    style DynamicArraysExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    style FinancialExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    style PowerQuery fill:#F0FFFF,stroke:#333,stroke-width:2px
    style TextProcessingExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    style WebDataExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    style InformationExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    style NewFunctionsExcel fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue (sample of 40 functions)
    style SORT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SORTBY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style UNIQUE_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FILTER_EXCEL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SEQUENCE_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style RANDARRAY_EXCEL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style STOCKHISTORY_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style POWERQUERY fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TEXTJOIN_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CONCAT_EXCEL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style WEBSERVICE_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FILTERXML_EXCEL fill:#B9E9EB,stroke:#333,stroke-width:2px
    style LAMBDA_EXCEL fill:#F0FFF0,stroke:#333,stroke-width:2px
    style LET_EXCEL fill:#B9E9EB,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style SORTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SORTBYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style UNIQUEEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FILTEREXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SEQUENCEEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RANDARRAYEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style STOCKHISTORYEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style POWERQUERYSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TEXTJOINEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CONCATEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style WEBSERVICEEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FILTERXMLEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LAMBDAEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LETEXCELSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style SORTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SORTBYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style UNIQUEEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FILTEREXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SEQUENCEEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RANDARRAYEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style STOCKHISTORYEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style POWERQUERYEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TEXTJOINEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CONCATEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style WEBSERVICEEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FILTERXMLEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LAMBDAEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LETEXCELEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---