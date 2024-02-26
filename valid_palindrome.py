class Solution:
    def isPalindrome(self, s: str) -> bool:
        text1 = s.lower()
        text2 = "".join(i for i in text1 if i.isalnum())
        p1 = 0
        p2 = -1
        res = True
        for i in text2:
            if text2[p1] == text2[p2]:
                p1 += 1
                p2 -= 1
            else:
                res = False

        return res