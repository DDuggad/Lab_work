abstract class Shape {
    int a, b;
    abstract void printArea();
}

class Rectangle extends Shape {
    Rectangle(int length, int width) {
        a = length;
        b = width;
    }
    void printArea() {
        System.out.println("Rectangle Area: " + (a * b));
    }
}

class Triangle extends Shape {
    Triangle(int base, int height) {
        a = base;
        b = height;
    }
    void printArea() {
        System.out.println("Triangle Area: " + (0.5 * a * b));
    }
}

class Circle extends Shape {
    Circle(int radius) {
        a = radius;
    }
    void printArea() {
        System.out.println("Circle Area: " + (3.14159 * a * a));
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(10, 5);
        Triangle t = new Triangle(10, 5);
        Circle c = new Circle(7);

        r.printArea();
        t.printArea();
        c.printArea();
    }
}
