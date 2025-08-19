---
categories: spreadsheets
subCategories: 
  - excel
  - sheets
topics: database
subTopics: []
dateCreated: 2025-06-20
dateRevised: 2025-08-19
aliases: []
tags: []
---

# DGET

## DGET Description

Retrieves a single value from a database that matches specified criteria by evaluating records against multiple conditions. DGET works with structured data where the first row contains field headers and subsequent rows contain data records. Returns an error if no records match or if multiple records match the criteria.

> [!f(x)] DGET Syntax
>
> ```spreadsheets
> DGET(database, field, criteria)
> ```
>
> **Parameters:**
> - `database` (required): The range of cells that makes up the database or list including headers
> - `field` (required): Column to retrieve value from - can be column label (in quotes) or column number  
> - `criteria` (required): Range containing conditions that specify which record to retrieve

> [!f(x)] DGET Examples
>
> ```spreadsheets
> // Get employee name where ID = "E001"
> DGET(A1:E20, "Name", G1:G2) → "John Smith"
> 
> // Get price where product = "Laptop" and model = "Pro"
> DGET(A1:F100, "Price", H1:I3) → 1299.99
> 
> // Get customer phone where account number matches
> DGET(Database, "Phone", AccountCriteria) → "555-0123"
> 
> // Get project status where ID = "P2024-001"
> DGET(A1:D50, "Status", F1:F2) → "In Progress"
> 
> // Get salary where employee = "Jane Doe"
> DGET(Employees, "Salary", NameCriteria) → 75000
> ```

## Use Cases

### [[Record lookup]]
- **Customer information retrieval**: Get specific customer details like phone numbers, addresses, or account status using unique identifiers for CRM and support systems
- **Product specification lookup**: Retrieve detailed product information including prices, descriptions, or inventory levels using product codes or names
- **Employee record access**: Look up specific employee data such as salaries, departments, or contact information using employee IDs or names
- **Transaction detail extraction**: Get specific transaction information like amounts, dates, or payment methods using transaction IDs or reference numbers
- **Configuration value retrieval**: Access specific system settings, parameters, or configuration values using setting names or categories

### [[Data validation]]
- **Unique constraint verification**: Ensure data integrity by checking if specific combinations of criteria return exactly one record, preventing duplicates
- **Reference integrity checking**: Validate that foreign keys exist in reference tables by attempting to retrieve related records
- **Data completeness validation**: Verify that all required related data exists by checking for successful DGET retrievals across related tables
- **Business rule enforcement**: Validate complex business rules by retrieving related data and checking against established constraints
- **Master data consistency**: Ensure consistency between related data elements by comparing retrieved values against expected patterns

### [[Automated reporting]]
- **Dynamic report population**: Automatically populate report fields with current data by retrieving specific values based on report parameters or filters
- **Dashboard data feeds**: Supply real-time data to dashboard widgets by retrieving current metrics, status indicators, or key performance values
- **Alert system data**: Get specific data points for monitoring systems that trigger alerts when certain conditions are met
- **Scheduled report generation**: Retrieve specific data elements for automated reports that run on scheduled intervals
- **Executive summary creation**: Pull key metrics and status information for executive dashboards and summary reports

## Related

### Similar Functions

- [[VLOOKUP]] - Looks up values by searching in first column of range and returning value from specified column
- [[INDEX]] + [[MATCH]] - Combination that provides similar lookup functionality with more flexibility
- [[XLOOKUP]] - Modern lookup function with more features and flexibility than VLOOKUP
- [[DSUM]] - Sums values instead of retrieving single value for database records matching criteria
- [[DCOUNT]] - Counts records instead of retrieving single value for database records matching criteria

## Database Lookup Functions

### [[VLOOKUP]]
Alternative to DGET for simpler single-criterion lookups. VLOOKUP searches first column while DGET handles complex multi-field databases with multiple criteria and can retrieve from any field.

