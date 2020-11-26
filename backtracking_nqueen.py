# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:39:33 2020

@author: Sansrit Paudel
"""
# time modeule to calculate the execution time for program


import time


print("Enter the number of queens")
N = int(input())

# starting point to record time

start = time.time()

# creating matrix to refer chessboard

# NxN matrix with all elements 0
board = [[0]*N for o in range(N)]
print(board)

print("\n")

# function to check if the queen got attack on row column or diagonal.


def is_attack(i, j):
    # checking if there is a queen in row or column
    # checking if there is any other queen in the row ‘i’ or column ‘j’.
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonals
    # Any cell (k,l) will be diagonal to the cell (i,j) if k+l is equal to i+j or k-l is equal to i-j.
    for k in range(0, N):
        for l in range(0, N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    return False

# function to check if the queen can be placed on board.


def N_queen(n):
    # if n is 0, solution found
   # print(n)
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            '''to check if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i, j))) and (board[i][j] != 1):  # checking if the cell is available to place a queen or not.
                board[i][j] = 1

                # recursion
                # wether we can put the next queen with this arrangment or not
                if N_queen(n-1) == True:
                    return True
                board[i][j] = 0

    return False


# execute the function to pass on placement of queen.
N_queen(N)

# printing the board with aquired solution.

for i in board:
    print(i)


end = time.time()

# calculate the total execution time.
total_time = (end - start)

print("\n")
print("total time of execution is ", total_time)
