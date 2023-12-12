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
        self.y = fastExp(g,x,p)
        self.Limit_searching_time = 3

    def encrypt(self, msg):
        en_msg = []
        r = random.randint(2, self.p - 2)
        c = fastExp(self.g, r, self.p)
        c2 = fastExp(self.y, r, self.p)

        for i in range(0, len(msg)):
            en_msg.append(msg[i])
        for i in range(0, len(en_msg)):
            en_msg[i] = c2 * ord(en_msg[i])
        return en_msg, c

    def decrypt(self, en_msg, c):
        temp = []
        a = fastExp(c, self.x, self.p)
        for i in range(0, len(en_msg)):
            temp.append(chr(int(en_msg[i] / a)))
        msg = ""
        return msg.join(temp)

    def encrypt_old(self, msg):
        r = random.randint(2, self.p - 2)
        c1 = fastExp(self.g, r, self.p)
        c2 = (msg*fastExp(self.y, r, self.p))%self.p
        return c1,c2

    def decrypt_old(self, c1, c2):
        a = fastExp(c1, self.x, self.p)
        msg = (c2*inverse(a,self.p))%self.p
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