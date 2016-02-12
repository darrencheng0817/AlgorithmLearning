package USACOTraining;

/*1
ID: darrenc3
LANG: JAVA
TASK: barn1
*/
import java.util.*;
import java.io.*;
public class barn1 {
 
	int M,S,C,tot,maxx=0,minn=99999999;
	int sleep[]=new int[201];
	int len[]=new int[201];
	public static void main(String[] args) throws IOException
	{
		new barn1().run();
	}
	void run() throws IOException
	{
		Scanner cin=new Scanner(new FileReader("barn1.in"));
		PrintWriter cout=new PrintWriter(new BufferedWriter(new FileWriter("barn1.out")));
		M=cin.nextInt();
		S=cin.nextInt();
		C=cin.nextInt();
		if(M>=C)
		{
			cout.println(C);
			cout.close();
			System.exit(0);
		}
		for(int i=1;i<=C;i++)
		{
			sleep[i]=cin.nextInt();
			maxx=maxx>sleep[i] ? maxx:sleep[i];
			minn=minn<sleep[i] ? minn:sleep[i];
		}
		Arrays.sort(sleep,1,C+1);
		for(int i=2;i<=C;i++)
			len[i-1]=sleep[i]-sleep[i-1];
		Arrays.sort(len,1,C);
		tot=maxx-minn;
		int cut=M-1;
		int now=C-1;
		while(cut>0)
		{
			tot-=len[now];
			now--;
			cut--;
		}
		cout.println(tot+M);
		cout.close();
		System.exit(0);
	}
}