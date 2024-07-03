import pygame
import time
import random
import math

pygame.init()

#Size of the game area
display_width = 1700
display_height = 600

#Colors for use in backgrounds or buttons
black = (0,0,0)
white = (255,255,255)
grey = (160,160,160)
darkgrey = (80,80,80)
red = (200,0,0)
green = (0,200,0)
bred = (255,0,0)
bgreen = (0,255,0)
blue = (0,0,200)

#Main character
l_width = 20
b_width = 50
#orientation = 1.5707963268
orientation = 0
speed = 1

#Global variable with the score
score = 0

#Matematica
pi        = 3.14
grados10  = 0.17
pi180     = 57.29
grados90  = 1.57
grados180 = 3.14
grados270 = 4.71
grados360 = 6.28


#grados10  = 10
#pi180     = 57.295779514
#grados90  = 90
#grados180 = 180
#grados270 = 270
#grados360 = 360

#Start position of the character?
X = 200
Y = 400


RayEnd = [0,0]
RayStart = [0,0]
RayEnd[0] = X + 10
RayEnd[1] = Y + 10


#Map
mapa = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1],
        [1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1],
        [1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1],
        [1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#Set the size of the game area.
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Caption for the name of the Window.
pygame.display.set_caption('Lobo3D')

#The timer to make the world move
reloj = pygame.time.Clock()


#The enemies


#To exit the game.
def quitgame():
  pygame.quit()
  quit()

#Function to create buttons on screen
def button(msg,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if (x + w) > mouse[0] > x and (y+h) > mouse[1] > y:
    pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

  smalltext = pygame.font.Font('freesansbold.ttf',20)
  TextSurf, TextRect = text_objects(msg, smalltext)
  TextRect.center = ((x+(w//2)),(y+(h//2)))
  gameDisplay.blit(TextSurf, TextRect)

#Function to display the score
def scored():
  global score
  font = pygame.font.SysFont(None, 25)
  text = font.render("Last Score: "+str(score), True, black)
  gameDisplay.blit(text, (0, 0))

#Enemy on screen
#def fantasmitas(tx, ty, tw, th, tc):
#  pygame.draw.rect(gameDisplay, tc, [tx, ty, tw, th])
  #gameDisplay.blit(fantasmita,(tx,ty))


#Function to draw test
def text_objects(text,font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

#Function to display a message
def message_display(text):
  largetext = pygame.font.Font('freesansbold.ttf',115)
  TextSurf, TextRect = text_objects(text, largetext)
  TextRect.center = ((display_width//2),(display_height//2))
  gameDisplay.blit(TextSurf, TextRect)
  pygame.display.update()
#  pygame.quit()
#Wait
  time.sleep(2)

#Colisiones

def calculodireccion(X,Y,orientation):
  #Aca deberia calcular la direccion para el rayo.
  #Si la orientacion esta en RAD
  #orientagrados = orientation * pi180
  global grados90
  global grados180
  global grados270
  global grados360
  X = X+10
  Y = Y+10

  distancia = 10

  orientagrados = orientation

  if orientagrados > grados270:
    orientagrados = grados360 - orientagrados
  elif orientagrados > grados180:
    orientagrados = orientagrados - grados180
  elif orientagrados > grados90:
    orientagrados = grados180 - orientagrados


  endray = [0,0]
  print("Formula")
  print("Grados: "+str(orientagrados))
  tan = math.tan(orientagrados)
  tan = round(tan, 2)
  print("TAN: "+str(tan))
  co = (tan*distancia)
  co = round(co, 2)
  print("CO: "+str(co))


  endray[0] = distancia
  endray[1] = co

  print(endray)
  print("End Formula")
  return endray


#Game Over!
def gameover():
  global score
  message_display("Game over!" + str(score))
  game_intro()

#Intro Screen
def game_intro():
  global score
  intro = True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    gameDisplay.fill(white)
    largetext = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Lobo3D", largetext)
    TextRect.center = ((display_width//2),(display_height//2))
    gameDisplay.blit(TextSurf, TextRect)

    button("Start!",150,450,100,50,green,bgreen,game_loop)
    button("Exit",550,450,100,50,red,bred,quitgame)

    scored()

    pygame.display.update()
    reloj.tick(15)

#GameLogic
def game_loop():
  global speed
#  game_intro()
  global orientation

  global RayEnd
  global RayStart

  global X
  global Y


#The character movement
  x_change = 0
  y_change = 0

#Fantasmitas position
  f_startx = 0
  f_starty = 0
  f_speed = 3
  f_width = 80
  f_height = 80

#Upper and Left Bar.
  ub_startx = 0
  ub_starty = 0
  ub_width = display_width
  ub_height = 40
  
  lb_startx = 0
  lb_starty = 0
  lb_width = 100
  lb_height = display_height
  
#Flag to know if the game loop should exit
  gameexit = False

  collisiones = []

  down_pressed = False

  fantaspos = False
  Distancia = 0
#Armar Mapa
  for F in range(len(mapa)):
      for C in range(len(mapa[F])):
          if mapa[F][C]:
            collisiones.append(((C*50),((C*50)),(F*50),((F*50))))

#PINTAR FONDO
  gameDisplay.fill(grey)
#PINTAR Marco
  #pygame.draw.rect(gameDisplay, blue, [lb_startx, lb_starty, lb_width, lb_height])

#PINTAR MAPA
  for cuadro in collisiones:
    pygame.draw.rect(gameDisplay, red, [cuadro[0], cuadro[2], b_width, b_width])

#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
  while not gameexit:

    #Limpiar area de juego
    pygame.draw.rect(gameDisplay, grey, [0, 0, 1700, 600])
  #PINTAR MAPA
    for cuadro in collisiones:
      pygame.draw.rect(gameDisplay, red, [cuadro[0], cuadro[2], b_width, b_width])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()


      if event.type == pygame.KEYDOWN:
        #IZQUIERDA---------------------------------
        if event.key == pygame.K_LEFT:
          #down_pressed = True

          if orientation < grados360:
            orientation = orientation+grados10
            orientation = round(orientation, 2)
          else:
            orientation = 0

          #Ver la orientacion en RAD
          print("Orientacion: "+str(orientation))



          RayEnd = calculodireccion(X,Y,orientation)

          if orientation > grados90 and orientation < grados270:
            RayEnd[0] = RayStart[0]-RayEnd[0]
          else:
            RayEnd[0] = RayStart[0]+RayEnd[0]
          
          if orientation > 0 and orientation < grados180:
            RayEnd[1] = RayStart[1]-RayEnd[1]
          else:
            RayEnd[1] = RayStart[1]+RayEnd[1]
          
          print(RayEnd)
          #BUSCAR FINAL DEL RAYO

        #DERECHA---------------------------------
        elif event.key == pygame.K_RIGHT:
          #down_pressed = True

          if orientation > 0:
            orientation = orientation-grados10
            orientation = round(orientation, 2)
          else:
            orientation = grados360

          #Ver la orientacion en RAD
          print("Orientacion: "+str(orientation))


          RayEnd = calculodireccion(X,Y,orientation)

          if orientation > grados90 and orientation < grados270:
            RayEnd[0] = X-RayEnd[0]
          else:
            RayEnd[0] = X+RayEnd[0]
          
          if orientation > 0 and orientation < grados180:
            RayEnd[1] = Y-RayEnd[1]
          else:
            RayEnd[1] = Y+RayEnd[1]
          print(RayEnd)
          #BUSCAR FINAL DEL RAYO

        #ARRIBA---------------------------------
        elif event.key == pygame.K_UP:
          #down_pressed = True
          y_change = (0-speed)
          x_change = 0

        elif event.key == pygame.K_DOWN:
          #down_pressed = True
          y_change = speed
          x_change = 0


      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          #down_pressed = True
          x_change = 0
          y_change = 0
          orientation = orientation
        elif event.key == pygame.K_RIGHT:
          #down_pressed = True
          x_change = 0
          y_change = 0
          orientation = orientation
        elif event.key == pygame.K_UP:
          #down_pressed = True
          y_change = 0
          x_change = 0

        elif event.key == pygame.K_DOWN:
          #down_pressed = True
          y_change = 0
          x_change = 0




#AVOID GOING AWAY FROM PLAYING AREA
#    if (X < 100) and down_pressed and orientation == "l":
#      x_change = 0
#    if (X > (display_width - (pacq_width + 3))) and down_pressed and orientation == "r":
#      x_change = 0
#    if (Y < 40) and down_pressed and orientation == "u":
#      y_change = 0
#    if (Y > (display_height - (pacq_width + 3))) and down_pressed and orientation == "d":
#      y_change = 0

#PINTAR PRIMERO LOS CUADRADOS POR DONDE PASO EL CARACTER, Y LUEGO PINTAR TODOS LOS CARACTERES EN PANTALLA

    #Pintar sobre donde estuvieron los characters para que no dejen un trail
    #    fantasmitas(t_startx, t_starty, t_width, t_height, black)
    #pygame.draw.rect(gameDisplay, grey, [f_startx, f_starty, f_width, f_height])

    #    character(orientation,int(X),int(Y))
    pygame.draw.rect(gameDisplay, grey, [X, Y, l_width, l_width])

    pygame.draw.rect(gameDisplay, green, [X, Y, l_width, l_width])

    X += x_change
    Y += y_change
    RayStart[0] = X+10
    RayStart[1] = Y+10







    #RAYOS
    pygame.draw.line(gameDisplay, black, RayStart, RayEnd)

#LOGIC
#COLISIONES

#COLISIONES


#VIejo codigo, si el enemigo paso toda la pantalla sin chocar sumaba uno al score
#
#    if (t_starty > display_height):
#      t_starty = 0 - t_height
#      t_startx = random.randrange(150,(display_width-232))
#      score += 1


#    if (Y < (t_starty + t_height)):
#      if (X > t_startx) and (X < (t_startx + t_width)) or ((X + pacq_width) > t_startx) and ((X + pacq_width) < (t_startx + t_width)):
#        gameover()
#        time.sleep(2)
#        gameexit = True

    pygame.display.update()
    reloj.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()