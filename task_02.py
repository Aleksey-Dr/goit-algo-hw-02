from collections import deque

d = deque()

print("Enter text:")
s = input()

def search_palindrome():
    for char in s.lower():
        d.append(char)

    while len(d) > 0:
        if not d.pop() == d.popleft() or len(d) == 1:
            return print("String is not palindrome")
        
    print("String is palindrome")

search_palindrome()