package test;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.TreeMap;


public class mapMap {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		HashMap<Integer, HashMap<Integer, Integer>> map = new HashMap<Integer, HashMap<Integer,Integer>>();
		put(map, 1, 1, 2);
		put(map, 1, 2, 3);
		System.out.println(get(map, 1, 2));
	
		
	}
	
	private static void put(HashMap<Integer, HashMap<Integer, Integer>> map,int key1,int key2,int value) {
		if (map.containsKey(key1)) {
			HashMap<Integer, Integer> tempHashMap=map.get(key1);
			tempHashMap.put(key2, value);
		}
		else{
			HashMap<Integer, Integer> item=new HashMap<Integer, Integer>();
			item.put(key2, value);
			map.put(key1, item);
		}
	}
	
	private static int get(HashMap<Integer, HashMap<Integer, Integer>> map,int key1,int key2) throws Exception {
		if (map.containsKey(key1)) {
			HashMap<Integer, Integer> tempHashMap=map.get(key1);
			if(tempHashMap.containsKey(key2)){
				return tempHashMap.get(key2);
			}
			else{
				throw new Exception("Error");
			}
		}
		throw new Exception("Error");
	}
}
