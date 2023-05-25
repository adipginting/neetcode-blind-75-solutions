import java.util.HashMap;
import java.util.List;

class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    // convert the string as key
    // create new List with number as its key
    // add every value inside the hashmap to a new List
    HashMap<String, List<String>> map = new HashMap<>();
    List<List<String>> result = new ArrayList<>();
    for (String str : strs) {
      char[] charArr = str.toCharArray();
      Arrays.sort(charArr);
      String orderedStr = String.valueOf(charArr);
      if (map.containsKey(orderedStr)) {
        map.get(orderedStr).add(str);
      } else {
        List<String> strList = new ArrayList<>();
        strList.add(str);
        map.put(orderedStr, strList);
      }
    }
    for (String key : map.keySet()) {
      result.add(map.get(key));
    }
    return result;
  }
}
