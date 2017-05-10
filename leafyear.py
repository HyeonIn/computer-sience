a=int(input("윤년을 판별하고 싶은 연도를 입력해주세요: "))

if (a%400 == 0):
    print("%d년은 윤년입니다." %a)
elif (a%100 == 0):
    print("%d년은 윤년이 아닙니다." %a)
elif (a%4 == 0):
    print("%d년은 윤년입니다." %a)
else :
    print("%d년은 윤년이 아닙니다." %a)
