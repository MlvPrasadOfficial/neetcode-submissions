class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"(":")",
        "{":"}",
        "[":"]"}


        temp = []
        if len(s) == 0 :
            return True

        temp = [s[0]]

        for i in range(1,len(s)) : 
            print(temp,s[i])
            if len(temp) > 0 :
                if temp[-1] in ["(","[","{"] :
                    if pairs[temp[-1]] == s[i] :
                        # print
                        temp.pop()
                    else :
                        temp.append(s[i])
                else :
                    temp.append(s[i])



            else :
                temp.append(s[i])  


        if len(temp) == 0 :
            return True
        else :
            return False   