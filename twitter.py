import re

url = input("url: ").strip()

matches = re.search(r'.*^(https?://)?(www\.)?twitter\.com/(.+)$', url, re.IGNORECASE)

if matches:
	print(f"username: {matches.group(3)}")