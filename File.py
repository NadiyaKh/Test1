#Copyright unknown 
from string import ascii_lowercase as az


def check(text):
    return set(text.lower()).issuperset(set(az))

<<<<<<< HEAD
print(check('abc'))
=======
print(check('abc') == False)
print(check('abcdefghijklmnopqrstuvwxyz') == True)
print(check('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True)
print(check('Quick brown fox jumps over the lazy dog') == True)
>>>>>>> testing
