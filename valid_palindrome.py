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

    # test
    def testPalindrome(self, s: str):
        answer = self.isPalindrome(s)
        print(f"Is '{s}' a valid palindrome?\n{answer}")


p = Palindrome()
p.testPalindrome("Kayak")
p.testPalindrome("Race Car")
p.testPalindrome("Rotators")
