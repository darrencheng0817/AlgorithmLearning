package USACOTraining;

/*
ID: darrenc
LANG: JAVA
TASK: transform
*/
import java.util.*;
import java.io.*;
public class transform {
	int n;
	int trans[][]=new int[11][11];
	int input[][]=new int[11][11];
	int cmp[][]=new int[11][11];
	char tmp;
	String str;
	public static void main(String[] args) throws IOException
	{
		new transform().run();
	}
	void run() throws IOException
	{
		Scanner cin=new Scanner(new FileReader("transform.in"));
		PrintWriter cout=new PrintWriter(new BufferedWriter(new FileWriter("transform.out")));
		n=cin.nextInt();
		for(int i=1;i<=n;i++)
		{
				str=cin.next();
				for(int j=0;j<n;j++)
				{
					if(str.charAt(j)=='@')
						input[i][j+1]=0;
					else
						input[i][j+1]=1;
				}
		}
		for(int i=1;i<=n;i++)
		{
				str=cin.next();
				for(int j=0;j<n;j++)
				{
					if(str.charAt(j)=='@')
						cmp[i][j+1]=0;
					else
						cmp[i][j+1]=1;
				}
		}
		change1(input,trans);
		if(check())
		{
			cout.println(1);
			cout.close();
			System.exit(0);
		}
		change2(input,trans);
		if(check())
		{
			cout.println(2);
			cout.close();
			System.exit(0);
		}
		change3(input,trans);
		if(check())
		{
			cout.println(3);
			cout.close();
			System.exit(0);
		}
		change4(input,trans);
		if(check())
		{
			cout.println(4);
			cout.close();
			System.exit(0);
		}
 
		int tmp1[][]=new int[11][11];
		change4(input,tmp1);
		change1(tmp1,trans);
		if(check())
		{
			cout.println(5);
			cout.close();
			System.exit(0);
		}
		change2(tmp1,trans);
		if(check())
		{
			cout.println(5);
			cout.close();
			System.exit(0);
		}
		change3(tmp1,trans);
		if(check())
		{
			cout.println(5);
			cout.close();
			System.exit(0);
		}
 
		change6(input,trans);
		if(check())
		{
			cout.println(6);
			cout.close();
			System.exit(0);
		}
		cout.println(7);
		cout.close();
		System.exit(0);
	}
	boolean check()
	{
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
				if(trans[i][j]!=cmp[i][j]) return false;
		}
		return true;
	}
	void change1(int input[][],int trans[][])
	{
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				trans[j][n-i+1]=input[i][j];
			}
	}
	void change2(int input[][],int trans[][])
	{
		int tmp[][]=new int[11][11];
		change1(input,tmp);
		change1(tmp,trans);
	}
	void change3(int input[][],int trans[][])
	{
		int tmp[][]=new int[11][11];
		int tmp2[][]=new int[11][11];
		change1(input,tmp);
		change1(tmp,tmp2);
		change1(tmp2,trans);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
	}
	void change4(int input[][],int trans[][])
	{
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				trans[i][n-j+1]=input[i][j];
	}
	void change6(int input[][],int trans[][])
	{
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				trans[i][j]=input[i][j];
	}
}