import csv
import os

def create_expenses(date, category, amount):
    file_exists = os.path.isfile(file_path)
    formatted_amount = "{:.2f}".format(float(amount))
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "category", "amount"])
        writer.writerow([date, category, formatted_amount])

def read_expenses():
    file_exists = os.path.isfile(file_path)
    if file_exists:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

def update_expenses(index, date, category, amount):
    formatted_amount = "{:.2f}".format(float(amount))
    with open(file_path, "r") as file:
        rows = list(csv.reader(file))
    if 1 <= index < len(rows):  # index 0 is header
        rows[index] = [date, category, formatted_amount]
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def delete_expenses(index):
    with open(file_path, "r") as file:
        rows = list(csv.reader(file))
    if 1 <= index < len(rows):  # index 0 is header
        del rows[index]
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

def find_index(target_date, target_category):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):  # start=1 to match row index
            if row["date"] == target_date and row["category"].lower() == target_category.lower():
                return i
    return -1

def main():
    while True:
        print("\n Smart Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. View Category Summary")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            create_expenses(date, category, amount)

        elif choice == "2":
            expenses = read_expenses()
            for i, row in enumerate(expenses, start=1):
                print(f"{i}. {row}")

        elif choice == "3":
            expenses = read_expenses()
            total = 0.0
            for row in expenses:
                total += float(row["amount"])
            print(f"Total Expenses: ₹{total:.2f}")

        elif choice == "4":
            expenses = read_expenses()
            summary = {}
            for row in expenses:
                cat = row["category"]
                amt = float(row["amount"])
                summary[cat] = summary.get(cat, 0) + amt
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt:.2f}")

        elif choice == "5":
                new_date = input("New date (YYYY-MM-DD): ")
                new_category = input("New category: ")
                new_amount = input("New amount: ")
                index = find_index(new_date, new_category)
                if index != -1:
                    update_expenses(index, new_date, new_category, new_amount)
                    print(" Expense updated successfully.")
                else:
                    print(" Expense not found.")

        elif choice == "6":
            date = input("Enter date of expense to delete (YYYY-MM-DD): ")
            category = input("Enter category of expense to delete: ")
            index = find_index(date, category)
            if index != -1:
                delete_expenses(index)
                print(" Expense deleted successfully.")
            else:
                print(" Expense not found.")

        elif choice == "7":
            print(" Exiting Smart Expense Tracker. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    file_path = "C:/Users/manoj/Desktop/python_assignment/task4/expenses.csv"
    main()