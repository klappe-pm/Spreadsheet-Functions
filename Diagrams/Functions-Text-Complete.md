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
    - - Spreadsheets-Functions-Text-Complete
  - - tags
    - []
---
# Spreadsheets-Functions-Text-Complete

```mermaid

graph LR
    Text["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Text</b><br/>────────────────<br/>Text manipulation and processing functions<br/><b>Total Functions:</b> 41</div>"]
    
    Text --> Conversion["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Conversion</b><br/>────────────────<br/>Text conversion and formatting<br/><b>Functions:</b> 13</div>"]
    
    Text --> StringManipulation["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>String Manipulation</b><br/>────────────────<br/>String processing and manipulation<br/><b>Functions:</b> 10</div>"]
    
    Text --> Formatting["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Formatting</b><br/>────────────────<br/>Text formatting functions<br/><b>Functions:</b> 10</div>"]
    
    Text --> SearchReplace["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Search and Replace</b><br/>────────────────<br/>Text search and replacement<br/><b>Functions:</b> 4</div>"]
    
    Text --> Regex["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>Regex</b><br/>────────────────<br/>Regular expression functions<br/><b>Functions:</b> 3</div>"]
    
    Text --> NewFunctions["<div align='left' style='font-family: MonoLisa, monospace;'><b style='font-size: 1.1em;'>New Functions</b><br/>────────────────<br/>Modern text functions<br/><b>Functions:</b> 1</div>"]
    
    %% Conversion Functions (13 functions)
    Conversion --> CHAR["<div align='left' style='font-family: MonoLisa, monospace;'><b>CHAR</b><br/>────────────────<br/>Returns the character for a given number</div>"]
    CHAR --> CHARSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CHAR(number)</div>"]
    CHAR --> CHAREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CHAR(65) → &quot;A&quot;</div>"]
    
    Conversion --> CODE["<div align='left' style='font-family: MonoLisa, monospace;'><b>CODE</b><br/>────────────────<br/>Returns numeric code for first character</div>"]
    CODE --> CODESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CODE(text)</div>"]
    CODE --> CODEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CODE(&quot;A&quot;) → 65</div>"]
    
    Conversion --> TEXT["<div align='left' style='font-family: MonoLisa, monospace;'><b>TEXT</b><br/>────────────────<br/>Formats a number and converts it to text</div>"]
    TEXT --> TEXTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TEXT(value, format_text)</div>"]
    TEXT --> TEXTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TEXT(1234.567, &quot;$#,##0.00&quot;) → &quot;$1,234.57&quot;</div>"]
    
    Conversion --> VALUE["<div align='left' style='font-family: MonoLisa, monospace;'><b>VALUE</b><br/>────────────────<br/>Converts a text string to a number</div>"]
    VALUE --> VALUESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>VALUE(text)</div>"]
    VALUE --> VALUEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=VALUE(&quot;$1,000&quot;) → 1000</div>"]
    
    %% String Manipulation Functions (10 functions)
    StringManipulation --> CONCATENATE["<div align='left' style='font-family: MonoLisa, monospace;'><b>CONCATENATE</b><br/>────────────────<br/>Joins text strings into one text string</div>"]
    CONCATENATE --> CONCATENATESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>CONCATENATE(text1, [text2], ...)</div>"]
    CONCATENATE --> CONCATENATEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=CONCATENATE(&quot;Hello&quot;, &quot; &quot;, &quot;World&quot;) → &quot;Hello World&quot;</div>"]
    
    StringManipulation --> LEFT["<div align='left' style='font-family: MonoLisa, monospace;'><b>LEFT</b><br/>────────────────<br/>Returns leftmost characters from a text string</div>"]
    LEFT --> LEFTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LEFT(text, [num_chars])</div>"]
    LEFT --> LEFTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LEFT(&quot;Hello World&quot;, 5) → &quot;Hello&quot;</div>"]
    
    StringManipulation --> RIGHT["<div align='left' style='font-family: MonoLisa, monospace;'><b>RIGHT</b><br/>────────────────<br/>Returns rightmost characters from a text string</div>"]
    RIGHT --> RIGHTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>RIGHT(text, [num_chars])</div>"]
    RIGHT --> RIGHTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=RIGHT(&quot;Hello World&quot;, 5) → &quot;World&quot;</div>"]
    
    StringManipulation --> MID["<div align='left' style='font-family: MonoLisa, monospace;'><b>MID</b><br/>────────────────<br/>Returns characters from the middle of a text string</div>"]
    MID --> MIDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>MID(text, start_num, num_chars)</div>"]
    MID --> MIDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=MID(&quot;Hello World&quot;, 7, 5) → &quot;World&quot;</div>"]
    
    StringManipulation --> LEN["<div align='left' style='font-family: MonoLisa, monospace;'><b>LEN</b><br/>────────────────<br/>Returns the number of characters in a text string</div>"]
    LEN --> LENSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LEN(text)</div>"]
    LEN --> LENEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LEN(&quot;Hello World&quot;) → 11</div>"]
    
    StringManipulation --> TRIM["<div align='left' style='font-family: MonoLisa, monospace;'><b>TRIM</b><br/>────────────────<br/>Removes spaces from text except single spaces between words</div>"]
    TRIM --> TRIMSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TRIM(text)</div>"]
    TRIM --> TRIMEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TRIM(&quot;  Hello   World  &quot;) → &quot;Hello World&quot;</div>"]
    
    %% Formatting Functions (10 functions)
    Formatting --> UPPER["<div align='left' style='font-family: MonoLisa, monospace;'><b>UPPER</b><br/>────────────────<br/>Converts text to uppercase</div>"]
    UPPER --> UPPERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>UPPER(text)</div>"]
    UPPER --> UPPEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=UPPER(&quot;hello world&quot;) → &quot;HELLO WORLD&quot;</div>"]
    
    Formatting --> LOWER["<div align='left' style='font-family: MonoLisa, monospace;'><b>LOWER</b><br/>────────────────<br/>Converts text to lowercase</div>"]
    LOWER --> LOWERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>LOWER(text)</div>"]
    LOWER --> LOWEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=LOWER(&quot;HELLO WORLD&quot;) → &quot;hello world&quot;</div>"]
    
    Formatting --> PROPER["<div align='left' style='font-family: MonoLisa, monospace;'><b>PROPER</b><br/>────────────────<br/>Capitalizes the first letter of each word</div>"]
    PROPER --> PROPERSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>PROPER(text)</div>"]
    PROPER --> PROPEREXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=PROPER(&quot;hello world&quot;) → &quot;Hello World&quot;</div>"]
    
    %% Search and Replace Functions (4 functions)
    SearchReplace --> FIND["<div align='left' style='font-family: MonoLisa, monospace;'><b>FIND</b><br/>────────────────<br/>Finds one text value within another (case-sensitive)</div>"]
    FIND --> FINDSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>FIND(find_text, within_text, [start_num])</div>"]
    FIND --> FINDEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=FIND(&quot;World&quot;, &quot;Hello World&quot;) → 7</div>"]
    
    SearchReplace --> SEARCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>SEARCH</b><br/>────────────────<br/>Finds one text value within another (case-insensitive)</div>"]
    SEARCH --> SEARCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SEARCH(find_text, within_text, [start_num])</div>"]
    SEARCH --> SEARCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SEARCH(&quot;world&quot;, &quot;Hello World&quot;) → 7</div>"]
    
    SearchReplace --> SUBSTITUTE["<div align='left' style='font-family: MonoLisa, monospace;'><b>SUBSTITUTE</b><br/>────────────────<br/>Substitutes new text for old text in a text string</div>"]
    SUBSTITUTE --> SUBSTITUTESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>SUBSTITUTE(text, old_text, new_text, [instance_num])</div>"]
    SUBSTITUTE --> SUBSTITUTEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=SUBSTITUTE(&quot;Hello World&quot;, &quot;World&quot;, &quot;Excel&quot;) → &quot;Hello Excel&quot;</div>"]
    
    SearchReplace --> REPLACE["<div align='left' style='font-family: MonoLisa, monospace;'><b>REPLACE</b><br/>────────────────<br/>Replaces characters within text</div>"]
    REPLACE --> REPLACESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REPLACE(old_text, start_num, num_chars, new_text)</div>"]
    REPLACE --> REPLACEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REPLACE(&quot;Hello World&quot;, 7, 5, &quot;Excel&quot;) → &quot;Hello Excel&quot;</div>"]
    
    %% Regex Functions (3 functions)
    Regex --> REGEXMATCH["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXMATCH</b><br/>────────────────<br/>Tests whether a piece of text matches a regular expression</div>"]
    REGEXMATCH --> REGEXMATCHSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXMATCH(text, regular_expression)</div>"]
    REGEXMATCH --> REGEXMATCHEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXMATCH(&quot;hello@gmail.com&quot;, &quot;.+@.+&quot;) → TRUE</div>"]
    
    Regex --> REGEXEXTRACT["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXEXTRACT</b><br/>────────────────<br/>Extracts matching substrings according to a regular expression</div>"]
    REGEXEXTRACT --> REGEXEXTRACTSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXEXTRACT(text, regular_expression)</div>"]
    REGEXEXTRACT --> REGEXEXTRACTEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXEXTRACT(&quot;hello@gmail.com&quot;, &quot;@(.+)&quot;) → &quot;gmail.com&quot;</div>"]
    
    Regex --> REGEXREPLACE["<div align='left' style='font-family: MonoLisa, monospace;'><b>REGEXREPLACE</b><br/>────────────────<br/>Replaces part of a text string with different text using regex</div>"]
    REGEXREPLACE --> REGEXREPLACESYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>REGEXREPLACE(text, regular_expression, replacement)</div>"]
    REGEXREPLACE --> REGEXREPLACEEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=REGEXREPLACE(&quot;hello@gmail.com&quot;, &quot;@.+&quot;, &quot;@yahoo.com&quot;) → &quot;hello@yahoo.com&quot;</div>"]
    
    %% New Functions (1 function)
    NewFunctions --> TEXTJOIN["<div align='left' style='font-family: MonoLisa, monospace;'><b>TEXTJOIN</b><br/>────────────────<br/>Combines text from multiple ranges with a delimiter</div>"]
    TEXTJOIN --> TEXTJOINSYNTAX["<div align='left' style='font-family: MonoLisa, monospace;'><b>Syntax</b><br/>────────────────<br/>TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)</div>"]
    TEXTJOIN --> TEXTJOINEXAMPLE["<div align='left' style='font-family: MonoLisa, monospace;'><b>Example</b><br/>────────────────<br/>=TEXTJOIN(&quot;, &quot;, TRUE, A1:A5) → &quot;Apple, Banana, Cherry&quot;</div>"]
    
    %% Styling
    style Text fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Conversion fill:#F0FFFF,stroke:#333,stroke-width:2px
    style StringManipulation fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Formatting fill:#F0FFFF,stroke:#333,stroke-width:2px
    style SearchReplace fill:#F0FFFF,stroke:#333,stroke-width:2px
    style Regex fill:#F0FFFF,stroke:#333,stroke-width:2px
    style NewFunctions fill:#F0FFFF,stroke:#333,stroke-width:2px
    
    %% Functions alternate: odd=green, even=blue (global numbering 1-41)
    style CHAR fill:#F0FFF0,stroke:#333,stroke-width:2px
    style CODE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TEXT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style VALUE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style CONCATENATE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style LEFT fill:#B9E9EB,stroke:#333,stroke-width:2px
    style RIGHT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style MID fill:#B9E9EB,stroke:#333,stroke-width:2px
    style LEN fill:#F0FFF0,stroke:#333,stroke-width:2px
    style TRIM fill:#B9E9EB,stroke:#333,stroke-width:2px
    style UPPER fill:#F0FFF0,stroke:#333,stroke-width:2px
    style LOWER fill:#B9E9EB,stroke:#333,stroke-width:2px
    style PROPER fill:#F0FFF0,stroke:#333,stroke-width:2px
    style FIND fill:#B9E9EB,stroke:#333,stroke-width:2px
    style SEARCH fill:#F0FFF0,stroke:#333,stroke-width:2px
    style SUBSTITUTE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style REPLACE fill:#F0FFF0,stroke:#333,stroke-width:2px
    style REGEXMATCH fill:#B9E9EB,stroke:#333,stroke-width:2px
    style REGEXEXTRACT fill:#F0FFF0,stroke:#333,stroke-width:2px
    style REGEXREPLACE fill:#B9E9EB,stroke:#333,stroke-width:2px
    style TEXTJOIN fill:#F0FFF0,stroke:#333,stroke-width:2px
    
    %% All syntax nodes - pink
    style CHARSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CODESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TEXTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style VALUESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style CONCATENATESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LEFTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style RIGHTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style MIDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LENSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TRIMSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style UPPERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style LOWERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style PROPERSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style FINDSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SEARCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style SUBSTITUTESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REPLACESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXMATCHSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXEXTRACTSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style REGEXREPLACESYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    style TEXTJOINSYNTAX fill:#FFE4E1,stroke:#333,stroke-width:2px
    
    %% All example nodes - lavender
    style CHAREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CODEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TEXTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style VALUEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style CONCATENATEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LEFTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style RIGHTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style MIDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LENEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TRIMEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style UPPEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style LOWEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style PROPEREXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style FINDEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SEARCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style SUBSTITUTEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REPLACEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXMATCHEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXEXTRACTEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style REGEXREPLACEEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    style TEXTJOINEXAMPLE fill:#E6E6FA,stroke:#333,stroke-width:2px
    
```

---