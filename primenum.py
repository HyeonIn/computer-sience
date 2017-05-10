print("소수 나열기")
p = int(input("양수를 입력해 주세요 : "))
if p == 1:
    print("1은 소수가 아닙니다.")
List = set([])
for i in range(2, p+1):
    if i == 2:
        List.add(2)
    if i > 2:
        for x in range(2, i):
            if i % x == 0:
                break
            elif x==i-1:
                List.add(i)
if p>=2:
    print(sorted(List))
