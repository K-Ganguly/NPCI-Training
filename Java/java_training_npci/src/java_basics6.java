import java.util.Scanner;

public class java_basics6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the matrix : (row * col)");
        int row = sc.nextInt();
        int col = sc.nextInt();
        sc.nextLine();
        System.out.println("Enter the elements of the matrix : ");
        int dir = 1;
        int[][] matrix = new int[row][col];
        for (int i = 0; i < row; i++){
            if (Math.pow(-1, dir++) == -1){
                for (int j = 0; j < col; j++){
                    matrix[i][j] = sc.nextInt();
                }
            }
            else {
                for (int j = col - 1; j >= 0; j--)
                    matrix[i][j] = sc.nextInt();
            }
            sc.nextLine();
        }
        System.out.println("\nDisplaying the matrix : ");
        for (int[] rowOfMatrix : matrix ){
            for (int element : rowOfMatrix)
                System.out.print(element + "\t");
            System.out.println();
        }
        sc.close();
    }
    
}
