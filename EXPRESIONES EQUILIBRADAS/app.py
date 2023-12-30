def balanced(expression):
    stack = []

    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
            print(stack)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack 

expresion = "3 * (2 + 5) / {4 - (1 + 2)}"
resultado = balanced(expresion)
print("La expresión está equilibrada:", resultado)
