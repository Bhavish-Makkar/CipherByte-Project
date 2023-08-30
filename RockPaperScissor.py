import random

print ("Welcome To Rock Paper Scissor Game")
user_score=0;
computer_score=0;
ties=0;
name=input("enter your name here : ")
print("""    Rules For The Game
      1. Paper vs Rock --->Paper
      2. Paper vs Scissor --->Scissor
      3. Scissor vs Rock --->Rock
      """)
print()
print(""" Choices Are : 
1.Rock
2.Paper
3.Scissor""")
while(True):
 user=int(input("enter your choice from 1-3 : "))
 print()
 while user>3 or user<1:
    user=int(input("enter valid input "))
    
 if user==1:
    user_choice="Rock";
 elif user==2:
    user_choice="Paper"
 else:
    user_choice="Scissor"
 print("The user choice is ",user_choice)
 print("Now it is Computer Turn ")
 computer= random.randint(1,3)

 if computer==1:
    computer_choice="Rock";
 elif computer==2:
    computer_choice="Paper"
 else:
    computer_choice="Scissor"
    
    
 print("the computer's choice is ",computer_choice)

 if ((user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Rock" and computer_choice=="Paper")):
    print("Paper Wins")
    result="Paper"
 elif ((user_choice=="Rock" and computer_choice=="Scissor") or (user_choice=="Scissor" and computer_choice=="Rock")):
    print("Rock Wins")
    result="Rock"
 elif(user_choice==computer_choice):
    print("Its A Tie")
    Result="Tie"
 else:
    print("Scissor Wins")
    result="Scissor"
 if result==user_choice :
    print("User Wins")
    user_score=user_score+1;
 elif user_choice==computer_choice :
    ties=ties+1;
 else:
    print("Computer Wins")
    computer_score=computer_score+1;
    
    
 print("Scores Are")
 print(name,"score is ",user_score)
 print("computer score is ",computer_score)
 print("Ties are ",ties)
 repeat=input("Do You Want To Play Again ? ")
 if(repeat=="No"):
    break;
print("Game Over Thanks For Playing ")
