'''
Create a frame!
Given an array of strings and a character to be used as border, output the frame with the content inside.
Notes:
Always keep a space between the input string and the left and right borders.
The biggest string inside the array should always fit in the frame.
The input array is never empty.
'''


def frame(text, char):
    long = max(list(map(len, text))) + 4
    result = ''
    result += char * long + '\n'
    for string in text:
        if len(string) == long - 4:
            result += f'{char} {string} {char}\n'
        else:
            result += f'{char} {string}' + (' ' * (long - 4 - len(string))) + f' {char}\n'
    result += char * long
    return result


'''
Tribonacci Sequence
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, 
returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)    
'''


def tribonacci(signature, n):
    l = signature
    count = 0
    if n < 3:
        return signature[:n]
    else:
        for i in range(n - 3):
            signature = l[i:(i + 3)]
            count += sum(signature)
            l.append(count)
            count = 0
        return l

'''
Who likes it?
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' ' + 'likes this'
    elif len(names) > 1 and len(names) <= 3:
        return ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
    else:
        count = len(names) - 2
        return ', '.join(names[:2]) + ' and ' + str(count) + ' others like this'
