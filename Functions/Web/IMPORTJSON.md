---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - web
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
# IMPORTJSON

## IMPORTJSON Description

Imports JSON data from a URL and converts it into a structured format for use in spreadsheet calculations. This powerful function enables real-time data integration from web APIs, making it essential for dynamic reporting and automated data workflows.

> [!f(x)] IMPORTJSON Syntax
>
> ```spreadsheets
> IMPORTJSON(url, [query], [parseHeaders], [includeXPath], [mutateType])
> ```
>
> **Parameters:**
> - `url` (required): The URL containing the JSON data to import
> - `query` (optional): JSONPath query string to extract specific data elements
> - `parseHeaders` (optional): TRUE to parse headers from first row, FALSE otherwise (default: TRUE)
> - `includeXPath` (optional): TRUE to include XPath information, FALSE otherwise (default: FALSE)
> - `mutateType` (optional): Data type conversion - "auto", "string", "number" (default: "auto")

> [!f(x)] IMPORTJSON Examples
>
> ```spreadsheets
> // Basic JSON import from API
> IMPORTJSON("https://api.example.com/users") → imports entire user dataset
> 
> // Import with JSONPath query
> IMPORTJSON("https://api.weather.com/data", "$.weather[*].temp") → extracts only temperature values
> 
> // Import without header parsing
> IMPORTJSON("https://api.stocks.com/prices", "", FALSE) → raw data without headers
> 
> // Cryptocurrency prices with specific query
> IMPORTJSON("https://api.coinbase.com/v2/exchange-rates", "$.data.rates.USD") → USD exchange rate
> 
> // Social media metrics import
> IMPORTJSON("https://api.social.com/stats/12345", "$.engagement[*]") → user engagement data
> ```

## Use Cases

### [[Real-time data integration]]
- **Financial market tracking**: Import live stock prices, cryptocurrency rates, and market indicators for investment portfolio monitoring and automated trading decisions
- **Weather-based logistics**: Pull current weather data to optimize shipping routes, adjust delivery schedules, and manage supply chain disruptions
- **Social media monitoring**: Track brand mentions, engagement metrics, and trending hashtags for marketing campaign optimization and reputation management
- **E-commerce pricing**: Monitor competitor pricing across multiple platforms to implement dynamic pricing strategies and maintain market competitiveness

### [[API data consumption]]
- **Customer relationship management**: Sync customer data from CRM APIs to create comprehensive client profiles and automated follow-up workflows
- **Inventory management**: Connect with supplier APIs to track stock levels, automate reordering, and predict demand patterns
- **Project management integration**: Import task status, team productivity metrics, and project timelines from project management tools for unified reporting
- **Payment processing analytics**: Retrieve transaction data, fraud alerts, and payment success rates from payment gateway APIs for financial analysis

### [[Automated reporting]]
- **Business intelligence dashboards**: Create dynamic reports combining data from multiple APIs, updating automatically without manual intervention
- **Performance monitoring**: Track website analytics, server metrics, and application performance indicators in real-time spreadsheet dashboards
- **Compliance reporting**: Automatically gather data from various systems to generate regulatory reports, audit trails, and compliance documentation
- **Sales performance tracking**: Combine data from CRM, advertising platforms, and analytics tools to create comprehensive sales funnel analysis

## Related

### Similar Functions

- [[WEBSERVICE]] - Imports data from web services but returns raw text/XML rather than parsed JSON structures
- [[IMPORTXML]] - Extracts data from XML/HTML documents using XPath queries, complementing JSON data import capabilities
- [[IMPORTDATA]] - Imports CSV and TSV data from URLs, useful for structured text data rather than JSON formats
- [[IMPORTHTML]] - Extracts tables and lists from HTML pages, providing alternative to JSON APIs for web data
- [[IMPORTRANGE]] - Imports data from other Google Sheets, enabling cross-sheet JSON data consolidation and analysis

## Data Processing Functions

### [[QUERY]]
Combined with IMPORTJSON to filter, sort, and aggregate imported JSON data using SQL-like syntax. QUERY provides powerful data manipulation capabilities after JSON import, enabling complex analysis workflows.

```spreadsheets
// Filter imported user data by status
=QUERY(IMPORTJSON("https://api.users.com/all"), "SELECT * WHERE status = 'active'")
// Returns only active users from JSON dataset

// Aggregate sales data by region
=QUERY(IMPORTJSON("https://api.sales.com/data"), "SELECT region, SUM(amount) GROUP BY region")
// Summarizes JSON sales data by geographical regions

// Sort and limit API results
=QUERY(IMPORTJSON("https://api.products.com/catalog"), "SELECT name, price ORDER BY price DESC LIMIT 10")
// Shows top 10 most expensive products from JSON catalog
```

