import pygame as pg
pg.init()
scr = pg.display.set_mode((600, 500))
pg.display.set_caption('Pygame Windows')
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
pg.display.flip()