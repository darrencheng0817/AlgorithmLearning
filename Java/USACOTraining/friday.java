package USACOTraining;

/*
 ID: darrenc3
 LANG: JAVA
 TASK: friday
 */
import java.util.*;
import java.io.*;

public class friday {
	static int[] days = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	public static void main(String args[]) throws IOException {
		int[] tot = new int[7];
		Scanner input = new Scanner(new FileReader("friday.in"));
		PrintWriter output = new PrintWriter(new BufferedWriter(new FileWriter(
				"friday.out")));
		int n = input.nextInt();
		int now = 13;
		tot[6]++;
		for (int y = 1900; y <= 1899 + n; y++)
			for (int j = 0; j < 12; j++) {
				now += days[j];
				if (((y % 400 == 0) || ((y % 4 == 0) && (y % 100 != 0)))
						&& (j == 1))
					now++;
				now %= 7;
				if ((y != n + 1899) || (j != 11))
					tot[now]++;
			}
		output.print(tot[6]);
		output.print(" ");
		for (int i = 0; i < 5; i++) {
			output.print(tot[i]);
			output.print(" ");
		}
		output.println(tot[5]);
		input.close();
		output.close();
		System.exit(0);
	}
}