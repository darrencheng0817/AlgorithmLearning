public class KStacks {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		myStacks stacks=new myStacks(10, 3);
		stacks.push(23, 1);
		System.out.println(stacks.pop(1));
		stacks.pop(0);
		
	}

}
class myStacks {
	private int[] stack;
	private int[] top;
	private int[] next;
	private int free;
	
	public myStacks(int n,int k) {
		// TODO Auto-generated constructor stub
		stack=new int[n];
		top=new int[k];
		next=new int[n];
		for (int i = 0; i < top.length; i++) {
			top[i]=-1;
		}
		for (int i = 0; i < next.length; i++) {
			next[i]=i+1;
		}
		next[next.length-1]=-1;
		free=0;
	}
	public boolean push(int item,int stackN) {
		if(stackN>=top.length){
			System.err.println("Invalid input!");
			return false;
		}
		if(isFull())
			return false;
		// Store index of first free slot
		int i=free;
		// Update index of free slot to index of next slot in free list
		free=next[i];
		// Update next of top and then top for stack number 'N'
		next[i]=top[stackN];
		top[stackN]=i;
		// Put the item in array
		stack[i]=item;
		return true;
		
	}
	public  boolean isEmpty(int stackN) {
		return top[stackN]==-1;
	}
	public int pop(int stackN) {
		if(isEmpty(stackN)){
			System.err.println("Stack is Empty!");
			return -1;}
		// Find index of top item in stack number 'N'
		int i=top[stackN];
		// Change top to store next of previous top
		top[stackN]=next[i];
		// Attach the previous top to the beginning of free list
		next[i]=free;
		free=i;
		// Return the previous top item
		return stack[i];
	}
	public int peek(int stackN) {
		if(isEmpty(stackN)){
			System.err.println("Stack is empty!");
			return -1;
		}
		return top[stackN];
	}
	public boolean isFull() {
		return free==-1;
	}

}
