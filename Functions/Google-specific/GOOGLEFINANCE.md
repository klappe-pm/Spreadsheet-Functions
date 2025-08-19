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

# GOOGLEFINANCE

## GOOGLEFINANCE Description

Retrieves real-time and historical financial market data from Google Finance directly into Google Sheets. Provides access to stock prices, currency exchange rates, mutual fund data, and market indices with automatic updates, eliminating manual data entry for financial analysis and portfolio management.

> [!f(x)] GOOGLEFINANCE Syntax
>
> ```spreadsheets
> GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date|num_days], [interval])
> ```
>
> **Parameters:**
> - `ticker` (required): Stock symbol, mutual fund symbol, or currency pair (e.g., "AAPL", "CURRENCY:USDEUR")
> - `attribute` (optional): Data type - "price", "volume", "high", "low", "open", "close", "change", etc.
> - `start_date` (optional): Start date for historical data (for historical queries only)
> - `end_date|num_days` (optional): End date or number of days for historical data
> - `interval` (optional): Data frequency - "DAILY" or "WEEKLY" for historical data

> [!f(x)] GOOGLEFINANCE Examples
>
> ```spreadsheets
> // Current stock price
> GOOGLEFINANCE("AAPL", "price") → returns current Apple stock price
> 
> // Multiple stock attributes
> GOOGLEFINANCE("GOOGL", "volume") → returns current Google trading volume
> 
> // Currency exchange rate
> GOOGLEFINANCE("CURRENCY:USDEUR") → returns USD to EUR exchange rate
> 
> // Historical stock data
> GOOGLEFINANCE("MSFT", "close", DATE(2024,1,1), DATE(2024,12,31), "DAILY") → Microsoft daily closes for 2024
> 
> // Market index data
> GOOGLEFINANCE(".INX", "price") → returns S&P 500 index current value
> ```

## Use Cases

### [[Portfolio management]]
- **Real-time portfolio valuation**: Track portfolio value automatically with live stock prices and currency rates
- **Performance analysis**: Calculate portfolio returns, gains/losses, and performance metrics using historical price data
- **Asset allocation monitoring**: Monitor portfolio diversification and rebalancing needs with current market values
- **Risk management**: Track volatility, beta, and other risk metrics using historical price and volume data

### [[Investment research]]  
- **Stock screening**: Compare multiple stocks using price, volume, market cap, and other financial metrics automatically
- **Technical analysis**: Build charts and indicators using historical price data, moving averages, and trading volumes
- **Market comparison**: Analyze stocks against market indices and sector benchmarks with real-time data feeds
- **Fundamental analysis**: Combine market data with financial ratios and performance metrics for investment decisions

### [[Financial reporting]]
- **Executive dashboards**: Create real-time financial dashboards showing portfolio performance and market conditions
- **Automated reporting**: Generate daily, weekly, or monthly investment reports with current market valuations
- **Currency hedging**: Monitor foreign exchange exposure and hedge effectiveness for international investments
- **Compliance monitoring**: Track investment guidelines compliance with automatic position sizing and limit monitoring

## Related

### Similar Functions

- [[IMPORTDATA]] - Imports CSV financial data from external sources, complementary to GOOGLEFINANCE for specialized data
- [[IMPORTXML]] - Extracts financial data from web pages when GOOGLEFINANCE doesn't cover specific metrics
- [[IMPORTHTML]] - Imports financial tables from web pages for data not available through GOOGLEFINANCE
- [[QUERY]] - Filters and analyzes GOOGLEFINANCE data with SQL-like syntax for complex reporting
- [[ARRAYFORMULA]] - Processes multiple GOOGLEFINANCE calls efficiently for portfolio analysis

## Financial Calculation Functions

### [[SUM]]
Essential for portfolio calculations and aggregating financial data from multiple GOOGLEFINANCE calls. Creates portfolio totals and financial summaries.

