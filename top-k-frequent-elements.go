func topKFrequent(nums []int, k int) []int {
	//Steps:
	// 1. Insert the numbers to a map to count to frequency of the numbers
	// 2. Loop through the map and insert the number to bucket list by the number
	// 3. The number of the array in the bucket list is the same with the length of the nums array
	if k == 1 && len(nums) <= 2 {
		return []int{nums[0]}
	}

	theMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		_, ok := theMap[nums[i]]
		if ok {
			theMap[nums[i]] = theMap[nums[i]] + 1
		} else {
			theMap[nums[i]] = 1
		}
	}

	array := make([][]int, len(nums))
	for key, value := range theMap {
		array[value] = append(array[value], key)
	}

	var result []int = []int{}
	for i := len(array) - 1; i > 0; i-- {
		for _, slic := range array[i] {
			if len(result) < k {
				result = append(result, slic)
			}
		}
	}
	return result
}
