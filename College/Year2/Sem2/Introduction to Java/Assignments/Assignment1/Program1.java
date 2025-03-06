import java.util.Scanner;
public class Program1 {
  public static void main(String[] args) {
    // create scanner
    Scanner scanner = new Scanner(System.in);
    // take in year input from user
    int year = Integer.parseInt(scanner.nextLine());
    // if the year is a century year
    if (year % 100 == 0) {
      // if the year is divisible by 400 it is a leap year
      if (year % 400 == 0) {
        System.out.println(String.valueOf(year) + " is a leap year!");
      } else {
        // if the year is a century year but is not divisible by 400 it is not a leap year
        System.out.println(String.valueOf(year) + " is not a leap year!");
      }
    } else if (year % 4 == 0) {
        // if the year is not a century year and is divisible by 4 it is a leap year
        System.out.println(String.valueOf(year) + " is a leap year!");
    } else {
        // if the year is not a century year and is not divisible by 4 it is not a leap year
        System.out.println(String.valueOf(year) + " is not a leap year!");
    }
    scanner.close();
  }
}
