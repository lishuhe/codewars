# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second 
# character of the final pair with an underscore ('_').


# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
    
def solution(s):
    result = []
    string1 = []
    string2 = []
    if len(s) % 2 == 0:
        for i in range(0, len(s),2):
            string = s[i:i+2]
            result.append(string)
        return result
    elif len(s) % 2 == 1:
        for i in range(0, len(s)-1,2):
            string1 = s[i:i+2]
            result.append(string1)
        string2 = s[len(s)-1] + '_'
        result.append(string2)
        return result
    
# test cases
print(solution('abcdef'))
print(solution('x'))