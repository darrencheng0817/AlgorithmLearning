package USACOTraining;

/*
ID: darrenc3
LANG: JAVA
TASK: gift1
 */
import java.io.*;
import java.util.*;
 
class person {
	person(String name, int money, int sendCount) {
		this.name = name;
		this.initial_money = this.money = money;
		this.sendCount = sendCount;
		friends = new String[sendCount];
		if (sendCount <= 0 || money <= 0) {
			avgMoney = 0;
		} else {
			avgMoney = money / sendCount;
			this.money = money % sendCount;
		}
	}
 
	public int avgMoney;
	public String name;
	public int money;
	public int initial_money;
	public int sendCount;
	public String[] friends;
}
 
public class gift1{
	public static void main(String[] args) throws IOException {
		// Use BufferedReader rather than RandomAccessFile; it's much faster
		BufferedReader f = new BufferedReader(new FileReader("gift1.in"));
		// input file name goes above
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(
				"gift1.out")));
		int sum = Integer.parseInt(f.readLine()); // first integer
		int i = 0, j = 0;
		String tempName;
		int tempMoney, tempSend;
		person p_temp, p_temp2;
		String temp;
		String[] names = new String[sum];
		HashMap<String, person> table = new HashMap<String, person>();
		for (i = 0; i < sum; i++) {
			names[i] = f.readLine();
		}
 
		StringTokenizer st;
		for (i = 0; i < sum; i++) {
			tempName = f.readLine();
			temp = f.readLine();
			st = new StringTokenizer(temp);
			tempMoney = Integer.parseInt(st.nextToken());
			tempSend = Integer.parseInt(st.nextToken());
			p_temp = new person(tempName, tempMoney, tempSend);
			for (j = 0; j < tempSend; j++) {
				p_temp.friends[j] = f.readLine();
			}
			table.put(tempName, p_temp);
		}
		for (i = 0; i < sum; i++) {
			p_temp = table.get(names[i]);
			for (j = 0; j < p_temp.sendCount; j++) {
				p_temp2 = table.get(p_temp.friends[j]);
				p_temp2.money += p_temp.avgMoney;
			}
		}
 
		for (i = 0; i < sum; i++) {
			p_temp = table.get(names[i]);
			out.println(p_temp.name + " "
					+ (p_temp.money - p_temp.initial_money));
		}
 
		out.close(); // close the output file
		f.close();
		System.exit(0); // don't omit this!
	}
}