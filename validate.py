import re

email = input("enter email: ").strip()

if re.search(r"^\w+@\w+\.(com|gov|edu|org)$", email):
	print("valid")
else:
	print("Invalid")
