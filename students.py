import csv
 
name = input("what's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames = ["name", "home"])
	writer.writerow({"home": home, "name": name})