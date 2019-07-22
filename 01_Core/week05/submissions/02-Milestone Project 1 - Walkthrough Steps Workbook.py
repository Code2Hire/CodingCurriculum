#!/usr/bin/env python
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[3]:


from IPython.display import clear_output

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[4]:


test_board = [' ','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[5]:


def player_input(): 
    symbol = ''
    while symbol != 'X' and symbol != 'O':
        symbol = input('Player 1: Please choose X or O: ').upper()
    if symbol == 'X':
        return ('X','O')
    else:
        return ('O','X')


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[6]:


player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[7]:


def place_marker(board, marker, position):
    board[position] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[8]:


place_marker(test_board,'$',8)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[9]:


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark))


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[10]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[11]:


import random

def choose_first():
    rand = random.randint(0,1)
    if rand == 0:
        return 'Player 1 goes first'
    else:
        return 'Player 2 goes first'


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[12]:


def space_check(board, position):
    return (board[position] == ' ')


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[22]:


def full_board_check(board):
    for space in range(1,10):
        if space_check(board, space):
            return False
    return True


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[ ]:


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a space 1-9: '))
    return position


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[26]:


def replay():
    choice = input('Do you want to play again? Please enter Yes or No: ')
    if choice == 'Yes':
        return True
    else:
        return False
    


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    choose_first()
    symbol = player_input()
    display_board(board)
    game_on = True;
    while game_on:
        place_marker(board, symbol[0], player_choice(board))
        display_board(board)
        if win_check(board, symbol[0]):
            print('Player 1 wins')
            game_on = False
            break
        elif full_board_check(board):
            print('Tie')
            game_on = False
            break
            
        place_marker(board, symbol[1], player_choice(board))
        display_board(board)
        if win_check(board, symbol[1]):
            print('Player 2 wins')
            game_on = False
            break
        elif full_board_check(board):
            print('Tie')
            game_on = False
            break
    if not replay():
        break


# ## Good Job!

# In[ ]:




