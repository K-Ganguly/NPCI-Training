import java.util.Arrays;
import java.util.Scanner;

public class java_oop1_fibSplit {
    static int[] fibSeries;

    public static int fib_1(int n){
        if (fibSeries[n] == -1){
            if (n < 2)
                fibSeries[n] = n;
            else
                fibSeries[n] = fib_1(n - 1) + fib_2(n - 2);    
        }
        return fibSeries[n];
    }

    public static int fib_2(int n){
        if (fibSeries[n] == -1){
            if (n < 2)
                fibSeries[n] = n;
            else
                fibSeries[n] = fib_1(n - 1) + fib_2(n - 2);    
        }
        return fibSeries[n];
        
    }

    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n : ");
        int n = sc.nextInt();
        sc.nextLine();
        
        fibSeries = new int [n];
        Arrays.fill(fibSeries, -1);
        for (int i = 0; i < n; i++){
            if (i % 1 == 0)
                fibSeries[i] = fib_1(i);
            else 
                fibSeries[i] = fib_2(i);
        }

        System.out.print("Printing out the fibonacci Series : ");
        for (int elem : fibSeries)
            System.out.print(elem + " ");
        sc.close();
         
    }
}
