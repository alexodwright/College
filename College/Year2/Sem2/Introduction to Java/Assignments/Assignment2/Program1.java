import java.util.Scanner;
import java.util.ArrayList;

public class Program1 {
  public static void main(String[] args) {
    // create the scanner
    Scanner scanner = new Scanner(System.in);
    // create the arraylist of type string
    ArrayList<String> names = new ArrayList<String>();
    // add 10 names from the user to the arraylist names
    for (int i = 0; i < 10; i++) {
      names.add(scanner.nextLine());
    }
    // sort the list using the default comparator which is alphabetically for strings
    names.sort(null);
    // print the output
    System.out.println(names);
    scanner.close();
  }
}
