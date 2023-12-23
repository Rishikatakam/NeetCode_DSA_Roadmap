class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split(" ");
        for i in reversed(range(len(s))):
            if len(s[i])>0:
                return len(s[i])