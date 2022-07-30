# all ways import lib.
import random
passlen = int(input("enter the length of password"))
# I use "abc" ,"123","@#$$$
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)






#OUTPUT 
'''
enter the length of password 30
h!OA@JU$f%K0FiM^dW)1Hk&Rug(t82  # NEW password gen..
'''
