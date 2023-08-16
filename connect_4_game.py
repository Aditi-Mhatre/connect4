from tkinter import *
from tkinter import messagebox as mb
import random
import copy
import main_menu
import global_variables
import choose_colour


global baseframe, levelN, hole_radius, red_in, red_out, yellow_in, yellow_out, red_moves, yellow_moves, human_chosen, playerfontcolour, compfontcolour, window_width, window_height     #globalise frequently used, unchanging variables & lists

#create root window
root = Tk()
root.title('Connect Four')
root.resizable(False, False)
#fixed frame to nest mainframe
baseframe = Frame(root)
baseframe.pack(anchor = 'center',
               expand = 1)  


# Gets the requested values of the height and width.
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
position_right = int((3 * root.winfo_screenwidth() / 8) - (window_width / 2))
position_down = int((root.winfo_screenheight() / 4) - (window_height / 2))
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(position_right, position_down))


#----------------------------------------------------------------------- V A R I A B L E S ----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

levelN = 7                                      #Normal Level: 7 columns x 6 rows
levelA = 9                                      #Advanced Level: 9 columns x 6 rows

level_selected = global_variables.V[0]          #get the level_selected variable from the radio buttons in main_menu.py 

if level_selected == 1:                         #if variable is 1; Advance mode is given
    BOARDWIDTH = levelA
    canvaswidth = 450
    score_file = 'advanced_mode.txt'
else:
    BOARDWIDTH = levelN                         #else, player plays Normal mode
    canvaswidth = 350
    score_file = 'easy_mode.txt'
    
BOARDHEIGHT = 6                                 #variables in all caps are global on a modular level

hole_radius = 50 / 2

red_moves = []
yellow_moves = []

human_chosen = BooleanVar()
human_chosen.set(False)


#images
empty = PhotoImage(file = 'hole.gif')

red_in = [PhotoImage(file = 'red42.gif'), PhotoImage(file = 'red41.gif'), PhotoImage(file = 'red40.gif'),                     #animation frames (doing this because
          PhotoImage(file = 'red39.gif'), PhotoImage(file = 'red38.gif'), PhotoImage(file = 'red37.gif'),                     #rounded transparent images get very
          PhotoImage(file = 'red36.gif'), PhotoImage(file = 'red35.gif'), PhotoImage(file = 'red34.gif'),                     #pixelated in gif format)
          PhotoImage(file = 'red33.gif'), PhotoImage(file = 'red32.gif'), PhotoImage(file = 'red31.gif'),
          PhotoImage(file = 'red30.gif'), PhotoImage(file = 'red29.gif'), PhotoImage(file = 'red28.gif'),
          PhotoImage(file = 'red27.gif'), PhotoImage(file = 'red26.gif'), PhotoImage(file = 'red25.gif'),
          PhotoImage(file = 'red24.gif'), PhotoImage(file = 'red23.gif'), PhotoImage(file = 'red22.gif'),
          PhotoImage(file = 'red21.gif'), PhotoImage(file = 'red20.gif'), PhotoImage(file = 'red19.gif'),
          PhotoImage(file = 'red18.gif'), PhotoImage(file = 'red17.gif'), PhotoImage(file = 'red16.gif'),
          PhotoImage(file = 'red15.gif'), PhotoImage(file = 'red14.gif'), PhotoImage(file = 'red13.gif'),
          PhotoImage(file = 'red12.gif'), PhotoImage(file = 'red10.gif'), PhotoImage(file = 'red9.gif'),
          PhotoImage(file = 'red9.gif'), PhotoImage(file = 'red8.gif'), PhotoImage(file = 'red7.gif'),
          PhotoImage(file = 'red6.gif'), PhotoImage(file = 'red5.gif'), PhotoImage(file = 'red4.gif'),
          PhotoImage(file = 'red3.gif'), PhotoImage(file = 'red2.gif'), PhotoImage(file = 'red1.gif')]

red_out = [PhotoImage(file = 'red42b.gif'), PhotoImage(file = 'red41b.gif'), PhotoImage(file = 'red40b.gif'),
           PhotoImage(file = 'red39b.gif'), PhotoImage(file = 'red38b.gif'), PhotoImage(file = 'red37b.gif'),
           PhotoImage(file = 'red36b.gif'), PhotoImage(file = 'red35b.gif'), PhotoImage(file = 'red34b.gif'),
           PhotoImage(file = 'red33b.gif'), PhotoImage(file = 'red32b.gif'), PhotoImage(file = 'red31b.gif'),
           PhotoImage(file = 'red30b.gif'), PhotoImage(file = 'red29b.gif'), PhotoImage(file = 'red28b.gif'),
           PhotoImage(file = 'red27b.gif'), PhotoImage(file = 'red26b.gif'), PhotoImage(file = 'red25b.gif'),
           PhotoImage(file = 'red24b.gif'), PhotoImage(file = 'red23b.gif'), PhotoImage(file = 'red22b.gif'),
           PhotoImage(file = 'red21b.gif'), PhotoImage(file = 'red20b.gif'), PhotoImage(file = 'red19b.gif'),
           PhotoImage(file = 'red18b.gif'), PhotoImage(file = 'red17b.gif'), PhotoImage(file = 'red16b.gif'),
           PhotoImage(file = 'red15b.gif'), PhotoImage(file = 'red14b.gif'), PhotoImage(file = 'red13b.gif'),
           PhotoImage(file = 'red12b.gif'), PhotoImage(file = 'red10b.gif'), PhotoImage(file = 'red9b.gif'),
           PhotoImage(file = 'red9b.gif'), PhotoImage(file = 'red8b.gif'), PhotoImage(file = 'red7b.gif'),
           PhotoImage(file = 'red6b.gif'), PhotoImage(file = 'red5b.gif'), PhotoImage(file = 'red4b.gif'),
           PhotoImage(file = 'red3b.gif'), PhotoImage(file = 'red2b.gif'), PhotoImage(file = 'hole.gif')]

