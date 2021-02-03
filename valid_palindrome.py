import collections


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

    # test
    def testPalindrome(self, s: str):
        answer = self.isPalindrome(s)
        answerDeque = self.isPalindromeDeque(s)
        print(f"""Is '{s}' a valid palindrome?
            List: {answer}
            Deque: {answerDeque}""")


p = Palindrome()
p.testPalindrome("Kayak")
p.testPalindrome("Race Car")
p.testPalindrome("Rotators")
