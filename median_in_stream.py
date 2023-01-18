from heapq import *


class MedianOfStream:
    max_heap_for_small_nums = []
    min_heap_for_large_nums = []

    def insert_num(self, num):
        if not self.max_heap_for_small_nums or -self.max_heap_for_small_nums[0] >= num:
            heappush(self.max_heap_for_small_nums, -num)
        else:
            heappush(self.min_heap_for_large_nums, num)

        if len(self.max_heap_for_small_nums) > len(self.min_heap_for_large_nums) + 1:
            heappush(self.min_heap_for_large_nums, -heappop(self.max_heap_for_small_nums))
        elif len(self.max_heap_for_small_nums) < len(self.min_heap_for_large_nums):
            heappush(self.max_heap_for_small_nums,-heappop(self.min_heap_for_large_nums))

    def find_median(self):
        if len(self.min_heap_for_large_nums) == len(self.max_heap_for_small_nums):
            return self.min_heap_for_large_nums[0]/2.0 +  -self.max_heap_for_small_nums[0]/2.0
        return -self.max_heap_for_small_nums[0]/1.0


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    median = MedianOfStream()
    for num in nums:
        median.insert_num(num)
        print(num)
        print(median.find_median())
