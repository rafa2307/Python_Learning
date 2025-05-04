import os
import time
import random
import curses

BOARD_WIDTH = 20
BOARD_HEIGHT = 5
DIFFICULT = 8

def create_fruit(tail_posistions):
    try:
        fruit_posistion = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]

        while fruit_posistion in tail_posistions:
            fruit_posistion = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
        return fruit_posistion
    except Exception as e:
        return e

def create_board(fruit_posistion, head_position, tail_posistions):
    try:
        board = ''
        for i in range(BOARD_HEIGHT + 2):
            for j in range(BOARD_WIDTH + 2):
                if i == 0 or j == 0 or i == BOARD_HEIGHT + 1 or j == BOARD_WIDTH + 1:
                    board += '#'
                elif fruit_posistion == [j,i]:
                    board += 'F'
                elif head_position == [j,i]:
                    board += 'O'
                elif [j,i] in tail_posistions:
                    board += 'O'
                else:
                    board += ' '
            board += '\n'
        return board
    except Exception as e:
        return e
    
def draw(fruit_posistion, head_position, tail_posistions, score):
    try:
        tail_posistions.pop(0)
        tail_posistions.append(head_position.copy())
        board = create_board(fruit_posistion, head_position, tail_posistions)
        os.system('clear')
        print(board)
        print('Score: ', score)
    except Exception as e:
        return e

def get_pressed_key():
    try:
        stdcsr = curses.initscr()
        stdcsr.nodelay(True)
        converter = {119: 'w', 97: 'a', 115: 's', 100: 'd', 113: 'q'}

        key = stdcsr.getch()
        key = converter.get(key, '')
    finally:
        curses.flushinp()
        curses.endwin()
        return key

def change_side(head_position):
    try:
        if head_position[0] == 0:
            head_position[0] == BOARD_WIDTH
        elif head_position[0] == BOARD_WIDTH + 1:
            head_position[0] = 1
        if head_position[1] == 0:
            head_position[1] == BOARD_HEIGHT
        elif head_position[1] == BOARD_HEIGHT + 1:
            head_position[1] = 1
        return head_position
    except Exception as e:
        return e

def move(head_position, directions):
    try:
        key = get_pressed_key()

        if key == 'd' and directions['LEFT'] == False:
            head_position[0] += 1
            directions['UP'] = False
            directions['DOWN'] = False
            directions['RIGHT'] = True
        elif key == 'a' and directions['RIGHT'] == False:
            head_position[0] -= 1
            directions['UP'] = False
            directions['DOWN'] = False
            directions['LEFT'] = True
        elif key == 's' and directions['UP'] == False:
            head_position[1] += 1
            directions['RIGHT'] = False
            directions['LEFT'] = False
            directions['DOWN'] = True
        elif key == 'w' and directions['DOWN'] == False:
            head_position[1] -= 1
            directions['RIGHT'] = False
            directions['LEFT'] = False
            directions['UP'] = True
        else:
            if directions['RIGHT'] == True:
                head_position[0] += 1
            elif directions['LEFT'] == True:
                head_position[0] -= 1
            elif directions['DOWN'] == True:
                head_position[1] += 1
            elif directions['UP'] == True:
                head_position[1] -= 1
        head_position = change_side(head_position)
        return head_position
    except Exception as e:
        return e


def main():
    try:
        head_position = [BOARD_WIDTH // 2, BOARD_HEIGHT // 2]
        tail_posistions = [head_position.copy()]
        fruit_position = create_fruit(tail_posistions)
        directions = {'RIGHT': True, 'LEFT': False, 'UP': False, 'DOWN': False}
        score = 0
        while True:
            draw(fruit_position, head_position, tail_posistions, score)
            head_position = move(head_position, directions)

            if head_position in tail_posistions:
                break

            if head_position == fruit_position:
                tail_posistions.append(head_position.copy())
                fruit_position = create_fruit(tail_posistions)
                score += 9
            time.sleep(1 / DIFFICULT)

    except Exception as e:
        print(e)

main()