```spreadsheets
// Compare DGET vs VLOOKUP approaches
=DGET(A1:E100,"Price",G1:G2) & " (DGET with criteria) vs " & VLOOKUP("SKU123",A1:E100,4,FALSE) & " (VLOOKUP)"
// Shows difference between database lookup with criteria and simple vertical lookup

// Method selection based on lookup complexity
=IF(ROWS(CriteriaRange)>2, DGET(Database,"Value",CriteriaRange), VLOOKUP(SearchKey,LookupRange,ColumnIndex,FALSE))
// Uses DGET for complex criteria, VLOOKUP for simple single-key lookups

// Cross-validation between DGET and VLOOKUP
=IF(DGET(Data,"Amount",SingleCriteria)=VLOOKUP(KeyValue,LookupTable,AmountColumn,FALSE), "Lookup verified", "Results differ")
// Validates DGET accuracy against VLOOKUP for single-criteria scenarios
```

### [[INDEX]] + [[MATCH]]
Powerful combination that provides similar functionality to DGET but with different syntax and flexibility. Can be used as alternative when DGET criteria become complex.

```spreadsheets
// Compare DGET vs INDEX/MATCH approaches
=DGET(A1:D100,"Name",F1:F2) & " vs " & INDEX(NameRange,MATCH(SearchValue,KeyRange,0))
// Shows database lookup versus array-based lookup methods

// Flexible lookup using INDEX/MATCH for multiple criteria
=INDEX(ResultRange,MATCH(1,(Criteria1Range=Value1)*(Criteria2Range=Value2),0))
// Array formula alternative to DGET for multiple criteria matching

// Error handling comparison
=IFERROR(DGET(Database,"Field",Criteria),"Not found") & " vs " & IFERROR(INDEX(Results,MATCH(Key,Keys,0)),"Not found")
// Shows error handling approaches for both lookup methods
```

## Data Retrieval Functions

### [[XLOOKUP]]
Modern alternative to DGET for advanced lookup scenarios. XLOOKUP offers more features but DGET excels with database-style multi-criteria filtering.

```spreadsheets
// Compare DGET database approach vs XLOOKUP
=DGET(A1:E100,"Price",CriteriaRange) & " vs " & XLOOKUP(SearchKey,KeyColumn,PriceColumn,"Not Found")
// Database criteria filtering versus direct array lookup

// Multi-criteria simulation with XLOOKUP
=XLOOKUP(1,(ProductRange="Laptop")*(ModelRange="Pro"),PriceRange,"Not found")
// XLOOKUP array approach to simulate DGET multi-criteria functionality

// Method selection based on data structure
=IF(ISRANGE(CriteriaRange), DGET(Database,"Value",CriteriaRange), XLOOKUP(Key,KeyRange,ValueRange))
// Uses DGET for structured database queries, XLOOKUP for simple key-value lookups
```

## Error Handling Functions

### [[IFERROR]]
Critical companion to DGET for handling cases where no records match criteria or multiple records are found. DGET returns errors in these cases, requiring proper error handling.

```spreadsheets
// Graceful error handling for DGET operations
=IFERROR(DGET(A1:E100,"CustomerName",G1:G2), "Customer not found")
// Provides user-friendly message when DGET cannot find matching record

// Multiple fallback strategies
=IFERROR(DGET(Current,"Value",Criteria), IFERROR(DGET(Archive,"Value",Criteria), "No data available"))
// Tries current data first, falls back to archive, then shows appropriate message

// Validation with specific error messages
=IF(DCOUNT(Database,"ID",Criteria)=0, "No matching records", 
   IF(DCOUNT(Database,"ID",Criteria)>1, "Multiple matches found - refine criteria", 
      DGET(Database,"Value",Criteria)))
// Provides specific error messages based on whether zero, one, or multiple records match
```

### [[ISERROR]]
Used with DGET to detect lookup failures and implement conditional logic based on whether records are found successfully.

