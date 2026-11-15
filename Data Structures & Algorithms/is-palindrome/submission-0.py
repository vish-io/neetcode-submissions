import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = str.maketrans('','', string.punctuation + ' ')
        c = s.translate(x).lower()
        return c == c[::-1]