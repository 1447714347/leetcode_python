
class Solution(object):
    def detectCapitalUse(self, word):
        if len(word) == 1:
            return True
        else:
            if word.islower():
                return True
            if word[0].isupper():
                if word[1:].islower() | word[1:].isupper():
                    return True
        return False

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

if __name__ == "__main__":
    s1 = Solution()
    print s1.detectCapitalUse("mL")