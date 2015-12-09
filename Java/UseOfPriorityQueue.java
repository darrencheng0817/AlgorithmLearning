import java.util.Comparator;
import java.util.PriorityQueue;


public class UseOfPriorityQueue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Comparator<Integer> orderIsdn=new Comparator<Integer>() {
			public int compare(Integer i,Integer j) {
				if(i>j) return -1;
				else if(i<j) return 1;
				else return 0;
			}

		};
		PriorityQueue<Integer> queue=new PriorityQueue<Integer>(10,orderIsdn);
		queue.add(1);
		queue.add(5);
		queue.add(3);
		System.out.println(queue.poll());
		System.out.println(queue.poll());
		System.out.println(queue.poll());
	}

}
