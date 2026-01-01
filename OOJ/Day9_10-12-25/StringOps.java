import java.util.Scanner;

public class StringOps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter string: ");
        String s = sc.nextLine();

        for (int i = 0; i < s.length(); i++) {
            System.out.println("Char: " + s.charAt(i) + " Position: " + i);
        }

        int half = s.length() / 2;
        char[] arr = new char[half];
        s.getChars(0, half, arr, 0);

        System.out.print("First half array: ");
        System.out.println(arr);
    }
}