yellow_in = [PhotoImage(file = 'yellow42.gif'), PhotoImage(file = 'yellow41.gif'), PhotoImage(file = 'yellow40.gif'),
             PhotoImage(file = 'yellow39.gif'), PhotoImage(file = 'yellow38.gif'), PhotoImage(file = 'yellow37.gif'),
             PhotoImage(file = 'yellow36.gif'), PhotoImage(file = 'yellow35.gif'), PhotoImage(file = 'yellow34.gif'),
             PhotoImage(file = 'yellow33.gif'), PhotoImage(file = 'yellow32.gif'), PhotoImage(file = 'yellow31.gif'),
             PhotoImage(file = 'yellow30.gif'), PhotoImage(file = 'yellow29.gif'), PhotoImage(file = 'yellow28.gif'),
             PhotoImage(file = 'yellow27.gif'), PhotoImage(file = 'yellow26.gif'), PhotoImage(file = 'yellow25.gif'),
             PhotoImage(file = 'yellow24.gif'), PhotoImage(file = 'yellow23.gif'), PhotoImage(file = 'yellow22.gif'),
             PhotoImage(file = 'yellow21.gif'), PhotoImage(file = 'yellow20.gif'), PhotoImage(file = 'yellow19.gif'),
             PhotoImage(file = 'yellow18.gif'), PhotoImage(file = 'yellow17.gif'), PhotoImage(file = 'yellow16.gif'),
             PhotoImage(file = 'yellow15.gif'), PhotoImage(file = 'yellow14.gif'), PhotoImage(file = 'yellow13.gif'),
             PhotoImage(file = 'yellow12.gif'), PhotoImage(file = 'yellow10.gif'), PhotoImage(file = 'yellow9.gif'),
             PhotoImage(file = 'yellow9.gif'), PhotoImage(file = 'yellow8.gif'), PhotoImage(file = 'yellow7.gif'),
             PhotoImage(file = 'yellow6.gif'), PhotoImage(file = 'yellow5.gif'), PhotoImage(file = 'yellow4.gif'),
             PhotoImage(file = 'yellow3.gif'), PhotoImage(file = 'yellow2.gif'), PhotoImage(file = 'yellow1.gif')]

yellow_out = [PhotoImage(file = 'yellow42b.gif'), PhotoImage(file = 'yellow41b.gif'), PhotoImage(file = 'yellow40b.gif'),
              PhotoImage(file = 'yellow39b.gif'), PhotoImage(file = 'yellow38b.gif'), PhotoImage(file = 'yellow37b.gif'),
              PhotoImage(file = 'yellow36b.gif'), PhotoImage(file = 'yellow35b.gif'), PhotoImage(file = 'yellow34b.gif'),
              PhotoImage(file = 'yellow33b.gif'), PhotoImage(file = 'yellow32b.gif'), PhotoImage(file = 'yellow31b.gif'),
              PhotoImage(file = 'yellow30b.gif'), PhotoImage(file = 'yellow29b.gif'), PhotoImage(file = 'yellow28b.gif'),
              PhotoImage(file = 'yellow27b.gif'), PhotoImage(file = 'yellow26b.gif'), PhotoImage(file = 'yellow25b.gif'),
              PhotoImage(file = 'yellow24b.gif'), PhotoImage(file = 'yellow23b.gif'), PhotoImage(file = 'yellow22b.gif'),
              PhotoImage(file = 'yellow21b.gif'), PhotoImage(file = 'yellow20b.gif'), PhotoImage(file = 'yellow19b.gif'),
              PhotoImage(file = 'yellow18b.gif'), PhotoImage(file = 'yellow17b.gif'), PhotoImage(file = 'yellow16b.gif'),
              PhotoImage(file = 'yellow15b.gif'), PhotoImage(file = 'yellow14b.gif'), PhotoImage(file = 'yellow13b.gif'),
              PhotoImage(file = 'yellow12b.gif'), PhotoImage(file = 'yellow10b.gif'), PhotoImage(file = 'yellow9b.gif'),
              PhotoImage(file = 'yellow9b.gif'), PhotoImage(file = 'yellow8b.gif'), PhotoImage(file = 'yellow7b.gif'),
              PhotoImage(file = 'yellow6b.gif'), PhotoImage(file = 'yellow5b.gif'), PhotoImage(file = 'yellow4b.gif'),
              PhotoImage(file = 'yellow3b.gif'), PhotoImage(file = 'yellow2b.gif'), PhotoImage(file = 'hole.gif')]       
       
#styles
header_font = ('Helvetic', 12, 'bold')
button_font = ('Helvetic', 11, 'bold')
text_font = ('Helvetic', 9, 'italic')
statboard_font = ('Helvetica', 10)


#--------------------------------------------------------------------- G A M E   G U I   S E T U P ------------------------------------------------------------------------------------------------------------------------------------'''

