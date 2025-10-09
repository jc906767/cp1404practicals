"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of num_of_months."""
    incomes = []
    num_of_months = int(input("How many num_of_months? "))

    for month in range(1, num_of_months + 1):
        #income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Income for month {month}: $"))
        incomes.append(income)

    print_report(num_of_months, incomes)

def print_report(num_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()


# Think about how to do this before reading on...

# We need a list to store the incomes.
# How do you add values to a list?
# list.append(input)

# We need a counter variable (int) for the month number.
# Remember that list indexes start at 0, but we want to print from 1.

# How many loops will we need? What kind of loops?
# To complete the task three loops will be needed.
# The first one to ask for incomes
# The second one to to print each months income
# The third to print the total incomes

# We need a cumulative total to update as we loop through the list to display the incomes.

# And lastly we need to format the output nicely, which we can use f-strings for.
