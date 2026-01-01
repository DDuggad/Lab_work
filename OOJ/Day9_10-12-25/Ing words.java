public class IngWords {
    public static void main(String[] args) {
        String para = "I was walking and singing in the morning rain";
        String[] words = para.split(" ");
        
        System.out.println("Paragraph: " + para);
        System.out.print("Words ending with ing: ");
        
        for (String w : words) {
            if (w.endsWith("ing")) {
                System.out.print(w + " ");
            }
        }
    }
}
