expenses = {
    "food": [],
    "transport": [],
    "entertainment": [],
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
    print(f"Expense added: {expense}")
    
    

def view_total_summary():
    print("function coming soon!!!")

def view_specific_summary():
    print("function coming soon!!!")

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