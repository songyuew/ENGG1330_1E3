#########################
# Written by Liu Yihan
#########################

def generateAll(n, arr, i):

	if i == n:
		print(arr)
		return
	
	arr[i] = 0
	generateAll(n, arr, i + 1)

	arr[i] = 1
	generateAll(n, arr, i + 1)

def main():

	n = int(input())
	arr = [''] * n

	generateAll(n, arr, 0)

main()