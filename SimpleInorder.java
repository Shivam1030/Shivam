public class SimpleInorder {
    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    public static void inorder(Node root) {
        if (root == null)
            return;

        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    public static void main(String[] args) {

        Node root = new Node(2);
        root.left = new Node(1);
        root.right = new Node(3);

        System.out.print("Inorder output: ");
        inorder(root);
    }
}
