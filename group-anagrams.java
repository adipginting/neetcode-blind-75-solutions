import java.util.HashMap;
import java.util.List;

class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    // Steps:
    // 1. convert the strings to array of characters
    // 2. sort the characters, convert the ordered characters back to string, and use it as a key in a hashmap
    // 3. check whether each string exists inside the hashmap and add them using list of string
    // 4. put all of the content of the anagrams and non anagrams to a list 
    add every value inside the hashmap to a new List
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
