# Ideas by Graham
# Coded by Ben

import os
os.system("cls")

# Boot System
# Fast_Boot = False
print("Booting...")
# from tqdm import tqdm
import time

# for i in tqdm(range(100)):
#   time.sleep(0.01)


# Def's
WorkTime = 3
def wait(x):
  if WorkTime <= 0.1:
    quit("TO MANY EMPLOYS!")
  import time
  time.sleep(x)


# def boot():
#   from tqdm import tqdm
#   import time

#   for i in tqdm(range(100)):
#       time.sleep(0.1)
# boot()

def sysquit(x,y=None):
  if y == None:
    exit(x)
  print("\033[0;31m", y, "\033[0;37m")
  exit(x)
  # codes
# Red = "\033[0;31m"
# Green = "\033[0;32m"
# Orange = "\033[0;33m"
# Blue = "\033[0;34m"
# Purple = "\033[0;35m"
# Cyan = "\033[0;36m"
# White = "\033[0;37m"
# black = "\033[0;30m"

def say(x):
  print(x)


def introcuction():
  say(
    "This city is a code based life! You enter stuff in the terimnal ' >>> '.")
  say("To check your money you type 'money'")
  say(
    "Type 'work' to get a default of $100. Working will drain your happness by 10."
  )
  say("Type 'place' to place a $50 building!")
  say("Type 'place.bank' to place a $1500 building. Gives you a 10x boost!")
  say("Type happness to see your happness!")
  say("To speed up working time add Employs by doing 'place.employ'. Each Employ will speed up work time by 0.1 seconds. Default work time is 3 seconds. Dont add to many tho!")
  say("")
  say("To see this mesaage type 'help'")


# say("welcome to 69ville")

# Variables
Coins = 1000
if Coins != 1000:
  quit("CHEATER")
Coinsx2 = 1
happness = 100

Employs = 0
Employs_Bounse = 0

print("Welcome to G93!")
print("Pick one!\n1. Start\n2. Patch Notes")
startmenupick = input(">>> ")
if startmenupick == "1":
  print("SPEED MODE ON!")
  # print("Game Starting", end="\r")
  # wait(1)
  # print("Game Starting.", end="\r")
  # wait(1)
  # print("Game Starting..", end="\r")
  # wait(1)
  # print("Game Starting...", end="\r")
  # wait(1)
  # print("Game Loaded!               ")
  Citynameinput = input("City Name: ")
  print("Your City Name Is: " + Citynameinput)
  yourname = input("Please Enter The Mayor's Name: ")
  print("Your Maiors Name is: " + yourname)
  introcuction()
  # Start Game
  buildings = 0
  while True:
    maingame1 = input(">>> ")
    if maingame1 == "money":
      print("You have ", Coins, " Coins!")
    elif maingame1 == "help":
      introcuction()
    elif maingame1 == "place.house":
      print("Placeing House")
      if Coins <= 2000:
        print("Not Enough Coins!")
      else:
        print("Done!")
        buildings = buildings + 1
        Coins = Coins - 2000
        happness = 200
    elif maingame1 == "place":
      buildings = buildings + 1
      Coins = Coins - 50
      print("Placed Building!")
    elif maingame1 == "place.bank":
      print("Placing Bank...")
      wait(2)
      if Coins <= 1500:
        print("Not Enough Coins!")
    elif maingame1 == "place.vault":
      print("Placing Vault...")
      wait(2)
      if Coins <= 3000:
        print("Not Enough Coins!")
      else:
        print("Done!")
        buildings = buildings + 1
        Coins = Coins - 3000
        Coinsx2 = 100
    elif maingame1 == "place.employ":
      if Coins <= 200:
        print("Not Enough Coins!")
      else:
        print("Placed Employ!")
        Coins = Coins - 200
        Employs = Employs + 1
        WorkTime = WorkTime - 0.1
        Employs_Bounse = Employs_Bounse + 0.1
        if WorkTime > 3:
          print("Max Value!")
          WorkTime = 0.1
    elif maingame1 == "employ-see":
      print("Employs: ", Employs)
    elif maingame1 == "place-see":
      print("You have ", buildings, "buildings")
    elif maingame1 == "work":
      say("Working...")
      wait(WorkTime)
      happness = happness - 10
      say("Done! + Coins!")
      Coins = Coins + 100 * Coinsx2
    elif maingame1 == "debug.coins":
      coinset = int(input("Enter Coin Ammount: "))
      Coins = coinset
    elif maingame1 == "debug.employ.bounce":
      print(Employs_Bounse, "Work Time: ", WorkTime)
    elif maingame1 == "relax":
      print("Relaxing...")
      wait(5)
      happness = happness + 30
    elif maingame1 == "happy":
      print(happness, "/100")
    elif maingame1 == "debug.workTime":
      askworktime = int(input("New Work Time: "))
      WorkTime = askworktime
elif startmenupick == "2":
  print("Ver Alapha 1.34.2")
elif startmenupick == "3":
  print("To load game please enter your data")
  askcoin = int(input("Coins: "))
  print("NOT DONE YET!")

else:
  print("Incorret Choice!")

# Checks

while True:
  if happness <= 0:
    print("You are very sad! $1000 Paied")
    Coins = Coins - 1000
    happness = 100
