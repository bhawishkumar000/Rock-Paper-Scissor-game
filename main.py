from random import randint
t=["rock","papel","tijeras"]
val=t[randint(0,2)]
player = False
while player ==False:
	xin=input("Enter:'rock','papel','tijeras'")
	if val==xin:
		print("It's a tie")
	elif xin=="rock" and  val =="papel":
		print("You won")
	elif xin=="papel" and val=="rock":
		print("You lost")
	elif xin=="rock" and val=="tijeras":
		print("you won")
	elif xin=="tijeras" and val=="rock":
		print("you lost")
	elif xin=="tijeras" and val=="papel":
		print("you won")
	elif xin=="papel" and val=="tijeras":
		print("you lost")
	else:
		print("Incorrect Spelling!")


