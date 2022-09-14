f=int(input("The biggest Side:\t"))
for i in range(f):
	for j in range(i):
		print(" ",end=" ")
	for j in range(i+1):
		print("*",end=" ")
	print()