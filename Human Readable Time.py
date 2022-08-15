'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

'''

def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"


#test cases
#make_readable(60)
#make_readable(12345)

'''


Notes:

Literal String Interpolation or more commonly as F-strings
(because of the leading f character preceding the string literal).
The idea behind f-strings is to make string interpolation simpler. 
To create an f-string, prefix the string with the letter “ f ”.
The string itself can be formatted in much the same way that you would with str.format().
F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting. 


"{:0>2d}" is a str.format function.

In the format string "{:0>2d}":
    
d means expecting an int:
>>> "{:d}".format(3)
'3'

2d means formats to 2 characters using padding (whitespace by default)
>>> "{:2d}".format(3)
' 3'

0> means using 0 as padding, and right adjust the result:
>>> "{:0>2d}".format(3)
'03'


'''