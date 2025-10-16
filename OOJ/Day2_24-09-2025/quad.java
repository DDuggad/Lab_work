import java.util.* ;
import static java.lang.Math.*;

public class quad {
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        System.out.println("Welcome to Quadratic Equation. Enter eqn in ax2+bx+c form.");
        System.out.println("Enter value of a: ");
        float a = Sc.nextFloat();
        System.out.println("Enter value of b: ");
        float b = Sc.nextFloat();
        System.out.println("Enter value of c: ");
        float c = Sc.nextFloat();

        float d = (b*b)-(4*a*c);
        if (a==0){
            if (b==0){System.out.println("No roots.");}
            else{
                System.out.println("Linear Equation.");
                float res1=-c/b;
                System.out.println("The root is: "+res1);
            }
        }
        else if (d>=0){
            System.out.println("Two real roots.");
            d=(float) sqrt(d);
            float root1 = (-b+d)/(2*a);
            float root2 = (-b-d)/(2*a);
            System.out.println("The roots are, Root1: "+root1+" & Root2: "+root2);
        }
        else if (d<0){
            System.out.println("Imaginary roots.");
            float imag=(float) sqrt(-d)/(2*a);
            float real = (-b)/(2*a);
            System.out.println("The roots are, Root1: "+real+" + "+imag+"i & Root2: "+real+" - "+imag+"i");

        }
        Sc.close();
    }
    
}
