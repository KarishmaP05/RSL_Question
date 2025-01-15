
def is_balanced(s):
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        elif char ==')':
            if not stack:
                return False
            stack.pop()

    return len(stack)==0

s="()()"
result=(f"string {s}  is balanced :{is_balanced(s)}")
print(result)