def createGUIFrames():
    '''Create GUI frames.'''
    global mainframe, compstat_frame, plyrstat_frame, statmsg_frame, boardbutton_frame, canvas, footer_frame
    
    #mainframe  
    mainframe = Frame(baseframe)
    mainframe.pack(anchor = 'center',
                   expand = 1)
      
    #statusbar
    if humanTile == 'O':
        compstat_bg = '#fefa85'
        plyrstat_bg = '#eca2a2'
    else:
        compstat_bg = '#eca2a2'
        plyrstat_bg = '#fefa85'
        
    statbar_frame = Frame(mainframe)                                        #create frame for STATUS BARS (child to mainframe)
    statbar_frame.grid(row = 0,                                             #place it in the first row; stick both horizontal ends
                       columnspan = 3,                                      #takes up 3 columns
                       sticky ='EW')


    compstat_frame = Frame(statbar_frame,                                   #create frame for COMPUTER'S STAT BAR (child to statbar_frame)
                           bg = compstat_bg,
                           width = 150,
                           height = 85)
    compstat_frame.grid(row = 0,                                            #place it in the first column and row w/ internal paddings of 5; stick to all corners
                        column = 0,
                        sticky = 'NSEW',
                        ipadx = 5,
                        ipady = 5)
    compstat_frame.grid_propagate(0)                                        #disabling propagation keeps the frame from shrinking



    plyrstat_frame = Frame(statbar_frame,                                   #create frame for PLAYER'S STAT BAR (child to statbar_frame)
                           bg = plyrstat_bg,
                           width = 150,
                           height = 85)
    plyrstat_frame.grid(row = 0,                                            #place it in the third column, first row w/ internal paddings of 5; stick to all corners
                        column = 2,
                        sticky = 'NSEW',
                        ipadx = 5,
                        ipady = 5)
    plyrstat_frame.grid_propagate(0)                                        #disabling propagation keeps the frame from shrinking



    statmsg_frame = Frame(statbar_frame,                                    #create frame for STAT MESSAGES (child to statbar_frame)
                          bg = '#d5dbe6',
                          width = 200,
                          height = 85)
    statmsg_frame.grid(row = 0,                                             #place it in the second column, first row w/ internal paddings of 5; stick to all corners
                       column = 1,
                       sticky = 'NSEW',
                       ipadx = 5,
                       ipady = 5)
    statmsg_frame.grid_propagate(0)                                         #disabling propagation keeps the frame from shrinking


    #board
    board_frame = Frame(mainframe)                                          #create frame for BOARD (child to mainframe)
    board_frame.grid(row = 1,                                               #place it in the second row; stick both horizontal ends
                     sticky = 'EW')    


    boardbutton_frame = Frame(board_frame,                                  #create frame for BOARD BUTTONS (child to board_frame)
                              bg = '#ddcbaf',
                              height = 60)
    boardbutton_frame.grid(column = 0,
                           row = 0,                                         #place it in the first row & column; stick to top and sides
                           columnspan = 5,                                  #takes up 5 columns
                           sticky = 'NEW')


    board_topEdge = Frame(board_frame,                                      #create BOARD TOP EDGE (child to board_frame)
                          bg = '#13508e',
                          width = (hole_radius * 2 * BOARDWIDTH) + 20,
                          height = 10)
    board_topEdge.grid(column = 1,                                          #place it in the second column, second row; stick to all corners
                       row = 1,
                       columnspan = 3,                                      #takes up 3 columns
                       sticky = 'NSEW')
    
    board_bottomEdge = Frame(board_frame,                                   #create BOARD BOTTOM EDGE (child to board_frame)
                             bg = '#13508e',
                             width = (hole_radius * 2 * BOARDWIDTH) + 20,
                             height = 10)
    board_bottomEdge.grid(column = 1,                                       #place it in the second column, fourth row; stick to all corners
                          row = 3,
                          columnspan = 3,                                   #takes up 3 columns
                          sticky = 'NSEW') 

    board_leftEdge = Frame(board_frame,                                     #create BOARD LEFT EDGE (child to board_frame)
                           bg = '#13508e',
                           width = 10,
                           height = (hole_radius * 12))
    board_leftEdge.grid(column = 1,                                         #place it in the second column, third row; stick to all corners
                        row = 2,
                        sticky = 'NSEW')
    
    board_rightEdge = Frame(board_frame,                                    #create BOARD RIGHT EDGE (child to board_frame)
                            bg = '#13508e',
                            width = 10,
                            height = (hole_radius * 12))
    board_rightEdge.grid(column = 3,                                        #place it in the fourth column, third row; stick to all corners
                         row = 2,
                         sticky = 'NSEW')


    canvas = Canvas(board_frame,                                            #create CANVAS for board (child to board_frame)
                    bg = '#13508e',
                    width = canvaswidth,
                    height = (hole_radius * 12),
                    highlightthickness = 0)
    canvas.grid(column = 2,
                row = 2,                                                    #place it in the third column & row; stick to all corners
                sticky = 'NSEW')


    if BOARDWIDTH == 7:
        whitespace_width = 80
    else:
        whitespace_width = 30

    whitespaceLeft = Frame(board_frame,                                     #create LEFT WHITESPACE (child to board_frame)
                           bg = '#ddcbaf',
                           width = whitespace_width,
                           height = (hole_radius * 12))
    whitespaceLeft.grid(column = 0,                                         #place it in the first column, second row; stick to all corners
                        row = 1,
                        rowspan = 3,                                        #takes up 3 rows
                        sticky = 'NSEW')

    whitespaceRight = Frame(board_frame,                                    #create RIGHT WHITESPACE (child to board_frame)
                            bg = '#ddcbaf',
                            width = whitespace_width,
                            height = (hole_radius * 12))
    whitespaceRight.grid(column = 4,                                        #place it in the fifth column, second row; stick to all corners
                         row = 1,
                         rowspan = 3,                                       #takes up 3 rows
                         sticky = 'NSEW')


    #footer
    footer_frame = Frame(mainframe,                                         #create frame for FOOTER (child to mainframe)
                         bg = '#ddcbaf',
                         height = 20)    
    footer_frame.grid(row = 2,                                              #place it in the third row w/ internal paddings of 5; stick both horizontal ends
                      columnspan = 5,                                       #takes up 5 columns
                      sticky = 'EW',
                      ipadx = 5,
                      ipady = 5)

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def createGUIStatusbar():
    '''Creates the elements in the statusbar.'''
    global playerScore, computerScore, plyrscoreLabel, compscoreLabel, plyrturnsLabel, compturnsLabel, statmessageLabel, statmessage
    
    #stat variables to be changed in real time on the GUI
    playerTurns = 0
    computerTurns = 0
    playerScore = 0
    computerScore = 0
    statmessage = 'Let\'s play Connect Four!'
    
    if humanTile == 'O':
        compstat_bg = '#fefa85'
        plyrstat_bg = '#eca2a2'
        compstat_title = '#d84d01'
        plyrstat_title = '#a70000'
    else:
        compstat_bg = '#eca2a2'
        plyrstat_bg = '#fefa85'
        compstat_title = '#a70000'
        plyrstat_title = '#d84d01'

    statcolour = '#323030'

        
    #computer's status bar
    Label(compstat_frame,
          text = ' C O M P U T E R ',
          anchor = 'center',
          bg = compstat_bg,
          fg = compstat_title,
          font = header_font).grid(row = 0,
                                   column = 0,
                                   columnspan = 2,
                                   padx = 3,
                                   pady = 3)
    compstat_frame.columnconfigure(0, weight = 1)
    compstat_frame.columnconfigure(1, weight = 1)
                                  
    Label(compstat_frame,
          text = 'SCORE',
          anchor = 'w',
          bg = compstat_bg,
          fg = statcolour,
          font = text_font).grid(row = 1,
                                 column = 0,
                                 padx = 3,
                                 pady = 3)
    Label(compstat_frame,
          text = 'TURNS',
          anchor = 'w',
          bg = compstat_bg,
          fg = statcolour,
          font = text_font).grid(row = 2,
                                 column = 0,
                                 padx = 3,
                                 pady = 3)
    
    compscoreLabel = Label(compstat_frame,
                           text = computerScore,
                           anchor = 'w',
                           bg = compstat_bg,
                           fg = statcolour,
                           font = button_font)
    compscoreLabel.grid(row = 1,
                        column = 1,
                        padx = 3,
                        pady = 3)

    compturnsLabel = Label(compstat_frame,
                           text = computerTurns,
                           anchor = 'w',
                           bg = compstat_bg,
                           fg = statcolour,
                           font = button_font)
    compturnsLabel.grid(row = 2,
                        column = 1,
                        padx = 3,
                        pady = 3)
    
   
    #player's status bar
    Label(plyrstat_frame,
          text = ' P L A Y E R ',
          anchor = 'e',
          bg = plyrstat_bg,
          fg = plyrstat_title,
          font = header_font).grid(row = 0,
                                   column = 0,
                                   columnspan = 2,
                                   padx = 6,
                                   pady = 3)
    plyrstat_frame.columnconfigure(0, weight = 1)
    plyrstat_frame.columnconfigure(1, weight = 1)

    Label(plyrstat_frame,
          text = 'SCORE',
          anchor = 'w',
          bg = plyrstat_bg,
          fg = statcolour,
          font = text_font).grid(row = 1,
                                 column = 0,
                                 padx = 3,
                                 pady = 3)
    Label(plyrstat_frame,
          text = 'TURNS',
          anchor = 'w',
          bg = plyrstat_bg,
          fg = statcolour,
          font = text_font).grid(row = 2,
                                 column = 0,
                                 padx = 3,
                                 pady = 3)
    
    plyrscoreLabel = Label(plyrstat_frame,
                           text = playerScore,
                           anchor = 'w',
                           bg = plyrstat_bg,
                           fg = statcolour,
                           font = button_font)
    plyrscoreLabel.grid(row = 1,
                        column = 1,
                        padx = 3,
                        pady = 3)

    plyrturnsLabel = Label(plyrstat_frame,
                           text = playerTurns,
                           anchor = 'w',
                           bg = plyrstat_bg,
                           fg = statcolour,
                           font = button_font)
    plyrturnsLabel.grid(row = 2,
                        column = 1,
                        padx = 3,
                        pady = 3)
    

    #statbar message
    statmessageLabel = Label(statmsg_frame,
                             text = statmessage,
                             bg = '#d5dbe6',
                             fg = statcolour,
                             font = statboard_font)
    statmessageLabel.place(x = 105,
                           y = 49,
                           anchor = 'center')
                             
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''  

