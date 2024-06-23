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
    name = input("Enter the name of item/service bought: ")
    amount = int(input("Enter amount spent (Ksh): "))
    category = input("Enter the name of the category the expense belongs to: ")
    date = input("Enter the date the expense was acquired (dd/mm/yy): ")
    
    if category not in expenses:
        print(f"Category '{category}' does not exist. Adding to 'others'.")
        category = "others"
    
    expense = {"name": name, "amount": amount, "date": date}
    expenses[category].append(expense)
    
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
        if expenses[category]:
            category_total = 0
            for expense in expenses[category]:
                print(f"\nName: {expense['name']}, Amount: Ksh.{expense['amount']}, Date: {expense['date']}")
                category_total += expense['amount']
            print(f"\n\t\tGrand total for the category {category.title()} is Ksh. {category_total} ")
        else:
            print(f"No expenses in the '{category}' category.")
    else:
        print(f"Category '{category}' does not exist.")

def get_expenses_for_day():
    day_expenses = []
    target_date = input("Enter the specific date you would like to search (dd/mm/yy): ")
    
    for category, expenses_list in expenses.items():
        for expense in expenses_list:
            if expense["date"] == target_date:
                day_expenses.append(expense)
                
    return day_expenses



def get_expenses_for_month():
    month_expenses = []
    month = int(input("Enter month (mm): "))
    year = int(input("Enter year (yy): "))
    target_month_year = f"/{month:02d}/{year:02d}"
    
    for category, expenses_list in expenses.items():
        for expense in expenses_list:
            if target_month_year in expense["date"]:
                month_expenses.append(expense)
                
    return month_expenses



def get_expenses_for_week():
    week_expenses = []
    day = int(input("Enter start day of the week (dd): "))
    month = int(input("Enter start month of the week (mm): "))
    year = int(input("Enter start year of the week (yy): "))
    target_date = datetime.strptime(f"{day:02d}/{month:02d}/{year:02d}", "%d/%m/%y")
    start_of_week = target_date - timedelta(days=target_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    for category, expenses_list in expenses.items():
        for expense in expenses_list:
            expense_date = datetime.strptime(expense["date"], "%d/%m/%y")
            if start_of_week <= expense_date <= end_of_week:
                week_expenses.append(expense)
                
    return week_expenses

def get_expenses_for_custom_range():
    range_expenses = []
    start_date = input("Enter start date (dd/mm/yy): ")
    end_date = input("Enter end date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date, "%d/%m/%y")
    end_date = datetime.strptime(end_date, "%d/%m/%y")
    
    for category, expenses_list in expenses.items():
        for expense in expenses_list:
            expense_date = datetime.strptime(expense["date"], "%d/%m/%y")
            if start_date <= expense_date <= end_date:
                range_expenses.append(expense)
                
    return range_expenses

def view_total_time():
    print("Time frames to choose from")
    print("1. Specific date")
    print("2. Specific month")
    print("3. Week")
    print("4. Custom date range")
    key = input("What time frame would you like to view (1-4): ")
    
    if key == "1":
        filtered_expenses = get_expenses_for_day()
    elif key == "2":
        filtered_expenses = get_expenses_for_month()
    elif key == "3":
        filtered_expenses = get_expenses_for_week()
    elif key == "4":
        filtered_expenses = get_expenses_for_custom_range()
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
        return
    
    if filtered_expenses:
        total_amount = sum(expense["amount"] for expense in filtered_expenses)
        for expense in filtered_expenses:
            print(f"Name: {expense['name']}, Amount: Ksh.{expense['amount']}, Date: {expense['date']}")
        print(f"Total amount: Ksh.{total_amount}")
    else:
        print("No expenses found for the specified time frame.")



is_running = True



while is_running:
    print("\n*********************************************************************************************************************************\n")
    print("\t\t\tPERSONAL EXPENSE TRACKER")
    print("\n*********************************************************************************************************************************")
    print("\n\t1. Add new expense")
    print("\n\t2. View summary of total expenses.")
    print("\n\t3. View summary of specific category.")
    print("\n\t4. View total expense spent in a specific time.")
    print("\n\t5. Exit")
    
    choice = input("Enter your choice (1-5): ")
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
