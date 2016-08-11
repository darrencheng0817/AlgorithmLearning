package USACOTraining;

/*
ID: darrenc
LANG: JAVA
TASK: numtri
*/
import java.util.*;
import java.io.*;
public class numtri {
	int[][] num = new int[1007][1007];
	int[][] f = new int[1007][1007];
	public static void main(String[] args) throws IOException 
	{
		new numtri().run();
	}
	StreamTokenizer cin;
	PrintWriter cout;
 
	 int nextInt() throws IOException
	   {
	      cin.nextToken();
	      return (int)cin.nval;
	   }
 
 
	void run() throws IOException
	{
		cin = new StreamTokenizer(new BufferedReader(new FileReader("numtri.in")));
	    cout = new PrintWriter(new FileWriter("numtri.out"));
 
		int n =nextInt();
		for(int i = 1;i <= n;i++)
			for(int j = 1;j <=i;j++)
				num[i][j] =nextInt();
		for(int i = n;i > 0;i--)
			for(int j = 1;j <= i;j++)
				f[i][j] = max(f[i+1][j], f[i+1][j+1]) + num[i][j];
		cout.println(f[1][1]);
		cout.flush();
		cout.close();
 
 
	}
	int max(int a,int b)
	{
		return a>b ? a:b;
	}
}
