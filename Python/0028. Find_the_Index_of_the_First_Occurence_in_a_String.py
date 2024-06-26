class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:(i+len(needle))] == needle:
                return i
            else:
                continue
        return -1