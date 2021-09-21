import java.util.Scanner;

public class java_basics3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.next();
        boolean isPoint = false;
        sc.nextLine();

        for (int i = 0, l = num.length(); i < l; i++) {
            if (num.charAt(i) == '.')
                isPoint = true;
        }

        if (isPoint) {
            double numVal = Double.parseDouble(num);
            if (numVal >= Float.MIN_VALUE && numVal <= Float.MAX_VALUE){
                System.out.println("Type : float");
            }
            else {
                System.out.println("Type : double");
            }
        }
        else {
            long numVal = Long.parseLong(num);
            if (numVal >= Byte.MIN_VALUE && numVal <= Byte.MAX_VALUE){
                System.out.println("Type : byte");
            }
            else if (numVal >= Short.MIN_VALUE && numVal <= Short.MAX_VALUE){
                System.out.println("Type : short");
            }
            else if (numVal >= Integer.MIN_VALUE && numVal <= Integer.MAX_VALUE){
                System.out.println("Type : int");
            }
            else {
                System.out.println("Type : long");
            }
        }
        sc.close();
    }
}
