import random

money = 100

#Write your game of chance functions here

def flip_coin(bet, choice, money):
    if money > 0 and money >= bet:
        num = random.randint(1, 2)
        money -= bet
        if num == 1 and choice == 'Heads':
            print('You have betted ' + str(bet) + ' on this game!\nYou now have ' + str(money) +  ' cash.\nYou picked heads!\nThe outcome was heads!') 
            bet *= 2
            money += bet
            print('You have won the bet! You earned ' + str(bet) + '! \n\nYou currently have ' + str(money) + ' cash.')
            return money

        elif num == 1 and choice == 'Tails':
            print('You have betted ' + str(bet) + ' on this game!\nYou now have ' + str(money) +  ' cash.\nYou picked heads!\nThe outcome was tails!') 
            print('You lost the bet! You lost ' + str(bet) + '! \n\nYou currently have ' + str(money) + ' cash.')
            return money
        
        elif num == 2 and choice == 'Heads':
            print('You have betted ' + str(bet) + ' on this game!\nYou now have ' + str(money) +  ' cash.\nYou picked tails!\nThe outcome was heads!') 
            print('You lost the bet! You lost ' + str(bet) + '! \n\nYou currently have ' + str(money) + ' cash.')
            return money

        if num == 2 and choice == 'Tails':
            print('You have betted ' + str(bet) + ' on this game!\nYou now have ' + str(money) +  ' cash.\nYou picked tails!\nThe outcome was tails!') 
            bet *= 2
            money += bet
            print('You have won the bet! You earned ' + str(bet) + '! \n\nYou currently have ' + str(money) + ' cash.')
            return money
    else:
        print('You do not have enough cash for this bet!')
            


#Call your game of chance functions here
flip_coin(50, 'Heads', money)

