'''
In this lesson i learned about the replace function

The time for this is O(n^3)
'''

from os import system
board = '''
1 # 2 # 3
#########
4 # 5 # 6
#########
7 # 8 # 9
'''

player_x = [] # this list holds all the values entered by X player
player_o = [] # this list holds all the values entered by O player
player_x_won = False
player_o_won = False
winning_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

# ouuter loop iterates 9 times since there are only 9 turns in a tic-tac-toe game
for i in range(9):
    system('cls||clear')
    print(board)
    if i % 2 == 0:
        player_x.append(input("Player X select a number: "))
        board = board.replace(player_x[-1], 'X') # replace will replace an old substring with a new substring. In this case each time we enter a number. the replace method will look for the number in the board string and the replace it with either an X.
        for combination in winning_combinations: # we iterate through winning comibinations 8 times. combination holds the list that we will compare to the player_x list
            count = 0
            for j in range(3):
                if str(combination[j]) in player_x: # this checks if the value in combination at index j is in the player_x list.
                    count += 1
            if count == 3: # if this is true we break out of the nested inner for loop
                player_x_won = True
                system('cls||clear')
                print(board)
                print('Player X won!')
                break
        if player_x_won: # if this is true, we break out of the inner for loop
            break
    else:
        player_o.append(input("Player O select a number: "))
        board = board.replace(player_o[-1], 'O') # replace will replace an old substring with a new substring. In this case each time we enter a number. the replace method will look for the number in the board string and the replace it with either an O.
        for combination in winning_combinations:
            count = 0
            for j in range(3):
                if str(combination[j]) in player_o:
                    count += 1
            if count == 3:
                player_o_won = True
                system('cls||clear')
                print(board)
                print('Player O won!')
                break
        if player_o_won:
            break
else:
    system('cls||clear')
    print(board)
    print("It's a draw")