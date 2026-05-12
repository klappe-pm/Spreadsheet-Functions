---
categories:
  - spreadsheet-functions
subCategories:
  - sheets
topics:
  - google-specific
  - data-import
  - web-feeds
subTopics:
  - rss-feeds
  - atom-feeds
  - syndication
  - news-aggregation
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - import rss
  - import atom
  - rss feed
  - news feed
  - feed reader
tags:
  - google-sheets
  - data-import
  - rss
  - atom
  - syndication
  - automation
  - news-monitoring
---

# IMPORTFEED

## Description

IMPORTFEED is a Google Sheets function that imports and parses RSS (Really Simple Syndication) and Atom web feeds, extracting structured information such as article titles, URLs, publication dates, authors, and content summaries directly into spreadsheet cells. RSS and Atom feeds are standardized XML formats used by websites to publish regularly updated content like blog posts, news articles, podcasts, video channels, and press releases, allowing subscribers to aggregate updates from multiple sources in one location. IMPORTFEED reads these feed URLs and converts the structured XML data into a tabular format suitable for spreadsheet analysis, eliminating the need for dedicated feed reader applications when building content monitoring systems, news dashboards, or research tools. This function bridges the gap between the world of web syndication and spreadsheet-based workflows, enabling powerful content aggregation and analysis capabilities within Google Sheets.

The primary use cases for IMPORTFEED center around media monitoring, content curation, competitive intelligence, and research aggregation. Marketing teams use it to monitor brand mentions across news sites and blogs, content creators track trending topics in their industry, PR professionals aggregate press coverage from multiple outlets, researchers monitor academic publications and preprints, and business analysts track competitor announcements and product releases. The function excels at creating centralized dashboards where updates from dozens or hundreds of sources appear in one view, sortable and filterable using Google Sheets' native capabilities. Combined with QUERY, conditional formatting, and Google Apps Script, IMPORTFEED enables sophisticated content monitoring systems that rival dedicated media monitoring platforms at a fraction of the cost.

There are significant limitations and gotchas to understand when using IMPORTFEED effectively. First, the function only works with valid RSS 2.0 or Atom feeds - it cannot parse arbitrary XML, JSON APIs, or HTML pages. Many modern websites have moved away from RSS or hide their feed URLs, requiring some detective work to locate them. Feeds must be publicly accessible without authentication; password-protected or login-required feeds cannot be imported. The function caches results similarly to other IMPORT functions, typically refreshing every one to two hours, so real-time news monitoring is not achievable. IMPORTFEED returns a maximum of approximately 250 items depending on feed size and Sheets' limits; older items in long feeds may be truncated. Some feeds contain minimal information (just titles and links) while others include full article text, publication dates, categories, and author information - the available data depends entirely on what the feed publisher includes. Finally, malformed feeds or feeds using non-standard extensions may produce errors or missing data.

From a platform perspective, IMPORTFEED is exclusive to Google Sheets with no direct equivalent in Microsoft Excel. Excel users historically relied on external RSS reader applications, Power Query with XML parsing, or third-party add-ins to consume RSS feeds. Power Query can technically parse RSS/Atom XML, but requires custom M code to properly interpret the feed structure, handle namespaces, and extract relevant fields - a complex task compared to IMPORTFEED's simple formula approach. Excel 365's WEBSERVICE function can fetch feed content as raw XML text, but parsing it into usable data requires extensive FILTERXML calls or VBA macros. For organizations using both platforms, RSS integration represents a significant workflow difference - what takes one formula in Sheets may require substantial development effort in Excel. Migration from Sheets to Excel requires completely rebuilding RSS functionality using Power Query, VBA, or external tools.

## Syntax

> [!NOTE] IMPORTFEED Syntax
> ```
> =IMPORTFEED(url, [query], [headers], [num_items])
> ```

