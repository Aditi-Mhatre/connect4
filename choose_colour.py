from tkinter import *
import global_variables

root = Tk()
root.title('Pick a colour')
root.resizable(False, False)                #keep the the window  unresizable in both x and y directions
root.overrideredirect(1)                    #disables the window to be closed by regular means: [X]


# Gets the requested values of the height and width.
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
position_right = int((4 * root.winfo_screenwidth() / 8) - (window_width / 2))
position_down = int((root.winfo_screenheight() / 2) - (window_height / 2))
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(position_right, position_down))
 


#frames
labelframe = Frame(root,
                   height = 35,
                   width = 290,
                   bg = '#6ca2c8')
labelframe.pack()
labelframe.pack_propagate(0)                #disabling propagation keeps the frame from shrinking

buttonframe = Frame(root,
                    height = 121,
                    width = 290,
                    bg = '#6ca2c8')
buttonframe.pack(side = 'bottom')
buttonframe.grid_propagate(0) 

#labels
label = Label(labelframe,
              text = 'Which colour do you want to play as?',
              bg = '#6ca2c8',
              fg = 'white',
              font = ('Helvetica', 11, 'bold'))
label.place(x = 145,
            y = 20,
            anchor = 'center')

redtext = Label(buttonframe,
                text = 'R E D',
                bg = '#6ca2c8',
                fg = 'white',
                font = ('Verdana', 8))
redtext.place(x = 89,
              y = 100,
              anchor = 'center')

yellowtext = Label(buttonframe,
                   text = 'Y E L L O W',
                   bg = '#6ca2c8',
                   fg = 'white',
                   font = ('Verdana', 8))
yellowtext.place(x = 201,
                 y = 100,
                 anchor = 'center')

#functions
def chooseRed():
    '''Appends O/red then X/yellow to the (empty) list in the global_variables module.'''
    global_variables.global_list.append('O')
    global_variables.global_list.append('X')

def chooseYellow():
    '''Appends X/yellow then O/red to the (empty) list in the global_variables module.'''
    global_variables.global_list.append('X')
    global_variables.global_list.append('O')


def closeWindow():
    '''Close the window.'''
    root.destroy()

def redAndClose():
    chooseRed()
    closeWindow()

def yellowAndClose():
    chooseYellow()
    closeWindow()
    
#buttons
redbutton = Button(buttonframe,
                   height = 4,
                   width = 10,
                   bg = '#f32337',
                   activebackground = '#ee6f6f',
                   relief = 'flat',
                   cursor = 'hand2',
                   command = redAndClose)
redbutton.place(x = 89,
                y = 50,
                anchor = 'center')

yellowbutton = Button(buttonframe,
                      height = 4,
                      width = 10,
                      bg = '#efe21a',
                      activebackground = '#fefa85',
                      relief = 'flat',
                      cursor = 'hand2',
                      command = yellowAndClose)
yellowbutton.place(x = 201,
                   y = 50,
                   anchor = 'center')


root.mainloop()
