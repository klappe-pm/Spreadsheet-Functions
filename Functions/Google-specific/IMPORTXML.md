---
categories: spreadsheets
subCategories: 
  - sheets
topics: google-specific
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# IMPORTXML

## IMPORTXML Description

Imports structured data from XML, HTML, CSV, TSV, or RSS feeds using XPath queries to target specific elements. More flexible and precise than IMPORTHTML, enabling extraction of specific data points from complex web pages and XML documents that don't follow standard table structures.

> [!f(x)] IMPORTXML Syntax
>
> ```spreadsheets
> IMPORTXML(url, xpath_query)
> ```
>
> **Parameters:**
> - `url` (required): URL of the web page, XML document, CSV, TSV, or RSS feed to import from
> - `xpath_query` (required): XPath expression that specifies which elements to extract from the document

> [!f(x)] IMPORTXML Examples
>
> ```spreadsheets
> // Extract specific text content
> IMPORTXML("https://example.com", "//span[@class='price']") → extracts all elements with class 'price'
> 
> // Get all links from a page
> IMPORTXML("https://site.com", "//a/@href") → extracts all href attributes from anchor tags
> 
> // Extract table data with specific criteria
> IMPORTXML("https://data-site.com", "//table[@id='results']//td") → gets all table cells from results table
> 
> // RSS feed parsing
> IMPORTXML("https://blog.com/feed.xml", "//item/title") → extracts all article titles from RSS feed
> 
> // Complex nested data extraction
> IMPORTXML("https://api-site.com", "//div[@class='product']//span[@class='name']") → gets product names from nested structure
> ```

## Use Cases

### [[Advanced web scraping]]
- **Precise data extraction**: Target specific elements when IMPORTHTML can't find the right table or data structure
- **Dynamic content parsing**: Extract data from JavaScript-rendered pages and complex HTML structures
- **API data import**: Parse XML and JSON responses from web APIs and data services
- **Custom data filtering**: Use XPath expressions to filter and transform data during import process

### [[RSS and XML processing]]  
- **News aggregation**: Import article titles, descriptions, and URLs from RSS feeds for content monitoring
- **Blog monitoring**: Track new posts, comments, and updates from multiple blog feeds automatically
- **XML data integration**: Import structured data from XML APIs, configuration files, and data exports
- **Syndication management**: Aggregate content from multiple RSS sources into unified dashboards

### [[SEO and marketing analysis]]
- **Competitor monitoring**: Extract pricing, product information, and content from competitor websites
- **SERP analysis**: Monitor search engine results pages for keyword rankings and competitor positions
- **Social media metrics**: Extract engagement data, follower counts, and performance metrics from social platforms
- **Content analysis**: Analyze meta tags, headers, and content structure from multiple websites systematically

## Related

### Similar Functions

- [[IMPORTHTML]] - Simpler table and list import, use IMPORTXML when IMPORTHTML can't find the right data
- [[IMPORTDATA]] - Imports CSV/TSV files, IMPORTXML can also handle these with more control
- [[IMPORTFEED]] - Specialized RSS/Atom import, IMPORTXML offers more flexibility for feed parsing
- [[IMPORTRANGE]] - Imports from Google Sheets, IMPORTXML handles external web data
- [[QUERY]] - Filters imported data, often used with IMPORTXML results for further processing

## Web Scraping Functions

### [[IMPORTHTML]]
Use IMPORTXML when IMPORTHTML fails or when you need more precise data extraction. IMPORTXML provides XPath control where IMPORTHTML's table indexing falls short.

```spreadsheets
// When IMPORTHTML can't find tables
=IFERROR(IMPORTHTML("https://site.com","table",1), IMPORTXML("https://site.com","//table[1]//tr"))
// Fallback to IMPORTXML when IMPORTHTML fails

// More precise table targeting
=IMPORTXML("https://data-site.com", "//table[@class='financial-data']//tr[position()>1]")
// Targets specific table class and skips header row

// Extract data not in table format
=IMPORTXML("https://listings.com", "//div[@class='listing-item']//span[@class='price']")
// Gets prices when they're in divs, not tables
```

### [[IMPORTDATA]]  
IMPORTXML can handle CSV/TSV data with more control than IMPORTDATA, especially when you need to filter or transform during import.

