
'''Create a class "Employee" that will contain the following attributes:
- Employee's first name
- Employee's last name
- Salary
- Work experience (in years)

Create a class "Department" that will contain the following attributes:
- Department name
- List of employees

The "Department" class should implement the following methods:
- Add employee
- Remove employee
- Get the list of all employees
- Get the average age of employees
- Get the average salary of employees
- Get the employee with the highest salary

Create a class "Company" that will contain the following attributes:
- Company name
- List of departments

The "Company" class should implement the following methods:
- Add department
- Remove department
- Get the list of all departments
- Get the list of all employees in the company
- Get the average age of employees in the company
- Get the average salary of employees in the company
- Get the employee with the highest salary in the company

Example:

john = Employee("John", "Doe", 5000, 3)
mary = Employee("Mary", "Sue", 4000, 2)

sales_department = Department("Sales", [john, mary])

company = Company("Acme Inc.", [sales_department])

# Get the list of all employees in the company
print(company.get_all_employees())

# Get the employee with the highest salary in the company
print(company.get_highest_paid_employee())

# Display information about an employee
print(john)

'''

class Employee:
    def __init__(self, name, surname, salary, experience):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return f'Employee: {self.name} {self.surname}, Salary: ${self.salary}, Experience: {self.experience} years'

    def __repr__(self):
        return self.name

class Department:
    def __init__(self, department, employees=None):
        self.department = department
        self.employees = employees if employees is not None else []

    def __str__(self):
        employee_names = ", ".join(str(employee) for employee in self.employees)
        return f'Department: {self.department}, Employees: {employee_names}'

    def __repr__(self):
        return f'Department: {self.department}, Employees: {self.employees}'

    def add_to_list(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError('Object does not belong to the Employee class')
        if employee not in self.employees:
            self.employees.append(employee)
            return f'{employee} added to the department'
        else:
            raise ValueError('Employee is already in the department')

    def del_employee(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError('Object does not belong to the Employee class')
        if employee in self.employees:
            self.employees.remove(employee)
            return f'{employee} removed from the department'
        raise ValueError(f'{employee} is not in the department')

    def get_employees_list(self):
        return self.employees

    def get_average_salary(self):
        salary = [employee.salary for employee in self.employees]
        return sum(salary) / len(salary)

    def get_avg_experience(self):
        experience = [employee.experience for employee in self.employees]
        return sum(experience) / len(experience)

    def get_max_salary(self):
        return max(self.employees, key=lambda employee: employee.salary)

class Company:
    def __init__(self, company_name, departments=None):
        self.company_name = company_name
        self.departments = departments if departments is not None else []

    def __str__(self):
        department_names = ", ".join(str(department) for department in self.departments)
        return f'Company: {self.company_name}, Departments: {department_names}'

    def __repr__(self):
        return f'Company: {self.company_name}, Departments: {self.departments}'

    def add_department(self, department):
        if not isinstance(department, Department):
            raise ValueError('Object does not belong to the Department class')
        if department not in self.departments:
            self.departments.append(department)
            return f'{department} added'
        else:
            raise ValueError(f'Department {department} already exists!')

    def del_department(self, department):
        if not isinstance(department, Department):
            raise ValueError('Object does not belong to the Department class')
        if department in self.departments:
            self.departments.remove(department)
            return f'{department} removed'
        raise ValueError(f'No such department {department} in the company')

    def get_department_list(self):
        return self.departments

    def get_department_employees(self):
        department_employees = []
        for department in self.departments:
            department_employees.extend(department.get_employees_list())
        return department_employees

    def avg_experience_company(self):
        employees = self.get_department_employees()
        experiences = [employee.experience for employee in employees]
        return sum(experiences) / len(experiences)

    def avg_salary_company(self):
        employees = self.get_department_employees()
        salary = [employee.salary for employee in employees]
        return sum(salary) / len(salary)

    def max_company_salary(self):
        return max(self.get_department_employees(), key=lambda employee: employee.salary)

# Example usage:
john = Employee("John", "Doe", 5000, 3)
mary = Employee("Mary", "Sue", 4000, 2)
sales_department = Department("Sales", [john, mary])
print(sales_department)
my = Employee("Mary", "Sue", 4000, 2)
e = sales_department.add_to_list(my)
# print(e)
# print(Department.get_employees_list)
company = Company("Acme Inc.", [sales_department])
print(company)
