# 📓 Problem 01 — Electricity Bill Calculator

## 🧠 Pattern Learned: Conditional Branching with Range-Based Calculations

I learned how to divide a problem into different cases based on the value of an input and apply a different calculation to each case using `if`, `elif`, and `else`.

This problem helped me understand how to identify conditions, determine their boundaries, and calculate the final result by processing different portions of an input value.

## 📌 What Is This Pattern?

When a problem has different rules for different ranges of values, I can divide it into separate cases and handle each case independently.

**General pattern:**

```text
IF value satisfies Condition 1:
    Apply Rule 1

ELIF value satisfies Condition 2:
    Apply Rule 2

ELSE:
    Apply Rule 3
```

In this problem, the electricity bill is calculated using three pricing slabs:

| Electricity Units | Rate |
|---|---:|
| First 100 units | Rs. 10 per unit |
| Next 100 units | Rs. 15 per unit |
| Units above 200 | Rs. 20 per unit |

The higher rates apply only to the units within their respective slabs.

### Example: 250 Units

```text
First 100 units  = 100 × 10 = Rs. 1000
Next 100 units   = 100 × 15 = Rs. 1500
Remaining 50     =  50 × 20 = Rs. 1000

Total Bill = Rs. 3500
```

## 💡 Important Sub-Pattern: Calculating the Remaining Value

I learned how to calculate the remaining value using subtraction after processing a fixed portion of the input.

**Example 1:**

```python
remaining = units - 100
```

If `units = 150`:

```text
remaining = 150 - 100
remaining = 50
```

**Example 2:**

```python
remaining = units - 200
```

If `units = 250`:

```text
remaining = 250 - 200
remaining = 50
```

This approach allows me to process the input in separate portions when each portion follows a different rule.

I also learned that I should not use floor division (`//`) or modulo (`%`) unnecessarily. I should choose operators based on the actual requirements of the problem.

## 🧩 When Should I Apply This Pattern?

I should consider applying conditional branching with range-based calculations when:

- A problem has different rules for different ranges of values.
- The calculation changes depending on the input.
- Multiple conditions determine which calculation should be performed.
- A fixed portion of a value must be processed before calculating the remaining portion.
- Different prices, rates, discounts, fees, or charges apply to different portions of a value.

### 🌍 Real-World Applications

This pattern can be useful for:

- Electricity bill calculations
- Progressive income tax calculations
- Shipping charges based on weight
- Discounts based on purchase amounts
- Delivery fees based on distance
- Parking fees based on duration
- Overtime salary calculations
- Internet or data usage charges
- Tiered service pricing

The exact conditions and calculations depend on the rules defined by each problem.

## 🧠 Key Problem-Solving Lessons

1. **Understand the requirements first:** Identify the rules before writing code.
2. **Identify the conditions:** Determine which cases need to be handled.
3. **Identify the boundaries:** Understand where one condition ends and another begins.
4. **Break the problem into smaller steps:** Calculate each portion separately when necessary.
5. **Calculate remaining values:** Use subtraction when a fixed portion has already been processed.
6. **Choose appropriate operators:** Use operators based on the logic required, not simply because they are available.
7. **Test different cases:** Verify that each condition produces the expected result.
8. **Validate user input:** Handle negative values and invalid numeric input appropriately.
9. **Explain the solution:** Understand why each condition and calculation is necessary instead of memorizing the code.

## 🧪 Boundary Testing

I learned that boundary values are particularly important when testing conditional statements.

For this problem, I should test the following values:

| Input | Expected Behavior |
|---:|---|
| 0 | Total bill is Rs. 0 |
| 100 | First pricing slab |
| 101 | Second pricing slab begins |
| 200 | Second pricing slab |
| 201 | Third pricing slab begins |
| 250 | All three pricing slabs |
| -10 | Reject negative units |
| `abc` | Handle invalid numeric input |

Testing these values helps me identify mistakes in conditional logic and verify that the program handles different cases correctly.

## 🔄 Thinking Pattern

The general problem-solving process I practiced in this problem is:

```text
Understand the Problem
          ↓
Identify the Input and Output
          ↓
Understand the Rules
          ↓
Identify Conditions and Boundaries
          ↓
Break the Calculation into Smaller Parts
          ↓
Calculate the Remaining Value When Necessary
          ↓
Apply the Appropriate Rule
          ↓
Combine the Results
          ↓
Test Different Cases
          ↓
Handle Invalid Inputs
```

## 📚 Python Concepts Practiced

- User input using `input()`
- Type conversion using `int()`
- Variables
- Arithmetic operators
- Comparison operators
- Conditional statements: `if`, `elif`, and `else`
- Exception handling using `try` and `except`
- Input validation
- Formatted strings using f-strings
- Boundary testing
- Logical problem decomposition

## ⭐ One-Line Takeaway

**I learned to break range-based problems into smaller conditional cases, calculate each portion according to its specific rule, and test the boundaries to verify the solution.**

## 🎯 Personal Learning Reflection

The most important lesson from this problem was learning to think about the logic before writing the code.

Instead of immediately using operators or trying to write the entire solution at once, I learned to understand the rules, identify the cases, calculate the remaining units, and combine the results.

My goal is to apply this thinking process independently when I encounter unfamiliar problems in the future.

**Progress:** Problem 01 completed.

**Next focus:** Continue practicing problem decomposition, conditional logic, and independent solution design before gradually increasing the difficulty.