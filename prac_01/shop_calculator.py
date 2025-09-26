"""
CP1404/CP5632 - Practical
Program for calculating the total cost of a number of items
"""
#retrieves the number of items being purchased
number_of_items = int(input("How many items are you purchasing?  "))

#while loop to handle the error
while number_of_items < 0:
    print("Invalid number of items.")
    number_of_items = int(input("How many items are you purchasing?  "))

total_cost = 0

#starts a for loop to calculate the total cost of "number_of_items" products
for i in range(0, number_of_items, 1):
    #adds new item cost to the current item cost
    price_of_item = float(input("How much does the item cost?  "))
    total_cost = total_cost + price_of_item
    print(f"The current cost of your order is:  ${total_cost}")

#checks if the total is over 100 and applies discount if applicable
if total_cost >= 100:
    print("Your order is over $100, you get a 10% discount!")
    total_cost = total_cost * 0.9

#prints the final total
print(f"The total cost for {number_of_items} items is ${total_cost}")