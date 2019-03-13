#!/usr/bin/env python3

import operator
#import random
import fractions


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def test():
    print("testing coverage")

def main():
    while True:
        result = calculate(str(input("rpn calc> ")))
        print("Result: ", fractions.Fraction(result))
    #print(random.randint(1, 100))

test()

if __name__ == '__main__':
    main()
