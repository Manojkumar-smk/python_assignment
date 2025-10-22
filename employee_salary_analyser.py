# Step 1: Store employee names and salaries
employee_salaries = {
    "Rahul": 55000,
    "Priya": 75000,
    "Amit": 48000,
    "Sneha": 62000,
    "Vikram": 50000
}

# Step 2: Calculate average salary
total_salary = sum(employee_salaries.values())
num_employees = len(employee_salaries)
average_salary = total_salary / num_employees

# Step 3: Identify highest-paid employee
highest_paid = max(employee_salaries, key=employee_salaries.get)
highest_salary = employee_salaries[highest_paid]

# Step 4: Find employees earning above average
above_average = [name for name, salary in employee_salaries.items() if salary > average_salary]

# Step 5: Display results
print("Employee Salary Details:")
for name, salary in employee_salaries.items():
    print(f"{name}: ₹{salary:,}")

print(f"\nAverage Salary: ₹{average_salary:,.1f}")
print(f"Highest Paid Employee: {highest_paid} — ₹{highest_salary:,}")
print(f"Employees earning above average: {above_average}")