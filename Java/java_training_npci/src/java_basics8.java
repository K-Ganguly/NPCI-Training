import java.util.Scanner;

public class java_basics8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the matrix : (row * col)");
        int row = sc.nextInt();
        int col = sc.nextInt();
        sc.nextLine();
        System.out.println("Enter the elements of the first matrix : ");
        
        int[][] matrix1 = new int[row][col];
        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                matrix1[i][j] = sc.nextInt();
            }
            sc.nextLine();
        }
        System.out.println("Enter the elements of the first matrix : ");
       
        int[][] matrix2 = new int[row][col];
        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                matrix2[i][j] = sc.nextInt();
            }
            sc.nextLine();
        }

        System.out.println("\nDisplaying the resultant matrix : ");
        int[][] sumMatrix = new int[row][col];
        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                sumMatrix[i][j] = matrix1[i][j] + matrix2[i][j];
                System.out.print(sumMatrix[i][j] + " ");
            }
            System.out.println();
        }

        sc.close();
    }
    
}
