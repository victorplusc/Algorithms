class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        todo, bit = num, 1
        while todo:
            num = num ^ bit
            bit = bit << 1
            todo = todo >> 1
        return num
