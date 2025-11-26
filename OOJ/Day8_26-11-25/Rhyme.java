public class Rhyme {
    public static void main(String[] args) {
        char[] chars = {'l','i','t','t','l','e',' ','l','a','m','b',',','l','i','t','t','l','e',' ','l','a','m','b'};
        byte[] bytes = "Mary had a little lamb".getBytes();
        StringBuilder sb = new StringBuilder("it's fleece was white as snow");

        String s1 = new String("Mary had a little lamb");
        String s2 = new String(chars);
        String s3 = new String(bytes);
        String s4 = new String(sb);

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        System.out.println(s4);
        
        int len = s1.length() + s2.length() + s3.length() + s4.length();
        System.out.println("Total Length: " + len);
    }
}
