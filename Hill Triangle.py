n=int(input("Triangle leg:\t"))
for i in range(n):
	for j in range(i,n):
		print(" ",end=" ")
	for j in range(i+1):
		print("*",end=" ")
	for j in range(i):
		print("*",end=" ")
	print()