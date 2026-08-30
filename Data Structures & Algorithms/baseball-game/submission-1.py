class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []



        for i in operations :
            if i =="+" :
                temp = ans[-1] + ans[-2]
                ans.append(temp)
            elif i == "C" :
                ans.pop()

            elif i == "D" :
                ans.append(2*ans[-1])
            else :
                ans.append(int(i))

        return sum(ans)