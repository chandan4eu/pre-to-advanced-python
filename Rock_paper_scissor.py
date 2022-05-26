import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


computerr=random.randint(0,2)
map=[rock,paper,scissors]
print(map[0])
print(map[1])
print(map[2])
print("computer chose "+ map[computerr])
user=input("Type '0' for rock,'1' for scissor,'2' for paper\n")

if(int(user)>2):
    print("Invalid click")
else:

    print("computer choose"+ map[computerr])

    print("You choose"+ map[int(user)])

    computer=str(computerr)

    if computer=='0':


        if user=='0':

            print("DRAW")
        elif user=='1':
            print("YOU WON")
        else:
            print("You LOST,BETTER LUCK NEXT TIME!!!")
    
    elif computer =='1':
        if user=='1':
            print("DRAW")
        elif user=='0':
            print("You LOST,BETTER LUCK NEXT TIME!!!")
        else:
            print("YOU WON")
    else:
        if user=='2':
            print("DRAW")
        elif user=='0':
            print("YOU WON")
        else:
            print("You LOST,BETTER LUCK NEXT TIME!!!")
