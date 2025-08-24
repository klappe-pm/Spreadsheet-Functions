---
!!python/object/apply:collections.OrderedDict
- - - categories
    - - spreadsheets
  - - subCategories
    - - excel
      - sheets
  - - topics
    - - excel
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
# SEQUENCE

## SEQUENCE Description

Generates a sequence of numbers in an array format, supporting both single-dimension and multi-dimensional arrays. Creates ordered numeric sequences with customizable start values, step sizes, and array dimensions, essential for dynamic array formulas and data generation.

> [!f(x)] SEQUENCE Syntax
>
> ```spreadsheets
> SEQUENCE(rows, [columns], [start], [step])
> ```
>
> **Parameters:**
> - `rows` (required): Number of rows in the sequence array
> - `columns` (optional): Number of columns in the sequence array (default: 1)
> - `start` (optional): Starting value for the sequence (default: 1)
> - `step` (optional): Step size between consecutive values (default: 1)

> [!f(x)] SEQUENCE Examples
>
> ```spreadsheets
> // Basic sequence from 1 to 10
> SEQUENCE(10) → {1; 2; 3; 4; 5; 6; 7; 8; 9; 10}
> 
> // Custom start and step values
> SEQUENCE(5, 1, 10, 2) → {10; 12; 14; 16; 18}
> 
> // Multi-dimensional array (3 rows, 4 columns)
> SEQUENCE(3, 4) → {1, 2, 3, 4; 5, 6, 7, 8; 9, 10, 11, 12}
> 
> // Date sequence starting from specific date
> SEQUENCE(7, 1, DATE(2024,1,1), 1) → sequential dates for one week
> 
> // Negative step for descending sequence
> SEQUENCE(5, 1, 100, -10) → {100; 90; 80; 70; 60}
> ```

## Use Cases

### [[Data generation]]
- **Time series data**: Generate sequential dates, months, or time intervals for financial modeling, project timelines, and periodic reporting schedules
- **Test data creation**: Create large datasets with sequential ID numbers, sample codes, or incremental values for testing formulas and database operations
- **Index generation**: Build row numbers, reference sequences, and unique identifiers for data organization and lookup operations
- **Pattern creation**: Generate mathematical sequences like Fibonacci numbers, prime number candidates, or custom progressions for analysis

### [[Dynamic arrays]]
- **Array formula foundations**: Create base sequences that serve as inputs for complex array formulas using MAP, FILTER, and other dynamic array functions
- **Spill range management**: Generate predictable array sizes that control how formulas spill across worksheets, ensuring consistent layout and formatting
- **Multi-dimensional data structures**: Build matrices and tables programmatically for mathematical calculations, lookup tables, and data transformation operations
- **Dynamic reporting ranges**: Create flexible data ranges that automatically adjust based on parameters, enabling scalable reports and dashboards

### [[Mathematical operations]]
- **Matrix operations**: Generate coordinate systems, grid references, and structured number patterns for linear algebra and geometric calculations
- **Statistical sampling**: Create evenly spaced intervals for data sampling, histogram bins, and distribution analysis across large datasets
- **Iterative calculations**: Provide step counters and iteration indices for complex mathematical models, optimization algorithms, and simulation processes
- **Coordinate generation**: Build x-y coordinate pairs, grid systems, and spatial references for charting, mapping, and geometric analysis

## Related

### Similar Functions

- [[ROW]] - Returns row numbers for cell references, more limited than SEQUENCE for custom ranges
- [[COLUMN]] - Returns column numbers for cell references, complements SEQUENCE for grid operations
- [[RANDARRAY]] - Creates arrays of random numbers instead of sequential values
- [[MAKEARRAY]] - Generates arrays using custom logic with LAMBDA functions
- [[SERIES]] - Creates series in charts, different application than SEQUENCE

## Array Generation Functions

### [[RANDARRAY]]
Often combined with SEQUENCE to create structured random data sets where sequential indices are paired with random values for testing and simulation purposes.

