import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class implementSingleton {

	public static void main(String[] args) {

		Singleton singleton1 = Singleton.getInstance();
		Singleton singleton2 = Singleton.getInstance();
		singleton1.doSomethings();
		singleton2.doSomethings();
	}

}

class Singleton {
	private static Singleton singleton = null;
	private static int num = 2;

	// 私有的构造函数，限制外部环境的非法创建和访问
	private Singleton() {
		// 一些初始化操作
		num++;
	}

	// 静态方法，用于创建单例类的“唯一”实例
	public static synchronized Singleton getInstance() {
		if (singleton == null) {
			singleton = new Singleton();
		}
		return singleton;
	}

	// 单例类也需要提供其他静态方法给外部环境访问，完成一定的服务
	public void doSomethings() {
		System.out.println("do somethings " + num);
	}
}

class Singleton03 {
	private final static int MAX_NUM_OF_INSTANCE = 3;
	private static List<Singleton03> singletonList = new ArrayList<Singleton03>();
	// 以静态代码块的方式来初始化一定数量的单例对象
	static {
		for (int i = 0; i < MAX_NUM_OF_INSTANCE; i++) {
			singletonList.add(new Singleton03());
		}
	}

	public static Singleton03 getInstance() {
		// 从单例类已持有的实例中随机取出一个实例
		Random random = new Random();
		int id = random.nextInt(MAX_NUM_OF_INSTANCE);
		return singletonList.get(id);
	}

	private Singleton03() {
		// 一些初始化操作
	}

	public void doSomethings() {
		System.out.println("do somethings ...");
	}
}

// 自动初始化，这样肯定不会造成多个实例，但是如果实际没有用到的话也会初始化实例，浪费了资源
class Singleton3 {
	private static Singleton3 uniqueInstance = new Singleton3();

	private Singleton3() {
	}

	public static Singleton3 getInstance() {
		return uniqueInstance;
	}
}

// 使用内部类的方法可以解决过早初始化的问题
class Singleton5 {

	private Singleton5() {
	}

	public static Singleton5 getInstance() {
		return Nested.instance;
	}

	static class Nested {
		static Singleton5 instance = new Singleton5();
	}
}
//用于多线程的改进方法如下
class Singleton6 {
	private volatile static Singleton6 uniqueInstance;

	private Singleton6() {
	}

	public static Singleton6 getInstance() {
		if (uniqueInstance == null) {
			synchronized (Singleton6.class) {
				if (uniqueInstance == null) {
					uniqueInstance = new Singleton6();
				}
			}
		}
		return uniqueInstance;
	}
}
