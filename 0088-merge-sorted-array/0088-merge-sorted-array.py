class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2, and the last position in nums1
        i, j, k = m - 1, n - 1, m + n - 1
        
        # Merge nums1 and nums2 from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
