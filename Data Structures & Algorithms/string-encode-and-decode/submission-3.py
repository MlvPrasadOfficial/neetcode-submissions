class Solution:

    def encode(self, strs: List[str]) -> str:


        e = ""


        for i in strs :
            # print(i)
            e += str(len(str(len(i))))
            e += str(len(i))
            e += i
        # print("p"+e)

        return e

    def decode(self, s: str) -> List[str]:
        print(s)

        ls = []

        i = 0 

        while i <len(s) :
            # print(s[i])
            # num of letters of number
            numofletters =int(s[i])
            # get number
            print(i,numofletters)
            num = int(s[i+1 :i+numofletters+1])       
            temp = s[i+numofletters+1:i+numofletters+num+1]
            # print(i+1,ln,temp)
            ls.append(temp)

            i = i + numofletters + num + 1
            # print(i)
        return ls 