# def increment(x):
#     return x + 1

# def decrement(x):
#     return x - 1

def eh_divisivel_por3(x):
    return x % 3 == 0

def eh_divisivel_por5(x):
    return x % 5 == 0

def eh_divisivel_por3e5(x):
    return eh_divisivel_por3(x) and eh_divisivel_por5(x)

def contem3(x):
    return '3' in str(x)

def contem5(x):
    return '5' in str(x)

def substituir(x):
    fizzbuzz =  "FIZZ" if eh_divisivel_por3(x) or contem3(x) else ""
    fizzbuzz += "BUZZ" if eh_divisivel_por5(x) or contem5(x) else ""

    return fizzbuzz if fizzbuzz != "" else str(x)

