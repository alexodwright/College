import java.util.Scanner;
public class Program4 {
  public static void main(String[] args) {
    // create the scanner
    Scanner scanner = new Scanner(System.in);
    // take in how many rows
    int n = Integer.parseInt(scanner.nextLine());
    // print every odd iteration with the star in the center and an even amount of space on either side
    for (int i = 1; i <= n;i = i + 2) {
            System.out.println(" ".repeat((n-i)/2) + "*".repeat(i) + " ".repeat((n-i)/2));
        }
    // print the inverse of above
    for (int i = n; i <= n;i = i - 2) {
        if (i != n && i > 0) {
            System.out.println(" ".repeat((n-i)/2) + "*".repeat(i) + " ".repeat((n-i)/2));
        }
    }
    scanner.close();
  }
}