def createGUIClickables():
    '''Creates the game buttons, as well as the help, exit and reset buttons in the GUI.'''
    global v, chosen_col, col_menu, dropbutton
    
    if humanTile == 'O':
        active_colour = '#df6c5a'
    else:
        active_colour = '#dfd45a'
        
    #game column optionmenu
    Label(boardbutton_frame,
          text = 'Choose a column: ',
          anchor = 'center',
          bg = '#ddcbaf',
          fg = 'steelblue',
          font = ('Arial', 16)).place(x = 185,
                                y = 30,
                                anchor = 'center')

    columns = [str(i+1) for i in range(BOARDWIDTH)]             #menu options
    
    chosen_col = {}
    chosen_col.update([(i, int(i)-1) for i in columns])         #update dictionary w/ values corresponding to menu options

    v = StringVar()                                             #text shown on option menu when selected
    v.set('Column')


    col_menu = OptionMenu(boardbutton_frame,
                          v,
                          *columns,
                          command = getHumanMove)

    col_menu.config(width = 7,
                    bg = '#625f5b',
                    fg = '#b1d1c5',
                    font = (5),
                    activebackground = '#625f5b',
                    activeforeground = active_colour,
                    relief = 'flat',
                    cursor = 'hand2')
    col_menu.place(x = 340,
                   y = 30,
                   anchor = 'center')

    
    dropbutton = Button(boardbutton_frame)                      #button merely used for waiting function in main()
        


    
    #help button
    helpbutton = Button(boardbutton_frame,                      #create HELP BUTTON (child to footer_frame)
                        text = 'help',
                        font = statboard_font,
                        command= guide)
    helpbutton.config(bg = '#b2c4e1',
                      fg = '#3d3d3d',
                      activebackground = '#d5dbe6',
                      relief = 'ridge',
                      cursor = 'hand2')    
    helpbutton.place(x = 490,
                     y = 30,
                     anchor = 'center')

                    

