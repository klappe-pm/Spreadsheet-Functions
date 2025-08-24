---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - math & trig
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-17
  - - aliases
    - []
  - - tags
    - []
---
# ROMAN

## ROMAN Description

Converts Arabic numerals (standard numbers) to Roman numeral text representation. Supports numbers from 1 to 3999 with optional formatting styles for different levels of classical authenticity and modern abbreviated forms.

> [!f(x)] ROMAN Syntax
>
> ```spreadsheets
> ROMAN(number, [form])
> ```
>
> **Parameters:**
> - `number` (required): Integer from 1 to 3999 to convert to Roman numerals
> - `form` (optional): Format style 0-4, where 0=classic, 4=simplified (default: 0)

> [!f(x)] ROMAN Examples
>
> ```spreadsheets
> // Basic Roman numeral conversion
> ROMAN(1984) → "MCMLXXXIV"
> 
> // Year conversion for documents
> ROMAN(2024) → "MMXXIV"
> 
> // Chapter numbering
> ROMAN(12) → "XII"
> 
> // Simplified form (more concise)
> ROMAN(1994, 4) → "MCDXCIV" (vs classic "MCMXCIV")
> 
> // Single digit conversion
> ROMAN(5) → "V"
> ```

## Use Cases

### [[Document formatting]]
- **Academic papers**: Convert chapter numbers, section headings, and appendix labels to Roman numerals for scholarly formatting
- **Legal documents**: Format clause numbers, article references, and contract sections using traditional Roman numeral conventions
- **Historical texts**: Create period-appropriate numbering systems for historical reproductions and archival materials
- **Formal presentations**: Add classical elegance to outlines, agendas, and ceremonial documents

### [[Publishing and design]]  
- **Book publishing**: Generate Roman numerals for front matter page numbers, chapter headings, and volume designations
- **Magazine layout**: Create sophisticated numbering for special editions, anniversary issues, and premium content
- **Architectural drawings**: Label building phases, construction stages, and design iterations with Roman numerals
- **Event planning**: Number sequential events, tournament rounds, and ceremonial proceedings

### [[Educational materials]]
- **History lessons**: Demonstrate historical dating systems, timeline markers, and period-specific documentation
- **Mathematics education**: Teach number system conversions, ancient mathematics, and cultural numeracy
- **Language arts**: Create authentic-looking classical texts, poetry numbering, and literary analysis materials
- **Art history**: Label artistic periods, dynasty numbers, and cultural movements with appropriate Roman numerals

## Related

### Similar Functions

- [[ARABIC]] - Converts Roman numerals back to standard numbers, inverse operation of ROMAN function
- [[TEXT]] - Formats numbers as text with custom patterns, alternative for specialized numbering systems
- [[CONCATENATE]] - Combines Roman numerals with other text for complex formatting applications
- [[ROW]] - Generates sequential numbers that can be converted to Roman numerals for automatic numbering
- [[COLUMN]] - Provides position numbers for Roman numeral conversion in grid-based applications

## Text Functions

### [[CONCATENATE]]
Combines Roman numerals with other text elements for complex document formatting and labeling systems.

```spreadsheets
// Chapter title formatting
=CONCATENATE("Chapter ", ROMAN(A1), ": ", B1)
// Creates "Chapter XII: Introduction" format

// Legal document section numbering
=CONCATENATE("Section ", ROMAN(C1), ".", D1)
// Produces "Section IV.A" style numbering

// Historical date formatting
=CONCATENATE("Anno Domini ", ROMAN(E1))
// Creates "Anno Domini MMXXIV" format
```

### [[TEXT]]
Works with ROMAN for advanced formatting, padding, and alignment in professional document layouts.

```spreadsheets
// Right-aligned Roman numerals with padding
=TEXT(ROMAN(A1), "@@@@@@@@@@@@@@@")
// Pads Roman numeral to consistent width

// Combined numeric and Roman formatting
=A1 & " (" & ROMAN(A1) & ")"
// Shows "1984 (MCMLXXXIV)" format

// Conditional Roman numeral formatting
=IF(B1<=3999, ROMAN(B1), TEXT(B1, "0"))
// Uses Roman for valid range, Arabic for larger numbers
```

## Logical Functions

### [[IF]]
Essential for conditional Roman numeral formatting, range validation, and error handling in document systems.

```spreadsheets
// Validate number range for Roman conversion
=IF(AND(A1>=1, A1<=3999), ROMAN(A1), "Out of range")
// Only converts valid Roman numeral range

// Conditional numbering style
=IF(B1<=100, ROMAN(B1), B1)
// Uses Roman for small numbers, Arabic for large

// Document type-specific formatting
=IF(C1="formal", ROMAN(D1), D1)
// Applies Roman numerals only for formal documents
```

### [[ROW]]
Generates sequential numbers for automatic Roman numeral conversion in lists, outlines, and structured documents.

```spreadsheets
// Automatic Roman numeral row numbering
=ROMAN(ROW()-1)
// Creates I, II, III... for each row (starting row 2)

// Chapter numbering with Roman numerals
=ROMAN(ROW(A1:A10))
// Generates Roman numerals I through X for chapters

// Outline numbering system
="" & ROMAN(ROW()) & ". " & A1
// Creates "I. Topic" format for outline items
```

## Commonly Used With Functions Examples

### ROMAN with Document Formatting
```spreadsheets
// Academic paper section formatting
=ROMAN(A1) & ". " & B1 & " (Page " & C1 & ")"
// Creates "IV. Literature Review (Page 23)" format

// Legal document cross-reference
="See Section " & ROMAN(D1) & ", Subsection " & E1
// Produces "See Section III, Subsection A" references
```

### ROMAN with Historical Applications
```spreadsheets
// Dynasty or reign formatting
="King Henry " & ROMAN(F1) & " (r. " & G1 & "-" & H1 & ")"
// Creates "King Henry VIII (r. 1509-1547)" format

// Century designation
="" & ROMAN(I1) & " Century " & J1
// Produces "XVI Century Renaissance" format
```

### ROMAN with Educational Content
```spreadsheets
// Mathematical progression display
=A1 & " = " & ROMAN(A1)
// Shows "24 = XXIV" for number system education

// Timeline event numbering
="Event " & ROMAN(K1) & ": " & L1 & " (" & M1 & ")"
// Creates "Event III: Battle of Hastings (1066)" format
```
