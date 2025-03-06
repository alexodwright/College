import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;

public class Main {
  public static void main(String[] args) {
    //program1();
    //program2();
    program3();
  }

  static ArrayList<String> program1() {
    Scanner scanner = new Scanner(System.in);
    String string = scanner.nextLine();
    ArrayList<String> substrings = new ArrayList<String>();
    for (int i = 0; i < string.length(); i++) {
      for (int j = i; j < string.length() + 1; j++) {
        if (i != j && !substrings.contains(string.substring(i, j))) {
          substrings.add(string.substring(i, j));
        }
      }
    }
    for (String s : substrings) {
      System.out.println("-" + s);
    }
    scanner.close();
    return substrings;
  }

  static void program2() {
    ArrayList<String> substrings = program1();
    // lenNoRpts is a list where at index i, is the length in that substring with no dpulicates
    int[] lenNoRpts = new int[substrings.size()];
    for (int index = 0; index < substrings.size(); index++) {
      String s = substrings.get(index);
      String[] lettersUsed = new String[s.length()];
      int len = 0;
      for (int i = 0; i < s.length(); i++) {
        String letter = String.valueOf(s.charAt(i));
        if (!Arrays.asList(lettersUsed).contains(letter)) {
          lettersUsed[i] = letter;
          len++;
        } else {
          break;
        }
      }
      lenNoRpts[index] = len;
    }
    int maxIdx = 0;
    int maxVal = 0;
    for (int i = 0; i < lenNoRpts.length; i++) {
      if (lenNoRpts[i] > maxVal) {
        maxIdx = i;
        maxVal = lenNoRpts[i];
      }
    }
    System.out.println(java.util.Arrays.toString(lenNoRpts));
    System.out
        .println("The substring with the longest length with no duplicate characters is: " + substrings.get(maxIdx));
  }

  static void program3() {
    Scanner scanner = new Scanner(System.in);
    String s = scanner.nextLine();
    // Create a dictionary in which the key is the index of the starting character,
    // and the value is how many characters after the key the character is still the same.
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int i = 0; i < s.length(); i++) {
      int count = 0;
      for (int j = i; j < s.length(); j++) {
        if (s.charAt(i) == s.charAt(j)) {
          count++;
        } else {
          break;
        }
      }
      map.put(i, count);
    }
    // get the key of the max value
    int maxKey = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
    // map.forEach((key, value) -> System.out.println(key + ": " + value));

    // print out the substring from the key to map[key] letters after the s[key]
    System.out.println(s.substring(maxKey, maxKey + map.get(maxKey)));
    scanner.close();
  }
}
