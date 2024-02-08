class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1
        mid = 0
        while 1:
            if head == tail - 1 or head == tail:
                if nums[tail] < target:
                    return tail+1
                elif nums[head] > target:
                    return head
                elif nums[tail] == target:
                    return tail
                elif nums[head] == target:
                    return head
                else:
                    return tail
            mid += (tail-head)//2

            if nums[mid] == target:
                print(mid)
                return mid
            elif nums[mid] < target:
                head = mid
            else:
                tail = mid
                mid = 0
            
        return 0


        