def reverseStringTwoPointer(s: list[str]) -> None:
    first, last = 0, len(s) - 1
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1
    print(s)


l = ['h','e','l','l','o']
reverseStringTwoPointer(l)