#============================================================================ M A I N =============================================================================================================================================

def main():
    global humanTile, computerTile, IDLEBoard, turn, playerTurns, computerTurns
    """
    b = getNewBoard()
    b[6][5] = 'X'
    b[5][4] = 'X'
    b[4][3] = 'X'
    b[3][2] = 'X'
    drawIDLEBoard(b)
    print(isWinner(b, 'X'))

    sys.exit()
    """

    print('\nLet\'s play Connect Four!\n')

    score = 3


    winner = None
    playerTurns = 0
    computerTurns = 0
    humanTile, computerTile = enterHumanTile()
    #set the font colours based on the player's chosen colour
    if humanTile == 'O':
        playerfontcolour = '#a70000'
        compfontcolour = '#d84d01'
    else:
        playerfontcolour = '#d84d01'
        compfontcolour = '#a70000'           

    #set up GUI
    createGUIFrames()
    createGUIStatusbar()
    createGUIClickables()
    
    
    turn = whoGoesFirst()
    print('The %s player will go first.' % (turn))

    IDLEBoard = getNewBoard()   
    emptyCANVASBoard()

    while True:
        if turn == 'human':                                     #if human plays,
            statmessage = 'It\'s your turn! Pick a move.'
            statmessageLabel.config(text = statmessage,             #update statusbar message
                                    fg = playerfontcolour)
            col_menu.configure(state = 'active')                    #enable the option menu
            while human_chosen.get() == False:                      #while loop which waits for the player to choose a column
                dropbutton.wait_variable(human_chosen)

            drawIDLEBoard()                                         #draw the IDLE board
            playerTurns += 1                                        #add one to variable for number of turns
            if BOARDWIDTH == levelN:
                if isNormalWinner(IDLEBoard, humanTile):
                    winner = 'human'                                    #check if player is the winner and set the winner variable
                    playerScore += 3 + (21 - playerTurns) * 5           #player earns extra points if they win based on how little moves they made
                    plyrturnsLabel.config(text = playerTurns)           #update the score and turn labels in real time
                    plyrscoreLabel.config(text = playerScore)
                    break                                               #break the loop if so
            else:
                if isAdvancedWinner(IDLEBoard, humanTile):
                    winner = 'human'
                    playerScore += 3 + (27 - playerTurns) * 5
                    plyrturnsLabel.config(text = playerTurns)
                    plyrscoreLabel.config(text = playerScore)
                    break
            playerScore = (score * playerTurns)                     #set the score variable
            plyrturnsLabel.config(text = playerTurns)               #update the score and turn labels in real time
            plyrscoreLabel.config(text = playerScore)
            
            human_chosen.set(False)                                 #reset the waiting loop
            turn = 'computer'                                       #computer's turn to play
                
        else:                                                   #if computer plays,
            statmessage = 'It\'s the computer\'s turn now!'
            statmessageLabel.config(text = statmessage,             #update statusbar message
                                    fg = compfontcolour)
            col_menu.configure(state = 'disabled')                  #disable the option menu
            drawIDLEBoard()                                         #draw the IDLE board
            print('The computer is thinking...')
            move = getComputerMove()
            makeMove(IDLEBoard, computerTile, move)                 #make the move
            computerTurns += 1                                      #add one to variable for number of turns
            if BOARDWIDTH == levelN:
                if isNormalWinner(IDLEBoard, computerTile):
                    winner = 'computer'                             #check if computer is the winner and break the loop if so
                    break
            else:
                if isAdvancedWinner(IDLEBoard, computerTile):
                    winner = 'computer'
                    break  
            computerScore = (score * computerTurns)                 #set the score variable 
            compturnsLabel.config(text = computerTurns)             #update the score and turn labels in real time
            compscoreLabel.config(text = computerScore)

            turn = 'human'                                          #human's turn to play

        if isBoardFull(IDLEBoard):      #if the board is full,
            winner = 'tie'                  #both players' are tied
            break                           #break the loop                      
    
    drawIDLEBoard()

    #determine which message to leave
    if winner == 'tie':
        statmessage = 'Draw!\nYou\'ve scored ' + str(playerScore) + ' points.'
        statmessageLabel.config(text = statmessage,                             #update statusbar message
                                fg = '#07347f')
        print(statmessage)
    else:
        if winner == 'computer':
            statmessage = 'The computer\'s won this round.\nBetter luck next time!\nHowever, you\'ve managed to\nscore ' + str(playerScore) + ' points! Well done.'
            statmessageLabel.config(text = statmessage,
                                    fg = '#07347f')
            print(statmessage)
            print("\nNumber of Attempts:", playerTurns)
        else:
            attempt = Message(playerTurns)
            statmessage = 'Yayyy, you won!\nYou\'ve scored ' + str(playerScore) + ' points\nin ' + str(playerTurns) + ' moves.\n' + attempt
            statmessageLabel.config(text = statmessage,
                                    fg = '#07347f')
            print(statmessage)

    global_variables.score.append(playerScore)          #append the player's score into the global list
    recordScore(score_file, winner)                     #record the player's username and score into the scorebard

    exec(open('scoreBoard.py').read())
    quit(main_menu)
                             
    

#========================================================================= G A M E   S Y S T E M ===========================================================================================================

def enterHumanTile():
    '''Lets the player choose which colour they want to play as.'''
    choose_colour                                                           #execute choose_colour pop-up
    if choose_colour.global_variables.global_list != []:                    #if the global list isn't empty,
        return choose_colour.global_variables.global_list                   #return the global list with the human player's tile as the first item,
                                                                            #and the computer's tile as the second.


