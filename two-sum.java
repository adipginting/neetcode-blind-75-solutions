import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        HashMap<Integer, Integer> dupmap = new HashMap<>();
        int[] solution = new int[2];
        for (int i = 0; i < nums.length; i++){
            if (hashmap.containsKey(nums[i]) == true){
                dupmap.put(nums[i], i);
            } else {
                hashmap.put(nums[i], i);
            }
        }

         for (int i = 0; i < nums.length; i++){
            if (hashmap.containsKey(target - nums[i]) == true 
                || hashmap.get(target - nums[i]) != hashmap.get(nums[i])
            ){
                solution[0] = hashmap.get(nums[i]);
                if (nums[i] == target - nums[i]){
                  System.out.println(target - nums[i]);
                   // solution[1] = dupmap.get(nums[i]);
                    break;
                } else {
                    solution[1] = hashmap.get(target - nums[i]);
                    break;
                }
            } else if (hashmap.containsKey(nums[i] - target) == true
            || hashmap.get(nums[i] - target) != hashmap.get(nums[i])
            ){
                solution[0] = hashmap.get(nums[i]);
                if (nums[i] == nums[i] - target){     
                  //  solution[1] = dupmap.get(nums[i]);
                    break;
                } else {
                    solution[1] = hashmap.get(nums[i] - target);
                    break;
                }
            }
        }
        return solution;
    }
}
