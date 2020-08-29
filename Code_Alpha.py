alphabets = ['A','B','C','D','E','F','G','H',
     'I','J','K','L','M','N','O','P',
     'Q','R','S','T','U','V','W','X','Y','Z','.','#','%','!','?','/',','] # series of alphabets in order (plus some symbols)

def find_index(letter):
    '''Returns the index of the alphabet in the series of alphabet'''
    return alphabets.index(letter.upper())
    

def code_cyclic(index, letter):
    '''Cyclic transform of letters based on the index of the letter in the word and
     that in the series of alphabets in order
     Arguments (Parameters, I guess):
     _____________
     index - index of the letter in the word (type : int)
     letter - the letter to b coded (type : str)'''
    # The formula used here is : 26 * (index of the letter in word - 1) + (index of the
    # letter in the alphabets)
    # I had to use a separate variable 'index' to avoid the confusion the program gets when
    # choosing the index of the letter (eg, in the case of "HELLO", there are 2 'l' 's and this will cause confusion
    # This problem has been solved in the upcoming function.
    return 33 * index + (find_index(letter) + 1)

def code_word(word):
    '''codes each word with an array of numbers'''
    number_code = []
    i = 0
    for letter in word:
            number_code.append(code_cyclic(i, letter))
            i += 1
    return number_code

def  code_sentence(sentence):
    '''codes the given sentence into an array of numbers'''
    sentence_number_coded = []
    for word in sentence.split():
        sentence_number_coded.append(code_word(word))
    return sentence_number_coded

def  code_sentence_to_numeric_string(sentence):
    '''codes the given sentence into an array of numbers, each array transfored into a
    numeric string'''
    sentence_number_coded = []
    for word in sentence.split():
        string = ""
        for number in code_word(word):
            string += str(number)+"-"
        sentence_number_coded.append(string)
        sentence_number_coded.append('<space>')
    converted_string =  str().join(sentence_number_coded)
    # hope the <space> won't taunt you or disturb you... :)
    return converted_string

def tokenize_numstring(numstring):
    '''tokenizes the number code for processing'''
    words = [] # array of the words (tokens)
    string = ""
    for i in numstring:
        if (i not in ['<','>'] or i.upper() not in alphabets) and (i.isdigit() or i == '-'):
            string += i
        else:
            words.append(string)
            string = ""
    for i in range(words.count('')):
        words.remove('')
    return words

def decode(nstring):
    '''decodes the coded string and prints it on screen'''
    tokenized = tokenize_numstring(nstring)
    for word in tokenized:
        word_str = ""
        num = ""
        for i in word:
                if i != '-':
                        num += i
                else:
                        word_str += alphabets[(int(num) % 33) - 1]
                        num = ""
        print(word_str)

