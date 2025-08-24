---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - sheets
  - - topics
    - - google-specific
  - - subTopics
    - []
  - - dateCreated
    - 2025-08-17
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# IMPORTHTML

## IMPORTHTML Description

Imports data from HTML tables or lists on web pages directly into Google Sheets. Automatically parses structured web content and converts it to spreadsheet format, enabling real-time data feeds from websites without manual copying or web scraping tools.

> [!f(x)] IMPORTHTML Syntax
>
> ```spreadsheets
> IMPORTHTML(url, query, index)
> ```
>
> **Parameters:**
> - `url` (required): URL of the web page containing the HTML table or list
> - `query` (required): Either "table" to import HTML tables or "list" to import HTML lists (ul, ol)
> - `index` (required): Numeric index (starting from 1) of the table or list on the page to import

> [!f(x)] IMPORTHTML Examples
>
> ```spreadsheets
> // Import first table from webpage
> IMPORTHTML("https://example.com/data.html", "table", 1) → imports the first table found on the page
> 
> // Import specific list from webpage
> IMPORTHTML("https://site.com/lists.html", "list", 2) → imports the second list (ul/ol) from the page
> 
> // Import stock market data
> IMPORTHTML("https://finance.yahoo.com/quote/AAPL", "table", 1) → imports Apple stock data table
> 
> // Import sports statistics
> IMPORTHTML("https://sports-site.com/standings", "table", 3) → imports the third table containing team standings
> 
> // Import product pricing
> IMPORTHTML("https://retailer.com/products", "table", 2) → imports product comparison table
> ```

## Use Cases

### [[Web data integration]]
- **Financial market data**: Import real-time stock prices, currency rates, and market indices from financial websites automatically
- **Sports statistics**: Pull live scores, player stats, and league standings from sports websites for analysis and reporting
- **E-commerce pricing**: Monitor competitor pricing, product availability, and market trends from retail websites
- **News and media monitoring**: Track article metrics, social media stats, and trending topics from news aggregation sites

### [[Research and analysis]]  
- **Academic research**: Import research data, publication lists, and citation metrics from academic databases and journals
- **Market research**: Gather competitive intelligence, industry benchmarks, and market trends from various business websites
- **Government data**: Access public datasets, economic indicators, and regulatory information from government websites
- **Social media analytics**: Pull engagement metrics, follower counts, and trending hashtags from social platforms

### [[Automated reporting]]
- **Daily dashboards**: Create automatically updating dashboards that pull fresh data from multiple web sources hourly
- **Inventory monitoring**: Track product availability and pricing changes across multiple vendor websites
- **Performance tracking**: Monitor website analytics, SEO metrics, and conversion rates from various tools and platforms
- **Compliance reporting**: Automatically collect regulatory data, filing statuses, and compliance metrics from official websites

## Related

### Similar Functions

- [[IMPORTXML]] - More flexible XML/HTML importing using XPath queries for complex data extraction
- [[IMPORTDATA]] - Imports CSV or TSV data from URLs, simpler than IMPORTHTML for structured text files
- [[IMPORTRANGE]] - Imports data from other Google Sheets, used for internal data consolidation
- [[IMPORTFEED]] - Imports RSS and ATOM feeds, specialized for news and blog content
- [[WEBSERVICE]] - Calls web services and APIs, more advanced than IMPORTHTML for dynamic data

## Web Scraping Functions

### [[IMPORTXML]]
More powerful and flexible than IMPORTHTML for complex web scraping. Use IMPORTXML when IMPORTHTML can't locate the right table or when you need specific elements from web pages.

```spreadsheets
// When IMPORTHTML fails, use IMPORTXML with XPath
=IMPORTXML("https://example.com", "//table[@class='data-table']//tr")
// Targets specific table by CSS class when IMPORTHTML index method insufficient

// Extract specific data elements
=IMPORTXML("https://stock-site.com", "//span[@class='price']")
// Gets stock prices when they're not in tables but in span elements

// Combine with IMPORTHTML for validation
=IF(ISERROR(IMPORTHTML("https://site.com","table",1)), 
    IMPORTXML("https://site.com","//table[1]//tr"), 
    IMPORTHTML("https://site.com","table",1))
// Fallback strategy when IMPORTHTML fails
```

