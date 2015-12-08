import java.util.Stack;


public class simplifyPath {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(simplify("/../asdf/../af/asdf//"));
	}

	public static String simplify(String path) {
        String[] stringArray=path.split("/");
        Stack<String> stack=new Stack<>();
        for(int i=0;i<stringArray.length;i++){
            if(stringArray[i].equals("..")){
                if(!stack.isEmpty())
                	stack.pop();
            }
            else if(!stringArray[i].equals(".")&&stringArray[i].length()>0){
                stack.push(stringArray[i]);
            }
        }
        StringBuilder res= new StringBuilder();
        if(!stack.isEmpty())  
        {  
            String[] strs = stack.toArray(new String[stack.size()]);  
            for(int j=0;j<strs.length;j++)  
            {  
              res.append("/"+strs[j]);  
            }  
        }  
        if(res.length()==0)
            res.append("/");
        return res.toString();
    }
}
