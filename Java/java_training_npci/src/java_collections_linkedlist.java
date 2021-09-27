class LinkedList {
    static class Node {
        int data;
        Node next;

        Node() {
            data = 0;
            next = null;
        }

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    static int count = 0;
    Node head = null;

    void addNode(int val) {
        count += 1;
        Node node = new Node(val);
        Node curr = this.head;

        if (this.head == null) {
            this.head = node;
        } else {
            while (curr.next != null) {
                curr = curr.next;
            }

            curr.next = node;
        }
    }

    int deleteNode(int val) {
        count -= 1;
        Node curr = head;

        if (curr.data == val) {
            Node temp = curr;
            curr = null;
            return temp.data;
        }

        while (curr.next.data != val) {
            curr = curr.next;
        }

        Node temp = curr.next;
        curr.next = curr.next.next;
        return temp.data;
    }

    int[] giveArray() {
        int[] arr = new int[count];
        Node curr = head;
        int i = 0;

        while (curr != null) {
            arr[i] = curr.data;
        }

        return arr;
    }
}

public class java_collections_linkedlist {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.addNode(1);
        ll.addNode(2);
        ll.addNode(34);
        ll.addNode(21);
        int[] arr = ll.giveArray();
        for (int elem: arr)
            System.out.print(elem + " ------> ");
        System.out.print("Null\n");
    }

}