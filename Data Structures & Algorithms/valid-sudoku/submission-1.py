class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board :
            temp = []
            for j in i :
                if j != "." :
                    temp.append(j)
            if len(temp) != len(set(temp)) :
                return False
        for m in range(9) :
            temp = []
            for k in board :
                if k[m ] != "." :
                    temp.append(k[m])
            if len(temp) != len(set(temp)) :
                return False
        r = 3        
        while r <= 9 : # 3
            c = 3
            while c <=9 :
                temp = []
                for a in range(r-3,r) :
                    for b in range(c-3,c) :
                        if board[a][b] != "." :
                            temp.append(board[a][b])
                if len(temp) != len(set(temp)) :
                    return False
                c+=3
            r +=3 
        return True



                

        

        