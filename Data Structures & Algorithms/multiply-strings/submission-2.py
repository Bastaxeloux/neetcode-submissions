class Solution:
    def str_to_int(self,s):
        if s == "0":
            return 0
        elif s == "1":
            return 1
        elif s == "2":
            return 2
        elif s == "3":
            return 3
        elif s == "4":
            return 4
        elif s == "5":
            return 5
        elif s == "6":
            return 6
        elif s == "7":
            return 7
        elif s == "8":
            return 8
        elif s == "9":
            return 9

    def multiply(self, num1: str, num2: str) -> str:
        int1,int2=0,0
        for i in range(len(num1)):
            int1 += self.str_to_int(num1[i]) * (10**(len(num1)-1-i))
        for j in range(len(num2)):
            int2 += self.str_to_int(num2[j]) * (10**(len(num2)-1-j))
        print(f"int1={int1}, int2={int2}")
        return str(int1*int2)