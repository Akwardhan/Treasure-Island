print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to the Treasure island")
print("Your Mission is to find the treasure")

direction=input("Where do you want to go: left or right\n").lower()

if direction == "left":
    print("Oops you got killed by the hunters.Game Over!!")
else:
    Choice=input("Since you took the right turn,you reached near a pond.Now do you want to : wait or swim \n").lower()
    

    if Choice=="wait":
      door= input("Excellent, you should wait and now you should take the most important decision; which color door should you pick: red or blue or yellow \n").lower()
     
      if door=="red":
        print("You got killed by hungry Lions! Game Over!!")
      elif door=="blue":
        print("OH NO! picked the wrong door,you got burnt by fire.Game Over!!")
      else:
        print("Hurray!! After taking all the correct decisions, you found the treasure. ")
    else:
        print("You died..Game Over")
       