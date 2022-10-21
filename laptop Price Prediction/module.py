def fact(number):
    num=number
    fact=1
    while number>1:
        fact=fact*number
        number=number-1
    return fact