---
categories:
  - spreadsheet-functions
subCategories:
  - sheets
topics:
  - google-specific
  - financial-data
  - market-data
subTopics:
  - stock-prices
  - historical-data
  - currency-exchange
  - market-metrics
dateCreated: '2025-08-17'
dateRevised: '2026-01-10'
aliases:
  - google finance
  - stock price
  - market data
  - financial quotes
  - ticker lookup
tags:
  - google-sheets
  - finance
  - stocks
  - real-time-data
  - investment
  - market-analysis
---

# GOOGLEFINANCE

## Description

GOOGLEFINANCE is one of Google Sheets' most powerful and unique functions, providing direct access to real-time and historical financial market data without requiring any external API keys, subscriptions, or complex data connections. This function can retrieve current stock prices, historical price data, currency exchange rates, mutual fund information, and dozens of financial metrics for publicly traded securities from exchanges around the world. Unlike traditional financial data solutions that require expensive Bloomberg terminals or Reuters subscriptions, GOOGLEFINANCE democratizes access to market data, making it available to anyone with a Google account. The function queries Google Finance's database and returns data directly into your spreadsheet cells, enabling everything from simple stock price lookups to sophisticated portfolio tracking dashboards and historical market analysis.

The primary use cases for GOOGLEFINANCE span personal finance, investment analysis, business operations, and educational applications. Individual investors use it to build portfolio trackers that automatically update with current market values, calculate gains and losses, and monitor watchlists of potential investments. Financial analysts leverage the historical data capabilities to perform technical analysis, calculate moving averages, analyze price patterns, and backtest trading strategies. Businesses with international operations use the currency exchange functionality to convert financial figures between currencies in real-time for reporting and planning purposes. Teachers and students in finance courses use GOOGLEFINANCE to bring real-world market data into educational spreadsheets, making abstract concepts tangible with live examples. The function is particularly valuable because it maintains data freshness automatically - prices update throughout the trading day without requiring manual refresh.

There are several critical limitations and gotchas that users must understand to use GOOGLEFINANCE effectively. First, the data provided is delayed - typically by 15-20 minutes for US markets and potentially longer for international exchanges - so it should not be used for real-time trading decisions. Google provides this data for informational purposes only and explicitly disclaims any guarantee of accuracy or completeness; always verify critical financial decisions with official sources. The function does not work with all securities - coverage is best for major US exchanges (NYSE, NASDAQ) and diminishes for smaller international markets, OTC stocks, and certain types of securities. Historical data availability varies by security and may not extend back as far as you need for long-term analysis. Additionally, Google has been known to change or deprecate certain attributes without warning, so formulas that work today may break in the future. The function also has usage limits - making too many GOOGLEFINANCE calls in a single spreadsheet can result in errors or incomplete data.

From a platform perspective, GOOGLEFINANCE is completely exclusive to Google Sheets with no equivalent function in Microsoft Excel. Excel users who need similar functionality must rely on the STOCKHISTORY function (introduced in Microsoft 365) for basic stock data, the Stocks data type for current prices, or external connections to financial data providers through Power Query. Excel's STOCKHISTORY function is actually quite capable for historical data but lacks the breadth of real-time attributes that GOOGLEFINANCE offers. For organizations using both platforms, this represents a significant capability gap that may influence which platform is chosen for financial analysis workbooks. Users migrating from Google Sheets to Excel will need to completely reimagine their approach to financial data, often requiring paid third-party add-ins or API connections to replicate GOOGLEFINANCE functionality.

## Syntax

> [!NOTE] GOOGLEFINANCE Syntax
> ```
> =GOOGLEFINANCE(ticker, [attribute], [start_date], [num_days|end_date], [interval])
> ```

