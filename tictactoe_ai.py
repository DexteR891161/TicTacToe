import pygame
import numpy as np
import time
from math import inf as infinity

pygame.init()

win=pygame.display.set_mode((450,360))
pygame.display.set_caption('TIC TAC TOE')

data=[0,0,0,0,0,0,0,0,0]

def get_empty(board):
    pos=[]
    for i,char in enumerate(board):
        if char==0:
            pos.append(i)
    return pos

def draw_board():
    pygame.draw.line(win,(255,255,255),(200,100),(200,250),3)
    pygame.draw.line(win,(255,255,255),(250,100),(250,250),3)
    pygame.draw.line(win,(255,255,255),(150,150),(300,150),3)
    pygame.draw.line(win,(255,255,255),(150,200),(300,200),3)

font = pygame.font.SysFont('comicsans',40,1)

def draw_X(Xx,Xy):
    X = font.render('X',1,(255,0,0))
    win.blit(X,(Xx,Xy))

def draw_O(Ox,Oy):
    O = font.render('O',1,(0,255,0))
    win.blit(O,(Ox,Oy))

def Xturn(turn):
    if turn==0:
        return True
    return False

def Oturn(turn):
    if turn==1:
        return True
    return False

def GetWin(inp):
    if(inp[0]==inp[1]==inp[2]=='O')or(inp[3]==inp[4]==inp[5]=='O')or(inp[6]==inp[7]==inp[8]=='O'):
        return True,1
    elif(inp[0]==inp[1]==inp[2]=='X')or(inp[3]==inp[4]==inp[5]=='X')or(inp[6]==inp[7]==inp[8]=='X'):
        return True,-1

    elif(inp[0]==inp[3]==inp[6]=='O')or(inp[1]==inp[4]==inp[7]=='O')or(inp[2]==inp[5]==inp[8]=='O'):
        return True,1
    elif(inp[0]==inp[3]==inp[6]=='X')or(inp[1]==inp[4]==inp[7]=='X')or(inp[2]==inp[5]==inp[8]=='X'):
        return True,-1

    elif(inp[0]==inp[4]==inp[8]=='O')or(inp[2]==inp[4]==inp[6]=='O'):
        return True,1
    elif(inp[0]==inp[4]==inp[8]=='X')or(inp[2]==inp[4]==inp[6]=='X'):
        return True,-1

    elif 0 not in inp:
        return True,0
    else:
        return False,None

def evaluate(state):
    ret,reward=GetWin(state)
    return reward

#HUMAN=-1   Player1  X
#AI=1       Player2  O

def minimax(state,turn):
    if turn==1:
        best=[-1,-infinity]
    else:
        best=[-1,infinity]

    if GetWin(state)[0]:
        return [-1,evaluate(state)]

    for pos in get_empty(state):
        if turn==-1:
            state[pos]='X'
        elif turn==1:
            state[pos]='O'

        score=minimax(state,-turn)
        state[pos]=0
        score[0]=pos
        if turn==1:
            if score[1]>best[1]:
                best=score
        else:
            if score[1]<best[1]:
                best=score
    return best


turn = 0
run = True

#Main Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if turn==0:
        key=pygame.mouse.get_pressed()
        x,y=pygame.mouse.get_pos()
    else:
        key=pygame.mouse.get_pressed()
        point=minimax(data.copy(),1)[0]
        print(point)
        if point==0:
            x,y=165,115
        elif point==1:
            x,y=215,115
        elif point==2:
            x,y=265,115
        elif point==3:
            x,y=165,165
        elif point==4:
            x,y=215,165
        elif point==5:
            x,y=265,165
        elif point==6:
            x,y=165,215
        elif point==7:
            x,y=215,215
        elif point==8:
            x,y=265,215
    #win.fill((0,0,0))
    if key[0]:
        if x>150 and y>100 and x<200 and y<150 and not(data[0]=='X' or data[0]=='O'):
            if Xturn(turn):
                draw_X(165,115)
                turn=1
                data[0]='X'
            elif Oturn(turn):
                draw_O(165,115)
                turn=0
                data[0]='O'
        if x>200 and y>100 and x<250 and y<150 and not(data[1]=='X' or data[1]=='O'):
            if Xturn(turn):
                draw_X(215,115)
                turn=1
                data[1]='X'
            elif Oturn(turn):
                draw_O(215,115)
                turn=0
                data[1]='O'
        if x>250 and y>100 and x<300 and y<150 and not(data[2]=='X' or data[2]=='O'):
            if Xturn(turn):
                draw_X(265,115)
                turn=1
                data[2]='X'
            elif Oturn(turn):
                draw_O(265,115)
                turn=0
                data[2]='O'
        if x>150 and y>150 and x<200 and y<200 and not(data[3]=='X' or data[3]=='O'):
            if Xturn(turn):
                draw_X(165,165)
                turn=1
                data[3]='X'
            elif Oturn(turn):
                draw_O(165,165)
                turn=0
                data[3]='O'
        if x>200 and y>150 and x<250 and y<200 and not(data[4]=='X' or data[4]=='O'):
            if Xturn(turn):
                draw_X(215,165)
                turn=1
                data[4]='X'
            elif Oturn(turn):
                draw_O(215,165)
                turn=0
                data[4]='O'
        if x>250 and y>150 and x<300 and y<200 and not(data[5]=='X' or data[5]=='O'):
            if Xturn(turn):
                draw_X(265,165)
                turn=1
                data[5]='X'
            elif Oturn(turn):
                draw_O(265,165)
                turn=0
                data[5]='O'
        if x>150 and y>200 and x<200 and y<250 and not(data[6]=='X' or data[6]=='O'):
            if Xturn(turn):
                draw_X(165,215)
                turn=1
                data[6]='X'
            elif Oturn(turn):
                draw_O(165,215)
                turn=0
                data[6]='O'
        if x>200 and y>200 and x<250 and y<250 and not(data[7]=='X' or data[7]=='O'):
            if Xturn(turn):
                draw_X(215,215)
                turn=1
                data[7]='X'
            elif Oturn(turn):
                draw_O(215,215)
                turn=0
                data[7]='O'
        if x>250 and y>200 and x<300 and y<250 and not(data[8]=='X' or data[8]=='O'):
            if Xturn(turn):
                draw_X(265,215)
                turn=1
                data[8]='X'
            elif Oturn(turn):
                draw_O(265,215)
                turn=0
                data[8]='O'
    draw_board()
    #print(get_empty(data))
    result,_=GetWin(data)
    if result:
        if _==-1:
            print("X Wins")
        elif _==1:
            print("O Wins")
        else:
            print("Its a Draw")
        run=False
    pygame.display.update()
time.sleep(2)
pygame.quit()
