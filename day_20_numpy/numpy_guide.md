# About NumPy

- NumPy \=\> Python library for numerical data.  
- ndarray \=\> N-dimensional array  
- Vectorization \=\> Apply operation to whole array, no loops  
- Broadcasting \=\> Operations between arrays of different shapes  
- Load \-\> Create \-\> Inspect \-\> Select \-\> Compute \-\> Aggregate \-\> Reshape \-\> Save

## Install:

```sh
pip install numpy
```

## Import

```py
import numpy as np
```

## Usage

- Creating arrays  
- Loading data from files  
- Inspecting arrays  
- Selecting and slicing  
- Math operations (vectorized)  
- Broadcasting  
- Handling NaN values  
- Aggregation  
- Reshaping  
- Random numbers  
- Exporting data

# Creating Arrays

```py
import numpy as np

data = [10, 20, 30, 40, 50]

arr = np.array(data)

print(arr)

# [10 20 30 40 50]

# 2D array (matrix):
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)

# [[1 2 3]
#  [4 5 6]]
```

Common ways to create arrays:

```py
np.zeros(5)            # [0. 0. 0. 0. 0.]
np.ones(3)             # [1. 1. 1.]
np.full(3, 7)          # [7 7 7]
np.arange(0, 10, 2)    # [0 2 4 6 8]  (start, stop, step)
np.linspace(0, 1, 5)   # [0.   0.25  0.5  0.75 1.  ]  (n evenly spaced values)
np.eye(3)              # 3x3 identity matrix
```

## Inspect arrays:

```py
arr.shape        # (rows, cols) -> e.g. (2, 3)
arr.ndim         # number of dimensions
arr.size         # total number of elements
arr.dtype        # data type -> e.g. int64, float64
```

## Array Vs List

List \-\> general purpose, mixed types, slow, element-by-element loops

ndarray \-\> numbers only, one type, fast, operations apply to the whole array

```py
# The NumPy way (vectorized, no loop):
arr = np.array([1, 2, 3, 4])
arr * 2

# array([2, 4, 6, 8])
```

# Reading Data

```py
arr = np.loadtxt("data.csv", delimiter=",")
arr = np.genfromtxt("data.csv", delimiter=",")   # handles missing values
arr = np.load("data.npy")                        # NumPy binary format
```

## Saving Data

```py
np.save("output.npy", arr)                       # NumPy binary
np.savetxt("output.csv", arr, delimiter=",")     # text file
```

# Selecting and Filtering

This is one of the most important NumPy skills.

```py
arr = np.array([10, 20, 30, 40, 50])

# Select one element (index starts at 0):
arr[0]
# 10

# Slice a range (stop is excluded):
arr[1:4]
# array([20, 30, 40])

# 2D selection:
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix[0, 1]       # row 0, column 1 -> 2
matrix[1, :]       # entire row 1 -> array([4, 5, 6])
matrix[:, 0]       # entire column 0 -> array([1, 4])

# Filter rows with a condition:
arr[arr > 25]

# array([30, 40, 50])

# Multiple conditions:

arr[(arr > 15) & (arr < 45)]
# array([20, 30, 40])

# OR:

arr[(arr < 15) | (arr > 45)]
# array([10, 50])

# isin() equivalent:
arr[np.isin(arr, [10, 30, 50])]
# array([10, 30, 50])
```

Boolean masks replace loops. This is the core mindset shift from Python lists to NumPy.

# Math Operations (Vectorized)

```py
arr = np.array([1, 2, 3, 4])

# Element-wise arithmetic, no loop needed:
arr + 10
# array([11, 12, 13, 14])

arr * 2
# array([2, 4, 6, 8])

arr ** 2
# array([ 1,  4,  9, 16])

# Two arrays combine element-wise:
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b
# array([11, 22, 33])

# Common math functions:
np.sqrt(arr)       # square roots
np.exp(arr)        # e^x
np.log(arr)        # natural log
np.abs(np.array([-1, 2]))   # absolute value
np.round(np.array([1.51]))  # [2.]
```

## Broadcasting