| Parameter | Description | Required | Data Type |
|-----------|-------------|----------|-----------|
| `ticker` | The stock ticker symbol for the security you want to look up. For US securities, this is typically just the symbol (e.g., "GOOG", "AAPL"). For international securities, use the format "EXCHANGE:SYMBOL" (e.g., "LON:VOD" for Vodafone on the London Stock Exchange, "TYO:7203" for Toyota on the Tokyo Stock Exchange). For currency pairs, use "CURRENCY:FROMTO" (e.g., "CURRENCY:USDEUR"). For mutual funds, use the fund ticker. | Yes | String (text) |
| `attribute` | The type of data to return. Defaults to "price" if omitted. See the Attributes section below for the complete list of available attributes including price, priceopen, high, low, volume, marketcap, pe, eps, and many more. For historical data, use "all" to get OHLCV data or specific attributes like "close" or "volume". | No | String (text) |
| `start_date` | For historical data queries, the start date from which to begin retrieving data. Can be a date value, a cell reference containing a date, or a date string. Required when requesting historical data (when num_days or end_date is specified). | No | Date |
| `num_days` or `end_date` | Either the number of days of historical data to retrieve (as an integer) or an end date for the historical range. If a number less than or equal to the number of days between start_date and today is provided, it is treated as num_days. If a date or larger number is provided, it is treated as end_date. | No | Number or Date |
| `interval` | The frequency of returned data for historical queries. Use "DAILY" or 1 for daily data, "WEEKLY" or 7 for weekly data. Only applicable when retrieving historical data. Defaults to "DAILY" if omitted. | No | String or Number |

### Available Attributes for Real-Time Data

| Attribute | Description | Example |
|-----------|-------------|---------|
| `price` | The current trading price (default if no attribute specified). Delayed 15-20 minutes. | 150.25 |
| `priceopen` | The opening price for the current trading day. | 149.80 |
| `high` | The highest price reached during the current trading day. | 151.50 |
| `low` | The lowest price reached during the current trading day. | 148.90 |
| `volume` | The trading volume for the current day. | 45678901 |
| `marketcap` | The market capitalization (shares outstanding multiplied by current price). | 2500000000000 |
| `tradetime` | The date and time of the last trade. | 1/10/2026 15:45:30 |
| `datadelay` | The number of minutes the data is delayed. | 15 |
| `volumeavg` | The average daily trading volume. | 52345678 |
| `pe` | The price-to-earnings ratio (trailing twelve months). | 28.5 |
| `eps` | Earnings per share (trailing twelve months). | 5.27 |
| `high52` | The 52-week high price. | 180.00 |
| `low52` | The 52-week low price. | 120.00 |
| `change` | The price change since the previous close (in currency units). | 2.45 |
| `changepct` | The percentage change since the previous close. | 0.0165 (1.65%) |
| `closeyest` | Yesterday's closing price. | 147.80 |
| `shares` | The number of outstanding shares. | 16500000000 |
| `currency` | The currency in which the security is traded. | USD |
| `name` | The full name of the security. | Apple Inc |

### Attributes for Historical Data

| Attribute | Description | Returns |
|-----------|-------------|---------|
| `open` | Historical opening prices | Date and Open columns |
| `high` | Historical high prices | Date and High columns |
| `low` | Historical low prices | Date and Low columns |
| `close` | Historical closing prices | Date and Close columns |
| `volume` | Historical trading volumes | Date and Volume columns |
| `all` | All available historical data | Date, Open, High, Low, Close, Volume columns |

### Currency Exchange Attributes

| Attribute | Description |
|-----------|-------------|
| `price` | Current exchange rate (default) |
| `name` | Currency pair description |

## Examples

### Example 1: Basic Current Stock Price
```
=GOOGLEFINANCE("AAPL")
```
**Result:** 185.92 (current Apple stock price)

**Explanation:** The simplest form of GOOGLEFINANCE returns the current price of a stock. When you omit the attribute parameter, it defaults to "price". The ticker symbol must be in quotes. This returns a single number representing the most recent traded price, delayed by approximately 15-20 minutes for US markets. The result updates automatically as the market price changes.

### Example 2: Retrieving the Price-to-Earnings Ratio
```
=GOOGLEFINANCE("MSFT", "pe")
```
**Result:** 35.42

**Explanation:** The PE ratio is a fundamental valuation metric comparing a company's stock price to its earnings per share. This formula retrieves Microsoft's trailing twelve-month P/E ratio. A higher PE suggests investors expect higher future growth, while a lower PE may indicate undervaluation or lower growth expectations. This attribute is invaluable for comparing valuations across similar companies or tracking a company's valuation over time.

### Example 3: Getting Market Capitalization
```
=GOOGLEFINANCE("GOOGL", "marketcap")
```
**Result:** 1850000000000 (1.85 trillion)

**Explanation:** Market capitalization represents the total market value of a company's outstanding shares (shares outstanding multiplied by current price). This returns a large number representing Alphabet's market cap in the trading currency (USD). For readability in dashboards, you might format this with billions: =GOOGLEFINANCE("GOOGL","marketcap")/1000000000 & "B" would display as "1850B".

### Example 4: Earnings Per Share
```
=GOOGLEFINANCE("NVDA", "eps")
```
**Result:** 11.93

