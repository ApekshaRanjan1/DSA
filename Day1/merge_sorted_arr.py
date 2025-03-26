# # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# # Output: [1,2,2,3,5,6]
# # Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# # The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

class Solution(object):
    def merge(self, n1, m, n2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 
        p2 = n - 1  
        p = m + n - 1  

        while p2 >= 0:
            if p1 >= 0 and n1[p1] > n2[p2]:
                n1[p] = n1[p1]
                p1 -= 1
            else:
                n1[p] = n2[p2]
                p2 -= 1
            p -= 1