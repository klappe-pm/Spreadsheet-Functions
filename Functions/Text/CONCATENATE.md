---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: text
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# CONCATENATE

## CONCATENATE Description

Joins multiple text strings, numbers, or cell references into a single text string. Essential for building dynamic text content, combining data fields, and creating formatted output strings in data processing workflows.

> [!f(x)] CONCATENATE Syntax
>
> ```spreadsheets
> CONCATENATE(text1, [text2], [text3], ...)
> ```
>
> **Parameters:**
> - `text1` (required): First text string, number, or cell reference to join
> - `text2, text3, ...` (optional): Additional text strings, numbers, or cell references (up to 255 arguments)

> [!f(x)] CONCATENATE Examples
>
> ```spreadsheets
> // Combine first and last name
> CONCATENATE("John", " ", "Smith") → "John Smith"
> 
> // Build formatted address
> CONCATENATE(A1, ", ", B1, " ", C1) → "123 Main St, City 12345"
> 
> // Create email address
> CONCATENATE("user", "@", "company.com") → "user@company.com"
> 
> // Format phone number
> CONCATENATE("(", "555", ") ", "123-4567") → "(555) 123-4567"
> 
> // Combine text with numbers
> CONCATENATE("Order #", 12345, " is ready") → "Order #12345 is ready"
> 
> // Build file path
> CONCATENATE("C:\Users\", "Name", "\Documents\file.txt") → "C:\Users\Name\Documents\file.txt"
> ```

## Use Cases

### [[Dynamic content generation]]
- **Email template building**: Combine personalized greetings, content sections, and signatures for automated email marketing campaigns
- **Report header creation**: Build dynamic report titles with dates, parameters, and contextual information for automated reporting systems
- **Form letter generation**: Merge template text with variable data for personalized communications and document automation
- **URL construction**: Combine base URLs with parameters and identifiers for dynamic web link generation and API calls

### [[Data formatting and display]]
- **Address formatting**: Combine address components with proper spacing and punctuation for mailing labels and shipping systems
- **Name standardization**: Join name components with consistent formatting for database storage and display purposes
- **Phone number formatting**: Build standardized phone number formats from component parts for consistent data presentation
- **Product description assembly**: Combine product attributes, specifications, and pricing information for catalog and e-commerce displays

### [[Data reconstruction and export]]
- **CSV field building**: Reconstruct delimited data formats for export and data transfer operations between systems
- **SQL statement construction**: Build dynamic SQL queries by combining static templates with variable parameters and conditions
- **File naming conventions**: Create standardized file names using date stamps, version numbers, and descriptive elements for document management
- **Configuration string assembly**: Combine configuration parameters and settings into formatted strings for system integration and setup**

## Related

### Similar Functions

- [[TEXTJOIN]] - Advanced text joining with delimiter control and empty value handling, modern alternative to CONCATENATE
- [[CONCAT]] - Simplified concatenation function, can join ranges and arrays more efficiently than CONCATENATE
- [[JOIN]] - Joins array elements with specified delimiter, useful for combining multiple values from ranges
- [[LEFT]] - Extracts text portions often combined with CONCATENATE for text reconstruction
- [[TEXT]] - Formats numbers and dates, frequently used with CONCATENATE for formatted output strings

## Text Processing Functions

### [[TEXT]]
Essential partnership for formatting numbers and dates before concatenation. TEXT ensures proper formatting of numeric values when building composite strings for display and export.

```spreadsheets
// Format currency in concatenated string
=CONCATENATE("Total: ", TEXT(A1, "$#,##0.00"))
// Example: "Total: $1,234.56"

// Include formatted date in message
=CONCATENATE("Report for ", TEXT(B1, "mmmm dd, yyyy"))
// Example: "Report for March 15, 2024"

// Format percentage with text
=CONCATENATE("Growth rate: ", TEXT(C1, "0.0%"), " this quarter")
// Example: "Growth rate: 12.5% this quarter"
```

