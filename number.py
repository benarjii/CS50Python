def main():
	x = get_info("what's x? ")
	print(f"x is {x}")
def get_info(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			pass
main()