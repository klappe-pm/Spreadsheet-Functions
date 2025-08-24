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
    - - Spreadsheets-Functions-Engineering
  - - tags
    - []
---
# Spreadsheets-Functions-Engineering

```mermaid

graph LR
    Engineering["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Engineering</b><br/>────────────────<br/>Engineering and technical calculations<br/><b>Total Functions:</b> 54</div>"]
    
    Engineering --> Bitwise["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Bitwise Operations</b><br/>────────────────<br/>Bitwise logical operations<br/><b>Functions:</b> 5</div>"]
    
    %% Bitwise Operations (5 functions)
    %% BITAND - Function 1
    Bitwise --> BITAND["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITAND</b><br/>────────────────<br/>Returns the bitwise AND of two numbers</div>"]
    BITAND --> BITANDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITAND(number1, number2)</div>"]
    BITAND --> BITANDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITAND(5, 3) → 1</div>"]
    
    %% BITLSHIFT - Function 2
    Bitwise --> BITLSHIFT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITLSHIFT</b><br/>────────────────<br/>Shifts a number left by a specified number of bits</div>"]
    BITLSHIFT --> BITLSHIFTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITLSHIFT(number, shift_amount)</div>"]
    BITLSHIFT --> BITLSHIFTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITLSHIFT(5, 2) → 20</div>"]
    
    %% BITOR - Function 3
    Bitwise --> BITOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITOR</b><br/>────────────────<br/>Returns the bitwise OR of two numbers</div>"]
    BITOR --> BITORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITOR(number1, number2)</div>"]
    BITOR --> BITOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITOR(5, 3) → 7</div>"]
    
    %% BITRSHIFT - Function 4
    Bitwise --> BITRSHIFT["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITRSHIFT</b><br/>────────────────<br/>Shifts a number right by a specified number of bits</div>"]
    BITRSHIFT --> BITRSHIFTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITRSHIFT(number, shift_amount)</div>"]
    BITRSHIFT --> BITRSHIFTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITRSHIFT(20, 2) → 5</div>"]
    
    %% BITXOR - Function 5
    Bitwise --> BITXOR["<div align='left' style='font-family: MonoLisa, monospace;'><b>BITXOR</b><br/>────────────────<br/>Returns the bitwise XOR of two numbers</div>"]
    BITXOR --> BITXORSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>BITXOR(number1, number2)</div>"]
    BITXOR --> BITXOREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=BITXOR(5, 3) → 6</div>"]
    
    %% Styling
    style Engineering fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Bitwise fill:#F0FFFF,stroke:#333,stroke-width:2px
    %% Functions alternate colors - continuous numbering across subcategories
    style BITAND fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BITLSHIFT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BITOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style BITRSHIFT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style BITXOR fill:#F0FFF0,stroke:#333,stroke-width:2px
    %% All syntax nodes - pink
    style BITANDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITLSHIFTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITRSHIFTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style BITXORSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    %% All example nodes - lavender
    style BITANDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITLSHIFTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITRSHIFTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style BITXOREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```