import java.util.Scanner;

public class ListIndex {
    public static void main(String[] args) {
        String[] items = {"Apple", "Banana", "Cherry"};
        Scanner sc = new Scanner(System.in);
        
        try {
            System.out.print("Enter index (0-2): ");
            int idx = sc.nextInt();
            System.out.println("Item: " + items[idx]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Index is out of range.");
        }
    }
}