### [[FILTER]]
Works with IMPORTJSON to create dynamic filtered views of JSON data based on multiple conditions. FILTER enables real-time data segmentation and conditional analysis of imported datasets.

```spreadsheets
// Filter products above price threshold
=FILTER(IMPORTJSON("https://api.store.com/products"), IMPORTJSON("https://api.store.com/products", "$.price") > 100)
// Shows only products priced over $100

// Filter recent transactions
=FILTER(IMPORTJSON("https://api.payments.com/transactions"), IMPORTJSON("https://api.payments.com/transactions", "$.date") > TODAY()-30)
// Returns transactions from last 30 days

// Multi-condition filtering
=FILTER(IMPORTJSON("https://api.employees.com/staff"), (IMPORTJSON("https://api.employees.com/staff", "$.department") = "Sales") * (IMPORTJSON("https://api.employees.com/staff", "$.performance") >= 80))
// Shows high-performing sales employees
```

## Array Processing Functions

### [[ARRAYFORMULA]]
Essential for processing IMPORTJSON arrays efficiently, enabling bulk operations across imported datasets. ARRAYFORMULA eliminates the need for manual array expansion and improves calculation performance.

```spreadsheets
// Calculate totals across imported array
=ARRAYFORMULA(SUM(IMPORTJSON("https://api.finance.com/expenses", "$.amounts[*]")))
// Sums all expense amounts from JSON array

// Transform imported data with calculations
=ARRAYFORMULA(IMPORTJSON("https://api.sales.com/data", "$.revenue[*]") * 1.1)
// Applies 10% markup to all revenue values

// Conditional array processing
=ARRAYFORMULA(IF(IMPORTJSON("https://api.inventory.com/stock", "$.quantity[*]") < 10, "Reorder", "Sufficient"))
// Flags low-stock items from inventory JSON
```

### [[TRANSPOSE]]
Converts IMPORTJSON row data to column format or vice versa, essential for data structure optimization and dashboard layout requirements.

```spreadsheets
// Convert horizontal JSON data to vertical layout
=TRANSPOSE(IMPORTJSON("https://api.metrics.com/daily"))
// Transforms daily metrics from rows to columns

// Restructure time series data
=TRANSPOSE(IMPORTJSON("https://api.analytics.com/trends", "$.data[*]"))
// Converts trend data for time-series analysis

// Optimize dashboard layout
=TRANSPOSE(IMPORTJSON("https://api.summary.com/kpis"))
// Reshapes KPI data for dashboard presentation
```

## Error Handling Functions

### [[IFERROR]]
Critical for robust IMPORTJSON implementations, handling network failures, API errors, and malformed JSON gracefully. IFERROR ensures spreadsheet functionality continues despite data import issues.

```spreadsheets
// Handle API unavailability
=IFERROR(IMPORTJSON("https://api.service.com/data"), "Service temporarily unavailable")
// Shows friendly message when API fails

// Fallback to cached data
=IFERROR(IMPORTJSON("https://api.live.com/feed"), IMPORTJSON("https://api.cache.com/backup"))
// Uses backup data source when primary fails

// Progressive error handling
=IFERROR(IMPORTJSON("https://api.primary.com/data"), IFERROR(IMPORTJSON("https://api.secondary.com/data"), "All services down"))
// Tries multiple data sources with final fallback message
```

### [[ISBLANK]]
Used with IMPORTJSON to validate data completeness and handle missing values in imported datasets. ISBLANK helps identify gaps in API responses and trigger appropriate actions.

```spreadsheets
// Validate required data fields
=IF(ISBLANK(IMPORTJSON("https://api.required.com/data", "$.critical_field")), "Missing critical data", "Data complete")
// Checks for essential data presence

// Count missing values in dataset
=SUMPRODUCT(--(ISBLANK(IMPORTJSON("https://api.survey.com/responses", "$.answers[*]"))))
// Counts blank responses in survey data

// Conditional data processing
=IF(ISBLANK(IMPORTJSON("https://api.optional.com/extra")), IMPORTJSON("https://api.main.com/core"), IMPORTJSON("https://api.main.com/core") & IMPORTJSON("https://api.optional.com/extra"))
// Combines core data with optional supplements when available
```