### [[IMPORTDATA]]  
Complementary to IMPORTHTML for CSV/TSV web data. Use when websites provide CSV exports or when IMPORTHTML can't parse complex table structures.

```spreadsheets
// CSV data import from web APIs
=IMPORTDATA("https://api.example.com/data.csv")
// Imports CSV data that IMPORTHTML cannot parse

// Structured data feeds
=IMPORTDATA("https://finance-site.com/export.tsv") 
// TSV financial data that's more reliable than HTML table scraping

// Government data feeds
=IMPORTDATA("https://government.gov/opendata/file.csv")
// Official data sources often provide CSV for better reliability
```

## Data Processing Functions

### [[QUERY]]
Essential companion to IMPORTHTML for filtering and processing imported web data. Transforms raw HTML table data into actionable insights and reports.

```spreadsheets
// Filter imported web data
=QUERY(IMPORTHTML("https://example.com/data", "table", 1), "SELECT Col1, Col3 WHERE Col2 > 100")
// Imports table and immediately filters for relevant data

// Aggregate web-sourced data
=QUERY(IMPORTHTML("https://sales-site.com/data", "table", 2), "SELECT Col1, SUM(Col4) GROUP BY Col1 ORDER BY SUM(Col4) DESC")
// Imports and creates summary from web data

// Date-filtered web imports  
=QUERY(IMPORTHTML("https://news-site.com/articles", "table", 1), "SELECT * WHERE Col3 >= date '"&TEXT(TODAY()-7,"yyyy-mm-dd")&"'")
// Gets web data for last 7 days only
```

### [[ARRAYFORMULA]]
Enables dynamic processing of IMPORTHTML results across multiple cells. Creates self-updating calculations that automatically adjust when web data changes.

```spreadsheets
// Dynamic calculations on imported data
=ARRAYFORMULA(IF(ROW(IMPORTHTML("https://site.com","table",1))>1, 
               INDEX(IMPORTHTML("https://site.com","table",1),0,2)*1.1, 
               INDEX(IMPORTHTML("https://site.com","table",1),0,2)))
// Adds 10% markup to all imported price data except header

// Multi-column web data processing
=ARRAYFORMULA(IMPORTHTML("https://converter.com","table",1) & " - Updated: " & TEXT(NOW(),"mm/dd hh:mm"))
// Adds timestamp to imported currency conversion data

// Conditional formatting of web imports
=ARRAYFORMULA(IF(IMPORTHTML("https://inventory.com","table",1)>0, "In Stock", "Out of Stock"))
// Converts numeric inventory to stock status
```

## Text Processing Functions

### [[SPLIT]]
Frequently used with IMPORTHTML when web tables contain combined data in single cells that need separation for analysis.

```spreadsheets
// Split combined web data
=ARRAYFORMULA(SPLIT(INDEX(IMPORTHTML("https://directory.com","table",1),0,2), " - "))
// Separates name-location data from directory website

// Parse addresses from imported tables
=SPLIT(INDEX(IMPORTHTML("https://listings.com","table",1),0,3), ",")
// Splits comma-separated address data into columns

// Extract product codes from descriptions
=ARRAYFORMULA(SPLIT(INDEX(IMPORTHTML("https://catalog.com","table",2),0,1), " | "))
// Separates product codes from combined description fields
```

### [[TRIM]]
Essential for cleaning imported web data which often contains extra spaces, tabs, and formatting artifacts from HTML parsing.

```spreadsheets
// Clean imported web data
=ARRAYFORMULA(TRIM(IMPORTHTML("https://messy-site.com","table",1)))
// Removes extra spaces from all imported table data

// Clean specific columns of web imports
=ARRAYFORMULA(IF(COLUMN(IMPORTHTML("https://site.com","table",1))<=3, 
               TRIM(IMPORTHTML("https://site.com","table",1)), 
               IMPORTHTML("https://site.com","table",1)))
// Trims only first three columns of imported data

// Standardize text from multiple web sources
=ARRAYFORMULA(UPPER(TRIM(IMPORTHTML("https://names-site.com","list",1))))
// Cleans and standardizes imported name list
```

## Error Handling Functions

### [[IFERROR]]
Critical for handling IMPORTHTML failures due to website changes, network issues, or blocked access. Provides graceful degradation and alternative data sources.

