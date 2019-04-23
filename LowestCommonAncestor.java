class Node{
    int val;
    Node left;
    Node right;

    Node(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Main{
    static Node LCA(Node root, Node p, Node q){
        if (root == null){
            return null;
        }
        if ((root.val == p.val) || (root.val == q.val)){
            return root;
        }
        Node left = LCA(root.left, p, q);
        Node right = LCA(root.right, p, q);

        // if ((left == null) && (right == null)){
        //     return null;
        // }
        if ((left != null) && (right != null)){
            return root;
        }
        if ((left != null)){
            return left;
        }
        if ((right != null)){
            return right;
        }
        return null;
    }
    public static void main(String[] args){
        Node root = new Node(3);
        root.left = new Node(5);
        root.right = new Node(1);
        root.left.left = new Node(6);
        root.left.right = new Node(2);
        root.right.left = new Node(0);
        root.right.right = new Node(8);
        root.left.right.left = new Node(7);
        root.left.right.right = new Node(4);

        Node result = LCA(root, new Node(6), new Node(2));
        System.out.println(result.val);
    }
}
