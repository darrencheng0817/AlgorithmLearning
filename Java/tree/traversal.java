package tree;

import java.util.Stack;

public class traversal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		treeNode rootNode=new treeNode(5);
		rootNode.leftNode=new treeNode(4);
		rootNode.rightNode=new treeNode(9);
		inOrder(rootNode);
		inOrder2(rootNode);
		preOrder(rootNode);
		preOrder2(rootNode);
		postOrder(rootNode);
		postOrder2(rootNode);
		
	}
	public static void inOrder(treeNode root) {
		if(root==null)
			return;
		inOrder(root.leftNode);
		System.out.println(root.val);
		inOrder(root.rightNode);
	}
	public static void preOrder(treeNode root) {
		if(root==null)
			return;
		System.out.println(root.val);
		preOrder(root.leftNode);
		preOrder(root.rightNode);
	}
	public static void postOrder(treeNode root) {
		if(root==null)
			return;
		postOrder(root.leftNode);
		postOrder(root.rightNode);
		System.out.println(root.val);
	}
	public static void inOrder2(treeNode root) {
		System.out.println("Inorder 2");
		Stack<treeNode> stack=new Stack<>();
		while(root!=null||!stack.isEmpty()){
			if(root!=null){
				stack.push(root);
				root=root.leftNode;
			}
			else{
				root=stack.pop();
				System.out.println(root.val);
				root=root.rightNode;
			}
		}
		System.out.println("Done!");
	}
	public static void preOrder2(treeNode root) {
		System.out.println("PreOrder 2");
		Stack<treeNode> stack=new Stack<>();
		while(root!=null||!stack.isEmpty()){
			if(root!=null){
				System.out.println(root.val);
				stack.push(root);
				root=root.leftNode;
			}
			else{
				root=stack.pop();
				root=root.rightNode;
			}
		}
		System.out.println("Done!");
	}
	public static void postOrder2(treeNode root) {
		System.out.println("PostOrder 2");
		Stack<treeNode> stack=new Stack<>();
		treeNode preNode=null;
		while(root!=null||!stack.isEmpty()){
			if(root!=null){
				stack.push(root);
				root=root.leftNode;
			}
			else{
				//1）如果当前栈顶元素的右结点存在并且还没访问过（也就是右结点不等于上一个访问结点），那么就把当前结点移到右结点继续循环；
				//2）如果栈顶元素右结点是空或者已经访问过，那么说明栈顶元素的左右子树都访问完毕，应该访问自己继续回溯了。
				treeNode peekNode=stack.peek();
				if(peekNode.rightNode!=null&&peekNode.rightNode!=preNode){
					root=peekNode.rightNode;
				}
				else{
					stack.pop();
					System.out.println(peekNode.val);
					preNode=peekNode;
				}
			}
		} 
		System.out.println("Done!");
	}
}

class treeNode{
	int val;
	treeNode leftNode;
	treeNode rightNode;
	treeNode(int val){
		this.val=val;
	}
}