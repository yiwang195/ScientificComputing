# ScientificComputing
Exercises for learning scientific computing techniques.

### Day 1: NumPy

### Day 2: Pandas

#### 04 - Getting started with Pandas

- [ ] Reading data in to a dataFrame (read_csv)
      - [ ] Skipping rows
      - [ ] Setting an index column
      - [ ] Setting header names
      - [ ] What to do with no data
- [ ] Displaying dataFrame properties
      - [ ] showing the full dataFrame in Jupyter
      - [ ] dtypes
      - [ ] columns
      - [ ] shape
      - [ ] len()
      - [ ] head()/tai()l/sample() 
- [ ] Generating Counts and Lists
      - [ ] Extracting a column of data --> series
      - [ ] Listing unique values within a series: `unique()`
      - [ ] Counting unique values within a series: `nunique`
      - [ ] Computing summary statistics: all with `describe()` and individual stats
- [ ] Grouping data in Pandas
      - [ ] `groupby()` function on dataFrames
      - [ ] computing statistics on DataFrameGroupBy objects
            - [ ] All columns...
            - [ ] Select columns...
- [ ] Creating summary counts in Pandas
      - [ ] `groupby` the variable we want
      - [ ] `agg`regate using the `count` function
      - [ ] optionally: supply a single value in the *grouped* column to count just those values

#### 05 - Pandas and SQL

- [ ] Objectives: 
      - [ ] Compare Pandas to Access/SQL
      - [ ] Learn more about how Pandas can query/subset data
- [ ] Reading in the data
      - [ ] setting the index
      - [ ] overriding default dtypes
      - [ ] converting dates
- [ ] Exploring the dataFrame
      - [ ] Listing unique values
- [ ] Selecting columns
      - [ ] Single columns --> series object
      - [ ] Multiple columns --. dataFrame *view*
- [ ] Selecting rows
      - [ ] Creating row masks
      - [ ] Applying row masks
      - [ ] Substring queries
      - [ ] Lambda queries
- [ ] Grouping and aggregating data
      - [ ] groupby command
- [ ] Joining tables
      - [ ] `merge` command
      - [ ] join types with `how`
      - [ ] specifying join columns or indices

#### 06 - Sara Redux

- [ ] Objectives:
      - [ ] Of task: Supply date and LC filter; return locations where criteria was met
      - [ ] To learn: Understanding data query and extraction in Pandas
- [ ] Reading in the data
      - [ ] Skipping comment lines
      - [ ] Overriding the default delimiter
      - [ ] Setting the index
      - [ ] Specifying data types
- [ ] Subsetting using masks
      - [ ] Date mask
      - [ ] LC mask
      - [ ] Applying the mask
- [ ] Returning results

#### 