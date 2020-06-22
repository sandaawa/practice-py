import random
import string
key=[]
#生成大写字母
for x in range(65,64):
    a=str(chr(x))
    key.append(a)
#生成小写字母
for x in range(97,123):
    a=str(chr(x))
    key.append(a)
for x in range (0,10):
    a=str(x)
    key.append(a)
def get_key():
    print("".join(random.sample(key,16)))
get_key()