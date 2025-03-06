import java.util.Arrays;
import java.util.Scanner;

public class LinkedList {
    Node first;
    int size;

    LinkedList() {
        this.first = null;
        this.size = 0;
    }

    public void appendToEnd(int element) {
        if (this.first == null) {
            this.first = new Node(element);
        } else {
            Node node = this.first;
            while (node.next != null) {
                node = node.next;
            }
            node.next = new Node(element);
        }
        this.size++;
    }

    static void printLL(LinkedList ll) {
        Node n = ll.first;
        if (n == null) {
            return;
        }
        while (n.next != null) {
            System.out.print(n.element + ", ");
            n = n.next;
        }
        System.out.print(n.element + "\n");
    }

    public void insertAtIndex(int element, int i) {
        int index = 0;
        Node newNode;
        this.size++;
        if (i == 0) {
            newNode = new Node(element);
            newNode.next = this.first;
            this.first = newNode;
            return;
        }
        Node nodeBefore = this.first;
        while (index < i-1) {
            nodeBefore = nodeBefore.next;
            index++;
        }
        newNode = new Node(element);
        newNode.next = nodeBefore.next;
        nodeBefore.next = newNode;
    }
    public void deleteAtIndex(int i) {
        if (i == 0) {
            this.first = this.first.next;
        } else {
            int index = 0;
            Node n = this.first;
            while (index < i-1) {
                n = n.next;
                index++;
            }
            n.next = n.next.next;
        }
        this.size--;
    }

    public static void main(String[] args) {        
        // program3();
        // userInputLL();
        LinkedList testLL = new LinkedList();
        testLL.appendToEnd(0);
        testLL.appendToEnd(1);
        testLL.appendToEnd(2);
        testLL.appendToEnd(3);
        testLL.appendToEnd(4);
        linkedToArrayList(testLL);
    }
    static void program3() {
        LinkedList ll = new LinkedList();

        ll.appendToEnd(11);
        ll.appendToEnd(22);
        ll.appendToEnd(6);
        ll.appendToEnd(89);
        ll.appendToEnd(99);

        printLL(ll);

        ll.insertAtIndex(50, 2);
        printLL(ll);
        
        ll.deleteAtIndex(1);
        printLL(ll);

        ll.deleteAtIndex(0);
        printLL(ll);

        ll.deleteAtIndex(ll.size-1);
        printLL(ll);
    }
    static void userInputLL() {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        LinkedList userLL = new LinkedList();
        for (int i = 0; i < n; i++) {
            userLL.appendToEnd(Integer.parseInt(scanner.nextLine()));
        }
        printLL(userLL);
        scanner.close();
    }
    static void linkedToArrayList(LinkedList ll) {
        int[] arr = new int[ll.size];
        Node n = ll.first;
        if (n == null) {
            return;
        } else {
            for (int i = 0; i < ll.size; i++) {
                arr[i] = n.element;
                n = n.next;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
class Node {
    int element;
    Node next = null;

    Node(int element) {
        this.element = element;
    }
}