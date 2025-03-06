import java.util.Scanner;

public class Program2 {
  public static void main(String[] args) {
    // create the scanenr
    Scanner scanner = new Scanner(System.in);
    // take in the first binary number and convert it to an integer
    int n1 = Integer.parseInt(scanner.nextLine(), 2);
    int n2 = Integer.parseInt(scanner.nextLine(), 2);
    // compute and print the output
    System.out.println(n1 + n2);
    scanner.close();
  }
}