```spreadsheets
// Portfolio value calculation
=SUM(B2:B10*ARRAYFORMULA(GOOGLEFINANCE(A2:A10,"price")))
// Calculates total portfolio value using shares * current prices

// Currency-adjusted portfolio
=SUM(C2:C5*GOOGLEFINANCE(A2:A5,"price")*GOOGLEFINANCE("CURRENCY:"&D2:D5&"USD"))
// Sums international holdings converted to USD

// Sector allocation totals
=SUMIF(E2:E20,"Technology",F2:F20*ARRAYFORMULA(GOOGLEFINANCE(A2:A20,"price")))
// Sums technology sector holdings value
```

### [[AVERAGE]]
Combined with GOOGLEFINANCE for calculating average prices, returns, and performance metrics across time periods and portfolios.

```spreadsheets
// Average portfolio return
=AVERAGE((ARRAYFORMULA(GOOGLEFINANCE(A2:A10,"price"))-B2:B10)/B2:B10*100)
// Calculates average percentage return across holdings

// Moving average calculation
=AVERAGE(GOOGLEFINANCE("AAPL","close",TODAY()-30,30,"DAILY"))
// 30-day moving average for Apple stock

// Portfolio beta calculation
=AVERAGE(GOOGLEFINANCE(A2:A10,"beta"))
// Average beta across portfolio holdings
```

## Date and Time Functions

### [[TODAY]]
Frequently used with GOOGLEFINANCE for dynamic date ranges and real-time financial analysis that updates automatically each day.

```spreadsheets
// Year-to-date performance
=GOOGLEFINANCE("SPY","close",DATE(YEAR(TODAY()),1,1),TODAY(),"DAILY")
// SPY performance from beginning of current year

// Last 30 days price history
=GOOGLEFINANCE("TSLA","close",TODAY()-30,TODAY(),"DAILY")
// Tesla price history for last month

// Monthly performance tracking
=GOOGLEFINANCE("BTC-USD","close",EOMONTH(TODAY(),-1)+1,TODAY(),"DAILY")
// Bitcoin performance for current month
```

### [[DATE]]
Used with GOOGLEFINANCE for specific historical analysis and backtesting investment strategies with precise date ranges.

```spreadsheets
// Specific period analysis
=GOOGLEFINANCE("QQQ","close",DATE(2023,1,1),DATE(2023,12,31),"WEEKLY")
// NASDAQ ETF weekly closes for 2023

// Earnings period analysis
=GOOGLEFINANCE("AAPL","volume",DATE(2024,1,25),DATE(2024,2,5),"DAILY")
// Apple trading volume around earnings announcement

// Market crash analysis
=GOOGLEFINANCE(".DJI","close",DATE(2020,2,15),DATE(2020,4,15),"DAILY")
// Dow Jones during COVID-19 market crash
```

## Conditional Logic Functions

### [[IF]]
Essential for financial analysis with GOOGLEFINANCE, enabling conditional calculations based on market conditions and portfolio metrics.

```spreadsheets
// Stop-loss monitoring
=IF(GOOGLEFINANCE("AAPL","price")<B2*0.9,"SELL SIGNAL","HOLD")
// Triggers sell signal if stock drops 10% below purchase price

// Portfolio rebalancing alerts
=IF(GOOGLEFINANCE("GOOGL","price")*C2/D2>0.15,"REBALANCE - OVERWEIGHT","OK")
// Alerts when position exceeds 15% of portfolio

// Market timing signals
=IF(GOOGLEFINANCE(".INX","change")>2,"STRONG UP DAY",IF(GOOGLEFINANCE(".INX","change")<-2,"STRONG DOWN DAY","NORMAL"))
// Categorizes market days based on S&P 500 performance
```

### [[IFERROR]]
Critical for handling GOOGLEFINANCE data availability issues and providing fallback values when market data is unavailable.

