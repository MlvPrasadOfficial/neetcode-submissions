class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        t = target
        i = 0 
        j = len(nums) -1 
        if j ==0 :
            if nums[j] == t :
                return True
            else :
                return False

        z = 0   
        # if i  
        print(i,j,"--")
        while i < j :
            z+=1
            print("hi")
            # print(i,nums[i],t)
            if nums[i] == t :
                return True
            elif nums[j] == t :
                return True

            mid = (i+j)//2
            if nums[mid] == t :
                return True
            print("pre",i,mid,j,"--",nums[i],nums[mid],nums[j])

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
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            elif nums[mid] < nums[j] and t > nums[mid] and t < nums[j] :
                print("2")
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
                i = mid 
                print(i,mid,j,"--",nums[i],nums[mid],nums[j])
 
            elif nums[mid] == nums[i] and nums[mid] == nums[j]  :
                i = i + 1

            # elif nums[mid] == nums[i] and t >  nums[mid]  :
            #     print("2")
            #     print(i,mid,j,"--",nums[i],nums[mid],nums[j])
            #     i = mid 
            #     print(i,mid,j,"--",nums[i],nums[mid],nums[j])
       


            print("----------------")
            if i+1 ==j:
              return False
            if z == 10:
              print(z)
              break       
           
        return False
        