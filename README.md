# Excel and Google Sheets Functions Documentation

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-purple?logo=obsidian)](https://obsidian.md/)
[![Functions](https://img.shields.io/badge/Functions-539+-brightgreen)](./Functions/)
[![Categories](https://img.shields.io/badge/Categories-15-blue)](./Functions/)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-success)](./README.md)

A comprehensive, standardized documentation system for 539+ Excel and Google Sheets functions with consistent YAML frontmatter and structured markdown optimized for Obsidian and other knowledge management systems. Every Excel and Sheets function in a handy markdown format, including definitions, explanations, and examples.

## 🚀 Features

- **Comprehensive Coverage**: 539 standardized function documentation files
- **Obsidian Optimized**: Perfect YAML frontmatter for knowledge management systems
- **Consistent Structure**: Uniform formatting across all function categories
- **Platform Agnostic**: Works with Excel and Google Sheets
- **Linked References**: Double-bracketed use cases and related functions
- **Category Organization**: 15 function categories with clear taxonomy
- **Date Tracking**: Created and revision dates for all functions
- **Search Ready**: Clean tags and aliases for powerful filtering

## 📊 Function Categories

| Category | Functions | Description |
|----------|-----------|-------------|
| **Statistical** | 89 | Distributions, averages, correlation, regression |
| **Math & Trig** | 77 | Arithmetic, trigonometry, matrix, rounding |
| **Engineering** | 68 | Number systems, complex numbers, conversions |
| **Financial** | 67 | Investments, loans, depreciation, yield |
| **Text** | 43 | String manipulation, formatting, search |
| **Information** | 42 | Type checking, error validation, metadata |
| **Excel Functions** | 40 | LAMBDA, dynamic arrays, advanced features |
| **Lookup & Reference** | 30 | VLOOKUP, INDEX/MATCH, array lookups |
| **Google Sheets** | 29 | IMPORT functions, QUERY, Sheets-specific |
| **Date & Time** | 25 | Date arithmetic, formatting, business days |
| **Logical** | 14 | IF statements, Boolean logic, conditionals |
| **Database** | 12 | DAVERAGE, DCOUNT, criteria-based operations |
| **Cube** | 6 | OLAP functions for business intelligence |
| **Dynamic Arrays** | 3 | UNIQUE, SORT, modern array functions |
| **Web** | 1 | Web services and data import |

## 🧠 Obsidian.md Integration

This repository is optimized for [Obsidian](https://obsidian.md/), a powerful knowledge management system that works perfectly with our standardized markdown structure.

### Quick Setup in Obsidian

1. **Clone or Download** this repository
2. **Open Obsidian** and choose "Open folder as vault"
3. **Select** the `/Functions/` directory as your vault root
4. **Enable** the following core plugins:
   - **Tags**: For filtering by function categories
   - **Graph View**: To visualize function relationships
   - **Search**: For powerful function discovery
   - **Templates**: For creating new function documentation

### Obsidian Features You'll Love

#### 🔍 **Powerful Search & Filtering**
```
tag:#mathematical              # Find all math functions
tag:#excel                     # Excel-specific functions  
tag:#sheets                    # Google Sheets functions
path:"Statistical/"            # All statistical functions
"[[Data validation]]"          # Functions used for data validation
```

#### 🌐 **Graph View**
- Visualize connections between functions
- See which functions are commonly used together
- Discover related functions through linked references

#### 📝 **Templates & Consistency**
- Every function follows the same YAML structure
- Consistent use cases with double-bracketed links
- Standardized "Related Functions" sections

#### 🏷️ **Smart Tagging System**
```yaml
categories: spreadsheets       # Always "spreadsheets"
subCategories: 
  - excel                     # Platform compatibility
  - sheets
topics: statistical           # Function category
subTopics: []                 # Specific subcategory
tags: []                      # Currently empty, ready for your workflow
aliases: []                   # Alternative function names
```

### Recommended Obsidian Plugins

#### Core Plugins (Built-in)
- ✅ **Graph View**: Visualize function relationships
- ✅ **Search**: Advanced filtering and discovery
- ✅ **Tags**: Category-based organization
- ✅ **Templates**: Consistent function creation

#### Community Plugins (Optional)
- **Dataview**: Query functions by metadata
- **Tag Wrangler**: Better tag management
- **Advanced Tables**: Enhanced markdown tables
- **Calendar**: View functions by creation date

### Example Obsidian Workflows

#### 📊 **Find Functions by Category**
1. Use graph view to see all statistical functions
2. Filter by `tag:#statistical`
3. Browse connected functions through links

#### 🔗 **Discover Function Relationships**
1. Open any function (e.g., `AVERAGE.md`)
2. Check "Related Functions" section
3. Follow links to commonly used functions
4. See use case connections in double brackets

#### 📅 **Track Recent Updates**
1. Search by `dateRevised:2025-08-17`
2. View all recently updated functions
3. Use calendar view to see revision timeline

## 🚀 Getting Started

### Option 1: Obsidian Vault (Recommended)
```bash
# Clone repository
git clone [your-repo-url]

# Open in Obsidian
1. Open Obsidian
2. Choose "Open folder as vault" 
3. Select the cloned repository folder
4. Start exploring with Graph View
```

### Option 2: Standard Markdown
```bash
# Clone repository  
git clone [your-repo-url]
cd spreadsheet-functions

# Browse with any markdown editor
# VS Code, Typora, MarkText, etc.
```

## 📚 Repository Structure

```
spreadsheet-functions/
├── README.md                   # This file - project overview
├── .gitignore                  # Clean repository (Functions + Diagrams only)
├── Functions/                  # 539 function documentation files
│   ├── Statistical/           # 89 statistical functions
│   ├── Math & Trig/           # 77 mathematical functions  
│   ├── Engineering/           # 68 engineering functions
│   ├── Financial/             # 67 financial functions
│   ├── Text/                  # 43 text manipulation functions
│   ├── Information/           # 42 information functions
│   ├── Excel-specific/        # 40 Excel-only functions
│   ├── Lookup & Reference/    # 30 lookup functions
│   ├── Google-specific/       # 29 Google Sheets functions
│   ├── Date & Time/           # 25 date/time functions
│   ├── Logical/              # 14 logical functions
│   ├── Database/             # 12 database functions
│   ├── Cube/                 # 6 OLAP cube functions
│   ├── Dynamic Arrays/       # 3 modern array functions
│   └── Web/                  # 1 web function
└── Diagrams/                  # Visual documentation and flowcharts
    ├── Functions-Summary Table.md
    ├── Functions-Engineering-Complete.md
    └── [Additional diagram files...]
```

## 🎯 Key Features & Structure

### Standardized YAML Frontmatter
Every function file includes consistent metadata:
```yaml
---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: engineering                   # Category from folder structure
subTopics: []                        # Future expansion
dateCreated: 2025-06-20             # Original creation date preserved
dateRevised: 2025-08-17             # Updated to current date
aliases: []                         # Alternative function names
tags: []                            # Ready for your workflow
---
```

### Linked Use Cases & Functions
Every function includes:
- **3 Use Cases** with double-bracketed links: `[[Data validation]]`
- **Similar Functions** section with related function names
- **Commonly Used With** section showing function combinations
- **Sub-use cases** for each commonly used function

### Automated Processing
The project includes scripts for:
- YAML frontmatter standardization across all files
- Topic assignment based on folder structure  
- Field migration from old formats to new standards
- Date preservation and revision tracking

## 📈 Project Statistics

### Current Status (August 17, 2025)
- **Total Functions**: 539 documented and standardized
- **Categories**: 15 functional groupings
- **Platform Support**: Excel and Google Sheets compatible
- **YAML Standardization**: 100% complete across all files
- **Link Structure**: Double-bracketed references for Obsidian

### Quality Metrics
- ✅ **Consistent Structure**: All 539 files follow identical format
- ✅ **Clean YAML**: Standardized frontmatter with proper arrays
- ✅ **Date Tracking**: Original creation dates preserved, revision dates updated
- ✅ **Platform Agnostic**: Works with Excel and Google Sheets
- ✅ **Obsidian Ready**: Perfect for knowledge management workflows
- ✅ **Search Optimized**: Clean topics, categories, and linking structure

## 🔧 Function Template

Each function follows this exact structure:
```markdown
---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: [category-name]
subTopics: []
dateCreated: [preserved-date]
dateRevised: 2025-08-17
aliases: []
tags: []
---

# FUNCTION_NAME

## FUNCTION_NAME Description

[Function description from original content]

> [!f(x)] FUNCTION_NAME Syntax
>
> ```spreadsheets
> FUNCTION_NAME()
> ```

> [!f(x)] FUNCTION_NAME Example
>
> ```spreadsheets
> FUNCTION_NAME() → result
> ```

## Use Cases

- [[Use case 1]]
- [[Use case 2]]  
- [[Use case 3]]

## Related

### Similar Functions

- FUNCTION1
- FUNCTION2
- FUNCTION3

### Commonly Used With Functions

- IF
  - [[Use case]]
  - [[Data validation]]
  - [[Report generation]]
[... 4 more functions with sub-use cases]
```

## 🔗 Related Resources

- **Excel Functions**: [Microsoft Excel Function Reference](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
- **Google Sheets Functions**: [Google Sheets Function List](https://support.google.com/docs/table/25273)
- **Obsidian**: [Obsidian Knowledge Management](https://obsidian.md/)
- **Markdown Guide**: [Markdown Syntax Reference](https://www.markdownguide.org/)

## 🤝 Contributing

Contributions welcome! To add or improve function documentation:

1. **Fork** this repository
2. **Follow** the established YAML frontmatter format
3. **Use** the function template structure
4. **Include** practical use cases with double-bracket links
5. **Test** in Obsidian or another markdown editor
6. **Submit** a pull request

### Contribution Guidelines
- Maintain consistent YAML structure across all files
- Use double-bracketed links for use cases: `[[Data validation]]`
- Include both Excel and Google Sheets compatibility where applicable
- Preserve original creation dates, update revision dates
- Follow the established "Related Functions" format

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact & Support

**Questions or Issues?**
- Create an issue in the GitHub repository
- Follow the project for updates
- Share with other spreadsheet enthusiasts!

---

*Last Updated: August 17, 2025 | 539 Functions Documented & Standardized*

## 🆕 Recent Improvements (August 17, 2025)

### ✅ Complete YAML Standardization
- **539 Functions** processed with consistent frontmatter
- **Field Migration** from old formats to new structure  
- **Date Preservation** of original creation dates
- **Topic Mapping** based on folder structure
- **Platform Updates** from "google-specific" → "sheets", "excel-specific" → "excel"

### 🗂️ Repository Optimization
- **Clean .gitignore** includes only Functions/ and Diagrams/ directories
- **Removed** all Python scripts and temporary files from repository
- **Preserved** all unique function documentation
- **Organized** by logical function categories

### 🧠 Obsidian Integration
- **Double-bracketed Links** for powerful cross-referencing
- **Consistent Structure** perfect for graph view visualization  
- **Smart Tagging** system ready for advanced workflows
- **Template Format** for adding new functions
