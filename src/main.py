
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

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        A.sort()
        index = len(A) - 1
        while index >= 2:
            if (A[index - 1] + A[index - 2] > A[index]):
                return A[index - 1] + A[index - 2] + A[index]
            index -= 1
        return 0


if __name__ == "__main__":
    s1 = Solution()
    print s1.detectCapitalUse("mL")