```spreadsheets
// Create indexed random data with SEQUENCE and RANDARRAY
=HSTACK(SEQUENCE(100), RANDARRAY(100, 1, 1, 1000))
// Generates 100 rows with ID numbers and random values

// Generate random dates within a sequential month structure
=SEQUENCE(12, 1, DATE(2024,1,1), 30) + RANDARRAY(12, 1, 0, 29)
// Creates random dates in each month of 2024

// Build test dataset with sequential and random components
=HSTACK(
   "ID-"&SEQUENCE(50),
   RANDARRAY(50, 1, 18, 65),
   RANDARRAY(50, 1, 25000, 100000))
// Creates IDs, random ages, and random salaries
```

### [[MAKEARRAY]]
Pairs with SEQUENCE to create complex array patterns where SEQUENCE provides the structure and MAKEARRAY applies custom logic to each position.

```spreadsheets
// Create multiplication table using SEQUENCE and MAKEARRAY
=MAKEARRAY(10, 10, LAMBDA(r, c, INDEX(SEQUENCE(10), r) * INDEX(SEQUENCE(10), c)))
// 10x10 multiplication table

// Generate compound interest table with SEQUENCE years
=MAKEARRAY(ROWS(SEQUENCE(20)), 1, 
   LAMBDA(r, c, principal * (1 + rate)^INDEX(SEQUENCE(20), r)))
// 20-year compound interest projection

// Create custom calendar grid with SEQUENCE
=MAKEARRAY(6, 7, LAMBDA(week, day, 
   DATE(year, month, 1) + (week-1)*7 + day - WEEKDAY(DATE(year, month, 1))))
// Monthly calendar with proper date alignment
```

## Data Processing Functions

### [[FILTER]]
Uses SEQUENCE to create dynamic filter conditions and index-based data selection, enabling sophisticated data extraction based on position and pattern.

```spreadsheets
// Filter every nth row using SEQUENCE
=FILTER(data_range, MOD(SEQUENCE(ROWS(data_range)), 5) = 0)
// Returns every 5th row from the data range

// Select data based on sequential conditions
=FILTER(sales_data, SEQUENCE(ROWS(sales_data)) <= target_count)
// Returns top N rows based on SEQUENCE limit

// Create alternating row pattern filter
=FILTER(employee_data, MOD(SEQUENCE(ROWS(employee_data)), 2) = 1)
// Returns odd-numbered rows for alternating selection
```

### [[MAP]]
Applies SEQUENCE-generated indices to perform position-based transformations across arrays, enabling complex data manipulation based on row/column positions.

```spreadsheets
// Apply different calculations based on position using SEQUENCE
=MAP(SEQUENCE(12), LAMBDA(month, 
   IF(month<=6, base_value*0.8, base_value*1.2)))
// Different rates for first and second half of year

// Create progressive scaling based on sequence position
=MAP(data_array, SEQUENCE(ROWS(data_array)), 
   LAMBDA(value, position, value * (1 + position*0.01)))
// Apply increasing scaling factor by position

// Generate formatted output with sequential numbering
=MAP(names_array, SEQUENCE(ROWS(names_array)), 
   LAMBDA(name, num, num & ". " & name))
// Creates numbered list from names array
```

## Date and Time Functions

### [[DATE]]
Combines with SEQUENCE to generate date ranges, calendar systems, and time-based sequences for financial and project planning applications.

```spreadsheets
// Generate business days for a quarter using SEQUENCE and DATE
=FILTER(DATE(2024,1,1) + SEQUENCE(90), 
   WEEKDAY(DATE(2024,1,1) + SEQUENCE(90), 2) <= 5)
// Returns only weekdays (Monday-Friday) for 90 days

// Create monthly reporting dates for entire year
=DATE(2024, SEQUENCE(12), 1)
// First day of each month in 2024

// Generate weekly date sequence for project timeline
=DATE(2024,1,1) + (SEQUENCE(52)-1)*7
// Every Monday for one year starting from specific date
```

### [[WORKDAY]]
Works with SEQUENCE to create business day sequences, project schedules, and work calendar systems excluding weekends and holidays.

```spreadsheets
// Generate 30 business days using SEQUENCE
=MAP(SEQUENCE(30), LAMBDA(n, WORKDAY(start_date, n-1)))
// Creates 30 consecutive business days

// Create milestone dates at regular business day intervals
=MAP(SEQUENCE(10), LAMBDA(milestone, 
   WORKDAY(project_start, milestone*5)))
// Project milestones every 5 business days

// Build quarterly business day reporting schedule
=MAP(SEQUENCE(4), LAMBDA(quarter, 
   WORKDAY(EOMONTH(DATE(2024,1,1), quarter*3-3), 1)))
// First business day of each quarter
```

