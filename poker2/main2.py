# -*- coding: utf-8 -*-
# Modules
import pygame
from director import Director
from my_scenes import SceneHome
 
def main():
    pygame.display.init()
    dr = Director()
    scene = SceneHome(dr)
    dr.change_scene(scene)
    dr.loop()
 
if __name__ == '__main__':
    main()