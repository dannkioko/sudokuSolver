import tkinter as tk
from tkinter import ttk


nums=[]
def createGUI():
	win = tk.Tk()
	win.title("Sudoku solver")
	frame = ttk.LabelFrame(win, text="Sudoku")
	frame.grid(column=0, row=0)
	action = ttk.Button(win, text="Solve", command=solve)
	action.grid(column=10, row=0)
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
	win.mainloop()
def getInitialValues():
	k=[]
	x=0
	for i in range(9):
		if (i==0 or i==3 or i==6):
			for j in range(3):
				n = []
				for m in range(3):
					if nums[i][j][m].get()=="":
						n.append(0)
					else:
						n.append(nums[i][j][m].get())
				k.append(n)
		if (i==1 or i ==2):
			for j in range(3):
				for m in range(3):
					if nums[i][j][m].get()=="":
						k[j].append(0)
					else:
						k[j].append(nums[i][j][m].get())
		if (i==4 or i==5):
			for j in range(3):
				for m in range(3):
					if nums[i][j][m].get()=="":
						k[j+3].append(0)
					else:
						k[j+3].append(nums[i][j][m].get())
		if  (i==7 or i ==8):
			for j in range(3):
				for m in range(3):
					if nums[i][j][m].get()=="":
						k[j+6].append(0)
					else:
						k[j+6].append(nums[i][j][m].get())
	return k

def solve():
	m = getInitialValues()
	printSudoku(m)
	if(solveSudoku(m)): 
		printSudoku(m) 
	else: 
		print ("No solution exists")

def printSudoku(sudoku):
    print("     Sudoku /n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)

def findEmptyCells(arr, l): 
	for row in range(9): 
		for col in range(9): 
			if(arr[row][col]== 0): 
				l[0]= row 
				l[1]= col 
				return True
	return False

def checkRow(arr, row, num): 
	for i in range(9): 
		if(arr[row][i] == num): 
			return True
	return False
 
def checkColumn(arr, col, num): 
	for i in range(9): 
		if(arr[i][col] == num): 
			return True
	return False

def checkBox(arr, row, col, num): 
	for i in range(3): 
		for j in range(3): 
			if(arr[i + row][j + col] == num): 
				return True
	return False

def checkIfSafe(arr, row, col, num): 

	return not checkRow(arr, row, num) and not checkColumn(arr, col, num) and not checkBox(arr, row - row % 3, col - col % 3, num) 

def solveSudoku(arr):  
	l =[0, 0] 
	if(not findEmptyCells(arr, l)): 
		return True
	row = l[0] 
	col = l[1] 
	for num in range(1, 10): 
		if(checkIfSafe(arr, row, col, num)): 
			arr[row][col]= num 
			if(solveSudoku(arr)): 
				return True
			arr[row][col] = 0
	return False

if __name__=="__main__": 
	createGUI()
	# if(solveSudoku(sudoku)): 
	# 	printSudoku(sudoku) 
	# else: 
	# 	print ("No solution exists")
