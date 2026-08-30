class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        pos = {}
        l = 0 
        ans = 0 
        z =""
        # print("...")
        # print(len(s))
        for r in range(len(s)) :
            # print()
            # print("/////")
            # print("value of r = ", r)/
            # print("value of s[r] = ", s[r])

            if s[r] not in st :
                # print(f" {r} ,{s[r]} -- not there ")
                # print("add to st ")
                st.add(s[r])
                # print("st",st)
                # print("add pos")
                pos[s[r]] = r
                # print("pos",pos)/
                z = z + s[r]
                # print("z",z)

                ans = max(ans,r-l+1)
                # print("ans",ans)

            else :
                # print(f" {r} ,{s[r]} -- not there ")
                z = z + s[r]
                # print("z",z)
                l = pos[s[r]]
                l = l + 1

                pos[s[r]] = r 
                # print("pos",pos)
                st = set(z[l:r+1])
                

                ans = max(ans,l-r+1)
                # print("ans",ans)


        

        return ans 
