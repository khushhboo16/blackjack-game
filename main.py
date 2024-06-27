import art
from art import logo

def rand():
  import random
  card=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(card)
def calculate_score(card):
    if sum(card)==21 and len(card)==2:
      return 0
    if 11 in card and sum(card)>21:
      card.remove(11)
      card.append(1)
    return sum(card)
def another_card(user_card):
  user_card.append(rand())
  user_sum=calculate_score(user_card)
  return user_card
idk=True
while idk==True:
  
 option=input("DO YOU WANT TO PLAY A GAME OF BLACKJACK? TYPE Y FOR YES AND N FOR NO:  ")
 if option=="Y" or option=="y":
   print(logo)
   user_card=[]
   computer_card=[]
   for _ in range(2):
     user_card.append(rand())
     computer_card.append(rand())
     user_sum=calculate_score(user_card)
     computer_sum=calculate_score(computer_card)
   print(f"Your Cards are:{user_card} and Your Score is {user_sum} ")  
   print(f"Computers Cards are : {computer_card[0]}  ")
   if user_sum==0 or computer_sum==0 or user_sum>21:
     print("Game over")
   flag=True  
   while flag==True:
     option2=input("TYPE Y TO GET ANOTHER CARD OR N TO PASS: ")
     if option2=="Y":
       another_card(user_card)
       print(f"Your New Cards are: {user_card} and Score is: {calculate_score(user_card)}")
      
       print(f"Computer'card is {computer_card[0]}")
       if calculate_score(user_card)>21:
         print("WOMP WOMP YOU LOST!")
         flag=False
     else:
      
       print(f"Your final hands are: {user_card} and Score is : {calculate_score(user_card)}")
       print(f"Computer's final hands are: {computer_card} and score is:{calculate_score(computer_card)}")
       if calculate_score(user_card)> calculate_score(computer_card):
         print("WOHOO!YOU WIN")
         flag=False
         
       elif calculate_score(user_card)== calculate_score(computer_card):
         print("ITS A DRAW!!!") 
         flag= False
       else:
         print("WOMP WOMP YOU LOST!")
       flag= False  
 else:
   print("You Dont Want To Play! Bye-Bye")
   idk=False
      
      
    
  
    
    
    

   
    

  
    
    
  
 


    
  
  
  
    
    
    
  
  
  
  