```spreadsheets
// CSV parsing with filtering
=IMPORTXML("https://data.com/export.csv", "//tr[position()>1 and td[3]>100]")
// Imports CSV rows where third column > 100

// TSV with specific columns
=IMPORTXML("https://api.com/data.tsv", "//tr/td[position()=1 or position()=3]")
// Extracts only first and third columns from TSV

// Structured data with validation
=IMPORTXML("https://feeds.com/data.xml", "//record[status='active']/name")
// Imports only active records from XML data
```

## Text Processing Functions

### [[REGEXEXTRACT]]
Often used with IMPORTXML to clean and extract specific patterns from scraped text data, especially when XPath alone isn't sufficient.

```spreadsheets
// Clean imported data with regex
=REGEXEXTRACT(IMPORTXML("https://site.com", "//span[@class='code']"), "[A-Z]{3}-\d{4}")
// Extracts product codes matching specific pattern from scraped text

// Parse complex imported strings
=ARRAYFORMULA(REGEXEXTRACT(IMPORTXML("https://listings.com", "//div[@class='address']"), "(\d+\s+[A-Za-z\s]+)"))
// Extracts street addresses from complex location strings

// Extract numbers from mixed content
=VALUE(REGEXEXTRACT(IMPORTXML("https://prices.com", "//span[@class='price']"), "\d+\.?\d*"))
// Converts scraped price text to numeric values
```

### [[SPLIT]]
Combined with IMPORTXML to parse delimited data and separate combined information extracted from web pages.

```spreadsheets
// Split imported combined data
=ARRAYFORMULA(SPLIT(IMPORTXML("https://directory.com", "//div[@class='contact']"), " | "))
// Separates pipe-delimited contact information

// Parse structured imported text
=SPLIT(INDEX(IMPORTXML("https://events.com", "//div[@class='event-info']"),1), " - ")
// Splits event information with dash separator

// Multi-level data parsing
=TRANSPOSE(SPLIT(TRANSPOSE(IMPORTXML("https://data.com", "//record/fields")), ","))
// Converts comma-separated fields into columns
```

## Error Handling Functions

### [[IFERROR]]
Critical for IMPORTXML operations since XPath queries can fail due to page structure changes, network issues, or blocked access.

```spreadsheets
// Fallback XPath expressions
=IFERROR(IMPORTXML("https://site.com", "//div[@class='new-layout']//span"), 
         IMPORTXML("https://site.com", "//div[@class='old-layout']//span"))
// Tries new layout first, falls back to old layout

// Multiple extraction strategies
=IFERROR(IMPORTXML("https://prices.com", "//span[@class='price']"), 
         IFERROR(IMPORTXML("https://prices.com", "//div[@id='price']"), 
                "Price not available"))
// Multiple XPath attempts with final fallback message

// Network error handling
=IFERROR(IMPORTXML("https://external-api.com", "//data/value"), 
         "Service unavailable - "&TEXT(NOW(),"hh:mm"))
// Handles network failures with timestamp
```

### [[LEN]]
Used to validate IMPORTXML results and ensure data quality, especially important when scraping dynamic or unreliable sources.

```spreadsheets
// Data quality validation
=IF(LEN(IMPORTXML("https://site.com","//title"))>0, IMPORTXML("https://site.com","//title"), "No title found")
// Only shows title if successfully extracted

// Content completeness check
=ARRAYFORMULA(IF(LEN(IMPORTXML("https://listings.com","//div[@class='description']"))>50, 
                IMPORTXML("https://listings.com","//div[@class='description']"), 
                "Description too short"))
// Filters out descriptions that are too brief

// Import success monitoring
=IF(LEN(CONCATENATE(IMPORTXML("https://data.com","//record")))>0, "Success", "Failed")&" - "&COUNT(IMPORTXML("https://data.com","//record"))&" records"
// Reports import status with record count
```

## Data Processing Functions

### [[QUERY]]
Powerful combination with IMPORTXML for filtering, aggregating, and analyzing scraped data using SQL-like syntax.

```spreadsheets
// Filter imported XML data
=QUERY(IMPORTXML("https://products.com/api.xml","//product/name | //product/price"), "SELECT * WHERE Col2 > 100")
// Filters products by price after XML import

// Aggregate scraped data
=QUERY(TRANSPOSE(IMPORTXML("https://sales.com","//sale/amount")), "SELECT SUM(Col1), AVG(Col1), COUNT(Col1)")
// Statistical analysis of scraped sales data

// Complex data transformation
=QUERY(ARRAYFORMULA({IMPORTXML("https://site.com","//item/name"), IMPORTXML("https://site.com","//item/category")}), 
       "SELECT Col2, COUNT(Col1) GROUP BY Col2 ORDER BY COUNT(Col1) DESC")
// Groups scraped items by category with counts
```

