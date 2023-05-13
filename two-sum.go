func twoSum(nums []int, target int) []int {
    var hashmap map[int]int
    hashmap = make(map[int]int)
    arr := []int{0, 0}
    for i:= 0; i < len(nums); i++{
      value, ok := hashmap[target - nums[i]]
      if ok {
        arr[0] = value
        arr[1] = i
      } else {
        hashmap[nums[i]] = i
      }
    }
    return arr
}
