#Problem statement: Given a string s containing just the characters 
#'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s) -> bool:
        parenthesis = {')':'(', '}':'{', ']':'['}
        stack = [0]
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif parenthesis[i] != stack.pop():
                    return False
        if len(stack) != 1:
            return False
        return True

s = '(){}[]'
print(isValid(s))