**Explanation:** EPS (Earnings Per Share) represents the portion of a company's profit allocated to each outstanding share of common stock. This retrieves NVIDIA's trailing twelve-month EPS. Combined with the PE ratio, EPS helps investors understand both profitability and valuation. You can calculate implied PE by dividing current price by EPS: =GOOGLEFINANCE("NVDA")/GOOGLEFINANCE("NVDA","eps").

### Example 5: 52-Week High and Low Range
```
=GOOGLEFINANCE("TSLA", "high52") & " - " & GOOGLEFINANCE("TSLA", "low52")
```
**Result:** 299.29 - 138.80

**Explanation:** The 52-week high and low represent the highest and lowest prices at which a stock has traded over the past year. This formula combines both values with a hyphen to show the trading range. You can calculate where the current price falls within this range: =(GOOGLEFINANCE("TSLA")-GOOGLEFINANCE("TSLA","low52"))/(GOOGLEFINANCE("TSLA","high52")-GOOGLEFINANCE("TSLA","low52")) returns a percentage from 0% (at 52-week low) to 100% (at 52-week high).

### Example 6: Daily Price Change and Percentage
```
="Change: $" & TEXT(GOOGLEFINANCE("AMZN", "change"), "0.00") & " (" & TEXT(GOOGLEFINANCE("AMZN", "changepct")*100, "0.00") & "%)"
```
**Result:** Change: $3.45 (1.89%)

**Explanation:** This formula combines the absolute price change with the percentage change into a readable string. The "change" attribute returns the dollar amount of change from the previous close, while "changepct" returns the decimal percentage (0.0189 for 1.89%). Note that changepct must be multiplied by 100 to display as a conventional percentage. This is essential for watchlists and portfolio dashboards where you need to see daily movement at a glance.

### Example 7: Currency Exchange Rate
```
=GOOGLEFINANCE("CURRENCY:USDEUR")
```
**Result:** 0.9234

**Explanation:** For currency conversion, use the format "CURRENCY:FROMTO" where FROM is the source currency and TO is the target currency. This returns how many Euros one US Dollar can buy. To convert a dollar amount to Euros, multiply by this rate: =A1*GOOGLEFINANCE("CURRENCY:USDEUR"). Exchange rates are updated frequently but still subject to the typical data delay. This is perfect for international business reporting or travel budgeting.

### Example 8: Converting Between Multiple Currencies
```
=100*GOOGLEFINANCE("CURRENCY:GBPJPY")
```
**Result:** 19234.56 (100 British Pounds in Japanese Yen)

**Explanation:** You can request exchange rates between any two major currencies directly. This converts 100 GBP to JPY. For currencies not directly paired in Google Finance, you might need to convert through USD: =100*GOOGLEFINANCE("CURRENCY:GBPUSD")*GOOGLEFINANCE("CURRENCY:USDJPY"). The function supports all major world currencies including USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, and many others.

### Example 9: International Stock on Foreign Exchange
```
=GOOGLEFINANCE("LON:BP", "price")
```
**Result:** 452.35 (price in British Pence)

**Explanation:** For stocks on international exchanges, prefix the ticker with the exchange code followed by a colon. Common exchange codes include: LON (London), TYO (Tokyo), HKG (Hong Kong), FRA (Frankfurt), EPA (Paris/Euronext), TSE (Toronto), ASX (Australian), NSE (India National), and BOM (Bombay). Note that prices are in local currency - London Stock Exchange prices are typically in pence (1/100 of a pound), so divide by 100 for pounds: =GOOGLEFINANCE("LON:BP")/100.

### Example 10: Historical Price Data - Last 30 Days
```
=GOOGLEFINANCE("META", "close", TODAY()-30, 30)
```
**Result:** Returns a two-column array with dates in column 1 and closing prices in column 2, showing 30 days of data.

**Explanation:** When you provide start_date and num_days parameters, GOOGLEFINANCE returns historical data as an array. This formula requests the closing prices for Meta stock for the last 30 days. The result spills into multiple cells automatically (in modern Sheets) showing Date in the first column and Close price in the second. The first row contains headers ("Date" and "Close"). This is perfect for creating price charts or calculating moving averages.

### Example 11: Historical Data with Specific Date Range
```
=GOOGLEFINANCE("JPM", "all", DATE(2025,1,1), DATE(2025,12,31), "DAILY")
```
**Result:** Returns a 6-column array with Date, Open, High, Low, Close, and Volume for all trading days in 2025.

