# -*- encoding: utf-8 -*-
# Modules
import pygame, sys

class Director:
    WIDTH = 800
    HEIGHT = 600
    CAPTION = "Source code viewer"
    FPS = 20
    #
    def __init__(self):
        self.screen = pygame.display.set_mode((Director.WIDTH, Director.HEIGHT))
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(Director.CAPTION)

    def loop(self):
        "Main game loop."

        while not self.quit_flag:
            time = self.clock.tick(Director.FPS)

            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

                # Detect events
                self.scene.on_event(event)

            # Update scene
            self.scene.on_update()

            # Draw the screen
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene

    def quit(self):
        self.quit_flag = True

class Scene:
     """Represents a scene of the game.

     Scenes must be created inheriting this class attributes
     in order to be used afterwards as menus, introduction screens,
     etc."""

     def __init__(self, director):
         self.director = director

     def on_update(self):

         raise NotImplementedError("on_update abstract method must be defined in subclass.")

     def on_event(self, event):

         raise NotImplementedError("on_event abstract method must be defined in subclass.")

     def on_draw(self, screen):

         raise NotImplementedError("on_draw abstract method must be defined in subclass.")
