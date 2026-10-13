"""
Problem: Shopping Cart Discount Calculator

Problem Statement:
Calculate the final purchase amount after applying a discount
based on the total purchase amount.

Discount Rules:
- Less than Rs. 1,000: 0% discount
- Rs. 1,000 to less than Rs. 5,000: 10% discount
- Rs. 5,000 to less than Rs. 10,000: 15% discount
- Rs. 10,000 and above: 20% discount

Requirements:
- Get the purchase amount from the user.
- Determine the applicable discount rate.
- Calculate the discount amount and final amount.
- Reject negative purchase amounts.
- Handle invalid numeric input.

Concepts Practiced:
- User input and type conversion
- Conditional statements
- Functions and parameters
- Return values
- Percentage calculations
- Exception handling
- Input validation
- Formatted output
"""


def calculate_final_amount(purchase_amount, discount_rate):
    discount_amount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount_amount

    return discount_amount, final_amount


try:
    purchase_amount = float(input("Enter purchase amount: "))

    if purchase_amount < 0:
        print("Purchase amount cannot be negative.")

    else:
        if purchase_amount < 1000:
            discount_rate = 0

        elif purchase_amount < 5000:
            discount_rate = 10

        elif purchase_amount < 10000:
            discount_rate = 15

        else:
            discount_rate = 20

        discount_amount, final_amount = calculate_final_amount(purchase_amount, discount_rate)

        print(f"\nPurchase amount: Rs. {purchase_amount:.2f}")
        print(f"Discount rate: {discount_rate}%")
        print(f"Discount amount: Rs. {discount_amount:.2f}")
        print(f"Final amount payable: Rs. {final_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")