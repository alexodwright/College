import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // program1();
        // program2();
        // program3();
        program4();
    }
    static void program1() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter string for problem 1: ");
        String string = scanner.nextLine();
        Map<String, Integer> count = new HashMap<>();
        for (int i = 0; i < string.length(); i++) {
            String letter = String.valueOf(string.charAt(i));
            if (!count.containsKey(letter)) {
                count.put(letter, 1);
            } else {
                count.put(letter, count.get(letter)+1);
            }
        }
        System.out.println(count);
        scanner.close();
    }
    static void program2() {
        System.out.println("Enter string for problem 2: ");
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        string = string.replaceAll("\\s+","");
        System.out.println(string);
        scanner.close();
    }
    static void program3() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter string for problem 3: ");
        String string = scanner.nextLine();
        System.out.println("Enter string 2 for problem 3: ");
        String string2 = scanner.nextLine();
        Map<String, Integer> count = new HashMap<>();
        Map<String, Integer> count2 = new HashMap<>();
        for (int i = 0; i < string.length(); i++) {
            String letter = String.valueOf(string.charAt(i));
            if (!count.containsKey(letter)) {
                count.put(letter, 1);
            } else {
                count.put(letter, count.get(letter)+1);
            }
        }
        for (int i = 0; i < string2.length(); i++) {
            String letter2 = String.valueOf(string2.charAt(i));
            if (!count2.containsKey(letter2)) {
                count2.put(letter2, 1);
            } else {
                count2.put(letter2, count2.get(letter2)+1);
            }
        }
        if (count.equals(count2)) {
            System.out.println("The strings are anagrams");
        } else {
            System.out.println("The strings are not anagrams");
        }
        scanner.close();
    }
    static void program4() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter n: ");
        int n = Integer.parseInt(scanner.nextLine());
        System.out.println("Enter a string to split into n parts: ");
        // pad the string with extra spaces if it is not a multiple of n 
        String string = scanner.nextLine();
        while (string.length()%n!=0) {
            string += " ";
        }
        for (int i = 0; i < string.length()/n; i++) {
            System.out.println(string.substring(i*n, (i+1)*n));
        }
        scanner.close();
    }
}
