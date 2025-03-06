package lab04;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static void main(String[] args) {
        // EvenOdds();
        // StandardDeviation();
        // Alphabetical();
        // QuotientRemainder();
        Power();
    }
    static void EvenOdds() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter 10 numbers: ");

        int evens = 0;
        int odds = 0;

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(scanner.nextLine());
            if (n % 2 == 0) {
                evens++;
            } else {
                odds++;
            }
        }
        System.out.println("User inputted " + evens + " evens and " + odds + " odds");
        scanner.close(); 
    }
    static void StandardDeviation() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter n: ");
        
        int n = Integer.parseInt(scanner.nextLine());
        double sum = 0;
        
        System.out.println("Enter n numbers: ");
        ArrayList<Integer> array = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(scanner.nextLine());
            array.add(number);
            sum += number;
        }

        double mean = (sum / n);

        double stdevsum = 0;

        for (int i = 0; i < n; i++) {
            stdevsum += Math.pow((array.get(i) - mean), 2);
        }

        double s = Math.sqrt(stdevsum / n);
        System.out.println("The standard deviation is: " + s);
        
        scanner.close();
    }
    static void Alphabetical() {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<String>();

        System.out.println("Enter 10 names: ");

        for (int i = 0; i < 10; i++) {
            names.add(scanner.nextLine());
        }
        names.sort(null);
        System.out.println(names);

        scanner.close();
    }
    static void QuotientRemainder() {
        Scanner scanner = new Scanner(System.in);

        double dividend = Double.parseDouble(scanner.nextLine());
        double divisor = Double.parseDouble(scanner.nextLine());

        int quotient = (int)Math.round(Math.floor(dividend/divisor));
        int remainder = (int)Math.round(dividend % divisor);

        System.out.println("The quotient is " + quotient);
        System.out.println("The remainder is " + remainder);

        scanner.close();
    }
    static void Power() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the base: ");
        double base = Double.parseDouble(scanner.nextLine());

        System.out.println("Enter the exponent");
        double exponent = Double.parseDouble(scanner.nextLine());

        double res = 0;

        for (int i = 0; i < exponent; i++) {
            res = res + (base * exponent);
        }
        System.out.println("The result is: " + res);

        scanner.close();
    }
}