```spreadsheets
// Fallback data source
=IFERROR(IMPORTHTML("https://primary-source.com","table",1), 
         IMPORTHTML("https://backup-source.com","table",1))
// Uses backup website when primary source fails

// Cached data fallback
=IFERROR(IMPORTHTML("https://live-data.com","table",1), 
         BackupData!A1:Z100)
// Falls back to cached data when live import fails

// Error notification with retry
=IFERROR(IMPORTHTML("https://api-site.com","table",2), 
         "Data unavailable - Last updated: "&TEXT(NOW(),"mm/dd hh:mm"))
// Shows error message with timestamp when import fails
```

### [[ISERROR]]
Used for monitoring IMPORTHTML reliability and creating data quality dashboards that track import success rates.

```spreadsheets
// Import success monitoring
=IF(ISERROR(IMPORTHTML("https://data-source.com","table",1)), "FAILED", "SUCCESS")
// Monitors whether data import is working

// Data freshness validation
=IF(ISERROR(IMPORTHTML("https://real-time.com","table",1)), 
   "Check connection", 
   "Last updated: "&TEXT(NOW(),"hh:mm"))
// Shows import status and update time

// Multi-source reliability check
=SUMPRODUCT(--(ISERROR(IMPORTHTML(ImportSources,E2:E10,"table",1))))&" of "&COUNTA(E2:E10)&" sources failing"
// Counts how many import sources are currently failing
```

## Commonly Used With Functions Examples

### Real-Time Financial Dashboard
```spreadsheets
// Multi-asset portfolio tracker
=QUERY(IMPORTHTML("https://finance.yahoo.com/quote/AAPL","table",1), "SELECT Col1, Col2") & " | " &
 QUERY(IMPORTHTML("https://finance.yahoo.com/quote/GOOGL","table",1), "SELECT Col1, Col2") & " | " &
 QUERY(IMPORTHTML("https://finance.yahoo.com/quote/MSFT","table",1), "SELECT Col1, Col2")
// Combines multiple stock data sources into single dashboard row
```

### Competitive Intelligence System
```spreadsheets
// Multi-competitor price monitoring
=ARRAYFORMULA(
  IF(ROW(A1:A20)=1, {"Competitor","Product","Price","Date Checked"}, 
     IF(A1:A20<>"", 
        {A1:A20, 
         INDEX(IMPORTHTML("https://competitor1.com/products","table",1),MATCH(A1:A20,INDEX(IMPORTHTML("https://competitor1.com/products","table",1),0,1),0),2),
         INDEX(IMPORTHTML("https://competitor1.com/products","table",1),MATCH(A1:A20,INDEX(IMPORTHTML("https://competitor1.com/products","table",1),0,1),0),3),
         TEXT(NOW(),"mm/dd/yyyy hh:mm")}, 
        "")))
// Automated competitive pricing analysis with timestamps
```

### Market Research Automation
```spreadsheets
// Industry trend aggregation  
=QUERY({IMPORTHTML("https://site1.com/trends","table",1);
        IMPORTHTML("https://site2.com/data","table",2);
        IMPORTHTML("https://site3.com/reports","table",1)}, 
       "SELECT Col1, AVG(Col3), COUNT(Col2) WHERE Col1 IS NOT NULL GROUP BY Col1 ORDER BY AVG(Col3) DESC")
// Combines market data from multiple sources with statistical analysis
```

### Automated News Monitoring
```spreadsheets
// Breaking news aggregator with filtering
=QUERY(IMPORTHTML("https://news-site.com/breaking","list",1), 
       "SELECT * WHERE Col1 CONTAINS 'technology' OR Col1 CONTAINS 'finance' OR Col1 CONTAINS 'market'")&
 " | Source: News Site | Checked: "&TEXT(NOW(),"hh:mm")
// Filters breaking news for relevant business topics with metadata
```

### Government Data Integration
```spreadsheets
// Economic indicators dashboard
=ARRAYFORMULA(
  {IMPORTHTML("https://bls.gov/data/unemployment","table",1);
   IMPORTHTML("https://census.gov/retail/sales","table",2);
   IMPORTHTML("https://treasury.gov/interest-rates","table",1)})
// Consolidates multiple government economic data sources automatically
```
