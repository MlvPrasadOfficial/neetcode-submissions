class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        num = 0
        alpha = ""

        for i in s :
            print("---------",i)
            if i.isdigit() :
                num = (num * 10 )+ int(i) 
                print(stack,"stack1",i)
            if i.isalpha() :
                alpha = alpha + i 
                print(stack,"stack2",i)
            if i == "[" :
                stack.append([alpha,num])
                print(stack,"stack3",i)
                alpha = ""
                num = 0 
            if i == "]" :
                a,b = stack.pop()
                print(stack,"stack4",i)
                # print(a,b,num)
                alpha = a + (b*alpha) 
                print(alpha,"a")

        return alpha


            # ""   2
            # a 3

            # b


            

