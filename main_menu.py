from tkinter import *
import global_variables
import connect_4_game

global root, position_right, position_down

#------------------------------------------------------------------------- F u n c t i o n s -----------------------------------------------------------------------------------------------------------

def getLevel():
    '''Function to choose difficulty level.'''
    lvlframe = Frame(display,
                     width = 900,
                     height = 500,
                     bg = '#6ca2c8')
    lvlframe.pack()
    
    label = Label(lvlframe,
                  text = 'Choose a level:',
                  bg = '#6ca2c8',
                  fg = 'white',
                  font=('Arial', 20))
    label.place(x = 265,
                y = 200,
                anchor = 'center')
    
    v = IntVar()
    
    norm = Radiobutton(lvlframe,
                       text = 'Normal',
                       font=('Arial', 16),
                       fg = '#3d3d3d',
                       bg = '#6ca2c8',
                       activebackground = '#b2c4e1',
                       variable = v,
                       value = 0,
                       command = lambda:getVandClose(v)).place(x = 190, y = 240)
    adv = Radiobutton(lvlframe,
                      text = 'Advanced',
                      font=('Arial', 16),
                      fg = '#3d3d3d',
                      bg = '#6ca2c8',
                      activebackground = '#b2c4e1',
                      variable = v,
                      value = 1,
                      command = lambda:getVandClose(v)).place(x = 190, y = 280)

    
    
def getUsernameandRunLevel():
    '''Get and append the entry variable to the list in global_variables,
    and run the level function.'''
    username = entrybox.get()
    global_variables.score.append(username)
    frame.destroy()
    getLevel()
    return


    
def usernameEntry():
    '''Ask for the player's username.'''
    global frame, entrybox, go_button
    #label
    frame = Frame(display,
                  width = 900,
                  height = 500,
                  bg = '#6ca2c8')
    frame.pack()
    
    label = Label(frame,
                  text = 'What\'s your username?',
                  bg = '#6ca2c8',
                  fg = 'white',
                  font=('Arial', 20))
    label.place(x = 265,
                y = 200,
                anchor = 'center')

    #button
    go_button = Button(frame,
                       text = 'Go!',
                       font = ('Arial', 16),
                       fg = '#3d3d3d',
                       bg = '#b2c4e1',
                       activebackground = '#d5dbe6',
                       width = 10,
                       height = 1,
                       cursor = 'hand2',
                       command = getUsernameandRunLevel,
                       relief = 'flat')

    #entry
    entrybox = Entry(frame,
                     bd = 2)
    entrybox.var = StringVar()
    entrybox['textvariable'] = entrybox.var
    entrybox.place(x = 265,
                   y = 260,
                   anchor = 'center')

    go_button.wait_variable(entrybox.var)       #wait for variable to be updated
    go_button.place(x = 265,
                    y = 350,
                    anchor = 'center')



def getVandClose(v):
    '''Appends v (level-selectedvariable to global V list in global_variables.py to be accessed later.
    Starts up the game module and destroys the main menu window.''' 
    global_variables.V.append(v.get())    #get the level_selected variable
    connect_4_game
    display.destroy()           #necessary, or connect_4_game won't run



def guide():
    '''Creates a top window with the help guide.'''
    g_window = Toplevel(display, bg = '#d5dbe6')
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


def hScore():
    '''Calls up the scoreboard.'''
    exec(open('scoreBoard.py').read())


def exitMenu():
    quit(connect_4_game)
    display.destroy()


#-------------------------------------------------------------------------- M a i n l o o p -------------------------------------------------------------------------------------------------------    

#Creates the main window
display = Tk()
display.title("Connect Four")
display.configure(background = '#6ca2c8')

# Gets the requested values of the height and width.
window_width = display.winfo_reqwidth()
window_height = display.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
position_right = int((3 * display.winfo_screenwidth() / 8) - (window_width / 2))
position_down = int((display.winfo_screenheight() / 4) - (window_height / 2))
 
# Positions the window in the center of the page.
display.geometry("530x505+{}+{}".format(position_right, position_down))



#Displays Image in the header
logo = PhotoImage(file = 'ConnectFour.gif')
logoLabel = Label(display,
                  bg ='#6ca2c8',
                  image = logo).place(x = 265, y = 150, anchor = 'center')

#Displays Button for New Game
play = Button(display,
              text = 'New Game',
              font = ('Arial', 16),
              fg = '#3d3d3d',
              bg = '#b2c4e1',
              activebackground = '#d5dbe6',
              width = 20,
              height = 1,
              relief = 'flat',
              cursor = 'hand2',
              command = usernameEntry)
play.place(x = 265, y = 250, anchor = 'center')

#Displays button for GameGuide
guide = Button(display,
               text = 'How to Play',
               font = ('Arial', 16),
               fg = '#3d3d3d',
               bg = '#b2c4e1',
               activebackground = '#d5dbe6',
               width = 20,
               height = 1,
               relief = 'flat',
               cursor = 'hand2',
               command = guide)
guide.place(x = 265, y = 300, anchor = 'center')

#Button to check highscore
hscore = Button(display,
                text = 'High Score',
                font=('Arial', 16),
                fg = '#3d3d3d',
                bg = '#b2c4e1',
                activebackground = '#d5dbe6',
                width = 20,
                height = 1,
                relief = 'flat',
                cursor = 'hand2',
                command = hScore)
hscore.place(x = 265, y = 350, anchor = 'center')

#Button to exit game
close = Button(display,
               text = 'Exit',
               font = ('Arial', 16),
               fg = '#3d3d3d',
               bg = '#b2c4e1',
               activebackground = '#d5dbe6',
               width = 20,
               height = 1,
               relief = 'flat',
               cursor = 'hand2',
               command = exitMenu)
close.place(x = 265, y = 400, anchor = 'center')



display.mainloop()
