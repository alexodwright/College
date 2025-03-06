import java.util.Scanner;

public class Program3 {
  public static void main(String[] args) {
    // create the scanner
    Scanner scanner = new Scanner(System.in);

    // take in the base and exponent from the user
    int base = Integer.parseInt(scanner.nextLine());
    int exponent = Integer.parseInt(scanner.nextLine());

    // multiply the base by itself exponent number of times
    int power = base;
    for (int i = 0; i < exponent-1; i++) {
      power *= base;
    }
    // output the result
    System.out.println(base + " to the power of " + exponent + " is: " + power);

    scanner.close();
  }
}
