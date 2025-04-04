# Employee Management System (EMS)

# Step 1 - Plan the Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Asha', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000}
}

# Step 2 - Define the Menu System
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3 - Add Employee Functionality
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee {name} added successfully!")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")

# Step 4 - View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    print("\n{:<10} {:<20} {:<5} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, info in employees.items():
        print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
            emp_id, info['name'], info['age'], info['department'], info['salary']
        ))

# Step 5 - Search for an Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee Found:\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.")

# Step 6 - Run the Program
if __name__ == "__main__":
    main_menu()
