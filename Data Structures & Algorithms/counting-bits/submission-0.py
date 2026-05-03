class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]* (n + 1)
    
        for i in range(n+1):
            temp = i
            res = 0
            while temp:
                temp &= (temp-1)
                res += 1
            arr[i] = res
            res = 0
        return arr
        