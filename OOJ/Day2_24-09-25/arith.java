import java.util.Scanner;

public class arith {

   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      int var2 = var1.nextInt();
      int var3 = var1.nextInt();
      int var4 = var2 + var3;
      int var5 = var2 - var3;
      int var6 = var2 * var3;
      float var7 = (float)(var2 / var3);
      System.out.println("Result of addition: " + var4);
      System.out.println("Result of subtraction: " + var5);
      System.out.println("Result of multiplication: " + var6);
      System.out.println("Result of division: " + var7);
      var1.close();
   }
}
