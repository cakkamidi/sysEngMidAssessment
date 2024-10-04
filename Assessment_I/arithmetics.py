import random

N = int(input("Jumlah bilangan deret aritmatika : "))

randomA = random.randint(1,100)
randomB = random.randint(1,20)

result = [randomA]
for i in range(N-1):
    result.append(randomA+randomB*(i+1))

print(result)