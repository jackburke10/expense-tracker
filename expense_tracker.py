import datetime
import csv
import os

expenses = []

expenses_file = "expenses.csv"

def load_expenses_from_csv():
	if not os.path.exists(expenses_file):
		return  # If the CSV file doesn't exist, there's nothing to load.

	with open(expenses_file, "r") as file:
		reader = csv.reader(file)
		next(reader)  # Skip the header
		for row in reader:
			if len(row) == 4:
				expense = {
				'description' : row[0],
				'amount' : float(row[1]),  # Ensure 'Amount' is a number
				'category' : row[2],
				'date' : row[3],
				}
				expenses.append(expense)

def add_expense(description, amount, category):
	expense = {
	'description': description,
	'amount': amount,
	'category': category,
	'date': datetime.date.today().isoformat(),
	}
	expenses.append(expense)

def list_expenses():
	for expense in expenses:
		print(f"{expense['date']}: {expense['description']} - {expense['category']} - ${expense['amount']}")

def delete_expense(index):
	if 0 <= index < len(expenses):
		del expenses[index]

def save_expenses_to_csv():
	with open(expenses_file, "w+", newline="") as file:
		writer = csv.writer(file)
		# Write header
		writer.writerow(["Description", "Amount", "Category", "Date"])
		# Write expenses
		for expense in expenses:
			writer.writerow([
			expense["description"],
			expense["amount"],
			expense["category"],
			expense["date"]
			])

def main():
	load_expenses_from_csv()
	while True:
		print("\nExpense Tracker")
		print("1. Add expense")
		print("2. List expenses")
		print("3. Delete expense")
		print("4. Save expenses")
		print("5. Exit")

		choice = input("Choose an option: ")

		if choice == "1":
			description = input("Enter expense description: ")
			amount = float(input("Enter expense amount: "))
			category = input("Enter expense category: ")
			add_expense(description, amount, category)
			print("Expense added.")

		elif choice == "2":
			list_expenses()

		elif choice == "3":
			list_expenses()
			index = int(input("Enter the index of the expense to delete: "))
			delete_expense(index)
			print("Expense deleted.")

		elif choice == "4":
			save_expenses_to_csv()

		elif choice == "5":
			break

		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()
