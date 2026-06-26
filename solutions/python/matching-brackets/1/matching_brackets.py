def is_paired(input_string):
    stack = []
    
    for character in input_string:
        if character == '(' or character == '{' or character == '[':
            stack.append(character)
        elif character == ')':
            if stack == []:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif character == '}':
            if stack == []:
                return False
            elif stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif character == ']':
            if stack == []:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack == []:
        return True
    return False
        
