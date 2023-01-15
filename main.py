from random import randint

randnum = randint(1,10)
userscore = 0
computerscore = 0

while True:
  print("Try to guess a number between 1 and 10")
  userguess = int(input())
  computerguess = randint(1,10)
  if userguess == randnum or computerguess == randnum:
    if userscore > computerscore:
      print("Congrats to the user")
      print("User score is: " + str(userscore))
      print("Computer score is: " + str(computerscore))
      break
    elif userscore == computerscore:
      print("Congrats to both of you")
      print("User score is: " + str(userscore))
      print("Computer score is: " + str(computerscore))
      break
    else:
      print("Congrats to the computer")
      print("User score is: " + str(userscore))
      print("Computer score is: " + str(computerscore))
      break
    
  else:
    if userguess > randnum:
      userguessdifferance = userguess - randnum
    else:
      userguessdifferance = randnum - userguess
      
    if computerguess > randnum:
      computerguessdifferance = computerguess - randnum
    else:
      computerguessdifferance = randnum - computerguess
      
    if computerguessdifferance < userguessdifferance:
      computerscore += 1
    elif computerguessdifferance == userguessdifferance:
      computerscore += 1
      userscore += 1
    else:
      userscore += 1
    