Arrays of different shapes still work together. NumPy stretches the smaller one.

```py
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix + 100

# [[101 102 103]
#  [104 105 106]]

row = np.array([10, 20, 30])

matrix + row

# [[11 22 33]
#  [14 25 36]]
```

Rule of thumb: dimensions must match, or one of them must be 1\.

# Handling missing data

```py
data = np.array([10.0, np.nan, 30.0])

# Check for missing values:
np.isnan(data)
# array([False,  True, False])

# Count them:
np.isnan(data).sum()
# 1

# NaN poisons normal aggregation:
data.mean()
# nan

# Safe aggregations (ignore NaN):
np.nanmean(data)
# 20.0

np.nansum(data)
# 40.0

# Replace NaN with a value:
clean = np.nan_to_num(data, nan=0.0)
# array([10.,  0., 30.])

# Fill NaN with the column average:
col = np.array([[10.0], [np.nan], [30.0]])
col[np.isnan(col)] = np.nanmean(col)
```

# Aggregation

```py
arr = np.array([10, 20, 30, 40])

arr.sum()
# 100

arr.mean()
# 25.0

arr.min()
# 10

arr.max()
# 40

arr.std()      # standard deviation
```

Aggregation along an axis:

```py
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix.sum(axis=0)   # sum of each COLUMN -> array([5, 7, 9])
matrix.sum(axis=1)   # sum of each ROW    -> array([ 6, 15])

matrix.max(axis=1)   # max of each row -> array([3, 6])
```

This pattern is worth remembering:

```py
ARRAY.AGGREGATION(axis=DIMENSION)
```

axis=0 \-\> down the rows (per column)  
axis=1 \-\> across the columns (per row)

# Statistics

```py
salaries = np.array([50000, 70000, 60000, 55000, 80000])

np.mean(salaries)      # 63000.0
np.median(salaries)    # 60000.0
np.std(salaries)       # spread of values
np.var(salaries)       # variance
np.percentile(salaries, 90)   # 90th percentile
np.corrcoef(x, y)      # correlation between two arrays
```

Real-world example:

```py
scores = np.random.normal(70, 10, 1000)   # 1000 exam scores

scores.mean()
# ~70.0

np.percentile(scores, 50)
# ~70.0 (median)
```

# Reshaping Arrays

```py
arr = np.arange(6)
# array([0, 1, 2, 3, 4, 5])

arr.reshape(2, 3)

# [[0 1 2]
#  [3 4 5]]

arr.reshape(3, 2)

# [[0 1]
#  [2 3]
#  [4 5]]

matrix.T                 # transpose (rows become columns)
arr.flatten()            # back to 1D
np.concatenate([a, b])   # join arrays
arr[:, np.newaxis]       # add a new dimension
```

# Random Numbers

```py
rng = np.random.default_rng(seed=42)

rng.random(5)              # 5 floats between 0 and 1
rng.integers(1, 7, 10)     # 10 dice rolls between 1 and 6
rng.normal(70, 10, 100)    # 100 values, mean 70, std 10
rng.choice([10, 20, 30])   # random pick
rng.shuffle(arr)           # shuffle in place
```

Setting a seed makes results reproducible.

# Sample Project

```py
import numpy as np

rng = np.random.default_rng(seed=42)

# Exam scores for 5 students, 3 subjects
scores = rng.integers(40, 100, size=(5, 3))

# Find all passing scores (>= 60)
passing = scores[scores >= 60]

# Add a new column: bonus of 5 points per student
scores = scores + 5

# Average score per student (per row)
scores.mean(axis=1)

# Average score per subject (per column)
scores.mean(axis=0)

# Highest score overall
scores.max()

# Index of the highest scoring student
np.argmax(scores.mean(axis=1))

# Sort students by their average score, descending
avg = scores.mean(axis=1)
avg_sorted = np.sort(avg)[::-1]

# Normalize scores to the 0-1 range
normalized = (scores - scores.min()) / (scores.max() - scores.min())

# Round and export as CSV
np.savetxt("scores_output.csv", normalized.round(2), delimiter=",")
```
