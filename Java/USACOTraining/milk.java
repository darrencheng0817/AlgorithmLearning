package USACOTraining;

/*
ID: darrenc3
LANG: JAVA
TASK: milk
 */
import java.util.*;
import java.io.*;

public class milk {

	class Data implements Comparable {
		int p, num;

		@Override
		public int compareTo(Object o) {
			Data t = (Data) o;
			if (p < t.p)
				return -1;
			else if (p == t.p)
				return 0;
			return 1;
			// TODO Auto-generated method stub
			// return 0;
		}
	}

	int need, num, tot = 0;
	Data pre[] = new Data[5007];

	public static void main(String[] args) throws IOException {
		new milk().run();

	}

	void run() throws IOException {
		Scanner cin = new Scanner(new FileReader("milk.in"));
		PrintWriter cout = new PrintWriter(new BufferedWriter(new FileWriter(
				"milk.out")));
		need = cin.nextInt();
		num = cin.nextInt();
		for (int i = 1; i <= num; i++) {
			pre[i] = new Data();
			pre[i].p = cin.nextInt();
			pre[i].num = cin.nextInt();
		}
		Arrays.sort(pre, 1, num + 1);
		int start = 0;
		while (need > 0) {
			start++;
			for (int i = 1; i <= pre[start].num; i++) {
				need--;
				tot += pre[start].p;
				if (need == 0)
					break;
			}
		}
		cout.println(tot);
		cout.close();
		System.exit(0);
	}
}