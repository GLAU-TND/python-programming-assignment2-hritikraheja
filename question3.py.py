a = bin(int(input()))
b=''
d = []
for i in range(2,len(a)):
	b = b + a[i]
for j in range(0,len(b)):
	c = 1
	for k in range(j,len(b)-1):
		if b[k] is '1':
			if b[k] is b[k+1]:
				c = c+1
	d.append(c)
d.sort()
print(d[-1])
		
	
