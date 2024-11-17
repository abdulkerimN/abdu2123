class Solution:
    def isPalindrome(self, s: str) -> bool:

        string=[]

        for i in s:
            if i.isalnum():
                string.append(i.lower())
            else:
                continue
        index_comp=(len(string)+1)//2
        for i in range(index_comp):
            if string[i]==string[len(string)-1-i]:
                continue
            else:
                return False
        return True

