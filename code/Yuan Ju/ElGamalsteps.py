# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:11:18 2023

@author: 35132
"""
from CS789_Final import fastExp
import random
import time

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
    def __init__(self,g,x,p):
        self.g = g
        self.x = x
        self.p = p
        self.y = 0
        self.Limit_searching_time = 3600
    def public_key(self):
        self.y = fastExp(self.g,self.x,self.p)
        return self.y

    def encrypt(msg,g,p,y):
        r = random.randint(2,p-2)
        c1 = fastExp(g,r,p)
        c2 = (msg* fastExp(y,r,p)) % p
        return c1,c2
    
    def decrypt(x,p,c1,c2):
        a = fastExp(c1,x,p)
        msg = (c2 * inverse(a,p)) % p
        return msg
    
    def Elgamal_decipher(self,p,g,c1,c2,y):
        start_time = time.time()
        x = -1
        for i in range(1, p):
            if time.time() - start_time > self.Limit_searching_time:
                break
            if fastExp(g, i, p) == y:
                x = i
        a = fastExp(c1,x,p)
        msg = (c2*inverse(a,p))%p
        return msg