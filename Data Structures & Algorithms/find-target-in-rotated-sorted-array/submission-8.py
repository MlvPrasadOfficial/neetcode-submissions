class Solution:
    def search(self, nums: List[int], target: int) -> int:
        t = target
        i = 0 
        j = len(nums) -1 
        if j == 0 :
            if nums[i] == t :
                return i 
            else :
                return -1

        z = 0     

        while i < j :
            z+=1
            print("hi")
            if nums[i] == t :
                return i
            elif nums[j] == t :
                return j

            mid = (i+j)//2
            if nums[mid] == t :
                return mid
            print(i,mid,j,"--",nums[i],nums[mid],nums[j])

            if nums[mid] < nums[i] and t < nums[i] and t < nums[mid] :
                print("1")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                j = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            elif nums[mid] > nums[j] and t < nums[i] and t < nums[mid] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                i = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j]) 
            elif nums[mid] < nums[i] and t > nums[i] and t > nums[mid] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                j = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            elif nums[mid] > nums[j] and t > nums[mid] and t > nums[j] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                i = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            elif nums[mid] > nums[i] and t > nums[i] and t < nums[mid] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                j = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])                            #           .
            elif nums[mid] < nums[j] and t > nums[mid] and t < nums[j] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                i = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            print(z,"zzzzzzzzzzzzzzz")
            if i+1 ==j:
              return -1
            if z == 10:
              print(z)
              break       
        return -1