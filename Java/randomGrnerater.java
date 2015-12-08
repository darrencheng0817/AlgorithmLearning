import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class randomGrnerater {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 ArrayList<Node> input = new ArrayList<Node>();
		    Node node1=new Node('A',5.0);
		    Node node2=new Node('B',10.0);
		    Node node3=new Node('C',5.0);
		    input.add(node1);
		    input.add(node2);
		    input.add(node3);
		    MyRandom random=new MyRandom(input);
		    
		    System.out.println(random.getChar());
	}

}
	class MyRandom{
	  List<Node> nodes;
	  double sum;
	  MyRandom(List<Node> input){
	      sum=0;
	      nodes=new ArrayList<Node>();
	      for(int i=0;i<input.size();i++){
	        Node tempNode=new Node(input.get(i).value,sum);
	        sum+=input.get(i).weight;
	        nodes.add(tempNode);
	      }
	      for(int i=0;i<input.size();i++){
	        nodes.get(i).weight/=sum;
	      }
	  }
	  public char getChar(){
	      Random rand=new Random();
	      //double randomNum=rand.nextDouble();
	      double randomNum=0.7;
	      int l=0,r=nodes.size();
	      while(nodes.get(l).weight<=randomNum){
	        l++;
	      }
	     return nodes.get(l+1).value;
//	       while(l<r){
//	           int m=l+(r-l)/2;
//	           if(nodes.get(m).weight<randomNum){
//	             l=m+1;
//	           }
//	           else{
//	             r=m-1;
//	           }
//	       }
//	       return nodes.get(l).value;
	  }
	}

	class Node{
	  public char value;
	  public double weight;
	  Node(char value,double weight){
	    this.value=value;
	    this.weight=weight;
	  }
	}