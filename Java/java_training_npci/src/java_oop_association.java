import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

abstract class Employee {
    float emp_salary;

    Employee() {
        emp_salary = 30000;
    }

    Employee(float salary) {
        emp_salary = salary;
    }
}

class ProjectManager extends Employee {
    ProjectManager() {
        this.emp_salary = 100000;
    }
}

class Developer extends Employee {
    Developer() {
        this.emp_salary = 40000;
    }
}

class Project {
    ProjectManager pm;
    Developer[] dev;
    float infrastructureCost;
    float maintenanceCost;

    Project() {
        pm = new ProjectManager();
        dev = new Developer[3];
        maintenanceCost = 25000;
        infrastructureCost = 100000;
    }

    Project(ProjectManager pm, Developer[] devs) {
        this.pm = pm;
        this.dev = devs;
    }

    float getProjectCost() {
        float cost = (pm.emp_salary + infrastructureCost + maintenanceCost);
        for (Developer d: dev) cost += d.emp_salary;
        return cost;
    }

    void displayProjectDetails(){
        float projectCost = getProjectCost();
        System.out.println("Project Cost : " + projectCost);
        System.out.println("Project Manager : " + pm.emp_salary);
        System.out.println("Number of Developers : " + dev.length); 
        System.out.printf("Developer Salary : %f * %d = %f \n", dev[0].emp_salary, dev.length, (dev[0].emp_salary * dev.length));
        System.out.println("Maintenance Cost : " + maintenanceCost);
        System.out.println("Infrastructure Cost : " + infrastructureCost);
    }
}

public class java_oop_association {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of Developers you want for your project : ");
        int devNo = sc.nextInt();
        ProjectManager pm = new ProjectManager();
        Developer[] devs = new Developer[devNo];
        Arrays.fill(devs, new Developer());
        Project p1 = new Project(pm, devs);
        System.out.print("Project Cost : " + p1.getProjectCost());
        p1.displayProjectDetails();
        sc.close();
    }

}