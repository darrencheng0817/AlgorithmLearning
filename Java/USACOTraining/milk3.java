package USACOTraining;

/*
 ID: darrenc
 LANG: JAVA
 TASK: milk3
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
 
public class milk3 {
 
	static int a;
	static int b;
	static int c;
	static boolean[] result;
	static boolean[][] matrix;
 
	public static void main(String[] args) {
		Scanner scanner = null;
		PrintWriter pw = null;
		try {
			scanner = new Scanner(new File("milk3.in"));
			pw = new PrintWriter(new File("milk3.out"));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
 
		a = scanner.nextInt();
		b = scanner.nextInt();
		c = scanner.nextInt();
 
		result = new boolean[c + 1];
		matrix = new boolean[a + 1][b + 1];
 
		dfs(0, 0, c);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < result.length; i++) {
			if (result[i])
				sb.append(i).append(" ");
		}
 
		if (sb.length() > 0)
			sb.deleteCharAt(sb.length() - 1);
		sb.append("\n");
 
		pw.write(sb.toString());
		pw.close();
	}
 
	private static void dfs(int A, int B, int C) {
 
		if (matrix[A][B]) {
			return;
		}
		matrix[A][B] = true;
		if (A == 0)
			result[C] = true;
 
		if (A <= b - B)
			dfs(0, B + A, C); // A->B
		else
			dfs(A - (b - B), b, C);
 
		if (A <= c - C)
			dfs(0, B, C + A); // A->C
		else
			dfs(A - (c - C), B, c);
 
		if (B <= a - A)
			dfs(A + B, 0, C); // B->A
		else
			dfs(a, B - (a - A), C);
 
		if (B <= c - C)
			dfs(A, 0, C + B); // B->C
		else
			dfs(A, B - (c - C), c);
 
		if (C <= a - A)
			dfs(A + C, B, 0); // C->A
		else
			dfs(a, B, C - (a - A));
 
		if (C <= b - B)
			dfs(A, B + C, 0); // C->B
		else
			dfs(A, b, C - (b - B));
 
		return;
 
	}
 
}