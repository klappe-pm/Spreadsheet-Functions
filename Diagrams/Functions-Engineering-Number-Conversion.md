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
    - - Spreadsheets-Functions-Engineering-Number Conversion
  - - tags
    - []
---
# Spreadsheets-Functions-Engineering-Number Conversion

```mermaid

graph LR
    Engineering["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering</b><br/>────────────────<br/>Engineering and technical calculations<br/><b>Total Functions:</b> 54</div>"]
    
    Engineering --> NumConv["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Number Conversion</b><br/>────────────────<br/>Number base conversions<br/><b>Functions:</b> 12</div>"]
    
    %% Number Conversion (12 functions)
    %% BIN2DEC - Function 1
    NumConv --> BIN2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2DEC</b><br/>────────────────<br/>Converts a binary number to decimal</div>"]
    BIN2DEC --> BIN2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2DEC(number)</div>"]
    BIN2DEC --> BIN2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2DEC(&quot;1010&quot;) → 10</div>"]
    
    %% BIN2HEX - Function 2
    NumConv --> BIN2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2HEX</b><br/>────────────────<br/>Converts a binary number to hexadecimal</div>"]
    BIN2HEX --> BIN2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2HEX(number, [places])</div>"]
    BIN2HEX --> BIN2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2HEX(&quot;1010&quot;) → &quot;A&quot;</div>"]
    
    %% BIN2OCT - Function 3
    NumConv --> BIN2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BIN2OCT</b><br/>────────────────<br/>Converts a binary number to octal</div>"]
    BIN2OCT --> BIN2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BIN2OCT(number, [places])</div>"]
    BIN2OCT --> BIN2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BIN2OCT(&quot;1010&quot;) → &quot;12&quot;</div>"]
    
    %% DEC2BIN - Function 4
    NumConv --> DEC2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2BIN</b><br/>────────────────<br/>Converts a decimal number to binary</div>"]
    DEC2BIN --> DEC2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2BIN(number, [places])</div>"]
    DEC2BIN --> DEC2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2BIN(10) → &quot;1010&quot;</div>"]
    
    %% DEC2HEX - Function 5
    NumConv --> DEC2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2HEX</b><br/>────────────────<br/>Converts a decimal number to hexadecimal</div>"]
    DEC2HEX --> DEC2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2HEX(number, [places])</div>"]
    DEC2HEX --> DEC2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2HEX(10) → &quot;A&quot;</div>"]
    
    %% DEC2OCT - Function 6
    NumConv --> DEC2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>DEC2OCT</b><br/>────────────────<br/>Converts a decimal number to octal</div>"]
    DEC2OCT --> DEC2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>DEC2OCT(number, [places])</div>"]
    DEC2OCT --> DEC2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=DEC2OCT(10) → &quot;12&quot;</div>"]
    
    %% HEX2BIN - Function 7
    NumConv --> HEX2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2BIN</b><br/>────────────────<br/>Converts a hexadecimal number to binary</div>"]
    HEX2BIN --> HEX2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2BIN(number, [places])</div>"]
    HEX2BIN --> HEX2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2BIN(&quot;A&quot;) → &quot;1010&quot;</div>"]
    
    %% HEX2DEC - Function 8
    NumConv --> HEX2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2DEC</b><br/>────────────────<br/>Converts a hexadecimal number to decimal</div>"]
    HEX2DEC --> HEX2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2DEC(number)</div>"]
    HEX2DEC --> HEX2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2DEC(&quot;A&quot;) → 10</div>"]
    
    %% HEX2OCT - Function 9
    NumConv --> HEX2OCT["<div align='left' style='font-family: MonoLisa, monospace;'><b>HEX2OCT</b><br/>────────────────<br/>Converts a hexadecimal number to octal</div>"]
    HEX2OCT --> HEX2OCTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>HEX2OCT(number, [places])</div>"]
    HEX2OCT --> HEX2OCTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=HEX2OCT(&quot;A&quot;) → &quot;12&quot;</div>"]
    
    %% OCT2BIN - Function 10
    NumConv --> OCT2BIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2BIN</b><br/>────────────────<br/>Converts an octal number to binary</div>"]
    OCT2BIN --> OCT2BINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2BIN(number, [places])</div>"]
    OCT2BIN --> OCT2BINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2BIN(&quot;12&quot;) → &quot;1010&quot;</div>"]
    
    %% OCT2DEC - Function 11
    NumConv --> OCT2DEC["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2DEC</b><br/>────────────────<br/>Converts an octal number to decimal</div>"]
    OCT2DEC --> OCT2DECSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2DEC(number)</div>"]
    OCT2DEC --> OCT2DECEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2DEC(&quot;12&quot;) → 10</div>"]
    
    %% OCT2HEX - Function 12
    NumConv --> OCT2HEX["<div align='left' style='font-family: MonoLisa, monospace;'><b>OCT2HEX</b><br/>────────────────<br/>Converts an octal number to hexadecimal</div>"]
    OCT2HEX --> OCT2HEXSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>OCT2HEX(number, [places])</div>"]
    OCT2HEX --> OCT2HEXEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=OCT2HEX(&quot;12&quot;) → &quot;A&quot;</div>"]
    
    %% Styling
    style Engineering fill:#F0FFFF,stroke:#333,stroke-width:2px
    style NumConv fill:#F0FFFF,stroke:#333,stroke-width:2px
    %% Functions alternate colors
    style BIN2DEC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BIN2HEX fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BIN2OCT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DEC2BIN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style DEC2HEX fill:#F0FFF0,stroke:#333,stroke-width:2px
    style DEC2OCT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style HEX2BIN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style HEX2DEC fill:#B9E9EB,stroke:#333,stroke-width:2px
    style HEX2OCT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style OCT2BIN fill:#B9E9EB,stroke:#333,stroke-width:2px
    style OCT2DEC fill:#F0FFF0,stroke:#333,stroke-width:2px
    style OCT2HEX fill:#B9E9EB,stroke:#333,stroke-width:2px
    %% All syntax nodes - pink
    style BIN2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BIN2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BIN2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style DEC2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style HEX2OCTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2BINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2DECSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style OCT2HEXSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    %% All example nodes - lavender
    style BIN2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BIN2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BIN2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style DEC2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style HEX2OCTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2BINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2DECEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style OCT2HEXEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```