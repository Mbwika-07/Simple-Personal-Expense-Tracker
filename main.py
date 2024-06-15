from datetime import datetime, timedelta

expenses = {
    "food": [
        {"name": "Pizza", "amount": 800, "date": "12/06/24"},
        {"name": "Burger", "amount": 500, "date": "13/06/24"},
        {"name": "Salad", "amount": 300, "date": "14/06/24"}
    ],
    "transport": [
        {"name": "Bus fare", "amount": 100, "date": "12/06/24"}
    ],
    "entertainment": [
        {"name": "Movie", "amount": 1200, "date": "11/06/24"}
    ],
    "clothes": [],
    "others": []  
}

def add_expense():
    name = input(f"Enter the name of item/service bought: ")
    amount = int(input("Enter amount spent(Ksh): "))
    category = input(f"Enter the name of the category the expense belongs to: ")
    date = input(f"Enter the date the expense was acquired(dd/mm/yy): ")
    
    if category not in expenses:
        print(f"Category '{category}' does not exist. Adding to 'others'.")
        category = "others"
    
    expense = {
        "name": name,
        "amount": amount,
        "date": date
    }
    expenses[category].append(expense)
    
    #print(f"\nExpense added: {expense}")
    print(f"\nYou added the item {name} of amount {amount} on date {date} to the category {category}.")
    

def view_total_summary():
    grand_total = 0
    print("\nTotal expenses by category:")
    
    for category, expense_list in expenses.items():
        category_total = sum(expense["amount"] for expense in expense_list)
        print(f"\t{category.capitalize()}: Ksh.{category_total}")
        
        grand_total += category_total
    
    print(f"\n\t\tGrand Total: Ksh.{grand_total}")

def view_specific_summary():
    category = input("Enter the category you want to view: ")
    
    if category in expenses:
        if expenses[category]:  # Check if there are any expenses in the category
            category_total = 0
            for expense in expenses[category]:
                print(f"\nName: {expense['name']}, Amount: Ksh.{expense['amount']}, Date: {expense['date']}")
                category_total += expense['amount']
            print(f"\n\t\tGrand total for the category {category.title()} is Ksh. {category_total} ")
        else:
            print(f"No expenses in the '{category}' category.")
    else:
        print(f"Category '{category}' does not exist.")

def view_total_time():
    print("function coming soon!!!")


is_running = True

while is_running:
    print("\n*********************************************************************************************************************************\n")
    print("\t\t\tPERSONAL EXPENSE TRACKER")
    print("\n*********************************************************************************************************************************")
    print("\n\t1.Add new expense")
    print("\n\t2.View summary of total expenses.")
    print("\n\t3.View summary of specific category.")
    print("\n\t4.View total expense spent in a specific time.")
    print("\n\t5.Exit")
    
    choice = input("Enter your choice(1-4): ")
    print("\n*********************************************************************************************************************************\n")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total_summary()
    elif choice == "3":
        view_specific_summary()
    elif choice == "4":
        view_total_time()
    elif choice == "5":
        is_running = False
    else:
        print("Invalid choice.")