## Commonly Used With Functions Examples

### Dynamic Data Analysis Dashboard
```spreadsheets
// Create a comprehensive data analysis system with SEQUENCE
=LET(
   months, SEQUENCE(12),
   dates, DATE(2024, months, 1),
   sales_data, MAP(months, LAMBDA(m, base_sales * (1 + SIN(m/2)))),
   growth_rates, MAP(SEQUENCE(11), LAMBDA(m, 
     (INDEX(sales_data, m+1) - INDEX(sales_data, m)) / INDEX(sales_data, m))),
   ytd_totals, SCAN(0, sales_data, LAMBDA(acc, val, acc + val)),
   dashboard, VSTACK(
     HSTACK("Month", "Date", "Sales", "Growth%", "YTD Total"),
     HSTACK(months, TEXT(dates, "mmm-yyyy"), sales_data, 
            VSTACK(0, growth_rates), ytd_totals)),
   dashboard)
```

### Financial Planning with Progressive Analysis
```spreadsheets
// Build a comprehensive investment growth model
=LAMBDA(initial_amount, annual_rate, years, additional_monthly,
   LET(
     year_sequence, SEQUENCE(years),
     month_sequence, SEQUENCE(years*12),
     monthly_rate, annual_rate/12,
     monthly_contributions, MAP(month_sequence, LAMBDA(m, additional_monthly)),
     compound_growth, SCAN(initial_amount, month_sequence,
       LAMBDA(balance, month,
         balance * (1 + monthly_rate) + additional_monthly)),
     annual_snapshots, MAP(year_sequence, LAMBDA(year, 
       INDEX(compound_growth, year*12))),
     annual_contributions, year_sequence * 12 * additional_monthly,
     total_contributions, initial_amount + annual_contributions,
     growth_amounts, annual_snapshots - total_contributions,
     summary_table, VSTACK(
       HSTACK("Year", "Balance", "Contributions", "Growth", "Growth%"),
       HSTACK(year_sequence, 
              TEXT(annual_snapshots, "$#,##0"),
              TEXT(total_contributions, "$#,##0"),
              TEXT(growth_amounts, "$#,##0"),
              TEXT(growth_amounts/total_contributions, "0.0%"))),
     summary_table))
```

### Advanced Project Management Timeline
```spreadsheets
// Create a dynamic project timeline with dependencies
=LET(
   task_count, 15,
   task_ids, SEQUENCE(task_count),
   start_date, DATE(2024, 1, 15),
   base_durations, RANDARRAY(task_count, 1, 3, 20),
   dependency_matrix, IF(RANDARRAY(task_count, task_count) > 0.7, task_ids, 0),
   
   // Calculate start dates considering dependencies
   calculated_starts, SCAN(start_date, task_ids, 
     LAMBDA(prev_date, task,
       MAX(prev_date,
           MAX(IF(INDEX(dependency_matrix, task, 0) > 0,
                  INDEX(calculated_starts, INDEX(dependency_matrix, task, 0)) + 
                  INDEX(base_durations, INDEX(dependency_matrix, task, 0)),
                  start_date))))),
   
   end_dates, calculated_starts + base_durations,
   work_days, MAP(calculated_starts, base_durations, LAMBDA(start, duration,
     NETWORKDAYS(start, start + duration))),
   
   milestone_dates, MAP(FILTER(task_ids, MOD(task_ids, 5) = 0), 
     LAMBDA(milestone_task, INDEX(end_dates, milestone_task))),
   
   project_timeline, VSTACK(
     HSTACK("Task ID", "Start Date", "Duration", "End Date", "Work Days", "Critical?"),
     HSTACK(task_ids,
            TEXT(calculated_starts, "mm/dd/yyyy"),
            base_durations,
            TEXT(end_dates, "mm/dd/yyyy"),
            work_days,
            IF(end_dates = MAX(end_dates), "CRITICAL", "Normal"))),
   
   project_timeline)
```