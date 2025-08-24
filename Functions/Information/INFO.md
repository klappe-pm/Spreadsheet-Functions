---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - information
  - - subTopics
    - []
  - - dateCreated
    - 2025-06-20
  - - dateRevised
    - 2025-08-19
  - - aliases
    - []
  - - tags
    - []
---
# INFO

## INFO Description

Returns information about the current operating environment and system configuration including directories, memory usage, operating system, and spreadsheet application details. Essential for environment-aware formulas, system diagnostics, and cross-platform compatibility.

> [!f(x)] INFO Syntax
>
> ```spreadsheets
> INFO(type_text)
> ```
>
> **Parameters:**
> - `type_text` (required): Text string specifying the type of system information to return

> [!f(x)] INFO Examples
>
> ```spreadsheets
> // Get current directory
> INFO("directory") → "C:\Users\Name\Documents"
> 
> // Check available memory
> INFO("memavail") → 1048576 (available memory in KB)
> 
> // Get operating system
> INFO("osversion") → "Windows (32-bit) 10.0"
> 
> // Find number of worksheets
> INFO("numfile") → 3 (number of worksheets in workbook)
> 
> // Get system origin
> INFO("origin") → "$A$1" (top-left cell reference)
> ```

## Use Cases

### [[System diagnostics]]
- **Performance monitoring**: Check available memory and system resources to optimize formula complexity and data processing
- **Environment validation**: Verify system configuration meets requirements for complex calculations and data operations
- **Capacity planning**: Monitor system resources to prevent memory issues during large data processing operations
- **Troubleshooting**: Identify system limitations that might affect spreadsheet performance and functionality

### [[Cross-platform compatibility]]
- **Operating system detection**: Adapt formulas and file paths based on whether system is Windows, Mac, or other platforms
- **Version compatibility**: Check application version to ensure formula compatibility and feature availability
- **Path management**: Handle file and directory paths appropriately based on operating system conventions
- **Feature detection**: Verify system capabilities before using advanced functions or features

### [[Application automation]]
- **Workbook management**: Track number of worksheets and files for automated processing and navigation
- **Directory operations**: Manage file locations and paths for import/export operations and data processing
- **Resource optimization**: Adjust processing intensity based on available system memory and resources
- **Environment logging**: Record system information for audit trails and troubleshooting documentation

## Related

### Similar Functions

- [[CELL]] - Returns specific cell information, complementing INFO's system-wide information
- [[TODAY]] - Returns current date, part of environment information like INFO but more specific
- [[NOW]] - Returns current date and time, similar system-aware function to INFO
- [[USER]] - Returns current user name in some systems, related to INFO's environment data
- [[VERSION]] - Returns application version in some systems, overlapping with INFO functionality

## Environment Detection Functions

### [[IF]]
INFO combined with IF enables environment-specific processing and conditional logic based on system configuration and capabilities.

```spreadsheets
// Operating system specific logic
=IF(LEFT(INFO("osversion"),7)="Windows", "C:\temp\", "/tmp/")
// Uses appropriate temp directory based on OS

// Memory-based processing decisions
=IF(INFO("memavail")>500000, "Process large dataset", "Use sample data")
// Adjusts data processing based on available memory

// Application version compatibility
=IF(INFO("release")>=16, "Use new functions", "Use legacy functions")
// Adapts formulas based on application version
```

### [[CONCATENATE]]
Works with INFO to build dynamic file paths, system reports, and environment-specific text strings.

```spreadsheets
// Dynamic file path construction
=INFO("directory") & "\backup_" & TEXT(TODAY(),"yyyy-mm-dd") & ".xlsx"
// Creates backup file path with current directory and date

// System information report
="System: " & INFO("osversion") & " | Memory: " & INFO("memavail") & "KB"
// Builds system status summary

// Environment-specific messaging
="Running on " & INFO("osversion") & " with " & INFO("numfile") & " worksheets"
// Creates environment-aware status message
```

## File Management Functions

### [[INDIRECT]]
INFO directory information works with INDIRECT for dynamic file referencing and path-based cell references.

```spreadsheets
// Dynamic file references
=INDIRECT("'[" & INFO("directory") & "\data.xlsx]Sheet1'!A1")
// References external file using current directory

// Path-based range references
=SUM(INDIRECT(INFO("origin") & ":C10"))
// Creates range starting from system origin

// Environment-specific ranges
=IF(INFO("numfile")>1, INDIRECT("Sheet2!A1:A10"), A1:A10)
// References different ranges based on worksheet count
```

### [[HYPERLINK]]
Combines with INFO to create dynamic hyperlinks and file references based on current system environment.

```spreadsheets
// Dynamic directory link
=HYPERLINK(INFO("directory"), "Open Current Directory")
// Creates clickable link to current working directory

// Environment-specific help links
=IF(LEFT(INFO("osversion"),7)="Windows", 
   HYPERLINK("https://support.microsoft.com/excel", "Excel Help"), 
   HYPERLINK("https://support.apple.com/numbers", "Numbers Help"))
// Links to appropriate help based on operating system

// System-specific documentation
=HYPERLINK(INFO("directory") & "\readme.txt", "View Documentation")
// Links to documentation in current directory
```

