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
    - - Spreadsheets-Functions-Cube
  - - tags
    - []
---
# Spreadsheets-Functions-Cube

```mermaid

graph LR
    A["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Cube</b><br/>────────────────<br/>OLAP functions for multidimensional data analysis<br/><b>Total Functions:</b> 6</div>"] --> B["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>OLAP Functions</b><br/>────────────────<br/>Functions for Online Analytical Processing<br/><b>Total Functions:</b> 6</div>"]
    
    B --> CUBEVALUE["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBEVALUE</b><br/>────────────────<br/>Returns an aggregated value from a cube</div>"]
    
    CUBEVALUE --> CUBEVALUESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBEVALUE(connection, [member_expression1, …])</div>"]
    
    CUBEVALUE --> CUBEVALUEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBEVALUE(&quot;Sales&quot;, &quot;[Measures].[Profit]&quot;, &quot;[Time].[2025]&quot;)</div>"]
    
    B --> CUBEMEMBER["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBEMEMBER</b><br/>────────────────<br/>Returns a member or tuple from the cube</div>"]
    
    CUBEMEMBER --> CUBEMEMBERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBEMEMBER(connection, member_expression, [caption])</div>"]
    
    CUBEMEMBER --> CUBEMEMBEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBEMEMBER(&quot;Sales&quot;, &quot;[Product].[All Products].[Bikes]&quot;)</div>"]
    
    B --> CUBERANKEDMEMBER["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBERANKEDMEMBER</b><br/>────────────────<br/>Returns the nth ranked member in a set</div>"]
    
    CUBERANKEDMEMBER --> CUBERANKEDMEMBERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBERANKEDMEMBER(connection, set_expression, rank, [caption])</div>"]
    
    CUBERANKEDMEMBER --> CUBERANKEDMEMBEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBERANKEDMEMBER(&quot;Sales&quot;, &quot;[Product].[Product].[All]&quot;, 1)</div>"]
    
    B --> CUBESET["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBESET</b><br/>────────────────<br/>Defines a calculated set of members or tuples</div>"]
    
    CUBESET --> CUBESETSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])</div>"]
    
    CUBESET --> CUBESETEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBESET(&quot;Sales&quot;, &quot;[Product].[All Products].Children&quot;)</div>"]
    
    B --> CUBESETCOUNT["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBESETCOUNT</b><br/>────────────────<br/>Returns the number of items in a set</div>"]
    
    CUBESETCOUNT --> CUBESETSYNTAX2["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBESETCOUNT(set)</div>"]
    
    CUBESETCOUNT --> CUBESETEXAMPLE2["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBESETCOUNT(A1)</div>"]
    
    B --> CUBEKPIMEMBER["<div align='left' style='font-family: MonoLisa, monospace;'><b>CUBEKPIMEMBER</b><br/>────────────────<br/>Returns a key performance indicator (KPI) property</div>"]
    
    CUBEKPIMEMBER --> CUBEKPIMEMBERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])</div>"]
    
    CUBEKPIMEMBER --> CUBEKPIMEMBEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CUBEKPIMEMBER(&quot;Sales&quot;, &quot;Revenue&quot;, 1)</div>"]
    
    style A fill:#F0FFFF,stroke:#333,stroke-width:2px
    style B fill:#F0FFFF,stroke:#333,stroke-width:2px
    style CUBEVALUE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CUBEVALUESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBEVALUEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CUBEMEMBER fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CUBEMEMBERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBEMEMBEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CUBERANKEDMEMBER fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CUBERANKEDMEMBERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBERANKEDMEMBEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CUBESET fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CUBESETSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBESETEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CUBESETCOUNT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CUBESETSYNTAX2 fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBESETEXAMPLE2 fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CUBEKPIMEMBER fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CUBEKPIMEMBERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CUBEKPIMEMBEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
    
```
