'''
Created on 2015年12月1日
internet -> i8t
但是如果有个新词 intranet
i8t就可能导致conflict
于是
internet -> inte8t
intranet -> intr8t


现在给一个dictionary，生成没有conflict的所有相应的缩写模式
楼主第一次见，应该是trie
@author: Darren
'''
'''
java code
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test {
    class TrieNode{
        boolean found;
        int nWords; // number of words below this node
//        int dis;    // distance to leaf if there is only one word below this node
        char c;     // leaf value if there is only one word below this node
        Map<Character,TrieNode> children;
        public TrieNode(){
            children = new HashMap<>();
        }
    }
    TrieNode root;
    void buildTrieTree(String[] input){
        root = new TrieNode();
        for (String str : input){
            TrieNode pt = root;
            for (int i = 0; i < str.length(); i++){
                char c = str.charAt(i);
                if (!pt.children.containsKey(c)){
                    pt.children.put(c, new TrieNode());
                }
                pt = (TrieNode) pt.children.get(c);
                pt.nWords++;
            }
            pt.found = true;
        }
    }
    public List<String> compressString(String[] input){
        buildTrieTree(input);
        List<String> ret = new ArrayList<String>();
        getCompressString(root, ret, "");
        return ret;
    }
    
    void getCompressString(TrieNode rt, List<String> ret, String path){
        if (rt.found) ret.add(path);
        // if nword is 1, get the substring.
        if (rt.nWords == 1){
            String sub = getSubString(rt);
            if (sub.length() <= 2) ret.add(path + sub);
            else{
                int len = sub.length() + path.length();
                ret.add(path + len + sub.charAt(sub.length() - 1));
            }
            return;
        }
        for (char ch : rt.children.keySet()){
            getCompressString(rt.children.get(ch), ret, path + ch);
        }
    }
    String getSubString(TrieNode rt){
        StringBuilder sbd = new StringBuilder();
        while (rt.children.size() != 0){
            Map<Character,TrieNode> sub = rt.children;
            for (char ch : sub.keySet()){
                sbd.append(ch);
                rt = rt.children.get(ch);
            }
        }
        return sbd.toString();
    }
    
    public static void main(String[] agrs){
        test sln = new test();
        String[] input = {"internet", "intranet", "modern", "great","intertet"};
        List<String> ret = sln.compressString(input);
        for (String str : ret){
            System.out.println(str);
        }
    }
}
'''



class TrieNode(object):
    def __init__(self,value=""):
        self.isEnd=False
        self.children={}
        self.value=value
        self.count=0

def buildTree(strings):
    root=TrieNode()
    for string in strings:
        pointer=root
        for char in string:
            if char not in pointer.children:
                pointer.children[char]=TrieNode(char)
            pointer.count+=1
            pointer=pointer.children[char]
        pointer.isEnd=True
    return root

def preProcess(res,strings):
    dic={}
    conflicts=[]
    for string in strings:
        if len(string)<=3:
            res.append(string)
        else:
            compressedWord=string[0]+str(len(string))+string[-1]
            if compressedWord not in dic:
                dic[compressedWord]=[]
            dic[compressedWord].append(string)
    for key in dic.keys():
        if len(dic[key])==1:
            res.append(key)
        else:
            conflicts+=dic[key]
    return conflicts
        
def getCompressedWords(strings):
    res=[]
    conflicts=preProcess(res,strings)
    root=buildTree(conflicts)
    getCompressedWordsUtil(root, res, "")
    return res

def getSuffix(root):
    res=""
    pointer=root
    while True:
        for key in pointer.children.keys():
            pointer=pointer.children[key]
        res+=pointer.value
        if pointer.isEnd:
            break
    return res
        
def getCompressedWordsUtil(root,res,path):
    if root.isEnd:
        res.append(path+root.value)
    if root.count==1:
        suffix=getSuffix(root)
        if len(suffix)<=2:
            res.append(path+root.value+suffix) 
        else:
            res.append(path+root.value+str(len(path)+len(suffix)+1)+suffix[-1])
        return
    for key in root.children.keys():
        getCompressedWordsUtil(root.children[key], res, path+root.value)
    
    
strings=["internet","interest","intranet","a","ab","abc","abcd"]
print(getCompressedWords(strings))