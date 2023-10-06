#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    argsLen = len(args)

    if argsLen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    match args[2]:
        case '+':
            operator = add
            op = '+'
        case '-':
            operator = sub
            op = '-'
        case '*':
            operator = mul
            op = '*'
        case '/':
            operator = div
            op = '/'
        case default:
            print("Unknown operator. Available operators: +, -, * and / f")
            sys.exit(1)

    a = int(args[1])
    b = int(args[3])

    print(f"{a:d} {op} {b:d} = {operator(a, b):d}")
