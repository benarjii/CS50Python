def main():
	name = input("what's your name? ")
	print(hello(name))

def hello(to = "world"):
	return f"hello, david"

if __name__ == "__main__":
	main()