package USACOTraining;

/*
ID: darrenc3
LANG: JAVA
TASK: palsquare
*/
import java.util.*;
import java.io.*;
public class palsquare {
	char mapping[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K'};
	String trans="";
	String oldtrans="";
	int b;
	public static void main(String[] args) throws IOException 
	{
		new palsquare().run();
	}
	void run() throws IOException
	{
		Scanner cin=new Scanner(new FileReader("palsquare.in"));
		PrintWriter cout=new PrintWriter(new BufferedWriter(new FileWriter("palsquare.out")));
		b=cin.nextInt();
		for(int i=1;i<=300;i++)
		{
			trans="";
			change(i*i);
			if(check())
			{
				oldtrans="";
				change2(i);
				for(int j=oldtrans.length()-1;j>=0;j--)
					cout.print(oldtrans.charAt(j));
				cout.println(" "+trans);
			}
		}
		cout.close();
		System.exit(0);
	}
	void change(int num)
	{
		if(num!=0)
		{
			trans=trans+(mapping[num%b]);
			num=num/b;
			change(num);
		}
	}
	void change2(int num)
	{
		if(num!=0)
		{
			oldtrans=oldtrans+(mapping[num%b]);
			num=num/b;
			change2(num);
		}
	}
	boolean check()
	{
		int len=trans.length();
		if(len%2==0)
		{
			for(int i=1;i<=len/2;i++)
			{
				if(trans.charAt(len/2-i)!=trans.charAt(len/2+i-1))
					return false;
			}
		}else
		{
			for(int i=1;i<=(len-1)/2;i++)
			{
				if(trans.charAt((len-1)/2-i)!=trans.charAt((len-1)/2+i))
					return false;
			}
		}
		return true;
	}
}
 