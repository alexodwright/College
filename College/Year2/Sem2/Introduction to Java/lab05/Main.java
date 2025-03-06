import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // arrayLength();
        // average();
        // matrixAddition();
        // tranpose();
        array3d();
    }
    static void arrayLength() {
        Integer[] numbers = {1, 2, 3, 4, 5};
        int i = 0;
        for (Integer n : numbers) {
            i++;
        }
        System.out.println(i);
    }
    static void average() {
        Integer[] numbers = {1, 2, 3, 4, 5};
        double sum = 0;
        for (Integer n : numbers) {
            sum += n;
        }
        double average = sum / numbers.length;
        System.out.println(average);
    }
    static void matrixAddition() {
        int[][] m1 = new int[3][3];
        int[][] m2 = new int[3][3];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[i].length; j++) {
                m1[i][j] = Integer.parseInt(scanner.nextLine());
            }
        }
        for (int i = 0; i < m2.length; i++) {
            for (int j = 0; j < m2[i].length; j++) {
                m2[i][j] = Integer.parseInt(scanner.nextLine());
            }
        }
        int[][] res = new int[3][3];
        for (int i = 0; i < res.length; i++) {
            for (int j = 0; j < res[i].length; j++) {
                res[i][j] = m1[i][j]+ m2[i][j];
            }
        }
        for (int i = 0; i < res.length; i++) {
            for (int j = 0; j < res[i].length; j++) {
            System.out.print(res[i][j] + "\t");
            }
            System.out.println();
        }
        scanner.close();
    }
    static void tranpose() {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        int[][] matrix = new int[n][n];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = Integer.parseInt(scanner.nextLine());
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i + 1; j < matrix.length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
            System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
        scanner.close();
    }
    static void array3d() {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        int[][][] matrix = new int[n][n][n];
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                for (int k = 0; k < matrix[i][j].length; k++) {
                    int input = Integer.parseInt(scanner.nextLine());
                    matrix[i][j][k] = input;
                    numbers.add(input);
                }
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                for (int k = 0; k < matrix[i][j].length; k++) {
                    System.out.print(matrix[i][j][k]);
                }
                System.out.println();
            }
        }
        // check if the user inputs a number if its in the 3d array
        System.out.println("Enter a number to check: ");
        int check = Integer.parseInt(scanner.nextLine());
        if (numbers.contains(check)) {
            System.out.println("Number exists in the 3d array");
        } else {
            System.out.println("Number is not in the 3d array");
        }
        scanner.close();

    }


}
