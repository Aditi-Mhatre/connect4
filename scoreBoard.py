'''Importing'''
# file_read.py
import easy_file_read as efr
import advanced_file_read as afr

# tkinter library
import tkinter as tk
import tkinter.ttk as ttk

global change_diff, diff_button, contents_afr, contents_efr, tree      #globalise these names so that this file can run properly from main_menu




'''Defining functions'''
# deletes all items in tree, then adds different difficulty
def change_diff():
    if diff_button["text"] == "Normal":
        diff_button["text"] = "Advanced"
        for i in tree.get_children():
            tree.delete(i)
        for i in range(len(contents_afr)):
             # changed this part to fix rank not showing up
            tree.insert("", i, values=(i+1, contents_afr[i][0], contents_afr[i][1]))

    else:
        diff_button["text"] = "Normal"
        for i in tree.get_children():
            tree.delete(i)
        for i in range(len(contents_efr)):
            # changed this part to fix rank not showing up
            tree.insert("", i, values=(i+1, contents_efr[i][0], contents_efr[i][1]))


##def reset_board():
##    '''Clear the board except for Creatorrrr's score, by overwriting the scorefiles.'''
##    if diff_button["text"] == "Normal":
##        f = open("easy_mode.txt", "w")
##    else:
##        f = open("advanced_mode.txt", "w")
##        
##    f.write('Creatorrrr\t100\n')
##    f.close()
##    tree_frame.destroy()
##    createTreeView
##    return


'''Variables'''
# file_read.py
contents_efr = efr.contents # easy_mode.txt contents
contents_afr = afr.contents # advanced_mode.txt contents
contents = contents_efr # Initial contents as easy_mode.txt contents

#------Tkinter-----------------------------------------------------------------------------------------
# Window
root = tk.Tk() # Parent window
root.resizable(False, False) # Disables resizing
# Gets the requested values of the height and width.
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
position_right = int((3 * root.winfo_screenwidth() / 8) - (window_width / 2))
position_down = int((root.winfo_screenheight() / 4) - (window_height / 2))
 
# Positions the window in the center of the page.
root.geometry("530x505+{}+{}".format(position_right, position_down))

# Frames
color = '#6ca2c8' # Color of frames
# Main frame
Width = 530
Height = 505


'''Widgets'''
#-----STYLING---------------------------------------------------------------------
style = ttk.Style()
style.configure('BW.TLabel', font = ('Arial', 10), foreground= '#3d3d3d',background='#d5dbe6')
style.configure("BW.TLabel.Heading", font=('Calibri', 13,'bold'), background='green', foreground='red') # Modify the font of the headings

#-----Main frame---------------------------------------------------------------------------
main_frame = tk.Frame(root, bg = color)
main_frame.place(anchor='center', relx=0.5, rely=0.5, width=Width, height=Height)

#-----Top label-------------------------------------------------------------------------------
# Frame
top_label_frame = tk.Frame(main_frame, bg=color, height = 45, width = 185)
top_label_frame.pack_propagate(0)
top_label_frame.place(x = (Width/2), y = 45, anchor = 'center')

# Label
top_label = tk.Label(top_label_frame, text="Score Board", bg=color, fg ='white', font=("Arial", 25), anchor = 'n')
top_label.pack()


#----Difficulty label and button-------------------------------------------------------------------
# Frame
diff_frame = tk.Frame(main_frame, bg=color)
diff_frame.place(x = (Width/2), y = 105, anchor = 'center')

# Label
diff_label = tk.Label(diff_frame, text="Difficulty:",font=("Arial", 10, 'italic'), fg ='white', bg=color)
diff_label.grid(row = 0, column = 0)

# Button
diff_button = tk.Button(diff_frame, text="Normal", font = ('Arial', 12), fg = '#3d3d3d', bg = '#b2c4e1', activebackground = '#d5dbe6',
                        width = 9, height = 1, cursor = 'hand2', relief = 'flat', command=change_diff)
diff_button.grid(row = 0, column = 1, padx = 5)


#----TreeView-----------------------------------------------------------------------------

# Frame
tree_frame = tk.Frame(main_frame, bg=color, height = 320, width = 390)
tree_frame.place(x = (Width/2), y = (Height/2)+50, anchor = 'center')
tree_frame.pack_propagate(0)

# tree
tree = ttk.Treeview(tree_frame, height = 35, style='BW.TLabel') # Included style

# Creates new columns in addition to column #0
tree["columns"] = ("one", "two", 'three')

# Sets size of columns
tree.column("#0", width=0, stretch=tk.NO)
tree.column("one", width=50, stretch=tk.NO)
tree.column("two", width=200, stretch=tk.NO)
tree.column("three", width=120, stretch=tk.NO)

# Heading of columns
tree.heading("#0", text="")
tree.heading("one", text="Rank")
tree.heading("two", text="Name")
tree.heading("three", text="Score")

# Inserts names and scores in columns
for i in range(len(contents)):
    tree.insert("", i, values=(str(i+1), contents[i][0], contents[i][1]))#,tags=('ttk', 'simple'))
##tree.tag_configure('simple', font = ('Arial', 10), foreground= '#3d3d3d',background='#d5dbe6')

# Packs tree
tree.pack(side='left', fill='y')

# Scrollbar
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y') # places scrollbar on right side
tree.configure(yscrollcommand=vsb.set)



###-----Back button------------------------------------------------------------------------
### Frame
##back_button_frame = tk.Frame(main_frame, bg=color, height = 45, width = 185)
##back_button_frame.place(x = (Width/2), y = 450, anchor = 'center')
##back_button_frame.pack_propagate(0)
##
##'''NO COMMAND SET YET'''
### Button
##back_button = tk.Button(back_button_frame, text="Reset Board", font = ('Arial', 14), fg = '#3d3d3d', bg = '#b2c4e1', activebackground = '#d5dbe6',
##                        width = 10, height = 1, cursor = 'hand2', relief = 'flat', command=reset_board)
##back_button.pack()

#------------------------------------------------------------------------------------------


root.mainloop()
