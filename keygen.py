# RESOURCS USED:
# https://pynative.com/python-secrets-module/

import hashlib
import secrets
import random

def generate_key():
    bits = secrets.randbits(256) 
    bits_hex = hex(bits)
    global gen_key
    gen_key = bits_hex[3:]
    print(gen_key)
    print(len(gen_key)) #63
    # my_key = 'c1b8ee89e5e57467a7756bef5ffc73286bb2498bb98caf2228dd2ddff781c9c'
    # you_key = 'c1b8ee89e5e57467a7756bef5ffc73286bb2498bb98caf2228dd2ddff781c9c'
    # print(secrets.compare_digest(you_key, my_key))


generate_key()

def validate_key(gen_key):
    guess = input('Key is 63 characters, a mix of letters and numbers. Guess:')
    print(secrets.compare_digest(gen_key, guess))

validate_key(gen_key)



