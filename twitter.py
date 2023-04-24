url = input("url: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"username: {username}")