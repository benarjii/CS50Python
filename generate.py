import random
heads = 0
tails = 0
for i in range(1000000):
	coin = random.choice(["heads", "tails"])
	if coin == "heads":
		heads+=1
	else:
		tails+=1
print(f"number of heads = {heads}\nnumber of tails = {tails}")
