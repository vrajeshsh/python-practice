'''To generate all Heronian Triangles within a given limit'''

print("To generate all Heronian Triangles within a given limit:")
n = int(input("Enter the limit: "))

hero,area="",0

for i in range(1,n):
	for j in range(1,n):
		for k in range(1,n):
			s = (i+j+k)/2
			if i+j>k and j+k>i and i+k>j:
				area = (s*(s-i)*(s-j)*(s-k))**0.5
				if area - int(area)==0:
					hero+=str(i)+"\t\t"+str(j)+"\t\t"+str(k)+"\t\t"+str(area)+"\n"

print("\nSIDE1\tSIDE2\tSIDE3\tAREA\n",hero)
