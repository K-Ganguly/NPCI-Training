import java.util.Scanner;

public class java_basics3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.next();
        boolean isPoint = false;
        sc.nextLine();

        for (int i = 0, l = num.length(); i < l; i++) {
            if (num.charAt(i) == '.'){
                isPoint = true;
                break;
            }
        }

        if (isPoint) {
            double numVal = Double.parseDouble(num);
            if (numVal >= Float.MIN_VALUE && numVal <= Float.MAX_VALUE){
                float val = (float)numVal;
                System.out.printf("Type of %f is : <float>", val);
            }
            else {
                System.out.printf("Type of %f is : <double>", numVal);
            }
        }
        else {
            long numVal = Long.parseLong(num);
            if (numVal >= Byte.MIN_VALUE && numVal <= Byte.MAX_VALUE){
                byte val = (byte)numVal;
                System.out.printf("Type of %d is : <byte>", val);
            }
            else if (numVal >= Short.MIN_VALUE && numVal <= Short.MAX_VALUE){
                short val = (byte)numVal;
                System.out.printf("Type of %d is : <short>", val);
            }
            else if (numVal >= Integer.MIN_VALUE && numVal <= Integer.MAX_VALUE){
                int val = (byte)numVal;
                System.out.printf("Type of %d is : <int>", val);
            }
            else {
                System.out.printf("Type of %f is : <long>", numVal);
            }
        }
        sc.close();
    }
}
