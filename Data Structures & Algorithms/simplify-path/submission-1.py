class Solution:
    def simplifyPath(self, path: str) -> str:



        r = path.split("/")
        stack = []
        print("r",r)

        for i in r :
            if i == ".." :
                if stack :
                    stack.pop()
            elif i == " " or i ==""  :
                continue
            elif i == "." :
                continue
            else :
                stack.append(i)
            print(stack)
        return "/" + "/".join(stack)
        