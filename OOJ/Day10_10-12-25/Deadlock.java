public class Deadlock {
    public static void main(String[] args) {
        String res1 = "Resource1";
        String res2 = "Resource2";

        new Thread(() -> {
            synchronized (res1) {
                System.out.println("Thread 1: Locked " + res1);
                try { Thread.sleep(100); } catch (Exception e) {}
                synchronized (res2) {
                    System.out.println("Thread 1: Locked " + res2);
                }
            }
        }).start();

        new Thread(() -> {
            synchronized (res2) {
                System.out.println("Thread 2: Locked " + res2);
                try { Thread.sleep(100); } catch (Exception e) {}
                synchronized (res1) {
                    System.out.println("Thread 2: Locked " + res1);
                }
            }
        }).start();
    }
}
