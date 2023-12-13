# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:40:26 2023

@author: 35132
"""
import CS789Final
import ElGamalsteps
import RSAsteps
import random

#Function Test Part

if __name__== '__main__':
    '''Fast Modulus Exponential Algorithm'''
    assert(CS789Final.fastExp(1,1,1)==pow(1,1,1))
    assert(CS789Final.fastExp(1,0,1)==pow(1,0,1))
    assert(CS789Final.fastExp(1234567,12345,123456)==pow(1234567,12345,123456))
    assert(CS789Final.fastExp(0,0,1)==pow(0,0,1))
    assert(CS789Final.fastExp(0,12,1)==pow(0,12,1))
    assert(CS789Final.fastExp(0,12,124)==pow(0,12,124))
    assert(CS789Final.fastExp(12,0,124)==pow(12,0,124))
    print("Fast Modulus Exponential Algorithm success\n")
    
    '''Millar Rabin Algorithm'''
    assert(CS789Final.MillerRabin(2, 10))
    assert(not CS789Final.MillerRabin(24, 10))
    assert(CS789Final.MillerRabin(13, 10))
    assert(CS789Final.MillerRabin(3, 10))
    assert(CS789Final.MillerRabin(5, 10))
    assert(CS789Final.MillerRabin(7, 10))
    assert(CS789Final.MillerRabin(97, 10))
    assert(CS789Final.MillerRabin(17, 10))
    assert(not CS789Final.MillerRabin(128371982, 10))
    print("Millar Rabin Algorithm success\n")
    '''random prime generator Algorithm, generate random prime value from 2 to 2^n'''
    assert(CS789Final.random_prime(1))
    assert(CS789Final.random_prime(2))
    assert(CS789Final.random_prime(10))
    assert(CS789Final.random_prime(100))
    assert(CS789Final.random_prime(12))
    assert(CS789Final.random_prime(15))
    assert(CS789Final.random_prime(21))
    assert(CS789Final.random_prime(125))
    
    print("random prime generator Algorithm success\n")
    
    '''primitive roots search Algorithm'''
    CS789Final.primitiveRoots(13)
    CS789Final.primitiveRoots(97)
    CS789Final.primitiveRoots(23)
    CS789Final.primitiveRoots(37)
    
    print("primitive roots search Algorithm success\n")
    '''test RSA'''
    rsa = RSAsteps.rsa(CS789Final.random_prime(31), CS789Final.random_prime(31))
    print("rsa public key:",rsa.public_key())
    print("rsa private key:",rsa.private_key())
    msg = 1234
    en_msg = rsa.RSA_encrypt(msg)
    print("rsa encrypt message:",en_msg)
    print("rsa decipher message:",rsa.decipher(en_msg, rsa.public_key()))
    assert(rsa.RSA_decrypt(en_msg)==msg)
    msg = 90786273512
    en_msg = rsa.RSA_encrypt(msg)
    print("rsa encrypt message:",en_msg)
    print("rsa decipher message:",rsa.decipher(en_msg, rsa.public_key()))
    assert(rsa.RSA_decrypt(en_msg)==msg)
    msg = 753131234
    en_msg = rsa.RSA_encrypt(msg)
    print("rsa encrypt message:",en_msg)
    print("rsa decipher message:",rsa.decipher(en_msg, rsa.public_key()))
    assert(rsa.RSA_decrypt(en_msg)==msg)
    msg = 89738965
    en_msg = rsa.RSA_encrypt(msg)
    print("rsa encrypt message:",en_msg)
    print("rsa decipher message:",rsa.decipher(en_msg, rsa.public_key()))
    assert(rsa.RSA_decrypt(en_msg)==msg)
    print("RSA test success\n")
    
    '''Elgamal Algorithm'''
    p = CS789Final.random_prime(7)
    g = CS789Final.primitiveRoots(p)
    x = random.randint(1,p-2)
    Elgamal = ElGamalsteps.Elgamal(g, x, p)
    msg = "1234sad 1 1"
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = ""
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = "       "
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = "1111111111111111111111111"
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = "aaaaaaaaaaaaaaaaaaaaaaaa"
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    msg = ",,,d13sad yjhyuj,,asadassd,,,,,,,1 2,,,,,,,,,,,,asd12 ,,,,,,,,, dfsc as d12 dx s,,,,,,,"
    c1,c2 = Elgamal.encrypt(msg)
    assert(Elgamal.decrypt(c1, c2)==msg)
    print("ElGamal test success\n")
    e = ElGamalsteps.Elgamal(386158545107796321,147035761485578403,1008158228250056683)
    print(e.decrypt_old(883003325782855760,744730117350543654))
    msg = "1234"
    c1,c2 = Elgamal.encrypt_old(int(msg))
    print(e.decrypt_old(c1,c2))

    '''Elgamal process'''
    print("\nElgamal process")
    p = int(input("enter prime p: "))
    g = int(input("enter generator g"))
    x = random.randint(1,p-2)
    Elgamal = ElGamalsteps.Elgamal(g,x,p)
    branch = input("Choose function: 0--encrypt, 1--decrypt, else--wrong")
    if branch!='0' or branch !='1':
        print("wrong input")
    elif branch =='0':
        msg = int(input("enter message"))
        c1,c2 = Elgamal.encrypt_old(msg)
        print('c1:',c1,'c2',c2)
    elif branch == '1':
        c1 = int(input("enter cipher text1"))
        c2 = int(input("enter cipher text2"))
        print("original message:",Elgamal.decrypt_old(c1,c2))

    '''rsa process'''
    print("\nrsa process")
    rsa = RSAsteps.rsa(int(input("please enter prime p")), int(input("please enter prime q")))
    branch = input("Choose function: 0--encrypt, 1--decrypt, else--wrong")
    if branch!='0' or branch !='1':
        print("wrong input")
    elif branch =='0':
        msg = int(input("enter message"))
        en_msg = rsa.RSA_encrypt(msg)
        print('encrypted message:',msg)
    elif branch == '1':
        print("original message:",rsa.RSA_decrypt(int(input("please enter encrypted message"))))
