from collections import defaultdict
class Employee :
    def __init__(self, id, name, designation, salary) :
        self.id = id 
        self.name = name
        self.designation = designation
        self.salary = salary 

class Project : 
    def __init__(self, id = 0, name = "") :
        self.id = id 
        self.name = name 
         

class Employee_Project_Allotment :
    def __init__(self, projects, employees) : 
        self.allotment = defaultdict(lambda : defaultdict())
        self.projects = projects 
        self.employees = employees

    def add_user_to_project(self, project, user, effort) : 
        self.allotment[project][user] = effort

    def get_project_list(self) :
        for project, employees in self.allotment.items() :
            print(" Project Details : ")
            print(" \tProject ID : {}".format(project.id))
            print(" \tProject Name : {}".format(project.name))
            print(" \tEmployees Assigned to project : ")
            for emp in employees :
                print("\t\t Employee ID : {}, Employee Name : {}, Employee Designation : {}, Employee Salary : {}".format(emp.id, emp.name, emp.designation, emp.salary))
            print("\n")

    def group_projects_by_emp(self) :
        emp_projects = defaultdict(lambda : list())
        for emp in self.employees :
            for project in self.projects :
                if emp in self.allotment[project] :
                    emp_projects[emp].append(project)
        return emp_projects

    def display_emp_projects(self) :
        emp_projects = self.group_projects_by_emp() 
        for emp, projects in emp_projects.items() :
            print("Employee ID : {} ".format(emp.id)) 
            for project in projects : 
                print("\t\tProject Name : {}, Project : {} ".format(project.name, project.id))

    def emp_performance(self, emp) :
        effort = 0
        for project in self.projects : 
            if emp in self.allotment[project] :
                effort += self.allotment[project][emp]
        if effort > 100 :
            return "OVERUTILIZED"
        elif effort < 50 : 
            return "UNDERUTILIZED"
        else : 
            return "NORMAL"
    
    def get_emp_performance_details(self) :
        print("Employee Performance Details : ")
        for emp in self.employees : 
            performance_msg = self.emp_performance(emp)
            print("Employee ID : {}, Employee Performance Details : {} ".format(emp.id, performance_msg))
        

### Taking the input : 
project_list = list()

## Taking input for the projects 
print("Add Projects : ")
for _ in range(3) : 
    project_name, project_id = input("\tEnter the project details (name, id) : ").split(",")
    project = Project(project_id, project_name)
    project_list.append(project)

## Taking input for the employees 
print("Add Employees : ") 
choice = "yes"
emp_list = list()
for _ in range(6) : 
    emp_id, emp_name, emp_designation, emp_salary = input("Enter the employee details (ID, Name, Designation, Salary) : ").split(",")
    emp_salary = float(emp_salary) 
    emp = Employee(emp_id, emp_name, emp_designation, emp_salary)
    emp_list.append(emp)
    

## Assigning employees to projects 
project_assignment = Employee_Project_Allotment(project_list, emp_list)

# assigning to project 1
project_assignment.add_user_to_project(project_list[0], emp_list[0], 27)
project_assignment.add_user_to_project(project_list[0], emp_list[4], 7)
project_assignment.add_user_to_project(project_list[0], emp_list[3], 67)


# assigning to project 2
project_assignment.add_user_to_project(project_list[1], emp_list[5], 47)
project_assignment.add_user_to_project(project_list[1], emp_list[3], 65)
project_assignment.add_user_to_project(project_list[1], emp_list[1], 86)


# assigning to project 3
project_assignment.add_user_to_project(project_list[2], emp_list[2], 34)
project_assignment.add_user_to_project(project_list[2], emp_list[0], 45)
project_assignment.add_user_to_project(project_list[2], emp_list[5], 76)

## Get the details of the projects 
project_assignment.get_project_list()             

## Display the Projects grouped by employees : 
project_assignment.display_emp_projects()

## Display Employee Performance Details : 
project_assignment.get_emp_performance_details()
####################################  SAMPLE OUTPUT ############################################################
########            Add Projects :
########                    Enter the project details (name, id) : ezPay, 7230942
########                    Enter the project details (name, id) : cryptoNex, 2037424  
########                    Enter the project details (name, id) : noCard, 7230497  
########            Add Employees : 
########            Enter the employee details (ID, Name, Designation, Salary) : 893247, kushal, get-ds, 39666
########            Enter the employee details (ID, Name, Designation, Salary) : 742038, akshay, get-ds, 41666
########            Enter the employee details (ID, Name, Designation, Salary) : 023200, preeti, swe, 43899
########            Enter the employee details (ID, Name, Designation, Salary) : 937247, palak, a-swe, 39000
########            Enter the employee details (ID, Name, Designation, Salary) : 382748, shreya, s-ds, 56700
########            Enter the employee details (ID, Name, Designation, Salary) : 248382, sumit, s-swe, 65000
########             Project Details : 
########                    Project ID :  7230942
########                    Project Name : ezPay
########                    Employees Assigned to project : 
########                             Employee ID : 893247, Employee Name :  kushal, Employee Designation :  get-ds, Employee Salary : 39666.0
########                             Employee ID : 382748, Employee Name :  shreya, Employee Designation :  s-ds, Employee Salary : 56700.0  
########                             Employee ID : 937247, Employee Name :  palak, Employee Designation :  a-swe, Employee Salary : 39000.0  
########            
########            
########             Project Details : 
########                    Project ID :  2037424
########                    Project Name : cryptoNex
########                    Employees Assigned to project : 
########                             Employee ID : 248382, Employee Name :  sumit, Employee Designation :  s-swe, Employee Salary : 65000.0  
########                             Employee ID : 937247, Employee Name :  palak, Employee Designation :  a-swe, Employee Salary : 39000.0  
########                             Employee ID : 742038, Employee Name :  akshay, Employee Designation :  get-ds, Employee Salary : 41666.0
########            
########            
########             Project Details : 
########                    Project ID :  7230497
########                    Project Name : noCard
########                    Employees Assigned to project : 
########                             Employee ID : 023200, Employee Name :  preeti, Employee Designation :  swe, Employee Salary : 43899.0   
########                             Employee ID : 893247, Employee Name :  kushal, Employee Designation :  get-ds, Employee Salary : 39666.0
########                             Employee ID : 248382, Employee Name :  sumit, Employee Designation :  s-swe, Employee Salary : 65000.0  
########            
########            
########            Employee ID : 893247 
########                            Project Name : ezPay, Project :  7230942 
########                            Project Name : noCard, Project :  7230497 
########            Employee ID : 742038 
########                            Project Name : cryptoNex, Project :  2037424 
########            Employee ID : 023200 
########                            Project Name : noCard, Project :  7230497 
########            Employee ID : 937247 
########                            Project Name : ezPay, Project :  7230942 
########                            Project Name : cryptoNex, Project :  2037424 
########            Employee ID : 382748 
########                            Project Name : ezPay, Project :  7230942 
########            Employee ID : 248382 
########                            Project Name : cryptoNex, Project :  2037424 
########                            Project Name : noCard, Project :  7230497 
########            Employee Performance Details : 
########            Employee ID : 893247, Employee Performance Details : NORMAL
########            Employee ID : 742038, Employee Performance Details : NORMAL
########            Employee ID : 023200, Employee Performance Details : UNDERUTILIZED
########            Employee ID : 937247, Employee Performance Details : OVERUTILIZED
########            Employee ID : 382748, Employee Performance Details : UNDERUTILIZED
########            Employee ID : 248382, Employee Performance Details : OVERUTILIZED