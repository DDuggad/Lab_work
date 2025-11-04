class ComplexNumber {
    double real, imaginary;

    public ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    @Override
    public String toString() {
        return real + " + " + imaginary + "i";
    }
}

class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public ComplexNumber add(ComplexNumber c1, ComplexNumber c2) {
        return new ComplexNumber(c1.real + c2.real, c1.imaginary + c2.imaginary);
    }
}

public class OverloadDemo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Integer Sum: " + calc.add(10, 20));

        ComplexNumber n1 = new ComplexNumber(2.5, 3.0);
        ComplexNumber n2 = new ComplexNumber(1.5, 4.5);
        
        System.out.println("Complex Sum: " + calc.add(n1, n2));
    }
}
