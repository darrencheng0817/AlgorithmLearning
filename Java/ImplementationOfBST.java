
public class ImplementationOfBST {
	public static BST search(BST root,int target) {
		if(root==null||root.val==target)
			return root;
		if(root.val<target){
			return search(root.right, target);
		}
		else {
			return search(root.left, target);
		}
	}
	public static BST insert(BST root,int target) {
		if(root==null){
			return new BST(target);
		}
		if(root.val<target){
			root.right= insert(root.right, target);
		}
		else {
			root.left= insert(root.left, target);
		}
		return root;
	}
	public static BST deleteNode(BST root, int key)
	{
	    // base case
	    if (root == null) return root;
	 
	    // If the key to be deleted is smaller than the root's key,
	    // then it lies in left subtree
	    if (key < root.val)
	        root.left = deleteNode(root.left, key);
	 
	    // If the key to be deleted is greater than the root's key,
	    // then it lies in right subtree
	    else if (key > root.val)
	        root.right = deleteNode(root.right, key);
	 
	    // if key is same as root's key, then This is the node
	    // to be deleted
	    else
	    {
	        // node with only one child or no child
	        if (root.left == null)
	        {
	            return root.right;
	        }
	        else if (root.right == null)
	        {
	            return root.left;
	        }
	 
	        // node with two children: Get the inorder successor (smallest
	        // in the right subtree)
	        BST temp= minValueNode(root.right);
	 
	        // Copy the inorder successor's content to this node
	        root.val = temp.val;
	 
	        // Delete the inorder successor
	        root.right = deleteNode(root.right, temp.val);
	    }
	    return root;
	}
	public static BST minValueNode(BST root) {
		if(root==null)
			return root;
		while(root.left!=null){
			root=root.left;
		}
		return root;
	}
	public static void main(String[] args) {
		BST treeBst=new BST(12);
		insert(treeBst, 10);
		insert(treeBst, 23);
		insert(treeBst, 5);
		System.out.println(search(treeBst, 5).val);
		deleteNode(treeBst, 23);
		System.out.println(search(treeBst, 5)==null?0:1);
	}
}
class BST{
	int val;
	BST left;
	BST right;
	public BST(int val) {
		// TODO Auto-generated constructor stub
		this.val=val;
	}
}