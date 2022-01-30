'''this is a sample board'''

board = [ [1,2,3]
         ,[4,5,6]
         ,[7,8,9] ]


'''this function takes board as an arguement and prints a tik-tak-toe look alike board'''
def display_board(board):
    z = 0                       # 'z' is the condition to break the loops at certain position like 3,6,9 
    for rows in board:
        for col in rows:
            print(col,end=' ')
            z += 1
            if z%3 == 0:
                break
            else:
                print(' | ',end=' ')
        print()
        if z != 9:
            print('---|-----|----')
        else:
            break
    #print(board)
#display_board(board)


''' this function takes Players value and checks the value - is a number and in range (1-9) '''
def users_value():

    # the user choice number must be in board range (means 1-9)
    board_range = range(1,10)
    in_range = False
    
    # checking if the input given by the user is a number
    user = 'WRONG'
    
    '''looping it till the user_input() is a number and in between (1-9)'''
    while user.isdigit() == False or in_range == False:
        user = input('What position would You like to Play ??? ')              # This always returns string 

        # DIGIT CHECK
        if user.isdigit() == False:
            print('OOPS!!! that is not a Number :(')
        
        #RANGE CHECK
        if user.isdigit() == True:
            if int(user) in board_range:
                in_range = True
            else:
                print('Please Choose a number Between (1-9) :')


    return int(user)
#users_value()


''' This function will update board to users choice to "X" or "O" '''
def user_positions(board,p,count):      # p is the users choice value or position

# This game works as an odd-even Turns like Player1 goes in 1st(turn) therefore Player2 goes in 2nd(turn) and so on>>> 
    if count%2 == 0:
        for rows in board:
            for col in rows:
                if col == p:
                    c = rows.index(col)
                    rows.remove(col)
                    rows.insert(c,'X')
                    break
                else:
                   continue
    else:
        for rows in board:
            for col in rows:
                if col == p:
                    c = rows.index(col)
                    rows.remove(col)
                    rows.insert(c,'O')
                    break
                else:
                   continue

    # calling it to update the board with users position
    display_board(board)  
#user_positions(board,4,1)


''' This function will check WINNER '''
def check_win(board):

    result = ' '

    row1 = board[0]  
    row2 = board[1]
    row3 = board[2]
    col1 = [board[0][0],board[1][0],board[2][0]]
    col2 = [board[0][1],board[1][1],board[2][1]]
    col3 = [board[0][2],board[1][2],board[2][2]]
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    diagonal2 = [board[0][2],board[1][1],board[2][0]]
    
    if len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1:
        result = True

    elif len(set(col1)) == 1 or len(set(col2)) == 1 or len(set(col3)) == 1:
        result = True

    elif len(set(diagonal1)) == 1 or len(set(diagonal2)) == 1:
        result =  True

    else :
        result = False
        
    
    return result
#print(check_win(board))


''' THIS FUNCTION WILL RUN ALL THE ABOVE FUNCTION IN A WHILE LOOP WITH 2 CONDITIONS '''
def game_on():
    
    nums = []
    won = False
    display_board(board)
    
    '''-------THIS WHILE LOOP WORKS UNTIL EITHER OF THE PLAYERS WINS OR THERE ARE NO MORE POSITIONS LEFT IN BOARD
              TO PLAY AND THEN THE IF STATEMENT AT END PRINTS "DRAW"-------'''
    
    while len(nums) != 9 and won == False:
        count = len(nums)

        #THIS IF STATEMENT IS FOR PLAYER_1 "X"
        if count%2 == 0:    
            v = users_value()
            if v in nums:
                print('That Position has been taken')
                continue
            else:
                nums.append(v)
                user_positions(board,v,count)      
                #NOW WE NEED TO CHECK IF THE PLAYER_1 WON OR NOT
                won_True_False = check_win(board)
                if won_True_False == True:
                    won = True
                    print('Player1 Wins')
                    print("Good Job! :)")

        #THIS ELSE STATEMENT IS FOR PLAYER_2 "O"
        else:
            v = users_value()
            if v in nums:
                print('That Position has been taken')
                continue
            else:
                nums.append(v)
                user_positions(board,v,count)

                won_True_False = check_win(board)
                if won_True_False == True:
                    won = True
                    print('Player2 Wins')
                    print("Good Job! :)")

    if len(nums) == 9:
        print('DRAW')

game_on()