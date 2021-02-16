a='123456789'

print(a)

q=a[3]
w=a[4]
temp='`'
a=a.replace(q,temp)
a=a.replace(w, q)
a=a.replace(temp,w)
print(a)