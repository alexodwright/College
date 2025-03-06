import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    program1();
    // program2();
  }
  static void program1() {
    ArrayList<String> subjects = new ArrayList<String>();
    subjects.add("Cryptography");
    subjects.add("Database");
    subjects.add("OS");
    subjects.add("Networking");

    for (int i = 0; i < subjects.size(); i++) {
      if (subjects.get(i) == "Networking") {
        subjects.remove(i);
      }
    }
    subjects.sort( (a, b) -> { return -1 * a.compareTo(b);});
    System.out.println(subjects);
  }
  static void program2() {
    ArrayList<String> subjects = new ArrayList<String>();
    Scanner scanner = new Scanner(System.in);
    int n = Integer.parseInt(scanner.nextLine());
    for (int i = 0; i < n; i++) {
      subjects.add(scanner.nextLine());
    }
    for (int i = 0; i < subjects.size(); i++) {
      if ("Networking".equals(subjects.get(i))) {
        subjects.remove(i);
      }
    }
    System.out.println(subjects);
    scanner.close();
  }
}
