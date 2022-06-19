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