```spreadsheets
// Conditional processing based on DGET success
=IF(ISERROR(DGET(A1:D100,"Status",Criteria)), "Process manual lookup", "Status: " & DGET(A1:D100,"Status",Criteria))
// Takes different actions based on whether DGET succeeds or fails

// Data availability checking
=IF(ISERROR(DGET(Inventory,"Quantity",ItemCriteria)), "Item not in inventory", 
   IF(DGET(Inventory,"Quantity",ItemCriteria)<10, "Low stock alert", "Stock adequate"))
// Checks availability first, then evaluates stock levels if item exists

// Fallback data source selection
=IF(NOT(ISERROR(DGET(PrimaryDB,"Value",Criteria))), DGET(PrimaryDB,"Value",Criteria), DGET(BackupDB,"Value",Criteria))
// Uses primary database if available, otherwise falls back to backup database
```

## Conditional Logic Functions

### [[IF]]
Essential for conditional data retrieval and processing DGET results. IF enables DGET to work with dynamic criteria and provide contextual results based on retrieved values.

```spreadsheets
// Conditional retrieval with business logic
=IF(DGET(A1:E100,"Department",EmpCriteria)="Sales", DGET(A1:E100,"Commission",EmpCriteria), "No commission")
// Only retrieves commission rate if employee is in sales department

// Dynamic pricing based on customer tier
=IF(DGET(Customers,"Tier",CustCriteria)="VIP", DGET(Products,"VIPPrice",ProdCriteria), DGET(Products,"RegularPrice",ProdCriteria))
// Retrieves different price based on customer status

// Status-dependent action determination
=IF(DGET(Projects,"Status",ProjCriteria)="Active", "Continue monitoring", "Archive project")
// Determines action based on current project status retrieved from database
```

## Commonly Used With Functions Examples

### Customer Service Dashboard
```spreadsheets
// Complete customer profile with related data retrieval
="Customer: " & DGET(Customers,"Name",CustCriteria) & 
" | Phone: " & DGET(Customers,"Phone",CustCriteria) & 
" | Tier: " & DGET(Customers,"Tier",CustCriteria) &
" | Last Order: $" & DGET(Orders,"Amount",LastOrderCriteria) & " on " & DGET(Orders,"Date",LastOrderCriteria) &
" | Status: " & IF(DGET(Customers,"Status",CustCriteria)="Active","✓","⚠") &
" | Support Priority: " & IF(DGET(Customers,"Tier",CustCriteria)="VIP","High","Standard")
// Comprehensive customer information retrieval for support agents

// Issue escalation with customer context
="Ticket #" & DGET(Tickets,"ID",TicketCriteria) & 
" | Customer: " & DGET(Customers,"Name",CustomerLookup) & " (" & DGET(Customers,"Tier",CustomerLookup) & ")" &
" | Issue: " & DGET(Tickets,"Category",TicketCriteria) & " - " & DGET(Tickets,"Subject",TicketCriteria) &
" | Assigned: " & DGET(Tickets,"Agent",TicketCriteria) & 
" | Escalate: " & IF(DGET(Tickets,"Priority",TicketCriteria)="Critical","Immediate","Standard")
// Ticket information with customer context for escalation decisions
```

### Inventory Management System
```spreadsheets
// Product availability with supplier information
="Product: " & DGET(Products,"Name",ProductCriteria) & 
" | SKU: " & DGET(Products,"SKU",ProductCriteria) &
" | Stock: " & DGET(Inventory,"Quantity",SKUCriteria) & " units" &
" | Supplier: " & DGET(Suppliers,"Name",SupplierCriteria) & 
" | Lead Time: " & DGET(Suppliers,"LeadDays",SupplierCriteria) & " days" &
" | Status: " & IF(DGET(Inventory,"Quantity",SKUCriteria)<DGET(Products,"MinStock",ProductCriteria),"REORDER","OK") &
" | Next Delivery: " & DGET(Orders,"ExpectedDate",PendingOrderCriteria)
// Complete inventory status with supplier and reorder information

// Price management with cost analysis
="Item: " & DGET(Products,"Description",ItemCriteria) & 
" | Cost: $" & DGET(Products,"Cost",ItemCriteria) &
" | Price: $" & DGET(Products,"Price",ItemCriteria) & 
" | Margin: " & ROUND((DGET(Products,"Price",ItemCriteria)-DGET(Products,"Cost",ItemCriteria))/DGET(Products,"Price",ItemCriteria)*100,1) & "%" &
" | Competitor: $" & DGET(Competition,"Price",CompCriteria) &
" | Position: " & IF(DGET(Products,"Price",ItemCriteria)<DGET(Competition,"Price",CompCriteria),"Competitive","Premium")
// Comprehensive pricing analysis with competitive positioning
```

