import java.util.Scanner;

public class java_basics7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the height of the tower : ");
        int h = sc.nextInt(); 
        int value = 1, increase = 0;
        for (int i = 1; i <= h; i++){
            int space = h;
            while (space-- > 0)
                System.out.print(" ");
            for (int j = 1; j <= i; j++){
                System.out.print(value);
                increase += value;
            }
            value += increase;
            h--;
            System.out.println();  
        }
        sc.close();
    }
}
