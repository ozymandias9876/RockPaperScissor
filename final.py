from drawings import *
from random import randint
import os
while(1):
	user_input=input("Enter your weapon of choice: rock, paper or scissor: ")

	
	val=0;
	if(user_input=="rock"):
		val=0
	elif(user_input=="paper"):
		val=1
	elif(user_input=="scissor"):
		val=2
	else:
		print("Wrong Input")
		continue
	num=randint(0,2)
	if(num):
		print("You Chose: ")
		print(drawing[val])
		print("Computer Chose: ")
		print(drawing[num])

		if(num==0 and val==2):
			print("Computer Won")
		elif(num==0 and val==1):
			print("You Won")
		if(num==1 and val==0):
			print("Computer Won")
		elif(num==1 and val==2):
			print("You Won")
		if(num==2 and val==0):
			print("You Won")
		elif(num==2 and val==1):
			print("Computer Won")
		if(num==val):
			print("It was a draw you both lost")
		key=input(" press c to continue, or q to quit: ")
		if(key=="q"):
			break
		if(key=="c"):
			os.system('clear')


