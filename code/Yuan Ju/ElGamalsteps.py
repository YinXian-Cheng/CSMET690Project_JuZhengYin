# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:11:18 2023

@author: 35132
"""
from CS789Final import fastExp,inverse
import random
import time

class Elgamal:
    '''g-generator, y-public key, p-modulus, x-private key'''
    def __init__(self,g,x,p):
        self.g = g
        self.x = x
        self.p = p
        self.y = fastExp(self.g,self.x,self.p)
        self.Limit_searching_time = 3600

    def encrypt(self,msg):
        r = random.randint(2,self.p-2)
        print("r",r)
        c1 = fastExp(self.g,r,self.p)
        c2 = (msg*fastExp(self.y,r,self.p)) % self.p
        return c1,c2
    
    def decrypt(self,c1,c2):
        a = fastExp(c1,self.x,self.p)
        msg = (c2 * inverse(a,self.p)) % self.p
        return msg
    
    def Elgamal_decipher(self,c1,c2):
        start_time = time.time()
        self.x = -1
        for i in range(1, self.p):
            if time.time() - start_time > self.Limit_searching_time:
                break
            if fastExp(self.g, i, self.p) == self.y:
                self.x = i
        a = fastExp(c1,self.x,self.p)
        msg = (c2*inverse(a,self.p))%self.p
        return msg