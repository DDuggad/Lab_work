package SEE;
import CIE.Personal;

public class External extends Personal {
    public int[] seeMarks = new int[5];

    public External(String u, String n, int s, int[] m) {
        super(u, n, s);
        seeMarks = m;
    }
}