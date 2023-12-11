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
        j = 0
        h = self.public_key()
        while(True):
            if (j*h)%self.t == 1:
                return j
            j+=1
        return -1 #not find
    def RSA_encrypt(msg, public_key, n):
        return fastExp(msg, public_key, n)
    
    
    def RSA_decrypt(en_msg, private_key, n):
        return fastExp(en_msg, private_key, n)