def getNewBoard():
    '''Create a new board in the game system.'''  
    IDLEboard = []                                                                              #board is a list of columns
    for x in range(BOARDWIDTH):                                                               #x - axis (columns) ((list of rows))
        IDLEboard.append([' '] * BOARDWIDTH)                                                  #y - axis (rows)    ((elements in said list))       
    return IDLEboard



def drawIDLEBoard():
    '''Draws a board on the IDLE.'''
    print()
    print(' ', end='')
    for x in range(1, BOARDWIDTH + 1):
        print(' %s  ' % x, end='')
    print()

    print('+---+' + ('---+' * (BOARDWIDTH - 1)))

    for y in range(BOARDHEIGHT):
        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

        print('|', end='')
        for x in range(BOARDWIDTH):
            print(' %s |' % IDLEBoard[x][y], end='')
        print()

        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

        print('+---+' + ('---+' * (BOARDWIDTH - 1)))


   
def emptyCANVASBoard():
    '''Create a new board in the game GUI.'''
    coordinates = [25, 75, 125, 175, 225, 275, 325, 375, 425]
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):           
            column = coordinates[x]
            row = coordinates[y]
                       
            canvas.create_image(column,                 #create the BOARD on the canvas
                                row,
                                image = empty)


def getHumanMove(*args):
    '''Sets the move variable to the player's chosen column from the optionmenu
    and plays the move.'''
    key = v.get()
    move = int(chosen_col[key])
    makeMove(IDLEBoard, humanTile, move)
    return

    

def getComputerMove():
    '''Selects a random move for the Computer from a list of the best possible moves.'''
    if BOARDWIDTH == levelN:
        potentialMoves = getNormalPotentialMoves(IDLEBoard, computerTile, 2)
    else:
        potentialMoves = getAdvancedPotentialMoves(IDLEBoard, computerTile, 2)
    bestMoveScore = max([potentialMoves[i] for i in range(BOARDWIDTH) if isValidMove(IDLEBoard,i) == True])
    bestMoves = []
    for i in range(len(potentialMoves)):
        if potentialMoves[i] == bestMoveScore:
            bestMoves.append(i)
    return random.choice(bestMoves)



def getNormalPotentialMoves(board, playerTile, lookAhead):
    '''Predicts the player's moves and makes it harder for the player to win >:) (uses the normal winning algorithm).'''
    if lookAhead == 0:
        return [0] * BOARDWIDTH

    potentialMoves = []

    if playerTile == 'X':
        enemyTile = 'O'
    else:
        enemyTile = 'X'

    # Returns (best move, average condition of this state)
    if isBoardFull(board):
        return [0] * BOARDWIDTH

    # Figure out the best move to make.
    potentialMoves = [0] * BOARDWIDTH
    for playerMove in range(BOARDWIDTH):
        dupeBoard = copy.deepcopy(board)
        if not isValidMove(dupeBoard, playerMove):
            continue
        makeDupeMove(dupeBoard, playerTile, playerMove)

        if isNormalWinner(dupeBoard, playerTile):
            potentialMoves[playerMove] = 1
            break
        else:
            # do other player's moves and determine best one
            if isBoardFull(dupeBoard):
                potentialMoves[playerMove] = 0
            else:
                for enemyMove in range(BOARDWIDTH):
                    dupeBoard2 = copy.deepcopy(dupeBoard)
                    if not isValidMove(dupeBoard2, enemyMove):
                        continue
                    makeDupeMove(dupeBoard2, enemyTile, enemyMove)
                    if isNormalWinner(dupeBoard2, enemyTile):
                        potentialMoves[playerMove] = -1
                        break
                    else:
                        results = getNormalPotentialMoves(dupeBoard2, playerTile, lookAhead - 1)
                        potentialMoves[playerMove] += (sum(results) / BOARDWIDTH) / BOARDWIDTH
    return potentialMoves



def getAdvancedPotentialMoves(board, playerTile, lookAhead):
    '''Predicts the player's moves and makes it harder for the player to win >:) (uses the advanced winning algorithm).'''
    if lookAhead == 0:
        return [0] * BOARDWIDTH

    potentialMoves = []

    if playerTile == 'X':
        enemyTile = 'O'
    else:
        enemyTile = 'X'

    # Returns (best move, average condition of this state)
    if isBoardFull(board):
        return [0] * BOARDWIDTH

    # Figure out the best move to make.
    potentialMoves = [0] * BOARDWIDTH
    for playerMove in range(BOARDWIDTH):
        dupeBoard = copy.deepcopy(board)
        if not isValidMove(dupeBoard, playerMove):
            continue
        makeDupeMove(dupeBoard, playerTile, playerMove)

        if isAdvancedWinner(dupeBoard, playerTile):
            potentialMoves[playerMove] = 1
            break
        else:
            # do other player's moves and determine best one
            if isBoardFull(dupeBoard):
                potentialMoves[playerMove] = 0
            else:
                for enemyMove in range(BOARDWIDTH):
                    dupeBoard2 = copy.deepcopy(dupeBoard)
                    if not isValidMove(dupeBoard2, enemyMove):
                        continue
                    makeDupeMove(dupeBoard2, enemyTile, enemyMove)
                    if isAdvancedWinner(dupeBoard2, enemyTile):
                        potentialMoves[playerMove] = -1
                        break
                    else:
                        results = getAdvancedPotentialMoves(dupeBoard2, playerTile, lookAhead - 1)
                        potentialMoves[playerMove] += (sum(results) / BOARDWIDTH) / BOARDWIDTH
    return potentialMoves


def whoGoesFirst():
    '''Randomly choose who goes first.'''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'


def isValidMove(board, move):
    '''Checks if the move to be made is executable.'''
    if move < 0 or move >= (BOARDWIDTH):
        return False

    if board[move][0] != ' ':
        return False

    return True


