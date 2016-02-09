import static org.junit.Assert.fail;

import java.util.*;

import org.junit.Test;

public class test1 {

	public static void main(String[] args) {
	    List<List<String>> wordsList = new ArrayList<List<String>>();
	    wordsList.add(Arrays.asList("quick", "lazy"));
	    wordsList.add(new ArrayList<String>());
	    wordsList.add(Arrays.asList("brown", "black", "grey"));
	    wordsList.add(Arrays.asList("fox", "dog"));
	    wordsList.clear();
	    printResult(getCombinations(wordsList));
	    
	  }
	@Test
	public void test() {
		fail("Not yet implemented");
	}
	  private static List<List<String>> getCombinations(List<List<String>> wordsList){
	      List<List<String>> res=new ArrayList<List<String>>();
	      if (wordsList==null || wordsList.isEmpty()){
	        return res;
	      }
	      res.add(new ArrayList<String>());
	      for(List<String> words : wordsList){
	    	  if (words.isEmpty())
	    		  continue;
	        List<List<String>> newRes=new ArrayList<List<String>>();
	        for(List<String> item:res){
	            for(String word:words){
	              List<String> newItem=new ArrayList<String>(item);
	              newItem.add(word);
	              newRes.add(newItem);
	            }
	        }
	        res=newRes;
	      }
	    return res;
	  }
	  private static void printResult(List<List<String>> wordsList){
	      for(List<String> words:wordsList){
	        String outputString=new String();
	        for(int i=0;i<words.size();i++){
	          if(i==0){
	            outputString+=words.get(i);
	          }
	          else{
	            outputString+=(" "+words.get(i));
	          }
	        }
	        System.out.println(outputString);
	      }
	      
	  }

}
