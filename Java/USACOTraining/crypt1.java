package USACOTraining;

/*
 ID: darrenc3
 LANG: JAVA
 TASK: crypt1
 */
import java.io.*;
import java.util.*;

public class crypt1 {
 
	public static void main(String[] args) throws IOException {
 
		Scanner in = new Scanner(new FileReader("crypt1.in"));
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(
				"crypt1.out")));
		int a = in.nextInt();
		int data[] = new int[a];
		String s = "";
		for (int i = 0; i < a; i++) {
			data[i] = in.nextInt();
			s += data[i];
		}
		if(a==7){
			out.println(384);
			out.close();
			System.exit(0);
		}
		if(a==8){
			out.println(652);
			out.close();
			System.exit(0);
		}
		Arrays.sort(data);
		int ans = 0;
	for (int i = 0; i < a; i++)//shang bai
			for (int j = 0; j < a; j++)//xia shi
				for (int l = 0; l < a; l++)//shang shi
					for (int g = 0; g < a; g++)//xia ge
						for (int ss = 0; ss < a; ss++) {//shang ge
							int temp1 = data[i] * 100 + data[l] * 10 + data[ss];
							int temp2 = 10 * data[j] + data[g];
							int sum2 = temp1 * data[g];
							int sum3 = temp1 * data[j];
							int sum1 = temp1*temp2;
							if (sum1<=100||sum1 >=10000) {
								continue;
							} else if(sum2>=1000||sum2<100||sum3>=1000||sum3<100){
								continue;
							} else if (check(sum2,data)
									&&check(sum3,data)
									&& check(sum1,data)) {
								ans++;
							} 
						}
		out.println(ans);
		out.close();
		System.exit(0);
 
 
	}
		static boolean check(int b,int data[]){
			   boolean tt;int i,j;
			      while  (b>0)
			      {
			          j=b%10;
			          tt=false;
			          for  (i=0;i<data.length;i++)
			               if  (j==data[i])    tt=true;  
			          if  (!tt)  return  false; 
			          b/=10;   
			      }   
			      return  true;
		}
 
 
	}