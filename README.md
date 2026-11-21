# Python Map, Filter and Lambda Functions

## About the Project

This project contains Python examples demonstrating the use of built-in `map()` and `filter()` functions along with `lambda` expressions.

The examples cover how to perform operations on lists, convert data types, filter elements based on conditions, and combine multiple functions.

## Topics Covered

### 1. Map Function

The `map()` function applies a given function to every element of an iterable and returns a map object.

**Examples:**
- Finding the length of each string using `len()`.
- Converting string numbers into integers using `int()`.
- Calculating the square of numbers using `lambda`.

### 2. Filter Function

The `filter()` function selects elements from an iterable based on a given condition.

**Examples:**
- Filtering even numbers from a list.
- Finding numbers divisible by 5.
- Filtering numbers based on specific conditions using `lambda`.

### 3. Lambda Function

A `lambda` function is a small anonymous function that can contain a single expression.

**Examples:**
- Squaring numbers using `lambda x: x**2`.
- Checking even numbers using `lambda x: x % 2 == 0`.
- Checking divisibility using `lambda x: x % 5 == 0`.

### 4. Combining Map and Filter

This project also demonstrates combining `map()` and `filter()`.

Example:

```python
a = [10, 12, 13, 6, 9, 7]

result = map(
    lambda x: x**2,
    filter(lambda x: x % 2 == 0, a)
)

print(list(result))
```

**Output:**

```text
[100, 144, 36]
```

Here:
1. `filter()` selects even numbers.
2. `map()` calculates the square of each selected number.
3. `list()` converts the result into a list.

## Technologies Used

- Python 3
- Lambda Functions
- Map Function
- Filter Function
- List Operations

## How to Run

1. Install Python 3 on your system.
2. Clone this repository:

```bash
git clone <repository-url>
```

3. Open the project folder.
4. Run the Python file:

```bash
python main.py
```

## Learning Outcomes

After completing these examples, you will understand:

- How `map()` works.
- How `filter()` works.
- How to write lambda functions.
- How to convert data types using `map()`.
- How to filter list elements using conditions.
- How to combine `map()`, `filter()`, and `lambda()`.

## Author

Pranay Vishwanath Jadhao
