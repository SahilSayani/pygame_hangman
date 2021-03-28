import pygame
import math
import random
#setup display    
pygame.init()#initializes all imported pygame modules
WIDTH,HEIGHT=800,500
win=pygame.display.set_mode((WIDTH,HEIGHT)) #set display area size 
pygame.display.set_caption("HANGMAN MINI PROJECT")

#button variables          EXPERIMENT AND CLARIFY
RADIUS=20
GAP=15
A=65      # ascii
letters=[]#[x,y,letter,bool] storing a quadruplet... the bool tells whether button has been clicked or not
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2) #aligns buttons perfectly in x 
starty=400
for i in range(26):#determine x and y pos of each button (X AND Y ARE CENTERES OF BUTTON)
  x=startx + GAP*2 +((RADIUS*2 + GAP)*(i%13)) #expt with gap*2 here OffsetVal
  y=starty + ((i//13) * (GAP+RADIUS* 2))
  letters.append([x,y,chr(A+i),True])

#fonts 
LETTER_FONT=pygame.font.SysFont('comicsans',40)
WORD_FONT=pygame.font.SysFont('comicsans',60)
TITLE_FONT=pygame.font.SysFont('comicsans',70)
#load images
images=[]
for i in range (7):
  image=pygame.image.load(".//sprites//hangman"+str(i)+".png")#.//folder/file helps access the sprites folder
  images.append(image)


#setup game variables
hangman_status=0 # tells us which image we wanna draw on the output screen
words=["SAHIL","PYTHON","APEKSHA","KARTIKA","SWARANGI","UMAIMA","YASH","AISHWARYA","HRISHIK","PYGAME","ENGINEER","PROGRAM","ASSIGNMENT","JAY","GAURAV","AANCHAL"]
WORD=random.choice(words) #keyword
guessed=[] #repr. letters guessed by the user so far

#colors
SILVER=(192,192,192)#tuple RGB
BLACK=(0,0,0)
#setup game loop
FPS=60
clock=pygame.time.Clock() #clock obj counts 60fps and keeps track of time
run=True

def draw():
  win.fill(SILVER)    #fill RGB value in screen min0 max255 silver(192,192,192)
  #draw TITLE
  text=TITLE_FONT.render("HANGMAN by Sahil Sayani",1,BLACK)
  win.blit(text,(WIDTH/2-text.get_width()/2,20))
  #draw word (blanks and guessed)
  display_word=""
  for letter in WORD:
    if letter in guessed:
      display_word += letter + ' '
    else:
      display_word+="_ " 
  text=WORD_FONT.render(display_word,1,BLACK)
  win.blit(text,(400,200))
  #draw buttons
  for letter in letters:
    x,y,ltr,visible=letter   #splitting up list of 4  [x,y,letter,visible]
    if visible:
      pygame.draw.circle(win,BLACK,(x,y),RADIUS,3) # 3IS THE PIXEL WIDTH OF OUTLINE 
      text=LETTER_FONT.render(ltr,1,BLACK)
      win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    
  win.blit(images[hangman_status],(150,100))# blit stands for draw image or a "surface" // render obj on a surface // the tuple shows position where to draw the image // parameter list (sorce,destination)

  pygame.display.update()

def display_message(message):
    pygame.time.delay(1000*2)#delay for 2 sec to see hangman 
    win.fill(SILVER)
    text=WORD_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2) )
    pygame.display.update()
    pygame.time.delay(5000) #delay for 5 secs


while run:
  clock.tick(FPS)#makes while loop run at the speed we set up in line 9

  #draw() shifted to bottom so all limbs of hangman can be seen if lost .......SO FIRST WE UPDATE SCREEN BY DRAW() AND THEN CHECK WIN OR LOST CONDITIONS

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False
    if event.type== pygame.MOUSEBUTTONDOWN:
      #pos=pygame.mouse.get_pos()
      #print(pos)
      m_x,m_y=pygame.mouse.get_pos() #get x y coordinate and check for collision with buttons
      for letter in letters:
         x,y,ltr,visible=letter #create simillar local var in main
         if visible:
           distance=math.sqrt((x-m_x)**2+(y-m_y)**2) #calc dist between mouse click x and y and center of button x and y and check if that distance is less than the radius for button press
           if distance<RADIUS:   #CHECK FOR COLLISION/BUTTON PRESS
             #print(ltr)
             letter[3]=False #makes the buttons pop / become invisible ie:guessed already
             guessed.append(ltr)
             if ltr not in WORD:
               hangman_status+=1
  draw()             
  won=True
  for letter in WORD:          #we loop thru all letters in keyword
    if letter not in guessed:  #if our letter is not in gussed list we set won=false and break
      won=False 
      break
  
  if won:
    #print("won")
    display_message("you WON!")
    break #break out of the main game loop (WHILE RUN)
  if hangman_status==6:
    #print("lost")  
    display_message("SORRY! you LOST" + " ("+WORD+") ")
    break
pygame.quit()
