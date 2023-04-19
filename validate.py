email = input("enter email: ").strip()

if "@" in email:
	print("Valid")
else:
	print("Invalid")