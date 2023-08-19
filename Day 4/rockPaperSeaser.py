import random
import os


def clear_screen():
    os.system("cls")  # For Windows


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
---'    ____)____
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
winArt = ''' 
__      __.___ _______   
/  \    /  \   |\      \  
\   \/\/   /   |/   |   \ 
 \        /|   /    |    \"
  \__/\  / |___\____|__  /
       \/              \/
       '''
LossArt = '''
.__   ________   ________    _________
|  |  \_____  \  \_____  \  /   _____/
|  |   /   |   \  /   |   \ \_____  \ 
|  |__/    |    \/    |    \/        \"
|____/\_______  /\_______  /_______  /
              \/         \/        \/ 
              '''
DrawArt = '''
________ __________    _____  __      __ 
\______ \\______   \  /  _  \/  \    /  \"
 |    |  \|       _/ /  /_\  \   \/\/   /
 |    `   \    |   \/    |    \        / 
/_______  /____|_  /\____|__  /\__/\  /  
        \/       \/         \/      \/   
'''
win = 0  # Initialize win count
loss = 0  # Initialize loss count
rockPaperSeaser = [rock, paper, scissors]
while True:
    choice = ((int(input(
        '''What do you choose? 
        Type 
        0 for Rock,
        1 for Paper,
        2 for Scissors: \t'''))) % 3)

    computerChoice = random.randint(0, 2)

    print(f"Your choice is:\n{rockPaperSeaser[choice]}")
    print(f"Computer choice is:\n{rockPaperSeaser[computerChoice]}")

    if choice == computerChoice:
        print(DrawArt)
    elif (choice == 1 and computerChoice == 0) or (choice == 2 and computerChoice == 1) or (choice == 0 and computerChoice == 2):
        print(winArt)
        win += 1  # Increment win count
    else:
        print(LossArt)
        loss += 1  # Increment loss count

    play_again = input("Do you want to play again? (yes/no): ")
    clear_screen()
    if play_again.lower() != "yes":
        print(f"You won {win} times and lost {loss} times.")
        break
