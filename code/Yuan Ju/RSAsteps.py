# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:11:19 2023

@author: 35132
"""


from CS789_Final import fastExp

class rsa:
    def __init__(self,p,q):
        self.p = p
        self.q = q
        self.n = p*q
        self.t = (p-1)*(q-1)
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        elif a % b == 0:
            return b;
        else:
            return self.gcd(b, a % b)
        
    def public_key(self):
        for i in range(2,self.t):
            if self.gcd(i, self.t)==1:
                return i
        return -1 #not find
    
    def private_key(self):
        d = 0
        e = self.public_key()
        while(True):
            if (d*e)%self.t == 1:
                return d
            d+=1
        return -1 #not find
    def RSA_encrypt(msg, public_key, n):
        return fastExp(msg, public_key, n)
    
    
    def RSA_decrypt(en_msg, private_key, n):
        return fastExp(en_msg, private_key, n)
    
    '''n-modulo, c-encrypted messsage, e-public key'''
    def decipher(n, c, e):
        #try to calculate one p-q pair
        data = []
        for i in range(2, n):
            if n % i == 0:
                data.append(i)
        # using euler theorem p,q are data[0],data[1]
        a = (data[0] - 1) * (data[1] - 1)
        #try to reach a private index
        d = 0
        for i in range(2, a):
            if i * e % a == 1:
                d = i
        return c ** d % n