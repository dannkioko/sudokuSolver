def solve():
	m = getInitialValues()
	printSudoku(m)
	if(solveSudoku(m)): 
		printSudoku(m) 
	else: 
		print ("No solution exists")

def printSudoku(sudoku):
    print("       Sudoku ")
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
	# Insert sudoku rows 
	sudoku = [[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]]
	if(solveSudoku(sudoku)): 
		printSudoku(sudoku) 
	else: 
		print ("No solution exists")
