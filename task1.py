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
    salary_date: date

class GenerateData :   
    def __init__(self):
        self.employees = []
        self.fake = Faker()


    def generate_employee_data(self) :
        for i in range(10):
            empid= i+1
            name= self.fake.name()
            salary = round(random.random() * 1000000, 2)
            salary_date = self.fake.date_between(start_date='-1y', end_date='today')
            self.employees.append(Employee(empid, name, salary, salary_date))
    
    
    def save_data_to_file(self, filename):
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["empid", "name", "salary", "salary_date"])
            for emp in self.employees:
                writer.writerow([emp.empid, emp.name, emp.salary, emp.salary_date])

    
if __name__ == "__main__":
    generator = GenerateData()
    generator.generate_employee_data()
    # for emp in generator.employees:
    #     print(emp)
    generator.save_data_to_file(filename='employees_data1.csv')
            
            