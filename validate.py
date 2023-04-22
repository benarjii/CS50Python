import re

email = input("enter email: ").strip()

if re.search(r".+@.+\.com", email):
	print("valid")
else:
	print("Invalid")
