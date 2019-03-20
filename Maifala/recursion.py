def sum_array(array):

    '''Return sum of all items in array'''

    sum_array_1 = 0
    for index in range (len(array)):
        sum_array_1 += array[index]
    return sum_array_1



def fibonacci(n):

    '''Return nth term in fibonacci sequence '''
    if n <= 1:
        return n

    else:
        return  fibonacci(n - 2) + fibonacci(n - 1)


def factorial(n):

    '''Return n!'''

    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n *  factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    reverse_word = ''
    for i in range(len(word)):
        reverse_word = word[i] + reverse_word
    return reverse_word
