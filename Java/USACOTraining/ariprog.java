package USACOTraining;
 /*
ID: darrenc3
LANG: JAVA
TASK: ariprog
*/
import java.util.*;
import java.io.*;
public class ariprog {
 
    class Data implements Comparable
    {
        int a,b;
        public int compareTo(Object o) {
            Data t=(Data)o;
            if (b<t.b) return -1;
            else if (b==t.b) return 0;
            return 1;
        }
    }
    int N,M;
    int num_bis=0,num_ans=0;
    boolean bis[] = new boolean[125007];
    int bislist[] = new int[125007];
    Data[] ans = new Data[10007];
    public static void main(String[] args) throws IOException 
    {
        new ariprog().run();
    }
    void run() throws IOException
    {
        Scanner cin = new Scanner(new FileReader("ariprog.in"));
        N = cin.nextInt();
        M = cin.nextInt();
        init();
        work();
        print();
    }
    void print() throws IOException
    {
        PrintWriter cout = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
        if(num_ans == 0) 
        {
            cout.println("NONE");
            cout.close();
            System.exit(0);
        }
        Arrays.sort(ans,1,num_ans+1);
        for(int i = 1;i <= num_ans;i++)
            cout.println(ans[i].a + " " + ans[i].b);
        cout.close();
    }
    void init()
    {
        int tmp;
        for(int i = 0;i <= M;i++)
            for(int j = 0;j <= M;j++)
            {
                tmp = i*i + j*j;
                bis[tmp]=true;
            }
        for(int i = 0;i <= M*M*2;i++)
            if(bis[i])
            {
                bislist[++num_bis]=i;
            }
    }
    void work()
    {
        int a,b;
        for(int i = 1;i < num_bis;i++)
        {
            for(int j = i+1;j <= num_bis;j++)
            {
                if(i != j)
                {
                    a = bislist[i];
                    b = bislist[j]-a;
                    if(check(a,b))
                    {
                        ans[++num_ans] = new Data();
                        ans[num_ans].a = a;
                        ans[num_ans].b = b;
                    }
                }
            }
        }
    }
    boolean check(int a,int b)
    {
        int tmp;
        for(int i = 0;i < N;i++)
        {
            tmp = a+b*i;
            if(tmp > M*M*2)
                return false;
            if(tmp<0) return false;
            if(!bis[tmp]) return false;
        }
        return true;
    }
}