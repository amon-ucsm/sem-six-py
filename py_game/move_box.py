import pygame as pg 

pg.init()
scr = pg.display.set_mode((600, 600))
pg.display.set_caption('Moving object')

x = 200
y = 200
width = 20
height = 20
vel = 1
run = True
while run:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 0:
        x -= vel
    if keys[pg.K_RIGHT] and x < 600 - width:
        x += vel
    if keys[pg.K_UP] and y > 0:
        y -= vel
    if keys[pg.K_DOWN] and y < 600 - height:
        y += vel
        
    scr.fill((0, 0, 0))
    pg.draw.rect(scr, (255, 0, 0), (x, y, width, height))
    pg.display.update()
    
pg.quit()