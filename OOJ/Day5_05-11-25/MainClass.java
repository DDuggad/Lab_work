import mypackage.Addition;

public class MainClass {
    public static void main(String[] args) {
        Addition obj = new Addition();
        int sum = obj.add(15, 20);
        System.out.println("Sum: " + sum);
    }
}
