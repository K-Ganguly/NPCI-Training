import java.util.Scanner;

public class java_basics5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Taking the Inputs 
        System.out.print("Enter the size of the array : ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            if (max <= arr[i])
                max = arr[i];
            if (min >= arr[i])
                min = arr[i];
        }
        int[] count_arr = new int [max - min + 1];
        
        // Counting the occurrences of each element 
        for (int num : arr )
            count_arr[num - min] += 1;

        // Step 1 : Grouped Together
        int[] groupedTogether = new int[n];
        int[] count_arr_copy = count_arr.clone();
        System.out.print("Step 1 : ");
        for (int i = 0; i < n; i++){
            while (count_arr_copy[arr[i] - min]-- > 0)
                groupedTogether[i++] = arr[i];
        }
        System.out.print("Step 1 : ");
        for (int num : groupedTogether)
            System.out.print(num + ", ");
        System.out.println();

        // Step 2 : Sorted By Value 
        count_arr_copy = count_arr.clone();
        int[] sortedByValue = new int[n];
        for (int i = 0, j = max; i < n; i++){
            while (count_arr_copy[j - min]-- == 0)
                j--;
            sortedByValue[i] = j;
        }
        System.out.print("Step 2 : ");
        for (int num : sortedByValue)
            System.out.print(num + ", ");
        System.out.println();

        // Step 3 : Sorted By Frequency 

        sc.close();
    }
    
}
