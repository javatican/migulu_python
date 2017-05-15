# -*- coding: utf-8 -*-
# Modules
import pygame
from director import Director
from my_scenes import SceneHome
 
def main():
    pygame.display.init()
    dir = Director()
    scene = SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    main()