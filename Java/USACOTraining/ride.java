package USACOTraining;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/*
 ID: darrenc3
 LANG: JAVA
 TASK: ride
 */
public class ride {
	public static void main(String[] args) throws IOException {
		// Use BufferedReader rather than RandomAccessFile; it's much faster
		BufferedReader f = new BufferedReader(new FileReader("ride.in"));
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
		String s1 = f.readLine(); // gets entire line
		String s2 = f.readLine();
		int num1 = 1;
		int num2 = 1;
		for (int i = 0; i < s1.length(); i++) {
			num1 *= s1.charAt(i) - 'A' + 1;
		}
		for (int i = 0; i < s2.length(); i++) {
			num2 *= s2.charAt(i) - 'A' + 1;
		}
		if (num1 % 47 == num2 % 47) {
			out.write("GO" + "\n");
		} else {
			out.write("STAY" + "\n");
		}
		out.close(); // close the output file
		System.exit(0); // don't omit this!
	}
}