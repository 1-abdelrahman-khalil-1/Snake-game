import pygame
import random
import time
pygame.init()
window = pygame.display.set_mode( (1000,600 ))
pygame.mouse.set_cursor(0)
food = [ 120 ,  105]
x,y=60,105
snake_body = [
    [x,y],
    [x-15 , y] ,
    [x-30 , y]
]
point = 0
direction = "" 
def show_score( font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f"POINTS : {point}", True, (255, 0, 0))
    rec = pygame.Surface.get_rect(score_surface)
    window.blit(score_surface, rec)
    
def losing( x, y ):  
     eatitself = False
     for i in range(0, len(snake_body)):
          if [x, y] == snake_body[i] and direction != "":
              eatitself = True
    #    (if i want to lose when moving in wall just incomment it)           
    #   if x == 600 or y == 600 or y < 0 or x < 0 :
     if eatitself :
          PRint = pygame.font.SysFont( "Chiller" , 80 )
          game_over = PRint.render("Game Over"  , False, (210, 69, 69) ,  (255,255,255))
          game_over1 = PRint.render( f"Your Points = {point}" , True, (210, 69, 69) , (255,255,255))
          window.blit(game_over1 , (100,290))
          window.blit(game_over , (150,200)) 
          pygame.display.update()
          time.sleep(2.5)
          quit()
           
          
speed , check ,pause = 90 , 100 , 0
#im = pygame.image.load("lolo.jpg")
while True:
        
     if point >= check and speed != 30:
      speed -= 20
      check += 50
     pygame.time.delay(speed)
     for i in pygame.event.get():
         if i.type == pygame.QUIT :
             pygame.quit()
             quit()
         if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_p:
                   if pause == 0 : pause = 1 
                   else: pause = 0
                        
     if pause == True:
         continue       
     newkey = pygame.key.get_pressed() 
     if newkey[pygame.K_n]: speed += 20 
     elif newkey[pygame.K_m] : speed -= 20 
 
     new_head = [snake_body[0][0] , snake_body[0][1]]
     if newkey[pygame.K_ESCAPE]:
         quit()
     if ( newkey[pygame.K_w] or newkey[pygame.K_UP]) and direction != "down":
         new_head[1]-= 15
         direction = "up"
     elif (newkey[pygame.K_s] or newkey[pygame.K_DOWN]) and direction != "up":
         new_head[1]+= 15
         direction = "down"
     elif (newkey[pygame.K_a] or newkey[pygame.K_LEFT]) and direction !=  "right"and direction!="":
         new_head[0]-= 15
         direction = "left"
     elif (newkey[pygame.K_d] or newkey[pygame.K_RIGHT]) and  direction != "left" :
         new_head[0]+= 15
         direction = "right"
     else :
         if direction == "up" :
             new_head[1] -= 15
         elif direction == "down" :
             new_head[1] += 15
         elif direction == "left" :
             new_head[0] -= 15
         elif direction == "right" :
             new_head[0] += 15          
     
    
     window.fill((127,199,217))
    
     if new_head[0] >= 1000:
        new_head[0] = 0
        
     elif new_head[0] < 0:
        new_head[0] = 985
        
     elif new_head[1] >= 600  :
        new_head[1] = 0
        
     elif new_head[1] < 0 :
        new_head[1] = 585  
     losing(new_head[0] , new_head[1])    
     if direction != "" : 
         snake_body.insert(0, new_head) 
         if (food[0] == new_head[0] and food[1] == new_head[1] ):
          food = [ random.randrange(1 , 985//15 )*15 , random.randrange(1,585//15)*15 ]   
          point+=10 
         elif direction != "":    
           snake_body.pop()
     pygame.draw.rect(window, (255,0,0), pygame.Rect(snake_body[0][0], snake_body[0][1], 15, 15))         
     for pos in range(1, len(snake_body)):
        pygame.draw.rect(window, (0,0,255), pygame.Rect(snake_body[pos][0], snake_body[pos][1], 15, 15)) 
     pygame.draw.rect(window , (135, 169, 34) , pygame.Rect(food[0] , food[1] , 15,15))
     
     show_score( 'Algerian', 20 )
     
     
     pygame.display.update()
     
