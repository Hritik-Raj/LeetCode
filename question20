class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dictBracket = {']':'[', '}':'{', ')':'('}
        if len(s) == 1:
            return False
        for char in s:

            if char in dictBracket.values():
                stack.append(char)
            elif char in dictBracket.keys():
                if stack == [] or dictBracket[char] != stack.pop():
                    return False
        return stack == []
        
        
        # {[( 
#         if there is an opening bracket, add it to stack
#         only pop it off from stack if there is a matching closing bracket

#         queue is fifo - not this
#         stack is lifo - this one
        
# once all the characters are done, the stack should be empty, otherwise return false
