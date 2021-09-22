import java.util.Scanner;

public class java_basics7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the height of the tower : ");
        int h = sc.nextInt(); 
        int value = 1, increase = 0, d = h;
        for (int i = 1; i <= h; i++){
            int space = d;
            while (--space > 0)
                System.out.print(" ");
            for (int j = 0; j < i; j++){
                System.out.print(value + " ");
                increase += value;
            }
            if (value == 1)
                value = 2;
            else
                value = increase;
            d--;
            System.out.println();  
        }
        sc.close();
    }
}
