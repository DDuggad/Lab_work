class Account {
    String name;
    int accNo;
    double balance;

    Account(String n, int a, double b) {
        name = n; accNo = a; balance = b;
    }

    void deposit(double amt) {
        balance += amt;
        System.out.println("Deposited: " + amt + ", New Balance: " + balance);
    }

    void display() {
        System.out.println("AccNo: " + accNo + ", Name: " + name + ", Balance: " + balance);
    }
}

class SavAcct extends Account {
    SavAcct(String n, int a, double b) { super(n, a, b); }

    void interest() {
        double ints = balance * 0.05;
        balance += ints;
        System.out.println("Interest added: " + ints + ", New Balance: " + balance);
    }

    void withdraw(double amt) {
        if (amt <= balance) {
            balance -= amt;
            System.out.println("Withdrawn: " + amt + ", Balance: " + balance);
        } else System.out.println("Insufficient funds.");
    }
}

class CurAcct extends Account {
    double minBal = 500;
    CurAcct(String n, int a, double b) { super(n, a, b); }

    void withdraw(double amt) {
        if (balance - amt < minBal) {
            balance -= (amt + 50); 
            System.out.println("Penalty applied. Withdrawn: " + amt + ", Balance: " + balance);
        } else {
            balance -= amt;
            System.out.println("Withdrawn: " + amt + ", Balance: " + balance);
        }
    }
}

public class BankDemo {
    public static void main(String[] args) {
        SavAcct s = new SavAcct("Alice", 101, 1000);
        s.display();
        s.interest();
        s.withdraw(200);

        CurAcct c = new CurAcct("Bob", 102, 1000);
        c.display();
        c.withdraw(600); 
    }
}