import random

x = 10

while True:
    print("display..")
    x -= 1 # 9 8 7 ...
    if x == 0:
        break

print("-"*15)

def is_prime(n):
    if n <= 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True
print(is_prime(9)) 

print("-"*15)

num = random.randrange(1,10)
print(num)