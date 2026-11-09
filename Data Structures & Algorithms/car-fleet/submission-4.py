class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pa = []

        for i in range(len(speed)):
            pa.append([position[i],speed[i]])

        pa.sort(reverse=True)

        fleet = []

        for p,t  in pa :
            fleet.append((target-p)/t)
            # print(fleet)

            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()



        return len(fleet)

        