from constants import *
from datetime import datetime as dt

def addNewEmployee():
    print("Adding New Employee...")
    empId = input("Enter Emp ID : ")
    empName = input("Enter Emp Name : ")
    empSalary = input("Enter Emp Salary : ")
    empDept = input("Enter Emp Department : ")
    empPwd = empId + "@" + empName.split()[0].lower()
    date = dt.now().date()
    regDate= date.strftime("%d-%m-%Y")

    emp = {"ID" : empId, "Name" : empName, "Pwd" : empPwd, "Salary" : empSalary, "Dept" : empDept,"Reg": regDate }
    employees.append(emp)

    print("New Employee Added Successfully...")


def deleteEmployees():
    #emp = input("Enter Employee ID : ")
    # reuse logic of search
    searchResult = searchEmployee()
    if searchResult:
        employees.remove(searchResult)
        print("Emplyee is deleted successfully.")
    else:
        print("Employee is not found")


def updateEmployee():
    emp = input("Enter Employee ID : ")
    # reuse logic of search
    searchResult = searchEmployee()
    if searchResult:
        # Now ask what you want to update : Name, Salary, Department
        print("""
            What do you want to update?
              1. Name
              2. Dept
              3.Salary""")
        updateChoice = input("Enter your choice: ")
        if updateChoice == '1':
            empName = input("Enter new name: ")
            print("Name of employee is updated.")
        elif updateChoice == '2':
            empDept = input("Enter new department name: ")
            print("Department of employee is updated.")
        elif updateChoice == '3':
            empSalary = input("Enter new salary: ")
            print("Salary of employee is updated.")
    else:
        print("Employee is not found.")


def searchEmployee():
    empID = input("Enter Employee ID : ")
    # logic to search employee
    for emp in employees:
        if emp['ID'] == empID:
            print("Employee Logged in Successfully...")
            return emp['ID']
    else:
        print("Employee Not Found...")
        return False


def printAllEmployees():
    for emp in employees:
        for key in emp:
            print(key, ":", emp[key])
        print("=====================")

def invalidChoice():
    print("You have pressed some wrong button...")