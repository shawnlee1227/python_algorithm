import collections
import re


class Palindrome:

    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # if char is alphanumeric
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
    
    def isPalindromeDeque(self, s: str) -> bool:
        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
    
    def isPlaindromeSlice(slef, s: str) -> bool:
        strs = s.lower()

        # search pattern and replace
        strs = re.sub('[^a-z0-9]', '', strs)

        return strs == strs[::-1]

    # test
    def testPalindrome(self, s: str):
        answer = self.isPalindrome(s)
        answerDeque = self.isPalindromeDeque(s)
        answerSlice = self.isPlaindromeSlice(s)
        print(f"""Is '{s}' a valid palindrome?
            List: {answer}
            Deque: {answerDeque}
            Slice: {answerSlice}""")


p = Palindrome()
p.testPalindrome("Kayak")
p.testPalindrome("Race Car")
p.testPalindrome("Rotators")