### [[IF]]
Critical for conditional concatenation and dynamic content building. IF enables CONCATENATE to build different text strings based on conditions and handle missing or invalid data gracefully.

```spreadsheets
// Conditional greeting based on time
=CONCATENATE(IF(HOUR(NOW())<12, "Good Morning", "Good Afternoon"), ", ", A1)
// Creates time-appropriate greeting with name

// Include middle initial only if present
=CONCATENATE(B1, " ", IF(C1<>"", C1&". ", ""), D1)
// Example: "John M. Smith" or "John Smith"

// Build address with optional apartment number
=CONCATENATE(E1, " ", F1, IF(G1<>"", ", Apt "&G1, ""))
// Example: "123 Main St" or "123 Main St, Apt 4B"
```

## String Building Functions

### [[LEFT]]
Works with CONCATENATE to rebuild formatted strings after text extraction and parsing. Together they enable sophisticated text restructuring and standardization operations.

```spreadsheets
// Reformat phone number using LEFT extraction
=CONCATENATE("(", LEFT(A1, 3), ") ", MID(A1, 4, 3), "-", RIGHT(A1, 4))
// Example: "5551234567" → "(555) 123-4567"

// Build initials from name components
=CONCATENATE(LEFT(B1, 1), ".", LEFT(C1, 1), ".")
// Example: "John Smith" → "J.S."

// Create abbreviated display name
=CONCATENATE(LEFT(D1, 1), ". ", E1)
// Example: "John Smith" → "J. Smith"
```

### [[SUBSTITUTE]]
Combines with CONCATENATE for text cleaning and reconstruction workflows. SUBSTITUTE prepares text components while CONCATENATE assembles the final formatted result.

```spreadsheets
// Clean and rebuild phone number
=CONCATENATE("(", MID(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), 1, 3), ") ", MID(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), 4, 3), "-", MID(SUBSTITUTE(SUBSTITUTE(A1, "(", ""), ")", ""), 7, 4))
// Standardizes various phone formats

// Build clean email from components
=CONCATENATE(SUBSTITUTE(B1, " ", ""), "@", SUBSTITUTE(C1, " ", ""), ".com")
// Creates email while removing spaces

// Reconstruct data after character replacement
=CONCATENATE(SUBSTITUTE(D1, "_", " "), " - ", SUBSTITUTE(E1, "_", " "))
// Replaces underscores with spaces in combined output
```

## Commonly Used With Functions Examples

### Customer Contact Information System
```spreadsheets
// Build complete customer contact card from separate fields
// A1=FirstName, B1=LastName, C1=Title, D1=Company, E1=Phone, F1=Email

// Full name with title
=CONCATENATE(C1, " ", A1, " ", B1)
// Result: "Dr. John Smith"

// Business card format
=CONCATENATE(A1, " ", B1, CHAR(10), C1, CHAR(10), D1, CHAR(10), E1, CHAR(10), F1)
// Result: Multi-line business card format

// Email signature line
=CONCATENATE(A1, " ", B1, " | ", C1, " | ", D1, " | ", E1)
// Result: "John Smith | Manager | ABC Corp | (555) 123-4567"

// Formal letter greeting
=CONCATENATE("Dear ", IF(C1<>"", C1&" ", ""), B1, ",")
// Result: "Dear Dr. Smith," or "Dear Smith," if no title
```

### E-commerce Product Display System
```spreadsheets
// Build product descriptions from attributes
// G1=Brand, H1=Model, I1=Size, J1=Color, K1=Price, L1=SKU

// Product title
=CONCATENATE(G1, " ", H1, " - ", I1, " ", J1)
// Result: "Nike Air Max - Large Blue"

// Price display with currency
=CONCATENATE("$", TEXT(K1, "#,##0.00"), " USD")
// Result: "$129.99 USD"

// Product summary line
=CONCATENATE(G1, " ", H1, " (", L1, ") - ", I1, "/", J1, " - $", K1)
// Result: "Nike Air Max (SKU123) - Large/Blue - $129.99"

// Inventory status message
=CONCATENATE("Product: ", G1, " ", H1, " | Stock: ", IF(M1>0, M1&" available", "Out of stock"))
// Result: "Product: Nike Air Max | Stock: 15 available"
```

