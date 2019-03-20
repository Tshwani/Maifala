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

    if n == 1:
        return n
    else:
        return n *  factorial(n-1)
