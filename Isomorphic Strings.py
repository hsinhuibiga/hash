#Isomorphic Strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        for i,x in enumerate(s):
            if x in dic.keys() and dic[x]!=t[i]:
                return  False
            elif x not in dic.keys() and t[i] in dic.values():
                return False
            else:
                dic[x]=t[i]

        return True

if __name__ == "__main__":
    print Solution().isIsomorphic("egg", "add")