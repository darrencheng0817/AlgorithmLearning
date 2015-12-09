import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class AncodeAndDecode {
	public static String encode(List<String> strs) {
        String res="";
        for(String str:strs){
            str.replace("#","##");
            res=res+str+" # ";
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    public static List<String> decode(String s) {
        List<String> res=new LinkedList<String>();
        String[] array=s.split(" # ",-1);
        System.out.println(array[0]);
        for (int i=0; i<array.length-1; ++i){
            res.add(array[i].replace("##","#"));
        }
        return res;
    }
    public static String encode1(List<String> strs) {
        StringBuffer out = new StringBuffer();
        for (String s : strs)
            out.append(s.replace("#", "##")).append(" # ");
        return out.toString();
    }
    
    public static List<String> decode1(String s) {
        List strs = new ArrayList<String>();
        String[] array = s.split(" # ", -1);
        System.out.println(array[0]);
        for (int i=0; i<array.length-1; ++i)
            strs.add(array[i].replace("##", "#"));
        return strs;
    }
	public static void main(String[] args) {
		List<String> strs=new LinkedList<String>();
		strs.add("#");
		
		System.out.println(encode1(strs));
		System.out.println(decode1(encode1(strs)));
		
	}
}