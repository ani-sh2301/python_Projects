import pygame
from pygame.locals import *
import random
from os.path import exists

pygame.init()

clock=pygame.time.Clock()
fps=60

window_width=864
window_height=780

window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Flappy Bird')

#define font
font=pygame.font.SysFont('Bauhaus 93',60)
#color
black=(135,135,135)
#high score font
font2=pygame.font.SysFont('Times New Roman',30)
black=(0,0,0)
font3=pygame.font.SysFont('Bauhaus 93',40)

#game variables
ground_scroll= 0
scroll_speed= 4
flying=False
game_over=False
pipe_gap=150
pipe_frequency=1500 #miliseconds
last_pipe=pygame.time.get_ticks()-pipe_frequency
score=0
file_exists = exists("highS.txt")
high_score=0
if(not file_exists):
    file_hs=open("highS.txt",'w')
    file_hs.write('0')
else: 
    file_hs=open("highS.txt",'r')
    high_score=int(file_hs.read())
file_hs.close()

pass_pipe=False


#images
bg=pygame.image.load('bk.png')
groundImg=pygame.image.load('img/ground.png')
rbutton_img=pygame.image.load('img/restart.png')

def draw_text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    window.blit(img,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x=100
    flappy.rect.y=int(window_height/2)
    high_score_update()
    global score
    score=0

def high_score_update():
    global score
    global high_score
    if score>high_score:
        high_score=score
    file_hs=open("highS.txt",'w')
    file_hs.write(str(high_score))
    file_hs.close()
    

class bird(pygame.sprite.Sprite):
    global score
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,4):
            img=pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        
        self.image= self.images[self.index]
        self.rect=self.image.get_rect() # creates an outer rectangle around the image
        self.rect.center=[x,y] 
        self.val= 0
        self.clicked=False

    def update(self):
        #gravity
        if flying==True:
            self.val+=0.5
            if self.val> 8:
                self.val=8
            if self.rect.bottom < 650:
                self.rect.y+=int(self.val)
        
        if game_over==False :
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked=True
                self.val= -8
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked=False
            
            #handle the animation
            self.counter+=1
            flap_cooldown=5

            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.images[self.index]

            #rotate
            self.image=pygame.transform.rotate(self.images[self.index],self.val*-2)

        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)   #on game over

class pipe(pygame.sprite.Sprite):

    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('img/pipe.png')
        self.rect=self.image.get_rect()

        #position 1 from top, -1 from bottom
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap/2)]
        if position==-1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]

    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()


class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=[x,y]

    def draw(self):

        action=False
        #mouse position
        pos=pygame.mouse.get_pos()
        #check mouse over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1 : #left mouse button
                action=True

        window.blit(self.image,(self.rect.x,self.rect.y))
        return action
    
bird_group=pygame.sprite.Group()
pipe_group=pygame.sprite.Group()

flappy=bird(100,int(window_height/2))
bird_group.add(flappy) #similar to list

#restart button
btn=button(window_width//2-50,window_height//2-100,rbutton_img)

run=True
while run:

    clock.tick(fps)

    #background
    window.blit(bg,(0,0))

    bird_group.draw(window)
    bird_group.update()

    pipe_group.draw(window)

    #check the score
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left >pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
             and pass_pipe==False: #within the zone
            pass_pipe=True
        if pass_pipe==True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score+=1
                pass_pipe=False

    #high score
    if game_over==False and flying==False:
        draw_text("High Score: "+str(high_score),font3,(0,200,0),int(window_width//2-110),int(window_height//2))
    elif game_over==False:
        draw_text(str(score),font,black,int(window_width/2),20)
        draw_text("High Score: "+str(high_score),font2,black,10,30)

    #collision check
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top < 0:   #killing bird_group =False, pipe_group =False.
        game_over=True

    #check ground hit
    if flappy.rect.bottom>= 650:
        game_over=True
        flying= False


    #scroll background
    window.blit(groundImg,(ground_scroll,650))
    if game_over==False:

        if flying==True:
        #generate new pipes
            time_now=pygame.time.get_ticks()
            if time_now-last_pipe > pipe_frequency:
                pipe_height=random.randint(-100,100)
                btm_pipe=pipe(window_width,int(window_height/2)+pipe_height,-1)
                top_pipe=pipe(window_width,int(window_height/2)+pipe_height,1)

                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe=time_now

        ground_scroll-=scroll_speed
        if abs(ground_scroll)>34:
            ground_scroll=0
        pipe_group.update()
        

    if game_over==True:
        #display high score
        high_score_update()
        draw_text("High Score: "+str(high_score),font2,black,int(window_width//2-65),int(window_height/2))
        if btn.draw()==True:
            game_over=False
            reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #window cross icon
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True

    pygame.display.update()

pygame.quit()