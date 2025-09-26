"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

while True:
    get_sales = float(input("Enter sales: $"))
    #Check for sales less than $1000 and calculate 10% bonus
    if get_sales < 1000:
        bonus = get_sales * 0.1
        print(f"Bonus: ${bonus:.2f}")
    #Check for sales over $1500 and calculate 15% bonus
    else:
        bonus = get_sales * 0.15
        print(f"Bonus: ${bonus:.2f}")