## System Monitoring Functions

### [[TEXT]]
INFO numeric values work with TEXT for formatted system reporting and readable environment information display.

```spreadsheets
// Formatted memory display
=TEXT(INFO("memavail")/1024, "#,##0.0") & " MB available"
// Converts KB to MB with proper formatting

// System uptime formatting
=IF(INFO("memavail")>0, "System OK - " & TEXT(INFO("memavail"), "#,##0") & "KB free", "System Error")
// Formats system status with memory information

// Performance metrics
="Performance: " & TEXT(INFO("memavail")/1024/1024, "0.00") & "GB RAM | " & INFO("numfile") & " files"
// Creates comprehensive performance summary
```

### [[CHOOSE]]
Works with INFO to select appropriate actions or values based on system configuration and environment state.

```spreadsheets
// OS-specific processing
=CHOOSE(IF(LEFT(INFO("osversion"),7)="Windows",1,2), "Windows processing", "Unix processing")
// Selects processing method based on operating system

// Memory-based performance levels
=CHOOSE(IF(INFO("memavail")<512000,1,IF(INFO("memavail")<1024000,2,3)), 
        "Low memory mode", "Standard mode", "High performance mode")
// Selects performance mode based on available memory

// File count-based operations
=CHOOSE(MIN(INFO("numfile"),3), "Single file mode", "Dual file mode", "Multi file mode")
// Adapts operation based on number of open files
```

## Resource Management Functions

### [[ROUND]]
INFO memory values work with ROUND for cleaned resource reporting and threshold-based system management.

```spreadsheets
// Rounded memory reporting
=ROUND(INFO("memavail")/1024/1024, 1) & " GB available"
// Reports available memory in GB with 1 decimal place

// Resource utilization calculation
=ROUND((INFO("memused")/INFO("memtotal"))*100, 0) & "% memory used"
// Calculates and displays memory utilization percentage

// Performance scoring
=ROUND(INFO("memavail")/100000, 0)
// Creates simple performance score based on available memory
```

### [[MAX]]
Combines with INFO for resource limit checking and system capacity validation before intensive operations.

```spreadsheets
// Memory threshold checking
=IF(INFO("memavail")>MAX(500000, INFO("memavail")*0.1), "Sufficient memory", "Low memory warning")
// Checks if available memory exceeds minimum threshold

// Capacity planning
=MAX(INFO("numfile"), 1) & " worksheets | Recommended max: " & MAX(INFO("memavail")/50000, 10)
// Calculates recommended maximum worksheets based on memory

// Resource optimization
=IF(INFO("memavail")<MAX(256000, INFO("totmem")*0.2), "Reduce data size", "OK to proceed")
// Recommends actions based on memory availability
```

## Commonly Used With Functions Examples

### System Environment Report
```spreadsheets
// Comprehensive system report
="Environment Report:" & CHAR(10) &
 "OS: " & INFO("osversion") & CHAR(10) &
 "Directory: " & INFO("directory") & CHAR(10) &
 "Available Memory: " & TEXT(INFO("memavail")/1024, "#,##0") & " MB" & CHAR(10) &
 "Active Worksheets: " & INFO("numfile") & CHAR(10) &
 "Origin: " & INFO("origin")
// Creates multi-line system information summary

// Performance assessment
=IF(AND(INFO("memavail")>1000000, INFO("numfile")<10),
   "✓ System performance: Excellent",
   IF(AND(INFO("memavail")>500000, INFO("numfile")<20),
      "⚠ System performance: Good", 
      "✗ System performance: Consider optimization"))
// Assesses overall system performance for spreadsheet operations
```

### Cross-Platform File Management
```spreadsheets
// Universal file path builder
=IF(ISERROR(FIND("Windows", INFO("osversion"))),
   INFO("directory") & "/" & "data.csv",
   INFO("directory") & "\" & "data.csv")
// Creates proper file paths for Windows vs Unix systems

// Environment-specific backup location
=IF(LEFT(INFO("osversion"),7)="Windows",
   "C:\Backup\" & TEXT(NOW(),"yyyy-mm-dd-hhmm") & ".xlsx",
   "/backup/" & TEXT(NOW(),"yyyy-mm-dd-hhmm") & ".xlsx")
// Creates OS-appropriate backup file paths with timestamps
```

### Resource-Aware Data Processing
```spreadsheets
// Memory-based data sampling
=IF(INFO("memavail")>2000000,
   "Process full dataset (" & COUNTA(A:A) & " records)",
   "Process sample (" & MIN(COUNTA(A:A), 10000) & " records) - Limited memory")
// Adjusts data processing scope based on available memory

// Dynamic formula complexity
=IF(INFO("memavail")<500000,
   AVERAGE(A1:A100),
   SUMPRODUCT((A1:A1000>AVERAGE(A1:A1000))*(B1:B1000))/SUMPRODUCT(--(A1:A1000>AVERAGE(A1:A1000))))
// Uses simpler formulas when memory is limited, complex formulas when sufficient
```