package USACOTraining;

/*
ID: darrenc3
LANG: JAVA
TASK: dualpal
*/
import java.util.*;
import java.io.*;
public class dualpal {
	char mapping[]={'0','1','2','3','4','5','6','7','8','9'};
	int start,num;
	int flag;
	String trans;
	public static void main(String[] args) throws IOException
	{
		new dualpal().run();
	}
	void run() throws IOException
	{
		Scanner cin=new Scanner(new FileReader("dualpal.in"));
		PrintWriter cout=new PrintWriter(new BufferedWriter(new FileWriter("dualpal.out")));
		num=cin.nextInt();
		start=cin.nextInt();
		while(num>0)
		{
			flag=0;
			start++;
			for(int i=2;i<=10;i++)
			{
				trans="";
				change(start,i);
				//System.out.println(trans);
				if(check())
					flag++;
				if(flag==2)
				{
					cout.println(start);
					num--;
					break;
				}
			}
		}
		cout.close();
		System.exit(0);
 
	}
	void change(int n,int k)
	{
		if(n!=0)
		{
			trans=trans+(mapping[n%k]);
			n=n/k;
			change(n,k);
		}
	}
	boolean check()
	{
		int len=trans.length();
		if(trans.charAt(0)=='0'||trans.charAt(len-1)=='0') return false;
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