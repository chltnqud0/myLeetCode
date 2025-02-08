class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n,'b')
        d = ''
        for i in range(len(b)):
            d += b[-1-i]
        
        d += '0' * (32 - len(b))

        return int(d, 2)