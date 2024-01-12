#Shiyam Vasanthan

#Welcome to tic tac toe, you are circle, cpu is X, circle goes first
import pygame
import random 

pygame.init()

#Set up game window
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
window.fill((255, 255, 255))

#Game colours
white = (255, 255, 255)
black = (0, 0, 0)

#Number of rows and columns
row = 3
column = 3

#Game Font
arial = pygame.font.SysFont('Arial Bold', 100)

#Draws the tic tac toe grid
def draw_grid():
	pygame.draw.line(window, black, (200, 0), (200, 600), 10)
	pygame.draw.line(window, black, (400, 0), (400, 600), 10)
	
	pygame.draw.line(window, black, (0, 200), (600, 200), 10)
	pygame.draw.line(window, black, (0, 400), (600, 400), 10)

#Creates a 3 by 3 two dimensional grid filled with zeros, 0 represents empty space on grid, returns the 2d list
def create_grid():
	grid = []
	for r in range(row):
		grid.append([])
		for c in range(column):
			grid[r].append(0)
	return grid
	
#Draws the end screen, takes who won as a string as the argument	
def end_screen(winner):
	pygame.draw.rect(window, white, (0, 0, 600, 600))
	win = arial.render(winner + " Wins!", False, black)
	if winner == "Circle":
		window.blit(win, (95, 245))
	elif winner == "X":
		window.blit(win, (160, 245))
	elif winner == "No One":
		window.blit(win, (80, 245))
	pygame.display.update()
	pygame.time.delay(1000)

#Sets the values on the grid to the placeholder where 1 represents circle, and 2 represents X
def set_value(grid, row, column, placeholder):
	grid[row][column] = placeholder

#Checks to see if there's an empty space on the grid, return True if there is
def empty_space(grid, row, column):
	if grid[row][column] == 0:
		return True 	

#Checks to see if someone wins, takes the grid and the placeholder value as arguements, returns true if someone wins
def winning_condition(grid, placeholder):
	#Vertical winning conditions: Every column can win so range(3), must be row 0, 1, and 2 in the same column
	for c in range(3):
		for r in range(1):
			if grid[r][c] == placeholder and grid[r+1][c] == placeholder and grid[r+2][c] == placeholder:
				return True
				
	#Horizontal winning conditions: Every row can win so range(3), must be column 0, 1, and 2 in the same row
	for c in range(1):
		for r in range(3):
			if grid[r][c] == placeholder and grid[r][c+1] == placeholder and grid[r][c+2] == placeholder:
				return True
		
	#Positive Slope Diagonal: Must be (row 2, column 0) and (row 1, column 1) and (row 0, column 2)
	for c in range(1):
		for r in range(1):
			if grid[r+2][c] == placeholder and grid[r+1][c+1] == placeholder and grid[r][c+2] == placeholder:
				return True
			
	#Negative slope diagonal: Must be (row 0, column 0) and (row 1, column 1) and (row 2, column 2)
	for c in range(1):
		for r in range(1):
			if grid[r][c] == placeholder and grid[r+1][c+1] == placeholder and grid[r+2][c+2] == placeholder:
				return True

#Make variable called grid, let it store the game grid
grid = create_grid()

#Draw the tic tac toe grid
draw_grid()

#Main function
def main():
	while True:	
		#Updates the display of the game, must be at the top of the while loop, so the game piece will be shown before going to end screen
		pygame.display.update()
	
		#List that checks to see if the grid is full and the game is a tie 
		tie = []
		
		#If a space on the game board is full add 1 to the list, otherwise skip through one iteration of the loop
		#If the length of list 'tie' is 9, that means that the entire game board is full
		for r in range(3):
			for c in range(3):
				if empty_space(grid, r, c):
					continue		
				else:
					tie.append(1)

		#Checks to see if circle wins
		if winning_condition(grid, 1):
			pygame.time.delay(1000)
			end_screen("Circle")
			break
		#Checks to see if X wins
		elif winning_condition(grid, 2):
			pygame.time.delay(1000)
			end_screen("X")
			break
		#Check to see if the entire grid is filled up and no one won, if it is, the game is a tie	
		elif len(tie) == 9 and (winning_condition(grid, 1) != True) and (winning_condition(grid, 2) != True):
			pygame.time.delay(1000)
			end_screen("No One")
			break	
			
		#List used to store which row and column pairs on the grid that are still empty
		#Cannot use empty_cpu list to check for ties because it only checks when the mouse is clicked
		empty_cpu = []
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				#Get the x and y coordinates where the user clicked the screen, floor divide it by size of one space on the grid to get the value of the row and column number 
				column = event.pos[0]//200
				row = event.pos[1]//200
				
				#Only if the user clicks where a space is empty
				if empty_space(grid, row, column):
					#Draw a circle on the space they clicked
					pygame.draw.circle(window, black, (column*200 + 100, row*200 + 100), 60, 10)
					
					#Set the value of the space on the grid to 1 (representing circle)
					set_value(grid, row, column, 1)
				
					#Determine which row and column pairs on the grid are still empty
					for r in range(3):
						for c in range(3):
							if empty_space(grid, r, c):
								empty_cpu.append([r, c])
					
					#If the number of empty spaces on the grid is greater than or equal to 1, randomly select one of the remaining empty spaces for the cpu
					if len(empty_cpu) >= 1:		
						random_cpu = random.choice(empty_cpu)
						#Assign the row and the column of the empty space to the cpu 'X'
						cpu_row = random_cpu[0]
						cpu_column = random_cpu[1]
						
					#If circle hasn't won, randomly draw an X	
					if winning_condition(grid, 1) != True:
						#Randomly draw an X where the space is empty			
						pygame.draw.line(window, black, (cpu_column*200 + 40, cpu_row*200 + 40), (cpu_column*200 + 160, cpu_row*200 + 160), 10)
						pygame.draw.line(window, black, (cpu_column*200 + 40, cpu_row*200 + 160), (cpu_column*200 + 160, cpu_row*200 + 40), 10)
						#Set the value of the space on the grid to 2 (representing X)
						set_value(grid, cpu_row, cpu_column, 2)

#Call the main function				
main()
