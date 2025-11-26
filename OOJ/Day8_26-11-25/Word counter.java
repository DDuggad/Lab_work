public class WordCounter {
    public static void main(String[] args) {
        String text = "Java is fun to learn";
        String[] words = text.split("\\s+");
        System.out.println("String: " + text);
        System.out.println("Word count: " + words.length);
    }
}
