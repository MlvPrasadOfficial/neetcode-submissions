class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        al = {"a" : 0,
        "b":1,
        "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
        "k":10,
        "l":11,
        "m":12,
        "n":13,
        "o":14,
        "p":15,
        "q":16,
        "r":17,
        "s":18,
        "t":19,
        "u":20,
        "v":21,
        "w":22,
        "x":23,
        "y":24,
        "z":25}

        res = {}
        for i in strs :
            # print("////",i)
            store = [0]*26
            for j in i :
                store[al[j]] +=1
            # print("store",store)
            # print("res",res)
            if str(store) not in res :
                res[str(store)] = [i]
            else :
                addnew = res[str(store)]
                addnew.append(i)
                # print(addnew,"addnew",res[str(store)])
                res[str(store)] = addnew  
            # print("res",res) 
            # print()
        # print()         
        finalans = []
        for k in res :
            finalans.append(res[k])
        return finalans









        