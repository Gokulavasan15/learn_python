for i in range (4):
    for j in range (4-i):
        print(j+1+i ,end="")
    print()
a,b="ABCD","PQR"
for i in range(4):
	print(a[:i+1]+b[i:])
    