```spreadsheets
// Data availability fallback
=IFERROR(GOOGLEFINANCE("PRIVATE-STOCK","price"),"Not Available - Private Company")
// Handles stocks not available in Google Finance

// Historical data gaps
=IFERROR(GOOGLEFINANCE("DELISTED","close",TODAY()-365,TODAY()),0)
// Returns 0 for delisted or unavailable historical data

// Currency rate backup
=IFERROR(GOOGLEFINANCE("CURRENCY:USDEUR"),IMPORTDATA("https://api.exchangerate.com/v4/latest/USD"))
// Falls back to external source if Google Finance currency fails
```

## Array Processing Functions

### [[ARRAYFORMULA]]
Powerful combination with GOOGLEFINANCE for processing multiple securities simultaneously and creating dynamic portfolio analysis.

```spreadsheets
// Multi-stock price lookup
=ARRAYFORMULA(GOOGLEFINANCE(A2:A20,"price"))
// Gets current prices for all stocks in range

// Portfolio performance calculation
=ARRAYFORMULA(IF(A2:A50="","",GOOGLEFINANCE(A2:A50,"price")*B2:B50))
// Calculates position values for entire portfolio

// Currency conversion array
=ARRAYFORMULA(IF(C2:C20="","",GOOGLEFINANCE(A2:A20,"price")*GOOGLEFINANCE("CURRENCY:"&C2:C20&"USD")))
// Converts international stock prices to USD
```

### [[QUERY]]
Combines with GOOGLEFINANCE for sophisticated financial analysis and reporting with SQL-like filtering and aggregation.

```spreadsheets
// Portfolio analysis with QUERY
=QUERY(ARRAYFORMULA({A2:A20,GOOGLEFINANCE(A2:A20,"price"),B2:B20,C2:C20}), 
       "SELECT Col1, Col2, Col3*Col2, Col4 WHERE Col2 IS NOT NULL ORDER BY Col3*Col2 DESC")
// Analyzes portfolio by position value

// Sector performance comparison
=QUERY(ARRAYFORMULA({D2:D20,GOOGLEFINANCE(A2:A20,"changepct")}), 
       "SELECT Col1, AVG(Col2) GROUP BY Col1 ORDER BY AVG(Col2) DESC")
// Average sector performance from individual stock returns

// Top performers identification
=QUERY(ARRAYFORMULA({A2:A20,GOOGLEFINANCE(A2:A20,"changepct")}), 
       "SELECT * WHERE Col2 > 5 ORDER BY Col2 DESC")
// Stocks with more than 5% daily gain
```

## Text Processing Functions

### [[CONCATENATE]]
Used with GOOGLEFINANCE for creating formatted financial reports and combining market data with descriptive text.

```spreadsheets
// Portfolio status reporting
=CONCATENATE("Portfolio value: $", TEXT(SUM(B2:B10*ARRAYFORMULA(GOOGLEFINANCE(A2:A10,"price"))),"#,##0.00"), 
             " | Daily change: ", TEXT(SUM(B2:B10*ARRAYFORMULA(GOOGLEFINANCE(A2:A10,"change"))),"$#,##0.00"))
// Complete portfolio summary with formatting

// Stock alert messages
=CONCATENATE(A2, " is trading at $", GOOGLEFINANCE(A2,"price"), 
             " (", GOOGLEFINANCE(A2,"changepct"), "% ", IF(GOOGLEFINANCE(A2,"changepct")>0,"UP","DOWN"), ")")
// Formatted stock status with direction

// Market summary
=CONCATENATE("S&P 500: ", GOOGLEFINANCE(".INX","price"), " (", GOOGLEFINANCE(".INX","changepct"), "%) | ",
             "NASDAQ: ", GOOGLEFINANCE(".IXIC","price"), " (", GOOGLEFINANCE(".IXIC","changepct"), "%)")
// Multi-index market summary
```

### [[TEXT]]
Essential for formatting GOOGLEFINANCE numerical data into readable financial reports and presentations.

