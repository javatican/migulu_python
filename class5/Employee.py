#Employee
#屬性: name, department, salary
#方法: print_info(), raise_salary()

class Employee:
    def __init__(self, name, department, salary):
        self.name=name
        self.department=department
        self.salary=salary
    def print_info(self):
        print("name:",self.name,",department:", self.department, ",salary:",self.salary)
    def raise_salary(self, percentage):
        self.salary = self.salary * (1+percentage)
        
def main():
    e1 = Employee("John Smith","Sales",10000 )
    e2 = Employee("Helen Brown", "Engineer",12000)
    e1.print_info()
    e2.print_info()
    e1.raise_salary(0.1)
    e2.raise_salary(-0.1)
    e1.print_info()
    e2.print_info()
        
    