package USACOTraining;

/*
ID: darrenc
LANG: JAVA
TASK: milk2
 */
import java.io.*;
import java.util.*;

class Interval {
	int st, en;

	public Interval(int st, int en) {
		this.st = st;
		this.en = en;
	}
}

class Compare implements Comparator<Interval> {
	public int compare(Interval a, Interval b) {
		if (a.st < b.st)
			return -1;
		if (a.st == b.st)
			return 0;
		return 1;
	}
}

public class milk2 {
	static int max(int a, int b) {
		return a > b ? a : b;
	}

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(new BufferedReader(new FileReader(
				"milk2.in")));
		PrintWriter output = new PrintWriter(new BufferedWriter(new FileWriter(
				"milk2.out")));
		int n = input.nextInt();
		Interval[] time = new Interval[n];
		for (int i = 0; i < n; i++)
			time[i] = new Interval(input.nextInt(), input.nextInt());
		Arrays.sort(time, new Compare());
		int f = time[0].st;
		int e = time[0].en;
		int r1 = e - f;
		int r2 = 0;
		for (int i = 1; i < n; i++) {
			if (time[i].en <= e)
				continue;
			if (time[i].st <= e) {
				e = time[i].en;
				r1 = max(e - f, r1);
			} else {
				f = time[i].st;
				r2 = max(f - e, r2);
				e = time[i].en;
			}
		}
		output.print(r1);
		output.print(' ');
		output.println(r2);
		input.close();
		output.close();
		System.exit(0);
	}
}