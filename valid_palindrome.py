class Solution:
    def isPalindrome(self, s: str) -> bool:
        text1 = s.lower()
        text2 = "".join(i for i in text1 if i.isalnum())
        l = 0
        r = -1
        res = True
        for i in text2:
            if text2[l] == text2[r]:
                l += 1
                r -= 1
            else:
                res = False

        return res