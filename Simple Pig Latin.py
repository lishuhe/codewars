# Pig Latin
# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.


    
def pig_it(text):
    pig_text = text.split()
    pig_list = []
    result = []
    punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    
    for word in pig_text:
        if word not in punctuation:
            word = word[1:] + word[0] + 'ay'
            pig_list.append(word)
        else:
            pig_list.append(word)

    result = ' '.join(pig_list)
    return result
    
# test cases
pig_it('O tempora o mores !')
pig_it('hello world')