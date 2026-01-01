class Q {
    int n;
    boolean valueSet = false;

    synchronized int get() {
        while (!valueSet)
            try { wait(); } catch (InterruptedException e) {}
        System.out.println("Got: " + n);
        valueSet = false;
        notify();
        return n;
    }

    synchronized void put(int n) {
        while (valueSet)
            try { wait(); } catch (InterruptedException e) {}
        this.n = n;
        valueSet = true;
        System.out.println("Put: " + n);
        notify();
    }
}

public class IPCDemo {
    public static void main(String[] args) {
        Q q = new Q();
        new Thread(() -> {
            for (int i = 0; i < 5; i++) q.put(i);
        }).start();
        new Thread(() -> {
            for (int i = 0; i < 5; i++) q.get();
        }).start();
    }
}