def makeMove(board, tile, column):
    '''Makes the move in the game system and on IDLE and the GUI.'''
    if tile == humanTile:
        human_chosen.set(True)                                  #set the condition which allows the player's move to be made
    else:
        pass
    for y in range(BOARDHEIGHT, 0, -1):
        if board[column][y-1] == ' ':              
            collectLatestMove(column, y-1, tile)                #collect the moves
            board[column][y-1] = tile                           #IDLE 
            dropTileAnimation(tile)                             #GUI
            return

def makeDupeMove(board, tile, column):
    '''Makes the move in the game system and on IDLE.'''
    for y in range(BOARDHEIGHT-1, -1, -1):
        if board[column][y] == ' ':
            board[column][y] = tile                             #IDLE
            return


def collectLatestMove(column, row, tile):
    '''Collect latest move made into the move lists.'''
    if tile == 'O':                                             #if a red tile is used,
        movelist = red_moves                                        #use the red list
    else:                                                       #else (yellow),
        movelist = yellow_moves                                     #use the yellow list

    movelist.append(column)                                     #append x-coordinates to the list
    movelist.append(row)                                        #append y-coordinates to the list

    print('Move made at: (' + str(movelist[-2]) + ',' + str(movelist[-1]) + ')')



def createPreviousMoves(tile):
    '''Create the previously made moves in the GUI.'''
    coordinates = [25, 75, 125, 175, 225, 275, 325, 375, 425]
    
    if humanTile == 'O':
        humanMoves = red_moves
        humanImg = red_in
        computerMoves = yellow_moves
        computerImg = yellow_in
    else:
        humanMoves = yellow_moves
        humanImg = yellow_in
        computerMoves = red_moves
        computerImg = red_in
        
    #player moves
    #latest moves
    if playerTurns > 0:
        if humanTile != tile:          #if player isn't the current player
            xcoord = humanMoves[-2]                                          #x-coordinates on board
            ycoord = humanMoves[-1]                                          #y-coordinates on board        
            canvas.create_image(coordinates[xcoord],                         #create the full tile image on the coordinates of the move made
                                coordinates[ycoord],                            
                                image = humanImg[41])
        else:
            pass
    else:
        pass
    
    #rest of the moves    
    for i in range(0, len(humanMoves) - 2, 2):                       #iterate through everything except the last two elements (latest move), skipping every second move
        xcoord = humanMoves[i]
        ycoord = humanMoves[i+1]
        
        canvas.create_image(coordinates[xcoord],
                            coordinates[ycoord],                            
                            image = humanImg[41])
   
    #computer moves
    #latest moves
    if computerTurns > 0:
        if computerTile != tile:
            xcoord = computerMoves[-2]
            ycoord = computerMoves[-1]
            canvas.create_image(coordinates[xcoord],
                            coordinates[ycoord],                            
                            image = computerImg[41])
        else:
            pass
    else:
        pass

    #rest of the moves  
    for i in range(0, len(computerMoves) - 2, 2):
        xcoord = computerMoves[i]
        ycoord = computerMoves[i+1]
        
        canvas.create_image(coordinates[xcoord],
                            coordinates[ycoord],                            
                            image = computerImg[41])




def dropTileAnimation(tile):
    '''Animates the tile drop sequence.'''
    if tile == 'O':
        movelist = red_moves
        imagelist_in = red_in
        imagelist_out = red_out

    else:
        movelist = yellow_moves
        imagelist_in = yellow_in
        imagelist_out = yellow_out

    col = movelist[-2]                                              #latest x coordinate in movelist
    row_dropped = movelist[-1]                                      #latest y coordinate in movelist

    rowcoords = [25, 75, 125, 175, 225, 275]
    coordinates = [25, 75, 125, 175, 225, 275, 325, 375, 425]
    column_chosen = coordinates[col]                                #CANVAS coordinates for the column chosen


    for i in range(row_dropped + 1):                                #drop distance (by hole)          
        #drop animation
        if i == 0:                                                          #if the drop distance is 1 or if it's the first iterated row,
            for j in range(42):                                                 #42 images per animation
                canvas.delete(ALL)                                                  #clear the canvas              
                emptyCANVASBoard()                                                  #create an empty board
                if red_moves != [] and yellow_moves != []:                         #create previously made moves if movelists are not empty
                    createPreviousMoves(tile)
                canvas.create_image(column_chosen,                                  #create the tile on the chosen column
                                    rowcoords[i],                                   #on each row
                                    image = imagelist_in[j])                        #image changes each loop to animate drop in
                canvas.update()                                                     #refresh object on the canvas

        else:                                                               #else,
            for j in range(42):
                canvas.delete(ALL)
                emptyCANVASBoard()
                if red_moves != [] and yellow_moves != []:                         #create previously made moves if movelists are not empty
                    createPreviousMoves(tile)
                canvas.create_image(column_chosen,                                  #animate the drop-in on the iterated hole
                                    rowcoords[i],                                      
                                    image = imagelist_in[j])
                canvas.create_image(column_chosen,                                  #animate the drop-out
                                    rowcoords[i-1],                                 #on each row above
                                    image = imagelist_out[j])           
                canvas.update()



def isBoardFull(board):
    '''Checks and returns True if board is full.'''
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == ' ':
                return False
    return True


def isNormalWinner(board, tile):
    '''The normal winning algorithm which requires 4 tiles in a row.'''
    # check horizontal spaces
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # check vertical spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # check (/) diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(3, BOARDHEIGHT):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # check (\) diagonal spaces
    for x in range(BOARDWIDTH - 3):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False


