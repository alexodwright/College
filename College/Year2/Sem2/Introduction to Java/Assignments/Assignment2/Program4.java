import java.util.Scanner;

public class Program4 {
  public static void main(String[] args) {
    // create the scanner
    Scanner scanner = new Scanner(System.in);

    // create 2 2d arrays of integers
    int[][] m1 = new int[3][3];
    int[][] m2 = new int[3][3];

    // populate the first matrix with values from the user
    for (int i = 0; i < m1.length; i++) {
      for (int j = 0; j < m1[i].length; j++) {
    System.out.println("Enter matrix 1 row " + (i+1) + " col " + (j+1) + ": ");
        m1[i][j] = Integer.parseInt(scanner.nextLine());
      }
    }
    // populate the second matrix with values from the user
    for (int i = 0; i < m2.length; i++) {
      for (int j = 0; j < m2[i].length; j++) {
    System.out.println("Enter matrix 2 row " + (i+1) + " col " + (j+1) + ": ");
        m2[i][j] = Integer.parseInt(scanner.nextLine());
      }
    }

    // create the result matrix
    int[][] res = new int[3][3];

    // populate each entry of the result matrix with the results and output them
    for (int i = 0; i < res.length; i++) {
      System.out.println();
      for (int j = 0; j < res[i].length; j++) {
        res[i][j] = m1[i][j] + m2[i][j];
        System.out.print(res[i][j] + " ");
      }
    }
    scanner.close();
  }
}
