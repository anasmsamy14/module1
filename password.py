import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""

for i in range(10):  
    password += random.choice(chars)

print('your password is :' \
'',password)