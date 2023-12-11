# -*- coding: utf-8 -*-
"""
Created on Sat Dec 9 22:34:03 2023

@author: 35132
"""


import random

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
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
def generate_public_key(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    e=7
    _,d,_=extended_gcd(7, phi)
    return n,d,e

def generate_key(p):
    a=format(p,"b")
    key=[]
    for i in a:
        key.append(i)
    while(1):
        if len(key)>=1024:
            break
        key.insert(0,0)
    return key
            
def breakdown(N):
    r=0
    while(1):
        if int(bin(N)[-1])==1:
            break;
        r+=1
        N>>=1
    d=N         
    return r,d

def fastExp(x, e, m):
    y = 1
    while e > 0:
        #if e is odd then make changes on y
        if int(bin(e)[-1])==1:
            y = (y * x) % m
        x = x ** 2 % m
        #already considered odd condition thus shift e by 1 bit
        e >>= 1
    return y

def MillerRabin(N, K):
    r,d=breakdown(N-1)
    a=0
    for i in range(K):
        flg = 0
        a=random.randint(2, N-2)
        x=fastExp(a,d,N)
        if x != 1 and x != N-1:
            for _ in range(r-1):
                x = fastExp(x, 2, N)
                if (x == 1):
                    return False
                if (x == N - 1):
                    flg=1
                    break
            if flg!=1:
                return False
            
    return True
            
def random_prime(n):
    r=0;
    while(1):
        r=random.randint(1, pow(2,n))
        if int(bin(r)[-1])==1 and MillerRabin(r, 10):
            break;            
    return r


def findPrimitiveRoot(p):
    import math
    arr = []
    phi = p - 1
    n = phi
    # Find prime factors
    while (n % 2 == 0) :
        arr.append(2) 
        n = n // 2
 
    #find all factors of p
    for i in range(3, int(math.sqrt(n)), 2):
        while (n % i == 0) :
            arr.append(i) 
            n = n // i
 
    for primitive in range(2, phi + 1): 
        #if r^(phi/x)mod n==1 Then primitive is not a primitive root
        #set a key to check if primitive is available
        key = False
        for x in arr: 
            if (fastExp(primitive, phi // x, n) == 1): 
                key = True
                break
        if not key:
            return primitive
    return -1
 
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


def RSA_encrypt(ptxt, pub1, pub2):
    return fastExp(ptxt, pub1, pub2)


def RSA_decrypt(cipher, pv1, pub2):
    return fastExp(cipher, pv1, pub2)