| Parameter | Description | Required | Data Type |
|-----------|-------------|----------|-----------|
| `url` | The complete URL of the RSS or Atom feed to import. Must include the protocol (https:// or http://). The URL should point to a valid RSS 2.0 or Atom feed XML file. Can be entered as a literal string in quotes or as a reference to a cell containing the URL. The feed must be publicly accessible without authentication. | Yes | String (text) |
| `query` | Specifies what information to retrieve from the feed. Options are: "feed" (feed metadata like title and description), "feed title", "feed description", "feed author", "feed url", "items" (list of all items/articles), "items title", "items summary", "items url", "items created" (publication date). Default is "items" if omitted. | No | String (text) |
| `headers` | Whether to include a header row with column labels. TRUE includes headers, FALSE omits them. Default is FALSE if omitted. | No | Boolean |
| `num_items` | The number of feed items to return, starting from the most recent. If omitted, returns all available items (up to the feed's limit). Set to a specific number to limit results, useful for feeds with many items. | No | Number (integer) |

## Examples

### Example 1: Import All Items from an RSS Feed
```
=IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml")
```
**Result:** Returns a multi-column array with item titles, URLs, publication dates, and summaries from BBC News.

**Explanation:** This is the simplest form of IMPORTFEED - providing only the URL returns all available feed items with default columns. The function automatically detects whether the feed is RSS or Atom format. Results include Title, URL, Date Created, and Summary columns by default. This basic usage is ideal for quickly seeing what a feed contains before refining the query.

### Example 2: Import Feed Items with Headers
```
=IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml", "items", TRUE)
```
**Result:** Returns feed items with a header row labeling each column (Title, URL, Date Created, Summary).

**Explanation:** Adding TRUE as the third parameter includes column headers, making the data self-documenting and easier to understand. Headers are especially useful when sharing spreadsheets with others or when using QUERY to filter by column names. The "items" query parameter explicitly requests the item list, though this is also the default behavior.

### Example 3: Limit the Number of Returned Items
```
=IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml", "items", TRUE, 10)
```
**Result:** Returns only the 10 most recent feed items with headers.

**Explanation:** The fourth parameter limits results to a specific number of items. This is useful for feeds with many entries when you only care about recent content. It also reduces spreadsheet clutter and improves performance. For dashboards showing "latest news," limiting to 5-10 items keeps the display focused and manageable.

### Example 4: Extract Only Item Titles
```
=IMPORTFEED("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "items title")
```
**Result:** Returns a single column containing only the titles of feed items.

**Explanation:** Using "items title" as the query returns just article headlines without URLs, dates, or summaries. This focused query is useful when you only need titles for display or analysis. Similar queries include "items url", "items summary", and "items created" for other individual fields. Combine multiple focused queries to build custom column arrangements.

### Example 5: Get Item URLs Only
```
=IMPORTFEED("https://www.reddit.com/r/technology/.rss", "items url", TRUE, 20)
```
**Result:** Returns a single column with 20 URLs from the r/technology subreddit feed, with a header row.

**Explanation:** Extracting just URLs is useful for building link lists, programmatic access, or integration with other systems. Reddit provides RSS feeds for all subreddits at /r/subreddit/.rss. Note that some Reddit URLs may be nested (linking to Reddit discussions rather than original content). The TRUE parameter adds a header, and 20 limits the results.

### Example 6: Extract Feed Metadata
```
=IMPORTFEED("https://blog.google/rss/", "feed")
```
**Result:** Returns feed-level metadata including the feed title, description, and URL.

**Explanation:** The "feed" query returns information about the feed itself rather than individual items. This includes the feed title (e.g., "Google Blog"), description, author (if specified), and feed URL. Use this to create documentation of your data sources or to validate that you have the correct feed. "feed title", "feed description", "feed author", and "feed url" extract individual metadata fields.

### Example 7: Get Feed Title Only
```
=IMPORTFEED("https://techcrunch.com/feed/", "feed title")
```
**Result:** Returns a single cell containing "TechCrunch" (or the current feed title).

**Explanation:** "feed title" extracts just the publication name from the feed, useful for labeling sections of a multi-source dashboard. Create a sources list by combining multiple "feed title" queries: ={IMPORTFEED(A1,"feed title"); IMPORTFEED(A2,"feed title"); IMPORTFEED(A3,"feed title")} where column A contains feed URLs.

### Example 8: Import Item Publication Dates
```
=IMPORTFEED("https://www.wired.com/feed/rss", "items created", FALSE, 15)
```
**Result:** Returns the publication timestamps of the 15 most recent articles.

**Explanation:** "items created" extracts publication dates, enabling time-based analysis of content. Dates are typically returned in ISO 8601 format or similar. Use these with date functions: =DATEDIF(A2,TODAY(),"D") calculates days since publication. Filter recent content: =QUERY(IMPORTFEED(url,"items",TRUE),"WHERE Col3 > date '"&TEXT(TODAY()-7,"YYYY-MM-DD")&"'") shows only last week's items.

### Example 9: Using Cell Reference for Feed URL
```
=IMPORTFEED(A1, "items", TRUE, 10)
```
**Result:** Imports the 10 most recent items from whatever feed URL is stored in cell A1.

**Explanation:** Referencing a cell for the URL enables dynamic feed selection and easier maintenance. Build a feed management system where column A lists feed URLs, column B contains names, and column C controls item count. Use data validation dropdowns to let users select feeds. This pattern is essential for dashboards that monitor multiple sources.

### Example 10: Combine Multiple Feeds with Array Notation
```
={
  IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml", "items", TRUE, 5);
  QUERY(IMPORTFEED("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "items", FALSE, 5), "SELECT *")
}
```
**Result:** Stacks 5 items from BBC News (with headers) above 5 items from NY Times (without headers to avoid duplication).

**Explanation:** Array literals (curly braces with semicolons) stack multiple IMPORTFEED results vertically. Include headers only on the first feed to avoid repetition. This creates a unified view of multiple news sources. For many feeds, use a helper column with feed URLs and ARRAYFORMULA or multiple IMPORTFEED calls arranged vertically in separate cells.

### Example 11: Filter Feed Items with QUERY
```
=QUERY(IMPORTFEED("https://hnrss.org/frontpage", "items", TRUE, 50), "SELECT Col1, Col2 WHERE Col1 CONTAINS 'AI' OR Col1 CONTAINS 'machine learning'", 1)
```
**Result:** Returns titles and URLs of Hacker News frontpage items mentioning AI or machine learning.

**Explanation:** QUERY transforms IMPORTFEED results, enabling filtering by keywords, dates, or any criteria. In QUERY, columns from IMPORTFEED are Col1, Col2, Col3, Col4 (Title, URL, Created, Summary typically). The third parameter (1) indicates one header row. This pattern creates targeted content monitors that surface only relevant items from high-volume feeds.

### Example 12: Import Podcast Feed Information
```
=IMPORTFEED("https://feeds.simplecast.com/54nAGcIl", "items", TRUE, 10)
```
**Result:** Returns recent podcast episodes with titles, episode URLs, publication dates, and descriptions.

**Explanation:** Podcast feeds are standard RSS feeds with audio enclosures. IMPORTFEED extracts the textual metadata (episode title, description, date) but not the audio file URLs directly. For audio URLs, use IMPORTXML with an XPath query targeting the enclosure element. Podcast monitoring is useful for PR, competitive analysis, or creating listening queues.

### Example 13: Monitor YouTube Channel via RSS
```
=IMPORTFEED("https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID_HERE", "items", TRUE, 10)
```
**Result:** Returns recent video uploads from the specified YouTube channel.

**Explanation:** YouTube provides RSS feeds for channels at youtube.com/feeds/videos.xml?channel_id=XXX. Find channel IDs by viewing page source on a channel page or using online tools. This enables monitoring YouTube content without the official API. Note that YouTube feeds may have delays compared to the platform itself. Combine with QUERY to filter by video title keywords.

### Example 14: Track GitHub Repository Releases
```
=IMPORTFEED("https://github.com/microsoft/vscode/releases.atom", "items", TRUE, 5)
```
**Result:** Returns the 5 most recent VS Code releases from GitHub.

**Explanation:** GitHub provides Atom feeds for repository releases, commits, and other activities. The pattern is github.com/owner/repo/releases.atom. This is valuable for DevOps teams tracking dependencies, security researchers monitoring vulnerability patches, or users wanting update notifications. Combine feeds from multiple repositories for comprehensive dependency monitoring.

### Example 15: Error Handling with IFERROR
```
=IFERROR(IMPORTFEED("https://example.com/feed.xml", "items", TRUE, 10), "Feed unavailable - check URL or feed status")
```
**Result:** Returns feed items if successful, or displays the error message if import fails.

**Explanation:** IMPORTFEED can fail due to network issues, invalid feeds, server blocks, or URL changes. IFERROR catches all failures and provides user-friendly messaging. In shared dashboards, this prevents confusion when feeds are temporarily unavailable. Consider more informative messages: "Feed offline as of "&TEXT(NOW(),"YYYY-MM-DD HH:MM").

### Example 16: Create a News Dashboard with Multiple Sources
```
Cell A1: =IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml", "feed title")
Cell A2: =IMPORTFEED("https://feeds.bbci.co.uk/news/rss.xml", "items", FALSE, 5)
Cell E1: =IMPORTFEED("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "feed title")
Cell E2: =IMPORTFEED("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "items", FALSE, 5)
```
**Result:** Creates side-by-side news sections with source names as headers.

**Explanation:** Combine "feed title" for section headers with "items" for content to create organized multi-source dashboards. Position each source in a separate column block. Add conditional formatting based on publication date (highlight items less than 1 hour old). This pattern scales to many sources across multiple sheets or sections.

### Example 17: Monitor Blog Updates Across Industry Sites
```
=SORT(
  {
    IMPORTFEED("https://techcrunch.com/feed/", "items", FALSE, 10);
    IMPORTFEED("https://www.theverge.com/rss/index.xml", "items", FALSE, 10);
    IMPORTFEED("https://www.wired.com/feed/rss", "items", FALSE, 10)
  },
  3, FALSE
)
```
**Result:** Combines items from three tech blogs and sorts all by publication date (newest first).

**Explanation:** This advanced pattern aggregates multiple feeds and sorts the combined results chronologically. Column 3 typically contains publication dates; FALSE specifies descending order (newest first). This creates a unified timeline of industry news. Add more feeds to the array. Wrap in QUERY to filter for specific keywords or time ranges.

### Example 18: Extract Article Summaries for Analysis
```
=IMPORTFEED("https://www.economist.com/rss", "items summary", FALSE, 20)
```
**Result:** Returns article summaries/descriptions from The Economist's feed.

**Explanation:** "items summary" extracts the description or content preview for each item. Summary quality varies by feed - some include full paragraphs while others have only a sentence. Use summaries for content analysis, keyword extraction, or preview displays. Combine with QUERY CONTAINS filters to find articles mentioning specific topics.

### Example 19: Build a Press Release Monitor
```
=QUERY(
  IMPORTFEED("https://www.prnewswire.com/rss/news-releases-list.rss", "items", TRUE, 100),
  "SELECT Col1, Col2, Col3 WHERE Col1 CONTAINS '"&A1&"' ORDER BY Col3 DESC",
  1
)
```
**Result:** Filters press releases containing the company name in cell A1, sorted by date.

**Explanation:** PR newswire and similar services provide RSS feeds of press releases. By filtering for company names, product names, or keywords, you create targeted media monitoring. Build a competitor tracker where A1:A10 contains competitor names, each row feeding a separate IMPORTFEED/QUERY combination. Add email alerts via Google Apps Script when new matches appear.

### Example 20: Academic Paper Monitoring with arXiv
```
=IMPORTFEED("https://export.arxiv.org/rss/cs.AI", "items", TRUE, 20)
```
**Result:** Returns recent AI/machine learning papers from arXiv's computer science category.

**Explanation:** arXiv provides RSS feeds for each subject category. Monitor new research in your field without manually checking the site. The pattern is export.arxiv.org/rss/category (cs.AI, math.ST, physics.gen-ph, etc.). Combine multiple category feeds for interdisciplinary monitoring. Use QUERY to filter by keywords in titles or abstracts.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` with "Resource at URL not found" | The URL is incorrect, the feed doesn't exist, or the server returned a 404 error. | Verify the URL is correct and accessible in a browser. RSS feed URLs often differ from website URLs; look for feed links in page source or use RSS discovery tools. |
| `#N/A` with "Could not fetch URL" | Google's servers cannot reach the feed. The site may block Google, require authentication, or be experiencing downtime. | Test the URL in an incognito browser window. Some sites block automated requests. Try alternative feeds from the same source if available. |
| `#N/A` with "Resource at URL contains errors" | The URL returns content but it's not a valid RSS/Atom feed. Could be HTML, JSON, malformed XML, or a partial feed. | Verify the URL points to an actual RSS or Atom feed (should show XML in browser). Common mistake: using website URL instead of feed URL. |
| `#REF!` | The imported data would overwrite existing cell content or exceed spreadsheet limits. | Ensure sufficient empty cells below and to the right of the formula. Use num_items parameter to limit returned data if needed. |
| `#ERROR!` with invalid query | The query parameter contains an unrecognized value. Only specific query strings are valid. | Use exact query strings: "feed", "feed title", "feed description", "feed author", "feed url", "items", "items title", "items summary", "items url", "items created". |
| Empty or partial results | The feed exists but contains few items, or the publisher includes minimal metadata. Some feeds only have titles without summaries. | Check the raw feed XML in a browser to see what data is actually available. Different feeds include different amounts of information. |
| `#VALUE!` | Invalid parameter types - URL is not text, headers is not boolean, or num_items is not a positive integer. | Verify parameter types: URL as quoted text or cell reference, TRUE/FALSE for headers, positive integer for num_items. |
| Date parsing issues | Dates appear as text or in unexpected formats, preventing date calculations. | Use DATEVALUE() to convert text dates to date values. Feed date formats vary; some may require custom parsing with TEXT functions. |
| Garbled text or encoding issues | The feed uses non-UTF-8 encoding or contains special characters that don't display correctly. | Limited solutions within Sheets. Try SUBSTITUTE to replace problematic characters. Source feeds with encoding issues may require preprocessing. |
| Stale/cached data | Feed content hasn't updated despite new items at the source. IMPORTFEED caches results for one to two hours. | Wait for cache to expire. Workaround (use sparingly): append unique parameter to URL to potentially bypass cache, but this may not always work. |

## Use Cases

### Media Monitoring and Brand Tracking

**Implementation:** Create a comprehensive media monitoring dashboard that aggregates news mentions, blog coverage, and social media discussions about your brand, products, or industry topics. Use multiple IMPORTFEED calls to pull from news sites, industry blogs, and aggregators, then filter for relevant keywords.

**Business Application:** PR teams, marketing departments, and communications professionals need to track media coverage for reputation management, competitive intelligence, and campaign measurement. IMPORTFEED enables building custom monitoring solutions that rival expensive PR software. Track brand mentions, monitor competitor announcements, identify trending topics, and measure share of voice across sources. Alert stakeholders to significant coverage using Google Apps Script email triggers.

**Technical Details:**
```
// News aggregator monitoring
=QUERY(
  {
    IMPORTFEED("https://news.google.com/rss/search?q=YourBrand", "items", FALSE, 50);
    IMPORTFEED("https://hnrss.org/newest?q=YourBrand", "items", FALSE, 20);
    IMPORTFEED("https://www.reddit.com/search.rss?q=YourBrand&sort=new", "items", FALSE, 20)
  },
  "SELECT * WHERE Col1 IS NOT NULL ORDER BY Col3 DESC",
  0
)
```
Build a multi-sheet dashboard:
- Sheet 1: Brand mentions (filtered by brand/product names)
- Sheet 2: Competitor mentions (filtered by competitor names)
- Sheet 3: Industry keywords (filtered by topic terms)
- Sheet 4: Summary metrics and trends

Add conditional formatting:
- Highlight items less than 4 hours old (breaking news)
- Color-code by source type (news vs. blog vs. social)
- Flag items containing crisis keywords

Create a Google Apps Script to email daily summaries or send immediate alerts for high-priority keywords.

### Content Curation and Research Aggregation

**Implementation:** Build a research feed aggregator that monitors academic preprints, industry publications, technical blogs, and professional newsletters. Organize content by topic, filter for relevant keywords, and maintain a searchable archive of interesting content.

**Business Application:** Researchers, analysts, consultants, and knowledge workers need to stay current with developments in their fields. IMPORTFEED creates a personalized reading list that aggregates updates from dozens of sources without manually visiting each site. Curate content for team newsletters, research reports, or competitive analysis. Build a personal knowledge base by archiving valuable content over time.

**Technical Details:**
```
// Academic monitoring
=IMPORTFEED("https://export.arxiv.org/rss/cs.LG", "items", TRUE, 20)  // Machine Learning
=IMPORTFEED("https://export.arxiv.org/rss/stat.ML", "items", FALSE, 20)  // Statistical ML

// Industry blogs
=IMPORTFEED("https://openai.com/blog/rss.xml", "items", TRUE, 10)
=IMPORTFEED("https://ai.googleblog.com/feeds/posts/default", "items", FALSE, 10)

// Aggregated view with keyword filter
=QUERY(
  {Sheet1!A:D; Sheet2!A:D; Sheet3!A:D; Sheet4!A:D},
  "SELECT * WHERE Col1 CONTAINS 'transformer' OR Col1 CONTAINS 'GPT' OR Col4 CONTAINS 'neural network'",
  1
)
```
Create a research workflow:
1. **Intake Sheet:** Raw feeds import automatically
2. **Filter Sheet:** QUERY filters for relevant keywords
3. **Review Sheet:** Copy interesting items for reading
4. **Archive Sheet:** Save valuable content with notes and tags

Add helper columns:
- Source name: =VLOOKUP(url, sources_table, 2, FALSE)
- Days since publication: =DATEDIF(C2, TODAY(), "D")
- Read status: Manual checkbox or dropdown

### Competitive Intelligence Dashboard

**Implementation:** Monitor competitor activities through their blogs, press releases, job postings, product updates, and social media by aggregating RSS feeds from all available sources. Track patterns in announcements, hiring trends, and market positioning.

**Business Application:** Product managers, marketing teams, and business strategists need visibility into competitor activities. Most companies publish content via RSS-enabled channels: company blogs, press release services, job boards, and social accounts. Aggregate these feeds to spot product launches, partnership announcements, executive changes, and strategic shifts. Combine with manual research for comprehensive competitive intelligence.

**Technical Details:**
```
// Competitor blogs
=IMPORTFEED("https://competitor1.com/blog/feed", "items", TRUE, 10)
=IMPORTFEED("https://competitor2.com/blog/rss", "items", FALSE, 10)

// Press releases (via PR Newswire, BusinessWire, etc.)
=QUERY(
  IMPORTFEED("https://www.prnewswire.com/rss/news-releases-list.rss", "items", TRUE, 100),
  "SELECT * WHERE Col1 CONTAINS 'Competitor1' OR Col1 CONTAINS 'Competitor2'",
  1
)

// Job postings (via Indeed RSS or company careers)
=IMPORTFEED("https://www.indeed.com/rss?q=Competitor1&l=", "items", TRUE, 20)
```
Build a competitor dashboard:
| Company | Recent Blog Posts | Press Releases | Open Positions | Social Activity |
|---------|------------------|----------------|----------------|-----------------|
| Comp 1  | [IMPORTFEED...] | [QUERY/FILTER...] | [IMPORTFEED...] | [IMPORTFEED...] |
| Comp 2  | [IMPORTFEED...] | [QUERY/FILTER...] | [IMPORTFEED...] | [IMPORTFEED...] |

Track metrics over time:
- Number of press releases per month
- Job posting trends (growth/decline indicators)
- Blog post frequency and topics
- Social media posting patterns

### Podcast and Video Content Monitoring

**Implementation:** Create a media consumption dashboard that tracks new episodes from podcasts you follow and videos from YouTube channels, organizing content for efficient consumption and team sharing.

**Business Application:** Marketing teams monitoring industry podcasts for trends and opportunities, sales teams tracking competitor executives' podcast appearances, learning and development teams curating educational content, and content teams researching topics all benefit from centralized podcast and video monitoring. IMPORTFEED extracts episode metadata without requiring platform-specific tools.

**Technical Details:**
```
// Podcast feeds
=IMPORTFEED("https://feeds.simplecast.com/PODCAST_ID", "items", TRUE, 10)
=IMPORTFEED("https://anchor.fm/s/SHOW_ID/podcast/rss", "items", FALSE, 10)

// YouTube channels
=IMPORTFEED("https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID", "items", TRUE, 10)

// Aggregate with source labels
={
  "Podcast A", IMPORTFEED(podcast_a_url, "items title", FALSE, 5);
  "Podcast B", IMPORTFEED(podcast_b_url, "items title", FALSE, 5);
  "YouTube Channel", IMPORTFEED(youtube_url, "items title", FALSE, 5)
}
```
Build a content consumption workflow:
1. **New Content:** Automatically populated via IMPORTFEED
2. **Queue:** Manually move interesting items to watch/listen list
3. **Completed:** Archive with notes and ratings
4. **Team Recommendations:** Share standout content with colleagues

Add helper columns:
- Duration (if available in feed)
- Category/topic tags
- Priority rating
- Assigned team member
- Completion status

## Platform Differences

| Feature | Google Sheets | Microsoft Excel |
|---------|---------------|-----------------|
| Function name | IMPORTFEED | No direct equivalent; requires Power Query with XML parsing |
| Syntax complexity | Single formula with optional parameters | Multi-step process: Data > From Web > Configure XML > Transform > Load |
| Query options | Simple query strings ("items", "items title", etc.) | Requires M code/Power Query to select specific elements |
| Live updates | Automatic on recalculation (cached 1-2 hours) | Manual refresh or scheduled refresh configuration |
| Headers option | Built-in parameter (TRUE/FALSE) | Must configure in Power Query transformation |
| Item limit | Built-in parameter (num_items) | Filter in Power Query or after loading |
| Feed metadata | "feed title", "feed description" queries | Requires additional XPath/M code queries |
| Multiple feeds | Combine with array notation {} | Requires multiple queries or complex M code |
| Error handling | IFERROR wrapper | Power Query error handling in M code |
| RSS vs Atom | Automatic detection and parsing | May require format-specific handling |
| Mobile support | Works in mobile app (read-only) | Power Query not available on mobile |

**Key Differences Explained:**

Google Sheets' IMPORTFEED provides purpose-built RSS/Atom parsing in a single formula with intuitive query parameters. Excel has no equivalent function; RSS parsing requires either Power Query's XML capabilities (complex), WEBSERVICE combined with FILTERXML (limited and complex), or third-party add-ins.

For simple RSS consumption, IMPORTFEED takes seconds to implement while Excel alternatives require significant XML and M code knowledge. This makes IMPORTFEED a standout feature for content monitoring use cases in Google Sheets.

When migrating from Sheets to Excel, IMPORTFEED workflows must be completely reimagined. Consider using Power Automate (Microsoft Flow) to fetch RSS feeds and push to Excel, or explore third-party RSS-to-Excel solutions.

## Tips and Best Practices

1. **Locate Valid Feed URLs:** Not all websites advertise their RSS feeds prominently. Look for RSS icons, check for /feed or /rss in the URL, view page source for <link type="application/rss+xml">, or use browser extensions like "Get RSS Feed URL" to discover hidden feeds. Many sites have feeds even without visible links.

2. **Use IFERROR for Reliability:** Feeds can become unavailable without notice. Always wrap IMPORTFEED in IFERROR: =IFERROR(IMPORTFEED(url,"items",TRUE,10),"Feed unavailable"). This is especially important for dashboards shared with others who may not understand error codes.

3. **Limit Results with num_items:** Unless you need historical data, limit results to reduce spreadsheet clutter and improve performance: =IMPORTFEED(url,"items",TRUE,10). Most use cases only need the 10-20 most recent items. Large feeds can slow down your spreadsheet significantly.

4. **Combine with QUERY for Power Filtering:** QUERY enables keyword filtering, date filtering, and column selection: =QUERY(IMPORTFEED(url,"items",TRUE),"WHERE Col1 CONTAINS 'keyword'",1). This creates targeted monitors that surface only relevant content from high-volume feeds.

5. **Sort Aggregated Feeds by Date:** When combining multiple feeds, sort chronologically for a unified timeline: =SORT({IMPORTFEED(url1); IMPORTFEED(url2)},3,FALSE). Column 3 typically contains publication dates; FALSE specifies descending (newest first).

6. **Monitor Feed Structure Changes:** Feeds occasionally change format or move to new URLs. Create validation formulas that check for expected content: =IF(ROWS(IMPORTFEED(url))>0,"Active","Check Feed"). Review feeds periodically to catch problems before they impact workflows.

7. **Respect Publisher Rate Limits:** Aggressive refreshing can get your requests blocked. Google's caching typically makes this manageable, but avoid formulas that force constant recalculation. Don't use NOW() or volatile functions in combination with IMPORTFEED. If building intensive monitoring, consider caching results to a separate sheet.

8. **Document Your Feed Sources:** Maintain a reference sheet with feed URLs, source names, expected update frequency, and purpose. This helps with troubleshooting and ensures continuity if you need to hand off the dashboard to others. Include notes on any special formatting or filtering applied.

## Related Functions

### Similar Functions

| Function | Description | Key Difference |
|----------|-------------|----------------|
| [[IMPORTXML]] | Imports data from web pages using XPath queries | More flexible for any XML; IMPORTFEED is specifically optimized for RSS/Atom |
| [[IMPORTHTML]] | Imports tables or lists from HTML web pages | For HTML structure; not designed for XML feeds |
| [[IMPORTDATA]] | Imports CSV or TSV data from URLs | For structured data files; cannot parse XML/RSS |
| [[IMPORTRANGE]] | Imports data from another Google Sheets spreadsheet | For Sheets-to-Sheets transfer; not for web content |

### Commonly Used Together

**[[QUERY]]** - Filter and transform feed items

QUERY is the essential companion to IMPORTFEED, enabling keyword filtering, date selection, and column reshaping.

```
=QUERY(IMPORTFEED("https://example.com/feed.rss", "items", TRUE, 50), "SELECT Col1, Col2 WHERE Col1 CONTAINS 'keyword' ORDER BY Col3 DESC", 1)
```
Filters feed items to only those containing the keyword, showing title and URL sorted by date.

**[[IFERROR]]** - Handle feed failures gracefully

IFERROR prevents error messages when feeds are unavailable, essential for production dashboards.

```
=IFERROR(IMPORTFEED("https://example.com/feed.rss", "items", TRUE, 10), "Feed temporarily unavailable")
```
Displays a friendly message instead of #N/A when the feed cannot be fetched.

**[[SORT]]** - Chronologically order combined feeds

SORT arranges aggregated feed items by publication date for a unified timeline.

```
=SORT({IMPORTFEED(url1,"items",FALSE,10); IMPORTFEED(url2,"items",FALSE,10)}, 3, FALSE)
```
Combines two feeds and sorts all items by column 3 (date) in descending order.

**[[FILTER]]** - Select items meeting criteria

FILTER extracts specific items based on date, keyword, or other conditions.

```
=FILTER(IMPORTFEED(url,"items",TRUE), SEARCH("AI", IMPORTFEED(url,"items title")))
```
Returns only feed items with "AI" in the title.

**[[INDEX]]** - Extract specific elements from feeds

INDEX retrieves individual items or fields from feed results.

```
=INDEX(IMPORTFEED("https://example.com/feed.rss", "items", FALSE, 1), 1, 1)
```
Returns only the title of the most recent feed item.

**[[HYPERLINK]]** - Create clickable links from feed URLs

HYPERLINK makes feed item URLs clickable for easy navigation.

```
=ARRAYFORMULA(HYPERLINK(IMPORTFEED(url, "items url", FALSE, 10), IMPORTFEED(url, "items title", FALSE, 10)))
```
Creates clickable links using titles as display text.

## Official Documentation

- **Google Sheets Help:** [IMPORTFEED function](https://support.google.com/docs/answer/3093337)
- **Google Sheets Function List:** [Google Sheets function list](https://support.google.com/docs/table/25273)
- **RSS 2.0 Specification:** [RSS 2.0 Specification](https://www.rssboard.org/rss-specification)
- **Atom Syndication Format:** [RFC 4287 - Atom Syndication Format](https://tools.ietf.org/html/rfc4287)
- **Microsoft Excel:** No direct equivalent; consider [Power Query XML handling](https://support.microsoft.com/en-us/office/xml-data-source-afe29d7e-5d7e-46f9-8f79-ce0b0e0a0e63) or [Power Automate RSS connector](https://docs.microsoft.com/en-us/connectors/rss/)

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2006 | Initial Release | IMPORTFEED introduced with Google Spreadsheets launch; basic RSS 2.0 support |
| 2008 | Update | Added Atom feed format support; expanded query options |
| 2010 | Update | Improved parsing of non-standard feeds; better handling of namespaced elements |
| 2012 | Update | Enhanced error messaging for troubleshooting; improved reliability |
| 2014 | Security Update | Added restrictions on certain URL patterns; enhanced security validation |
| 2016 | Update | Performance improvements; better handling of large feeds |
| 2018 | Update | Improved handling of international character sets and encodings |
| 2020 | Update | Enhanced caching behavior; better handling of feed redirects |
| 2022 | Update | Improved compatibility with modern feed formats; better error recovery |
| 2024 | Update | Performance optimizations; improved mobile app display of feed data |
