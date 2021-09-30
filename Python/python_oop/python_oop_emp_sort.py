class User :
    def __init__(self, id, name, salary) :
        self.id = id 
        self.name = name
        self.salary = salary 

class Project : 
    def __init__(self, id = 0, name = "", users = list()) :
        self.id = id 
        self.name = name 
        self.users = users 

class Project_List :
    def __init__(self, project_list = list()) : 
        self.project_list = project_list
    
    def add_project(self, project) : 
        self.project_list.append(project)

    def sort_project_users_by_salary(self) :
        for project in self.project_list : 
            project.users.sort(key = lambda user : user.salary) 

    def create_project_dict(self) : 
        project_dict = dict() 
        for project in self.project_list : 
            project_dict[project.id] = {user.name : user.salary for user in project.users} 
        return project_dict 

    def display_project_details(self) : 
        for project in self.project_list : 
            print()
            print("Project ID : {} ".format(project.id))
            print("Project Name : {}".format(project.name)) 
            print("Project Users : ")
            for user in project.users :
                print("Username : {} (Rs. {}".format(user.name, user.salary))
            print()

# Taking the input : 
projects = Project_List()
choice = input("Add project details ? \n\tEnter Y to continue\n\tEnter anything else to stop\n?\t") 
while choice == "Y" : 
    print("Enter the details of the project : ")
    project_id = input("Enter the project id : ")
    project_name = input("Enter the name of the project : ")
    print("Enter the details of the project users : (enter 'stop' when done")
    project_users = list()
    usr_choice = "1"
    while usr_choice != "stop" :
        usr_choice = input("Enter the user_id, user_name, user_salary : ")
        user_details = usr_choice.split(",")
        if len(user_details) == 3 : 
            user_id, user_name, user_salary = user_details
            user_salary = float(user_salary) 
            user = User(user_id, user_name, user_salary)
            project_users.append(user)
        
    project = Project(project_id, project_name, project_users)
    projects.add_project(project)
    choice = input("Add another project details ? \tEnter Y to continue\n\tEnter anything else to stop : \n ")

# Show project details before sorting 
print("Project Details before Sorting : ")
projects.display_project_details()

# Sorting Projects By Salary of Users 
projects.sort_project_users_by_salary()

# Creating Dictionary of Sorted Projects
project_dict = projects.create_project_dict()
print(project_dict)

### Output : 
####        Add project details ? 
####                Enter Y to continue        
####                Enter anything else to stop
####        ?       Y
####        Enter the details of the project : 
####        Enter the project id : 3242
####        Enter the name of the project : easyPay
####        Enter the details of the project users : (enter 'stop' when done
####        Enter the user_id, user_name, user_salary : 2342432, akshay, 45000
####        Enter the user_id, user_name, user_salary : 3242422, shreya, 35000
####        Enter the user_id, user_name, user_salary : 3224322, payel, 43222
####        Enter the user_id, user_name, user_salary : stop
####        Add another project details ?   Enter Y to continue
####                Enter anything else to stop : 
####         Y
####        Enter the details of the project : 
####        Enter the project id : 324232
####        Enter the name of the project : cryptoNex
####        Enter the details of the project users : (enter 'stop' when done
####        Enter the user_id, user_name, user_salary : 324232, kushal, 39000
####        Enter the user_id, user_name, user_salary : 234232, shruti, 78000
####        Enter the user_id, user_name, user_salary : 324312, neha, 34000
####        Enter the user_id, user_name, user_salary : stop
####        Add another project details ?   Enter Y to continue
####        
####        Project ID : 3242
####        Project Name : easyPay
####        Username :  akshay (Rs. 45000.0
####        Username :  shreya (Rs. 35000.0
####        Username :  payel (Rs. 43222.0
####        
####        
####        Project ID : 324232
####        Project Name : cryptoNex
####        Project Users :
####        Username :  kushal (Rs. 39000.0
####        Username :  shruti (Rs. 78000.0
####        Username :  neha (Rs. 34000.0
####        
####        {'3242': {' shreya': 35000.0, ' payel': 43222.0, ' akshay': 45000.0}, '324232': {' neha': 34000.0, ' kushal': 39000.0, ' shruti': 78000.0}}