**Explanation:** Using "all" as the attribute returns complete OHLCV (Open, High, Low, Close, Volume) data. Specifying both a start date and end date retrieves exactly that range. The "DAILY" interval parameter ensures one row per trading day (weekends and holidays are excluded). This data structure is ideal for technical analysis, creating candlestick charts, or calculating indicators like RSI, MACD, or Bollinger Bands.

### Example 12: Weekly Historical Data
```
=GOOGLEFINANCE("DIS", "close", TODAY()-365, TODAY(), "WEEKLY")
```
**Result:** Returns approximately 52 rows of weekly closing prices for the past year.

**Explanation:** Setting the interval to "WEEKLY" aggregates data into weekly periods, reducing the number of data points. This is useful for longer-term trend analysis where daily fluctuations create too much noise. Weekly data shows the closing price for each week (typically Friday's close). For a one-year view, this gives you about 52 data points instead of approximately 252 trading days.

### Example 13: Building a Portfolio Tracker
```
=GOOGLEFINANCE(A2)*B2
```
**Result:** If A2 contains "AAPL" and B2 contains 100, returns the current value of 100 Apple shares.

**Explanation:** Reference ticker symbols from cells to build dynamic portfolio trackers. In a spreadsheet with tickers in column A and shares owned in column B, this formula calculates position value. Extend with additional columns for cost basis, gain/loss, and percentage of portfolio. The formulas automatically update as prices change throughout the trading day.

### Example 14: Calculating Portfolio Total with Multiple Positions
```
=SUMPRODUCT(GOOGLEFINANCE(A2:A10), B2:B10)
```
**Result:** Returns the total market value of all positions.

**Explanation:** SUMPRODUCT multiplies each stock's current price by the number of shares and sums the results. This single formula calculates total portfolio value across all positions. Note: This approach makes multiple GOOGLEFINANCE calls, which can slow down your spreadsheet. For large portfolios, consider using a helper column with individual GOOGLEFINANCE calls rather than embedding them in SUMPRODUCT.

### Example 15: Comparing Stock Performance
```
=GOOGLEFINANCE("AAPL","changepct")-GOOGLEFINANCE("SPY","changepct")
```
**Result:** 0.0052 (Apple outperforming S&P 500 by 0.52% today)

**Explanation:** Compare a stock's daily performance against a benchmark by subtracting percentage changes. SPY is an ETF tracking the S&P 500 index. A positive result means the stock is outperforming the market that day; negative means underperforming. You can track any stock against any benchmark (QQQ for NASDAQ, DIA for Dow Jones, IWM for Russell 2000).

### Example 16: Getting Stock Name and Currency
```
=GOOGLEFINANCE("BABA", "name") & " (" & GOOGLEFINANCE("BABA", "currency") & ")"
```
**Result:** Alibaba Group Holding Ltd (USD)

**Explanation:** The "name" attribute returns the full company name, and "currency" returns the trading currency. This is helpful when building dashboards where users may not recognize ticker symbols, or when dealing with international stocks where it is important to know what currency the prices are quoted in. Alibaba trades on NYSE in USD, not in Chinese Yuan.

### Example 17: Checking Data Freshness
```
=GOOGLEFINANCE("GOOG", "tradetime")
```
**Result:** 1/10/2026 15:32:45 (date and time of last trade)

**Explanation:** The "tradetime" attribute returns when the last trade occurred. This helps verify data freshness and understand if markets are open or closed. During market hours, this updates frequently. After hours, it shows the last trade time before close. Combined with the "datadelay" attribute, you can understand exactly how current your data is.

### Example 18: Volume Analysis
```
=GOOGLEFINANCE("AMD", "volume")/GOOGLEFINANCE("AMD", "volumeavg")
```
**Result:** 1.45 (current volume is 145% of average)

**Explanation:** Comparing today's trading volume to the average volume indicates unusual activity. A ratio greater than 1 means higher-than-normal trading; less than 1 means lower-than-normal. Unusually high volume often accompanies significant news or price movements. This metric is essential for momentum traders and anyone watching for breakout patterns.

### Example 19: Creating a Price Alert Formula
```
=IF(GOOGLEFINANCE("NVDA")>500, "SELL ALERT: NVDA above $500", IF(GOOGLEFINANCE("NVDA")<400, "BUY ALERT: NVDA below $400", "No action"))
```
**Result:** Returns an alert message if price crosses specified thresholds.

**Explanation:** While GOOGLEFINANCE cannot send notifications on its own, you can create alert conditions in your spreadsheet. Combine with conditional formatting to highlight cells when conditions are met. For actual notifications, you would need to add a Google Apps Script that checks these conditions and sends emails. This formula demonstrates the logic for price-based alerts.

### Example 20: Historical Moving Average Calculation
```
=AVERAGE(INDEX(GOOGLEFINANCE("MSFT", "close", TODAY()-50, 50), , 2))
```
**Result:** Returns the 50-day simple moving average for Microsoft.

**Explanation:** This formula retrieves 50 days of closing prices and calculates their average. INDEX with column 2 extracts just the price column (excluding dates). The 50-day moving average is a common technical indicator. You can modify the days parameter for different periods (20-day, 100-day, 200-day). Comparing current price to moving averages helps identify trends and potential support/resistance levels.

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `#N/A` | The ticker symbol is not recognized or not available in Google Finance's database. | Verify the ticker symbol is correct. For international stocks, include the exchange prefix (e.g., "LON:BP"). Try searching for the company in Google Finance directly to find the correct ticker. Some securities (OTC, certain ETFs, smaller international stocks) are not available. |
| `#N/A` with "Invalid" message | The attribute you requested is not valid or not available for the specified security. | Check spelling of the attribute. Not all attributes work for all security types (e.g., PE ratio is not available for ETFs or indices). Currency pairs only support limited attributes. |
| `#REF!` | The formula is returning an array but there is not enough space in the destination cells. | Historical data queries return multi-row arrays. Ensure sufficient empty cells below and to the right of the formula. In legacy Sheets, you might need to manually specify the output range. |
| `#VALUE!` | Invalid date format in start_date or end_date parameters, or invalid data type for parameters. | Ensure dates are valid date values, not text strings. Use DATE() function or cell references to dates. Verify num_days is a positive integer. |
| `#ERROR!` | Syntax error in the formula, such as missing quotes around text parameters. | Check that ticker and attribute are enclosed in quotes. Verify all parameters are separated by commas. Ensure parentheses are balanced. |
| `Loading...` | The function is still fetching data from Google Finance servers. | Wait a few seconds for data to load. If it persists, the data may be temporarily unavailable. Try refreshing the page. Very large historical data requests may take longer. |
| `0` or blank for volume | The market is closed or there has been no trading activity. | Check if the market is open. After hours and on weekends/holidays, some real-time attributes may show zero or stale data. This is expected behavior. |
| Stale data (not updating) | Google Finance data is delayed and may not reflect the most recent trades. | Understand that data is delayed 15-20 minutes for US markets, longer for some international markets. For real-time data, use a dedicated trading platform. Force refresh by editing any cell in the sheet. |
| `#NUM!` | The historical date range is invalid or extends before available data. | Verify start_date is before end_date. Not all securities have complete historical data. Try a more recent date range. Some newer stocks may not have data extending back to your requested start date. |

## Use Cases

### Personal Portfolio Tracker

**Implementation:** Create a comprehensive portfolio management spreadsheet that tracks all your investments, calculates current values, monitors gains/losses, and provides allocation analysis. The spreadsheet uses GOOGLEFINANCE to automatically update prices throughout the trading day, eliminating manual data entry.

**Business Application:** Individual investors can track holdings across multiple brokerage accounts in a single unified view. The tracker shows real-time portfolio value, daily changes, total return on each position, and portfolio allocation percentages. You can set up watchlists for potential investments, track dividends, and monitor how your portfolio compares to benchmark indices. This replaces expensive portfolio management software for most personal finance needs.

**Technical Details:**
```
| A (Ticker) | B (Shares) | C (Cost Basis) | D (Current Price) | E (Market Value) | F (Gain/Loss) | G (% Return) |
|------------|------------|----------------|-------------------|------------------|---------------|--------------|
| AAPL       | 100        | $12,500        | =GOOGLEFINANCE(A2)| =D2*B2           | =E2-C2        | =F2/C2       |
| MSFT       | 50         | $15,000        | =GOOGLEFINANCE(A3)| =D3*B3           | =E3-C3        | =F3/C3       |
```
Include a summary section with: =SUM(E2:E100) for total portfolio value, =SUMPRODUCT(GOOGLEFINANCE(A2:A10,"changepct"),E2:E10)/SUM(E2:E10) for weighted portfolio daily change, and comparison to =GOOGLEFINANCE("SPY","changepct") for benchmark performance.

### Currency Conversion Dashboard

**Implementation:** Build a multi-currency conversion tool for international business operations that converts any amount between multiple currencies using live exchange rates. This supports financial reporting, procurement decisions, and pricing across international markets.

**Business Application:** International businesses need to convert between currencies for vendor payments, pricing decisions, financial consolidation, and travel expense reporting. This dashboard provides instant conversion between all major currencies, shows currency trends over time, and can convert entire columns of financial data from one currency to another. Finance teams can use it to understand currency impact on international P&L statements.

**Technical Details:**
```
=A2 * GOOGLEFINANCE("CURRENCY:" & $B$1 & C$1)
```
Where A2 contains the amount, B1 contains the source currency code (e.g., "USD"), and C1 contains the target currency code (e.g., "EUR"). Create a conversion matrix:
```
=GOOGLEFINANCE("CURRENCY:" & $A2 & B$1)
```
With currency codes in both row 1 (B1:G1) and column A (A2:A7), this creates a complete cross-currency conversion table. Add historical exchange rate tracking: =SPARKLINE(INDEX(GOOGLEFINANCE("CURRENCY:USDEUR","close",TODAY()-30,30),,2)) to show 30-day currency trends.

### Stock Screening and Analysis Tool

**Implementation:** Build a stock screener that evaluates multiple companies across key financial metrics, enabling systematic comparison for investment research. The tool pulls PE ratios, market caps, 52-week ranges, and volume data to identify potential investments.

**Business Application:** Investment analysts and individual investors can screen stocks across multiple criteria without expensive research platforms. Compare peer companies in an industry by valuation metrics, identify oversold stocks near 52-week lows, find stocks with unusual volume activity, or rank companies by market cap. This democratizes access to the same types of screening tools used by professional investors.

**Technical Details:**
```
| Ticker | Price | PE | EPS | MarketCap | 52W High | 52W Low | % from 52W High | Volume Ratio |
|--------|-------|-----|-----|-----------|----------|---------|-----------------|--------------|
| =A2    | =GOOGLEFINANCE(A2) | =GOOGLEFINANCE(A2,"pe") | =GOOGLEFINANCE(A2,"eps") | =GOOGLEFINANCE(A2,"marketcap")/1e9 | =GOOGLEFINANCE(A2,"high52") | =GOOGLEFINANCE(A2,"low52") | =(B2-F2)/F2 | =GOOGLEFINANCE(A2,"volume")/GOOGLEFINANCE(A2,"volumeavg") |
```
Add conditional formatting to highlight: PE ratios below industry average (green), stocks more than 20% below 52-week highs (yellow for potential value), volume ratios above 1.5 (blue for unusual activity). Include FILTER or QUERY to create dynamic views showing only stocks meeting specific criteria.

### Historical Price Analysis and Technical Indicators

**Implementation:** Create a technical analysis worksheet that retrieves historical price data and calculates common technical indicators like moving averages, RSI, and price channels. This enables charting and trend analysis directly in Google Sheets.

**Business Application:** Traders and analysts can perform technical analysis without specialized charting software. Calculate and visualize moving average crossovers (golden cross/death cross signals), identify support and resistance levels from historical highs and lows, track volatility through price ranges, and backtest simple trading strategies. While not a replacement for professional trading platforms, this serves educational purposes and basic analysis needs.

**Technical Details:**
```
=GOOGLEFINANCE("AAPL", "all", TODAY()-365, TODAY(), "DAILY")
```
This returns a full year of OHLCV data. Add calculated columns:
- 50-day SMA: =AVERAGE(OFFSET($E$2,ROW()-2,0,-50,1)) where column E is Close prices
- 200-day SMA: =AVERAGE(OFFSET($E$2,ROW()-2,0,-200,1))
- Daily Range: =(C2-D2)/E2 (High-Low as percentage of Close)
- 20-day High Channel: =MAX(OFFSET($C$2,ROW()-2,0,-20,1))
- 20-day Low Channel: =MIN(OFFSET($D$2,ROW()-2,0,-20,1))

Create a candlestick chart from the OHLC data using Insert > Chart > Candlestick chart. Overlay line charts for moving averages to visualize crossover signals.

## Platform Differences

| Feature | Google Sheets | Microsoft Excel |
|---------|---------------|-----------------|
| Function name | GOOGLEFINANCE | STOCKHISTORY (historical data), Stocks data type (current data) |
| Real-time current prices | Yes, via =GOOGLEFINANCE("AAPL") | Yes, via Stocks data type: cell with ticker converted to linked data type |
| Historical data | Yes, via attribute "close", "all", etc. with date parameters | Yes, via =STOCKHISTORY("AAPL", start, end, interval, headers, properties) |
| Available attributes | 20+ attributes including pe, eps, marketcap, high52, low52, etc. | Limited to OHLCV historical data; current data via data type provides more |
| Currency conversion | Yes, via "CURRENCY:USDEUR" syntax | No native function; requires external data source or manual rates |
| Data delay | 15-20 minutes for US markets | Varies by data provider; Excel uses Refinitiv data |
| Exchange coverage | Major global exchanges; best coverage for US markets | Good coverage through Refinitiv partnership |
| Cost | Free | Requires Microsoft 365 subscription for STOCKHISTORY |
| Custom portfolios | Build manually with formulas | Can use Stocks data type with portfolio templates |
| Mobile support | Full functionality in Sheets mobile app | Stocks data type works in mobile Excel |
| Refresh behavior | Automatic refresh during market hours | Manual refresh or scheduled refresh depending on version |

**Key Differences Explained:**

Google Sheets' GOOGLEFINANCE provides an all-in-one solution for financial data with a simple, intuitive syntax. Excel's approach is more fragmented - you use the Stocks data type for current data (which requires converting cells to a special linked data type) and STOCKHISTORY for historical data (which has different syntax and parameters). GOOGLEFINANCE's currency conversion capability has no native equivalent in Excel.

Excel's Stocks data type is actually quite powerful once understood, providing access to extensive company information beyond just price data. However, it requires a different workflow - you type a company name or ticker, convert the cell to a Stocks data type, then reference properties. This is less formula-friendly than GOOGLEFINANCE's straightforward function approach.

For organizations using both platforms, GOOGLEFINANCE formulas will not work in Excel and must be redesigned using Excel's native capabilities or external data connections.

## Tips and Best Practices

1. **Cache Expensive Calls:** Rather than calling GOOGLEFINANCE multiple times for the same ticker with different attributes, retrieve the value once and reference that cell elsewhere. For example, put =GOOGLEFINANCE("AAPL") in one cell and reference that cell in multiple calculations. This reduces API calls and improves spreadsheet performance.

2. **Handle Errors Gracefully:** Always wrap GOOGLEFINANCE in IFERROR for production dashboards: =IFERROR(GOOGLEFINANCE("AAPL"),"Data unavailable"). This prevents ugly #N/A errors when data is temporarily unavailable or ticker symbols are incorrect. Consider using IFERROR with a fallback to cached data for critical applications.

3. **Understand Data Limitations:** Remember that GOOGLEFINANCE data is delayed (typically 15-20 minutes), not guaranteed for accuracy, and should never be used for real-time trading decisions. Google can change data availability without notice. Always verify critical financial decisions with your broker or official market data sources.

4. **Use Cell References for Tickers:** Instead of hardcoding ticker symbols in formulas, reference cells containing tickers: =GOOGLEFINANCE(A2) instead of =GOOGLEFINANCE("AAPL"). This makes your spreadsheet more flexible, allows easy addition of new stocks, and enables dynamic portfolio management.

5. **Minimize Historical Data Requests:** Large historical data queries slow down your spreadsheet significantly. Request only the date range and attributes you actually need. If you need historical data for multiple stocks, consider running the analysis once and copying values (Paste Special > Values Only) rather than keeping live historical formulas.

6. **Format Currency and Percentage Attributes Appropriately:** GOOGLEFINANCE returns raw numbers. The "changepct" attribute returns a decimal (0.0165 for 1.65%), not a percentage. Apply appropriate number formatting or multiply by 100 for display. Market cap returns the full number, so divide by 1e9 and add "B" suffix for readability.

7. **Know the Exchange Codes:** For international stocks, you must use the correct exchange prefix. Common codes: NYSE/NASDAQ (no prefix needed for US), LON (London), TYO (Tokyo), HKG (Hong Kong), FRA (Frankfurt), EPA (Euronext Paris), TSE (Toronto), ASX (Australia). Search Google Finance directly if unsure of the correct ticker format.

8. **Monitor Function Limits:** Google Sheets has undocumented limits on external data function calls. If you have a very large spreadsheet with hundreds of GOOGLEFINANCE calls, you may experience errors or incomplete data. Consider consolidating to fewer calls, using a separate "data" sheet that other sheets reference, or splitting across multiple spreadsheets.

## Related Functions

### Similar Functions

| Function | Description | Key Difference |
|----------|-------------|----------------|
| [[STOCKHISTORY]] (Excel) | Retrieves historical stock price data in Microsoft Excel | Excel equivalent for historical data only; different syntax; requires Microsoft 365 |
| [[IMPORTDATA]] | Imports data from a URL in CSV or TSV format | Can import financial data from external sources if provided as CSV; no built-in finance knowledge |
| [[IMPORTHTML]] | Imports tables or lists from web pages | Can scrape financial data from web pages, but requires manual parsing |
| [[IMPORTXML]] | Imports data using XPath queries from web pages | More flexible web scraping for financial sites not supported by GOOGLEFINANCE |
| [[IMPORTFEED]] | Imports RSS/Atom feed data | Can import financial news feeds |

### Commonly Used Together

**[[IFERROR]]** - Handle data unavailability gracefully

IFERROR prevents error messages when GOOGLEFINANCE cannot retrieve data, providing fallback values or messages.

```
=IFERROR(GOOGLEFINANCE("TICKER", "pe"), "N/A")
```
Returns "N/A" if the PE ratio is unavailable (common for ETFs, funds, or when data is temporarily unavailable).

**[[INDEX]]** - Extract specific values from historical data arrays

INDEX helps extract specific rows or columns from the arrays returned by historical GOOGLEFINANCE queries.

```
=INDEX(GOOGLEFINANCE("AAPL", "close", TODAY()-7, 7), 2, 2)
```
Extracts the closing price from the first data row (row 2, after headers) of a historical query.

**[[SPARKLINE]]** - Create inline charts from historical data

SPARKLINE creates mini charts directly in cells, perfect for visualizing price trends from GOOGLEFINANCE historical data.

```
=SPARKLINE(INDEX(GOOGLEFINANCE("GOOG", "close", TODAY()-30, 30), , 2))
```
Creates a 30-day price trend sparkline by extracting the close prices (column 2) from historical data.

**[[QUERY]]** - Filter and transform historical data

QUERY can filter GOOGLEFINANCE historical results by date ranges, price thresholds, or other criteria.

```
=QUERY(GOOGLEFINANCE("MSFT", "all", DATE(2025,1,1), DATE(2025,12,31)), "SELECT * WHERE Col5 > 400", 1)
```
Returns only the days where Microsoft's closing price (column 5) exceeded $400.

**[[TEXT]]** - Format financial numbers for display

TEXT converts raw GOOGLEFINANCE numbers into formatted strings for dashboards and reports.

```
=TEXT(GOOGLEFINANCE("AAPL"), "$#,##0.00")
```
Formats the current price as currency with thousands separator: "$185.92" instead of 185.92.

**[[IF]]** - Create conditional logic based on financial data

IF enables price alerts, threshold monitoring, and conditional formatting based on GOOGLEFINANCE values.

```
=IF(GOOGLEFINANCE("AAPL") < GOOGLEFINANCE("AAPL", "low52") * 1.1, "Near 52-week low", "Above threshold")
```
Alerts when the current price is within 10% of the 52-week low.

## Official Documentation

- **Google Sheets Help:** [GOOGLEFINANCE function](https://support.google.com/docs/answer/3093281)
- **Google Finance Disclaimer:** [Google Finance Terms](https://www.google.com/intl/en/googlefinance/disclaimer/)
- **Microsoft Excel:** No direct equivalent; see [STOCKHISTORY function](https://support.microsoft.com/en-us/office/stockhistory-function-1c8a3c3c-1d43-4f72-81dc-3c78e5a1b8f8) for Excel's historical stock data function, and [Get stock quotes and geographic data](https://support.microsoft.com/en-us/office/get-stock-quotes-and-geographic-data-61a33056-9935-484f-8ac8-f1a89e210877) for Excel's Stocks data type

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2006 | Initial Release | GOOGLEFINANCE introduced with basic stock price lookup functionality |
| 2008 | Update | Added support for international exchanges with exchange prefix syntax |
| 2010 | Update | Introduced historical data capabilities with date parameters |
| 2012 | Update | Added currency conversion functionality (CURRENCY:USDEUR syntax) |
| 2014 | Update | Expanded available attributes including PE, EPS, market cap |
| 2016 | Update | Added 52-week high/low attributes; improved data coverage |
| 2018 | Change | Some mutual fund data deprecated; changes to data sources |
| 2020 | Update | Improved reliability and reduced latency for real-time data |
| 2022 | Update | Enhanced mobile app support; improved error messages |
| 2024 | Update | Expanded international exchange coverage; performance improvements |
