class Employee {
    int empId;
    String name;
    double salary;

    public Employee(int empId, String name, double salary) {
        this.empId = empId;
        this.name = name;
        this.salary = salary;
    }

    public void display() {
        System.out.println("ID: " + empId + ", Name: " + name + ", Salary: " + salary);
    }
}

public class EmployeeDemo {
    public static void main(String[] args) {
        Employee emp1 = new Employee(101, "John Doe", 75000);
        emp1.display();
        
        Employee emp2 = new Employee(102, "Jane Smith", 82000);
        emp2.display();
    }
}
