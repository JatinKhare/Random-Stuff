import pygame
import time
from pygame.locals import *

pygame.init()

# Grid to check the what has been filled where:

grid = [[None,None,None],[None,None,None],[None,None,None]]
win  = None

# Game Variable, will change with each turn. Initiated with X.

var = 'X'

# Declaration of required Parameters

width = 600
height = 600
black = (0,0,0)
white = (255,255,255)
game_display = pygame.display.set_mode((width,height)) 
pygame.display.set_caption('Tic Tac Toe')

# Loading images

o_icon = pygame.image.load('o1.png')
x_icon = pygame.image.load('x1.png')

# Functions

# Writing Text

def text_objects(text,font):

	textSurface = font.render(text,True,white)
	return textSurface, textSurface.get_rect()

def game_winner(win):

	text = 'PLAYER WITH {} HAS WON!'.format(win)
	largeText = pygame.font.Font('freesansbold.ttf',40)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (width/2,height/2)
	game_display.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	
#Checking if someone has won or not. Tie will be added soon, along with a menu interface.

def check_win():

	global grid, win
	for r in range (0, 3):
		if ((grid [r][0] == grid[r][1] == grid[r][2]) and (grid [r][0] is not None)):
			win = grid[r][0]
			game_winner(win)
			break
	for c in range (0, 3):
		if ((grid [0][c] == grid[1][c] == grid[2][c]) and (grid [0][c] is not None)):
			win = grid[0][c]
			game_winner(win)
			break
	if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
		win = grid[0][0]
		game_winner(win)
	if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
		win = grid[0][2]
		game_winner(win)
		
# To get the row and column position according to where the player has clicked.

def click_position(x,y):

    if y < 200:
        r = 0
    elif y < 400:
        r = 1
    else:
        r = 2
    if x < 200:
        c = 0
    elif x < 400:
        c = 1
    else:
        c = 2
    return (r,c)

#Adding icons at the places where the player has clicked.

def add_image(r,c,var,game_display):

	cx = (c*200) + 50
	cy = (r*200) + 50
	if var == 'O':
		game_display.blit(o_icon,(cx,cy))
	else:
		game_display.blit(x_icon,(cx,cy))
	pygame.display.update()
	grid[r][c] = var

# Updating the board after every turn.

def update_board(game_display):
	
	global var, grid
	(x,y) = pygame.mouse.get_pos()
	(r,c) = click_position(x,y)
	if (grid[r][c] == 'X') or (grid[r][c] == 'O'):
		return 
	add_image(r,c,var,game_display)
	if var == 'X':
		var = 'O'
	else:
		var = 'X'

# Driver Function
exit = False

while not exit:
	for event in pygame.event.get(): 
	    if event.type == pygame.QUIT:
	        exit = True
	    elif event.type is MOUSEBUTTONDOWN:
	    	update_board(game_display)
	check_win()

pygame.quit()
