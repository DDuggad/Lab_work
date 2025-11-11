package CIE;

public class Internals extends Personal {
    public int[] internalMarks = new int[5];

    public Internals(String u, String n, int s, int[] m) {
        super(u, n, s);
        internalMarks = m;
    }
}