print("최대공약수를 구합니다.")

a=int(input("양수 a를 입력해주세요.: "))
b=int(input("양수 b를 입력해주세요.: "))
if b > a:
    (a, b) = (b, a)
while a > b :
	x = a
	a = b
	b = x%a
	if b == 0:
		break

print(a)
