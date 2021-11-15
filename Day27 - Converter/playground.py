def adder(*args):
    total = 0
    for n in args:
        total += n
    print(total)

def calculate(n, **kwargs):
    if kwargs['add']:
        n += kwargs['add']
    n *= kwargs['multiply']
    return n

adder(1, 2, 3, 4, 5, 6)
print(calculate(3, multiply=4))