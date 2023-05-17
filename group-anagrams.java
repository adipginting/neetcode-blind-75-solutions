import java.util.HashMap;
import java.util.List;
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    HashMap<Integer, ArrayList<String>> map = new HashMap<Integer, ArrayList<String>>();
    for (int i = 0; i < strs.length; i++){
      int integerValue = 0;
      for (int j = 0; j < strs[i].length(); j++){
        integerValue = integerValue + strs[i].charAt(j);
      }
      ArrayList<String> list = new ArrayList<String>();
      if (map.containsKey(integerValue)){
        list = map.get(integerValue);
        list.add(strs[i]);
        map.put(integerValue, list);
      } else {
        list.add(strs[i]);
        map.put(integerValue, list);
      }
    }

    ArrayList<ArrayList<String>> returnValue = new ArrayList<ArrayList<String>>();
    for(Integer key: map.keySet()){
      returnValue.add(map.get(key));
    }

    return (List<List<String>>) (List<?>) returnValue;
  }
}
