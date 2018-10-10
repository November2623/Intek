#!/usr/bin/env python3
import sys
import math

def position(board):
    permanent = []
    ephemeral = []
    list = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "A":
                player = [row, col]
            elif board[row][col] == "o":
                permanent.append([row, col])
            elif board[row][col] == "!":
                ephemeral.append([row, col])
            elif board[row][col] == "#":
                list.append([row, col])
    return player, permanent, ephemeral, list

def get_distance(board):
    list_dist = []
    player, permanent, ephemeral, list = position(board)
    pos_x = player[0]
    pos_y = player[1]

    for x,y in permanent:
        dist = math.sqrt(pow(pos_x - x, 2) + pow(pos_y - y, 2))
        list_dist.append(dist)
    return list_dist
def get_min_dict(board):
    list_dist = get_distance(board)
    for i in range(len(list_dist)):
        if list_dist[i] == min(list_dist):
            first_move = i
    return first_move

def move():
    move

if __name__ == '__main__':

    sys.stdin.readline()
    sys.stdin.readline()

    sys.stdout.write('I AM IA1\n\n')
    sys.stdout.flush()

    sys.stdin.readline()
    sys.stdin.readline()

    sys.stdout.write('OK\n\n')
    sys.stdout.flush()

    sys.stdin.readline()
    size = sys.stdin.readline()
    board = [size]
    pos_x = 0
    pos_y = 0
    while True:
        s = sys.stdin.readline()
        board.append(s)
        if s == size:
            break
    get_min_dict(board)
    while True:
        print("MOVE_DOWN")
