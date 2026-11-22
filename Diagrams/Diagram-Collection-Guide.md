---
domain: Spreadsheet Functions
category: Diagrams
subcategory: Overview
purpose:
  - Function Relationships
use-case:
  - Choosing a Diagram
  - Reading the Color Legend
  - Viewing Mermaid Diagrams
related: []
level: 2
source:
  - https://support.microsoft.com/en-us/office/excel-functions-by-category-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb
  - https://support.google.com/docs/table/25273
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - diagrams
  - mermaid
  - overview
---

# Diagram Collection Guide

This collection maps Excel and Google Sheets functions with Mermaid diagrams. Each file holds one diagram, written as a Mermaid code block inside a Markdown file.

## What the Diagrams Show

The collection has two kinds of diagram.

- Relationship diagrams (file names ending in `_diagram.md`) show the functions of one category, the functions they are commonly used with, and the functions they are similar to.
- Function trees (file names starting with `Functions-`) group a category's functions under group nodes, with a syntax node and an example node for each function.

A diagram can show fewer functions than its category holds. Where it does, its introduction says how many it shows. A function that belongs to another category can appear in a diagram for its relationships, and the introduction names its category.

## How to View the Diagrams

- On GitHub, Markdown files render Mermaid code blocks, so the diagram displays in the file view.
- Obsidian renders Mermaid code blocks in notes.
- In other tools, paste the text inside the code block into the Mermaid Live Editor at https://mermaid.live.

## Color Legend

- Category and group nodes: light cyan (`#F0FFFF`)
- Function nodes: light green (`#F0FFF0`) and light blue (`#B9E9EB`), alternating
- Syntax nodes: light pink (`#FFE4E1`)
- Example nodes: lavender (`#E6E6FA`)
- Gray dashed nodes: functions from other categories, shown for their relationships (`#f9f9f9` fill, dashed `#666` border)
- Solid arrows: commonly used together
- Dashed arrows: similar functions

Each relationship diagram sets its category color in a `classDef` line at the top of its Mermaid block.

## Categories and Function Counts

The counts are the functions in each category folder as of 2026-11-22. Each function is filed under its official Microsoft category, or under its Google category when it exists only in Google Sheets.

| Category | Functions | Folder |
|---|---|---|
| Statistical | 151 | Functions/Statistical |
| Math & Trig | 83 | Functions/Math & Trig |
| Engineering | 57 | Functions/Engineering |
| Financial | 55 | Functions/Financial |
| Text | 54 | Functions/Text |
| Lookup & Reference | 41 | Functions/Lookup & Reference |
| Google-specific | 29 | Functions/Google-specific |
| Information | 26 | Functions/Information |
| Date & Time | 26 | Functions/Date & Time |
| Logical | 19 | Functions/Logical |
| Database | 13 | Functions/Database |
| Web | 12 | Functions/Web |
| Cube | 7 | Functions/Cube |
| Add-in & Automation | 3 | Functions/Add-in & Automation |
| Total | 576 | |
