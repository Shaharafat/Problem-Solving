class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_array = list(map(lambda x: x*x, nums))


        return self.quick_sort(squared_array)
        # print(self.quick_sort(squared_array))

    def quick_sort(self, list_to_be_sorted: list[int]) -> list[int]: 
      if len(list_to_be_sorted) <= 1:
        return list_to_be_sorted
      else:
        pivot = list_to_be_sorted[0]
        less = [i for i in list_to_be_sorted[1:] if i <= pivot]
        more = [i for i in list_to_be_sorted[1:] if i > pivot]

        return self.quick_sort(less) + [pivot] + self.quick_sort(more)


if __name__ == "__main__":
    solution = Solution()
    solution.sortedSquares([-4,-1,0,3,10])
