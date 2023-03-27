def main():
	print_grid(3)

def print_grid(n):
	for i in range(n):
		for j in range(n):
			print("#",end="")
		print()
		

main()