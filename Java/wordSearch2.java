import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;


public class wordSearch2 {
	public static List<String> findWords(char[][] board, String[] words) {
        Set<String> res=new HashSet<String>();
        Trie trie=new Trie();
        for(String word:words){
            trie.insert(word);
        }
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                findWordsUtil(res,board,"",i,j,new boolean[board.length][board[0].length],trie);
            }
        }
        return new LinkedList(res);
    }
    private static void findWordsUtil(Set<String> res,char[][] board,String str,int i,int j,boolean[][] visited,Trie trie){
        if(i<0||i>=board.length||j<0||j>=board[0].length||visited[i][j]==true)
            return;
        str+=board[i][j];
        if(!trie.startsWith(str))
            return;
        if(trie.search(str)){
            res.add(str);
        }
        visited[i][j]=true;
        findWordsUtil(res,board,str,i+1,j,visited,trie);
        findWordsUtil(res,board,str,i-1,j,visited,trie);
        findWordsUtil(res,board,str,i,j+1,visited,trie);
        findWordsUtil(res,board,str,i,j-1,visited,trie);
        visited[i][j]=false;
    }
	public static void main(String[] args) {
		char[][] board={{'a','b'}};
		String[] words={"ba"};
		System.out.println(findWords(board,words));

	}

}

class Trie{
    TrieNode root=new TrieNode();
    public void insert(String s){
        TrieNode pointer=root;
        for(int i=0;i<s.length();i++){
            int index=s.charAt(i)-'a';
            if(pointer.children[index]==null){
                TrieNode temp=new TrieNode();
                pointer.children[index]=temp;
            }
            pointer=pointer.children[index];
        }
        pointer.isWord=true;
    }
    public boolean startsWith(String s){
        return find(s)!=null;
    }
    
    public boolean search(String s){
        TrieNode tail=find(s);
        return tail!=null&&tail.isWord==true;
    }
    public TrieNode find(String s){
        TrieNode pointer=root;
        for(int i=0;i<s.length();i++){
            int index=s.charAt(i)-'a';
            if(pointer.children[index]==null)
                return null;
            pointer=pointer.children[index];
        }
        return pointer;
    }
}