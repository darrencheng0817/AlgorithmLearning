import java.util.LinkedList;
import java.util.Queue;


public class BlockingQueue<T> {
	private Queue<T> q = new LinkedList<T>();
    private int limit;

    public BlockingQueue(int limit) {
        this.limit = limit;
    }

    public synchronized void put (T t) throws InterruptedException {
        while (isFull()) {
            wait();
        }
        boolean e = isEmpty();
        q.add(t);
        if (e)
            notifyAll();
    }


    public synchronized T get () throws InterruptedException {
        while (isEmpty()) {
            wait();
        }
        boolean f = isFull();
        T t = q.poll();
        if (f)
            notifyAll();
        return t;
    }

    private boolean isEmpty() {
        return q.size() == 0;
    }
    private boolean isFull() {
        return q.size() == limit;
    }
}
