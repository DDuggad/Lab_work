import java.util.Scanner;

class Student {
    String usn;
    String name;
    int[] credits;
    int[] marks;
    int numSubjects;
// Method to accept student details
    void acceptDetails() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter USN: ");
        usn = sc.nextLine();
        System.out.print("Enter Name: ");
        name = sc.nextLine();
        System.out.print("Enter number of subjects: ");
        numSubjects = sc.nextInt();
        credits = new int[numSubjects];
        marks = new int[numSubjects];
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Enter credits for subject " + (i + 1) + ": ");
            credits[i] = sc.nextInt();
            System.out.print("Enter marks for subject " + (i + 1) + ": ");
            marks[i] = sc.nextInt();
        }
        sc.close();
    }
    
    // Method to calculate SGPA
    double calculateSGPA() {
        int totalCredits = 0;
        double weightedSum = 0.0;
        for (int i = 0; i < numSubjects; i++) {
            int gradePoint = getGradePoint(marks[i]);
            weightedSum += gradePoint * credits[i];
            totalCredits += credits[i];
        }
        return weightedSum / totalCredits;
    }
    
    // Helper method to convert marks to grade points
    int getGradePoint(int marks) {

        if (marks >= 90)
            return 10;
        else if (marks >= 80)
            return 9;
        else if (marks >= 70)
            return 8;
        else if (marks >= 60)
            return 7;
        else if (marks >= 50)
            return 6;
        else if (marks >= 45)
            return 5;
        else if (marks >= 40)
            return 4;
        else
            return 0; // fail
    }
    
    // Method to display student details
    void displayDetails() {
        System.out.println("\n--- Student Details ---");
        System.out.println("USN: " + usn);
        System.out.println("Name: " + name);
        System.out.println("Subject-wise details:");
        for (int i = 0; i < numSubjects; i++) {
            System.out.println("Subject " + (i + 1) + " -> Marks: " + marks[i] + ", Credits: "
                    + credits[i]);
        }
        double sgpa = calculateSGPA();
        System.out.printf("SGPA: %.2f\n", sgpa);
    }
}
public class StudentSGPA {
    public static void main(String[] args) {
        Student s = new Student();
        s.acceptDetails();
        s.displayDetails();
    }
}