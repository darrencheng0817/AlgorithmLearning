package USACOTraining;

/*
 ID: darrenc3
 LANG: JAVA
 TASK: beads
 */
import java.io.*;
import java.util.*;
public class beads{
  public static void main(String[]args)throws IOException{
    Scanner input=new Scanner(new FileReader("beads.in"));
    PrintWriter output=new PrintWriter(new BufferedWriter(new FileWriter("beads.out")));
    String a=input.nextLine();
    a=input.nextLine();
    int n=a.length();
    a=a+a;
    int color=0,curr=0,prev=0,res=0,w=0,i=0;
    for(i=0;i<n*2&&res<n;i++){
      if(a.charAt(i)=='w'){
        w++;
        curr++;
      }
      else if(a.charAt(i)==color){
        w=0;
        curr++;
      }
      else{
        color=a.charAt(i);
        res=(prev+curr>res)?prev+curr:res;
        prev=curr-w;
        curr=w+1;
        w=0;
      }
    }
    res=(prev+curr>res)?prev+curr:res;
    output.println(res<n?res:n);
    input.close();
    output.close();
    System.exit(0);
  }
}