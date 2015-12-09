import java.util.LinkedList;
import java.util.Queue;


public class wordDictionary {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		myWordDictionary test=new myWordDictionary();
		test.addWord("bad");test.addWord("dad");test.addWord("mad");
		System.out.println(test.search("pad"));
		System.out.println(test.search("bad"));
		System.out.println(test.search(".ad"));
		System.out.println(test.search("b.."));
	}



}
class myWordDictionary {
    TrieNode root=new TrieNode();
    
    // Adds a word into the data structure.
    public void addWord(String word) {
        TrieNode pointer=root;
        for(int i=0;i<word.length();i++){
            int index=word.charAt(i)-'a';
            if(pointer.children[index]==null){
                pointer.children[index]=new TrieNode();
            }
            pointer=pointer.children[index];
        }
        pointer.isWord=true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        Queue<TrieNode> queue=new LinkedList<TrieNode>();
        queue.add(root);
        for(int i=0;i<word.length();i++){
            char c=word.charAt(i);
            if(queue.isEmpty())
                return false;
            Queue<TrieNode> tempQueue=new LinkedList<TrieNode>();
            while(!queue.isEmpty()){
                TrieNode tempNode=queue.poll();
                if(c=='.'){
                    for(int j=0;j<26;j++){
                        if(tempNode.children[j]!=null)
                            tempQueue.offer(tempNode.children[j]);
                    }
                }
                else{
                    if(tempNode.children[c-'a']!=null)
                        tempQueue.add(tempNode.children[c-'a']);
                }
            }
            queue=tempQueue;
        }
        boolean res=false;
        while(!queue.isEmpty()){
        	TrieNode tempNode=queue.poll();
        	res=res||tempNode.isWord;
        }
        return res;
    }
}
class TrieNode{
    public boolean isWord;
    TrieNode[] children;
    TrieNode(){
        isWord=false;
        children=new TrieNode[26];
    }
}