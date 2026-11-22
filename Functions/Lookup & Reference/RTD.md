---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
purpose:
  - Data Import
  - Data Retrieval
use-case:
  - Live Feed Monitoring
  - Live Sensor Readings
  - Market Quote Boards
related:
  - GETPIVOTDATA
  - GOOGLEFINANCE
  - HYPERLINK
  - IMPORTRANGE
  - INDIRECT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/rtd-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Real Time Data
  - Real-Time Data Feed
tags:
  - com-automation
  - excel
  - real-time
---

# RTD

## Description

**RTD** retrieves real-time data from a program that supports COM automation. It connects a worksheet cell to a live data server, such as a market feed, a laboratory instrument or a plant monitoring system, and shows the latest value the server sends for the topics you name.

The data server is a COM automation add-in that must be created and registered on the local computer. You identify it with its ProgID, which is the name it is registered under. If the server is on another computer, you also give its name. The topics describe the piece of data to return, such as an instrument symbol and a field name.

RTD is a specialist function that depends on a locally installed add-in. It is a Microsoft Excel function and is not part of Google Sheets. When a server pushes updates continually, RTD formulas recalculate in automatic calculation mode, unlike most other functions. If no real-time data server is installed, the cell shows `#N/A`.

## Syntax

```excel
=RTD(ProgID, server, topic1, [topic2], ...)
```

<!-- Image 1: RTD Arguments. See Images/Lookup & Reference/RTD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `ProgID` | Yes | The ProgID of the registered COM automation add-in, in quotation marks. |
| `server` | Yes | The name of the computer where the add-in runs, in quotation marks. Leave it empty (`""`) when the add-in runs on the local computer. |
| `topic1` | Yes | The first value that identifies one piece of real-time data. |
| `topic2, ...` | No | Additional topics, up to 253 in total, that together identify the data. |

### Return Value

The latest value the server provides for the topics. The page does not describe the data type in general. When no real-time data server is installed, RTD returns `#N/A`.

## Examples

The examples use `Vendor.Feed.1` as a placeholder ProgID. Replace it with the ProgID of the add-in installed on your computer.

### Example 1: Local Feed, One Topic Pair

```excel
=RTD("Vendor.Feed.1", "", "ACME", "Last")
```

**Result:** The last value that the local feed reports for the ACME instrument. If the feed is not installed, the cell shows `#N/A`.

The empty server argument tells Excel to use the local computer.

### Example 2: Feed on Another Computer

```excel
=RTD("Vendor.Feed.1", "trading-server01", "ACME", "Bid")
```

**Result:** The bid value from the feed running on the computer named `trading-server01`, or `#N/A` when that server cannot supply it.

### Example 3: Topics From Cells

```excel
=RTD("Vendor.Feed.1", "", A2, B2)
```

**Result:** The value for the topic in `A2` and the field in `B2`. Changing either cell changes the topic the formula requests.

Keeping the topics in cells lets people choose what to monitor without editing formulas.

<!-- Image 2: Local and Remote Feeds. See Images/Lookup & Reference/RTD.md -->

## Story Problems

### Problem 1: Plant Temperature Monitor

A plant engineer wants the current temperature of a reactor. The sensor name is in `A2`, the field is in `B2`, and the feed ProgID is `Vendor.Feed.1`.

**Task:** Write the formula so the cell shows "Feed offline" when the feed is not available, and returns the live value otherwise.

**Solution:**

```excel
=IFERROR(RTD("Vendor.Feed.1", "", A2, B2), "Feed offline")
```

**Answer:** On a computer without the feed installed, the cell shows `Feed offline`. On a computer with the feed running, it shows the live reading.

### Problem 2: Quote Board Setup

A trader has two topics for each quote: the symbol in `A2` and the field, such as Last, in `B2`. The feed runs on the server `quotes-01`.

**Task:** Write the formula that requests the quote through that server.

**Solution:**

```excel
=RTD("Vendor.Feed.1", "quotes-01", A2, B2)
```

**Answer:** The formula asks the server named `quotes-01` for the field in `B2` for the symbol in `A2`. Because the server name is quoted, it is passed as text.

## Use Cases

### Live Sensor Readings

**Scenario:** A laboratory tracks the temperature and pressure of an instrument that streams readings to a local data server.

```excel
=RTD("Lab.Sensors.1", "", "Chamber1", "Temperature")
```

**Why It Works:** The server pushes new readings, and RTD recalculates the cell when the value changes, so the sheet reflects the instrument without manual refreshes.

### Quote Board

**Scenario:** A trading desk shows the last trade and bid for a list of symbols on one sheet.

```excel
=RTD("Vendor.Feed.1", "quotes-01", $A2, "Last")
```

**Why It Works:** Each row names its own symbol in column A, and the formula is copied down the sheet to follow the list.

### Feed Health Check

**Scenario:** An operations team wants a quick warning when a monitoring feed stops responding.

```excel
=IF(ISNA(RTD("Plant.Monitor.1", "", "Line3", "Status")), "No feed", "Feed running")
```

**Why It Works:** ISNA catches the `#N/A` that RTD returns when the server is missing, and the cell shows a plain status instead.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | No real-time data server is installed, or the server cannot supply the topic. | Install and register the add-in, and check the topics. |
| `#N/A` with an add-in installed | The ProgID does not match the registered name. | Check the ProgID used in the registry or the add-in documentation. |
| No value from a remote server | The server name is wrong or the computer cannot be reached. | Check the computer name and the network connection. |
| Formula is not updating | Calculation mode is not automatic. | Set Excel to automatic calculation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Requires a COM automation add-in registered on the computer. Up to 253 topic parameters. |
| Google Sheets | Not available | For live market prices, use GOOGLEFINANCE. For other live data, use a connector or an add-on supplied for Sheets. |

## Tips and Best Practices

- Test the ProgID on one cell before copying the formula to many rows.
- Wrap RTD in IFERROR or ISNA when the sheet should show a message instead of `#N/A` while the feed is offline.
- Store topics in cells so people can change them without editing the formula.
- Use an empty server argument for a local feed, and avoid mixing local and remote feeds for the same topic set.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IMPORTRANGE](../Web/IMPORTRANGE.md) | Imports data from another spreadsheet, a different kind of external source. |
| [INDIRECT](INDIRECT.md) | Builds a reference from text, which can supply topics to RTD. |
| [HYPERLINK](HYPERLINK.md) | Creates a link to a page or document rather than live data. |
| [GETPIVOTDATA](GETPIVOTDATA.md) | Retrieves values from a pivot table, a different source of summary data. |
| [GOOGLEFINANCE](../Google-specific/GOOGLEFINANCE.md) | The closest Google Sheets function for live market prices. |

## Official Documentation

- [Microsoft Support: RTD function](https://support.microsoft.com/en-us/excel/functions/rtd-function)
