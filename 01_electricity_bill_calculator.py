"""
Problem: Electricity Bill Calculator

Problem Statement:
Calculate the monthly electricity bill based on the number of electricity units consumed by the user.

Billing Rules:
- First 100 units: Rs. 10 per unit
- Next 100 units: Rs. 15 per unit
- Above 200 units: Rs. 20 per unit

Requirements:
- Get the number of units from the user.
- Calculate the bill according to the applicable pricing slab.
- Display the total bill.
- Reject negative units.
- Handle invalid numeric input appropriately.

Example:
Input:
250

Calculation:
First 100 units -> 100 × 10 = 1000
Next 100 units  -> 100 × 15 = 1500
Remaining 50    -> 50 × 20 = 1000

Output:
Total Bill: Rs. 3500

Concepts Practiced:
- User input
- Type conversion
- Variables
- Arithmetic operators
- Conditional statements
- Comparison operators
- Exception handling
- Input validation
- Formatted output
"""

try:
    units = int(input("Enter the units: "))

    if units < 0:
        print("Units cannot be negative.")

    elif units <= 100:
        total = units * 10
        print(f"Total Bill: Rs.{total}")

    elif units <= 200:
        remaining = units - 100
        total = (100 * 10) + (remaining * 15)
        print(f"Total Bill: Rs.{total}")

    else:
        remaining = units - 200
        total = (100 * 10) + (100 * 15) + (remaining * 20)
        print(f"Total Bill: Rs.{total}")

except ValueError:
    print("Invalid input. Please enter a whole number.")