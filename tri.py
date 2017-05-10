print("삼각형 판별기 입니다.")

x = int(input("x값을 입력해주세요.(양수) : "))
y = int(input("y값을 입력해주세요.(y>=x) : "))
z = int(input("z값을 입력해주세요.(z>=y) : "))

if z>=x+y :
    print(3)
elif z**2 < x**2+y**2:
    print(0)
elif z**2 == x**2+y**2:
    print(1)
else :
    print(2)
