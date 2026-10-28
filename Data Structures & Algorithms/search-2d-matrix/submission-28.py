class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = target
        m = matrix

        r = len(m)
        c = len(m[0])
        # outside boundary
        print("m")
        check = 0 
        if t < m[0][0] or t > m[-1][-1]  :
            return False
        if t >= m[r-1][0] and t <= m[r-1][-1] :
            check = r - 1
            print("l")
        else :
            print("m1")
            i = 0 
            j = r-1
            while i < j :
                if m[i][0] == t or m[j][0] == t:
                    return True
                elif j - i == 1:
                    check = i
                    break 
                mid = (i + j) //2
                print(mid,"mid")
                if m[mid][0] == t :
                    return True
                elif m[mid][0] > t :
                    j = mid
                elif m[mid][0] < t :
                    i = mid

        
        ls = m[check]
        print("check",ls)
        a = 0 
        b = len(ls) - 1
        if b == 0 :
          if ls[0] == t :
            return True
          else :
            return False
        while a < b :
            if ls[a] == t or ls[b] == t:
                return True
            elif b - a == 1:
                return False

            mid = (a + b) //2

            if ls[mid] == t :
                return True
            elif ls[mid] > t :
                b = mid
            elif ls[mid] < t :
                a = mid

        # return False














        

        