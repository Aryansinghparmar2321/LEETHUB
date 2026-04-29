class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def countLessEqual(mid):
            count = 0
            row = n - 1
            col = 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            
            return count
        
        left = matrix[0][0]
        right = matrix[-1][-1]
        
        while left < right:
            mid = (left + right) // 2
            
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left