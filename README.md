
````markdown
# Data Analyzer and Transformer Program

A Python-based console program that allows users to enter data and perform different operations such as data analysis, filtering, sorting, factorial calculation, and statistical calculations.

This project was created to practice important Python programming concepts including functions, recursion, lambda functions, built-in functions, arrays, and returning multiple values.

## About the Project

The Data Analyzer and Transformer Program provides a simple menu-driven interface for working with numerical data.

The program supports both **1D and 2D arrays** and provides different operations depending on the entered data.

It was developed as a practical Python project to understand how different programming concepts can be combined into one application.

## Features

- Input data using 1D or 2D arrays
- Display basic data summary
- Find minimum and maximum values
- Calculate the total and average of the data
- Calculate factorial using recursion
- Filter data using a threshold value
- Use lambda functions with `filter()`
- Sort data in ascending or descending order
- Return multiple statistical values from a function
- Menu-driven console interface
- Function documentation using docstrings

## Python Concepts Used

This project focuses on the following Python concepts:

- Lists
- 1D and 2D arrays
- `append()` method
- Functions
- Function arguments
- `*args`
- `**kwargs`
- Built-in functions
- Lambda functions
- `filter()`
- Recursion
- Sorting
- Return multiple values
- Conditional statements
- Loops
- User input
- Docstrings

## Program Menu

The program contains seven main options:

```text
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
````

## How It Works

### 1. Input Data

The user can select either a 1D or 2D array and enter numerical values.

Example:

```text
Enter a number for array: 1

Enter data for a 1D array:
10 20 30 40 50
```

The values are stored in the array using the `append()` method.

### 2. Display Data Summary

This option displays basic information about the entered data:

* Total number of elements
* Minimum value
* Maximum value
* Sum of values
* Average value

Example:

```text
Total elements: 5
Minimum Value: 10
Maximum Value: 50
Sum of all Values: 150
Average Value: 30.0
```

### 3. Calculate Factorial

The factorial of a number is calculated using a recursive function.

Example:

```text
Enter a number to calculate factorial: 5

Factorial of 5 is: 120
```

### 4. Filter Data by Threshold

The user enters a threshold value and the program filters the data using a lambda function.

For example:

```text
Data:
10 20 30 40 50

Threshold:
30
```

Output:

```text
[30, 40, 50]
```

### 5. Sort Data

The entered data can be sorted in:

* Ascending order
* Descending order

### 6. Display Dataset Statistics

This option calculates and returns multiple values from a function:

* Minimum
* Maximum
* Total
* Average

The program uses `*args` to pass the dataset to the function and `**kwargs` to control the display of results.

### 7. Exit Program

The program displays a simple exit message and terminates the application.

## Requirements

You only need Python installed on your computer.

Recommended:

```text
Python 3.x
```

No external Python libraries are required for this project.

## How to Run

1. Download or clone this repository.

2. Open the project folder.

3. Run the Python file:

```bash
python functional_treat.py
```

4. Follow the options shown in the main menu.

## Project Structure

```text
project_4_functional_treat/
│
├── functional_treat.py
└── README.md
```

## Learning Purpose

The main purpose of this project is to practice Python functions and understand how different programming concepts work together in a menu-driven application.

While developing this project, I worked with recursion, lambda functions, filtering, sorting, built-in functions, lists, and multiple return values.

## Author

**Vaidika Ghoghari**

BCA Graduate | Python Learner

### Connect With Me

* 📧 [vaidika ghoghari](mailto:ghogharivaidika@gmail.com)
* 💼 [LinkedIn](https://www.linkedin.com/in/vaidika-ghoghari-2196a534a)

### Project Explanation

🎥 [Watch the Project Explanation Video](YOUR_VIDEO_LINK_HERE)


## Future Improvements

Some possible improvements for this project are:

* Add more data filtering options
* Improve handling of different types of datasets
* Add more statistical calculations
* Improve the user interface
* Add data visualization in a future version

## License

This project is created for learning and educational purposes.

