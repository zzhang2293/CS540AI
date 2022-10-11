import os.path
import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    # Implementing vectors e,s as lists (arrays) of length 26
    # with p[0] being the probability of 'A' and so on
    e = [0] * 26
    s = [0] * 26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            # strip: removes the newline character
            # split: split the string on space character
            char, prob = line.strip().split(" ")
            # ord('E') gives the ASCII (integer) value of character 'E'
            # we then subtract it from 'A' to give array index
            # This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char) - ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char) - ord('A')] = float(prob)
    f.close()

    return (e, s)


def shred(filename):
    # Using a dictionary here. You may change this to any data structure of
    # your choice such as lists (X=[]) etc. for the assignment
    X = dict()
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z']
    for i in alpha:
        X[i] = 0

    with open(filename, encoding='utf-8') as f:
        s = f.read()
        for i in s:
            if i.upper() in alpha:
                X[i.upper()] += 1
        # TODO: add your code here

    return X

def q2(filename):
    X = shred(filename)
    e, s = get_parameter_vectors()
    return format(X["A"] * math.log(e[0]), '.4f'), format(X["A"] * math.log(s[0]), '.4f')

def q3(filename):
    totalEng = 0
    totalSpan = 0
    X = shred(filename)
    e, s = get_parameter_vectors()
    j = 0
    for i in X.values():
        totalEng += i * math.log(e[j])
        totalSpan += i * math.log(s[j])
        j += 1

    Feng = math.log(0.6) + totalEng
    Fspan = math.log(0.4) + totalSpan
    return round(Feng, 4), round(Fspan, 4)

def q4(filename):
    e, s = q3(filename)
    if s - e >= 100:
        return 0, 1
    if s - e <= -100:
        return 1, 0
    probE = 1/(1 + math.e ** (s - e))
    probS = 1/(1 + math.e ** (e - s))
    return format(probE, '.4f'),  format(probS, '.4f')

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
def main(filename):
    x = shred(filename)
    print("Q1")
    for i in x.keys():
        print(i, x[i])
#print("hello")
#y = languageId("samples\\letter1.txt")
    print("Q2")
    a, b = q2(filename)
    print(a)
    print(b)
    print('Q3')
    e, s = q3(filename)
    print(e)
    print(s)
    print("Q4")
    pe, ps = q4(os.path.join(filename))
    print(pe)



main("samples/letter2.txt")