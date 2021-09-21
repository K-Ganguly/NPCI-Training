import java.util.Scanner;
import java.lang.Math;
public class java_basics2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int numDigits = (int)Math.log10(num) + 1;
        if (numDigits == 1)
            System.out.printf("result = %d", numDigits);
        else if (numDigits % 2 == 0)
            System.out.printf("result = %d, %d", numDigits, (int)Math.pow(numDigits, 2));
        else if (numDigits % 3 == 0)
            System.out.printf("result = %d, %d", numDigits, (int)Math.pow(numDigits, 3));
        else 
            System.out.printf("result = %d [%d], %d", numDigits, (numDigits - 1), (int)Math.pow((numDigits - 1), 2));
    }
    
}
