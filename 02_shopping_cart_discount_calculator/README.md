# Shopping Cart Discount Calculator

## Problem Statement

Create a Python program that calculates the discount and final payable amount based on the customer's purchase amount.

The program should determine the applicable discount rate, calculate the discount amount, and display the final amount payable.

## Discount Rules

| Purchase Amount | Discount Rate |
|---|---:|
| Less than Rs. 1,000 | 0% |
| Rs. 1,000 to less than Rs. 5,000 | 10% |
| Rs. 5,000 to less than Rs. 10,000 | 15% |
| Rs. 10,000 and above | 20% |

## Example

**Input**
```text
Enter purchase amount: 6000
```

**Calculation**

- Purchase amount = Rs. 6,000
- Discount rate = 15%
- Discount amount = 6,000 × 15 / 100 = Rs. 900
- Final amount = 6,000 − 900 = Rs. 5,100

**Output**
```text
Purchase amount: Rs. 6000.00
Discount rate: 15%
Discount amount: Rs. 900.00
Final amount payable: Rs. 5100.00
```

## Formula

**1. Calculate the discount amount**

```text
Discount Amount = Purchase Amount × Discount Rate / 100
```

**2. Calculate the final amount**

```text
Final Amount = Purchase Amount − Discount Amount
```

## Python Concepts Practiced

- User input using `input()`
- Type conversion using `float()`
- Variables and assignment
- Conditional statements: `if`, `elif`, and `else`
- Comparison operators
- Functions and parameters
- Arguments and function calls
- Return values using `return`
- Multiple-value returns
- Tuple unpacking
- Arithmetic and percentage calculations
- Exception handling using `try` and `except`
- Input validation
- Formatted output using f-strings

## Key Learning Notes

### 1. Conditional Branching with Multiple Ranges

Conditional statements allow a program to select the appropriate discount rate based on the purchase amount.

```python
if purchase_amount < 1000:
    discount_rate = 0

elif purchase_amount < 5000:
    discount_rate = 10

elif purchase_amount < 10000:
    discount_rate = 15

else:
    discount_rate = 20
```

**Important:** Python evaluates the conditions from top to bottom. Once a condition is true, the remaining branches are skipped.

For example, if the purchase amount is Rs. 6,000, the first two conditions are false, and the third condition is true. Therefore, the discount rate is 15%.

### 2. Code Reusability Through Functions

A function groups related instructions into a reusable block of code.

```python
def calculate_final_amount(purchase_amount, discount_rate):
    discount_amount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount_amount

    return discount_amount, final_amount
```

Instead of repeating the calculation logic, the program can call this function whenever it needs to calculate a discount and final amount.

**When to use functions:**
- When a task forms a clear, reusable unit of logic.
- When repeated calculations would otherwise duplicate code.
- When dividing a program into smaller, understandable parts improves readability.

### 3. Parameters and Arguments

**Parameters** are the variable names defined in a function.

```python
def calculate_final_amount(purchase_amount, discount_rate):
```

Here, `purchase_amount` and `discount_rate` are parameters.

**Arguments** are the actual values passed to the function.

```python
calculate_final_amount(6000, 15)
```

Here, `6000` and `15` are arguments.

### 4. Understanding `return` vs. `print()`

`print()` displays information on the screen, whereas `return` sends a value back to the code that called the function.

Example using `return`:

```python
def calculate_discount(amount, rate):
    return amount * rate / 100

discount = calculate_discount(8000, 15)

print(discount)
```

Output:

```text
1200.0
```

The returned value is stored in the `discount` variable, so it can be reused in another calculation.

**Important:** A function without an explicit `return` statement returns `None` by default, even if it prints a calculated value.

### 5. Returning Multiple Values

A Python function can return multiple values separated by commas.

```python
return discount_amount, final_amount
```

These values can be received using tuple unpacking:

```python
discount_amount, final_amount = calculate_final_amount(
    purchase_amount, discount_rate
)
```

The first returned value is assigned to `discount_amount`, and the second is assigned to `final_amount`.

This makes the calculated values available for printing or further processing.

### 6. Input Validation and Exception Handling

The program rejects negative purchase amounts:

```python
if purchase_amount < 0:
    print("Purchase amount cannot be negative.")
```

It also handles inputs that cannot be converted into a floating-point number:

```python
try:
    purchase_amount = float(input("Enter purchase amount: "))

except ValueError:
    print("Invalid input. Please enter a valid number.")
```

This prevents the program from terminating with an unhandled `ValueError` when the user enters input such as `abc`.

## Testing and Expected Results

| Test Input | Expected Discount | Expected Final Amount |
|---:|---:|---:|
| 0 | 0% | Rs. 0.00 |
| 500 | 0% | Rs. 500.00 |
| 999 | 0% | Rs. 999.00 |
| 1000 | 10% | Rs. 900.00 |
| 4999 | 10% | Rs. 4,499.10 |
| 5000 | 15% | Rs. 4,250.00 |
| 9999 | 15% | Rs. 8,499.15 |
| 10000 | 20% | Rs. 8,000.00 |
| -100 | Rejected | No calculation |
| `abc` | Invalid input | Error message |

## Problem-Solving Approach

1. Read the purchase amount from the user.
2. Validate that the amount is not negative.
3. Determine the applicable discount rate using conditional statements.
4. Pass the purchase amount and discount rate to the calculation function.
5. Calculate the discount and final payable amount.
6. Return both calculated values.
7. Store the returned values in separate variables.
8. Display the purchase amount, discount rate, discount amount, and final amount.
9. Handle invalid numeric input using exception handling.

## Key Takeaways

- Conditional statements can handle multiple pricing ranges.
- Functions help organize reusable calculation logic.
- Parameters receive values, while arguments supply those values.
- `return` makes calculated results available to the calling code.
- Multiple values can be returned and assigned using tuple unpacking.
- Input validation improves program reliability.
- Testing boundary values helps identify errors in conditional logic.

## Conclusion

This project strengthened my understanding of conditional branching, percentage calculations, function design, return values, tuple unpacking, input validation, and exception handling.

It also helped me understand how to separate calculation logic from output display, making Python programs easier to maintain and extend.