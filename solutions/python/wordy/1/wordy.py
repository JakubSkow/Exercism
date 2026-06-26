def answer(question):
    if not(question.startswith("What is ")) or not(question.endswith("?")):
        raise ValueError("syntax error")

    question = question[8:-1]

    tokens = question.split()

    if not(tokens[0].lstrip("-").isdigit()):
        raise ValueError("syntax error")
        
    result = int(tokens[0])
    
    i = 1
    while i < len(tokens):
        if tokens[i] == "plus":
            if i+1 >= len(tokens) or not tokens[i+1].lstrip("-").isdigit():
                raise ValueError("syntax error")
            result += int(tokens[i+1])
            i += 2
            
        elif tokens[i] == "minus":
            if i+1 >= len(tokens) or not tokens[i+1].lstrip("-").isdigit():
                raise ValueError("syntax error")
            result -= int(tokens[i+1])
            i += 2
            
        elif tokens[i] == "multiplied":
            if i+2 >= len(tokens) or tokens[i+1] != "by":
                raise ValueError("unknown operation")
            if not tokens[i+2].lstrip("-").isdigit():
                raise ValueError("syntax error")
            result *= int(tokens[i+2])
            i += 3
            
        elif tokens[i] == "divided":
            if i+2 >= len(tokens) or tokens[i+1] != "by":
                raise ValueError("unknown operation")
            if not tokens[i+2].lstrip("-").isdigit():
                raise ValueError("syntax error")
            result //= int(tokens[i+2])
            i += 3

        else:
            if tokens[i].lstrip("-").isdigit():
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

    return result
        
