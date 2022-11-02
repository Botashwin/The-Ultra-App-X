import random
import sys

def main():
    print("\n-----------------------------------------------------------------")
    print("          (ツ)   Rock! Paper! And Scissors! Shoot!!   (ツ)         ")
    print("-------------------------------------------------------------------")
    while True:
        options = ['Rock', 'Paper', 'Scissor']
        username = input("Enter your name : - ")
        name = username.title()
        while True:
            rounds = input("Enter The Number Of Rounds: - ")
            if rounds.isdigit():
                num = int(rounds)
                CompScore = 0
                PlayerScore = 0
                NumberOfRounds: int = 1
                gameOn = True
                print(f"\nWelcome ( {name} ) !! Enjoy The Game!! Hope You Win!! ⧹(⦁ᴗ⦁)⧸")
                while NumberOfRounds < num:
                    while True:
                        print("------------------------------------------------------")
                        print(f"Round No: - {NumberOfRounds}")
                        user_action = input("\nEnter Rock(r)/ Paper(p)/ Scissor(s) : - ").title()
                        if user_action == "R" or user_action == "Rock":
                            ua = 'Rock'
                            NumberOfRounds += 1
                        elif user_action == "P" or user_action == "Paper":
                            ua = 'Paper'
                            NumberOfRounds += 1
                        elif user_action == "S" or user_action == "Scissor" or user_action == "Scissors":
                            ua = 'Scissor'
                            NumberOfRounds += 1
                        else:
                            print('Invalid Option...Please Try Again (▱˘︹˘▱)')
                            continue
                        computer_action = random.choice(options)
                        print('\nYou Chose (',ua,') , And The Computer Chose (',computer_action,')')
                        if ua == computer_action:
                            print(f"Both Players Selected {ua}.So, It's A Tie! -_-")
                        elif ua == "Rock" and computer_action == "Scissor":
                            print("Rock Crushes Scissor... U Win (ツ)")
                            PlayerScore += 1
                        elif ua == "Scissor" and computer_action == "Rock":
                            print("Rock Smashes Scissor... U Lose (╥﹏╥)")
                            CompScore += 1
                        elif ua == "Paper" and computer_action == "Rock":
                            print("Paper Covers Rock... U Win (ツ)")
                            PlayerScore += 1
                        elif ua == 'Rock' and computer_action == 'Paper':
                            print('Paper Covers Rock... U Lose (╥﹏╥)')
                            CompScore += 1
                        elif ua == 'Scissor' and computer_action == "Paper":
                            print("Scissor Cuts Paper... U Win (ツ)")
                            PlayerScore += 1
                        elif ua == 'Paper' and computer_action == "Scissor":
                            print("Scissor Cuts Paper... U Lose (╥﹏╥)")
                            CompScore += 1
                        if NumberOfRounds == num+1:
                            gameOn = False
                            break
                if PlayerScore == CompScore:
                    print("\nDraw Match!! -_-")
                elif PlayerScore > CompScore:
                    print(f"\nCongrats {name}, You won the game !! ⧹(⦁ᴗ⦁)⧸")
                else:
                    print(f"\nOops Computer won the game!! Better luck next time {name}! (▱˘︹˘▱)")
                play_again = input("\nPlay again? (y/n): ")
                if play_again.lower() != "y":
                    print("\nHope You Enjoyed The Game.. See You Soon (ツ)")
                    sys.exit()
            else:
                print("Invalid Option.. Please Try Again (▱˘︹˘▱)")
                continue