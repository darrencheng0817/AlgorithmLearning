


public class trinaryTree {
	public static treeNode insert(treeNode root,int val){
		if(root==null){
			return new treeNode(val);
		}
		if(val>root.val){
			root.rightNode= insert(root.rightNode, val);
		}
		else if(val<root.val){
			root.leftNode= insert(root.leftNode, val);
		}
		else{
			root.midNode=insert(root.midNode, val);
		}
		return root;
	}
	public static treeNode getSuccessor(treeNode root){
		while(root.leftNode!=null){
			root=root.leftNode;
		}
		return root;
	}
	public static treeNode delete(treeNode root,int val) {
		if(root==null)
			return null;
		if(root.val==val){
			if(root.leftNode==null&&root.midNode==null&&root.rightNode==null){
				return null;
			}
			if(root.midNode!=null){
				root.midNode=delete(root.midNode, val);
			}
			else{ 
				if(root.leftNode!=null&&root.rightNode!=null){
					treeNode tempNode=getSuccessor(root.rightNode);
					root.val=tempNode.val;
					root.rightNode=delete(root.rightNode, tempNode.val);
				}
				else if(root.leftNode!=null){
					return root.leftNode;
				}
				else {
					return root.rightNode;
				}
			}
		}
		else if(root.val>val){
			root.leftNode=delete(root.leftNode, val);
		}
		else{
			root.rightNode=delete(root.rightNode, val);
		}
		return root;
	}
	public static void main(String[] args) {
		treeNode rootNode=null;
		rootNode=insert(rootNode, 7);
		rootNode=insert(rootNode, 10);
		rootNode=insert(rootNode, 10);
		rootNode=delete(rootNode, 10);
		System.out.println("done");
	}

}
class treeNode{
	public int val;
	public treeNode leftNode;
	public treeNode midNode;
	public treeNode rightNode;
	public treeNode(int val) {
		this.val=val;
	}
	
}

