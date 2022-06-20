# As the name may already reveal, it works basically like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(


def tribonacci(signature, n):
    result = []
    if n <= 3:
        return signature[0:n]
    else:
        result.extend(signature)
        while len(result) < n:
            last_three_digits = result[len(result)-3:len(result)]
            sum_of_last_three = sum(last_three_digits)
            result.append(sum_of_last_three)
    return result

# test case
test = [50,49,138]
print(tribonacci(test,2))