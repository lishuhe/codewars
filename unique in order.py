#Implement the function unique_in_order which takes as argument a sequence and returns a list of items
#without any elements with the same value next to each other and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(test):
    result = []
    if len(test) > 1:
        for i in range(len(test)-1):
            if test[i] != test[i+1]:
                result.append(test[i])
        result.append(test[len(test)-1])
    elif len(test) == 1:
        result.append(test)
    else:
        result = []
    return result

#test case
print(unique_in_order('hello world'))