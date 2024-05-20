def reverse_string(string):
    stack = []

    for char in string: 
        stack.append(char)

    reversed = ""  
    while stack: 
        reversed += stack.pop()

    return reversed 

print(reverse_string("hello"))

# It initializes an empty stack.
# It iterates through each character in the input string and pushes them onto the stack.
# It initializes an empty string to hold the reversed string.
# It pops characters from the stack one by one and appends them to the reversed string.
# Finally, it returns the reversed string.

def evaluate_keystrokes(string): 
    i=len(string)-1
    result = ""
    skip = 0
    
    while i >= 0:
        if string[i]== "<":
            skip += 1
            i -= 1
        else: 
            if skip >0:
                 i-=skip
                 skip =0
            else: 
                result = stringi[i]+result
                i-=1
    return result                     

# approaching the same problem using stack

def evaluate_keystrokes(string):
    stack = []
    for char in string: 
        if char == "<":
            if len(stack) != 0: 
                stack.pop()
        else: 
            stack.append(char)

    result =""
    while stack: 
        result = stak.pop() + result

    return result