class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            if matrix[i][l] <= target and matrix[i][r] >= target:
                l1, r1 = 0, len(matrix[i]) - 1
                while l1 <= r1:    
                    m = l1 + ((r1 - l1) // 2)
                    if target > matrix[i][m]:
                        l1 = m + 1
                    elif target < matrix[i][m]:
                        r1 = m - 1
                    else:
                        return True
                return False
