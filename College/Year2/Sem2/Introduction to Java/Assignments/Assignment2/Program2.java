import java.util.Scanner;

public class Program2 {
  public static void main(String[] args) {
    // create the scanner
    Scanner scanner = new Scanner(System.in);
    // input the dividend and the divisor from the user
    int dividend = Integer.parseInt(scanner.nextLine());
    int divisor = Integer.parseInt(scanner.nextLine());

    // calculate the quotient and the remainder
    double quotient = Math.floor(dividend/divisor);
    double remainder = dividend - (quotient * divisor);

    // output the results
    System.out.println(dividend + " / " + divisor);
    System.out.println("The quotient is: " + quotient);
    System.out.println("The remainder is: " + remainder);
    scanner.close();
  }
}
