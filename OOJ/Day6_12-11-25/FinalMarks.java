import CIE.Internals;
import SEE.External;

public class FinalMarks {
    public static void main(String[] args) {
        int[] iMarks = {30, 40, 35, 45, 40}; 
        int[] eMarks = {40, 50, 45, 55, 50};

        Internals in = new Internals("1CR", "John", 5, iMarks);
        External ex = new External("1CR", "John", 5, eMarks);

        System.out.println("Final Marks for " + in.name + ":");
        for(int i=0; i<5; i++) {
            System.out.println("Subject " + (i+1) + ": " + (in.internalMarks[i] + (ex.seeMarks[i]/2)));
        }
    }
}