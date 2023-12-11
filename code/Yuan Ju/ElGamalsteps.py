# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:11:18 2023

@author: 35132
"""
from CS789_Final import fastExp,random_prime
import random

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    
def inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return -1 #not exist
    else:
        return x % m
    
class Elgamal:
    '''g-generator, y-public key, p-modulus, x-private key'''
    def public_key(g,x,p):
        y = fastExp(g,x,p)
        return y

    def encrypt(msg,g,p,y):
        r = random.randint(2,p-2)
        c1 = fastExp(g,r,p)
        c2 = (msg* fastExp(y,r,p)) % p
        return c1,c2
    
    def decrypt(x,p,c1,c2):
        a = fastExp(c1,x,p)
        msg = (c2 * inverse(a,p)) % p
        return msg
    
    def Exe_hack():
        return 0