## Text Processing Functions

### [[REGEXEXTRACT]]
Complements IMPORTJSON by parsing specific patterns from imported text fields, enabling advanced data extraction from JSON string values.

```spreadsheets
// Extract phone numbers from JSON contact data
=REGEXEXTRACT(IMPORTJSON("https://api.contacts.com/person/123", "$.notes"), "\d{3}-\d{3}-\d{4}")
// Finds phone number patterns in contact notes

// Parse email domains from user data
=REGEXEXTRACT(IMPORTJSON("https://api.users.com/profile", "$.email"), "@(.+)")
// Extracts domain portion from email addresses

// Extract product codes from descriptions
=REGEXEXTRACT(IMPORTJSON("https://api.catalog.com/items", "$.description"), "SKU:([A-Z0-9]+)")
// Finds SKU codes in product descriptions
```

### [[CONCATENATE]]
Combines IMPORTJSON results with other data sources and formatting elements to create comprehensive data views and formatted outputs.

```spreadsheets
// Create formatted status messages
=CONCATENATE("Current temperature: ", IMPORTJSON("https://api.weather.com/now", "$.temp"), "°F at ", IMPORTJSON("https://api.weather.com/now", "$.location"))
// Formats weather data into readable sentence

// Combine multiple API endpoints
=CONCATENATE("User: ", IMPORTJSON("https://api.users.com/123", "$.name"), " | Balance: $", IMPORTJSON("https://api.accounts.com/123", "$.balance"))
// Merges user and account information

// Build dynamic URLs for further API calls
=CONCATENATE("https://api.details.com/user/", IMPORTJSON("https://api.users.com/current", "$.id"), "/profile")
// Creates personalized API endpoints based on current user
```

## Commonly Used With Functions Examples

### Live Dashboard Creation
```spreadsheets
// Multi-source dashboard combining sales, inventory, and weather
=IF(IFERROR(IMPORTJSON("https://api.sales.com/today"),"Error")="Error", "Sales API Down", 
   CONCATENATE("Sales: $", IMPORTJSON("https://api.sales.com/today", "$.total"), 
   " | Stock: ", SUMPRODUCT(IMPORTJSON("https://api.inventory.com/levels", "$.quantities[*]")),
   " | Weather: ", IMPORTJSON("https://api.weather.com/local", "$.condition")))
// Creates comprehensive business dashboard with error handling
```

### Automated Price Monitoring
```spreadsheets
// Competitor price tracking with alerts
=ARRAYFORMULA(IF(IMPORTJSON("https://api.competitors.com/prices", "$.products[*].price") > 
   IMPORTJSON("https://api.ourstore.com/prices", "$.products[*].price") * 0.95,
   CONCATENATE("UNDERPRICED: ", IMPORTJSON("https://api.competitors.com/prices", "$.products[*].name")),
   "Price OK"))
// Flags products priced significantly below competition
```

### Real-time Inventory Management
```spreadsheets
// Stock level monitoring with reorder triggers
=QUERY(FILTER(IMPORTJSON("https://api.warehouse.com/inventory"),
   IMPORTJSON("https://api.warehouse.com/inventory", "$.stock_level[*]") < 
   IMPORTJSON("https://api.warehouse.com/inventory", "$.reorder_point[*]")),
   "SELECT product_name, stock_level, supplier ORDER BY priority DESC")
// Identifies products needing reorder, sorted by priority
```

### Dynamic Financial Reporting
```spreadsheets
// Portfolio performance with multiple data sources
=TRANSPOSE(ARRAYFORMULA(CONCATENATE(IMPORTJSON("https://api.portfolio.com/holdings", "$.symbols[*]"), ": $",
   IMPORTJSON("https://api.prices.com/current", "$.prices[*]") * 
   IMPORTJSON("https://api.portfolio.com/holdings", "$.quantities[*]"))))
// Shows current value of all portfolio holdings in readable format
```

### Automated Social Media Analytics
```spreadsheets
// Engagement tracking across platforms
=IFERROR(ARRAYFORMULA(REGEXEXTRACT(IMPORTJSON("https://api.social.com/posts", "$.content[*]"), "#(\w+)")),
   QUERY(IMPORTJSON("https://api.social.com/engagement"), 
   "SELECT hashtag, SUM(likes), SUM(shares) GROUP BY hashtag ORDER BY SUM(likes) DESC LIMIT 5"))
// Extracts trending hashtags or shows top engagement metrics as fallback
```
