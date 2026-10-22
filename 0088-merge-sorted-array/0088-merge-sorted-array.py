
class Solution:
    def merge(self, nums1, m, nums2, n):
        # Copy the real values from nums1
        first = nums1[:m]

        # Copy the values from nums2
        second = nums2[:n]

        # Start comparing from the beginning
        i = 0
        j = 0
        k = 0

        # Merge the two sorted arrays
        while i < m and j < n:
            if first[i] <= second[j]:
                nums1[k] = first[i]
                i += 1
            else:
                nums1[k] = second[j]
                j += 1

            k += 1

        # Copy any remaining values from the first array
        while i < m:
            nums1[k] = first[i]
            i += 1
            k += 1

        # Copy any remaining values from the second array
        while j < n:
            nums1[k] = second[j]
            j += 1
            k += 1