### Employee Information System
```spreadsheets
// Employee profile with performance and compensation
="Employee: " & DGET(Employees,"FullName",EmpCriteria) & 
" | ID: " & DGET(Employees,"EmployeeID",EmpCriteria) &
" | Department: " & DGET(Employees,"Department",EmpCriteria) & 
" | Manager: " & DGET(Managers,"Name",ManagerCriteria) &
" | Salary: $" & DGET(Payroll,"Salary",PayrollCriteria) & 
" | Performance: " & DGET(Reviews,"Rating",ReviewCriteria) & "/10" &
" | Next Review: " & DGET(Reviews,"NextReviewDate",ReviewCriteria)
// Complete employee information for HR and management use

// Training and development tracking
="Employee: " & DGET(Employees,"Name",EmpID) & 
" | Role: " & DGET(Employees,"Position",EmpID) &
" | Last Training: " & DGET(Training,"CompletionDate",TrainingCriteria) & 
" | Certification: " & DGET(Certifications,"Status",CertCriteria) &
" | Required Training: " & DGET(Requirements,"NextTraining",RoleCriteria) &
" | Budget Used: $" & DGET(TrainingBudget,"AmountUsed",BudgetCriteria) & 
" of $" & DGET(TrainingBudget,"TotalBudget",BudgetCriteria)
// Training and development status with budget tracking
```

### Project Management Dashboard
```spreadsheets
// Project status with resource and timeline information
="Project: " & DGET(Projects,"Name",ProjectCriteria) & 
" | PM: " & DGET(Projects,"Manager",ProjectCriteria) &
" | Status: " & DGET(Projects,"Status",ProjectCriteria) & 
" | Budget: $" & DGET(Projects,"Budget",ProjectCriteria) & 
" | Spent: $" & DGET(Expenses,"Total",ExpenseCriteria) &
" | Remaining: $" & (DGET(Projects,"Budget",ProjectCriteria)-DGET(Expenses,"Total",ExpenseCriteria)) &
" | Due: " & DGET(Projects,"DueDate",ProjectCriteria) &
" | Health: " & IF(DGET(Projects,"Status",ProjectCriteria)="On Track","✓","⚠")
// Comprehensive project overview with financial and timeline status

// Resource allocation with capacity analysis
="Resource: " & DGET(Resources,"Name",ResourceCriteria) & 
" | Current Project: " & DGET(Assignments,"ProjectName",CurrentAssignment) &
" | Utilization: " & DGET(Assignments,"Percentage",CurrentAssignment) & "%" &
" | Available: " & (100-DGET(Assignments,"Percentage",CurrentAssignment)) & "%" &
" | Rate: $" & DGET(Resources,"HourlyRate",ResourceCriteria) & "/hr" &
" | Skills: " & DGET(Resources,"Skills",ResourceCriteria) &
" | Next Available: " & DGET(Assignments,"EndDate",CurrentAssignment)
// Resource management with availability and capacity planning
```

### Financial Analysis System
```spreadsheets
// Account analysis with transaction details
="Account: " & DGET(Accounts,"Name",AccountCriteria) & 
" | Balance: $" & DGET(Accounts,"Balance",AccountCriteria) &
" | Last Transaction: $" & DGET(Transactions,"Amount",LastTransCriteria) & 
" on " & DGET(Transactions,"Date",LastTransCriteria) &
" | Monthly Average: $" & DGET(Analytics,"MonthlyAvg",AnalyticsCriteria) &
" | Status: " & DGET(Accounts,"Status",AccountCriteria) &
" | Alert: " & IF(DGET(Accounts,"Balance",AccountCriteria)<DGET(Accounts,"MinBalance",AccountCriteria),"Low Balance","OK")
// Complete account overview with transaction history and status monitoring
```
