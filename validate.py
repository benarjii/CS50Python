import re

email = input("enter email: ").strip()

if re.search("@", email):
	print("valid")
else:
	print("Invalid")