### Report Generation System
```spreadsheets
// Generate dynamic report headers and summaries
// N1=ReportType, O1=StartDate, P1=EndDate, Q1=TotalRecords, R1=Department

// Report title with date range
=CONCATENATE(N1, " Report: ", TEXT(O1, "mm/dd/yyyy"), " - ", TEXT(P1, "mm/dd/yyyy"))
// Result: "Sales Report: 03/01/2024 - 03/31/2024"

// Summary statistics line
=CONCATENATE("Department: ", R1, " | Total Records: ", TEXT(Q1, "#,##0"), " | Period: ", TEXT(P1-O1, "0"), " days")
// Result: "Department: Sales | Total Records: 1,234 | Period: 31 days"

// File naming convention
=CONCATENATE(R1, "_", N1, "_", TEXT(O1, "yyyymmdd"), "_", TEXT(P1, "yyyymmdd"), ".xlsx")
// Result: "Sales_Report_20240301_20240331.xlsx"

// Executive summary opening
=CONCATENATE("This ", LOWER(N1), " report covers the period from ", TEXT(O1, "mmmm d, yyyy"), " to ", TEXT(P1, "mmmm d, yyyy"), " and includes ", TEXT(Q1, "#,##0"), " records from the ", R1, " department.")
// Result: Complete executive summary paragraph
```

### Database Query Construction
```spreadsheets
// Build dynamic SQL queries from parameters
// S1=Table, T1=Field, U1=Operator, V1=Value, W1=OrderBy

// SELECT statement construction
=CONCATENATE("SELECT * FROM ", S1, " WHERE ", T1, " ", U1, " '", V1, "'")
// Result: "SELECT * FROM customers WHERE name = 'Smith'"

// UPDATE statement with conditions
=CONCATENATE("UPDATE ", S1, " SET ", T1, " = '", V1, "' WHERE id = ", X1)
// Result: "UPDATE customers SET status = 'active' WHERE id = 123"

// Complex WHERE clause building
=CONCATENATE("SELECT * FROM ", S1, " WHERE ", T1, " ", U1, " '", V1, "' ORDER BY ", W1)
// Result: "SELECT * FROM customers WHERE name = 'Smith' ORDER BY date"

// INSERT statement construction
=CONCATENATE("INSERT INTO ", S1, " (", T1, ", ", Y1, ") VALUES ('", V1, "', '", Z1, "')")
// Result: "INSERT INTO customers (name, email) VALUES ('John Smith', 'john@email.com')"
```

### Configuration File Generation
```spreadsheets
// Generate configuration strings for system setup
// AA1=ServerName, BB1=Port, CC1=Database, DD1=Username, EE1=Timeout

// Database connection string
=CONCATENATE("Server=", AA1, ";Port=", BB1, ";Database=", CC1, ";UID=", DD1, ";Timeout=", EE1, ";")
// Result: "Server=localhost;Port=3306;Database=mydb;UID=admin;Timeout=30;"

// Application configuration line
=CONCATENATE("[", FF1, "]", CHAR(10), "server=", AA1, CHAR(10), "port=", BB1, CHAR(10), "database=", CC1)
// Result: Multi-line INI format configuration

// JSON configuration string
=CONCATENATE("{""server"":""", AA1, """,""port"":", BB1, ",""database"":""", CC1, """,""timeout"":", EE1, "}")
// Result: Valid JSON configuration object

// Environment variable format
=CONCATENATE("DB_HOST=", AA1, " DB_PORT=", BB1, " DB_NAME=", CC1, " DB_USER=", DD1)
// Result: "DB_HOST=localhost DB_PORT=3306 DB_NAME=mydb DB_USER=admin"
```
