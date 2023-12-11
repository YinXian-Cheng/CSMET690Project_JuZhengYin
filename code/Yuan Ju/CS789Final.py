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
    
def inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return -1 #not exist
    else:
        return x % m
    
def fastExp(x, e, m):
    if e==0:
        if m>1:
            return 1
        else:
            return 0
    if e<0:
        return -1
    y = 1
    while e > 0:
        #if e is odd then make changes on y
        if int(bin(e)[-1])==1:
            y = (y * x) % m
        x = x ** 2 % m
        #already considered odd condition thus shift e by 1 bit
        e >>= 1
    return y

def breakdown(N):
    r=0
    while(1):
        if int(bin(N)[-1])==1:
            break;
        r+=1
        N>>=1
    d=N         
    return r,d

def MillerRabin(N, K):
    if N==2 or N==3:
        return True
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
    if n == 1:
        return 2
    r=0;
    while(1):
        r=random.randint(2, pow(2,n))   
        if int(bin(r)[-1])==1 and MillerRabin(r, 5):
            break;            
    return r
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primitiveRoots(m):
    results = []
    s = set(i for i in range (1, m) if gcd(i, m) == 1)
    for g in range(1, m):
        primitives = set(fastExp(g, i, m)for i in range (1, m))
        if s == primitives:
            results.append(g)
    rand = random.randint(0,len(results)-1)
    print("primitive roots of",m,'are',results)
    return results[rand]