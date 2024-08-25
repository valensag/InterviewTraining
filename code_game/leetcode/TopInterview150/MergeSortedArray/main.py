
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class MergeSortedArray():
    
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:m]
        nums1 = nums1 + nums2
        nums1.sort()
        print(nums1)

if __name__ == '__main__':
    result = MergeSortedArray()
    result.merge(nums1, m, nums2, n)
