import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // charToString();
        // stringToChar();
        // reverseString();
        // duplicateChars();
        palindrome();
    }
    static void charToString() {
        Scanner scanner = new Scanner(System.in);
        char c = scanner.nextLine().charAt(0);
        System.out.println(String.valueOf(c));
        scanner.close();
    }
    static void stringToChar() {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        System.out.println(s.charAt(0));
        scanner.close();
    }
    static void reverseString() {
        Scanner scanner = new Scanner(System.in);
        String r = "";
        String s = scanner.nextLine();

        for (int i = 0; i < s.length(); i++) {
            r = s.charAt(i) + r;
        }

        System.out.println(r);

        scanner.close();

    }
    static void duplicateChars() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter string for duplicateChars: ");
        String s = scanner.nextLine();
        Map<String, Integer> count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            String letter = String.valueOf(s.charAt(i));
            if (!count.containsKey(letter)) {
                count.put(letter, 1);
            } else {
                count.put(letter, count.get(letter)+1);
            }
        }
        for (Map.Entry<String, Integer> e : count.entrySet()) {
            String k = e.getKey();
            Integer v = e.getValue();
            if (v > 1) {
                System.out.println("The character " + k + " has duplicates!");
            }
        }
        System.out.println(count);


        scanner.close();
    }
    static void palindrome() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string to check for a palindrome: ");
        String string = scanner.nextLine();
        Stack<String> stack = new Stack<>();
        // iterate across the string and add to the stack
        for (int i = 0; i < string.length(); i++) {
            stack.push(String.valueOf(string.charAt(i)));
        }
        Boolean isPalindrome = true;
        for (int i = 0; i < string.length(); i++) {
            if (!String.valueOf(string.charAt(i)).equals(stack.pop())) {
                isPalindrome = false;
                break;
            }
        }
        if (isPalindrome) {
            System.out.println("The string was a palindrome!");
        } else {
            System.out.println("The string was not a palindrome!");
        }
        scanner.close();
    }
}   
