import re

email = input("enter email: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
	print("valid")
else:
	print("Invalid")
