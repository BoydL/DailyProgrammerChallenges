a = int(input())
total = 0
for b in range(1, int(a**(0.5))+1):
	if(a%b == 0):
		c = a / b
		temp = b + c
		if(total == 0 or temp <= total):
			total = temp
print(total)
	