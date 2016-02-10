package USACOTraining;

/*
ID: darrenc
LANG: JAVA
TASK: namenum
*/

import java.util.*;
import java.io.*;
public class namenum {
 
	char num[]={'2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','0','7','7','8','8','8','9','9','9','0'};
	int num_out=0;
	String std,dictin;
	char trans[]=new char[13];
	public static void main(String[] args) throws IOException 
	{
		new namenum().run();
	}
	void run() throws IOException
	{
		Scanner dict=new Scanner(new FileReader("dict.txt"));
		Scanner cin=new Scanner(new FileReader("namenum.in"));
		PrintWriter cout=new PrintWriter(new BufferedWriter(new FileWriter("namenum.out")));
		std=cin.next();
		while(dict.hasNext())
		{
			dictin=dict.next();
			if(std.length()==dictin.length())
			{
				change();
				if(cmp())
				{
					num_out++;
					cout.println(dictin);
				}
			}
		}
		if(num_out==0)
			cout.println("NONE");
		cout.close();
		System.exit(0);
	}
	void change()
	{
		for(int i=0;i<dictin.length();i++)
			trans[i]=num[dictin.charAt(i)-'A'];
	}
	boolean cmp()
	{
		for(int i=0;i<std.length();i++)
			if(std.charAt(i)!=trans[i])
				return false;
		return true;
	}
}
 