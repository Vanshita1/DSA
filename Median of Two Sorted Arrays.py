""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2. """


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array = nums1 + nums2
        merge_array.sort()
        l = len(merge_array)
        n = int(l/2)
        if l%2 != 0:
            return merge_array[n]
        else:
            ans = (merge_array[n-1] + merge_array[n])/2
            return ans
            
        