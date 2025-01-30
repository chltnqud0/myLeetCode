from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sorted_list = SortedList()
        self.even = True
        self.leng = 0
    def addNum(self, num: int) -> None:
        self.even = not self.even
        self.sorted_list.add(num)
        self.leng += 1

    def findMedian(self) -> float:
        if self.even:
            return (self.sorted_list[self.leng // 2] + self.sorted_list[self.leng // 2 - 1]) / 2
        else:
            return self.sorted_list[self.leng // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()