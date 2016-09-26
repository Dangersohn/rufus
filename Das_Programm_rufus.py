#Cleart das Terminal sollte unter Windows und Unix gehen
import os
import sys,time,random

def intro():
	print('           _                _                             _             _____   __            ')
	print('     /\   | |              | |                           | |           |  __ \ / _|           ')
	print('    /  \  | |__   ___ _ __ | |_ ___ _   _  ___ _ __    __| | ___  ___  | |__) | |_ _   _ ___  ')
	print('   / /\ \ |  _ \ / _ \  _ \| __/ _ \ | | |/ _ \  __|  / _` |/ _ \/ __| |  _  /|  _| | | / __| ')
	print('  / ____ \| |_) |  __/ | | | ||  __/ |_| |  __/ |    | (_| |  __/\__ \ | | \ \| | | |_| \__ \ ')
	print(' /_/    \_\_.__/ \___|_| |_|\__\___|\__ _|\___|_|     \__,_|\___||___/ |_|  \_\_|  \__,_|___/ ')
	print("\n\n\n")

def ende():
	print("___________           .___     ")
	print("\_   _____/ ____    __| _/____ ")
	print("|    __)_ /    \  / __ |/ __ \ ")
	print("|        \   |  \/ /_/ \  ___/ ")
	print("/_______  /___|  /\____ |\___  ")
	print("        \/     \/      \/    \/") 
		
	
# öffnet das Richtige file
def output(x):
	file = open(x, "r")
	cont = file.read()
	print_slow(cont)
	file.close()
	return
#Schreibt den Text langsam auf den screen
def print_slow(str):
	print("\n")
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.08)
	print("\n")
# gibt die Auswahl aus und  den Input zurück
def choices(x,y):
	print("1) " + x)
	print("2) " + y)
	inpu = int(input("\n=> "))
	return inpu

def error():
	print("ERROR WRONG ANSWER!!!")
#Kleines Menu
def menu():
	intro()
	print("\t---------------------------------------------------------")
	print("\t|\tHallo kleiner schatz,\t\t\t\t|")
	print("\t|\tIch hoffe du hast Spaß beim spielen.\t\t|")
	print("\t|\twenn du bereit bist bist einfach y drücken\t|")
	print("\t---------------------------------------------------------")
	m = input()
	if m == "y":
		print("\tGleich gehts los!!")
		for i in range(5):
			print("\t" + str(i))
			time.sleep(1)
	else:
		print("okay dann nicht :C")
		ende()
		sys.exit()

#----------ab hier kommt alles was mit dem Kampfsystem zutun hat--------

# legt die Einheiten an
class unit:
	def __init__(self,name, hp):
		self.name = name
		self.hp = hp

#Fähigkeiten
	def dmg_strong(self):
		x = random.randrange(4,20)
		self.hp = self.hp - x
		print("\n" + self.name + " hat " + str(x) + " Schaden bekommen!!")

	def dmg_normal(self):
		x = random.randrange(8,10)
		self.hp = self.hp - x
		print("\n" + self.name + " hat " + str(x) + " Schaden bekommen!!")

	def heal(self):
		x = random.randrange(8,15)
		self.hp = self.hp + x
		print("\n" + self.name + " hat sich um  " + str(x) + " geheilt!") 


def fight(x,y):
	while x.hp >= 0 and y.hp >=0:
	 	print("\n" + str(x.name) + " hat noch " + str(x.hp) + " Leben")
	 	print(str(y.name) + " hat noch " + str(y.hp) + " Leben\n")
	 	fehler = 1
	 	while fehler == 1:
	 		userin = input("1)kratzen\n2)Nagen\n3)Super Heilsalbe\n\nWas soll rufus machen? ")
	 		fehler = 100
	 		if userin == "1":
	 			y.dmg_normal()
	 		elif userin == "2":
	 			y.dmg_strong()
	 		elif userin == "3":
	 			x.heal()
	 		else:
	 			print("Rufus ist verwirrt")
	 		if y.hp >=0:
	 			npcin = random.randrange(1,4)
	 		if npcin == 1:
	 			x.dmg_normal()
	 		elif npcin == 2:
	 			x.dmg_strong()
	 		elif npcin == 3:
	 			y.heal()
	 		else:
	 			print("Falsche eingabe")
	if x.hp >= 0:
		print("\n" + str(y.name) + " wird ohnmächtig!")
		print (str(x.name) + " hat den Kampf gewonnen!!")
	else:
		print ("\n" + str(y.name) + " hat den Kampf gewonnen!!")
		sys.exit()


#############Einheiten###############
rufus = unit("Rufus",100)
schnappschildkröte = unit("Schnappschildkröte",100)


#-----------Eigentlches Programm--------------------------
os.system('cls' if os.name == 'nt' else 'clear')
menu()
os.system('cls' if os.name == 'nt' else 'clear')
# printet das intro
output("intro.txt")
choice = choices("Kanalisation", "Gleitdrache")

if choice == 1: #Choice 1
	output("choice1.txt")
	choice = choices("Beeilen","Prüfen")
	if choice == 1:
		output("choice1.1.txt")
	elif choice == 2:
		output("choice1.2.txt")
	else:
		error()
elif choice == 2: #Choice 2
	output("choice2.txt")
	choice = choices("Springen","Hinablassen")
	if choice == 1:
		output("choice2.1.txt")
	elif choice == 2:
		output("choice2.2.txt")
	else:
		error()
else:
	error()

# Im Gebäude angekommen
output("sequens.txt")
choice = choices("Renne","Seilschleuder")

if choice == 1:
	output("choice3.1.txt")
elif choice == 2:
	output("choice3.2.txt")
else:
	error()

fight(rufus,schnappschildkröte)

#nach dem Kampf
output("nachdemkampf.txt")
choice = choices("Schacht","Gang")

if choice == 1:
	output("choice4.1.txt")
elif choice == 2:
	output("choice4.2.txt")
else:
	error()


output("herz.txt")
ende()	
