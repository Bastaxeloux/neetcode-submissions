class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,b = 0, len(nums)-1
        mid = 0
        #print(nums)
        # first search the pivot 
        while a < b :
            mid = a + (b-a)//2
            #print(f"a={a},b={b} et mid={mid}")
            if nums[mid] > nums[a]:
                a = mid
                #print(f"a now ={a}")
            else : 
                b = mid
                #print(f"b now ={b}")
        mid += 1
        #print(f"pivot = {mid}")
        left = nums[:mid]
        right = nums[mid:]
        l,r = 0, len(left)
        #print(f"left = {left} and right = {right}")
        while l<r:
            mid = l + (r-l)//2
            #print(f"l={l},r={r} et mid={mid}")
            if left[mid] == target:
                return mid
            elif left[mid] > target:
                r = mid
            else : l = mid + 1
        #print("not found in left")
        l,r = 0, len(right)
        while l<r:
            mid = l + (r-l)//2
            # print(f"l={l},r={r} et mid={mid}")
            if right[mid] == target:
                return mid + len(left)
            elif right[mid] > target:
                r = mid
            else : l = mid + 1
        return -1