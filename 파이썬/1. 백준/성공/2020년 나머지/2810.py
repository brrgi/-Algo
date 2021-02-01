n=int(input())
k=list(input())

hum=0
v=1
v+=k.count('S')+k.count('L')//2

if n <= v:
	print(n)
else:
	print(v)
