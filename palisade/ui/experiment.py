'''
Created on 22.08.2013

@author: bova
'''
import string
import random

def id_generator(size=6, chars=string.ascii_lowercase+string.ascii_uppercase+\
                 string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == '__main__':
    print id_generator(32)
    