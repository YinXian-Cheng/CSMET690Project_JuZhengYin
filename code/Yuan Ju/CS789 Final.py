# -*- coding: utf-8 -*-
"""
Created on Sat Dec 9 22:34:03 2023

@author: 35132
"""


import random

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
 