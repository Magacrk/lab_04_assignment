class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class Main:
    def __init__(self, employees):
        self.employees = employees

    def search(self, key, value):
        if key == "age":
            results = [emp for emp in self.employees if emp.age == value]
        elif key == "name":
            results = [emp for emp in self.employees if emp.name == value]
        elif key == "salary":
            operator, target_salary = value
            if operator == ">":
                results = [emp for emp in self.employees if emp.salary > target_salary]
            elif operator == "<":
                results = [emp for emp in self.employees if emp.salary < target_salary]
            elif operator == ">=":
                results = [emp for emp in self.employees if emp.salary >= target_salary]
            elif operator == "<=":
                results = [emp for emp in self.employees if emp.salary <= target_salary]
            else:
                results = []
        else:
            results = []
        return results

# Sample data
employees_data = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

main_table = Main(employees_data)

print("Choose search parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    target_age = int(input("Enter the age to search: "))
    results = main_table.search("age", target_age)
elif choice == "2":
    target_name = input("Enter the name to search: ")
    results = main_table.search("name", target_name)
elif choice == "3":
    operator = input("Enter the salary operator (> / < / >= / <=): ")
    target_salary = int(input("Enter the salary to compare: "))
    results = main_table.search("salary", (operator, target_salary))
else:
    print("Invalid choice!")

if results:
    print("Search results:")
    for emp in results:
        print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
else:
    print("No results found.")
