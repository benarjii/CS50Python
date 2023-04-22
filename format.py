import re

name = input("name: ")
if matches := re.search(r"^(.+), ?(.+)$", name):
	name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")