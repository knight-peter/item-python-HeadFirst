print("welcome!")
g=input("guess the number:")
guess=int(g)
if guess==5:
	print("You win!")
else:
	if guess>5:
		print("太高了!")
	else:
		print("太低了!")
print("游戏结束！")
