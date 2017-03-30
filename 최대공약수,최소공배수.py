#최소공배수
x=input()
y=input()
A=int(x)
B=int(y)
if A>B:
    MAX=A
    MIN=B
else:
    MIN=A
    MAX=B
while True:
    R=MAX%MIN
    MAX=MIN
    MIN=R
    if R==0:
        break
LCM=A*B/MAX #최소공약수(MAX)로 나누어 최소공배수(LOM)를 구하는 식(LCM은 최소공배수를 보관하는 변수)
print(LCM,MAX)
