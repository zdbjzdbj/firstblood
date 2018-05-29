print("hello world")
sum = 0
for i in range(1,101):
	sum += i
	
print(sum)

for row in range(1,10):
	for col in range(1，row+1):
		print(row,"*",col,"=",row*col,end="\t")
	print()
#
