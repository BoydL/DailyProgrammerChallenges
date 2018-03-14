import sys
def flip_pancake(x, f):
	for i in range((f+1)//2):
		x[i], x[f-i] = x[f-i], x[i]
	print(x)
	return(x)

def sort_pancake(x, n):
	moves = 0
	for i in range(n, 1, -1):
		xmax, xindex = x[0], 0
		for j in range(i):
			if(x[j] > xmax):
				xmax, xindex = x[j], j
		x = flip_pancake(x, xindex)
		moves+=1
		x = flip_pancake(x, i-1)
		moves+=1
	print(x)
	return(moves)

def main():
	filename = sys.argv[1]
	f = open(filename)
	n = int(f.readline())
	x = [int(i) for i in f.readline().split(" ")]
	print(x)
	moves = sort_pancake(x,n)
	print(moves)

if __name__ == "__main__":
	main()