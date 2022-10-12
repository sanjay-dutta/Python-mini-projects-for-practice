import random
passlen = int(input("enter the length of password"))
# stored the letters, numbers and special characters that I want to be considered while generating a password
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#doing a random sampling by joining the length of the password and the variable s, which will finally generate a random password
p = "".join(random.sample(s,passlen ))
print(p)