def isAdvancedWinner(board, tile):
    '''The advanced winning algorithm which requires 5 tiles in a row.'''
    # check horizontal spaces
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH-4):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile and board[x+4][y] == tile:
                return True

    # check vertical spaces        
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT-4):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile and board[x][y+4] == tile:
                return True

    # check (/) diagonal spaces        
    for x in range(BOARDWIDTH-4):
        for y in range(BOARDHEIGHT-4):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile and board[x+4][y+4] == tile:
                return True
            
    # check (\) diagonal spaces
    for x in range(BOARDWIDTH-4):
        for y in range(4,BOARDHEIGHT):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile and board[x+4][y-4] == tile:
                return True
    return False



def Message(count):
    '''Returns the final message for when the game ends which depends on how many turns were taken by the player.'''
    if count < 10:
        message = "You have the talent!"
    elif count < 15:
        message = "Not too Bad"
    else:
        message = "You can do Better"
    return message

    

def guide():
    '''Creates a top window with the help guide.'''
    g_window = Toplevel(root, bg = '#d5dbe6')
    g_window.title("How to Play")
    g_window.geometry("530x505+{}+{}".format(position_right, position_down))
    g_window.resizable(False, False)

    #textbox
    textbox = Text(g_window,
                  height = 50,
                  width = 64,
                  bg = '#d5dbe6',
                  relief = 'flat')
    #scrollbar
    scrollbar = Scrollbar(g_window,
                          command = textbox.yview)
    textbox.configure(yscrollcommand = scrollbar.set)


    #fonts
    textbox.tag_configure('title',
                          font = ('Arial', 20),
                          foreground = 'steelblue')
    textbox.tag_configure('instructions',
                          font = ('Verdana', 11),
                          foreground = '#3d3d3d')

    #instuctions
    title = '\n                       How to play:\n'

    instruction_1 = '''
                1.  To drop a tile into the column of your choosing,
                     choose the column's corresponding number from
                     the drop-down menu.
                                '''
    instruction_2 = '''
                2.  The tile will fall to the last empty row.
                                '''
    instruction_3 = '''
                3.  The aim of the game in Normal mode is to have
                     four of your tiles in a row, be it horizontally,
                     vertically or diagonally.
                                '''
    instruction_4 = '''
                4.  To spice things up in the Advanced mode,
                     five tiles are required instead of four.
                                '''
    instruction_5 = '''
                5.  You and the computer will take turns dropping
                     tiles. The first player to connect four or five
                     of their tiles wins!
                                '''
    instruction_6 = '''
                6.  Three points are allocated for each drop. If you
                     win, 5 extra points will be give for the moves you
                     didn't have to make to win. Have fun!\n'''

    #insert text & images into textbox
    textbox.insert(END, title, 'title')
    textbox.insert(END, instruction_1, 'instructions')
    textbox.insert(END, instruction_2, 'instructions')
    textbox.insert(END, instruction_3, 'instructions')
    textbox.insert(END, instruction_4, 'instructions')
    textbox.insert(END, instruction_5, 'instructions')
    textbox.insert(END, instruction_6, 'instructions')

    #pack textbox and scrollbar into the window
    textbox.pack(side = LEFT)
    scrollbar.pack(side = RIGHT, fill = Y)

    #disable textbox from being edited
    textbox.config(state = DISABLED)



'''-------------------------------------------------------------------- S C O R E   B O A R D --------------------------------------------------------------------------------------------------'''

def read_file(file):
    '''Opens file for reading.'''
    f = open(file, 'r')
    result = f.readlines()
    f.close()

    return result

# Removes \n and \t. Also separates items in contents list
def strip_and_split(item):
    '''Strips and splits items in contents list.'''
    for i in range(len(item)):
        item[i] = item[i].strip('\n')
        item[i] = item[i].split('\t')
    return item


def temp_list(item1, item2):
    '''Creates list that can be added to contents list.'''
    adderList = []
    adderList.append(item1)
    adderList.append(item2)
    return adderList


def add_contents(item1, item2):
    '''Adds temp list to contents based on:
        1) score
        2) indesentinel'''
    sentinel = 0 # Sentinel to stop loop
    count = 0
    # Compares user score to scores in contents
    if item1 != [] and item2 != []: #if lists are not empty       
        while sentinel != 1:
            if int(item1[1]) > int(item2[count][1]): # If score larger, insert above
                item2.insert(count, item1)
                sentinel = 1
            elif count == len(item2) - 1: # Score lower than all, append to end
                item2.append(item1)
                sentinel = 1
            else: # Score lower, check nesentinelt
                count += 1
        return item2
    else:
        pass


def file_overwrite(item1):
    '''Overwrites old contents in the text files'''
    filo = open(score_file, 'w')
    if item1 != []: #if list isn't empty  
        count = 0
        while count < len(item1):
            if count != len(item1) - 1: # Inserts \t and \n for non-last items
                filo.write(item1[count][0])
                filo.write('\t')
                filo.write(item1[count][1])
                filo.write('\n')
            else: # Inserts only \t for last item
                filo.write(item1[count][0])
                filo.write('\t')
                filo.write(item1[count][1])
            count += 1
    else:
        pass
    
    filo.close()

    return item1

def recordScore(file, winner):
    '''Gets username and score from score list in global_variables and appends them to the score textfiles.'''
    username = global_variables.score[-2]
    print("Username:", username)
    score = str(global_variables.score[-1])
    print("Score:", score)
    
    # f = open(file, 'a')
    # f.write(username + '\t' + str(score) + '\n')
    # f.close()


    '''Main code for scoreboard'''
    # read_file
    contents = read_file(score_file) # Reads currently selected difficulty's file
                                     # as list

    # strip_and_split
    contents = strip_and_split(contents)

    # temp_list
    temporary_list = temp_list(username, score)

    # add_contents
    contents = add_contents(temporary_list, contents)

    # file_overwrite
    file_overwrite(contents)

    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


main()

root.mainloop()    #display window
