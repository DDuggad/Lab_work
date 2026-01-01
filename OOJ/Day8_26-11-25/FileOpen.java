import java.io.*;
import java.util.Scanner;

public class FileOpen {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter filename: ");
        String name = sc.next();
        
        try {
            FileInputStream fis = new FileInputStream(name);
            System.out.println("File found and opened.");
        } catch (FileNotFoundException e) {
            System.out.println("Error: File does not exist.");
        }
    }
}
