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