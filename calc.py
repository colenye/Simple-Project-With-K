while (True):
    num_1 = float(input('Enter the first number:'))
    num_2 = float(input('Enter the second number:'))
    sign = input('Enter the operator: ')

    if sign == '+':
        sum = float(num_1 + num_2)
        print(sum)
    elif sign == '*':
        product = float(num_1 * num_2)
        print(product)
    elif sign == '/':
        quotient = float(num_1 / num_2)
        print(quotient)
    else sign == '-':
        diff = float(num_1 - num_2)
        print(diff)





