import java.util.LinkedList;
import java.util.List;


public class restoreIpAddresses {

	public static void main(String[] args) {
		System.out.println(restore("11111"));

	}
	public static List<String> restore(String s) {
        List<String> res=new LinkedList<String>();
        if(s==null||s.length()<4)
            return res;
        restoreUtil(res,s,0,1,new String());
        return res;
    }
    private static void restoreUtil(List<String> res,String s,int index,int count,String item){
        if(index>=s.length()||count>4)
            return;
        if(count==4){
        	String str=s.substring(index);
            if(isValid(str)){
                res.add(item+"."+str);
            }
            return;
        }
        for(int i=1;i<4&&((i+index)<s.length());i++){
            String tempString=s.substring(index,index+i);
            if(isValid(tempString)==true){
                if(count==1){
                    item=tempString;
                }
                else{
                    item=item+"."+tempString;
                }
                restoreUtil(res,s,index+i,count+1,item);
            }
        }
    }
    private static void restoreUtil1(List<String> res,String s,int index,int count,String item){
	    if(index>=s.length()||count>4)
	        return;
	    if(count==4){
	        String str=s.substring(index);
	        if(isValid(str)){
	            res.add(item+"."+str);
	        }
	        return;
	    }
	    for(int i=1;i<4&&((i+index)<s.length());i++){
	        String tempstring=s.substring(index,index+i);
	        if(isValid(tempstring)){
	            {  
	                if(count==1)  
	                	restoreUtil1(res,s,index+i,count+1,tempstring);  
	                else  
	                	restoreUtil1(res,s,index+i,count+1,item+"."+tempstring);  
	            }  
	        }
	    }
    }
    private static boolean isValid(String s){
        if(s==null||s.length()==0||s.length()>3)
            return false;
        if(s.length()>1&&s.charAt(0)=='0')
            return false;
        int value=Integer.parseInt(s);
        if(value<0||value>255)
            return false;
        return true;
    }
}
