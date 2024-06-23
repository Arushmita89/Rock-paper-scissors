import random
rock = '''
R O C K
'''
paper= '''
P A P E R
'''
scissors= '''
S C I S S O R S
'''
inp=[rock,paper,scissors]
print("Enter 0 for rock, 1 for paper, 2 for scissors")
user=int(input())
if user>=3 or user<0:
    print("ERROR")
else:
    print(inp[user])
    computer=random.randint(0,2)
    print("computer choice")
    print(inp[computer])
    if user == computer:
        print("DRAW")
    elif user==2 and computer==0:
        print("YOU LOSE")
    elif user==0 and computer==2:
        print("YOU WIN")
    elif user>computer:
        print("YOU WIN")
    elif user<computer:
        print("YOU LOSE")
