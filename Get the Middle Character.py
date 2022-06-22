# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

# Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"

#Input: A word (string) of length 0 < str < 1000. You do not need to test for this. 
# This is only here to tell you that you do not need to worry about your solution timing out.

#Output: The middle character(s) of the word represented as a string.
    
    
    
def get_middle(s):
    a = 0
    b = 0
    result = 0
    if len(s) % 2 == 0:
        a = int(len(s)/2)
        result = s[a-1:a+1]
        return result
    else:
        b = len(s)/2
        a = int(b)
        result = s[a]
        return result
    
# test cases
get_middle("test")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")