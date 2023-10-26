# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    string = list(string)
    string.reverse()
    return "".join(string)
    print(string)
    pass

#test cases
solution('world')
solution('')
