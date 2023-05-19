import java.util.HashMap;
import java.util.List;
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    if (strs.length == 1){
      ArrayList<ArrayList<String>> listOfList = new ArrayList<ArrayList<String>>();
      ArrayList<String> listOfString = new ArrayList<String>();
      listOfString.add(strs[0]);
      listOfList.add(listOfString);
      return (List<List<String>>) (List<?>) listOfList;
    }

    HashMap<Integer, ArrayList<String>> map = new HashMap<Integer, ArrayList<String>>();
    for (int i = 0; i < strs.length; i++){
      int integerValue = 0;
      for (int j = 0; j < strs[i].length(); j++){
        integerValue = integerValue + strs[i].charAt(j);
      }
      ArrayList<String> list = new ArrayList<String>();
      if (map.containsKey(integerValue)){
        if (integerValue == 0){
          list = map.get(integerValue);
          list.add(strs[i]);
          map.put(integerValue, list);
        } else if (map.get(integerValue).get(0).contains(strs[i].substring(0,1))){
          list = map.get(integerValue);
          list.add(strs[i]);
          map.put(integerValue, list);
        } else{
          list.add(strs[i]);
          map.put(integerValue + 2847, list);
        }
      }else {
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
