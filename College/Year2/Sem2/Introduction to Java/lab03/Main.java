import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        perfectNumber(28);
        System.out.println(factorial(5));
        System.out.println();
        program3(4);
        System.out.println();
        program4(4);
        System.out.println();
        program5(5);
    }
    static void perfectNumber(int n) {
        ArrayList<Integer> divisors = new ArrayList<Integer>();
        for (int i = 1; i <= n/2; i++) {
            if (n % i == 0) {
                divisors.add(i);
            }
        }
        int total = 0;
        for (int i = 0; i < divisors.size(); i++) {
            total = total + divisors.get(i);
        }
        if (n == total) {
            System.out.println("The number is a perfect number");
        } else {
            System.out.println("The number is not a perfect number");
        }
        System.out.println(divisors);
    }
    static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    static void program3(int n) {
        for (int i = 1; i <= n; i++) {
            System.out.println("*".repeat(i));
        }
    }
    static void program4(int n) {
        for (int i = 1; i <= n; i++) {
            System.out.println(" ".repeat(n-i) + "*".repeat(i));
        }
    }
    static void program5(int n) {
        for (int i = 1; i <= n;i = i + 2) {
            System.out.println(" ".repeat((n-i)/2) + "*".repeat(i) + " ".repeat((n-i)/2));
        }
        for (int i = n; i <= n;i = i - 2) {
            if (i != n && i > 0) {
                System.out.println(" ".repeat((n-i)/2) + "*".repeat(i) + " ".repeat((n-i)/2));
            }
        }
    }

}
