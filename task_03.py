print("Enter expression:")
exp = input()

stack = []

def symmetry_check():
    for char in exp:
        if char in ["(", "[", "{"]:
            stack.append(char)

        if len(stack) != 0 and char in [")", "]", "}"]:
            match stack[-1]:
                case "(":
                    if char == ")":
                        stack.pop()
                case "[":
                    if char == "]":
                        stack.pop()
                case "{":
                    if char == "}":
                        stack.pop()
                
    if len(stack) == 0:
        return print("Symmetrically")
    else:
        return print("Not symmetrical")
    
symmetry_check()