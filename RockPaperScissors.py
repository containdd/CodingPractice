#note to self, time.sleep function will not work when import time is removed duh
#im still learning how 2 code pls be patient im retarded i swear
#code last updated 16/03/2023
#containd is a legend frfr
import turtle 
import time
import random
print("Lets Play Rock Paper Scissors!")
time.sleep(1)
print(" ")
print("Loading")
time.sleep(0.5)
print("Remember to Pick Between Rock, Paper Or Scissors!")
#player chooses move
player=input("Enter Your Move: ")
time.sleep(0.1)
#start of while loop
while player!="Paper" and player!="Rock" and player!="Scissors":
     player=input("Please Enter Either Rock, Paper or Scissors: ")
#end of while loop
if player=="Rock":
     time.sleep(1.5)
     print("You Picked Rock")
elif player=="Paper":
     time.sleep(1.5)
     print("You Picked Paper")
elif player=="Scissors":
     time.sleep(1.5)
     print ("You Picked Scissors")
cpu=random.randint(1,3)
#computer chooses move
if cpu==1:
     print("Computer Picked Rock")
     time.sleep(1.5)
elif cpu==2:
     print("Computer Picked Paper")
     time.sleep(1.5)
else:
     print("Computer Picked Scissors")
     time.sleep(1.5)
#player chooses rock varients
if cpu==1 and player=="Rock":
     time.sleep(1.5)
     print("Draw!")
elif cpu==2 and player=="Rock":
     time.sleep(1.5)
     print("Computer Wins!")
elif cpu==3 and player=="Rock":
     time.sleep(1.5)
     print("Player Wins!")
#player chooses paper varients
if cpu==1 and player=="Paper":
     time.sleep(1.5)
     print("Player Wins!")
elif cpu==2 and player=="Paper":
     time.sleep(1.5)
     print("Draw!")
elif cpu==3 and player=="Paper":
     time.sleep(1.5)
     print("Computer Wins!")
#player chooses scissor varients
if cpu==1 and player=="Scissors":
     time.sleep(1.5)
     print("Computer Wins!")
elif cpu==2 and player=="Scissors":
     time.sleep(1.5)
     print("Player Wins!")
elif cpu==3 and player=="Scissors":
     time.sleep(1.5)
     print("Draw!")
#2nd Game of RPS
     time.sleep(3)
print("Lets Play Again One more time!")
print(" ")
print(" ")
player=input("Enter Your Move: ")
#start of while loop
while player!="Paper" and player!="Rock" and player!="Scissors":
     player=input("Please Enter Either Rock, Paper or Scissors: ")
#end of while loop
if player=="Rock":
     time.sleep(1.5)
     print("You Picked Rock")
elif player=="Paper":
     time.sleep(1.5)
     print("You Picked Paper")
elif player=="Scissors":
     time.sleep(1.5)
     print ("You Picked Scissors")
cpu=random.randint(1,3)
#computer chooses move
if cpu==1:
     time.sleep(1.5)
     print("Computer Picked Rock")
elif cpu==2:
     time.sleep(1.5)
     print("Computer Picked Paper")
else:
     time.sleep(1.5)
     print("Computer Picked Scissors")
#player chooses rock varients
if cpu==1 and player=="Rock":
     time.sleep(1.5)
     print("Draw!")
elif cpu==2 and player=="Rock":
     time.sleep(1.5)
     print("Computer Wins!")
elif cpu==3 and player=="Rock":
     time.sleep(1.5)
     print("Player Wins!")
#player chooses paper varients
if cpu==1 and player=="Paper":
     time.sleep(1.5)
     print("Player Wins!")
elif cpu==2 and player=="Paper":
     time.sleep(1.5)
     print("Draw!")
elif cpu==3 and player=="Paper":
     time.sleep(1.5)
     print("Computer Wins!")
#player chooses scissor varients
if cpu==1 and player=="Scissors":
     time.sleep(1.5)
     print("Computer Wins!")
elif cpu==2 and player=="Scissors":
     time.sleep(1.5)
     print("Player Wins!")
elif cpu==3 and player=="Scissors":
     time.sleep(1.5)
     print("Draw!")
print("Phew Im Tired, Wish I could Play more!")
time.sleep(1)
print("Thanks For Playing!")
#end code


     
     
     
