class WrongAge extends Exception {
    WrongAge(String msg) { super(msg); }
}

class Father {
    Father(int age) throws WrongAge {
        if (age < 0) throw new WrongAge("Father's age cannot be negative");
        System.out.println("Father created with age: " + age);
    }
}

class Son extends Father {
    Son(int fAge, int sAge) throws WrongAge {
        super(fAge);
        if (sAge >= fAge) throw new WrongAge("Son's age cannot be >= Father's age");
        System.out.println("Son created with age: " + sAge);
    }
}

public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            System.out.println("--- Test Case 1 (Valid) ---");
            new Son(50, 25);
        } catch (WrongAge e) {
            System.out.println("Exception: " + e.getMessage());
        }

        try {
            System.out.println("\n--- Test Case 2 (Invalid Son Age) ---");
            new Son(40, 45);
        } catch (WrongAge e) {
            System.out.println("Exception: " + e.getMessage());
        }

        try {
            System.out.println("\n--- Test Case 3 (Invalid Father Age) ---");
            new Son(-5, 10);
        } catch (WrongAge e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
