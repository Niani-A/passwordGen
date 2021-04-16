import random

#create function to shuffle characters in string
def charShuffle(string):
    tList = list(string)
    random.shuffle(tList)
    return "".join(tList)

#Program starts
uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctuation1 = chr(random.randint(33,152))
punctuation2 = chr(random.randint(33,152))

#Password generation
password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + digit1 + digit2 + punctuation1 + punctuation2
password = charShuffle(password)

print(password)