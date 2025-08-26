# Create Rock, Paper, Scissors project with counting
import random
computer = random.randint(1, 3)
#print(computer)
import json
def com_turn(num):
    if num == 1: return "R"
    elif num == 2: return "P"
    else: return "S"

get_com = com_turn(computer)
#print(get_com) 

prompt = "Rock(R), Paper(P), Scissor(S)"
def play():
    get_user_any = input("Player's turn        :" + prompt)
    get_user = get_user_any.upper()
    print("Computer's turn      :" + prompt + get_com)
    print(f"Computer vs. Player  : {get_com} vs. {get_user}")
    if get_user == get_com:
        print("Draw")
        
print("Rock Paper Scissors Fame\n")
count_num = int(input("How many times you want to play: "))

for count in range(1, count_num+1):
    play()
print("Exit. Thanks for playing")
