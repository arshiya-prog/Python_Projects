from logo import logo
import random

# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cont = 0

user_cards = []
computer_cards = []

def take_card(card_list):
    card = random.choice(cards)
    total = sum(card_list)

    if card == 11 and total+card > 21:
        card = 1

    card_list.append(card)

    return sum(card_list)

def display_cards(cards, score):
    print(f"Your cards: {cards}, current score = {score}")

user_score = take_card(user_cards)
user_score = take_card(user_cards)

computer_score = take_card(computer_cards)

while cont == 0:
        display_cards(user_cards, user_score)
        print(f"Computer's first card: {computer_cards[0]}")
        
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_another_card == "y":
            user_score = take_card(user_cards)

            if user_score > 21:
                print(f"Your score: {user_score} is over 21. You lose!")
                cont = 1
                break
            elif user_score == 21:
                print(f"Your score is 21. You win!")
                break
        else:
            cont = 1
            print(f"Your final hand: {user_cards}, final score = {user_score}")
            while computer_score < 17:
                computer_score = take_card(computer_cards)
            print(f"Computer's final hand: {computer_cards}, final score = {computer_score}")

            if computer_score > 21:
                print(f"You win!")
            elif user_score > computer_score:
                print(f"You win!")
            elif computer_score > user_score:
                print(f"You lose!")
            else:
                print("Draw.")