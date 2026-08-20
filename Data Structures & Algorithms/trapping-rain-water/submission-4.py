class Solution:
    def nextWall(self, liste, i_depart):
        found = True
        n = len(liste)
        i = i_depart + 1
        biggest, i_biggest = liste[i], i
        while found and (i <= n - 1):
            # print("OK")
            mur = liste[i]
            if mur >= liste[i_depart]:
                # print(f"vrai avec i_a={i_depart} et indice trouvé {i}. Hauteur en i_a = {liste[i_depart]} et hauteur en i_b = {liste[i]}")
                found = False
                return i
            if mur >= biggest :
                biggest, i_biggest = mur, i
            i += 1
        return i_biggest
        

    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        i_a, i_b = 0,0
        while i_a <= n-2 :
            i_b = self.nextWall(height, i_a)
            # print(f"i_a={i_a}, i_b={i_b}")
            water_temp = min(height[i_a],height[i_b])*(i_b-i_a-1) - sum(height[i_a+1:i_b])
            if water_temp > 0 :
                water += water_temp
            i_a = i_b
        return water
            