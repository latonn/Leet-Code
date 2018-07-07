class Solution(object):
        ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans




