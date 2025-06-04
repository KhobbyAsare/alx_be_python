"""
LEGB

Local Enclosing Global Built-In


This is how python checks for a variable: Local -> Enclosing -> Global -> Built-in
"""

import builtins

print(dir(builtins))


def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)

count = 0

def increment(power:int = 1):
    global count
    count += power

    inner_count = 1

    def inner_increment():
        nonlocal inner_count
        inner_count +=2

    inner_increment()
    print(inner_count)

increment(5)
print(count)
