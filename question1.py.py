a = input().split()
a.sort()
b = [a[0]]
while len(b) != len(a):
	for i in a:
		if i not in b and b[-1][-1]==i[0]:
			b.append(i)
print(b)