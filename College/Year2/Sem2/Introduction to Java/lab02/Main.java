package lab02;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");

        interest();
        isavowel("e");
        max();
        leapyear(2023);
        leapyear(2024);
        leapyear(2025);
        addBinary("1011", "1010");
    }
    static void interest() {
        int principle = 15000;
        double rate = 0.055;
        int time = 3;
        System.out.println(principle*rate*time);
    }
    static void isavowel(String vowel) {
        boolean isVowel = false;
        String[] vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"};
        for (int i = 0; i < 10; i++) {
            if (vowel == vowels[i]) {
                System.out.println("The input character was a vowel!");
                isVowel = true;
            }
        }
        if (isVowel == false) {
            System.out.println("The input character was not a vowel");
        }
    }
    static void max() {
        int[] ints = {10, 15, 20};
        int max = ints[0];
        for (int i = 0; i < ints.length; i++) {
            if (ints[i] > max) {}
                max = ints[i];
        }
        System.out.println(max);
    }
    static void leapyear(int year) {
        if ((year % 400) == 0) {
            System.out.println("The input year was a leap year");
        } else if (year % 4 == 0) {
            System.out.println("The input year was a leap year");
        } else {
            System.out.println("The input year was not a leap year");
        }
    }
    static void addBinary(String s1, String s2) {
        int sum = Integer.parseInt(s1, 2) + Integer.parseInt(s2, 2);
        System.out.println(sum);
    }
}
