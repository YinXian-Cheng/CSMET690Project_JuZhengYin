# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:34:03 2023

@author: 35132
"""


import time, socket, sys
import random
import bitstring
import hashlib


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
 
# Generating large random numbers
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key
 
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
# Asymmetric encryption
def elgamal_encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
 
    return en_msg, p
 
def elgamal_decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
         
    return dr_msg




def power_a(x, y, p):
 
    # Initialize result
    res = 1
 
    while (y > 0):
 
        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x
 
        # y must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2
 
    return res % p


def RSA_encrypt(ptxt,pub1,pub2):
    return power_a(ptxt, pub1, pub2)


def RSA_decrypt(cipher,pv1,pub2):
    return power_a(cipher, pv1, pub2)


