import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;


public class generatePalindromes {
	public static List<String> generatePalindromes(String s) {
        HashMap<Character,Integer> map=new HashMap<>();
        List<String> res=new LinkedList<String>();
        List<Character> list=new LinkedList<>();
        int odd=0;
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(map.containsKey(c)){
                map.put(c,map.get(c)+1);
            }
            else{
                map.put(c,1);
            }
            if((map.get(c)&1)==0){
                odd--;
            }
            else
                odd++;
        }
        if(odd>1)
            return res;
        String mid="";
        for(Map.Entry<Character,Integer> entry: map.entrySet()){
            char c=entry.getKey();
            int n=entry.getValue();
            if((n&1)==1)
                mid+=c;
            for(int i=0;i<(n>>1);i++)
                list.add(c);
        }
        helper(res,list,new StringBuilder(),mid,new boolean[list.size()]);
        return res;
    } 
    private static void helper(List<String> res,List<Character> list,StringBuilder item,String mid,boolean[] used){
        if(item.length()==list.size()){
            res.add(item.toString()+mid+item.reverse().toString());
            item.reverse();
            return;
        }
        
        for(int i=0;i<list.size();i++){
            if(i>0&&list.get(i-1)==list.get(i)&&used[i-1]==false) continue;
            if(used[i]==false){
	            used[i]=true;
	            helper(res,list,item.append(list.get(i)),mid,used);
	            used[i]=false;
	            item.deleteCharAt(item.length()-1);
            }
        }
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(generatePalindromes("aabb"));
	}

}
