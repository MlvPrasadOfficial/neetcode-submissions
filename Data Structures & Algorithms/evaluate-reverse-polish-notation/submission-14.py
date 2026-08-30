class Solution:
    def evalRPN(self, tokens: List[str]) -> int:     

        if len(tokens) == 1 :
            return int(tokens[0])

        temp = []
        for i in tokens :
            if i == "+" :
                c = temp[-2] + temp[-1] 
                temp.pop()
                temp.pop()
                temp.append(c)
            elif i == "-" :
                c = temp[-2] - temp[-1] 
                temp.pop()
                temp.pop()
                temp.append(c)
            elif i == "/" :
                c = int(temp[-2] / temp[-1])
                temp.pop()
                temp.pop()
                temp.append(c)
            elif i == "*" :
                c = temp[-1] * temp[-2] 
                temp.pop()
                temp.pop()
                temp.append(c)
            else :
                temp.append(int(i))


        return temp[-1]