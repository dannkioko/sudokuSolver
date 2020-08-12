import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Sudoku solver")

nums = []
def createSudoku():
    x=0
    while x<3:
        y=0
        while y<3:
            minFrame = ttk.LabelFrame(frame, text="")
            minFrame.grid(column=y, row=x)
            j=0
            box = [[0,0,0], # a 3*3 box
            [0,0,0],
            [0,0,0]]
            while j<3:
                i=0
                while i<3:
                    box[j][i] = tk.StringVar()
                    num_in = ttk.Entry(minFrame, width=5, textvariable=box[j][i])
                    num_in.grid(column=i,row=j)
                    i=i+1
                j=j+1
            nums.append(box)
            y=y+1
        x=x+1
def setValues():
    pass    

def click():
    k=[]
    x=0
    for i in range(9):
        if (i==0 or i==3 or i==6):
            for j in range(3):
                k.append(nums[i][j])
        if (i==1 or i ==2):
            for j in range(3):
                for m in range(3):
                    k[j].append(nums[i][j][m])
        if (i==4 or i==5):
            for j in range(3):
                for m in range(3):
                    k[j+3].append(nums[i][j][m])
        if  (i==7 or i ==8):
            for j in range(3):
                for m in range(3):
                    k[j+6].append(nums[i][j][m])
    for i in k:
        for a in i: 
            print(a.get(), end="")
        print()


frame = ttk.LabelFrame(win, text="Sudoku")
frame.grid(column=0, row=0)
createSudoku()
action = ttk.Button(win, text="Solve", command=click)
action.grid(column=10, row=0)
win.mainloop()