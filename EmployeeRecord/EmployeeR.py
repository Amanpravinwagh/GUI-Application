import csv
import os

EMPLOYEE_FILE = "employees.csv"

class EmployeeRecordsSystem:
    def __init__(self):
        self.employees = self.load_employees()
    
    def load_employees(self):
        employees = []
        if os.path.exists(EMPLOYEE_FILE):
            with open(EMPLOYEE_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(row)
        return employees
    
    def save_employees(self):
        with open(EMPLOYEE_FILE, mode='w', newline='') as file:
            fieldnames = ["ID", "Name", "Age", "Department", "Salary"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.employees)
    
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        age = input("Enter Employee Age: ")
        department = input("Enter Employee Department: ")
        salary = input("Enter Employee Salary: ")
        self.employees.append({"ID": emp_id, "Name": name, "Age": age, "Department": department, "Salary": salary})
        self.save_employees()
        print("Employee added successfully!\n")
    
    def view_employees(self):
        if not self.employees:
            print("No employee records found.\n")
            return
        print("\nEmployee Records:")
        for emp in self.employees:
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Age: {emp['Age']}, Department: {emp['Department']}, Salary: {emp['Salary']}")
        print()
    
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for emp in self.employees:
            if emp['ID'] == emp_id:
                print(f"\nFound Employee: ID: {emp['ID']}, Name: {emp['Name']}, Age: {emp['Age']}, Department: {emp['Department']}, Salary: {emp['Salary']}\n")
                return
        print("Employee not found!\n")
    
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        for emp in self.employees:
            if emp['ID'] == emp_id:
                emp['Name'] = input(f"Enter new name ({emp['Name']}): ") or emp['Name']
                emp['Age'] = input(f"Enter new age ({emp['Age']}): ") or emp['Age']
                emp['Department'] = input(f"Enter new department ({emp['Department']}): ") or emp['Department']
                emp['Salary'] = input(f"Enter new salary ({emp['Salary']}): ") or emp['Salary']
                self.save_employees()
                print("Employee updated successfully!\n")
                return
        print("Employee not found!\n")
    
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        self.employees = [emp for emp in self.employees if emp['ID'] != emp_id]
        self.save_employees()
        print("Employee deleted successfully (if existed)!\n")
    
    def main_menu(self):
        while True:
            print("\nEmployee Records System")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    system = EmployeeRecordsSystem()
    system.main_menu()
