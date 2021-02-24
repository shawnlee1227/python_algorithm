def reverseStringTwoPointer(s: list[str]) -> None:
    first, last = 0, len(s) - 1
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1
    print(s)

def reverseStringPythonic(s: list[str]) -> None:
    s.reverse()
    print(s)


l1 = ['h','e','l','l','o']
l2 = ['w','o','r','l','d']
reverseStringTwoPointer(l1)
reverseStringPythonic(l2)