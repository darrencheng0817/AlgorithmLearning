import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


public class AlienDictionary {

	public static void main(String[] args) {
		String[] words={"dvpzu","bq","lwp","akiljwjdu","vnkauhh","ogjgdsfk","tnkmxnj","uvwa","zfe","dvgghw","yeyruhev","xymbbvo","m","n"};
		System.out.println(alienOrder(words));
	}

	public static String alienOrder(String[] words) {
        HashMap<Character,List<Character>> map=new HashMap<>();
        HashMap<Character,Integer> inDegree=new HashMap<>();
        for(int j=0;j<words[0].length();j++){
            char c=words[0].charAt(j);
            if(!map.containsKey(c)){
                map.put(c,new LinkedList<>());
            }
            if(!inDegree.containsKey(c)){
                inDegree.put(c,0);
            }
        }
        for(int i=1;i<words.length;i++){
            for(int j=0;j<words[i].length();j++){
                char c=words[i].charAt(j);
                if(!map.containsKey(c)){
                    map.put(c,new LinkedList<>());
                }
                if(!inDegree.containsKey(c)){
                    inDegree.put(c,0);
                }
            }
            int j=0;
            while(j<words[i].length()&&j<words[i-1].length()&&words[i].charAt(j)==words[i-1].charAt(j)){
                    j++;
            }
            if(j<words[i].length()&&j<words[i-1].length()&&words[i].charAt(j)!=words[i-1].charAt(j)){
                map.get(words[i-1].charAt(j)).add(words[i].charAt(j));
                inDegree.put(words[i].charAt(j),inDegree.get(words[i].charAt(j))+1);
            }
        }
 
        
        Queue<Character> queue=new LinkedList<>();
        HashSet<Character> visited=new HashSet<>();
        String res=new String();
        for(Character c:inDegree.keySet()){
            if(inDegree.get(c)==0){
                queue.offer(c);
            }
        }
        while(!queue.isEmpty()){
            char c=queue.poll();
            if(visited.contains(c))
                return "";
            res+=c;
            List<Character> temp=map.get(c);
            for(int i=0;i<temp.size();i++){
                queue.offer(temp.get(i));
            }
            visited.add(c);
        }
        if(visited.size()==inDegree.size())
        	return res;
        else {
        	return "";
		}
    }
}