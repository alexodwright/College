import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    ArrayList<String> names = new ArrayList<String>();
    names.add("John D");
    names.add("John e");
    names.add("John o");
    for (String name : names) {
    System.out.println(name);
    }
    System.out.println();
    for (int i = 0; i < names.size(); i++) {
    System.out.println(names.get(i));
    }
  }
}
