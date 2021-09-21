import java.util.Scanner;

public class java_basics {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        sc.nextLine();
        boolean isSq = (num1 * num1) == num2;
        boolean isMultiple = (num2 % num1) == 0;
        int multiples = num2 / num1;
        if (isSq)
            System.out.println(num2 + " is a square and multiple of " + num1);
        else if (isMultiple)
            System.out.println(num2 + " is a multiple of " + num1 + " = " + multiples + "s of " + num1);
        else 
            System.out.println(num2 + " is neither a square nor multiple of " + num1);
    }
}