```spreadsheets
// Currency formatting for prices
=TEXT(GOOGLEFINANCE("AAPL","price"),"$#,##0.00")
// Formats Apple stock price as currency

// Percentage formatting for changes
=TEXT(GOOGLEFINANCE("MSFT","changepct"),"+0.00%;-0.00%;0.00%")
// Formats Microsoft percentage change with + sign for gains

// Volume formatting
=TEXT(GOOGLEFINANCE("TSLA","volume"),"#,##0,") & "K shares"
// Formats Tesla volume in thousands with label
```

## Commonly Used With Functions Examples

### Real-Time Portfolio Dashboard
```spreadsheets
// Complete portfolio tracking system
=ARRAYFORMULA(
  IF(A2:A20="", "", 
     {A2:A20, 
      GOOGLEFINANCE(A2:A20,"price"), 
      B2:B20, 
      GOOGLEFINANCE(A2:A20,"price")*B2:B20,
      (GOOGLEFINANCE(A2:A20,"price")-C2:C20)/C2:C20*100,
      TEXT(GOOGLEFINANCE(A2:A20,"changepct"),"+0.00%;-0.00%")}))
// Shows symbol, current price, shares, value, gain/loss %, daily change %
```

### Market Analysis Dashboard
```spreadsheets
// Multi-index market overview
=QUERY(ARRAYFORMULA({
  {"Index","Current","Change $","Change %","Volume"};
  {"S&P 500",GOOGLEFINANCE(".INX","price"),GOOGLEFINANCE(".INX","change"),GOOGLEFINANCE(".INX","changepct"),GOOGLEFINANCE(".INX","volume")};
  {"NASDAQ",GOOGLEFINANCE(".IXIC","price"),GOOGLEFINANCE(".IXIC","change"),GOOGLEFINANCE(".IXIC","changepct"),GOOGLEFINANCE(".IXIC","volume")};
  {"Dow Jones",GOOGLEFINANCE(".DJI","price"),GOOGLEFINANCE(".DJI","change"),GOOGLEFINANCE(".DJI","changepct"),GOOGLEFINANCE(".DJI","volume")}
}), "SELECT * WHERE Col2 IS NOT NULL")
// Comprehensive market indices dashboard
```

### Currency-Adjusted International Portfolio
```spreadsheets
// Multi-currency portfolio valuation
=SUMPRODUCT(
  ARRAYFORMULA(GOOGLEFINANCE(A2:A10,"price")),
  B2:B10,
  ARRAYFORMULA(IF(C2:C10="USD",1,GOOGLEFINANCE("CURRENCY:"&C2:C10&"USD"))))
// Portfolio value with automatic currency conversion to USD
```

### Historical Performance Analysis
```spreadsheets
// 5-year performance comparison
=ARRAYFORMULA({
  A2:A10,
  (GOOGLEFINANCE(A2:A10,"price")-GOOGLEFINANCE(A2:A10,"price",TODAY()-365*5,1))/GOOGLEFINANCE(A2:A10,"price",TODAY()-365*5,1)*100,
  (GOOGLEFINANCE(A2:A10,"price")-GOOGLEFINANCE(A2:A10,"price",TODAY()-365,1))/GOOGLEFINANCE(A2:A10,"price",TODAY()-365,1)*100,
  GOOGLEFINANCE(A2:A10,"changepct")
})
// 5-year return, 1-year return, and daily change for stock comparison
```

### Risk Management System
```spreadsheets
// Portfolio risk monitoring
=ARRAYFORMULA(
  IF(A2:A20="", "", 
     IF(GOOGLEFINANCE(A2:A20,"price")/C2:C20<0.9, "STOP LOSS - "&TEXT(GOOGLEFINANCE(A2:A20,"price"),"$0.00"),
        IF(GOOGLEFINANCE(A2:A20,"price")*B2:B20/SUMPRODUCT(GOOGLEFINANCE(A2:A20,"price"),B2:B20)>0.15, "OVERWEIGHT - "&TEXT(GOOGLEFINANCE(A2:A20,"price")*B2:B20,"$#,##0"),
           "OK"))))
// Automated stop-loss and position size alerts
```
