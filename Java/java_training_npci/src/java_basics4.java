import java.util.Scanner;

public class java_basics4 {

    public static int[] fib_rev(int n){
        int[] fibSeries = new int[n];
        fibSeries[n - 1] = 0;
        fibSeries[n - 2] = 1;
        for(int i = n - 3; i > -1; i--){
            fibSeries[i] = fibSeries[i + 1] + fibSeries[i + 2];
        }
        return fibSeries;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n : ");
        int n = sc.nextInt();
        int[] fib_series_rev = fib_rev(n);
        for(int element : fib_series_rev){
            System.out.print(element + ", ");
        }
        System.out.println();
        sc.close();
    }   
}
