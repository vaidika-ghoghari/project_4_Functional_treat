print("==" * 10 + " FUNCTIONAL TREAT " + "==" * 10)

# printing a welcome message for user
print("Welcome to the Data Analyzer and Transformer Program")

Arrays = []

#-----------------input values -------------------
def add_data():
    global Arrays

    print("\n1. 1D array")
    print("2. 2D array")

    option = int(input("Enter a number for array: "))

    if option == 1:

        num = list(map(int, input(
            "Enter data for a 1D array (separated by space): "
        ).split()))

        for value in num:
            Arrays.append(value)

        print("Data has been stored successfully!")
        print("Array:", Arrays)

    elif option == 2:

        print("\nEnter 3 rows:")

        for i in range(3):
            row = list(map(int, input(
                "Enter Row " + str(i + 1) + " : "
            ).split()))

            Arrays.append(row)

        print("Data has been stored successfully!")
        print("Array:", Arrays)

    else:
        print("Invalid choice")


def get_values():
    values = []

    for item in Arrays:
        if type(item) == list:
            for value in item:
                values.append(value)
        else:
            values.append(item)

    return values

#-------------------- display details ---------------------
def Display_data():
    """Display basic information about the entered data."""

    if len(Arrays) == 0:
        print("\nNo Data Found!")
        return

    values = get_values()

    print("\nData Summary:")
    print("-" * 30)

    print("- Total elements:", len(values))
    print("- Minimum Value:", min(values))
    print("- Maximum Value:", max(values))
    print("- Sum of all Values:", sum(values))

    average = sum(values) / len(values)

    print("- Average Value:", round(average, 2))


#-----------------------calculate factorial-----------------
def calculate_factorial():
    """Calculate factorial using recursion."""

    n = int(input("\nEnter a number to calculate factorial: "))

    def factorial(n):
        if n == 0 or n == 1:
            return 1

        return n * factorial(n - 1)

    if n < 0:
        print("Please enter a positive number.")
    else:
        answer = factorial(n)
        print("Factorial of", n, "is:", answer)


#------------ filetr data --------------------------
def filter_data():
    """Filter values using lambda and filter function."""

    if len(Arrays) == 0:
        print("\nNo Data Found!")
        return

    values = get_values()

    value = int(input("\nEnter a threshold value: "))

    numbers = list(filter(lambda x: x >= value, values))

    print("\nFunction Description:")
    print(filter_data.__doc__)

    print("\nFiltered Data:")
    print(numbers)

    return numbers

#----------------------- sorting data -------------------------
def sort_data():
    """Sort array values in ascending or descending order."""

    if len(Arrays) == 0:
        print("\nNo Data Found!")
        return

    values = get_values()

    print("\nSorting Options:")
    print("1. Ascending Order")
    print("2. Descending Order")

    choice = input("Enter your choice: ")

    if choice == "1":
        values.sort()
        print("\nSorted Data in Ascending Order:")
        print(values)

    elif choice == "2":
        values.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
        print(values)

    else:
        print("\nInvalid choice")


#----------------------- display dataset statistics ----------------
def display_dataset(*args, **kwargs):
    """Calculate and return multiple statistics."""

    Minimum = min(args)
    Maximum = max(args)
    Total = sum(args)
    Average = Total / len(args)

    if kwargs.get("show", True):
        print("\nData Statistics:")
        print("- Minimum value:", Minimum)
        print("- Maximum value:", Maximum)
        print("- Total value:", Total)
        print("- Average value:", round(Average, 2))

    return Minimum, Maximum, Total, Average


#------------------ exit message --------------------------
def exit():
    """Display exit message."""

    print("\nThank you for using the Data Analyzer")
    print("and Transformer Program. Goodbye!")

#---------------main menu -------------------------------

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        add_data()

    elif choice == 2:
        Display_data()

    elif choice == 3:
        calculate_factorial()

    elif choice == 4:
        filter_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:

        if len(Arrays) == 0:
            print("\nNo Data Found!")

        else:
            values = get_values()

            Minimum, Maximum, Total, Average = display_dataset(*values,show=True)

    elif choice == 7:
        exit()
        break

    else:
        print("\nInvalid choice. Please select 1 to 7.")
