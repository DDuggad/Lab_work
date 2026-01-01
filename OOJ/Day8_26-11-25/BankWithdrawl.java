import java.util.Scanner;

public class BankWithdrawl {
    public static void main(String[] args) {
        double balance = 500.00;
        Scanner sc = new Scanner(System.in);
        
        try {
            System.out.print("Enter withdrawal amount: ");
            double amount = Double.parseDouble(sc.next());
            
            if (amount > balance) {
                throw new Exception("Insufficient funds.");
            }
            System.out.println("Success. New Balance: " + (balance - amount));
            
        } catch (NumberFormatException e) {
            System.out.println("Error: Non-numeric input.");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
