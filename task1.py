from faker import Faker
import names
import random
from dataclasses import dataclass
from datetime import date
import csv

@dataclass
class Employee:
    empid: int
    name: str
    salary: float
    salary_date: str

class GenerateData(Employee) :   
    employees = [] 
    def generate_employee_data(self):
        self.fake = Faker()
        
        for i in range(100):
            self.empid= i+1#random.randint(1,1000)
            self.name= self.fake.name()
            self.salary = round(random.random() * 1000000, 2)
            self.salary_date = self.fake.date_between(start_date='-1y', end_date='today')
            self.employees.append(Employee(self.empid, self.name, self.salary, self.salary_date))

        return self.employees
    
    
    def save_data_to_file(self, filename='employees_data1.csv'):
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["empid", "name", "salary", "salary_date"])
            for emp in self.employees:
                writer.writerow([emp.empid, emp.name, emp.salary, emp.salary_date])

    
if __name__ == "__main__":
    generator = GenerateData(0, "", 0.0, date.today())
    employee_data = generator.generate_employee_data()
    for emp in employee_data:
        print(emp)
    generator.save_data_to_file()
            
            