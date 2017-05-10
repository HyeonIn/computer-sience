import random

print("이번주 로또 번호 입니다.")
print("-" * 24)

for i in range(1):
    lotto = [0, 0, 0, 0, 0]
    for x in range(5):
        num = 0
        while num in lotto:
            num = random.randint(1,45)
        lotto[x] = num
    print(lotto)
