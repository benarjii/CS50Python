import re

url = input("url: ").strip()

username = re.sub(r".*^(https?://)?(www\.)?twitter\.com/", "",url)
print(f"username: {username}")