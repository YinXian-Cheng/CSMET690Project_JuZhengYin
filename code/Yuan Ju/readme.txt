Elgamal:
1.Alice:
Receive imformation from Bob:prime: 2039091589 next prime: 97 public key component: 1660146964
Generate c1,c2 from message 97123:(1041777339, 938258062) and resend to Bob
2.Bob:
generate keys: prime:1008158228250056683,primitive_root:386158545107796321 and send to Alice
Receiving encrypted message from Alice:(883003325782855760, 744730117350543654)
decrypt the message:27586972865048988
3. Eve:
decipher failed cause the number is too large and the program reach the limitation
RSA:
1.Alice:
Receive imformation from Bob: RSA public_key: (65537, 2263088288228123623)
Generate c1,c2 from message 827193:1913668455974556533 and resend to Bob
2.Bob:
generate keys: public key(e,n):(2147483651,3196621149927423389) keep secret key 1574871931184208959 and sent to Alice
Receiving encrypted message from Alice:3076366032960990332
decrypt the message:5481293
3.Eve:
decipher failed cause the number is too large which is impossible to get two large prime numbers in a limited time