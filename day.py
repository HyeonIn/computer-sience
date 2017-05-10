year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))





n = 0
i = 1
while (i < year) :
    if (i % 400==0) or (i % 4 == 0) and (not(i % 100 == 0)):
        n += 366
    else:
        n += 365
    i += 1

if month == 1:
    n+=0
else:
    A = [1,3,5,7,8,10,12]
    B = [4,6,9,11]
    for x in range(1, month):
        if x in A:
            n += 31
        elif x in B:
            n += 30
        elif month == 2:
            if (year % 400==0) or (year % 4 == 0) and (not(yaer % 100 == 0)):
                n += 29
            else :
                n += 28
n += day-1
if (year %400==0) or (year%4==0) and(not(year%100==0)) and(month>=3):
    n+=1
print(n)
if n % 7 == 0:
    print(year, "년", month, "월", day, "일은 월요일입니다.")
if n % 7 == 1:
    print(year, "년", month, "월", day, "일은 화요일입니다.")
if n % 7 == 2:
    print(year, "년", month, "월", day, "일은 수요일입니다.")
if n % 7 == 3:
    print(year, "년", month, "월", day, "일은 목요일입니다.")
if n % 7 == 4:
    print(year, "년", month, "월", day, "일은 금요일입니다.")
if n % 7 == 5:
    print(year, "년", month, "월", day, "일은 토요일입니다.")
if n % 7 == 6:
    print(year, "년", month, "월", day, "일은 일요일입니다.")
