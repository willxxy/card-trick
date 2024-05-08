import numpy as np

def find_index(participant_chosen_number):
    first_num = ((participant_chosen_number -1) // 9) ## if not based on 0 ,+ 1
    second_num = (participant_chosen_number - (first_num * 9) -1) // 3
    third_num = participant_chosen_number  -(first_num * 9) - (second_num * 3) -1
    order_of_collection = list((np.array([first_num, second_num, third_num]) -1) * -1 + 1)
    order_of_collection = order_of_collection[::-1]
    return order_of_collection


print('Welcome to the card trick!')
print()

participant_chosen_number = int(input('Please choose a number between 1 and 27: '))
assert 1 <= participant_chosen_number <= 27, 'The number must be between 1 and 27.'

print('You chose the number: ', participant_chosen_number)
print()

cards = np.arange(1, 28)
np.random.shuffle(cards)
card_matrix = cards.reshape(9, 3)
order_of_collection = find_index(participant_chosen_number)

print('Here are the cards: ')
print(card_matrix)
print()

print('Please choose a card and remember the number on it.') 
print(f'Remember the number of the card is different from the initial number you chose, which was {participant_chosen_number}.')
print()

print('Okay, after you have chosen the card, please identify which column your card is in.')
print('Please type the column number (0, 1, or 2) below, where 0 indicates the left column, 1 indicates the middle column and 2 inidicates the right column.')
print('We will do this operation three times.')
print()
for i, j in enumerate(order_of_collection):
    print(f'Round {i+1}')
    print(card_matrix)
    column_number = int(input('Please choose the column number: '))
    assert 0 <= column_number <= 2, 'The column number must be between 0 and 2.'

    print('Now I will collect the cards.')

    first_column = card_matrix[:, 0][::-1]
    second_column = card_matrix[:, 1][::-1]
    third_column = card_matrix[:, 2][::-1]
    
    
    chosen_column = card_matrix[:, column_number][::-1]
    
    if j == 0:
        if column_number == 0:
            card_matrix = np.concatenate((chosen_column, second_column, third_column))
        elif column_number == 1:
            card_matrix = np.concatenate((chosen_column, first_column, third_column))
        else:
            card_matrix = np.concatenate((chosen_column, first_column, second_column))
    elif j == 1:
        if column_number == 0:
            card_matrix = np.concatenate((second_column, chosen_column, third_column))
        elif column_number == 1:
            card_matrix = np.concatenate((first_column, chosen_column, third_column))
        else:
            card_matrix = np.concatenate((first_column, chosen_column, second_column))
    else:
        if column_number == 0:
            card_matrix = np.concatenate((second_column, third_column, chosen_column))
        elif column_number == 1:
            card_matrix = np.concatenate((first_column, third_column, chosen_column))
        else:
            card_matrix = np.concatenate((first_column, second_column, chosen_column))
    

    card_matrix = card_matrix[::-1].reshape(9,3)
    print('--------------------------------------------')
    
chosen_card = card_matrix.flatten()[participant_chosen_number-1]

print(f"You're chosen card is the following: {chosen_card}")

    
    


