import pygame as pg

pg.init()
scr = pg.display.set_mode((600, 500))
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        scr.fill((255, 255, 255))
        pg.draw.circle(scr, (200, 0, 0), (250, 250), 80)
        pg.display.flip()
pg.quit()