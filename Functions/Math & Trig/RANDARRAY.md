---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: math & trig
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-17
aliases: []
tags: []
---

# RANDARRAY

## RANDARRAY Description

Generates an array of random numbers with specified dimensions and parameters. More efficient than multiple RAND() calls, supporting both decimal and integer random numbers with optional minimum and maximum bounds for advanced simulation and analysis.

> [!f(x)] RANDARRAY Syntax
>
> ```spreadsheets
> RANDARRAY([rows], [columns], [min], [max], [whole_number])
> ```
>
> **Parameters:**
> - `rows` (optional): Number of rows in array (default: 1)
> - `columns` (optional): Number of columns in array (default: 1)  
> - `min` (optional): Minimum value (default: 0)
> - `max` (optional): Maximum value (default: 1)
> - `whole_number` (optional): TRUE for integers, FALSE for decimals (default: FALSE)

> [!f(x)] RANDARRAY Examples
>
> ```spreadsheets
> // Basic 3x3 array of decimals (0-1)
> RANDARRAY(3, 3) → 3x3 array with values like 0.7341, 0.2854, etc.
> 
> // 5x2 array of integers (1-100)
> RANDARRAY(5, 2, 1, 100, TRUE) → 5x2 array with whole numbers 1-100
> 
> // Single row of 10 random percentages
> RANDARRAY(1, 10, 0, 100) → 1x10 array with decimals 0-100
> 
> // 4x4 array of dice rolls (1-6)
> RANDARRAY(4, 4, 1, 6, TRUE) → 4x4 array with integers 1-6
> 
> // Temperature simulation (-10 to 40 degrees)
> RANDARRAY(7, 1, -10, 40) → 7x1 array with decimals -10 to 40
> ```

## Use Cases

### [[Statistical simulations]]
- **Monte Carlo analysis**: Generate large datasets for financial risk modeling, portfolio optimization, and scenario planning
- **Hypothesis testing**: Create random samples for statistical tests, confidence intervals, and significance analysis
- **Bootstrap sampling**: Generate resampled datasets for robust statistical inference and model validation
- **Distribution modeling**: Simulate various probability distributions for research and business forecasting

### [[Data science applications]]  
- **Machine learning**: Create synthetic training data, test datasets, and validation samples for model development
- **A/B testing**: Generate random user assignments and control groups for experimental design
- **Survey research**: Produce random sampling frames and stratified samples for market research and polling
- **Quality assurance**: Simulate measurement errors, process variations, and testing scenarios

### [[Business modeling]]
- **Sales forecasting**: Generate random demand scenarios for inventory planning and revenue projections
- **Risk assessment**: Model potential losses, market fluctuations, and operational uncertainties
- **Capacity planning**: Simulate resource utilization, queue lengths, and service level variations
- **Game theory**: Create random payoff matrices and strategic scenarios for decision analysis

## Related

### Similar Functions

- [[RAND]] - Generates single random number 0-1, more basic but widely supported across platforms
- [[RANDBETWEEN]] - Creates single random integer in range, simpler syntax for bounded integers
- [[SEQUENCE]] - Generates sequential number arrays, complementary for creating ordered datasets
- [[UNIQUE]] - Removes duplicates from arrays, often used with RANDARRAY for unique random selections
- [[SORT]] - Arranges array data, frequently combined with RANDARRAY for random ordering

## Array Functions

### [[SEQUENCE]]
Complementary to RANDARRAY for creating structured datasets. SEQUENCE provides ordered arrays while RANDARRAY provides random arrays.

```spreadsheets
// Create random data with sequential IDs
=HSTACK(SEQUENCE(10), RANDARRAY(10, 1, 1, 100, TRUE))
// Combines sequential IDs with random values

// Random sampling from sequential data
=INDEX(SEQUENCE(100), RANDARRAY(10, 1, 1, 100, TRUE))
// Randomly selects 10 values from 1-100 sequence

// Paired sequential and random arrays
=VSTACK(SEQUENCE(1, 10), RANDARRAY(1, 10, 0, 100))
// Top row: 1,2,3...10, Bottom row: random 0-100
```

### [[UNIQUE]]
Essential for removing duplicate values from RANDARRAY output, ensuring truly unique random samples.

```spreadsheets
// Generate unique random integers
=UNIQUE(RANDARRAY(20, 1, 1, 100, TRUE))
// Creates unique random integers, removes duplicates

// Unique random selection from dataset
=UNIQUE(INDEX(A2:A1000, RANDARRAY(50, 1, 1, 999, TRUE)))
// Randomly selects unique values from range A2:A1000

// Random unique team assignments
=UNIQUE(RANDARRAY(15, 1, 1, 5, TRUE))
// Assigns unique team numbers 1-5 (some teams may be empty)
```

## Statistical Functions

### [[AVERAGE]]
Frequently used with RANDARRAY to calculate mean values of random samples for statistical analysis and validation.

```spreadsheets
// Average of random sample (should approach expected value)
=AVERAGE(RANDARRAY(1000, 1, 0, 100))
// Average of 1000 random numbers 0-100 (should ≈ 50)

// Compare means across random groups
=AVERAGE(RANDARRAY(100, 3, 1, 10, TRUE))
// Calculates mean of each column in random array

// Monte Carlo mean estimation
=AVERAGE(RANDARRAY(10000, 1, -5, 15))
// Estimates population mean from large random sample
```

### [[STDEV]]
Combined with RANDARRAY to analyze variation and distribution characteristics in simulated datasets.

```spreadsheets
// Standard deviation of random uniform distribution
=STDEV(RANDARRAY(1000, 1, 0, 10))
// Should approximate theoretical std dev = (max-min)/sqrt(12)

// Variability analysis across random samples
=STDEV(RANDARRAY(500, 5, 20, 80))
// Calculates standard deviation for each column

// Quality control simulation
=STDEV(RANDARRAY(200, 1, 98, 102))
// Simulates process variation around target value 100
```

## Commonly Used With Functions Examples

### RANDARRAY with Statistical Analysis
```spreadsheets
// Complete statistical summary of random data
={MIN(A1:A1000), AVERAGE(A1:A1000), MAX(A1:A1000), STDEV(A1:A1000)}
// Where A1:A1000 contains RANDARRAY(1000,1,10,90)

// Confidence interval estimation
=CONFIDENCE.T(0.05, STDEV(B1:B100), COUNT(B1:B100))
// For random sample generated by RANDARRAY
```

### RANDARRAY with Business Simulation
```spreadsheets
// Sales scenario modeling
=SUM(RANDARRAY(12, 1, 50000, 150000))
// Simulates annual sales with monthly randomization

// Resource allocation simulation
=RANDARRAY(10, 3, 5, 25, TRUE)
// Random allocation of resources across 10 projects, 3 categories
```

### RANDARRAY with Data Validation
```spreadsheets
// Generate test data for validation
=HSTACK(RANDARRAY(100,1,1,1000,TRUE), RANDARRAY(100,1,0,1))
// Creates ID and probability columns for testing

// Random quality control samples
=INDEX(C2:C1000, RANDARRAY(50, 1, 1, 999, TRUE))
// Randomly selects 50 items for quality inspection
```