### [[ARRAYFORMULA]]
Enables efficient processing of multiple IMPORTXML results and creates dynamic scraped data analysis systems.

```spreadsheets
// Multi-URL scraping
=ARRAYFORMULA(IF(A2:A10="","",IMPORTXML(A2:A10,"//title")))
// Scrapes titles from multiple URLs in column A

// Batch data processing
=ARRAYFORMULA(IF(IMPORTXML("https://site.com","//item/status")="active", 
                IMPORTXML("https://site.com","//item/name"), 
                ""))
// Processes scraped data conditionally

// Dynamic XPath construction
=ARRAYFORMULA(IMPORTXML("https://api.com", "//record[@id='"&B2:B20&"']/value"))
// Uses cell values to construct dynamic XPath queries
```

## Date and Time Functions

### [[TODAY]]
Used with IMPORTXML for time-sensitive scraping and creating dated archives of scraped content.

```spreadsheets
// Daily content archiving
=IMPORTXML("https://news-site.com", "//article[contains(@data-date,'"&TEXT(TODAY(),"yyyy-mm-dd")&"')]//title")
// Scrapes only today's articles

// Cache expiration management
=IF(TODAY()>B1, IMPORTXML("https://api.com","//data/updated"), C1)
// Refreshes scraped data based on cache expiration date

// Time-based content filtering
=IMPORTXML("https://events.com", "//event[@date>='"&TEXT(TODAY(),"yyyy-mm-dd")&"']/title")
// Scrapes only future events
```

## Commonly Used With Functions Examples

### Advanced E-commerce Price Monitoring
```spreadsheets
// Multi-site competitive pricing
=ARRAYFORMULA({
  IMPORTXML("https://competitor1.com/product/123", "//span[@class='price']"),
  IMPORTXML("https://competitor2.com/items/123", "//div[@id='price-display']"),
  IMPORTXML("https://competitor3.com/shop/123", "//p[@class='cost']//strong")
})
// Monitors prices across different site structures
```

### SEO Competitor Analysis
```spreadsheets
// Multi-site meta tag analysis
=QUERY(ARRAYFORMULA({
  IMPORTXML("https://competitor1.com", "//title"),
  IMPORTXML("https://competitor1.com", "//meta[@name='description']/@content"),
  LEN(IMPORTXML("https://competitor1.com", "//title")),
  LEN(IMPORTXML("https://competitor1.com", "//meta[@name='description']/@content"))
}), "SELECT Col1, Col2, Col3, Col4 WHERE Col1 IS NOT NULL")
// Analyzes title and description length across competitors
```

### RSS Feed Content Aggregation
```spreadsheets
// Multi-source news aggregation
=QUERY({
  ARRAYFORMULA({IMPORTXML("https://techcrunch.com/feed", "//item/title"), "TechCrunch"});
  ARRAYFORMULA({IMPORTXML("https://venturebeat.com/feed", "//item/title"), "VentureBeat"});
  ARRAYFORMULA({IMPORTXML("https://mashable.com/feeds/all", "//item/title"), "Mashable"})
}, "SELECT Col1, Col2 WHERE Col1 CONTAINS 'AI' OR Col1 CONTAINS 'artificial intelligence' ORDER BY Col2")
// Aggregates AI-related headlines from multiple tech blogs
```

### Social Media Monitoring
```spreadsheets
// Multi-platform engagement tracking
=ARRAYFORMULA(IF(
  ISNUMBER(VALUE(REGEXEXTRACT(IMPORTXML("https://social-platform.com/user/profile", "//span[@class='follower-count']"), "\d+"))),
  VALUE(REGEXEXTRACT(IMPORTXML("https://social-platform.com/user/profile", "//span[@class='follower-count']"), "\d+")),
  "Error extracting count"
))
// Extracts and validates follower counts from social media profiles
```

### API Data Integration
```spreadsheets
// XML API data processing with error handling
=IFERROR(
  QUERY(TRANSPOSE(ARRAYFORMULA({
    IMPORTXML("https://api.company.com/data.xml", "//record/id"),
    IMPORTXML("https://api.company.com/data.xml", "//record/name"),
    IMPORTXML("https://api.company.com/data.xml", "//record/value"),
    IMPORTXML("https://api.company.com/data.xml", "//record/@status")
  })), "SELECT * WHERE Col4 = 'active' ORDER BY Col3 DESC"),
  "API currently unavailable"
)
// Comprehensive XML API integration with filtering and error handling
```
