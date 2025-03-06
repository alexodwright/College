public class Program3 {
  public static void main(String[] args) {
    // print 5 - i spaces on each line followed by i stars
    // increment i on each iteration
    for (int i = 0; i < 5; i++) {
      System.out.println(" ".repeat(5-(i+1)) + "*".repeat(i+1));
    }
  }
}
