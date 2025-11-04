class Car {
    String make;
    String model;
    int year;

    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public void displayInfo() {
        System.out.println(year + " " + make + " " + model);
    }

    @Override
    protected void finalize() {
        System.out.println("Garbage collecting: " + model);
    }
}

public class GCDemo {
    public static void main(String[] args) {
        Car car1 = new Car("Ford", "Mustang", 2021);
        Car car2 = new Car("Honda", "Civic", 2022);
        
        car1.displayInfo();
        car2.displayInfo();

        car1 = null;
        car2 = null;

        System.out.println("Calling System.gc()...");
        System.gc();
        System.out.println("System.gc() call finished.");
    }
}
