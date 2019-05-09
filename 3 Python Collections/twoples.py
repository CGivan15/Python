def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    print(product)
    return

multiply(2,4,2,2)    