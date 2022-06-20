#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
 
import pygame
import pygame, os

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
PANEL_width,PANEL_highly = info.current_w,info.current_h

FONT_PX = 2#15
 
pygame.init()
 
# Создать окно но
winSur = pygame.display.set_mode((PANEL_width, PANEL_highly))
 
font = pygame.font.SysFont("123.ttf", 25)
 
bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)
 
pygame.Surface.convert(bg_suface)
 
bg_suface.fill(pygame.Color(0, 0, 0, 28))
 
winSur.fill((0, 0, 0))
 
 # Цифровая версия
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
 
 # Письменная версия
letter = ['q', 'w', '1', 'e', '9', 'r', 't', '2','y', 'u', 'i', '3', 'o', 'p', 'a', 's', '4', 
          'd', 'f', '0', 'g', 'h', '5', 'j', 'k', 'l', '6', 'z', 'x', 'c', '7','v', 'b', 'n', '8','m']
texts = [
    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(36)
]
 
 # В соответствии с расчетом широкополосного доступа на экране, вы можете поместить несколько столбцов координат на монтажной панели и создать список
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]
 
while True:
         # Получить события из очереди
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
 
            chang = pygame.key.get_pressed()
            if(chang[32]):
                exit()
 
         # Приостановится на указанное количество миллисекунд
    pygame.time.delay(30)
 
         # Повторно отредактируйте изображение. Второй параметр - сидеть на угловых координатах.
    winSur.blit(bg_suface, (0, 0))
 
    for i in range(len(drops)):
        text = random.choice(texts)
 
                 # Повторно отредактируйте изображение каждой координатной точки
        winSur.blit(text, (i * (FONT_PX + 10), drops[i] * (FONT_PX + 10)))
 
        drops[i] += 1
        if drops[i] * 10 > PANEL_highly or random.random() > 0.99:
            drops[i] = 0 
 
    pygame.display.flip()


# In[ ]:




